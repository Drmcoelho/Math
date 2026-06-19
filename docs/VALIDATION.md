# Validação técnica

A validação estrutural local é feita por `scripts/validate.py` e não depende de pacotes externos.

Ela não pretende provar correção matemática, psicoacústica ou pedagógica. O objetivo é bloquear regressões mecânicas antes do deploy: arquivo obrigatório ausente, link local quebrado, âncora interna quebrada, ID duplicado, seção fora de ordem ou canvas essencial removido.

## Comando

```bash
python3 scripts/validate.py
```

Saída esperada:

```text
OK: estrutura validada
```

## O que é validado

### Arquivos obrigatórios

- `index.html`
- `why-machines-learn.html`
- `matematica-introdutoria.html`
- `matematica-fundamental.html`
- `musica-matematica.html`
- `favicon.svg`
- `og-image.svg`
- `.nojekyll`
- `README.md`

### Integridade comum das páginas HTML

Para cada página validada, o script verifica:

- IDs duplicados.
- Âncoras internas quebradas (`href="#..."` sem ID correspondente).
- Referências locais ausentes em `href` e `src`.

### Caderno principal de IA

Em `why-machines-learn.html`, o script exige a ordem estrutural:

```text
p1, p2, p3, p4, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, epi
```

Também exige os canvases principais:

```text
spiro, perceptron, gd, pca
```

### Caderno A Matemática da Música

Em `musica-matematica.html`, o script exige a ordem estrutural:

```text
corda, timbre, consonancia, batimentos, cents, escala, temperamento, tonal, modelo, beethoven
```

Também exige os canvases principais:

```text
hero-canvas, corda-canvas, timbre-canvas, cons-canvas, diss-curve, beat-canvas, cents-canvas, circle-canvas, tet-canvas, puretemp-canvas, tonal-canvas, model-canvas, beet-canvas
```

E bloqueia a remoção acidental de marcadores pedagógicos essenciais:

- rótulos de estatuto epistêmico (`epi math`, `epi phys`, `epi hist`, `epi peda`);
- descrições textuais para botões sonoros (`snd-desc`);
- controles de acessibilidade (`aria-label`);
- motor de áudio com limiter master;
- `stopAll()`;
- seção de modelo mental;
- Beethoven como caso específico pós-lingual, não modelo universal.

## Limite explícito

A validação estrutural não substitui revisão matemática, revisão historiográfica, teste auditivo real, auditoria de acessibilidade completa ou execução em múltiplos navegadores. Ela é um gate mecânico mínimo antes da publicação.