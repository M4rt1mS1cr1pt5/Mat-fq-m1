# M1TR4M — Relatório final

Versão 1.0 · build de 2026-10-23 · by M1TR4M

> Tudo o que este relatório descreve correu **só no computador**: simulador
> do ecrã, CPython 3.13 e MicroPython 1.12 (porta unix de 32 bits). **Nada
> foi testado na calculadora.** O que falta confirmar no aparelho está na
> Parte A e na lista [docs/TESTES_NO_APARELHO.md](docs/TESTES_NO_APARELHO.md).

Os números deste relatório vêm de `dist/build.json` (build completo, sem
`--rapido`).

---

## Parte A — Compatibilidade e limitações

### A.1 O que falta em relação ao prompt

1. **Testes no aparelho: nenhum foi feito.** Sonda, tempos (arranque, menus,
   pacotes, pesquisa), memória real, nomes das teclas, símbolos da fonte, as
   duas formas de instalação e as edições de reserva estão por confirmar
   (lista com 88 pontos em `docs/TESTES_NO_APARELHO.md`).
2. **Matemática diferente da secção 8 do prompt, por pedido do aluno.** O
   aluno pediu para ignorar a cidadania e refazer a Matemática do 7.º ao
   10.º ano. Por isso:
   - não existe o tema "Modelos matemáticos para a cidadania" (eleições,
     Hondt, Sainte-Laguë, salários, IRS, juros, Condorcet, prestações) nem
     as calculadoras dele da secção 10.4 (Borda, Hondt e Sainte-Laguë, juros
     e salário, IRS);
   - as "Revisões do 3.º ciclo" deram lugar a 12 temas completos (4 por ano
     do 7.º ao 9.º), com 48 lições, 36 exemplos e 102 exercícios;
   - a trigonometria do triângulo retângulo está no 9.º ano (tema g9); os
     radianos e as leis dos senos e dos cossenos ficam como extensão;
   - o menu diz "Matemática" e o ecrã inicial "Física e Química A 10.º ·
     Matemática 7.º-10.º", em vez de "Matemática A — 10.º ano".
3. **Ponto de partida.** As fontes do M1TR4M_(Mat) v1.0 (36 lições, 16
   calculadoras) e do m1tr4m (tabela periódica) não foram fornecidas: tudo foi
   escrito de novo. A medição da secção 3 (cerca de 600 KB de heap para 315
   KB de código) não foi repetida com essa app.
4. **Atividades laboratoriais.** Há 11 assistentes próprios. A AL 2.3
   (diluição) usa a calculadora geral de diluição, que dá o volume e o fator
   de diluição mas não a incerteza. A AL 2.4 (reação fotoquímica) é
   qualitativa e liga à calculadora de fotões.
5. **Documentos oficiais não consultados.** O ambiente do build não tinha
   acesso a dge.mec.pt (Aprendizagens Essenciais) nem às tabelas do IAVE. A
   distribuição dos conteúdos pelos anos segue as Aprendizagens Essenciais de
   Matemática de 2021 tal como as conheço. Deve ser revista por um professor.
   As constantes do exame 715 estão marcadas "2024 (confirmar)" em
   `dados/constantes.csv`.
6. **Edições de reserva com menos conteúdo.** "M1TR4M FQ" tem os 9 temas do
   10.º ano, sem AL nem revisões; "M1TR4M Mat" tem o 7.º, o 8.º e o 9.º ano,
   sem o 10.º. Nenhuma tem pesquisa. O limite de 300 KB foi lido como 300 ×
   1024 = 307 200 bytes, como todos os orçamentos do build; a edição Mat tem
   300 293 bytes (293 bytes acima de 300 000).

### A.2 Aparelho e Python assumidos

- TI-Nspire CX II-T com o sistema operativo 5.2 ou posterior (segundo a TI, o
  Python vem com o sistema a partir dessa versão).
- Python da TI, baseado no MicroPython. Referência usada em todas as
  medições: MicroPython 1.12, porta unix de 32 bits, e mpy-cross 1.12.
- Módulos usados: `math`, `time`, `ti_system` e `ti_draw`; `gc` e `sys` só
  dentro de `try/except`. O build recusa f-strings, `:=`, anotações de tipos,
  `eval`, `exec`, comentários não ASCII, métodos de `str` que o MicroPython
  1.12 não tem e imports fora desta lista.
- Ecrã: a app lê `get_screen_dim()`. O simulador assume 318 × 212 px, 7 px
  por carácter e 17 px por linha (valores das apps anteriores); a app tem uma
  régua de calibração nas Definições.

