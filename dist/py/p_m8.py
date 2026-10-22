# p_m8.py - M1TR4M: Vetores no plano e no espa\xe7o (gerado pelo build).
D = "@V 1\n\
@N 7\n\
@T Vetores no plano e no espa\xe7o\n\
@L m8a|Vetores: dire\xe7\xe3o, sentido e norma|vetor segmento orientado direcao sentido norma vetores iguais\
 vetor simetrico vetor nulo translacao seta|c_matv.vet|10|n\xfacleo||f1b:Trabalho de uma for\xe7a\
 constante|AE Mat A 10.\xba, Geometria anal\xedtica (c\xe1lculo vetorial)\n\
@A\n\
- Reconhecer um vetor pela dire\xe7\xe3o, sentido e norma.\n\
- Identificar vetores iguais, sim\xe9tricos e o vetor nulo.\n\
- Associar um vetor a uma transla\xe7\xe3o.\n\
- Representar um vetor por um segmento orientado.\n\
@B\n\
Um vetor diz \"para onde\" e \"quanto\": \xe9 o deslocamento de uma transla\xe7\xe3o.\n\
Setas paralelas, com o mesmo sentido e o mesmo comprimento, representam o mesmo vetor.\n\
@C\n\
- Segmento orientado [A, B]: origem A e extremidade B.\n\
- Vetor AB: dire\xe7\xe3o da reta AB, sentido de A para B, norma igual a AB.\n\
- Vetores iguais: mesma dire\xe7\xe3o, sentido e norma.\n\
- Sim\xe9trico de u: -u (sentido oposto).\n\
- Vetor nulo: AA, de norma 0.\n\
- A transla\xe7\xe3o de vetor u leva P em P + u.\n\
@D\n\
Exemplo: [ABCD] \xe9 um paralelogramo de centro O.\n\
- Vetor AB = vetor DC: mesma dire\xe7\xe3o, sentido e norma.\n\
- Vetor BA = -AB: sentido oposto.\n\
- Vetor AO = vetor OC, porque O \xe9 o ponto m\xe9dio de [AC].\n\
- A transla\xe7\xe3o de vetor AB leva D em C.\n\
Num quadriculado de lado 1, uma seta que avan\xe7a 3 para a direita e 4 para cima tem norma \u221a(9 + 16) = 5.\n\
A seta sim\xe9trica tem tamb\xe9m norma 5.\n\
@F Vetor sim\xe9trico|-AB = BA|A: origem;B: extremidade|mesma dire\xe7\xe3o e norma, sentido oposto|-AB = BA|\n\
@F Transla\xe7\xe3o|P' = P + u|u: vetor da transla\xe7\xe3o|todos os pontos se deslocam segundo u|a\
 transla\xe7\xe3o de vetor AB leva A em B|c_matv.vet\n\
@F\n\
Dados: hex\xe1gono regular [ABCDEF] de centro O e lado 2.\n\
Objetivo: vetores iguais a AB; normas de AO e de AD.\n\
1. Os tri\xe2ngulos [OAB], [OBC], ... s\xe3o equil\xe1teros.\n\
2. Vetores iguais a AB: FO, OC e ED (mesma dire\xe7\xe3o, sentido e norma).\n\
3. \u2016AO\u2016 = lado = 2.\n\
4. O \xe9 o ponto m\xe9dio de [AD], logo \u2016AD\u2016 = 2 + 2 = 4.\n\
> AB = FO = OC = ED; \u2016AO\u2016 = 2 e \u2016AD\u2016 = 4.\n\
Verifica\xe7\xe3o: [AD] \xe9 uma diagonal maior, o dobro do lado.\n\
@G\n\
Na F\xedsica, a velocidade, a for\xe7a e o deslocamento s\xe3o vetores.\n\
N\xe3o basta dizer quanto: \xe9 preciso dizer para onde.\n\
@H\n\
- Confundir dire\xe7\xe3o com sentido (uma dire\xe7\xe3o tem dois sentidos).\n\
- Achar que vetores iguais t\xeam de ter a mesma origem.\n\
- Esquecer que AB e BA s\xe3o sim\xe9tricos.\n\
- Dar uma dire\xe7\xe3o ao vetor nulo.\n\
@I\n\
- Vetor: dire\xe7\xe3o, sentido e norma.\n\
- Iguais: as tr\xeas iguais (a origem pode mudar).\n\
- -u: sentido oposto, mesma norma.\n\
- Transla\xe7\xe3o de vetor u: P passa a P + u.\n\
@J\n\
Num paralelogramo [ABCD], que vetor \xe9 igual a AD?\n\
@R\n\
BC: tem a mesma dire\xe7\xe3o, o mesmo sentido e a mesma norma que AD.\n\
@L m8b|Opera\xe7\xf5es com vetores|soma de vetores regra do triangulo regra do paralelogramo diferenca ponto\
 mais vetor produto por um numero real propriedades resultante|c_matv.vet|10|n\xfacleo|m8a:Vetores:\
 dire\xe7\xe3o, sentido e norma|f1c:Teorema da energia cin\xe9tica|AE Mat A 10.\xba, Geometria anal\xedtica\
 (c\xe1lculo vetorial)\n\
@A\n\
- Somar vetores pela regra do tri\xe2ngulo e do paralelogramo.\n\
- Somar um ponto com um vetor.\n\
- Subtrair vetores.\n\
- Multiplicar um vetor por um n\xfamero real.\n\
@B\n\
Somar vetores \xe9 encadear deslocamentos.\n\
Andar u e depois v leva ao mesmo s\xedtio que andar u + v.\n\
@C\n\
- Regra do tri\xe2ngulo: AB + BC = AC.\n\
- Regra do paralelogramo: u + v \xe9 a diagonal do paralelogramo feito com u e v.\n\
- u - v = u + (-v).\n\
- Ponto + vetor: A + AB = B.\n\
- k u: mesma dire\xe7\xe3o; sentido de u se k > 0, oposto se k < 0.\n\
- \u2016k u\u2016 = |k| \xd7 \u2016u\u2016; 0u = 0.\n\
@D\n\
Exemplo: [ABCD] \xe9 um paralelogramo.\n\
- AB + BC = AC (regra do tri\xe2ngulo).\n\
- AB + AD = AC (regra do paralelogramo).\n\
- AB - AD = AB + DA = DA + AB = DB.\n\
- A + BC = D, porque BC = AD.\n\
Se \u2016u\u2016 = 3, ent\xe3o \u2016-2u\u2016 = |-2| \xd7 3 = 6.\n\
O vetor -2u tem sentido oposto a u.\n\
Propriedades:\n\
- u + v = v + u;\n\
- (u + v) + w = u + (v + w);\n\
- k (u + v) = k u + k v.\n\
@F Regra do tri\xe2ngulo|AB + BC = AC|A, B, C: pontos|a extremidade de um vetor \xe9 a origem do outro|AB +\
 BC = AC|c_matv.vet\n\
@F Produto por um n\xfamero real|\u2016k u\u2016 = \u2223k\u2223 \xd7 \u2016u\u2016|k: n\xfamero real;u:\
 vetor|k > 0, mesmo sentido; k < 0, sentido oposto|\u2016-2u\u2016 = 2 \u2016u\u2016|c_matv.vet\n\
@F\n\
Dados: tri\xe2ngulo [ABC]; M \xe9 o ponto m\xe9dio de [BC].\n\
Objetivo: escrever AM com AB e AC.\n\
1. AM = AB + BM (regra do tri\xe2ngulo).\n\
2. BM = 1/2 BC e BC = BA + AC = AC - AB.\n\
3. AM = AB + 1/2 AC - 1/2 AB = 1/2 AB + 1/2 AC.\n\
> AM = 1/2 (AB + AC).\n\
Verifica\xe7\xe3o: com A(0, 0), B(4, 0) e C(0, 2), M \xe9 (2, 1), metade de (4, 2).\n\
@G\n\
Na F\xedsica, a for\xe7a resultante \xe9 a soma vetorial das for\xe7as.\n\
Duas for\xe7as perpendiculares de 3 N e 4 N d\xe3o uma resultante de 5 N, e n\xe3o de 7 N.\n\
@H\n\
- Somar as normas: \u2016u + v\u2016 = \u2016u\u2016 + \u2016v\u2016 s\xf3 com o mesmo sentido.\n\
- Encadear setas que n\xe3o est\xe3o \"em fila\" na regra do tri\xe2ngulo.\n\
- Escrever AB - AD = BD (\xe9 DB).\n\
- Esquecer que -2u muda o sentido.\n\
@I\n\
- AB + BC = AC.\n\
- u + v: diagonal do paralelogramo.\n\
- u - v = u + (-v).\n\
- \u2016k u\u2016 = |k| \xd7 \u2016u\u2016.\n\
- P + u: onde chega u aplicado em P.\n\
@J\n\
\u2016u\u2016 = 4. Qual \xe9 a norma de -3u?\n\
@R\n\
\u2016-3u\u2016 = |-3| \xd7 4 = 12.\n\
@L m8c|Coordenadas e norma de um vetor|coordenadas de um vetor ab = b - a norma vetor posicao operacoes com\
 coordenadas plano espaco componentes|c_matv.vet|10|n\xfacleo|m8b:Opera\xe7\xf5es com\
 vetores;m7b:Dist\xe2ncia e ponto m\xe9dio||AE Mat A 10.\xba, Geometria anal\xedtica (c\xe1lculo vetorial no\
 plano e no espa\xe7o)\n\
@A\n\
- Escrever as coordenadas de um vetor.\n\
- Calcular AB = B - A.\n\
- Calcular a norma de um vetor no plano e no espa\xe7o.\n\
- Operar com vetores em coordenadas.\n\
@B\n\
Com coordenadas, as setas passam a n\xfameros.\n\
Somar vetores \xe9 somar coordenadas.\n\
@C\n\
- Coordenadas: (u1, u2) ou (u1, u2, u3).\n\
- AB = B - A (extremidade menos origem).\n\
- u + v = (u1 + v1, u2 + v2).\n\
- k u = (k u1, k u2).\n\
- \u2016u\u2016 = \u221a(u1\xb2 + u2\xb2); no espa\xe7o junta-se u3\xb2.\n\
- B = A + AB; o vetor OP tem as coordenadas de P.\n\
@D\n\
Exemplo: A(1, -2) e B(4, 2).\n\
- AB = B - A = (4 - 1, 2 + 2) = (3, 4).\n\
- \u2016AB\u2016 = \u221a(3\xb2 + 4\xb2) = 5.\n\
Com u = (2, -1) e v = (-1, 3):\n\
- u + v = (1, 2);\n\
- 2u - v = (5, -5).\n\
No espa\xe7o, com w = (2, -1, 2):\n\
- \u2016w\u2016 = \u221a(4 + 1 + 4) = 3.\n\
O ponto C = A + 2u \xe9 (5, -4).\n\
@F Vetor definido por dois pontos|AB = B - A|A: origem;B: extremidade|no plano e no espa\xe7o|A(1, -2), B(4,\
 2): AB = (3, 4)|c_matv.vet\n\
@F Norma de um vetor|\u2016u\u2016 = \u221a(u1\xb2 + u2\xb2 + u3\xb2)|u1, u2, u3: coordenadas|no plano n\xe3o\
 h\xe1 u3|u = (3, 4): \u2016u\u2016 = 5|c_matv.vet\n\
@F\n\
Dados: A(2, 1, -1) e u = (1, 2, -2).\n\
Objetivo: o ponto B = A + 3u e a dist\xe2ncia AB.\n\
1. 3u = (3, 6, -6).\n\
2. B = (2 + 3, 1 + 6, -1 - 6) = (5, 7, -7).\n\
3. \u2016u\u2016 = \u221a(1 + 4 + 4) = 3.\n\
4. AB = \u20163u\u2016 = 3 \xd7 3 = 9.\n\
> B(5, 7, -7) e AB = 9.\n\
Verifica\xe7\xe3o: \u221a(3\xb2 + 6\xb2 + 6\xb2) = \u221a81 = 9.\n\
@G\n\
As componentes horizontal e vertical de uma for\xe7a s\xe3o as coordenadas do vetor for\xe7a.\n\
A norma d\xe1 a intensidade da for\xe7a.\n\
@H\n\
- Fazer A - B em vez de B - A.\n\
- Somar as coordenadas antes de as elevar ao quadrado.\n\
- Esquecer que (-3)\xb2 = 9 e n\xe3o -9.\n\
- Dar uma norma negativa.\n\
@I\n\
- AB = B - A.\n\
- Opera\xe7\xf5es coordenada a coordenada.\n\
- \u2016u\u2016 = \u221a(u1\xb2 + u2\xb2 + u3\xb2).\n\
- B = A + AB.\n\
@J\n\
Qual \xe9 a norma de u = (-6, 8)?\n\
@R\n\
\u2016u\u2016 = \u221a(36 + 64) = 10.\n\
@L m8d|Vetores colineares|vetores colineares mesma direcao v = ku coordenadas proporcionais pontos alinhados\
 mesmo sentido sentidos opostos|c_matv.vet|10|n\xfacleo|m8c:Coordenadas e norma de um vetor||AE Mat A\
 10.\xba, Geometria anal\xedtica (c\xe1lculo vetorial)\n\
@A\n\
- Reconhecer vetores colineares.\n\
- Usar a condi\xe7\xe3o v = k u.\n\
- Ver se tr\xeas pontos est\xe3o alinhados.\n\
@B\n\
Vetores colineares t\xeam a mesma dire\xe7\xe3o: um \xe9 m\xfaltiplo do outro.\n\
@C\n\
- u e v, n\xe3o nulos, s\xe3o colineares se v = k u (k \u2208 \u211d).\n\
- Em coordenadas: v1 / u1 = v2 / u2 (= k), sem zeros.\n\
- k > 0: mesmo sentido; k < 0: sentidos opostos.\n\
- Conven\xe7\xe3o: o vetor nulo \xe9 colinear com qualquer vetor.\n\
- A, B e C est\xe3o alinhados se AB e AC s\xe3o colineares.\n\
@D\n\
Exemplo: u = (2, -3) e v = (-6, 9).\n\
- -6 / 2 = -3 e 9 / (-3) = -3.\n\
- v = -3u: colineares, com sentidos opostos.\n\
O vetor w = (4, 6) n\xe3o \xe9 colinear com u: 4 / 2 = 2, mas 6 / (-3) = -2.\n\
Pontos A(1, 1), B(3, 4) e C(7, 10):\n\
- AB = (2, 3) e AC = (6, 9);\n\
- AC = 3 AB, logo A, B e C est\xe3o alinhados.\n\
Valor de a para (a, 6) ser colinear com (2, 3): a / 2 = 6 / 3, logo a = 4.\n\
@F Vetores colineares|v = k u|k: n\xfamero real|u n\xe3o nulo|(-6, 9) = -3 (2, -3)|c_matv.vet\n\
@F Pontos alinhados|AC = k AB|A, B, C: pontos|A \u2260 B|A(1, 1), B(3, 4), C(7, 10): AC = 3 AB|c_matv.retav\n\
@F\n\
Dados: u = (k, 2) e v = (8, k), com k real.\n\
Objetivo: valores de k para os quais u e v s\xe3o colineares.\n\
1. Coordenadas proporcionais: k / 8 = 2 / k.\n\
2. k\xb2 = 2 \xd7 8 = 16, logo k = -4 ou k = 4.\n\
3. k = 4: u = (4, 2) e v = (8, 4) = 2u, mesmo sentido.\n\
4. k = -4: u = (-4, 2) e v = (8, -4) = -2u, sentidos opostos.\n\
> k = -4 ou k = 4.\n\
Verifica\xe7\xe3o: para k = 4, u1 v2 - u2 v1 = 4 \xd7 4 - 2 \xd7 8 = 0.\n\
@G\n\
Na F\xedsica, a for\xe7a e o deslocamento podem ser colineares.\n\
Ent\xe3o o trabalho \xe9 F d (mesmo sentido) ou -F d (sentidos opostos).\n\
@H\n\
- Trocar as fra\xe7\xf5es: comparar u1 / v1 com v2 / u2.\n\
- Dividir por zero quando uma coordenada \xe9 0.\n\
- Esquecer a solu\xe7\xe3o negativa de k\xb2 = 16.\n\
- Achar que vetores com a mesma norma s\xe3o colineares.\n\
@I\n\
- Colineares: v = k u.\n\
- Coordenadas proporcionais.\n\
- k < 0: sentidos opostos.\n\
- Alinhados: AB e AC colineares.\n\
@J\n\
Os vetores u = (3, -1) e v = (-9, 3) s\xe3o colineares?\n\
@R\n\
Sim: v = -3 u, com sentidos opostos.\n\
@L m8e|Equa\xe7\xe3o vetorial da reta|equacao vetorial da reta vetor diretor parametro ponto pertence declive\
 m = u2/u1 equacao reduzida retas paralelas espaco|c_matv.retav|10|n\xfacleo|m8d:Vetores\
 colineares;m7d:Equa\xe7\xe3o reduzida da reta e semiplanos||AE Mat A 10.\xba, Geometria anal\xedtica\
 (equa\xe7\xe3o vetorial da reta)\n\
@A\n\
- Escrever a equa\xe7\xe3o vetorial de uma reta.\n\
- Ver se um ponto pertence a uma reta.\n\
- Relacionar o declive com o vetor diretor.\n\
- Passar da equa\xe7\xe3o vetorial \xe0 reduzida.\n\
@B\n\
Uma reta fica definida por um ponto e uma dire\xe7\xe3o.\n\
Cada valor do par\xe2metro k d\xe1 um ponto da reta.\n\
@C\n\
- (x, y) = A + k u, k \u2208 \u211d: reta que passa em A com vetor diretor u (n\xe3o nulo).\n\
- No espa\xe7o: (x, y, z) = A + k u, k \u2208 \u211d.\n\
- Qualquer vetor colinear com u, n\xe3o nulo, \xe9 diretor.\n\
- Declive: m = u2 / u1 (u1 \u2260 0); u1 = 0: reta vertical.\n\
- Declive m: (1, m) \xe9 um vetor diretor.\n\
- P pertence \xe0 reta se AP for colinear com u.\n\
@D\n\
Exemplo: reta r que passa em A(1, 2) e B(3, 5).\n\
- Vetor diretor: AB = (2, 3).\n\
- r: (x, y) = (1, 2) + k (2, 3), k \u2208 \u211d.\n\
- k = 2 d\xe1 o ponto (1 + 4, 2 + 6) = (5, 8).\n\
- Declive: m = 3 / 2 = 1,5.\n\
- Ordenada na origem: b = 2 - 1,5 \xd7 1 = 0,5.\n\
- Equa\xe7\xe3o reduzida: y = 1,5x + 0,5.\n\
P(7, 11) pertence a r? AP = (6, 9) = 3 (2, 3): sim, com k = 3.\n\
Q(5, 7) n\xe3o pertence a r: AQ = (4, 5) e 4 / 2 \u2260 5 / 3.\n\
@F Equa\xe7\xe3o vetorial da reta|(x, y) = (a1, a2) + k (u1, u2), k \u2208 \u211d|(a1, a2): ponto da\
 reta;(u1, u2): vetor diretor|u n\xe3o nulo; no espa\xe7o junta-se z|A(1, 2), u = (2, 3)|c_matv.retav\n\
@F Declive e vetor diretor|m = u2 / u1|(u1, u2): vetor diretor|u1 \u2260 0|u = (2, 3): m = 1,5|c_matv.retav\n\
@F\n\
Dados: reta s: y = -2x + 3 e ponto P(1, 4).\n\
Objetivo: equa\xe7\xe3o vetorial da reta paralela a s que passa em P.\n\
1. Declive de s: m = -2, logo (1, -2) \xe9 um vetor diretor.\n\
2. Retas paralelas t\xeam vetores diretores colineares.\n\
3. (x, y) = (1, 4) + k (1, -2), k \u2208 \u211d.\n\
4. Reduzida: b = 4 - (-2) \xd7 1 = 6, logo y = -2x + 6.\n\
> (x, y) = (1, 4) + k (1, -2), k \u2208 \u211d.\n\
Verifica\xe7\xe3o: k = 1 d\xe1 (2, 2) e -2 \xd7 2 + 6 = 2.\n\
@G\n\
No 11.\xba ano, em F\xedsica, a posi\xe7\xe3o num movimento retil\xedneo uniforme \xe9 P = P0 + t v.\n\
\xc9 uma equa\xe7\xe3o vetorial em que o par\xe2metro \xe9 o tempo.\n\
@H\n\
- Usar um vetor diretor nulo.\n\
- Trocar o declive: m = u1 / u2.\n\
- Achar que a equa\xe7\xe3o vetorial \xe9 \xfanica.\n\
- Esquecer \"k \u2208 \u211d\".\n\
@I\n\
- (x, y) = A + k u, k \u2208 \u211d.\n\
- u: vetor diretor, n\xe3o nulo.\n\
- m = u2 / u1.\n\
- P est\xe1 na reta se AP for colinear com u.\n\
@J\n\
Qual \xe9 o declive da reta (x, y) = (0, 1) + k (2, -6), k \u2208 \u211d?\n\
@R\n\
m = -6 / 2 = -3.\n\
@L m8f|Vetores em problemas de geometria (aprofundamento)|quarto vertice paralelogramo ponto medio com\
 vetores baricentro medianas centro de massa ga + gb + gc = 0|c_matv.bar|10|aprofundamento|m8c:Coordenadas e\
 norma de um vetor;m3d:Medianas e baricentro||AE Mat A 10.\xba, Geometria anal\xedtica (aprofundamento)\n\
@A\n\
- Determinar o 4.\xba v\xe9rtice de um paralelogramo.\n\
- Escrever o ponto m\xe9dio com vetores.\n\
- Determinar o baricentro de um tri\xe2ngulo com vetores.\n\
@B\n\
Os vetores transformam constru\xe7\xf5es em contas.\n\
O quarto v\xe9rtice, o ponto m\xe9dio e o baricentro saem de somas.\n\
@C\n\
- Paralelogramo [ABCD]: D = A + BC.\n\
- Ponto m\xe9dio de [AB]: M = A + 1/2 AB.\n\
- Baricentro G (encontro das medianas): G = A + 2/3 AM, com M o ponto m\xe9dio de [BC].\n\
- Em coordenadas: G = (A + B + C) / 3.\n\
- GA + GB + GC = 0 (vetor nulo).\n\
@D\n\
Exemplo: A(1, 1), B(5, 2) e C(6, 6).\n\
- BC = (1, 4), logo D = A + BC = (2, 5).\n\
- Ponto m\xe9dio de [BC]: M = (5,5, 4).\n\
- AM = (4,5, 3).\n\
- G = A + 2/3 AM = (4, 3).\n\
- Confirma\xe7\xe3o: ((1 + 5 + 6) / 3, (1 + 2 + 6) / 3) = (4, 3).\n\
@F Quarto v\xe9rtice do paralelogramo|D = A + BC|[ABCD]: paralelogramo|v\xe9rtices por ordem|A(1, 1), B(5,\
 2), C(6, 6): D(2, 5)|c_matv.vet\n\
@F Baricentro|G = A + 2/3 AM = (A + B + C) / 3|M: ponto m\xe9dio de [BC]|tri\xe2ngulo [ABC]|A(0, 0), B(6, 0),\
 C(3, 6): G(3, 2)|c_matv.bar\n\
@F\n\
Dados: A(2, -1), B(6, 1) e o baricentro G(4, 2) do tri\xe2ngulo [ABC].\n\
Objetivo: o v\xe9rtice C.\n\
1. G = (A + B + C) / 3, logo C = 3G - A - B.\n\
2. xC = 3 \xd7 4 - 2 - 6 = 4.\n\
3. yC = 3 \xd7 2 - (-1) - 1 = 6.\n\
> C(4, 6).\n\
Verifica\xe7\xe3o: ((2 + 6 + 4) / 3, (-1 + 1 + 6) / 3) = (4, 2).\n\
@G\n\
Na F\xedsica, o centro de massa de tr\xeas massas iguais \xe9 o baricentro do tri\xe2ngulo que formam.\n\
@H\n\
- Escrever D = A + CB (sentido trocado).\n\
- Usar 1/3 em vez de 2/3 a partir do v\xe9rtice.\n\
- Trocar a ordem dos v\xe9rtices do paralelogramo.\n\
@I\n\
- D = A + BC.\n\
- M = A + 1/2 AB.\n\
- G = A + 2/3 AM = (A + B + C) / 3.\n\
@J\n\
Qual \xe9 o baricentro do tri\xe2ngulo de v\xe9rtices (0, 0), (9, 0) e (0, 6)?\n\
@R\n\
G = (9 / 3, 6 / 3) = (3, 2).\n\
@L m8g|Produto escalar (extens\xe3o, 11.\xba)|produto escalar angulo de dois vetores perpendiculares cosseno\
 trabalho de uma forca u1 v1 + u2 v2|c_matv.vet|11|extens\xe3o|m8c:Coordenadas e norma de um\
 vetor|f1b:Trabalho de uma for\xe7a constante|AE Mat A 11.\xba, Geometria anal\xedtica (produto escalar); extens\xe3o\n\
@A\n\
- Calcular o produto escalar em coordenadas.\n\
- Relacionar o produto escalar com o \xe2ngulo.\n\
- Reconhecer vetores perpendiculares.\n\
@B\n\
O produto escalar junta dois vetores num n\xfamero.\n\
Mede quanto um vetor \"puxa\" na dire\xe7\xe3o do outro.\n\
@C\n\
- u \xb7 v = \u2016u\u2016 \xd7 \u2016v\u2016 \xd7 cos \u03b8 (\u03b8: \xe2ngulo de u com v).\n\
- Coordenadas: u \xb7 v = u1 v1 + u2 v2 (+ u3 v3).\n\
- u e v n\xe3o nulos: u \xb7 v = 0 se e s\xf3 se forem perpendiculares.\n\
- u \xb7 v > 0: \u03b8 agudo; u \xb7 v < 0: \u03b8 obtuso.\n\
- cos \u03b8 = u \xb7 v / (\u2016u\u2016 \xd7 \u2016v\u2016).\n\
- Mat\xe9ria do 11.\xba ano (extens\xe3o).\n\
@D\n\
Exemplo: u = (3, 4) e v = (4, -3).\n\
- u \xb7 v = 3 \xd7 4 + 4 \xd7 (-3) = 0: s\xe3o perpendiculares.\n\
Com w = (2, 1):\n\
- u \xb7 w = 3 \xd7 2 + 4 \xd7 1 = 10;\n\
- cos \u03b8 = 10 / (5 \xd7 \u221a5) \u2248 0,894;\n\
- \u03b8 \u2248 26,6\xb0.\n\
@F Produto escalar (11.\xba)|u \xb7 v = u1 v1 + u2 v2 + u3 v3|u, v: vetores|no plano n\xe3o h\xe1 u3 v3|(3,\
 4) \xb7 (4, -3) = 0|c_matv.vet\n\
@F \xc2ngulo de dois vetores (11.\xba)|cos \u03b8 = u \xb7 v / (\u2016u\u2016 \xd7 \u2016v\u2016)|\u03b8:\
 \xe2ngulo de u com v|u e v n\xe3o nulos|u = (3, 4), w = (2, 1): \u03b8 \u2248 26,6\xb0|c_matv.vet\n\
@F\n\
Dados: for\xe7a F = (30, 40) N e deslocamento d = (5, 0) m.\n\
Objetivo: trabalho de F, W = F \xb7 d.\n\
1. W = 30 \xd7 5 + 40 \xd7 0 = 150 J.\n\
2. \u2016F\u2016 = \u221a(900 + 1600) = 50 N e \u2016d\u2016 = 5 m.\n\
3. cos \u03b1 = 150 / (50 \xd7 5) = 0,6, logo \u03b1 \u2248 53,1\xb0.\n\
> W = 150 J.\n\
Verifica\xe7\xe3o: W = F d cos \u03b1 = 50 \xd7 5 \xd7 0,6 = 150 J, como em F\xedsica no 10.\xba ano.\n\
@G\n\
Em F\xedsica (10.\xba ano), o trabalho de uma for\xe7a constante, W = F d cos \u03b1, \xe9 um produto escalar.\n\
@H\n\
- Multiplicar coordenadas cruzadas (u1 v2).\n\
- Achar que o produto escalar \xe9 um vetor (\xe9 um n\xfamero).\n\
- Esquecer que cos \u03b8 < 0 num \xe2ngulo obtuso.\n\
@I\n\
- u \xb7 v = u1 v1 + u2 v2.\n\
- u \xb7 v = \u2016u\u2016 \u2016v\u2016 cos \u03b8.\n\
- u \xb7 v = 0: perpendiculares.\n\
@J\n\
Os vetores (2, -1) e (1, 2) s\xe3o perpendiculares?\n\
@R\n\
Sim: 2 \xd7 1 + (-1) \xd7 2 = 0.\n\
@E 1|m8e1|Vetor, norma e ponto m\xe9dio|c_matv.vet|m8c\n\
Enunciado: A(-1, 3) e B(5, -5). Calcula o vetor AB, a sua norma e o ponto P = A + 1/2 AB.\n\
Resolu\xe7\xe3o:\n\
1. AB = B - A = (5 + 1, -5 - 3) = (6, -8)\n\
2. \u2016AB\u2016 = \u221a(36 + 64) = 10\n\
3. P = (-1 + 3, 3 - 4) = (2, -1)\n\
Resultado: AB = (6, -8), \u2016AB\u2016 = 10 e P(2, -1).\n\
Interpreta\xe7\xe3o: P \xe9 o ponto m\xe9dio de [AB].\n\
Erros a evitar: calcular A - B.\n\
@E 2|m8e2|Tr\xeas pontos alinhados|c_matv.retav|m8d\n\
Enunciado: para que valor de a est\xe3o A(1, 2), B(3, 6) e C(a, 10) alinhados?\n\
Resolu\xe7\xe3o:\n\
1. AB = (2, 4) e AC = (a - 1, 8).\n\
2. Colineares: (a - 1) / 2 = 8 / 4 = 2.\n\
3. a - 1 = 4, logo a = 5.\n\
Resultado: a = 5.\n\
Interpreta\xe7\xe3o: C(5, 10) e AC = 2 AB: B \xe9 o ponto m\xe9dio de [AC].\n\
Erros a evitar: igualar as normas em vez de usar a propor\xe7\xe3o.\n\
@E 3|m8e3|Da equa\xe7\xe3o vetorial \xe0 reduzida|c_matv.retav|m8e\n\
Enunciado: r: (x, y) = (-2, 5) + k (4, -2), k \u2208 \u211d. Determina o declive, a equa\xe7\xe3o reduzida e\
 o ponto de r no eixo Ox.\n\
Resolu\xe7\xe3o:\n\
1. m = -2 / 4 = -0,5\n\
2. b = 5 - (-0,5) \xd7 (-2) = 4, logo y = -0,5x + 4.\n\
3. No eixo Ox, y = 5 - 2k = 0, logo k = 2,5 e x = -2 + 4 \xd7 2,5 = 8.\n\
Resultado: y = -0,5x + 4; r corta Ox em (8, 0).\n\
Interpreta\xe7\xe3o: na equa\xe7\xe3o reduzida, -0,5 \xd7 8 + 4 = 0.\n\
Erros a evitar: usar m = u1 / u2 = -2.\n\
"
