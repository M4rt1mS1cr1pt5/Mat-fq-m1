# Testes no aparelho (TI-Nspire CX II-T)

Esta lista é para o aluno fazer na calculadora. Até agora, a M1TR4M só correu
no computador (simulador, CPython e MicroPython 1.12 de 32 bits). Nenhum ponto
desta lista foi ainda feito.

Como preencher: em cada linha, escreve **ok** ou o que correu mal (com o texto
do erro) na coluna "Resultado". Fotografa os ecrãs pedidos e envia as fotos
com a lista.

Os caminhos de teclas começam no menu principal e foram confirmados no
simulador. Os resultados esperados foram calculados pela própria app no
computador (com as definições de origem: 4 casas decimais em Matemática).

## 0. Antes de começar

| # | O que fazer | O que ver | Resultado |
| --- | --- | --- | --- |
| 0.1 | Ver a versão do sistema operativo (no ecrã inicial: Definições ▸ Estado) | O Python precisa da versão 5.2 ou posterior |  |
| 0.2 | Copiar os ficheiros de `dist/tns` para a calculadora com o TI-Nspire CX II Connect (ver o README) | Os ficheiros aparecem em Documentos |  |

## 1. Sonda (Fase 0)

| # | O que fazer | O que ver | Resultado |
| --- | --- | --- | --- |
| 1.1 | Abrir `M1TR4M_sonda.tns`, ir à página do `m1sonda.py` e correr (ctrl+R) | Um ecrã com: ecrã L×A, mem, sys, import, grava, data, ms, texto, plat; uma linha de símbolos; uma régua vermelha. **Fotografar.** |  |
| 1.2 | Na linha "import": diz `funciona`? | Se sim, importar entre programas do mesmo problema funciona (forma "um só documento") |  |
| 1.3 | Na linha de símbolos: √ Δ π ≈ → ∈ ≤ ² ³ ⁻ ⁴ × · é ç ã ✓ ✗ ◂ ▸ … | Anotar os que aparecem como `?` ou caixas |  |
| 1.4 | Carregar numa tecla: entra o teste de teclas. Carregar em: setas, enter, esc, del, clear, tab, shift, ctrl, menu, 0, 5, 9, vírgula, ponto, (−), x, ^, letras | Anotar o nome que aparece para cada tecla. **Fotografar.** Sair com esc duas vezes. |  |

## 2. Instalação e arranque

| # | O que fazer | O que ver | Resultado |
| --- | --- | --- | --- |
| 2.1 | Forma "um só documento": abrir `M1TR4M.tns`, ir à página do `m1.py` e correr (ctrl+R) | Animação curta (até 2 s; qualquer tecla salta) e o menu principal com 13 opções |  |
| 2.2 | Menu principal ▸ 1 2 (Definições, ajuda e Diagnóstico) ▸ 4 (Diagnóstico) ▸ 1 (Resumo do aparelho) | "Importação: documento". **Fotografar.** |  |
| 2.3 | Forma PyLib: copiar os 113 ficheiros de `dist/tns/PyLib` para a pasta PyLib; abrir `M1TR4M_arranque.tns` e correr o `m1.py` | O mesmo menu principal; no Diagnóstico, "Importação: PyLib" |  |
| 2.4 | Edição de reserva FQ: abrir `M1TR4M_FQ.tns` e correr | Menu principal com Física e Química A |  |
| 2.5 | Edição de reserva Mat: abrir `M1TR4M_Mat.tns` e correr | Menu principal com Matemática do 7.º ao 9.º ano |  |
| 2.6 | Em cada forma que arrancou: Diagnóstico ▸ Resumo do aparelho | Anotar a memória livre. **Fotografar.** |  |

Se a forma 2.1 der "falta o módulo …", usa a forma PyLib (2.3). Se uma
edição de reserva der "memória insuficiente", anota isso: no computador, a
edição FQ precisou de 876 KB de memória e a de Matemática de 1 176 KB (ver o
RELATORIO).

## 3. Tempos (critérios de aceitação)

Mede com um cronómetro (ou o telemóvel). Repete cada medição duas vezes.