### A.3 Memória medida (no computador, MicroPython 1.12 de 32 bits)

| Medição | Valor |
| --- | --- |
| Memória ocupada depois de importar o núcleo | 60 768 bytes (m1_nucleo 17 952, m1_ui 12 000, m1_app 11 744, m1_plat 9 472, m1_cat 6 272, m1_cont 3 328) |
| Código residente (fonte) | 90 859 bytes (orçamento: 117 760); m1_app + m1_cont + m1_cat: 27 103 (orçamento: 30 720) |
| Heap mínimo para importar um módulo a pedido, com o núcleo carregado (bisseção de 1 KB) | 106 KB a 156 KB; 106 KB a 185 KB se o texto inteiro do módulo ficar na memória |
| Módulos mais exigentes | índice da pesquisa m1_idx e m1_idxm (156 / 185 KB); pacote p_m2 (151 / 176 KB); c_mprb (151 / 172 KB) |
| 12 percursos de teclas com heap de 512 KB | todos chegam ao fim; pico de memória viva (medido a cada ecrã) de 96 768 bytes (definições) a 198 064 bytes (pesquisa) |
| Edições de reserva (percurso de teclas de cada uma) | heap mínimo de 876 KB (FQ) e 1 176 KB (Mat); depois de compiladas, o pico de memória viva foi de 422 736 e 424 304 bytes |

O heap real da calculadora não é conhecido. O Diagnóstico mostra a memória
livre no arranque e no momento.

### A.4 O que só o aparelho pode confirmar

- O tamanho do ecrã, a largura dos carateres e a altura das linhas.
- Os nomes das teclas (a sonda e o Diagnóstico têm um teste de teclas).
- Os símbolos que a fonte desenha (√ Δ π ≈ → ∈ ≤ ² ³ e outros). Se
  `draw_text` falhar, a app passa sozinha para letras simples.
