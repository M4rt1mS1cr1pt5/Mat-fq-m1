# x_m2.py - M1TR4M: exercicios de Estat\xedstica (gerado pelo build).
D = "@V 1\n\
@N 13\n\
@T Estat\xedstica\n\
@X n|m2x1|m2d|r|\n\
Qual \xe9 a m\xe9dia de 4, 7, 7 e 10?\n\
@S 7\n\
@P Soma os dados e divide pelo n\xfamero de dados.\n\
@D\n\
(4 + 7 + 7 + 10) / 4 = 7.\n\
@X n|m2x2|m2d|r|\n\
Qual \xe9 a mediana de 5, 1, 9, 3, 7 e 11?\n\
@S 6\n\
@P Ordena; com n par, faz a m\xe9dia dos dois do meio.\n\
@D\n\
Ordenados: 1, 3, 5, 7, 9, 11; mediana (5 + 7) / 2 = 6.\n\
@X m|m2x3|m2a|r|\n\
Qual destas vari\xe1veis \xe9 quantitativa cont\xednua?\n\
@O o tempo de uma corrida|o clube preferido|a cor dos olhos|o n\xfamero de irm\xe3os\n\
@S 1\n\
@P Cont\xednua: pode tomar qualquer valor num intervalo.\n\
@D\n\
O tempo pode ser 12,3 s ou 12,31 s; o n\xfamero de irm\xe3os \xe9 discreto; a cor e o clube s\xe3o qualitativos.\n\
@X n|m2x4|m2e|r|\n\
Dados: 2, 3, 5, 6, 8, 9, 12 e 15. Qual \xe9 o 1.\xba quartil?\n\
@S 4\n\
@P Q1 \xe9 a mediana da metade de baixo.\n\
@D\n\
Metade de baixo: 2, 3, 5, 6; Q1 = (3 + 5) / 2 = 4.\n\
@X n|m2x5|m2e|r|\n\
Com Q1 = 20 e Q3 = 30, acima de que valor um dado \xe9 outlier?\n\
@S 45\n\
@P Barreira de cima: Q3 + 1,5 AIQ.\n\
@D\n\
AIQ = 10; 30 + 1,5 \xd7 10 = 45.\n\
@X n|m2x6|m2f|r|\n\
Qual \xe9 a amplitude de 3, 9, 4, 15 e 7?\n\
@S 12\n\
@P Amplitude = m\xe1ximo - m\xednimo.\n\
@D\n\
15 - 3 = 12.\n\
@X n|m2x7|m2f|r|\n\
Qual \xe9 a vari\xe2ncia amostral de 2, 4 e 6?\n\
@S 4\n\
@P s\xb2 = soma dos desvios\xb2 / (n - 1).\n\
@D\n\
M\xe9dia 4; desvios -2, 0, 2; s\xb2 = (4 + 0 + 4) / 2 = 4.\n\
@X v|m2x8|m2g|r|\n\
Se somarmos 5 a todos os dados, o desvio padr\xe3o aumenta 5.\n\
@S F\n\
@P Somar uma constante desloca os dados sem os afastar uns dos outros.\n\
@D\n\
Falso: o desvio padr\xe3o fica igual; s\xf3 a m\xe9dia, a mediana e os quartis aumentam 5.\n\
@X n|m2x9|m2g|r|\n\
A m\xe9dia das temperaturas \xe9 10 \xb0C. Qual \xe9 a m\xe9dia em \xb0F, com F = 1,8 C + 32?\n\
@S 50\n\
@P m\xe9dia(y) = a \xd7 m\xe9dia(x) + b.\n\
@D\n\
1,8 \xd7 10 + 32 = 50 \xb0F.\n\
@X m|m2x10|m2h|r|\n\
Um coeficiente de correla\xe7\xe3o r = 0,05 indica:\n\
@O que x causa y|correla\xe7\xe3o linear muito fraca|correla\xe7\xe3o positiva forte|correla\xe7\xe3o negativa forte\n\
@S 2\n\
@P Valores perto de 0 indicam pouca rela\xe7\xe3o linear.\n\
@D\n\
r = 0,05 est\xe1 perto de 0: quase n\xe3o h\xe1 correla\xe7\xe3o linear.\n\
@X v|m2x11|m2h|r|\n\
Uma correla\xe7\xe3o forte entre x e y prova que x causa y.\n\
@S F\n\
@P Pensa nos gelados e nos afogamentos.\n\
@D\n\
Falso: correla\xe7\xe3o n\xe3o \xe9 causalidade; pode haver uma terceira vari\xe1vel (o calor).\n\
@X n|m2x12|m2c|r|\n\
Classes [0, 10[, [10, 20[ e [20, 30] com frequ\xeancias 2, 5 e 3. Qual \xe9 a m\xe9dia aproximada?\n\
@S 16\n\
@P Usa os pontos m\xe9dios 5, 15 e 25.\n\
@D\n\
(5 \xd7 2 + 15 \xd7 5 + 25 \xd7 3) / 10 = 16.\n\
@X n|m2x13|m2b|r|\n\
Em 50 respostas, 12 foram \"sim\". Qual \xe9 a frequ\xeancia relativa de \"sim\", em percentagem?\n\
@S 24\n\
@P fi = ni / n.\n\
@D\n\
12 / 50 = 0,24 = 24%.\n\
"
