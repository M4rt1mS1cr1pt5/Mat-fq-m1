# Registo de alterações

A versão da app está em `src/m1_app.py` (`APPV`). Cada pacote de conteúdos
declara a versão e o número de lições, e o núcleo recusa pacotes de outra
versão.

## 1.0 — 2026-10-23 (primeira versão)

Ainda não foi corrida numa calculadora: ver
[docs/TESTES_NO_APARELHO.md](docs/TESTES_NO_APARELHO.md).

### Conteúdos

- Física e Química A, 10.º ano: 9 temas (Química: q1 a q6; Física: f1 a f3),
  13 atividades laboratoriais (aq, af) e revisões do 7.º, 8.º e 9.º ano (r7,
  r8, r9) ligadas às lições do 10.º ano.
- Matemática do 7.º ao 10.º ano, organizada por anos: Números, Álgebra,
  Geometria e Medida e Dados (ou Probabilidades) em cada ano do 3.º ciclo, e
  7 temas do 10.º ano (Estatística, Geometria sintética, Funções, Função
  quadrática, Ramos e módulo, Geometria analítica e Vetores).
- Total: 33 temas, 155 lições, 270 fórmulas, 99 exemplos resolvidos e 313
  exercícios. Cada número marcado no texto é recalculado pelo build.

### Calculadoras

- 103 calculadoras: 7 comuns, 44 de FQ (11 assistentes das AL) e 52 de
  Matemática. Os resolvedores do 3.º ciclo mostram os passos com frações e
  radicais exatos.

### App

- Pesquisa global com índice pré-calculado, tabela periódica com fichas,
  formulário, constantes com fonte, treino, teste do capítulo, revisão rápida
  com cartões, progresso e definições.
- Duas formas de instalação (um só documento ou PyLib), sonda da calculadora
  e Diagnóstico.
- Edições de reserva num só programa: "M1TR4M FQ" (288 546 bytes) e
  "M1TR4M Mat" (300 293 bytes), comprimidas com um dicionário.

### Durante o desenvolvimento

- 2026-10-22: sonda (Fase 0); plataforma, núcleo, interface e simulador
  (Fase 1); pacotes piloto e build completo (Fase 2); temas de FQ, AL,
  revisões e os temas de Matemática A do 10.º ano (Fase 3).
- 2026-10-23: a Matemática foi refeita por anos, do 7.º ao 10.º ano, a
  pedido do aluno. Saíram os Modelos para a cidadania (eleições, salários,
  IRS e juros) e as revisões curtas do 3.º ciclo, que deram lugar aos temas
  completos do 7.º, 8.º e 9.º ano. A trigonometria passou para o 9.º ano.
- 2026-10-23: edições de reserva, prévia dos ecrãs no build, documentação e
  lista de testes no aparelho.
