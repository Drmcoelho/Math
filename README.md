# Math — Cadernos de matemática interativa

Cadernos técnicos interativos, em português, sobre duas trilhas complementares:

- a matemática por trás de aprendizado de máquina moderno;
- a matemática da música, da corda vibrante à percepção multimodal.

A trilha de IA reorganiza *Why Machines Learn: The Elegant Math Behind Modern AI* como uma cadeia causal única:

`vetor → produto escalar → erro → gradiente → profundidade → generalização`

A trilha musical constrói a teoria da música por uma cadeia dedutiva e perceptiva:

`corda → harmônicos → timbre → consonância → batimentos → cents → temperamento → tonalidade → modelo mental → Beethoven`

O projeto é propositalmente simples: HTML estático, sem build obrigatório. A trilha de IA usa KaTeX embarcado localmente (`vendor/katex/`, sem dependência de CDN). A trilha musical é offline-first, sem dependências externas, com WebAudio API e Canvas 2D.

## Conteúdo

- `index.html` — portal ilustrado que reúne os quatro cadernos (trilhas máquina e música).
- `why-machines-learn.html` — caderno principal *Why Machines Learn* (perceptron → atenção), com laboratórios em canvas e 850 exercícios.
- `matematica-introdutoria.html` — pré-caderno com a matemática introdutória do livro, do zero e na ordem da cadeia causal (vetor, produto escalar, matriz, variância/PCA, probabilidade, gradiente), com exercícios e solução passo a passo. KaTeX local, offline-first.
- `matematica-fundamental.html` — pré-caderno de matemática do zero (variável, razão, fração, potências, função, logaritmo, seno, somatório, derivada, integral, equação de onda). Offline-first, sem dependências.
- `musica-matematica.html` — caderno dedutivo *A Matemática da Música* em 10 níveis: corda vibrante, timbre/Fourier, consonância e roughness, batimentos, cents, escala, temperamento, estrutura tonal, modelo mental e Beethoven como caso pós-lingual específico. Inclui rótulos de estatuto epistêmico, descrições textuais para experiências sonoras, controles ARIA, WebAudio com limiter master, `stopAll()` e visualizações Canvas. Offline-first, sem dependências.
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

Este material não reproduz o livro. Ele usa a sequência temática como trilho pedagógico e refaz as derivações e laboratórios de modo independente para fins didáticos. A trilha musical segue o mesmo princípio: não substitui educação musical formal nem avaliação audiológica; organiza física, matemática, psicoacústica e pedagogia inclusiva em uma sequência dedutiva executável.