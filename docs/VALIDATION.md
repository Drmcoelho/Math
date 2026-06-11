# Validação técnica

Status local desta versão:

- HTML principal presente.
- 13 seções esperadas: `c1` a `c12` + `epi`.
- 4 canvases esperados: `spiro`, `perceptron`, `gd`, `pca`.
- Sem IDs duplicados.
- Sem âncoras internas quebradas.
- Sem referência local ausente.

Comando:

```bash
python3 scripts/validate.py
```

A validação estrutural não substitui revisão matemática. Ela só bloqueia falhas mecânicas antes do deploy.
