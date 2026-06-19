#!/usr/bin/env python3
"""Validação estrutural mínima do repositório Math.

Sem dependências externas. A intenção não é provar correção matemática,
psicoacústica ou pedagógica, mas impedir quebras grosseiras antes de publicar:
arquivos ausentes, âncoras quebradas, IDs duplicados, referências locais
inexistentes e remoção acidental de estruturas centrais dos cadernos.
"""
from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "index.html",
    "why-machines-learn.html",
    "matematica-introdutoria.html",
    "matematica-fundamental.html",
    "musica-matematica.html",
    "favicon.svg",
    "og-image.svg",
    ".nojekyll",
    "README.md",
]

PAGES = [
    "index.html",
    "why-machines-learn.html",
    "matematica-introdutoria.html",
    "matematica-fundamental.html",
    "musica-matematica.html",
]

WML_SECTIONS = ["p1", "p2", "p3", "p4"] + [f"c{i}" for i in range(1, 13)] + ["epi"]
WML_CANVASES = ["spiro", "perceptron", "gd", "pca"]

MUSIC_SECTIONS = [
    "corda",
    "timbre",
    "consonancia",
    "batimentos",
    "cents",
    "escala",
    "temperamento",
    "tonal",
    "modelo",
    "beethoven",
]

MUSIC_CANVASES = [
    "hero-canvas",
    "corda-canvas",
    "timbre-canvas",
    "cons-canvas",
    "diss-curve",
    "beat-canvas",
    "cents-canvas",
    "circle-canvas",
    "tet-canvas",
    "puretemp-canvas",
    "tonal-canvas",
    "model-canvas",
    "beet-canvas",
]

MUSIC_SENTINELS = [
    "epi math",
    "epi phys",
    "epi hist",
    "epi peda",
    "snd-desc",
    "aria-label",
    "masterLimiter",
    "function stopAll()",
    "Som externo, som interno",
    "caso p&oacute;s-lingual",
    "n&atilde;o um modelo universal",
]


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.srcs: list[str] = []
        self.sections: list[str] = []
        self.canvases: list[str] = []

    def handle_starttag(self, tag: str, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.append(d["id"])
        if "href" in d:
            self.hrefs.append(d["href"])
        if "src" in d:
            self.srcs.append(d["src"])
        if tag == "section" and "id" in d:
            self.sections.append(d["id"])
        if tag == "canvas" and "id" in d:
            self.canvases.append(d["id"])


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


def parse_page(name: str) -> tuple[str, Parser]:
    path = ROOT / name
    if not path.exists():
        fail(f"arquivo obrigatório ausente: {name}")
    html = path.read_text(encoding="utf-8")
    parser = Parser()
    parser.feed(html)
    return html, parser


def validate_common_page(name: str, html: str, parser: Parser) -> None:
    duplicated = sorted({x for x in parser.ids if parser.ids.count(x) > 1})
    if duplicated:
        fail(f"{name}: IDs duplicados: {duplicated}")

    idset = set(parser.ids)
    broken_anchors = [h for h in parser.hrefs if h.startswith("#") and h[1:] not in idset]
    if broken_anchors:
        fail(f"{name}: âncoras internas quebradas: {broken_anchors}")

    local_refs = []
    for ref in parser.hrefs + parser.srcs:
        if not ref or ref.startswith("#") or ref.startswith("data:"):
            continue
        parsed = urlparse(ref)
        if parsed.scheme or parsed.netloc:
            continue
        local_refs.append(parsed.path)

    missing = sorted({r for r in local_refs if r and not (ROOT / r).exists()})
    if missing:
        fail(f"{name}: referências locais ausentes: {missing}")


def require_exact_sections(name: str, parser: Parser, expected: list[str]) -> None:
    if parser.sections != expected:
        fail(f"{name}: ordem de seções inesperada: {parser.sections}")


def require_canvases(name: str, parser: Parser, required: list[str]) -> None:
    missing = [cid for cid in required if cid not in parser.canvases]
    if missing:
        fail(f"{name}: canvas ausente: {missing}")


def require_sentinels(name: str, html: str, sentinels: list[str]) -> None:
    missing = [s for s in sentinels if s not in html]
    if missing:
        fail(f"{name}: marcador essencial ausente: {missing}")


def main() -> None:
    for name in REQUIRED:
        if not (ROOT / name).exists():
            fail(f"arquivo obrigatório ausente: {name}")

    parsed_pages: dict[str, tuple[str, Parser]] = {}
    for name in PAGES:
        html, parser = parse_page(name)
        validate_common_page(name, html, parser)
        parsed_pages[name] = (html, parser)

    wml_html, wml = parsed_pages["why-machines-learn.html"]
    require_exact_sections("why-machines-learn.html", wml, WML_SECTIONS)
    require_canvases("why-machines-learn.html", wml, WML_CANVASES)

    music_html, music = parsed_pages["musica-matematica.html"]
    require_exact_sections("musica-matematica.html", music, MUSIC_SECTIONS)
    require_canvases("musica-matematica.html", music, MUSIC_CANVASES)
    require_sentinels("musica-matematica.html", music_html, MUSIC_SENTINELS)

    print("OK: estrutura validada")
    print(
        " ".join(
            [
                f"pages={len(PAGES)}",
                f"wml_sections={len(wml.sections)}",
                f"wml_canvases={len(wml.canvases)}",
                f"music_sections={len(music.sections)}",
                f"music_canvases={len(music.canvases)}",
            ]
        )
    )


if __name__ == "__main__":
    main()
