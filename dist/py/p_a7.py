# p_a7.py - M1TR4M: \xc1lgebra (7.\xba ano) (gerado pelo build).
D = "@V 1\n\
@N 5\n\
@T \xc1lgebra (7.\xba ano)\n\
@L a7a|Sequ\xeancias e regularidades|sequencia regularidade termo geral termo de ordem n lei de formacao\
 diferenca constante sequencia aritmetica e termo|c_mprp.seq|7|n\xfacleo|||AE Matem\xe1tica 7.\xba ano,\
 Sequ\xeancias e regularidades\n\
@A\n\
- Descobrir a regularidade de uma sequ\xeancia.\n\
- Escrever o termo geral de uma sequ\xeancia com diferen\xe7a constante.\n\
- Calcular termos e ver se um n\xfamero \xe9 termo.\n\
@C\n\
- Termo de ordem n: u(n); u(1) \xe9 o 1.\xba termo.\n\
- Se a diferen\xe7a entre termos seguidos \xe9 sempre d, ent\xe3o u(n) = d n + (u(1) - d).\n\
- Para calcular u(20), substitui n por 20.\n\
- Um n\xfamero \xe9 termo se u(n) = n\xfamero tem solu\xe7\xe3o n inteira e positiva.\n\
@F Termo geral (diferen\xe7a constante)|u(n) = d \xd7 n + (u(1) - d)|d: diferen\xe7a entre termos seguidos;n:\
 ordem|sequ\xeancias com diferen\xe7a constante (aritm\xe9ticas)|3, 7, 11...: u(n) = 4n - 1|c_mprp.seq\n\
@F\n\
Dados: a sequ\xeancia 3, 7, 11, 15, ...\n\
Objetivo: termo geral, u(20) e ver se 95 \xe9 termo.\n\
1. Diferen\xe7a constante: d = 7 - 3 = 4.\n\
2. u(n) = 4n + (3 - 4), ou seja, u(n) = 4n - 1.\n\
3. u(20) = 4 \xd7 20 - 1 = 79\n\
4. 4n - 1 = 95 d\xe1 4n = 96 e n = 24: 95 \xe9 o 24.\xba termo.\n\
> u(n) = 4n - 1; u(20) = 79; 95 \xe9 termo.\n\
Verifica\xe7\xe3o: u(1) = 4 - 1 = 3 \u2713.\n\
@J\n\
Qual \xe9 o termo geral da sequ\xeancia 10, 8, 6, 4, ...?\n\
@R\n\
d = -2, logo u(n) = -2n + 12 (u(1) = 10).\n\
@L a7b|Express\xf5es alg\xe9bricas|expressao algebrica variavel monomio termos semelhantes simplificar\
 reduzir propriedade distributiva valor numerico|c_mpol.pol|7|n\xfacleo|||AE Matem\xe1tica 7.\xba ano,\
 Express\xf5es alg\xe9bricas\n\
@A\n\
- Traduzir situa\xe7\xf5es por express\xf5es com letras.\n\
- Simplificar, juntando termos semelhantes.\n\
- Calcular o valor de uma express\xe3o para um valor da vari\xe1vel.\n\
@C\n\
- 3x e -5x s\xe3o termos semelhantes (mesma parte literal): 3x - 5x = -2x.\n\
- Distributiva: a(b + c) = ab + ac; -(x - 2) = -x + 2.\n\
- Os termos com x\xb2 n\xe3o se juntam com os termos com x.\n\
- Valor num\xe9rico: substitui a letra (usa par\xeanteses nos negativos).\n\
@F Propriedade distributiva|a(b + c) = ab + ac|a, b, c: n\xfameros ou express\xf5es|o fator multiplica cada\
 parcela|3(x - 4) = 3x - 12|c_mpol.pol\n\
@F\n\
Dados: 2(3x - 1) - (x + 4).\n\
Objetivo: simplificar e calcular o valor para x = -2.\n\
1. Distributiva: 6x - 2 - x - 4.\n\
2. Termos semelhantes: 6x - x = 5x e -2 - 4 = -6.\n\
3. Express\xe3o simplificada: 5x - 6.\n\
4. Para x = -2: 5 \xd7 (-2) - 6 = -16\n\
> 5x - 6; para x = -2 vale -16.\n\
Verifica\xe7\xe3o: 2(3 \xd7 (-2) - 1) - (-2 + 4) = -16 \u2713.\n\
@J\n\
Simplifica 4a + 3 - (a - 5).\n\
@R\n\
4a + 3 - a + 5 = 3a + 8 (para a = 1 vale 11).\n\
@L a7c|Equa\xe7\xf5es do 1.\xba grau|equacao incognita solucao membros equacoes equivalentes resolver\
 parenteses possivel impossivel indeterminada problemas|c_mexp.eq1|7|n\xfacleo|||AE Matem\xe1tica 7.\xba ano,\
 Equa\xe7\xf5es\n\
@A\n\
- Resolver equa\xe7\xf5es do 1.\xba grau, mesmo com par\xeanteses.\n\
- Classificar uma equa\xe7\xe3o (poss\xedvel, imposs\xedvel, indeterminada).\n\
- Resolver problemas com equa\xe7\xf5es.\n\
@C\n\
- Tira os par\xeanteses; os termos com x num membro e os n\xfameros no outro.\n\
- Ao mudar de membro, o termo muda de sinal.\n\
- Reduz e divide pelo coeficiente de x.\n\
- 0x = 5: imposs\xedvel; 0x = 0: indeterminada (qualquer x).\n\
- Verifica: substitui a solu\xe7\xe3o nos dois membros.\n\
@F Equa\xe7\xe3o do 1.\xba grau|a x = b \u21d4 x = b / a|a, b: n\xfameros|a \u2260 0 (se a = 0, \xe9\
 imposs\xedvel ou indeterminada)|3x = 15 \u21d4 x = 5|c_mexp.eq1\n\
@F\n\
Dados: 3(x - 2) = x + 4.\n\
Objetivo: resolver e verificar.\n\
1. Par\xeanteses: 3x - 6 = x + 4.\n\
2. Mudar de membro: 3x - x = 4 + 6.\n\
3. Reduzir: 2x = 10, logo x = 5.\n\
> C.S. = {5}.\n\
Verifica\xe7\xe3o: 3 \xd7 (5 - 2) = 9 e 5 + 4 = 9 \u2713.\n\
@J\n\
O dobro de um n\xfamero, mais 7, \xe9 31. Qual \xe9 o n\xfamero?\n\
@R\n\
2x + 7 = 31 \u21d4 2x = 24 \u21d4 x = 12.\n\
@L a7d|Proporcionalidade direta|proporcionalidade direta constante de proporcionalidade y = kx regra de tres\
 tabela grafico reta pela origem escala|c_mprp.prop|7|n\xfacleo|||AE Matem\xe1tica 7.\xba ano,\
 Proporcionalidade direta como fun\xe7\xe3o\n\
@A\n\
- Reconhecer grandezas diretamente proporcionais.\n\
- Calcular a constante de proporcionalidade e completar tabelas.\n\
- Interpretar o gr\xe1fico: reta que passa na origem.\n\
@C\n\
- Diretamente proporcionais: y / x \xe9 sempre o mesmo n\xfamero k.\n\
- Fun\xe7\xe3o de proporcionalidade direta: y = kx.\n\
- O gr\xe1fico \xe9 uma reta que passa na origem (0, 0).\n\
- Valor em falta: y = k \xd7 x ou x = y : k (regra de tr\xeas simples).\n\
- Escala: medida no desenho : medida real.\n\
@F Proporcionalidade direta|y = k \xd7 x|k = y / x: constante de proporcionalidade|grandezas diretamente\
 proporcionais|3 kg custam 6 \u20ac: k = 2 \u20ac/kg|c_mprp.prop\n\
@F\n\
Dados: 2 kg de laranjas custam 3,60 \u20ac.\n\
Objetivo: constante, pre\xe7o de 5 kg e peso que se compra com 9 \u20ac.\n\
1. k = 3,60 / 2 = 1,80 \u20ac/kg.\n\
2. 5 kg: 1,80 \xd7 5 = 9 \u20ac.\n\
3. Com 9 \u20ac: 9 / 1,80 = 5 kg.\n\
> k = 1,80 \u20ac/kg (o pre\xe7o do quilo); 5 kg custam 9 \u20ac.\n\
Verifica\xe7\xe3o: 9 / 5 = 1,8, o mesmo k \u2713.\n\
@J\n\
Num mapa \xe0 escala 1 : 50 000, 3 cm correspondem a quantos quil\xf3metros?\n\
@R\n\
3 \xd7 50 000 = 150 000 cm = 1,5 km.\n\
@L a7e|Percentagens|percentagem por cento aumento desconto iva valor inicial variacao percentual fator\
 multiplicativo|c_mprp.perc|7|n\xfacleo|||AE Matem\xe1tica 7.\xba ano, Percentagens\n\
@A\n\
- Calcular uma percentagem de uma quantidade.\n\
- Aplicar aumentos e descontos.\n\
- Calcular o valor inicial e a varia\xe7\xe3o percentual.\n\
@C\n\
- p% de a = (p / 100) \xd7 a.\n\
- Aumento de p%: a \xd7 (1 + p/100); desconto: a \xd7 (1 - p/100).\n\
- Valor inicial: divide pelo fator (por exemplo, por 1,23 para tirar o IVA).\n\
- Varia\xe7\xe3o percentual = (novo - inicial) / inicial \xd7 100.\n\
- +10% e depois -10% n\xe3o volta ao valor inicial.\n\
@F Aumento e desconto|novo = a \xd7 (1 \xb1 p / 100)|a: valor inicial;p: percentagem|+ para aumento, - para\
 desconto|50 \u20ac com 20% de desconto: 40 \u20ac|c_mprp.perc\n\
@F Varia\xe7\xe3o percentual|(b - a) / a \xd7 100|a: valor inicial;b: valor final|a \u2260 0|de 80 para 92:\
 +15%|c_mprp.perc\n\
@F\n\
Dados: uns t\xe9nis custam 80 \u20ac e t\xeam 15% de desconto.\n\
Objetivo: pre\xe7o com desconto e percentagem que se poupa em euros.\n\
1. Fator: 1 - 0,15 = 0,85.\n\
2. Pre\xe7o: 80 \xd7 0,85 = 68 \u20ac.\n\
3. Poupan\xe7a: 80 - 68 = 12 \u20ac, que \xe9 15% de 80.\n\
> Pagam-se 68 \u20ac.\n\
Verifica\xe7\xe3o: 0,15 \xd7 80 = 12 \u2713.\n\
@J\n\
Um pre\xe7o passou de 40 \u20ac para 50 \u20ac. Qual foi o aumento percentual?\n\
@R\n\
(50 - 40) / 40 \xd7 100 = 25%.\n\
@E 1|a7e1|Padr\xe3o com f\xf3sforos|c_mprp.seq|a7a\n\
Enunciado: com f\xf3sforos fazem-se quadrados lado a lado: 1 quadrado usa 4 f\xf3sforos, 2 usam 7 e 3 usam\
 10. Quantos f\xf3sforos s\xe3o precisos para 25 quadrados?\n\
Resolu\xe7\xe3o:\n\
1. A diferen\xe7a \xe9 constante: 7 - 4 = 10 - 7 = 3.\n\
2. u(n) = 3n + (4 - 3), ou seja, u(n) = 3n + 1.\n\
3. u(25) = 3 \xd7 25 + 1 = 76\n\
Resultado: 76 f\xf3sforos.\n\
Interpreta\xe7\xe3o: cada quadrado novo acrescenta 3 f\xf3sforos ao primeiro.\n\
Erros a evitar: multiplicar 25 por 4 (os lados comuns contam uma s\xf3 vez).\n\
@E 2|a7e2|Equa\xe7\xe3o com o dobro e o triplo|c_mexp.eq1|a7c\n\
Enunciado: a Ana tem o triplo da idade do irm\xe3o. Daqui a 6 anos ter\xe1 o dobro. Que idades t\xeam?\n\
Resolu\xe7\xe3o:\n\
1. Irm\xe3o: x anos; Ana: 3x anos.\n\
2. Daqui a 6 anos: 3x + 6 = 2(x + 6).\n\
3. 3x + 6 = 2x + 12, logo x = 6.\n\
4. A Ana tem 3 \xd7 6 = 18 anos.\n\
Resultado: o irm\xe3o tem 6 anos e a Ana 18.\n\
Interpreta\xe7\xe3o: daqui a 6 anos, 24 = 2 \xd7 12 \u2713.\n\
Erros a evitar: somar 6 s\xf3 a uma das idades.\n\
@E 3|a7e3|Dois descontos seguidos|c_mprp.perc|a7e\n\
Enunciado: um casaco de 120 \u20ac tem 20% de desconto e, na caixa, mais 10% sobre o novo pre\xe7o. Qual \xe9\
 o desconto total, em percentagem?\n\
Resolu\xe7\xe3o:\n\
1. Fator total: 0,80 \xd7 0,90 = 0,72.\n\
2. Pre\xe7o final: 120 \xd7 0,72 = 86,40 \u20ac.\n\
3. Desconto total: 1 - 0,72 = 0,28, ou seja, 28%.\n\
Resultado: 28% de desconto (e n\xe3o 30%).\n\
Interpreta\xe7\xe3o: o 2.\xba desconto aplica-se a um pre\xe7o j\xe1 mais baixo.\n\
Erros a evitar: somar as percentagens (20% + 10%).\n\
"
