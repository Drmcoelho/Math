# Deploy

## GitHub Pages por branch

1. Confirme que `index.html` está na raiz do repositório.
2. No GitHub: `Settings → Pages`.
3. Em `Build and deployment`, selecione `Deploy from a branch`.
4. Branch: `main`.
5. Pasta: `/ root`.

URL esperada:

```text
https://drmcoelho.github.io/Math/
```

## Validação antes do commit

```bash
python3 scripts/validate.py
```

## Servidor local

```bash
python3 -m http.server 8000
```

Abrir:

```text
http://localhost:8000
```
