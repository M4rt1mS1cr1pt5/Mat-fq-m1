# x_m8.py - M1TR4M: exercicios de Vetores no plano e no espa\xe7o (gerado pelo build).
D = "@V 1\n\
@N 11\n\
@T Vetores no plano e no espa\xe7o\n\
@X n|m8x1|m8c|r|\n\
Qual \xe9 a norma do vetor u = (5, -12)?\n\
@S 13\n\
@P \u2016u\u2016 = \u221a(u1\xb2 + u2\xb2).\n\
@D\n\
\u2016u\u2016 = \u221a(25 + 144) = 13.\n\
@X m|m8x2|m8a|r|\n\
Num paralelogramo [ABCD], que vetor \xe9 igual a AB?\n\
@O BC|AC|DC|CD\n\
@S 3\n\
@P Vetores iguais: mesma dire\xe7\xe3o, sentido e norma.\n\
@D\n\
AB e DC t\xeam a mesma dire\xe7\xe3o, o mesmo sentido e a mesma norma; CD \xe9 o sim\xe9trico de AB.\n\
@X n|m8x3|m8c|r|\n\
A(2, -1) e AB = (3, 4). Qual \xe9 a ordenada de B?\n\
@S 3\n\
@P B = A + AB.\n\
@D\n\
B = (2 + 3, -1 + 4) = (5, 3).\n\
@X v|m8x4|m8b|r|\n\
Se \u2016u\u2016 = 3 e \u2016v\u2016 = 4, ent\xe3o \u2016u + v\u2016 = 7.\n\
@S F\n\
@P A norma da soma depende do \xe2ngulo entre os vetores.\n\
@D\n\
Falso: s\xf3 \xe9 7 se u e v tiverem o mesmo sentido. Se forem perpendiculares, \u2016u + v\u2016 = \u221a(9\
 + 16) = 5.\n\
@X n|m8x5|m8d|r|\n\
Para que valor de a s\xe3o u = (2, a) e v = (6, -9) colineares?\n\
@S -3\n\
@P Coordenadas proporcionais: v = k u.\n\
@D\n\
v = 3u, porque 6 / 2 = 3; logo 3a = -9 e a = -3.\n\
@X m|m8x6|m8e|r|\n\
Qual destes \xe9 um vetor diretor da reta y = 3x - 2?\n\
@O (3, 1)|(-2, 3)|(1, 3)|(1, -2)\n\
@S 3\n\
@P Se o declive \xe9 m, ent\xe3o (1, m) \xe9 um vetor diretor.\n\
@D\n\
m = 3, logo (1, 3) \xe9 diretor (e qualquer m\xfaltiplo n\xe3o nulo, como (2, 6)).\n\
@X v|m8x7|m8e|r|\n\
O ponto P(3, 1) pertence \xe0 reta (x, y) = (1, 2) + k (2, -1), k \u2208 \u211d.\n\
@S V\n\
@P Procura k tal que P = A + k u.\n\
@D\n\
Verdadeiro: k = 1 d\xe1 (1 + 2, 2 - 1) = (3, 1).\n\
@X n|m8x8|m8b|r|\n\
\u2016u\u2016 = 2,5. Qual \xe9 a norma de -4u?\n\
@S 10\n\
@P \u2016k u\u2016 = |k| \xd7 \u2016u\u2016.\n\
@D\n\
\u2016-4u\u2016 = |-4| \xd7 2,5 = 10.\n\
@X n|m8x9|m8f|r|\n\
Tri\xe2ngulo de v\xe9rtices A(1, 2), B(4, 7) e C(7, 0). Qual \xe9 a abcissa do baricentro?\n\
@S 4\n\
@P G = (A + B + C) / 3.\n\
@D\n\
xG = (1 + 4 + 7) / 3 = 4 e yG = (2 + 7 + 0) / 3 = 3.\n\
@X n|m8x10|m8c|r|\n\
A(1, 0, 2) e B(3, -2, 3). Qual \xe9 a norma de AB?\n\
@S 3\n\
@P AB = B - A; depois \u2016AB\u2016 = \u221a(u1\xb2 + u2\xb2 + u3\xb2).\n\
@D\n\
AB = (2, -2, 1) e \u2016AB\u2016 = \u221a(4 + 4 + 1) = 3.\n\
@X n|m8x11|m8g|r|\n\
Qual \xe9 o produto escalar de u = (2, -3) e v = (4, 1)?\n\
@S 5\n\
@P u \xb7 v = u1 v1 + u2 v2.\n\
@D\n\
u \xb7 v = 2 \xd7 4 + (-3) \xd7 1 = 5.\n\
"
