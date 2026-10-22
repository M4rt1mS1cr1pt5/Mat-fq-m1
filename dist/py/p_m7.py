# p_m7.py - M1TR4M: Geometria anal\xedtica no plano e no espa\xe7o (gerado pelo build).
D = "@V 1\n\
@N 6\n\
@T Geometria anal\xedtica no plano e no espa\xe7o\n\
@L m7a|Referenciais: quadrantes, octantes, planos e simetrias|referencial cartesiano quadrantes octantes\
 planos coordenados planos paralelos retas paralelas aos eixos reflexao simetrico meia-volta\
 coordenadas|c_matg.dist|10|n\xfacleo|||AE Mat A 10.\xba, Geometria anal\xedtica; caderno de atividades (Unidade 5)\n\
@A\n\
- Identificar quadrantes, octantes e planos coordenados.\n\
- Escrever equa\xe7\xf5es de planos paralelos aos planos coordenados.\n\
- Escrever condi\xe7\xf5es de retas paralelas aos eixos.\n\
- Determinar sim\xe9tricos de pontos.\n\
@B\n\
Um referencial d\xe1 uma \"morada\" a cada ponto: no plano bastam dois n\xfameros; no espa\xe7o, tr\xeas.\n\
@C\n\
- No plano, os eixos dividem-no em 4 quadrantes (1.\xba: x > 0 \u2227 y > 0).\n\
- No espa\xe7o: planos xOy (z = 0), xOz (y = 0) e yOz (x = 0); 8 octantes.\n\
- x = a: plano paralelo a yOz; z = c: plano paralelo a xOy.\n\
- x = 3 \u2227 z = 5: reta paralela a Oy (s\xf3 y varia).\n\
- Sim\xe9trico em rela\xe7\xe3o a Ox: (x, -y); a Oy: (-x, y).\n\
- Meia-volta (em rela\xe7\xe3o \xe0 origem): (-x, -y).\n\
@D\n\
Exemplo: P(2, -3) est\xe1 no 4.\xba quadrante.\n\
Sim\xe9tricos de P: em rela\xe7\xe3o a Ox, (2, 3); a Oy, (-2, -3); \xe0 origem, (-2, 3).\n\
No espa\xe7o, Q(1, -2, 4):\n\
- sim\xe9trico em rela\xe7\xe3o ao plano xOy: (1, -2, -4) (troca o sinal de z);\n\
- em rela\xe7\xe3o ao eixo Oz: (-1, 2, 4) (troca x e y);\n\
- em rela\xe7\xe3o \xe0 origem: (-1, 2, -4).\n\
O eixo Oy \xe9 definido por x = 0 \u2227 z = 0.\n\
O 1.\xba octante: x > 0 \u2227 y > 0 \u2227 z > 0.\n\
A dist\xe2ncia de Q ao plano xOy \xe9 |4| = 4.\n\
@F Sim\xe9tricos no plano|Ox: (x, -y); Oy: (-x, y); origem: (-x, -y)|(x, y): ponto inicial|reflex\xf5es e\
 meia-volta|P(2, -3): em rela\xe7\xe3o a Ox, (2, 3)|\n\
@F Planos paralelos aos coordenados|x = a; y = b; z = c|x = a \xe9 paralelo a yOz|no espa\xe7o|plano por (1,\
 2, 5) paralelo a xOy: z = 5|\n\
@F\n\
Dados: A(3, -1, 2).\n\
Objetivo: sim\xe9tricos de A e um plano por A.\n\
1. Em rela\xe7\xe3o ao plano xOz (troca o sinal de y): (3, 1, 2).\n\
2. Em rela\xe7\xe3o ao eixo Ox (troca y e z): (3, 1, -2).\n\
3. Plano por A paralelo a xOy: z = 2.\n\
4. Dist\xe2ncia de A ao plano yOz: |3| = 3.\n\
> (3, 1, 2), (3, 1, -2) e z = 2.\n\
Verifica\xe7\xe3o: os sim\xe9tricos est\xe3o \xe0 mesma dist\xe2ncia de xOz e de Ox.\n\
@G\n\
Os referenciais permitem passar da geometria para contas com n\xfameros.\n\
@H\n\
- Trocar o eixo com o plano na simetria.\n\
- Esquecer que no espa\xe7o x = a \xe9 um plano (no plano \xe9 uma reta).\n\
- Confundir o 2.\xba com o 4.\xba quadrante.\n\
- Mudar o sinal de todas as coordenadas numa reflex\xe3o num eixo.\n\
@I\n\
- 4 quadrantes no plano; 8 octantes no espa\xe7o.\n\
- x = a, y = b, z = c: planos paralelos aos coordenados.\n\
- Sim\xe9tricos: troca-se o sinal das coordenadas certas.\n\
@J\n\
Em que quadrante est\xe1 o ponto (-4, 2)?\n\
@R\n\
No 2.\xba quadrante: x < 0 \u2227 y > 0.\n\
@L m7b|Dist\xe2ncia e ponto m\xe9dio|distancia entre dois pontos ponto medio plano espaco pitagoras diametro\
 raio perimetro coordenadas|c_matg.dist|10|n\xfacleo|m7a:Referenciais: quadrantes, octantes, planos e\
 simetrias||AE Mat A 10.\xba, Geometria anal\xedtica\n\
@A\n\
- Calcular a dist\xe2ncia entre dois pontos no plano e no espa\xe7o.\n\
- Calcular as coordenadas do ponto m\xe9dio.\n\
- Usar a dist\xe2ncia e o ponto m\xe9dio em problemas.\n\
@B\n\
A dist\xe2ncia entre dois pontos \xe9 a hipotenusa de um tri\xe2ngulo ret\xe2ngulo com os catetos paralelos aos eixos.\n\
@C\n\
- d(A, B) = \u221a((x2 - x1)\xb2 + (y2 - y1)\xb2).\n\
- No espa\xe7o junta-se (z2 - z1)\xb2.\n\
- Ponto m\xe9dio: M = ((x1 + x2) / 2, (y1 + y2) / 2).\n\
- No espa\xe7o, tamb\xe9m a m\xe9dia das cotas.\n\
@D\n\
Exemplo: A(1, 2) e B(4, 6): AB = \u221a(9 + 16) = 5.\n\
O ponto m\xe9dio \xe9 M = (2,5; 4).\n\
No espa\xe7o: A(1, 2, 3) e B(2, 0, 1): AB = \u221a(1 + 4 + 4) = 3.\n\
Conhecendo A e o ponto m\xe9dio M, o outro extremo \xe9 B = 2M - A.\n\
Exemplo: A(1, 1) e M(3, 2) d\xe3o B = (5, 3).\n\
A dist\xe2ncia de P(x, y) \xe0 origem \xe9 \u221a(x\xb2 + y\xb2).\n\
@F Dist\xe2ncia entre dois pontos|d = \u221a((x2 - x1)\xb2 + (y2 - y1)\xb2 + (z2 - z1)\xb2)|sem o termo em z\
 no plano|qualquer par de pontos|(1, 2) e (4, 6): d = 5|c_matg.dist\n\
@F Ponto m\xe9dio|M = ((x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2)|sem a coordenada z no plano|segmento\
 [AB]|(1, 2) e (4, 6): M = (2,5; 4)|c_matg.dist\n\
@F\n\
Dados: A(-1, 2) e B(3, -1).\n\
Objetivo: AB, ponto m\xe9dio e raio da circunfer\xeancia de di\xe2metro [AB].\n\
1. AB = \u221a(4\xb2 + (-3)\xb2) = \u221a(16 + 9) = 5\n\
2. M = ((-1 + 3) / 2, (2 - 1) / 2): abcissa 1 e ordenada 0,5\n\
3. Raio: 5 / 2 = 2,5\n\
> AB = 5, M(1; 0,5) e r = 2,5.\n\
Verifica\xe7\xe3o: MA = \u221a(4 + 2,25) = 2,5 = r.\n\
@G\n\
O ponto m\xe9dio fica \xe0 mesma dist\xe2ncia dos dois extremos: \xe9 o centro da circunfer\xeancia de\
 di\xe2metro [AB].\n\
@H\n\
- Somar as diferen\xe7as em vez dos seus quadrados.\n\
- Esquecer a raiz quadrada.\n\
- Subtrair as coordenadas no ponto m\xe9dio (\xe9 uma m\xe9dia).\n\
- Esquecer a coordenada z no espa\xe7o.\n\
@I\n\
- d = \u221a(soma dos quadrados das diferen\xe7as).\n\
- M = m\xe9dia das coordenadas.\n\
- B = 2M - A.\n\
@J\n\
Qual \xe9 a dist\xe2ncia entre A(0, 0, 0) e B(2, 3, 6)?\n\
@R\n\
AB = \u221a(4 + 9 + 36) = \u221a49 = 7.\n\
@L m7c|Mediatriz e plano mediador|mediatriz plano mediador equidistante equacao lugar geometrico\
 perpendicular ponto medio|c_matg.medz|10|n\xfacleo|m7b:Dist\xe2ncia e ponto m\xe9dio;m3a:Revis\xf5es de\
 tri\xe2ngulos; mediatriz e bissetriz||AE Mat A 10.\xba, Geometria anal\xedtica\n\
@A\n\
- Definir mediatriz e plano mediador.\n\
- Obter a equa\xe7\xe3o igualando dist\xe2ncias.\n\
- Verificar que a mediatriz passa no ponto m\xe9dio.\n\
@B\n\
A mediatriz da geometria sint\xe9tica ganha agora uma equa\xe7\xe3o: s\xe3o os pontos P com PA = PB.\n\
@C\n\
- Mediatriz de [AB] (no plano): pontos P(x, y) com PA = PB.\n\
- Plano mediador (no espa\xe7o): pontos P(x, y, z) com PA = PB.\n\
- Equa\xe7\xe3o: iguala-se PA\xb2 = PB\xb2 e simplifica-se.\n\
- Os termos x\xb2, y\xb2 (e z\xb2) cortam-se: fica uma equa\xe7\xe3o do 1.\xba grau.\n\
- A mediatriz \xe9 perpendicular a [AB] e passa no ponto m\xe9dio.\n\
@D\n\
Exemplo: A(1, 1) e B(5, 3).\n\
(x - 1)\xb2 + (y - 1)\xb2 = (x - 5)\xb2 + (y - 3)\xb2\n\
-2x + 1 - 2y + 1 = -10x + 25 - 6y + 9\n\
8x + 4y = 32 \u21d4 y = -2x + 8.\n\
Verifica\xe7\xe3o: o ponto m\xe9dio M(3, 2) est\xe1 na reta: -6 + 8 = 2.\n\
Declive de AB: (3 - 1) / (5 - 1) = 0,5; a mediatriz tem declive -2.\n\
O produto dos declives de retas perpendiculares \xe9 -1: 0,5 \xd7 (-2) = -1.\n\
@F Mediatriz|PA\xb2 = PB\xb2|P(x, y): ponto da mediatriz|A \u2260 B|A(1, 1) e B(5, 3): y = -2x + 8|c_matg.medz\n\
@F Plano mediador|(x - x1)\xb2 + (y - y1)\xb2 + (z - z1)\xb2 = (x - x2)\xb2 + (y - y2)\xb2 + (z -\
 z2)\xb2|A(x1, y1, z1) e B(x2, y2, z2)|no espa\xe7o|A(1, 2, 3) e B(3, 2, 1): x - z = 0|c_matg.medz\n\
@F\n\
Dados: A(1, 2, 3) e B(3, 2, 1).\n\
Objetivo: equa\xe7\xe3o do plano mediador de [AB].\n\
1. (x - 1)\xb2 + (y - 2)\xb2 + (z - 3)\xb2 = (x - 3)\xb2 + (y - 2)\xb2 + (z - 1)\xb2\n\
2. -2x + 1 - 6z + 9 = -6x + 9 - 2z + 1\n\
3. 4x - 4z = 0 \u21d4 x - z = 0\n\
> Plano mediador: x - z = 0.\n\
Verifica\xe7\xe3o: o ponto m\xe9dio M(2, 2, 2) verifica x - z = 0.\n\
@G\n\
A mediatriz e o plano mediador s\xe3o lugares geom\xe9tricos. Todos os seus pontos est\xe3o \xe0 mesma\
 dist\xe2ncia de A e de B.\n\
@H\n\
- Igualar as dist\xe2ncias sem as elevar ao quadrado (fica com ra\xedzes).\n\
- Errar o desenvolvimento de (x - a)\xb2.\n\
- Esquecer de verificar com o ponto m\xe9dio.\n\
- Achar que a mediatriz passa em A ou em B.\n\
@I\n\
- PA = PB, igualando os quadrados.\n\
- Equa\xe7\xe3o do 1.\xba grau (reta ou plano).\n\
- Passa no ponto m\xe9dio e \xe9 perpendicular a [AB].\n\
@J\n\
Qual \xe9 a mediatriz de [AB], com A(0, 0) e B(4, 0)?\n\
@R\n\
x = 2: a reta vertical que passa no ponto m\xe9dio (2, 0).\n\
@L m7d|Equa\xe7\xe3o reduzida da reta e semiplanos|equacao reduzida da reta declive ordenada na origem retas\
 paralelas reta vertical horizontal semiplano acima abaixo|c_matg.reta|10|n\xfacleo|m4c:Fun\xe7\xe3o afim||AE\
 Mat A 10.\xba, Geometria anal\xedtica\n\
@A\n\
- Escrever a equa\xe7\xe3o reduzida de uma reta.\n\
- Reconhecer retas paralelas, verticais e horizontais.\n\
- Representar semiplanos com inequa\xe7\xf5es.\n\
@B\n\
Uma reta fica definida por dois pontos, ou por um ponto e a inclina\xe7\xe3o.\n\
@C\n\
- Equa\xe7\xe3o reduzida: y = mx + b.\n\
- m = (y2 - y1) / (x2 - x1); retas paralelas t\xeam o mesmo declive.\n\
- Reta vertical: x = a (n\xe3o tem declive); horizontal: y = b.\n\
- y > mx + b: semiplano acima da reta; y < mx + b: abaixo.\n\
- Com \u2265 ou \u2264, a reta faz parte do semiplano (fechado).\n\
@D\n\
Exemplo: reta por A(1, 3) e B(3, 7): m = 2 e b = 3 - 2 \xd7 1 = 1.\n\
A equa\xe7\xe3o \xe9 y = 2x + 1; a paralela pela origem \xe9 y = 2x.\n\
Semiplano y \u2265 2x + 1: pontos acima da reta, incluindo a reta.\n\
P(0, 5): 5 \u2265 1, pertence.\n\
Q(2, 1): 1 \u2265 5 \xe9 falso, n\xe3o pertence.\n\
Se dois pontos t\xeam a mesma abcissa, a reta \xe9 vertical: x = abcissa comum.\n\
@F Equa\xe7\xe3o reduzida da reta|y = mx + b|m: declive;b: ordenada na origem|reta n\xe3o vertical|m = 2 e b\
 = 1: y = 2x + 1|c_matg.reta\n\
@F Semiplanos|y > mx + b (acima) ou y < mx + b (abaixo)|\u2265 e \u2264 incluem a reta|reta n\xe3o vertical|y\
 \u2265 2x + 1: P(0, 5) pertence|c_matg.cond\n\
@F\n\
Dados: a reta r passa em A(-1, 2) e tem declive -0,5; P(4, 4).\n\
Objetivo: equa\xe7\xe3o de r, paralela por P e posi\xe7\xe3o de P.\n\
1. b = 2 - (-0,5) \xd7 (-1) = 1,5, logo r: y = -0,5x + 1,5.\n\
2. Paralela por P: b\u2032 = 4 - (-0,5) \xd7 4 = 6, logo y = -0,5x + 6.\n\
3. Em r, para x = 4: y = -0,5; como 4 > -0,5, P est\xe1 acima de r.\n\
> r: y = -0,5x + 1,5; paralela: y = -0,5x + 6; P acima de r.\n\
Verifica\xe7\xe3o: A verifica r: -0,5 \xd7 (-1) + 1,5 = 2.\n\
@G\n\
A equa\xe7\xe3o reduzida mostra logo a inclina\xe7\xe3o e onde a reta corta Oy.\n\
@H\n\
- Calcular o declive com \u0394x / \u0394y.\n\
- Escrever y = a para uma reta vertical.\n\
- Trocar \"acima\" com \"abaixo\" nos semiplanos.\n\
- Esquecer que \u2264 inclui a pr\xf3pria reta.\n\
@I\n\
- y = mx + b.\n\
- Paralelas: mesmo m.\n\
- x = a vertical; y = b horizontal.\n\
- y > mx + b: acima.\n\
@J\n\
Escreve a equa\xe7\xe3o da reta horizontal que passa em (3, -2).\n\
@R\n\
y = -2.\n\
@L m7e|Condi\xe7\xf5es no plano com conjun\xe7\xe3o e disjun\xe7\xe3o|condicoes no plano regiao conjuncao\
 disjuncao intersecao uniao semiplano faixa quadrante circulo\
 semicirculo|c_matg.cond|10|n\xfacleo|m4d:Condi\xe7\xf5es, conjun\xe7\xe3o, disjun\xe7\xe3o e\
 intervalos;m7d:Equa\xe7\xe3o reduzida da reta e semiplanos||AE Mat A 10.\xba, Geometria anal\xedtica\n\
@A\n\
- Associar condi\xe7\xf5es em x e y a regi\xf5es do plano.\n\
- Interpretar \u2227 como interse\xe7\xe3o e \u2228 como uni\xe3o de regi\xf5es.\n\
- Verificar se um ponto pertence a uma regi\xe3o.\n\
@B\n\
Num mapa, \"a norte do rio e a oeste da estrada\" \xe9 uma regi\xe3o: duas condi\xe7\xf5es ao mesmo tempo.\n\
@C\n\
- Uma condi\xe7\xe3o em x e y define uma regi\xe3o do plano.\n\
- \u2227: interse\xe7\xe3o das regi\xf5es; \u2228: uni\xe3o.\n\
- x \u2265 0 \u2227 y \u2265 0: 1.\xba quadrante, com os eixos.\n\
- -1 \u2264 x \u2264 2: faixa vertical entre x = -1 e x = 2.\n\
- (x - a)\xb2 + (y - b)\xb2 \u2264 r\xb2: c\xedrculo.\n\
@D\n\
Exemplo: y \u2265 x - 1 \u2227 x \u2264 2: acima da reta y = x - 1 e \xe0 esquerda de x = 2.\n\
O ponto (1, 1) verifica: 1 \u2265 0 e 1 \u2264 2.\n\
O ponto (3, 1) n\xe3o verifica: 3 \u2264 2 \xe9 falso.\n\
Com \u2228: x < -1 \u2228 x > 1 s\xe3o duas regi\xf5es separadas.\n\
Para descrever uma regi\xe3o, identificam-se as fronteiras (retas ou circunfer\xeancias) e o lado de cada uma.\n\
Testa o lado com um ponto f\xe1cil, como a origem.\n\
@F Regi\xe3o definida por \u2227|C.S.(p \u2227 q) = regi\xe3o de p \u2229 regi\xe3o de q|p e q:\
 condi\xe7\xf5es em x e y|plano|y \u2265 x - 1 \u2227 x \u2264 2|c_matg.cond\n\
@F Regi\xe3o definida por \u2228|C.S.(p \u2228 q) = regi\xe3o de p \u222a regi\xe3o de q|p e q:\
 condi\xe7\xf5es em x e y|plano|x < -1 \u2228 x > 1|c_matg.cond\n\
@F\n\
Dados: a regi\xe3o definida por x\xb2 + y\xb2 \u2264 4 \u2227 y \u2265 0.\n\
Objetivo: descrever a regi\xe3o e calcular a \xe1rea.\n\
1. x\xb2 + y\xb2 \u2264 4: c\xedrculo de centro O e raio 2.\n\
2. y \u2265 0: semiplano superior (acima de Ox, com o eixo).\n\
3. Regi\xe3o: semic\xedrculo superior; \xe1rea = \u03c0 \xd7 2\xb2 / 2 = 2\u03c0 \u2248 6,28.\n\
> Semic\xedrculo de raio 2, com \xe1rea 2\u03c0.\n\
Verifica\xe7\xe3o: (0, 1) pertence: 1 \u2264 4 e 1 \u2265 0.\n\
@G\n\
As condi\xe7\xf5es com \u2227 e \u2228 permitem descrever regi\xf5es complicadas juntando pe\xe7as simples.\n\
@H\n\
- Trocar \u2227 (interse\xe7\xe3o) com \u2228 (uni\xe3o).\n\
- Esquecer as fronteiras inclu\xeddas (\u2264, \u2265).\n\
- Escolher o lado errado de uma reta.\n\
- Esquecer que x = 2 no plano \xe9 uma reta.\n\
@I\n\
- \u2227: interse\xe7\xe3o; \u2228: uni\xe3o.\n\
- Fronteiras: retas e circunfer\xeancias.\n\
- Testa o lado com um ponto.\n\
@J\n\
Que condi\xe7\xe3o define o 3.\xba quadrante, sem os eixos?\n\
@R\n\
x < 0 \u2227 y < 0.\n\
@L m7f|Circunfer\xeancia, c\xedrculo, superf\xedcie esf\xe9rica e esfera|circunferencia circulo superficie\
 esferica esfera centro raio equacao reduzida diametro tangente plano\
 coordenado|c_matg.circ|10|n\xfacleo|m7b:Dist\xe2ncia e ponto m\xe9dio||AE Mat A 10.\xba, Geometria\
 anal\xedtica; caderno de atividades (Unidade 5)\n\
@A\n\
- Escrever a equa\xe7\xe3o reduzida da circunfer\xeancia e da superf\xedcie esf\xe9rica.\n\
- Distinguir circunfer\xeancia de c\xedrculo e superf\xedcie esf\xe9rica de esfera.\n\
- Usar di\xe2metros e pontos para obter o centro e o raio.\n\
@B\n\
A circunfer\xeancia \xe9 o conjunto dos pontos \xe0 mesma dist\xe2ncia de um centro: a dist\xe2ncia d\xe1 a\
 equa\xe7\xe3o.\n\
@C\n\
- Circunfer\xeancia de centro (a, b) e raio r: (x - a)\xb2 + (y - b)\xb2 = r\xb2.\n\
- C\xedrculo: (x - a)\xb2 + (y - b)\xb2 \u2264 r\xb2.\n\
- Superf\xedcie esf\xe9rica: (x - a)\xb2 + (y - b)\xb2 + (z - c)\xb2 = r\xb2.\n\
- Esfera: o mesmo com \u2264.\n\
- Esfera tangente a um plano coordenado: r = |coordenada do centro|.\n\
@D\n\
Exemplo: centro (1, -2) e raio 3: (x - 1)\xb2 + (y + 2)\xb2 = 9.\n\
Com o centro e um ponto, o raio \xe9 a dist\xe2ncia entre eles.\n\
Com um di\xe2metro [AB], o centro \xe9 o ponto m\xe9dio e o raio \xe9 AB / 2.\n\
Exemplo: A(1, 1) e B(5, 1): centro (3, 1) e raio 2.\n\
A equa\xe7\xe3o \xe9 (x - 3)\xb2 + (y - 1)\xb2 = 4.\n\
O ponto (3, 3) est\xe1 sobre a circunfer\xeancia: 0 + 4 = 4.\n\
Esfera de centro (1, 2, -3) tangente a xOy: r = |-3| = 3.\n\
@F Circunfer\xeancia|(x - a)\xb2 + (y - b)\xb2 = r\xb2|(a, b): centro;r: raio|no plano|centro (1, -2), r = 3:\
 (x - 1)\xb2 + (y + 2)\xb2 = 9|c_matg.circ\n\
@F Superf\xedcie esf\xe9rica|(x - a)\xb2 + (y - b)\xb2 + (z - c)\xb2 = r\xb2|(a, b, c): centro;r: raio|no\
 espa\xe7o (\u2264 para a esfera)|centro (2, -1, 3), r = 3|c_matg.circ\n\
@F\n\
Dados: superf\xedcie esf\xe9rica de centro C(2, -1, 3) que passa em P(4, 1, 2).\n\
Objetivo: equa\xe7\xe3o e posi\xe7\xe3o de Q(2, -1, 0).\n\
1. r\xb2 = (4 - 2)\xb2 + (1 + 1)\xb2 + (2 - 3)\xb2 = 9, logo r = 3.\n\
2. Equa\xe7\xe3o: (x - 2)\xb2 + (y + 1)\xb2 + (z - 3)\xb2 = 9.\n\
3. Q: 0 + 0 + (0 - 3)\xb2 = 9: Q est\xe1 sobre a superf\xedcie.\n\
> (x - 2)\xb2 + (y + 1)\xb2 + (z - 3)\xb2 = 9; Q pertence \xe0 superf\xedcie.\n\
Verifica\xe7\xe3o: |3| = r, por isso a superf\xedcie \xe9 tangente a xOy, precisamente em Q.\n\
@G\n\
A equa\xe7\xe3o reduzida mostra logo o centro (com os sinais trocados) e o raio (a raiz do 2.\xba membro).\n\
@H\n\
- Ler o centro sem trocar os sinais: (x + 2)\xb2 corresponde a a = -2.\n\
- Escrever r em vez de r\xb2 no 2.\xba membro.\n\
- Confundir circunfer\xeancia (s\xf3 a linha) com c\xedrculo.\n\
- Esquecer o termo em z no espa\xe7o.\n\
@I\n\
- (x - a)\xb2 + (y - b)\xb2 = r\xb2.\n\
- Com \u2264: c\xedrculo (ou esfera).\n\
- Di\xe2metro: centro no ponto m\xe9dio, r = metade.\n\
@J\n\
Escreve a equa\xe7\xe3o da circunfer\xeancia de centro na origem e raio 4.\n\
@R\n\
x\xb2 + y\xb2 = 16.\n\
@E 1|m7e1|Dist\xe2ncia e ponto m\xe9dio|c_matg.dist|m7b\n\
Enunciado: A(2, -1) e B(8, 7). Calcula AB e o ponto m\xe9dio de [AB].\n\
Resolu\xe7\xe3o:\n\
1. AB = \u221a(6\xb2 + 8\xb2) = \u221a(36 + 64) = 10\n\
2. M = ((2 + 8) / 2, (-1 + 7) / 2) = (5, 3): abcissa 5 e ordenada 3\n\
Resultado: AB = 10 e M(5, 3).\n\
Interpreta\xe7\xe3o: M est\xe1 a 5 unidades de A e de B.\n\
Erros a evitar: escrever \u221a(6 + 8).\n\
@E 2|m7e2|Equa\xe7\xe3o de uma mediatriz|c_matg.medz|m7c\n\
Enunciado: determina a equa\xe7\xe3o reduzida da mediatriz de [AB], com A(-2, 1) e B(4, 3).\n\
Resolu\xe7\xe3o:\n\
1. (x + 2)\xb2 + (y - 1)\xb2 = (x - 4)\xb2 + (y - 3)\xb2\n\
2. 4x + 4 - 2y + 1 = -8x + 16 - 6y + 9\n\
3. 12x + 4y = 20 \u21d4 y = -3x + 5\n\
Resultado: y = -3x + 5.\n\
Interpreta\xe7\xe3o: o ponto m\xe9dio (1, 2) verifica: -3 + 5 = 2.\n\
Erros a evitar: (x + 2)\xb2 = x\xb2 + 4 (falta o termo 4x).\n\
@E 3|m7e3|Circunfer\xeancia de di\xe2metro dado e um ponto|c_matg.circ|m7f\n\
Enunciado: [AB] \xe9 um di\xe2metro, com A(-1, 4) e B(5, -4). Escreve a equa\xe7\xe3o e v\xea se P(6, 3)\
 est\xe1 dentro.\n\
Resolu\xe7\xe3o:\n\
1. Centro: ponto m\xe9dio ((-1 + 5) / 2, (4 - 4) / 2) = (2, 0): abcissa 2\n\
2. AB = \u221a(36 + 64) = 10, logo r = 5 e r\xb2 = 25.\n\
3. Equa\xe7\xe3o: (x - 2)\xb2 + y\xb2 = 25.\n\
4. P: (6 - 2)\xb2 + 3\xb2 = 25: P est\xe1 sobre a circunfer\xeancia.\n\
Resultado: (x - 2)\xb2 + y\xb2 = 25; P pertence \xe0 circunfer\xeancia.\n\
Interpreta\xe7\xe3o: o \xe2ngulo APB \xe9 reto, porque [AB] \xe9 um di\xe2metro.\n\
Erros a evitar: usar AB como raio.\n\
"