| # | O que medir | Limite | Tempo 1 | Tempo 2 |
| --- | --- | --- | --- | --- |
| 3.1 | Arranque: de ctrl+R até ao menu principal (saltando a animação) | 3 s |  |  |
| 3.2 | Mudança de menu: menu principal ▸ 2 (Matemática) | 1 s |  |  |
| 3.3 | Abrir um pacote: Matemática ▸ 4 (10.º ano) ▸ 4 (Função quadrática) ▸ 1 (Lições) ▸ 1 | 2 s |  |  |
| 3.4 | Pesquisa: escrever `massa` (cada tecla) | 0,3 s por tecla |  |  |
| 3.5 | Edição de reserva FQ: de ctrl+R até ao menu principal | anotar |  |  |
| 3.6 | Edição de reserva Mat: de ctrl+R até ao menu principal | anotar |  |  |

## 4. Uma lição de cada pacote

Em cada lição: ver a página A, carregar em ▸ até à última página e confirmar
que o texto não sai do ecrã. Depois, esc até ao menu principal.

| # | Pacote | Teclas a partir do menu principal | Lição a abrir | Resultado |
| --- | --- | --- | --- | --- |
| 4.1 | q1 · Massa e tamanho dos átomos | 1 › enter › 1 › 1 › 1 › 1 | Constituição do átomo e isótopos |  |
| 4.2 | q2 · Energia dos eletrões nos átomos | 1 › enter › 1 › 2 › 1 › 1 | Espetros e radiação eletromagnética |  |
| 4.3 | q3 · Tabela Periódica | 1 › enter › 1 › 3 › 1 › 1 | História e organização da Tabela Periódica |  |
| 4.4 | q4 · Ligação química | 1 › enter › 1 › 4 › 1 › 1 | Ligação química: estabilidade, energia e comprimento |  |
| 4.5 | q5 · Gases e dispersões | 1 › enter › 1 › 5 › 1 › 1 | Lei de Avogadro, volume molar e massa volúmica de gases |  |
| 4.6 | q6 · Transformações químicas | 1 › enter › 1 › 6 › 1 › 1 | Energia nas reações: variação de entalpia |  |
| 4.7 | f1 · Energia e movimentos | 1 › enter › 2 › 1 › 1 › 1 | Energia cinética, potencial gravítica e mecânica |  |
| 4.8 | f2 · Energia e fenómenos elétricos | 1 › enter › 2 › 2 › 1 › 1 | Corrente elétrica, diferença de potencial e resistência |  |
| 4.9 | f3 · Energia, fenómenos térmicos e radiação | 1 › enter › 2 › 3 › 1 › 1 | Sistema, energia interna e temperatura |  |
| 4.10 | aq · Atividades laboratoriais de Química | 1 › enter › 3 › 1 › 1 › 1 | AL 1.1 Volume e número de moléculas de uma gota de água |  |
| 4.11 | af · Atividades laboratoriais de Física | 1 › enter › 3 › 2 › 1 › 1 | AL 1.1 Movimento num plano inclinado: energia cinética e distância |  |
| 4.12 | r7 · Revisões do 7.º ano | 1 › enter › 4 › 1 › 1 › 1 | Espaço: distâncias, Sistema Solar, peso e massa |  |
| 4.13 | r8 · Revisões do 8.º ano | 1 › enter › 4 › 2 › 1 › 1 | Átomos, moléculas, iões e fórmulas químicas |  |
| 4.14 | r9 · Revisões do 9.º ano | 1 › enter › 4 › 3 › 1 › 1 | Movimentos: rapidez, aceleração e gráficos |  |
| 4.15 | n7 · Números (7.º ano) | 2 › 1 › 1 › 1 › 1 | Números racionais: comparar e ordenar |  |
| 4.16 | a7 · Álgebra (7.º ano) | 2 › 1 › 2 › 1 › 1 | Sequências e regularidades |  |
| 4.17 | g7 · Geometria e Medida (7.º ano) | 2 › 1 › 3 › 1 › 1 | Ângulos e retas paralelas |  |
| 4.18 | d7 · Dados (7.º ano) | 2 › 1 › 4 › 1 › 1 | Tabelas de frequências e gráficos |  |
| 4.19 | n8 · Números (8.º ano) | 2 › 2 › 1 › 1 › 1 | Potências de expoente inteiro |  |
| 4.20 | a8 · Álgebra (8.º ano) | 2 › 2 › 2 › 1 › 1 | Polinómios e casos notáveis |  |
| 4.21 | g8 · Geometria e Medida (8.º ano) | 2 › 2 › 3 › 1 › 1 | Teorema de Pitágoras |  |
| 4.22 | d8 · Dados (8.º ano) | 2 › 2 › 4 › 1 › 1 | Quartis e diagrama de extremos e quartis |  |
| 4.23 | n9 · Números (9.º ano) | 2 › 3 › 1 › 1 › 1 | Números reais: racionais e irracionais |  |
| 4.24 | a9 · Álgebra (9.º ano) | 2 › 3 › 2 › 1 › 1 | Inequações do 1.º grau |  |
| 4.25 | g9 · Geometria e Medida (9.º ano) | 2 › 3 › 3 › 1 › 1 | Circunferência: ângulos e arcos |  |
| 4.26 | d9 · Probabilidades (9.º ano) | 2 › 3 › 4 › 1 › 1 | Experiências aleatórias e lei de Laplace |  |
| 4.27 | m2 · Estatística | 2 › 4 › 1 › 1 › 1 | O problema estatístico: população, amostra e variáveis |  |
| 4.28 | m3 · Geometria sintética no plano | 2 › 4 › 2 › 1 › 1 | Revisões de triângulos; mediatriz e bissetriz |  |
| 4.29 | m4 · Funções: generalidades, função afim e condições | 2 › 4 › 3 › 1 › 1 | Conceito de função e formas de a representar |  |
| 4.30 | m5 · Função quadrática | 2 › 4 › 4 › 1 › 1 | A função quadrática e o seu gráfico |  |
| 4.31 | m6 · Funções definidas por ramos e função módulo | 2 › 4 › 5 › 1 › 1 | Funções definidas por ramos |  |
| 4.32 | m7 · Geometria analítica no plano e no espaço | 2 › 4 › 6 › 1 › 1 | Referenciais: quadrantes, octantes, planos e simetrias |  |
| 4.33 | m8 · Vetores no plano e no espaço | 2 › 4 › 7 › 1 › 1 | Vetores: direção, sentido e norma |  |

