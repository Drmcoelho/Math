# Math — Why Machines Learn · Caderno Técnico

Caderno técnico interativo, em português, sobre a matemática por trás de aprendizado de máquina moderno. O material reorganiza *Why Machines Learn: The Elegant Math Behind Modern AI* como uma cadeia causal única:

`vetor → produto escalar → erro → gradiente → profundidade → generalização`

O projeto é propositalmente simples: um `index.html` estático, sem build obrigatório, com KaTeX embarcado localmente (`vendor/katex/`, sem dependência de CDN) e três laboratórios interativos em `<canvas>`: perceptron, gradiente descendente e PCA.

## Conteúdo

- `index.html` — portal ilustrado que reúne os quatro cadernos (trilhas máquina e música).
- `why-machines-learn.html` — caderno principal *Why Machines Learn* (perceptron → atenção), com laboratórios em canvas e 850 exercícios.
- `matematica-introdutoria.html` — pré-caderno com a matemática introdutória do livro, do zero e na ordem da cadeia causal (vetor, produto escalar, matriz, variância/PCA, probabilidade, gradiente), com exercícios e solução passo a passo. KaTeX local, offline-first.
- `matematica-fundamental.html` — pré-caderno de matemática do zero (variável, razão, fração, potências, função, logaritmo, seno, somatório, derivada, integral, equação de onda). Offline-first, sem dependências.
- `musica-matematica.html` — caderno dedutivo *A Matemática da Música* (corda vibrante, timbre, consonância, batimentos, cents, escala, temperamento, tonalidade). Offline-first, sem dependências.
- `favicon.svg` — ícone vetorial.
- `og-image.svg` — imagem vetorial para preview social.
- `.nojekyll` — impede o GitHub Pages de passar o site pelo Jekyll.
- `docs/VALIDATION.md` — checklist técnico de integridade.
- `docs/REFERENCES.md` — referências conceituais e bibliográficas.
- `docs/DEPLOY.md` — instruções operacionais de publicação.
- `scripts/validate.py` — checagem local sem dependências externas.
- `vendor/katex/` — KaTeX 0.16.9 embarcado (CSS, JS, auto-render e fontes).

## Publicação no GitHub Pages

Este repositório foi preparado para servir o site pela raiz:

```text
https://drmcoelho.github.io/Math/
```

No GitHub, ative Pages com:

`Settings → Pages → Build and deployment → Deploy from a branch → main / root`

Alternativamente, mantenha o workflow em `.github/workflows/pages.yml` e configure Pages para GitHub Actions.

## Validação local

```bash
python3 scripts/validate.py
python3 -m http.server 8000
```

Abra `http://localhost:8000`.

## Nota de escopo

Este material não reproduz o livro. Ele usa a sequência temática como trilho pedagógico e refaz as derivações e laboratórios de modo independente para fins didáticos.
