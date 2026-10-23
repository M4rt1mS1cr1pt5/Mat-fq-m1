# M1TR4M — plano de trabalho e estado

Documento de trabalho (para retomar o desenvolvimento). O relatório final
fica em `RELATORIO.md`; a lista para a calculadora em
`docs/TESTES_NO_APARELHO.md`.

## Fases (secção 14 do prompt)

- Fase 0 — sonda da calculadora: `src/sonda/m1sonda.py` + `m1sonda2.py`
  (3,4 KB). Feita; falta correr no aparelho.
- Fase 1 — plataforma, núcleo, interface, simulador e testes. Feita.
- Fase 2 — pacotes piloto, três calculadoras, build e orçamentos. Feita.
- Fase 3 — restantes pacotes, calculadoras, exercícios e pesquisa. Feita.
  A Matemática foi depois refeita por anos (7.º ao 10.º), a pedido do aluno,
  sem os Modelos para a cidadania.
- Fase 4 — acabamentos, edições de reserva, prévia, relatório e lista de
  testes no aparelho. Feita no computador; os testes no aparelho estão por
  fazer.

## Módulos

| Módulo | Função | Carregado |
| --- | --- | --- |
| m1 | arranque e erros fatais | sempre |
| m1_plat | ecrã, teclas, tempo, memória, gravação | sempre |
| m1_nucleo | números, expressões, unidades, validação | sempre |
| m1_ui | componentes de ecrã (menu, texto, formulário, gráfico) | sempre |
| m1_app, m1_cont, m1_cat | navegação, leitor de pacotes, catálogo | sempre |
| m1_ini | ecrã inicial; lê as definições e o progresso guardados | só no arranque |
| m1_nav | escolha de disciplina e tema, formulário, exemplos, resumo, menu das calculadoras, histórico, constantes | a pedido |
| m1_calc | catálogo das calculadoras | a pedido (ranhura k) |
| m1_ex | treino, teste, revisão rápida, progresso | a pedido (ranhura f) |
| m1_cfg | definições, ajuda, sobre, diagnóstico | a pedido (ranhura f) |
| m1_pesq + m1_idx, m1_idx2, m1_idxm, m1_idxm2 | pesquisa (código + índice em 4 partes) | a pedido (f + p) |
| m1_tp | tabela periódica (dados + ecrã) | a pedido (p) |
| m1_q | aritmética exata (frações, radicais, polinómios) | com as calculadoras do 3.º ciclo |
| p_* / x_* | lições / exercícios de um tema | a pedido (p) |
| c_* | calculadoras de um grupo | a pedido (c) |

## Ferramentas

- `ferramentas/build.py`: os 10 passos do build (ver o início do ficheiro).
- `ferramentas/conteudo.py`: leitor e validador dos conteúdos (o formato
  está descrito no início).
- `ferramentas/edicoes.py`: edições de reserva num só ficheiro.
- `ferramentas/previa.py`: prévia dos ecrãs a partir das capturas.
- `ferramentas/simulador/`: `correr.py` corre a app com uma sequência de
  teclas (CPython ou MicroPython); `capturas.py` desenha os ecrãs em PNG.
- `ferramentas/teclas/`: 12 percursos de teclas e 2 das edições.
- MicroPython 1.12, porta unix de 32 bits, e Luna 2.1: `ferramentas/prepara.sh`.
