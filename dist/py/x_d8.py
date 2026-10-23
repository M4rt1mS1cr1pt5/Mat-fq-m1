# x_d8.py - M1TR4M: exercicios de Dados (8.\xba ano) (gerado pelo build).
D = "@V 1\n\
@N 8\n\
@T Dados (8.\xba ano)\n\
@X n|d8x1|d8a|r|\n\
Calcula Q1 dos dados 2, 4, 5, 7, 8, 10, 11, 13.\n\
@S 4,5\n\
@P Metade de baixo: 2, 4, 5, 7.\n\
@D\n\
Q1 = (4 + 5) / 2 = 4,5.\n\
@X n|d8x2|d8a|r|\n\
Calcula Q3 dos dados 1, 3, 3, 4, 6, 7, 9 (n = 7).\n\
@S 7\n\
@P Com n \xedmpar, a mediana (4) fica de fora.\n\
@D\n\
Metade de cima: 6, 7, 9; Q3 = 7.\n\
@X n|d8x3|d8a|r|\n\
Num diagrama de extremos e quartis: m\xednimo 2, Q1 = 5, mediana 8, Q3 = 11, m\xe1ximo 15. Qual \xe9 a\
 amplitude interquartil?\n\
@S 6\n\
@P AIQ = Q3 - Q1.\n\
@D\n\
11 - 5 = 6.\n\
@X m|d8x4|d8a|r|\n\
Que percentagem dos dados est\xe1, aproximadamente, abaixo de Q1?\n\
@O 50%|75%|25%|10%\n\
@S 3\n\
@P Os quartis dividem os dados em quatro partes.\n\
@D\n\
Abaixo de Q1 est\xe1 cerca de 25% dos dados.\n\
@X v|d8x5|d8a|r|\n\
A amplitude interquartil \xe9 sempre maior do que a amplitude total.\n\
@S F\n\
@P A AIQ s\xf3 usa os 50% centrais.\n\
@D\n\
Falso: AIQ = Q3 - Q1 nunca \xe9 maior do que m\xe1ximo - m\xednimo.\n\
@X n|d8x6|d8b|r|\n\
Qual \xe9 o ponto m\xe9dio da classe [12,5; 17,5[?\n\
@S 15\n\
@P (a + b) / 2.\n\
@D\n\
(12,5 + 17,5) / 2 = 15.\n\
@X n|d8x7|d8b|r|\n\
Classes [0, 10[ com 2 dados, [10, 20[ com 5 e [20, 30[ com 3. Qual \xe9 a m\xe9dia aproximada?\n\
@S 16\n\
@P Pontos m\xe9dios 5, 15 e 25.\n\
@D\n\
(5 \xd7 2 + 15 \xd7 5 + 25 \xd7 3) / 10 = 16.\n\
@X m|d8x8|d8b|r|\n\
Num histograma, as barras...\n\
@O est\xe3o separadas por espa\xe7os|t\xeam larguras ao acaso|representam dados qualitativos|est\xe3o\
 encostadas umas \xe0s outras\n\
@S 4\n\
@P As classes s\xe3o intervalos seguidos.\n\
@D\n\
Num histograma as barras est\xe3o encostadas: as classes s\xe3o intervalos cont\xedguos.\n\
"
