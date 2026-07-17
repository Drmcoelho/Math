#!/usr/bin/env python3
"""Gate mecânico da trilha de geometria.

Confirma estrutura, IDs, controles, diagnósticos e sentinelas do motor Canvas.
Não substitui execução em navegador real.
"""
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "geometria-do-possivel.html"
INTRO = ROOT / "geometria-fundamental.html"

SECTIONS = ["espaco", "transformacao", "curvatura", "caos", "fronteira"]
CANVASES = [
    "metricas-canvas",
    "transformacoes-canvas",
    "curvatura-canvas",
    "caos-canvas",
]
CONTROLS = [
    "metric-select", "metric-radius", "rot", "scale", "shear",
    "curve", "chaos-r", "chaos-x", "chaos-reset",
]
STATUSES = ["metric-status", "transform-status", "curve-status", "chaos-status"]
SENTINELS = [
    "getContext('2d')",
    "ResizeObserver",
    "requestAnimationFrame",
    "devicePixelRatio",
    "setTransform",
    "addEventListener('input'",
]


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.sections = []
        self.canvases = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        element_id = data.get("id")
        if element_id:
            self.ids.append(element_id)
        if tag == "section" and element_id:
            self.sections.append(element_id)
        if tag == "canvas" and element_id:
            self.canvases.append(element_id)


def fail(message):
    raise SystemExit(f"FAIL geometry: {message}")


def main():
    for path in (INTRO, PAGE):
        if not path.exists():
            fail(f"arquivo ausente: {path.name}")

    html = PAGE.read_text(encoding="utf-8")
    parser = Parser()
    parser.feed(html)

    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        fail(f"IDs duplicados: {duplicates}")
    if parser.sections != SECTIONS:
        fail(f"ordem de seções inesperada: {parser.sections}")

    for label, required, found in (
        ("canvas", CANVASES, parser.canvases),
        ("controle", CONTROLS, parser.ids),
        ("status", STATUSES, parser.ids),
    ):
        missing = [item for item in required if item not in found]
        if missing:
            fail(f"{label} ausente: {missing}")

    missing_sentinels = [item for item in SENTINELS if item not in html]
    if missing_sentinels:
        fail(f"sentinela JS ausente: {missing_sentinels}")

    if "canvas ativo" not in html or "contexto 2D indisponível" not in html:
        fail("diagnóstico visível de sucesso/erro foi removido")

    print("OK: geometria validada")
    print(f"sections={len(SECTIONS)} canvases={len(CANVASES)} controls={len(CONTROLS)}")


if __name__ == "__main__":
    main()
