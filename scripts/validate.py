#!/usr/bin/env python3
"""Validação estrutural mínima do caderno Math.

Sem dependências externas. A intenção não é provar correção matemática, mas impedir
quebras grosseiras antes de publicar: arquivos ausentes, âncoras quebradas, IDs
duplicados e referências locais inexistentes.
"""
from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
REQUIRED = ["index.html", "favicon.svg", "og-image.svg", ".nojekyll", "README.md"]

class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.srcs: list[str] = []
    def handle_starttag(self, tag: str, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.append(d["id"])
        if "href" in d:
            self.hrefs.append(d["href"])
        if "src" in d:
            self.srcs.append(d["src"])

def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")

def main() -> None:
    for name in REQUIRED:
        if not (ROOT / name).exists():
            fail(f"arquivo obrigatório ausente: {name}")

    html = INDEX.read_text(encoding="utf-8")
    p = Parser(); p.feed(html)

    duplicated = sorted({x for x in p.ids if p.ids.count(x) > 1})
    if duplicated:
        fail(f"IDs duplicados: {duplicated}")

    idset = set(p.ids)
    broken_anchors = [h for h in p.hrefs if h.startswith("#") and h[1:] not in idset]
    if broken_anchors:
        fail(f"âncoras internas quebradas: {broken_anchors}")

    local_refs = []
    for ref in p.hrefs + p.srcs:
        if not ref or ref.startswith("#") or ref.startswith("data:"):
            continue
        parsed = urlparse(ref)
        if parsed.scheme or parsed.netloc:
            continue
        local_refs.append(parsed.path)
    missing = sorted({r for r in local_refs if r and not (ROOT / r).exists()})
    if missing:
        fail(f"referências locais ausentes: {missing}")

    sections = re.findall(r'<section\s+id="([^"]+)"', html)
    expected = [f"c{i}" for i in range(1, 13)] + ["epi"]
    if sections != expected:
        fail(f"ordem de seções inesperada: {sections}")

    canvases = re.findall(r'<canvas\s+id="([^"]+)"', html)
    for cid in ["spiro", "perceptron", "gd", "pca"]:
        if cid not in canvases:
            fail(f"canvas ausente: {cid}")

    print("OK: estrutura validada")
    print(f"sections={len(sections)} canvases={len(canvases)} ids={len(idset)}")

if __name__ == "__main__":
    main()
