# p_a8.py - M1TR4M: \xc1lgebra (8.\xba ano) (gerado pelo build).
D = "@V 1\n\
@N 5\n\
@T \xc1lgebra (8.\xba ano)\n\
@L a8a|Polin\xf3mios e casos not\xe1veis|monomio polinomio grau termos semelhantes multiplicar polinomios\
 casos notaveis quadrado do binomio diferenca de quadrados|c_mpol.pol|8|n\xfacleo|||AE Matem\xe1tica 8.\xba\
 ano, Express\xf5es alg\xe9bricas (polin\xf3mios)\n\
@A\n\
- Somar, subtrair e multiplicar polin\xf3mios.\n\
- Usar os casos not\xe1veis.\n\
- Escrever um polin\xf3mio na forma reduzida e dizer o grau.\n\
@C\n\
- Multiplicar: cada termo de um por cada termo do outro.\n\
- Quadrado do bin\xf3mio: (a + b)\xb2 = a\xb2 + 2ab + b\xb2; (a - b)\xb2 = a\xb2 - 2ab + b\xb2.\n\
- Diferen\xe7a de quadrados: (a + b)(a - b) = a\xb2 - b\xb2.\n\
- Cuidado: (a + b)\xb2 n\xe3o \xe9 a\xb2 + b\xb2.\n\
- Forma reduzida: juntar os termos semelhantes e ordenar pelo grau.\n\
@F Quadrado do bin\xf3mio|(a \xb1 b)\xb2 = a\xb2 \xb1 2ab + b\xb2|a, b: mon\xf3mios|o termo do meio \xe9 o\
 dobro do produto|(x + 3)\xb2 = x\xb2 + 6x + 9|c_mpol.pol\n\
@F Diferen\xe7a de quadrados|(a + b)(a - b) = a\xb2 - b\xb2|a, b: mon\xf3mios|soma vezes diferen\xe7a|(x -\
 1)(x + 1) = x\xb2 - 1|c_mpol.pol\n\
@F\n\
Dados: (x + 3)\xb2 - (x - 1)(x + 1).\n\
Objetivo: forma reduzida e valor para x = 2.\n\
1. (x + 3)\xb2 = x\xb2 + 6x + 9.\n\
2. (x - 1)(x + 1) = x\xb2 - 1.\n\
3. x\xb2 + 6x + 9 - x\xb2 + 1 = 6x + 10.\n\
4. Para x = 2: 6 \xd7 2 + 10 = 22\n\
> 6x + 10 (grau 1); vale 22 para x = 2.\n\
Verifica\xe7\xe3o: (2 + 3)\xb2 - 1 \xd7 3 = 22 \u2713.\n\
@J\n\
Desenvolve (2x - 5)\xb2.\n\
@R\n\
4x\xb2 - 20x + 25 (para x = 1 vale 9).\n\
@L a8b|Fatorizar e resolver equa\xe7\xf5es por fatoriza\xe7\xe3o|fatorizar fator comum por em evidencia casos\
 notaveis diferenca de quadrados lei do anulamento do produto equacao do 2.o grau\
 incompleta|c_mpol.fat|8|n\xfacleo|||AE Matem\xe1tica 8.\xba ano, Equa\xe7\xf5es (fatoriza\xe7\xe3o)\n\
@A\n\
- Fatorizar pondo um fator comum em evid\xeancia.\n\
- Fatorizar com os casos not\xe1veis.\n\
- Resolver equa\xe7\xf5es com a lei do anulamento do produto.\n\
@C\n\
- Fator comum: 2x\xb2 - 8x = 2x(x - 4).\n\
- Diferen\xe7a de quadrados: x\xb2 - 9 = (x - 3)(x + 3).\n\
- Quadrado do bin\xf3mio: x\xb2 + 6x + 9 = (x + 3)\xb2.\n\
- Lei do anulamento do produto: a \xd7 b = 0 \u21d4 a = 0 ou b = 0.\n\
- Para resolver: tudo no 1.\xba membro, fatoriza e iguala cada fator a 0.\n\
@F Lei do anulamento do produto|a \xd7 b = 0 \u21d4 a = 0 \u2228 b = 0|a, b: n\xfameros ou express\xf5es|um\
 produto \xe9 0 se um dos fatores for 0|x(x - 4) = 0 \u21d4 x = 0 \u2228 x = 4|c_mpol.fat\n\
@F\n\
Dados: 2x\xb2 = 8x e x\xb2 - 25 = 0.\n\
Objetivo: resolver as duas equa\xe7\xf5es.\n\
1. 2x\xb2 - 8x = 0 \u21d4 2x(x - 4) = 0 \u21d4 x = 0 \u2228 x = 4\n\
2. x\xb2 - 25 = 0 \u21d4 (x - 5)(x + 5) = 0 \u21d4 x = 5 \u2228 x = -5\n\
> C.S. = {0; 4} e C.S. = {-5; 5}.\n\
Verifica\xe7\xe3o: 2 \xd7 4\xb2 = 32 e 8 \xd7 4 = 32 \u2713.\n\
@J\n\
Fatoriza x\xb2 - 10x + 25.\n\
@R\n\
(x - 5)\xb2, um quadrado do bin\xf3mio (para x = 0 vale 25).\n\
@L a8c|Equa\xe7\xf5es com denominadores e equa\xe7\xf5es literais|equacao com denominadores mmc equacao\
 literal resolver em ordem a uma letra formulas isolar variavel|c_mexp.eq1|8|n\xfacleo|||AE Matem\xe1tica\
 8.\xba ano, Equa\xe7\xf5es (literais)\n\
@A\n\
- Resolver equa\xe7\xf5es do 1.\xba grau com denominadores.\n\
- Resolver uma f\xf3rmula em ordem a uma das letras.\n\
@C\n\
- Denominadores: multiplica os dois membros pelo m.m.c.\n\
- Aten\xe7\xe3o ao sinal - antes de uma fra\xe7\xe3o: -(x - 1)/2 = (-x + 1)/2.\n\
- Equa\xe7\xe3o literal: a inc\xf3gnita \xe9 a letra pedida; as outras s\xe3o n\xfameros.\n\
- Isola a inc\xf3gnita como numa equa\xe7\xe3o num\xe9rica.\n\
- Ex.: A = b \xd7 h / 2 em ordem a h: h = 2A / b (b \u2260 0).\n\
@F Resolver em ordem a uma letra|isolar a letra pedida, como numa equa\xe7\xe3o|as outras letras s\xe3o\
 n\xfameros|n\xe3o se pode dividir por 0|v = d / t \u21d4 d = v \xd7 t|c_mexp.eq1\n\
@F\n\
Dados: (x - 1)/2 + x/3 = 4.\n\
Objetivo: resolver a equa\xe7\xe3o.\n\
1. m.m.c.(2, 3) = 6; \xd7 6: 3(x - 1) + 2x = 24.\n\
2. 3x - 3 + 2x = 24, logo 5x = 27.\n\
3. x = 27/5 = 5,4\n\
> C.S. = {5,4}.\n\
Verifica\xe7\xe3o: (5,4 - 1)/2 + 5,4/3 = 2,2 + 1,8 = 4 \u2713.\n\
@J\n\
Resolve P = 2c + 2l em ordem a l.\n\
@R\n\
2l = P - 2c, logo l = (P - 2c) / 2 (com P = 20 e c = 6, l = 4).\n\
@L a8d|Sistemas de duas equa\xe7\xf5es|sistema de duas equacoes do 1.o grau duas incognitas metodo de\
 substituicao solucao par ordenado possivel determinado indeterminado impossivel\
 retas|c_mexp.sis|8|n\xfacleo|||AE Matem\xe1tica 8.\xba ano, Sistemas de equa\xe7\xf5es\n\
@A\n\
- Resolver sistemas pelo m\xe9todo de substitui\xe7\xe3o.\n\
- Classificar um sistema.\n\
- Interpretar a solu\xe7\xe3o como o ponto de interse\xe7\xe3o de duas retas.\n\
@C\n\
- Isola uma inc\xf3gnita numa das equa\xe7\xf5es.\n\
- Substitui na outra e resolve a equa\xe7\xe3o com uma s\xf3 inc\xf3gnita.\n\
- Volta \xe0 express\xe3o isolada para calcular a outra inc\xf3gnita.\n\
- Poss\xedvel e determinado: uma solu\xe7\xe3o (retas concorrentes).\n\
- Imposs\xedvel: retas paralelas; indeterminado: retas coincidentes.\n\
@F M\xe9todo de substitui\xe7\xe3o|isolar uma inc\xf3gnita e substituir na outra equa\xe7\xe3o|x, y:\
 inc\xf3gnitas|sistemas de duas equa\xe7\xf5es do 1.\xba grau|x + y = 10 e 2x - y = 2: (4, 6)|c_mexp.sis\n\
@F\n\
Dados: x + y = 10 e 2x - y = 2.\n\
Objetivo: resolver o sistema.\n\
1. Da 1.\xaa: x = 10 - y.\n\
2. Na 2.\xaa: 2(10 - y) - y = 2, logo -3y = -18.\n\
3. y = -18 : (-3) = 6\n\
4. x = 10 - 6 = 4\n\
> (x, y) = (4, 6): sistema poss\xedvel e determinado.\n\
Verifica\xe7\xe3o: 2 \xd7 4 - 6 = 2 \u2713.\n\
@J\n\
Num estacionamento h\xe1 carros e motas: 20 ve\xedculos e 70 rodas. Quantos carros h\xe1?\n\
@R\n\
c + m = 20 e 4c + 2m = 70: c = 15 carros e 5 motas.\n\
@L a8e|Fun\xe7\xe3o afim|funcao afim y = mx + b declive ordenada na origem grafico reta funcao linear\
 proporcionalidade direta zero da funcao dois pontos|c_matf.afim|8|n\xfacleo|||AE Matem\xe1tica 8.\xba ano,\
 Fun\xe7\xf5es (fun\xe7\xe3o afim)\n\
@A\n\
- Reconhecer uma fun\xe7\xe3o afim e o seu gr\xe1fico (uma reta).\n\
- Interpretar o declive e a ordenada na origem.\n\
- Escrever a express\xe3o a partir de dois pontos.\n\
@C\n\
- Fun\xe7\xe3o afim: f(x) = mx + b; o gr\xe1fico \xe9 uma reta.\n\
- m (declive): quanto sobe y quando x aumenta 1.\n\
- b (ordenada na origem): onde a reta corta o eixo Oy.\n\
- Com b = 0: fun\xe7\xe3o linear (proporcionalidade direta).\n\
- Dois pontos: m = (y\u2082 - y\u2081) / (x\u2082 - x\u2081); depois b = y\u2081 - m x\u2081.\n\
@F Declive|m = (y\u2082 - y\u2081) / (x\u2082 - x\u2081)|(x\u2081, y\u2081) e (x\u2082, y\u2082): pontos da\
 reta|x\u2081 \u2260 x\u2082|(1, 3) e (3, 7): m = 2|c_matf.afim\n\
@F Fun\xe7\xe3o afim|f(x) = m x + b|m: declive;b: ordenada na origem|o gr\xe1fico \xe9 uma reta|m = 2, b = 1:\
 f(x) = 2x + 1|c_matf.afim\n\
@F\n\
Dados: a reta passa em A(1, 3) e B(3, 7).\n\
Objetivo: express\xe3o da fun\xe7\xe3o afim e zero.\n\
1. m = (7 - 3) / (3 - 1) = 2\n\
2. b = 3 - 2 \xd7 1 = 1, logo f(x) = 2x + 1.\n\
3. Zero: 2x + 1 = 0 \u21d4 x = -0,5.\n\
> f(x) = 2x + 1; o zero \xe9 -0,5.\n\
Verifica\xe7\xe3o: f(3) = 2 \xd7 3 + 1 = 7 \u2713.\n\
@J\n\
Um t\xe1xi cobra 3,50 \u20ac fixos e 0,80 \u20ac por km. Quanto custa uma viagem de 10 km?\n\
@R\n\
f(x) = 0,8x + 3,5; f(10) = 11,50 \u20ac.\n\
@E 1|a8e1|\xc1rea de um quadrado aumentado|c_mpol.pol|a8a\n\
Enunciado: o lado de um quadrado mede x cm. Aumenta-se o lado 3 cm. Quanto aumenta a \xe1rea?\n\
Resolu\xe7\xe3o:\n\
1. Nova \xe1rea: (x + 3)\xb2 = x\xb2 + 6x + 9.\n\
2. Aumento: x\xb2 + 6x + 9 - x\xb2 = 6x + 9.\n\
3. Para x = 5: 6 \xd7 5 + 9 = 39 cm\xb2.\n\
Resultado: a \xe1rea aumenta 6x + 9 cm\xb2 (39 cm\xb2 se x = 5).\n\
Interpreta\xe7\xe3o: 8\xb2 - 5\xb2 = 39 \u2713.\n\
Erros a evitar: escrever (x + 3)\xb2 = x\xb2 + 9.\n\
@E 2|a8e2|Bilhetes de cinema|c_mexp.sis|a8d\n\
Enunciado: foram vendidos 120 bilhetes: os de adulto custam 7 \u20ac e os de crian\xe7a 4 \u20ac.\
 Receberam-se 690 \u20ac. Quantos bilhetes de cada tipo se venderam?\n\
Resolu\xe7\xe3o:\n\
1. a + c = 120 e 7a + 4c = 690.\n\
2. a = 120 - c; 7(120 - c) + 4c = 690, logo -3c = -150.\n\
3. c = 50 e a = 120 - 50 = 70.\n\
Resultado: 70 bilhetes de adulto e 50 de crian\xe7a.\n\
Interpreta\xe7\xe3o: 7 \xd7 70 + 4 \xd7 50 = 690 \u2713.\n\
Erros a evitar: trocar as inc\xf3gnitas na resposta.\n\
@E 3|a8e3|Duas tarifas de telem\xf3vel|c_matf.afim|a8e\n\
Enunciado: o tarif\xe1rio A custa 10 \u20ac por m\xeas e 0,05 \u20ac por minuto. O B custa 0,15 \u20ac por\
 minuto, sem mensalidade. A partir de quantos minutos o A fica mais barato?\n\
Resolu\xe7\xe3o:\n\
1. A(x) = 0,05x + 10 e B(x) = 0,15x.\n\
2. Iguais quando 0,05x + 10 = 0,15x, ou seja, 0,1x = 10 e x = 100 min.\n\
3. Para 200 min: A = 20 \u20ac e B = 30 \u20ac.\n\
Resultado: acima de 100 minutos, o tarif\xe1rio A \xe9 mais barato.\n\
Interpreta\xe7\xe3o: as duas retas cruzam-se no ponto (100, 15).\n\
Erros a evitar: comparar s\xf3 as mensalidades.\n\
"
