# Math v1.0.0 — cadernos de matemática interativa

Quatro cadernos estáticos, em português, offline-first (KaTeX embarcado, sem
dependências externas), com laboratórios e **exercícios com gabarito passo a
passo + múltipla escolha** em todos os módulos.

## Portal

- `index.html` — portal ilustrado que reúne os quatro cadernos, em duas
  trilhas (máquina e música).

## Trilha — A máquina (Why Machines Learn)

- `matematica-introdutoria.html` — pré-caderno: a matemática introdutória do
  livro, do zero (vetor, produto escalar, matriz, variância/PCA, probabilidade,
  gradiente).
- `why-machines-learn.html` — caderno principal: Movimento 0 + 12 capítulos +
  epílogo (perceptron → atenção), com laboratórios em canvas (perceptron,
  gradiente descendente, PCA).

## Trilha — A música (A Matemática da Música)

- `matematica-fundamental.html` — pré-caderno: da balança algébrica à equação de
  onda (razão, logaritmo, seno, derivada, integral…).
- `musica-matematica.html` — caderno principal: corda, timbre, consonância,
  batimentos, cents, escala, temperamento, tonalidade, modelo e Beethoven, com
  WebAudio + canvas.

## Exercícios

Cada módulo segue o mesmo molde: **10 de aquecimento** (pré-requisitos), **20 de
consolidação** (com callbacks a módulos anteriores) e **20 de múltipla escolha**
de dificuldade crescente.

| Caderno | Módulos | Exercícios |
| --- | --- | --- |
| matematica-fundamental.html | 11 | 550 |
| matematica-introdutoria.html | 8 | 400 |
| musica-matematica.html | 10 | 500 |
| why-machines-learn.html | 17 | 850 |
| **Total** | **46** | **2300** |

## Notas técnicas

- KaTeX 0.16.9 embarcado em `vendor/katex/` (sem CDN).
- `.nojekyll` na raiz; publicação por GitHub Actions (`.github/workflows/pages.yml`).
- `scripts/validate.py` verifica estrutura, âncoras, IDs e links locais.

URL: https://drmcoelho.github.io/Math/
