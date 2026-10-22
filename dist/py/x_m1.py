# x_m1.py - M1TR4M: exercicios de Modelos matem\xe1ticos para a cidadania (gerado pelo build).
D = "@V 1\n\
@N 13\n\
@T Modelos matem\xe1ticos para a cidadania\n\
@X n|m1x1|m1a|r|\n\
Numa vota\xe7\xe3o com 37 votos, quantos votos s\xe3o precisos, no m\xednimo, para a maioria absoluta?\n\
@S 19\n\
@P \xc9 preciso ter mais de metade dos votos.\n\
@D\n\
Metade de 37 \xe9 18,5; mais do que isso s\xe3o pelo menos 19 votos.\n\
@X m|m1x2|m1a|r|\n\
Um candidato tem mais votos em 1.\xba lugar do que os outros, mas n\xe3o tem mais de metade. Ganha por:\n\
@O maioria absoluta|m\xe9todo de Borda|unanimidade|maioria simples\n\
@S 4\n\
@P Maioria absoluta exige mais de metade dos votos.\n\
@D\n\
Mais votos do que cada um dos outros, sem passar de metade: \xe9 maioria simples (relativa).\n\
@X n|m1x3|m1b|r|\n\
Com 4 candidatos, quantos pontos de Borda d\xe1 ao 2.\xba classificado uma coluna de 5 votantes?\n\
@S 15\n\
@P Com 4 candidatos: 4, 3, 2 e 1 pontos.\n\
@D\n\
O 2.\xba lugar vale 3 pontos: 5 \xd7 3 = 15.\n\
@X v|m1x4|m1c|r|\n\
Com os mesmos votos, a segunda volta e o m\xe9todo de Borda d\xe3o sempre o mesmo vencedor.\n\
@S F\n\
@P Experimenta com a tabela 40 ABC, 35 CBA, 25 BCA.\n\
@D\n\
Falso: nessa tabela, a 2.\xaa volta d\xe1 C e o m\xe9todo de Borda d\xe1 B.\n\
@X n|m1x5|m1d|r|\n\
Quantos duelos de Condorcet (pares de candidatos) h\xe1 com 6 candidatos?\n\
@S 15\n\
@P Com n candidatos h\xe1 n (n - 1) / 2 pares.\n\
@D\n\
6 \xd7 5 / 2 = 15 duelos.\n\
@X n|m1x6|m1e|r|\n\
Pelo m\xe9todo de Hondt, com 3 mandatos e listas de 900, 500 e 400 votos, quantos mandatos recebe a lista de\
 900 votos?\n\
@S 2\n\
@P Divide os votos por 1, 2, 3 e escolhe os 3 maiores quocientes.\n\
@D\n\
Quocientes: 900, 450 e 300; 500 e 250; 400. Os 3 maiores s\xe3o 900, 500 e 450: a lista de 900 votos recebe 2.\n\
@X v|m1x7|m1e|r|\n\
Num empate no \xfaltimo mandato, a lei eleitoral portuguesa d\xe1 o mandato \xe0 lista mais votada.\n\
@S F\n\
@P L\xea a regra de empate da Lei n.\xba 14/79 (art. 16.\xba).\n\
@D\n\
Falso: fica a lista com menos votos.\n\
@X m|m1x8|m1f|r|\n\
Quais s\xe3o os divisores do m\xe9todo de Sainte-Lagu\xeb?\n\
@O 1, 2, 3, 4, ...|1, 3, 5, 7, ...|1, 10, 100, ...|2, 4, 6, 8, ...\n\
@S 2\n\
@P S\xe3o n\xfameros \xedmpares.\n\
@D\n\
Sainte-Lagu\xeb usa os \xedmpares 1, 3, 5, 7, ...; o Hondt usa 1, 2, 3, 4, ...\n\
@X n|m1x9|m1g|r|\n\
Qual \xe9 o desconto para a Seguran\xe7a Social, em euros, de um sal\xe1rio bruto de 1 300 \u20ac?\n\
@S 143\n\
@P O trabalhador desconta 11% do bruto.\n\
@D\n\
0,11 \xd7 1 300 = 143 \u20ac.\n\
@X n|m1x10|m1h|r|\n\
Com a tabela de IRS de 2026, qual \xe9 a coleta, em euros, de um rendimento colet\xe1vel de 8 000 \u20ac?\n\
@S 1000\n\
@P 8 000 \u20ac est\xe1 no 1.\xba escal\xe3o (at\xe9 8 342 \u20ac, 12,5%).\n\
@D\n\
8 000 \xd7 0,125 = 1 000 \u20ac.\n\
@X m|m1x11|m1h|r|\n\
O que \xe9 a taxa marginal de IRS?\n\
@O a coleta a dividir pelo rendimento|a taxa do \xfaltimo escal\xe3o atingido|a taxa de reten\xe7\xe3o\
 mensal|a taxa aplicada a todo o rendimento\n\
@S 2\n\
@P A taxa m\xe9dia \xe9 a coleta a dividir pelo rendimento.\n\
@D\n\
A taxa marginal \xe9 a do \xfaltimo escal\xe3o atingido; s\xf3 paga essa taxa a parte do rendimento que\
 est\xe1 nesse escal\xe3o.\n\
@X n|m1x12|m1i|r|\n\
Qual \xe9 o juro, em euros, de 2 500 \u20ac a 2% ao ano, em juro simples, ao fim de 3 anos?\n\
@S 150\n\
@P J = C \xd7 r \xd7 t.\n\
@D\n\
J = 2 500 \xd7 0,02 \xd7 3 = 150 \u20ac.\n\
@X n|m1x13|m1i|r|\n\
Quanto vale, em euros, um capital de 1 000 \u20ac a 10% ao ano, em juro composto anual, ao fim de 2 anos?\n\
@S 1210\n\
@P Cn = C (1 + r)^t.\n\
@D\n\
1 000 \xd7 1,1\xb2 = 1 210 \u20ac.\n\
"