No menu principal há 13 opções: "1" fica à espera de um 2.º algarismo (o
rodapé mostra "1_"); enter escolhe a opção 1.

## 5. Uma calculadora de cada grupo

Escreve os valores em cada campo e carrega em enter; no último campo, enter
calcula. Os campos não indicados ficam como estão (valor por defeito ou vazio);
clear apaga um valor por defeito. Num campo de escolha, ◂ ▸ mudam a opção.
Para mudar a unidade de um campo: ▾ leva à unidade e ◂ ▸ mudam-na.

| # | Calculadora (grupo) | Teclas | Valores a escrever | Resultado esperado | Resultado |
| --- | --- | --- | --- | --- | --- |
| 5.1 | AL 2.1 Características de uma pilha (`c_alf1`) | 4 › 1 › 3 › 8 | Correntes (mA): `50 100 150 200 250`; Tensões (V): `4,40 4,32 4,26 4,18 4,11` | ε = 4,47 V; r ≈ 1,4 Ω |  |
| 5.2 | AL 3.2 Capacidade térmica mássica (`c_alf2`) | 4 › 1 › 3 › 1 › 0 | m = `1,00` e unidade kg (▾ ▸); P = `30,0`; tempos `0 60 120 180 240 300`; temperaturas `20,0 22,0 24,0 26,0 28,0 30,0`; tabelado `897` | c = 900 J kg⁻¹ K⁻¹; erro percentual = 0,33 % |  |
| 5.3 | AL 1.1 Gota de água (`c_alq1`) | 4 › 1 › 3 › 1 › enter | (valores por defeito) | m(gota) = (0,0503 ± 0,0009) g; N ≈ 1,68 × 10²¹ moléculas |  |
| 5.4 | AL 2.2 Solução a partir de soluto sólido (`c_alq2`) | 4 › 1 › 3 › 5 | M = `249,7`; concentração pretendida `0,100` | m a pesar ≈ 2,50 g |  |
| 5.5 | Dados experimentais (`c_comd`) | 4 › 3 › 2 | Valores `2,31 2,35 2,33`; unidade `s`; incerteza de leitura `0,01` | média = 2,33 s; x = (2,33 ± 0,02) s |  |
| 5.6 | Calculadora científica (`c_comu`) | 4 › 3 › 4 | `2^10+3/4` | = 1024,75 |  |
| 5.7 | Massa molar (`c_fqat`) | 4 › 1 › 1 › 1 › enter | clear (apaga H2O) e `CuSO4.5H2O` | M = 249,71 g mol⁻¹ |  |
| 5.8 | Resistências em série e em paralelo (`c_fqci`) | 4 › 1 › 2 › 1 › 0 | Associação: em paralelo (▸ uma vez); resistências `10 20 30` (por defeito) | Req ≈ 5,5 Ω |  |
| 5.9 | Configuração eletrónica (`c_fqel`) | 4 › 1 › 1 › 7 | clear (apaga o 8) e Z = `26` | 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶ |  |
| 5.10 | Energia cinética, potencial e mecânica (`c_fqen`) | 4 › 1 › 2 › 1 › enter | m = `2,0` kg; v = `3,0` m/s; h = `5,0` m | Ec = 9,0 J; Epg = 1,0 × 10² J; Em ≈ 1,1 × 10² J |  |
| 5.11 | Acerto de equações químicas (`c_fqlg`) | 4 › 1 › 4 › 1 | (por defeito) `CH4 + O2 -> CO2 + H2O` | CH4 + 2 O2 → CO2 + 2 H2O |  |
| 5.12 | Diluição de soluções (`c_fqso`) | 4 › 1 › 1 › 1 › 2 | c inicial `0,50`; V inicial `10` mL; c final vazio; V final `100` mL | c final = 0,050 mol dm⁻³ |  |
| 5.13 | Temperatura de equilíbrio de uma mistura (`c_fqte`) | 4 › 1 › 2 › 1 › 5 | Corpo 1: m = `200` e unidade g (▾ ▸), c por defeito, `80` °C; corpo 2 sem mudança de estado: m = `100` g (▾ ▸), c por defeito, `20` °C (clear apaga o 0) | θe = 60 °C |  |
| 5.14 | Estatística de uma variável (`c_mate`) | 4 › 2 › 4 › 1 › enter | (dados por defeito) | Média = 8,2; Mediana = 7,5; Q1 = 4 · Q3 = 9; AIQ = 5 |  |
| 5.15 | Função escrita por ti (`c_matf`) | 4 › 2 › 4 › 7 | (por defeito) `x^2 - 4`, de −5 a 5 | Zeros em [-5, 5]: -2, 2 |  |
| 5.16 | Distância e ponto médio (`c_matg`) | 4 › 2 › 4 › 1 › 4 | (por defeito) A = `1 2`; B = `4 6` | AB = 5; M = (2,5; 4) |  |
| 5.17 | Equação do 2.º grau e função quadrática (`c_matq`) | 4 › 2 › 4 › 9 | a = `2`; b = `-3`; c = `1` (clear antes de cada valor) | x = 1/2 ∨ x = 1 |  |
| 5.18 | Triângulo retângulo (`c_matr`) | 4 › 2 › 3 › 5 | (por defeito) a = `3`; b = `4` | c = 5; α ≈ 36,9° e β ≈ 53,1° |  |
| 5.19 | Pontos notáveis do triângulo (`c_matt`) | 4 › 2 › 4 › 4 | (por defeito) P(0, 0), Q(6, 0), R(2, 4) | B = (8/3, 4/3); C = (3, 1); O = (2, 2) |  |
| 5.20 | Operações com vetores (`c_matv`) | 4 › 2 › 4 › 1 › 9 | (por defeito) u = `3 -4` | ‖u‖ = √(9 + 16) = 5 |  |
| 5.21 | Equação do 1.º grau (`c_mexp`) | 4 › 2 › 1 › 4 | (por defeito) `3(x - 2) + 4 = 2x - 1` | x = 1 ; C.S. = {1} |  |
| 5.22 | Ângulos, triângulos e polígonos (`c_mgeo`) | 4 › 2 › 1 › 9 | Calcular: Paralelas e secante (desenho) (◂ uma vez); ângulo `35` | 1 = 3 = 5 = 7 = 35°; 2 = 4 = 6 = 8 = 145°; opção 5: desenho |  |
| 5.23 | Isometrias (`c_mgtr`) | 4 › 2 › 2 › 8 | (por defeito) vértices `1 1; 4 1; 2 3`, translação `3 2` | A'(4, 3); B'(7, 3); C'(5, 5) |  |
| 5.24 | Frações e números racionais (`c_mnum`) | 4 › 2 › 1 › 1 › enter | (por defeito) `1/2 + 3/4 × (2/3 - 1)` | = 1/4 |  |
| 5.25 | Fatorizar e resolver por fatorização (`c_mpol`) | 4 › 2 › 2 › 5 | (por defeito) `x^3 - 4x` | x³ - 4x = x(x - 2)(x + 2) |  |
| 5.26 | Dois dados ou moedas (`c_mprb`) | 4 › 2 › 3 › 1 › 1 | Soma de dois dados; acontecimento `7` | P(A) = 6/36 = 1/6 ≈ 0,17 ≈ 16,7%; opção 5: tabela |  |
| 5.27 | Proporcionalidade direta (`c_mprp`) | 4 › 2 › 1 › 6 | (por defeito) x: `2 3 5 ?`; y: `6 9 ? 21` | k = y/x = 3; y = 3x |  |
| 5.28 | Notação científica (`c_mrea`) | 4 › 2 › 2 › 2 | (por defeito) `0,00052` | A = 5,2 × 10⁻⁴ |  |
| 5.29 | Sólidos: áreas e volumes (`c_msol`) | 4 › 2 › 3 › 9 | Sólido: Esfera (◂ uma vez); 1.ª medida `3` | V = 36π ≈ 113,1 u.v.; A = 36π ≈ 113,1 u.a. |  |