- Se um programa consegue importar outro do mesmo problema (forma "um só
  documento") ou só da PyLib.
- Se `store_list` e `recall_list` guardam as definições e o progresso, e se
  `time` dá a data.
- A memória livre real e se as edições de reserva cabem (precisaram de 876 KB
  e 1 176 KB de heap no computador).
- Os tempos dos critérios de aceitação: arranque até 3 s, mudança de menu até
  1 s, abertura de um pacote até 2 s e cada tecla da pesquisa abaixo de 0,3 s.
- Se os `.tns` criados pelo Luna abrem e correm.

### A.5 Limitações conhecidas

- Só números reais: não há números complexos.
- Configuração eletrónica de Z = 1 a 36. Raio atómico e energia de ionização
  só de Z = 1 a 54 (para Z > 54 a ficha diz "sem dados nesta app").
- Lewis, geometria e polaridade: só as moléculas da tabela verificada.
- Acerto de equações químicas: até 8 espécies e coeficientes até 1000.
- A pesquisa procura o texto escrito, sem acentos nem maiúsculas, e tem
  sinónimos, mas não corrige erros de escrita.
- Exercícios "numérico com unidade": só 4 (em q1, q5, f1 e f2).
- As limitações também aparecem no ecrã "Sobre a M1TR4M"; cada edição de
  reserva mostra só as que lhe dizem respeito.

---

## Parte B — Código

### B.1 Ficheiros

Código-fonte em `src/` (ASCII; os acentos das strings estão como `\uXXXX`):
44 ficheiros, 532 027 bytes.

| Ficheiro | Bytes | Função |
| --- | --- | --- |
| `m1.py` | 1 213 | Arranque: mede a memória, importa o núcleo e apanha os erros fatais |
| `m1_plat.py` | 11 920 | Plataforma: ecrã, teclas, tempo, memória, gravação e símbolos de recurso |
| `m1_nucleo.py` | 28 371 | Núcleo de cálculo: números, leitor de expressões, unidades, alg. significativos, validação |
| `m1_ui.py` | 22 252 | Componentes de ecrã: menu, texto paginado, lição, formulário, gráfico, perguntas |
| `m1_app.py` | 15 441 | Navegação, definições, catálogo e motor das calculadoras |
| `m1_cont.py` | 5 748 | Leitor de pacotes (versão e número de registos conferidos) |
| `m1_ini.py` | 3 463 | Ecrã inicial; lê as definições e o progresso guardados |
| `m1_nav.py` | 5 647 | Escolha de tema, formulário, exemplos, resumo, menu das calculadoras, histórico |
| `m1_ex.py` | 11 916 | Treino, teste do capítulo, revisão rápida e "O meu progresso" |
| `m1_cfg.py` | 10 371 | Definições, ajuda, sobre e Diagnóstico |
| `m1_pesq.py` | 5 418 | Pesquisa global |
| `m1_tp.py` | 14 779 | Tabela periódica (dados e ecrã) |
| `m1_q.py` | 18 065 | Aritmética exata: frações, radicais, polinómios, leitura de expressões em árvore |
| `calc/c_comu.py` | 8 331 | Comuns: científica, algarismos significativos, conversor de unidades, prefixos |
| `calc/c_comd.py` | 10 048 | Comuns: constantes, dados experimentais com incerteza, regressão linear e gráfico |
| `calc/c_fqat.py` | 11 951 | Química: massa molar, quantidade de matéria, Ar médio, frações molar e mássica |
| `calc/c_fqel.py` | 9 546 | Química: espetros e fotões, átomo de hidrogénio, configuração eletrónica |
| `calc/c_fqlg.py` | 12 630 | Química: Lewis e geometria (tabela), entalpia de reação, acerto de equações |
| `calc/c_fqso.py` | 8 527 | Química: concentrações, massa a pesar, percentagens e ppm, diluição, gases |
| `calc/c_fqen.py` | 14 866 | Física: energias, conservação, trabalho, teorema da energia cinética, potência, rendimento |
| `calc/c_fqci.py` | 12 270 | Física: lei de Ohm, resistividade, associações, gerador, potência, energia e custo |
| `calc/c_fqte.py` | 14 625 | Física: Q = m c ΔT, mudança de estado, equilíbrio térmico, condução, 1.ª Lei, painel |
| `calc/c_alq1.py` | 6 244 | Assistentes das AL de Química 1.1, 1.2 e 1.3 |
| `calc/c_alq2.py` | 5 011 | Assistentes das AL de Química 2.1 e 2.2 |
| `calc/c_alf1.py` | 6 737 | Assistentes das AL de Física 1.1, 1.2 e 2.1 |
| `calc/c_alf2.py` | 7 353 | Assistentes das AL de Física 3.1, 3.2 e 3.3 |
| `calc/c_mnum.py` | 16 675 | 7.º e 8.º: frações e racionais, potências, m.d.c. e m.m.c., dízimas |
| `calc/c_mrea.py` | 15 024 | 8.º e 9.º: notação científica, raízes e radicais, intervalos |
| `calc/c_mexp.py` | 17 381 | Equação do 1.º grau, inequação do 1.º grau, sistemas 2 × 2 |
| `calc/c_mpol.py` | 15 047 | Polinómios: desenvolver, fatorizar, Ruffini |
| `calc/c_mprp.py` | 14 312 | Sequências, proporcionalidade direta e inversa, percentagens |
| `calc/c_mgeo.py` | 20 899 | Ângulos, triângulos, polígonos e paralelas (desenho); áreas e perímetros |
| `calc/c_msol.py` | 10 834 | Sólidos: áreas e volumes, com a medida em falta |
| `calc/c_mgtr.py` | 15 696 | Isometrias com desenho; ângulos na circunferência |
| `calc/c_mprb.py` | 21 297 | Frequências e gráfico de barras; Laplace; dois dados ou moedas; árvores |
| `calc/c_matt.py` | 14 847 | Pontos notáveis (desenho), inscrita e circunscrita, Euler, nove pontos, Pitágoras, semelhança |
| `calc/c_matr.py` | 12 698 | Trigonometria: triângulo retângulo, radianos e valores exatos, leis dos senos e cossenos |
| `calc/c_mate.py` | 14 530 | Estatística: uma variável, classes e histograma, caule-e-folhas |
| `calc/c_matf.py` | 16 925 | Funções: função escrita pelo aluno, afim, por ramos, módulo |
| `calc/c_matq.py` | 14 376 | Quadrática: equação e estudo, inequações do 2.º grau, transformações |
| `calc/c_matg.py` | 16 678 | Geometria analítica: distância, reta, mediatriz e plano mediador, circunferência, condições |
| `calc/c_matv.py` | 8 685 | Vetores: operações, equação vetorial da reta, baricentro |
| `sonda/m1sonda.py` | 3 226 | Sonda da calculadora (Fase 0) |
| `sonda/m1sonda2.py` | 154 | Auxiliar da sonda (testa o import entre programas) |

Gerados pelo build em `dist/py` (114 módulos, todos ASCII):

| Módulos | Quantos | Bytes | Função |
| --- | --- | --- | --- |
| `p_*` (lições, fórmulas e exemplos de um tema) | 33 | 459 350 | carregados a pedido |
| `x_*` (exercícios de um tema) | 33 | 80 218 | carregados a pedido |
| `m1_idx`, `m1_idx2`, `m1_idxm`, `m1_idxm2` | 4 | 60 911 | índice da pesquisa (FQ e Mat) |
| `m1_cat` | 1 | 5 914 | catálogo de temas, constantes, versão e limitações |
| `m1_calc` | 1 | 5 729 | catálogo das 103 calculadoras |

Edições de reserva (`dist/edicoes`): `M1TR4M_FQ.py` (288 546 bytes) e
`M1TR4M_Mat.py` (300 293 bytes). Para a calculadora (`dist/tns`):
`M1TR4M.tns` (114 módulos, 394 591 bytes), 113 ficheiros para a PyLib,
`M1TR4M_arranque.tns`, `M1TR4M_sonda.tns` e as duas edições.

Ferramentas do computador (16 ficheiros, 110 846 bytes):

| Ficheiro | Função |
| --- | --- |
| `ferramentas/build.py` | Os 10 passos do build; para no primeiro erro |
| `ferramentas/conteudo.py` | Leitor e validador dos conteúdos; gera pacotes, catálogo e índice |
| `ferramentas/verifica.py` | Verificação do código (passo 5) |
| `ferramentas/memoria.py` | Medição de memória por bisseção (passo 7) |
| `ferramentas/edicoes.py` | Edições de reserva num só ficheiro, com compressão por dicionário |
| `ferramentas/tns.py` | Empacotamento com o Luna e conferência byte a byte |
| `ferramentas/previa.py` | Prévia dos ecrãs principais (`dist/previa.png`) |
| `ferramentas/dados.py` | Gera os dados da tabela periódica e das constantes a partir dos CSV |
| `ferramentas/simulador/` | `ti_draw` e `ti_system` falsos, corredor de percursos de teclas, capturas em PNG |
| `ferramentas/teclas/` | 12 percursos de teclas da app e 2 das edições |
| `ferramentas/prepara.sh` | Compila o MicroPython 1.12 (32 bits), o mpy-cross e o Luna |

Testes (`testes/`): 14 ficheiros de testes, 338 testes.

### B.2 Como os módulos se ligam

```
m1 ──> m1_app ──> m1_plat, m1_nucleo, m1_ui, m1_cont, m1_cat   (residentes)
          │
          ├─ ranhura f (um de cada vez): m1_ini · m1_ex · m1_cfg · m1_pesq · m1_nav
          ├─ ranhura p: p_<tema> · x_<tema> · m1_tp · m1_idx…   (pacotes)
          ├─ ranhura c: c_<grupo> (calculadoras; as do 3.º ciclo importam m1_q)
          └─ ranhura k: m1_calc (catálogo das calculadoras)
```

- `m1_cont.get(ranhura, nome)` importa com `__import__`, confere a versão e
  o número de registos do pacote e liberta o módulo anterior da mesma
  ranhura (apaga-o de `sys.modules` e corre `gc.collect()`).
- Cada calculadora é uma função `nome()` que devolve `(título, campos,
  função)`; a função recebe os valores e devolve `(texto, passos, valor,
  unidade[, gráfico])`. O motor (`m1_app`) faz o formulário, a validação e o
  ecrã de resultado.
- Os pacotes guardam o texto num só `D = "..."` com marcadores (`@L`, `@A`…
  `@J`, `@F`, `@E`, `@X`); o leitor procura com `str.find` e só parte em
  linhas a página que mostra.

---

## Parte C — Conteúdos

### C.1 Por tema

Exemplos por nível (básico / intermédio / avançado); exercícios por tipo
(escolha múltipla / numérico / numérico com unidade / verdadeiro ou falso).

| Grupo | Tema | Título | Lições | Fórmulas | Exemplos | Exercícios | Tipos | Calc. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FQ · Química | q1 | Massa e tamanho dos átomos | 5 | 13 | 1 / 1 / 1 | 10 | 3 / 4 / 1 / 2 | 7 |
| FQ · Química | q2 | Energia dos eletrões nos átomos | 5 | 9 | 1 / 1 / 1 | 10 | 4 / 4 / 0 / 2 | 5 |
| FQ · Química | q3 | Tabela Periódica | 3 | 5 | 1 / 1 / 1 | 9 | 5 / 2 / 0 / 2 | 3 |
| FQ · Química | q4 | Ligação química | 6 | 7 | 1 / 1 / 1 | 10 | 6 / 2 / 0 / 2 | 4 |
| FQ · Química | q5 | Gases e dispersões | 5 | 9 | 1 / 1 / 1 | 10 | 4 / 4 / 1 / 1 | 7 |
| FQ · Química | q6 | Transformações químicas | 3 | 6 | 1 / 1 / 1 | 9 | 5 / 2 / 0 / 2 | 3 |
| FQ · Física | f1 | Energia e movimentos | 5 | 10 | 1 / 1 / 1 | 10 | 2 / 6 / 1 / 1 | 7 |
| FQ · Física | f2 | Energia e fenómenos elétricos | 5 | 11 | 1 / 1 / 1 | 10 | 2 / 6 / 1 / 1 | 6 |
| FQ · Física | f3 | Energia, fenómenos térmicos e radiação | 6 | 11 | 1 / 1 / 1 | 10 | 2 / 7 / 0 / 1 | 8 |
| FQ · AL | aq | Atividades laboratoriais de Química | 7 | 9 | 1 / 1 / 1 | 14 | 5 / 6 / 0 / 3 | 7 |
| FQ · AL | af | Atividades laboratoriais de Física | 6 | 8 | 1 / 1 / 1 | 12 | 3 / 6 / 0 / 3 | 8 |
| FQ · Revisões | r7 | Revisões do 7.º ano | 3 | 5 | 1 / 1 / 1 | 8 | 4 / 3 / 0 / 1 | 2 |
| FQ · Revisões | r8 | Revisões do 8.º ano | 5 | 7 | 1 / 1 / 1 | 8 | 4 / 3 / 0 / 1 | 3 |
| FQ · Revisões | r9 | Revisões do 9.º ano | 4 | 8 | 1 / 1 / 1 | 8 | 1 / 5 / 0 / 2 | 4 |
| Mat · 7.º | n7 | Números | 5 | 9 | 1 / 1 / 1 | 9 | 2 / 6 / 0 / 1 | 4 |
| Mat · 7.º | a7 | Álgebra | 5 | 6 | 1 / 1 / 1 | 9 | 2 / 6 / 0 / 1 | 5 |
| Mat · 7.º | g7 | Geometria e Medida | 5 | 9 | 1 / 1 / 1 | 9 | 2 / 6 / 0 / 1 | 3 |
| Mat · 7.º | d7 | Dados | 3 | 5 | 1 / 1 / 1 | 8 | 1 / 6 / 0 / 1 | 3 |
| Mat · 8.º | n8 | Números | 3 | 5 | 1 / 1 / 1 | 8 | 3 / 4 / 0 / 1 | 4 |
| Mat · 8.º | a8 | Álgebra | 5 | 7 | 1 / 1 / 1 | 9 | 3 / 5 / 0 / 1 | 6 |
| Mat · 8.º | g8 | Geometria e Medida | 4 | 6 | 1 / 1 / 1 | 8 | 3 / 4 / 0 / 1 | 4 |
| Mat · 8.º | d8 | Dados | 2 | 2 | 1 / 1 / 1 | 8 | 2 / 5 / 0 / 1 | 3 |
| Mat · 9.º | n9 | Números | 3 | 3 | 1 / 1 / 1 | 8 | 5 / 2 / 0 / 1 | 3 |
| Mat · 9.º | a9 | Álgebra | 4 | 4 | 1 / 1 / 1 | 8 | 2 / 5 / 0 / 1 | 5 |
| Mat · 9.º | g9 | Geometria e Medida | 6 | 9 | 1 / 1 / 1 | 10 | 3 / 7 / 0 / 0 | 5 |
| Mat · 9.º | d9 | Probabilidades | 3 | 4 | 1 / 1 / 1 | 8 | 1 / 6 / 0 / 1 | 3 |
| Mat · 10.º | m2 | Estatística | 9 | 18 | 1 / 1 / 1 | 13 | 2 / 9 / 0 / 2 | 4 |
| Mat · 10.º | m3 | Geometria sintética no plano | 6 | 13 | 1 / 1 / 1 | 11 | 2 / 7 / 0 / 2 | 5 |
| Mat · 10.º | m4 | Funções: generalidades, função afim e condições | 4 | 9 | 1 / 1 / 1 | 10 | 2 / 6 / 0 / 2 | 3 |
| Mat · 10.º | m5 | Função quadrática | 4 | 11 | 1 / 1 / 1 | 10 | 4 / 4 / 0 / 2 | 4 |
| Mat · 10.º | m6 | Funções definidas por ramos e função módulo | 3 | 6 | 1 / 1 / 1 | 8 | 2 / 5 / 0 / 1 | 3 |
| Mat · 10.º | m7 | Geometria analítica no plano e no espaço | 6 | 12 | 1 / 1 / 1 | 10 | 3 / 5 / 0 / 2 | 5 |
| Mat · 10.º | m8 | Vetores no plano e no espaço | 7 | 14 | 1 / 1 / 1 | 11 | 2 / 7 / 0 / 2 | 3 |
| **Total** | **33** | | **155** | **270** | **33 / 33 / 33** | **313** | **96 / 165 / 4 / 48** | |

- 103 calculadoras: 7 comuns, 44 de FQ (11 assistentes das AL) e 52 de
  Matemática ("Calc." na tabela conta as calculadoras ligadas a cada tema;
  uma calculadora pode servir vários temas).
- Nível das lições: 136 de núcleo, 13 de revisão, 4 de aprofundamento e 2 de
  extensão.
- Mínimos da secção 11: todos os temas têm 3 exemplos (um de cada nível) e
  pelo menos 8 exercícios; os temas das AL têm 2 exercícios por atividade.
- Cada número marcado no texto (`[[...]]`) é recalculado pelo build a partir
  de um bloco de verificação no ficheiro-fonte; o build também confirma que a
  resposta certa de cada exercício é aceite pelo corretor.

### C.2 Adaptações ao currículo

- **FQ A, 10.º ano:** os 6 subdomínios de Química e os 3 de Física do
  programa, as 13 AL e as revisões do 7.º ao 9.º ano (lições curtas ligadas às
  lições do 10.º que delas precisam). As leis de Stefan-Boltzmann e de Wien
  estão numa lição marcada como extensão.
- **Matemática 7.º-9.º:** um tema por domínio e por ano (Números, Álgebra,
  Geometria e Medida, Dados ou Probabilidades), em formato de ficha (objetivos,
  conceitos, fórmulas, exemplo resolvido, exercício com resposta).
- **Matemática A, 10.º ano:** Estatística, Geometria sintética, Funções
  (generalidades, afim, condições), Função quadrática, Ramos e módulo,
  Geometria analítica e Vetores. Ficam como aprofundamento Fermat e Nagel,
  parte inteira, chão, teto, sinal e Heaviside; o produto escalar, os
  radianos e as leis dos senos e dos cossenos ficam como extensão.
- Ligações FQ ↔ Matemática: notação científica, proporções e conversões,
  função afim e regressão nas AL, função quadrática e energia cinética,
  vetores e forças.

### C.3 Fontes

- Aprendizagens Essenciais (DGE): FQ A, Físico-Química do 7.º ao 9.º ano,
  Matemática do 7.º ao 9.º ano (2021) e Matemática A do 10.º ano; Programa de
  FQ A (DGE). Usadas como as conheço: não foi possível descarregá-las (ver
  A.1, ponto 5).
- Constantes: tabela de constantes do exame de FQ A (IAVE, 715), CODATA 2018
  e valores convencionais; cada valor tem a fonte em `dados/constantes.csv`.
- Tabela periódica: Ar da IUPAC (abreviados), raio calculado (Clementi e
  outros, 1967) e energia de ionização do NIST, em `dados/elementos.csv`.
- TI-Nspire Python Programming Guidebook (Texas Instruments): módulos,
  PyLib e "Install as Python Module".

---

## Parte D — Funcionalidades

- **Ecrã inicial:** animação de até 2 s com o átomo, "M1TR4M" em letras
  grandes e a legenda; qualquer tecla salta.
- **Menu principal** com 13 opções: Física e Química A, Matemática,
  Pesquisa global, Calculadoras, Tabela periódica, Formulário, Constantes e
  unidades, Exemplos resolvidos, Exercícios e testes, O meu progresso,
  Revisão rápida, Definições/ajuda/Diagnóstico e Sair.
- **FQ** por grupos (Química, Física, AL, Revisões); **Matemática** por anos
  (7.º, 8.º, 9.º, 10.º).
- **Menu de cada tema:** Lições, Formulário do tema, Exemplos, Exercícios,
  Teste do capítulo, Calculadoras do tema e Resumo.
- **Lições** com páginas A a J (O que vais aprender, Intuição, Definição
  formal, Explicação detalhada, Fórmulas, Exemplo resolvido, Interpretação,
  Erros frequentes, Resumo, Exercício de verificação) e a resposta; as fichas
  do 7.º ao 9.º usam as páginas A, C, E, F e J. A app lembra a página onde o
  aluno ficou.
- **Calculadoras:** formulário com rótulo, unidade, valor por defeito e o
  erro escrito por baixo; resultado com fórmula, substituição e resultado
  (= ou ≈, com unidades); opções 1 passos, 2 alterar, 3 novo, 4 usar noutra
  calculadora e 5 gráfico; histórico dos últimos 5 resultados e `ans`.
  Lembram os últimos valores.
- **Gráficos e desenhos** com eixos, escala, legenda, setas para mover e +/−
  para a escala: funções, parábolas, regiões, pontos notáveis, isometrias,
  paralelas, árvores e tabelas de dupla entrada.
- **Pesquisa global:** resultados a cada tecla, sem acentos nem maiúsculas,
  por esta ordem: título igual, título que começa pela pesquisa, palavra do
  título, palavras-chave. Etiquetas L, C, F, E, X, T e K; filtro tudo/FQ/Mat
  com tab; até 60 resultados; sinónimos; o índice só está na memória durante a
  pesquisa. Se uma tecla demorar mais de 0,3 s, a pesquisa passa a começar
  com 2 letras.
- **Tabela periódica:** grelha de 18 colunas com cursor, pesquisa por nome,
  símbolo ou Z, filtros por grupo, período e bloco, e ficha de cada elemento
  com fonte.
- **Exercícios:** escolha múltipla (opções baralhadas), numérico (tolerância
  das Definições ou arredondamento pedido), numérico com unidade e verdadeiro
  ou falso; aceita 0,5, 1/2, 5e-1 e 5 × 10^-1; pista, correção e resolução.
- **Teste do capítulo:** perguntas baralhadas (semente de `get_time_ms`),
  "x de n certas", lista para rever e a frase "O resultado diz respeito só a
  estas perguntas."
- **Revisão rápida:** resumos (páginas I) e cartões pergunta-resposta com três
  caixas de repetição.
- **O meu progresso:** por tema, lições vistas, exercícios feitos e certos,
  último teste; "Temas a rever" (metade ou mais dos exercícios errados);
  "Continuar onde fiquei"; datas só se `time` der uma data credível; apagar
  com confirmação.
- **Definições** (10): casas decimais, algarismos significativos automáticos,
  notação científica, unidade angular, valor de g, tolerância, acentos e
  símbolos, calibração do texto, apagar o progresso, repor as predefinições.
- **Ajuda** (5 tópicos), **Sobre** (versão, build, fontes, limitações) e
  **Diagnóstico** (resumo do aparelho, teste de teclas, teste de gravação,
  régua de calibração).
- **Robustez:** nenhuma entrada faz a app falhar; ValueError,
  ZeroDivisionError, OverflowError, IndexError e MemoryError têm mensagens
  próprias; o ciclo principal apanha o resto e volta ao menu sem perder as
  definições.

---

## Parte E — Instalar e correr

1. Instalar o **TI-Nspire CX II Connect** no computador e ligar a
   calculadora por USB. O Python precisa do sistema operativo 5.2 ou posterior.
2. **Sonda:** copiar `dist/tns/M1TR4M_sonda.tns`, abrir, ir à página do
   `m1sonda.py` e correr (ctrl+R). Fotografar o ecrã; carregar em teclas para
   ver os nomes; esc duas vezes para sair.
3. **Um só documento (forma preferida):** copiar `dist/tns/M1TR4M.tns`,
   abrir e correr o `m1.py`.
4. **PyLib (se a forma 3 falhar):** copiar os 113 ficheiros de
   `dist/tns/PyLib` para a pasta PyLib da calculadora; abrir
   `dist/tns/M1TR4M_arranque.tns` e correr o `m1.py`. O Diagnóstico mostra
   qual forma funcionou ("Importação: documento" ou "PyLib").
5. **Edições de reserva (se nenhuma das anteriores arrancar):**
   `M1TR4M_FQ.tns` ou `M1TR4M_Mat.tns`, cada uma num só programa.
6. **Gravar:** as definições e o progresso ficam em variáveis do documento;
   para ficarem guardados de vez, gravar o documento com **ctrl+S** antes de o
   fechar.
7. **Sair:** menu principal ▸ 13 (Sair) ou esc no menu principal, e
   confirmar.

---

## Parte F — Testes

### F.1 O que foi executado

| Camada | Resultado |
| --- | --- |
| Unitários | 338 testes, 0 falhas no CPython 3.13 e 338 testes, 0 falhas no MicroPython 1.12 de 32 bits (heap de 2 MB); inclui 400 equações do 2.º grau ao acaso e conversões de unidades de ida e volta |
| Conteúdos | 33 temas, 155 lições, 270 fórmulas, 99 exemplos e 313 exercícios validados; 0 erros e 0 avisos; todas as marcas `[[...]]` recalculadas conferem |
| Código | 114 módulos: ASCII, sem construções proibidas, imports permitidos, compilam no mpy-cross 1.12 |
| Memória | pico de importação de cada módulo por bisseção (ver A.3); 12 percursos de teclas acabam com heap de 512 KB |
| Ecrã | 12 percursos de teclas no simulador: 700 ecrãs, 8 361 textos, 519 teclas, 0 textos fora do ecrã, 0 teclas a sobrar; capturas em `dist/capturas` (14 ficheiros, com as 2 das edições) |
| Modo texto | os mesmos percursos sem `ti_draw`: resultados iguais nos dois Pythons |
| Edições de reserva | percursos e01_fq e e02_mat nos dois Pythons com heap de 1,5 MB; compressão reversível; cada pacote descomprimido pela própria edição confere |
| Empacotamento | `M1TR4M.tns` (114 módulos), 113 `.tns` da PyLib, arranque, sonda e 2 edições: cada `.py` lá dentro é igual ao original, byte a byte |
| Prévia | `dist/previa.png` com 12 ecrãs tirados das capturas |
| Tempo | build completo em 152 s |

Além do build: os 33 caminhos de teclas até às lições e os 29 até às
calculadoras da lista de testes no aparelho foram corridos no simulador; os
resultados esperados foram calculados pela própria app com os mesmos
valores (3 deles também tecla a tecla, com mudança de unidade e de opção).

### F.2 O que foi só revisto, sem executar

- Os `.tns` foram lidos de volta e conferidos, mas não foram abertos no
  software da TI nem numa calculadora.
- A forma PyLib e o "Install as Python Module" seguem o guia da TI; não
  foram experimentados.
- As métricas da fonte (7 px por carácter, 17 px por linha) e os nomes das
  teclas são os das apps anteriores, não medidos.
- A distribuição dos conteúdos pelos anos foi revista com o conhecimento das
  Aprendizagens Essenciais, sem os documentos da DGE.

### F.3 O que falta testar no aparelho

Tudo o que está em `docs/TESTES_NO_APARELHO.md`: a sonda, as duas formas de
instalação e as edições, os 4 tempos dos critérios de aceitação, uma lição de
cada um dos 33 pacotes, uma calculadora de cada um dos 29 grupos (com o
resultado esperado), a pesquisa, a gravação das definições e do progresso, e
a memória livre depois de 10 minutos de uso.

### F.4 Erros encontrados e corrigidos

Nesta fase (acabamentos):

- Desenho das paralelas: o eixo dos xx aparecia como uma terceira reta, porque
  a janela incluía y = 0. A figura passou para y = 10 a 14; há um teste novo.
- Notação científica: o resultado não tinha a marca de resultado quando só se
  pedia para escrever A.
- Ajuda das unidades: dizia ◂▸, mas é preciso ▾ antes (encontrado ao correr a
  lista de testes no simulador).
- Leitor de pacotes: conferia a versão mas não o número de lições ou
  exercícios; agora confere os dois.
- O teste `t_pot_invalido` estava definido duas vezes e o primeiro nunca
  corria; o build passa a recusar nomes de testes repetidos.
- Capturas de percursos apagados ficavam em `dist/capturas`; o build limpa a
  pasta.
- A edição Mat tinha as limitações de FQ no ecrã "Sobre"; agora cada edição
  mostra só as suas.

Nas fases anteriores (registados nos commits):

- `str.capitalize()` não existe no MicroPython 1.12 (só falhava lá); o build
  passou a recusar estes métodos.
- Índice da pesquisa grande demais para um módulo: partido por disciplina em
  partes de 28 KB no máximo.
- Escolha múltipla com a resposta certa quase sempre na opção 1: as opções
  passaram a ser baralhadas no build.
- Regressão: "todos os x iguais" dependia de arredondamentos.
- Equações: membros trocados quando a incógnita só estava à direita;
  conjunto-solução repetido; substituição com números nos sistemas.
- Símbolos sem substituto no modo de letras simples (∩ ∪ ∅ ∛ γ ⁿ ö…); o
  build passou a verificar que todos têm substituto.
- Calculadora de geometria com 28,7 KB (acima dos 25 KB): os sólidos
  passaram para `c_msol`.
- Probabilidades: rótulos sobrepostos nas árvores de 3 categorias e linha do
  cabeçalho a cortar a tabela de dupla entrada.
- Edições de reserva: compressão irreversível quando um pedaço começava
  dentro de um token; separador da tabela com quebras de linha; compressor
  lento (131 s, depois 55 s).
