# p_mr.py - M1TR4M: Revis\xf5es do 3.\xba ciclo (gerado pelo build).
D = "@V 1\n\
@N 8\n\
@T Revis\xf5es do 3.\xba ciclo\n\
@L mra|N\xfameros: fra\xe7\xf5es, pot\xeancias e nota\xe7\xe3o cient\xedfica|fracoes operacoes potencias\
 regras expoente negativo raiz quadrada notacao cientifica numeros racionais irracionais\
 dizimas|c_comu.sci|9|revis\xe3o||q1b:Tamanho dos \xe1tomos: ordens de grandeza e escalas|AE Matem\xe1tica\
 7.\xba a 9.\xba anos (n\xfameros e opera\xe7\xf5es); revis\xe3o\n\
@A\n\
- Operar com fra\xe7\xf5es.\n\
- Aplicar as regras das pot\xeancias.\n\
- Escrever n\xfameros em nota\xe7\xe3o cient\xedfica.\n\
@C\n\
- a/b + c/d = (ad + bc) / (bd); a/b \xd7 c/d = (ac) / (bd).\n\
- a^n \xd7 a^m = a^(n + m); a^n / a^m = a^(n - m).\n\
- (a^n)^m = a^(n \xd7 m); a\u2070 = 1; a\u207b\xb9 = 1 / a.\n\
- Nota\xe7\xe3o cient\xedfica: a \xd7 10^n, com 1 \u2264 a < 10.\n\
- \u221a2 e \u03c0 s\xe3o irracionais; d\xedzimas finitas e peri\xf3dicas s\xe3o racionais.\n\
@F Produto de pot\xeancias com a mesma base|a^n \xd7 a^m = a^(n + m)|a: base;n, m: expoentes|a \u2260 0 com\
 expoentes negativos|2\xb3 \xd7 2\u2074 = 2\u2077 = 128|c_comu.sci\n\
@F Nota\xe7\xe3o cient\xedfica|a \xd7 10^n|a: entre 1 e 10 (sem o 10);n: inteiro|n\xfameros positivos|0,00045\
 = 4,5 \xd7 10\u207b\u2074|c_comu.sci\n\
@F\n\
Dados: (2/3 + 1/4) \xd7 12; 3\u2075 / 3\xb2; 0,00052 \xd7 3000.\n\
Objetivo: calcular e escrever o \xfaltimo em nota\xe7\xe3o cient\xedfica.\n\
1. 2/3 + 1/4 = 8/12 + 3/12 = 11/12, e 11/12 \xd7 12 = 11.\n\
2. 3\u2075 / 3\xb2 = 3\xb3 = 27.\n\
3. 5,2 \xd7 10\u207b\u2074 \xd7 3 \xd7 10\xb3 = 15,6 \xd7 10\u207b\xb9 = 1,56.\n\
> 11, 27 e 1,56 (ou 1,56 \xd7 10\u2070).\n\
Verifica\xe7\xe3o: 0,00052 \xd7 3000 = 1,56 na calculadora.\n\
@J\n\
Escreve 72 000 em nota\xe7\xe3o cient\xedfica.\n\
@R\n\
7,2 \xd7 10\u2074.\n\
@L mrb|Percentagens, aumentos e descontos|percentagem aumento desconto iva variacao percentual fator\
 multiplicativo percentagens sucessivas|c_comu.sci|7|revis\xe3o||q1e:Fra\xe7\xe3o molar e fra\xe7\xe3o\
 m\xe1ssica|AE Matem\xe1tica 7.\xba ano (percentagens); revis\xe3o\n\
@A\n\
- Calcular percentagens de uma quantidade.\n\
- Aplicar aumentos e descontos com fatores.\n\
- Calcular varia\xe7\xf5es percentuais.\n\
@C\n\
- p% de x = (p / 100) \xd7 x.\n\
- Aumento de p%: x \xd7 (1 + p/100); desconto: x \xd7 (1 - p/100).\n\
- Percentagens sucessivas multiplicam-se: + 10% e - 10% d\xe3o \xd7 0,99.\n\
- Varia\xe7\xe3o percentual = (novo - antigo) / antigo \xd7 100.\n\
- IVA de 23%: pre\xe7o com IVA = pre\xe7o sem IVA \xd7 1,23.\n\
@F Aumento percentual|novo = x \xd7 (1 + p / 100)|p: percentagem;x: valor inicial|aumentos (desconto: 1 - p /\
 100)|50 \u20ac com + 20%: 60 \u20ac|c_comu.sci\n\
@F Varia\xe7\xe3o percentual|(novo - antigo) / antigo \xd7 100|antigo: valor de refer\xeancia|antigo \u2260\
 0|de 80 \u20ac para 92 \u20ac: + 15%|c_comu.sci\n\
@F\n\
Dados: um casaco custa 120 \u20ac, com IVA de 23%, e tem um desconto de 25%.\n\
Objetivo: pre\xe7o com desconto, pre\xe7o inicial sem IVA e o efeito de subir depois 25%.\n\
1. Com desconto: 120 \xd7 0,75 = 90 \u20ac.\n\
2. Pre\xe7o inicial sem IVA: 120 / 1,23 \u2248 97,56 \u20ac.\n\
3. Se os 90 \u20ac subirem 25%: 90 \xd7 1,25 = 112,50 \u20ac.\n\
> 90 \u20ac; 97,56 \u20ac sem IVA; 112,50 \u20ac depois do aumento.\n\
Verifica\xe7\xe3o: 0,75 \xd7 1,25 = 0,9375: menos 25% e mais 25% n\xe3o voltam ao pre\xe7o inicial.\n\
@J\n\
Um pre\xe7o passa de 40 \u20ac para 50 \u20ac. Qual \xe9 o aumento percentual?\n\
@R\n\
(50 - 40) / 40 \xd7 100 = 25%.\n\
@L mrc|Proporcionalidade direta e inversa|proporcionalidade direta inversa constante de proporcionalidade y =\
 kx y = k/x hiperbole regra de tres escala|c_matf.fx|9|revis\xe3o||q5e:Dilui\xe7\xe3o de solu\xe7\xf5es|AE\
 Matem\xe1tica 9.\xba ano (proporcionalidade inversa); revis\xe3o\n\
@A\n\
- Reconhecer grandezas direta e inversamente proporcionais.\n\
- Calcular a constante de proporcionalidade.\n\
- Representar y = kx e y = k / x.\n\
@C\n\
- Direta: y / x = k; y = kx; gr\xe1fico: reta que passa na origem.\n\
- Inversa: x \xd7 y = k; y = k / x; gr\xe1fico: ramo de hip\xe9rbole.\n\
- A regra de tr\xeas simples s\xf3 serve para proporcionalidade direta.\n\
- Escala = medida no desenho / medida real.\n\
@F Proporcionalidade direta|y = k x|k = y / x: constante de proporcionalidade|grandezas diretamente\
 proporcionais|3 kg custam 6 \u20ac: k = 2 \u20ac/kg|c_matf.fx\n\
@F Proporcionalidade inversa|y = k / x|k = x \xd7 y: constante de proporcionalidade|grandezas inversamente\
 proporcionais|4 torneiras em 6 h: k = 24|c_matf.fx\n\
@F\n\
Dados: 4 torneiras iguais enchem um tanque em 6 h; 3 kg de ma\xe7\xe3s custam 4,50 \u20ac.\n\
Objetivo: tempo com 3 torneiras e pre\xe7o de 5 kg de ma\xe7\xe3s.\n\
1. Torneiras e tempo: proporcionalidade inversa, k = 4 \xd7 6 = 24.\n\
2. Com 3 torneiras: 24 / 3 = 8 h.\n\
3. Ma\xe7\xe3s: proporcionalidade direta, k = 4,50 / 3 = 1,50 \u20ac/kg.\n\
4. 5 kg custam 1,50 \xd7 5 = 7,50 \u20ac.\n\
> 8 h e 7,50 \u20ac.\n\
Verifica\xe7\xe3o: 3 \xd7 8 = 24, igual a 4 \xd7 6.\n\
@J\n\
Se y = 12 / x, quanto vale y quando x = 4?\n\
@R\n\
y = 12 / 4 = 3.\n\
@L mrd|Equa\xe7\xf5es do 1.\xba grau e sistemas|equacao do 1.o grau resolver solucao denominadores sistema de\
 duas equacoes metodo de substituicao incognita problemas|c_matq.q2|8|revis\xe3o|||AE Matem\xe1tica 7.\xba e\
 8.\xba anos (equa\xe7\xf5es e sistemas); revis\xe3o\n\
@A\n\
- Resolver equa\xe7\xf5es do 1.\xba grau.\n\
- Resolver sistemas pelo m\xe9todo de substitui\xe7\xe3o.\n\
- Traduzir problemas em equa\xe7\xf5es.\n\
@C\n\
- Somar o mesmo aos dois membros, ou multiplic\xe1-los pelo mesmo n\xfamero (n\xe3o nulo), d\xe1 uma\
 equa\xe7\xe3o equivalente.\n\
- Denominadores: multiplica-se tudo pelo m.m.c.\n\
- Sistema: isola-se uma inc\xf3gnita e substitui-se na outra equa\xe7\xe3o.\n\
- Um sistema pode ter uma solu\xe7\xe3o, nenhuma ou infinitas.\n\
@F Equa\xe7\xe3o do 1.\xba grau|a x + b = 0 \u21d4 x = -b / a|a, b: n\xfameros|a \u2260 0|2x + 6 = 0: x = -3|c_matq.q2\n\
@F M\xe9todo de substitui\xe7\xe3o|isolar uma inc\xf3gnita e substituir na outra equa\xe7\xe3o|x, y:\
 inc\xf3gnitas|sistema de duas equa\xe7\xf5es|x + y = 5 e x - y = 1: (3, 2)|\n\
@F\n\
Dados: a equa\xe7\xe3o (x - 1) / 2 + x / 3 = 4 e o sistema x + y = 10, 2x - y = 2.\n\
Objetivo: resolver os dois.\n\
1. Equa\xe7\xe3o \xd7 6: 3(x - 1) + 2x = 24, logo 5x = 27 e x = 5,4.\n\
2. Sistema: y = 10 - x e 2x - (10 - x) = 2, logo 3x = 12 e x = 4.\n\
3. y = 10 - 4 = 6.\n\
> x = 5,4; (x, y) = (4, 6).\n\
Verifica\xe7\xe3o: (5,4 - 1) / 2 + 5,4 / 3 = 4 e 2 \xd7 4 - 6 = 2.\n\
@J\n\
Resolve 3x - 7 = 11.\n\
@R\n\
3x = 18, logo x = 6.\n\
@L mre|Intervalos e inequa\xe7\xf5es do 1.\xba grau|intervalos de numeros reais inequacao do 1.o grau\
 conjunto-solucao inverter o sinal reta real uniao intersecao conjuncao disjuncao||9|revis\xe3o|||AE\
 Matem\xe1tica 9.\xba ano (inequa\xe7\xf5es e intervalos); revis\xe3o\n\
@A\n\
- Representar conjuntos de n\xfameros com intervalos.\n\
- Resolver inequa\xe7\xf5es do 1.\xba grau.\n\
- Fazer a interse\xe7\xe3o e a uni\xe3o de intervalos.\n\
@C\n\
- [a, b]: a \u2264 x \u2264 b; ]a, b[: a < x < b; [a, +\u221e[: x \u2265 a.\n\
- Multiplicar ou dividir por um n\xfamero negativo inverte o sinal.\n\
- Conjun\xe7\xe3o (e): interse\xe7\xe3o \u2229.\n\
- Disjun\xe7\xe3o (ou): uni\xe3o \u222a.\n\
- O conjunto-solu\xe7\xe3o escreve-se com intervalos.\n\
@F Inverter o sinal|-x < 3 \u21d4 x > -3|multiplicar os dois membros por -1|inequa\xe7\xf5es|-2x \u2264 6: x\
 \u2265 -3|\n\
@F Intervalo fechado|[a, b] = {x: a \u2264 x \u2264 b}|a, b: extremos|a < b|[1, 4] cont\xe9m 1 e 4|\n\
@F\n\
Dados: 3 - 2x \u2265 7 e x + 1 > -4.\n\
Objetivo: conjunto-solu\xe7\xe3o da conjun\xe7\xe3o das duas condi\xe7\xf5es.\n\
1. 3 - 2x \u2265 7 \u21d4 -2x \u2265 4 \u21d4 x \u2264 -2 (o sinal inverte-se).\n\
2. x + 1 > -4 \u21d4 x > -5.\n\
3. Conjun\xe7\xe3o: ]-5, -2].\n\
> C.S. = ]-5, -2].\n\
Verifica\xe7\xe3o: x = -3 verifica as duas: 3 + 6 = 9 \u2265 7 e -3 + 1 = -2 > -4.\n\
@J\n\
Resolve -3x > 12.\n\
@R\n\
x < -4: C.S. = ]-\u221e, -4[.\n\
@L mrf|Teorema de Pit\xe1goras|teorema de pitagoras hipotenusa catetos triangulo retangulo reciproco diagonal\
 ternos pitagoricos distancia|c_matt.pit|8|revis\xe3o|||AE Matem\xe1tica 8.\xba ano (teorema de\
 Pit\xe1goras); revis\xe3o\n\
@A\n\
- Aplicar o teorema de Pit\xe1goras.\n\
- Usar o rec\xedproco para ver se um tri\xe2ngulo \xe9 ret\xe2ngulo.\n\
- Calcular diagonais no plano e no espa\xe7o.\n\
@C\n\
- Tri\xe2ngulo ret\xe2ngulo: c\xb2 = a\xb2 + b\xb2 (c: hipotenusa).\n\
- Rec\xedproco: se c\xb2 = a\xb2 + b\xb2, o tri\xe2ngulo \xe9 ret\xe2ngulo.\n\
- Diagonal de um ret\xe2ngulo a \xd7 b: \u221a(a\xb2 + b\xb2).\n\
- Diagonal de um paralelep\xedpedo: \u221a(a\xb2 + b\xb2 + c\xb2).\n\
- Ternos pitag\xf3ricos: 3, 4, 5; 5, 12, 13; 8, 15, 17.\n\
@F Teorema de Pit\xe1goras|c\xb2 = a\xb2 + b\xb2|c: hipotenusa;a, b: catetos|tri\xe2ngulo\
 ret\xe2ngulo|catetos 3 e 4: c = 5|c_matt.pit\n\
@F Diagonal de um paralelep\xedpedo|d = \u221a(a\xb2 + b\xb2 + c\xb2)|a, b, c: arestas|paralelep\xedpedo\
 ret\xe2ngulo|arestas 2, 3 e 6: d = 7|c_matt.pit\n\
@F\n\
Dados: uma televis\xe3o 16:9 com 120 cm de largura; um tri\xe2ngulo com lados 7, 24 e 25.\n\
Objetivo: diagonal do ecr\xe3 e ver se o tri\xe2ngulo \xe9 ret\xe2ngulo.\n\
1. Altura: 120 \xd7 9 / 16 = 67,5 cm.\n\
2. Diagonal: \u221a(120\xb2 + 67,5\xb2) \u2248 137,68 cm, cerca de 54 polegadas.\n\
3. 7\xb2 + 24\xb2 = 49 + 576 = 625, que \xe9 25\xb2: o tri\xe2ngulo \xe9 ret\xe2ngulo.\n\
> Diagonal \u2248 137,68 cm; o tri\xe2ngulo \xe9 ret\xe2ngulo.\n\
Verifica\xe7\xe3o: a diagonal \xe9 maior do que a largura, como deve ser.\n\
@J\n\
Os catetos de um tri\xe2ngulo ret\xe2ngulo medem 6 e 8. Quanto mede a hipotenusa?\n\
@R\n\
\u221a(36 + 64) = 10.\n\
@L mrg|Semelhan\xe7a de figuras|semelhanca razao de semelhanca ampliacao reducao criterios aa lal lll areas\
 volumes escala teorema de tales|c_matt.sem|7|revis\xe3o|||AE Matem\xe1tica 7.\xba e 9.\xba anos\
 (semelhan\xe7a); revis\xe3o\n\
@A\n\
- Reconhecer figuras semelhantes e a raz\xe3o de semelhan\xe7a.\n\
- Usar os crit\xe9rios de semelhan\xe7a de tri\xe2ngulos.\n\
- Relacionar per\xedmetros, \xe1reas e volumes.\n\
@C\n\
- Figuras semelhantes: mesma forma; comprimentos multiplicados por k.\n\
- k > 1: amplia\xe7\xe3o; k < 1: redu\xe7\xe3o.\n\
- Tri\xe2ngulos: crit\xe9rios AA, LAL e LLL.\n\
- Per\xedmetros \xd7 k; \xe1reas \xd7 k\xb2; volumes \xd7 k\xb3.\n\
- Tales: retas paralelas cortam segmentos proporcionais.\n\
@F Raz\xe3o de semelhan\xe7a|k = lado novo / lado correspondente|lados correspondentes|figuras semelhantes|6\
 cm passa a 9 cm: k = 1,5|c_matt.sem\n\
@F \xc1reas e volumes|A' = k\xb2 A; V' = k\xb3 V|k: raz\xe3o de semelhan\xe7a|figuras semelhantes|k = 2:\
 \xe1rea \xd7 4 e volume \xd7 8|c_matt.sem\n\
@F\n\
Dados: uma foto de 10 cm \xd7 15 cm \xe9 ampliada e o lado de 10 cm passa a 25 cm.\n\
Objetivo: raz\xe3o de semelhan\xe7a, novo comprimento e nova \xe1rea.\n\
1. k = 25 / 10 = 2,5.\n\
2. Comprimento: 15 \xd7 2,5 = 37,5 cm.\n\
3. \xc1rea: 150 \xd7 2,5\xb2 = 937,5 cm\xb2.\n\
> k = 2,5; 25 cm \xd7 37,5 cm; 937,5 cm\xb2.\n\
Verifica\xe7\xe3o: 25 \xd7 37,5 = 937,5 cm\xb2.\n\
@J\n\
Num mapa \xe0 escala 1 : 50 000, 4 cm correspondem a quantos quil\xf3metros?\n\
@R\n\
4 \xd7 50 000 = 200 000 cm, ou seja, 2 km.\n\
@L mrh|\xc1reas e volumes|areas volumes circulo perimetro prisma cilindro cone piramide esfera solidos\
 unidades litro|c_comu.sci|9|revis\xe3o|||AE Matem\xe1tica 7.\xba a 9.\xba anos (\xe1reas e volumes); revis\xe3o\n\
@A\n\
- Calcular \xe1reas de figuras planas.\n\
- Calcular volumes de s\xf3lidos.\n\
- Converter unidades de \xe1rea e de volume.\n\
@C\n\
- C\xedrculo: A = \u03c0 r\xb2; per\xedmetro 2\u03c0 r.\n\
- Tri\xe2ngulo: base \xd7 altura / 2; trap\xe9zio: (B + b) \xd7 h / 2.\n\
- Prisma e cilindro: V = \xe1rea da base \xd7 altura.\n\
- Pir\xe2mide e cone: V = \xe1rea da base \xd7 altura / 3.\n\
- Esfera: V = (4/3) \u03c0 r\xb3; superf\xedcie 4\u03c0 r\xb2.\n\
- 1 m\xb2 = 10 000 cm\xb2; 1 dm\xb3 = 1 L.\n\
@F Volume do cilindro|V = \u03c0 r\xb2 h|r: raio;h: altura|cilindro reto|r = 3 cm e h = 10 cm: V \u2248 282,7\
 cm\xb3|c_comu.sci\n\
@F Volume da esfera|V = (4/3) \u03c0 r\xb3|r: raio|esfera|r = 3 cm: V \u2248 113,1 cm\xb3|c_comu.sci\n\
@F\n\
Dados: uma lata cil\xedndrica tem 4 cm de raio e 12 cm de altura. Um cone tem a mesma base e a mesma altura.\n\
Objetivo: volumes e capacidade da lata em litros.\n\
1. Lata: \u03c0 \xd7 4\xb2 \xd7 12 \u2248 603,19 cm\xb3 (exatamente 192\u03c0).\n\
2. Cone: um ter\xe7o da lata, \u2248 201,06 cm\xb3.\n\
3. Capacidade: 603,19 cm\xb3 \u2248 0,603 L.\n\
> Cerca de 603 cm\xb3 (0,6 L) e 201 cm\xb3.\n\
Verifica\xe7\xe3o: 1 L = 1000 cm\xb3.\n\
@J\n\
Qual \xe9 a \xe1rea de um c\xedrculo com 5 cm de raio?\n\
@R\n\
\u03c0 \xd7 5\xb2 \u2248 78,54 cm\xb2 (exatamente 25\u03c0).\n\
@E 1|mre1|Desconto em percentagem|c_comu.sci|mrb\n\
Enunciado: um telem\xf3vel custava 300 \u20ac e passou a custar 255 \u20ac. Qual foi o desconto, em percentagem?\n\
Resolu\xe7\xe3o:\n\
1. Varia\xe7\xe3o: 255 - 300 = -45 \u20ac.\n\
2. Varia\xe7\xe3o percentual: -45 / 300 \xd7 100 = -15%.\n\
Resultado: um desconto de 15%.\n\
Interpreta\xe7\xe3o: o pre\xe7o foi multiplicado por 0,85.\n\
Erros a evitar: dividir pelo pre\xe7o novo.\n\
@E 2|mre2|Uma vara dentro de uma caixa|c_matt.pit|mrf\n\
Enunciado: uma caixa mede 30 cm \xd7 40 cm \xd7 120 cm. Cabe l\xe1 dentro uma vara de 1,3 m?\n\
Resolu\xe7\xe3o:\n\
1. Diagonal da base: \u221a(30\xb2 + 40\xb2) = 50 cm.\n\
2. Diagonal da caixa: \u221a(50\xb2 + 120\xb2) = 130 cm.\n\
Resultado: sim; a vara de 130 cm cabe \xe0 justa na diagonal.\n\
Interpreta\xe7\xe3o: 30, 40, 50 e 50, 120, 130 s\xe3o ternos pitag\xf3ricos.\n\
Erros a evitar: somar as arestas em vez de usar Pit\xe1goras.\n\
@E 3|mre3|Um sistema num problema|c_matq.q2|mrd\n\
Enunciado: num parque, um bilhete de adulto custa 8 \u20ac e um de crian\xe7a 5 \u20ac. Venderam-se 120\
 bilhetes por 780 \u20ac. Quantos de cada?\n\
Resolu\xe7\xe3o:\n\
1. a + c = 120 e 8a + 5c = 780.\n\
2. c = 120 - a, logo 8a + 600 - 5a = 780, 3a = 180 e a = 60.\n\
3. c = 120 - 60 = 60.\n\
Resultado: 60 bilhetes de adulto e 60 de crian\xe7a.\n\
Interpreta\xe7\xe3o: 8 \xd7 60 + 5 \xd7 60 = 780 \u20ac.\n\
Erros a evitar: esquecer de multiplicar o pre\xe7o pelo n\xfamero de bilhetes.\n\
"