## 6. Pesquisa, definições, progresso e memória

| # | O que fazer | O que ver | Resultado |
| --- | --- | --- | --- |
| 6.1 | Menu principal ▸ 3 (Pesquisa global); escrever `massa molar` | Resultados a cada tecla; um deles é "C Massa molar" |  |
| 6.2 | Abrir esse resultado; depois esc | Abre a calculadora; ao voltar, a pesquisa escrita mantém-se |  |
| 6.3 | Na pesquisa, carregar em tab | O filtro muda entre tudo, FQ e Mat |  |
| 6.4 | Definições: menu principal ▸ 1 2 ▸ 1 (Definições) ▸ 1 enter (Casas decimais) ▸ ▴ ▴ até ao valor 2 ▸ enter | A opção passa a "Casas decimais em Matemática: 2" (no menu, o valor 2 está na linha 3) |  |
| 6.5 | Fazer um exercício: menu principal ▸ 9 (Exercícios e testes) e responder a uma pergunta | Correção com ✓ ou ✗ |  |
| 6.6 | Sair da app (menu principal ▸ 1 3 ▸ confirmar), gravar o documento (ctrl+S), fechar e voltar a abrir; correr outra vez | As casas decimais continuam em 2; "O meu progresso" (opção 10) mostra o exercício feito |  |
| 6.7 | Usar a app durante 10 minutos (lições, calculadoras, pesquisa); depois Diagnóstico ▸ Resumo do aparelho | Anotar a memória livre. **Fotografar.** |  |
| 6.8 | Se algum símbolo aparecer como `?` ou caixa: Definições ▸ Acentos e símbolos ▸ letras simples | O texto passa a usar só letras simples |  |

## 7. No fim

Envia: as fotografias (1.1, 1.4, 2.2, 2.6, 6.7), esta lista preenchida e os
tempos da secção 3.
