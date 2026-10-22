# p_m6.py - M1TR4M: Fun\xe7\xf5es definidas por ramos e fun\xe7\xe3o m\xf3dulo (gerado pelo build).
D = "@V 1\n\
@N 3\n\
@T Fun\xe7\xf5es definidas por ramos e fun\xe7\xe3o m\xf3dulo\n\
@L m6a|Fun\xe7\xf5es definidas por ramos|funcao definida por ramos ramo fronteira intervalo imagem grafico\
 salto continuidade equacao ramo a ramo tarifario|c_matf.ramos|10|n\xfacleo|m4b:Estudo de uma fun\xe7\xe3o:\
 zeros, sinal, monotonia e extremos||AE Mat A 10.\xba, Fun\xe7\xf5es (fun\xe7\xf5es definidas por ramos)\n\
@A\n\
- Ler fun\xe7\xf5es definidas por ramos.\n\
- Calcular imagens escolhendo o ramo certo.\n\
- Esbo\xe7ar o gr\xe1fico e estudar zeros e sinal.\n\
- Resolver equa\xe7\xf5es ramo a ramo.\n\
@B\n\
Num tarif\xe1rio, at\xe9 um certo consumo paga-se um pre\xe7o e acima dele outro.\n\
A conta \xe9 uma fun\xe7\xe3o com dois ramos.\n\
@C\n\
- Fun\xe7\xe3o por ramos: express\xf5es diferentes em intervalos diferentes.\n\
- Para calcular f(a), v\xea-se primeiro a que intervalo pertence a.\n\
- Nas fronteiras, s\xf3 um ramo se aplica: aten\xe7\xe3o a < e a \u2264.\n\
- O gr\xe1fico junta os gr\xe1ficos de cada ramo, s\xf3 nos seus intervalos.\n\
- Equa\xe7\xf5es: resolve-se ramo a ramo e s\xf3 valem as solu\xe7\xf5es do intervalo.\n\
@D\n\
Exemplo: f(x) = x + 1 se x < 1; f(x) = 5 - x se 1 \u2264 x < 3; f(x) = 2 se x \u2265 3.\n\
f(0) = 1; f(1) = 5 - 1 = 4; f(3) = 2.\n\
Em x = 1 h\xe1 um salto: \xe0 esquerda os valores aproximam-se de 2, mas f(1) = 4.\n\
Zeros, ramo a ramo:\n\
- x + 1 = 0 \u21d4 x = -1, e -1 < 1: serve.\n\
- 5 - x = 0 \u21d4 x = 5, mas 5 n\xe3o est\xe1 em [1, 3[: n\xe3o serve.\n\
- O ramo constante 2 n\xe3o tem zeros.\n\
O \xfanico zero \xe9 -1.\n\
No gr\xe1fico, nas fronteiras marca-se bola cheia no ramo a que o ponto pertence e bola vazia no outro.\n\
@F Fun\xe7\xe3o definida por ramos|f(x) = f1(x) se x < a; f(x) = f2(x) se x \u2265 a|f1 e f2: express\xf5es\
 de cada ramo;a: fronteira|cada x pertence a um s\xf3 ramo|-x se x < 0 e x\xb2 se x \u2265 0: f(-3) = 3|c_matf.ramos\n\
@F\n\
Dados: f(x) = -x se x < 0 e f(x) = x\xb2 se x \u2265 0.\n\
Objetivo: f(-3), f(2) e as solu\xe7\xf5es de f(x) = 4.\n\
1. f(-3) = 3 (1.\xba ramo); f(2) = 4 (2.\xba ramo)\n\
2. 1.\xba ramo: -x = 4 \u21d4 x = -4, e -4 < 0: serve.\n\
3. 2.\xba ramo: x\xb2 = 4 \u21d4 x = -2 \u2228 x = 2; s\xf3 x = 2 est\xe1 em [0, +\u221e[.\n\
> f(-3) = 3, f(2) = 4 e f(x) = 4 \u21d4 x \u2208 {-4, 2}.\n\
Verifica\xe7\xe3o: f(-4) = 4 e f(2) = 4.\n\
@G\n\
O mesmo valor de x nunca pode estar em dois ramos: sen\xe3o teria duas imagens.\n\
@H\n\
- Usar o ramo errado numa fronteira.\n\
- Aceitar solu\xe7\xf5es fora do intervalo do ramo.\n\
- Desenhar cada ramo em todo o eixo dos x.\n\
- Esquecer as bolas abertas e fechadas nas fronteiras.\n\
@I\n\
- Primeiro o ramo, depois a conta.\n\
- Fronteiras: cuidado com < e \u2264.\n\
- Equa\xe7\xf5es: ramo a ramo, confirmando o intervalo.\n\
@J\n\
Com f(x) = 2x se x \u2264 1 e f(x) = 3 se x > 1, quanto vale f(1)?\n\
@R\n\
f(1) = 2 \xd7 1 = 2: o 1 pertence ao 1.\xba ramo.\n\
@L m6b|Fun\xe7\xe3o m\xf3dulo|modulo valor absoluto distancia funcao modulo vertice ramos equacao com modulo\
 inequacao com modulo contradominio|c_matf.mod|10|n\xfacleo|m6a:Fun\xe7\xf5es definidas por ramos||AE Mat A\
 10.\xba, Fun\xe7\xf5es (fun\xe7\xe3o m\xf3dulo); caderno de atividades\n\
@A\n\
- Definir o m\xf3dulo de um n\xfamero e a fun\xe7\xe3o m\xf3dulo.\n\
- Escrever a|x - h| + k por ramos.\n\
- Determinar v\xe9rtice, contradom\xednio, monotonia e zeros.\n\
- Resolver equa\xe7\xf5es e inequa\xe7\xf5es simples com m\xf3dulo.\n\
@B\n\
O m\xf3dulo \xe9 a dist\xe2ncia a zero na reta: |-3| = |3| = 3.\n\
|x - h| \xe9 a dist\xe2ncia de x a h.\n\
@C\n\
- |x| = x se x \u2265 0 e |x| = -x se x < 0.\n\
- f(x) = a|x - h| + k: gr\xe1fico em \"V\" com v\xe9rtice (h, k).\n\
- a > 0: abre para cima, m\xednimo k; a < 0: abre para baixo, m\xe1ximo k.\n\
- |x - 6| = x - 6 se x \u2265 6 e |x - 6| = -x + 6 se x < 6.\n\
- |x - h| = d (d > 0) \u21d4 x = h - d \u2228 x = h + d.\n\
@D\n\
Exemplo: f(x) = -4|x| + 2.\n\
Ramos: -4x + 2 se x \u2265 0 e 4x + 2 se x < 0.\n\
V\xe9rtice (0, 2); m\xe1ximo 2; D\u2032f = ]-\u221e, 2].\n\
Zeros: 4|x| = 2 \u21d4 |x| = 0,5 \u21d4 x = -0,5 \u2228 x = 0,5.\n\
|x - h| < d \u21d4 h - d < x < h + d (pontos a menos de d de h).\n\
|x - h| > d \u21d4 x < h - d \u2228 x > h + d.\n\
Exemplo: |x - 6| < 3 \u21d4 6 - 3 < x < 6 + 3: C.S. = ]3, 9[.\n\
Se d < 0, |x - h| = d \xe9 imposs\xedvel: um m\xf3dulo nunca \xe9 negativo.\n\
@F M\xf3dulo|\u2223x\u2223 = x se x \u2265 0; \u2223x\u2223 = -x se x < 0|\u2223x\u2223: dist\xe2ncia de x a\
 0|x real|\u2223-3\u2223 = 3|\n\
@F Fun\xe7\xe3o m\xf3dulo|f(x) = a\u2223x - h\u2223 + k|(h, k): v\xe9rtice;a: abertura e sentido|a \u2260\
 0|-4\u2223x\u2223 + 2: v\xe9rtice (0, 2)|c_matf.mod\n\
@F Equa\xe7\xe3o com m\xf3dulo|\u2223x - h\u2223 = d \u21d4 x = h - d \u2228 x = h + d|d: dist\xe2ncia a h|d\
 > 0 (d = 0: s\xf3 x = h)|\u2223x - 2\u2223 = 5: x = -3 \u2228 x = 7|c_matf.mod\n\
@F\n\
Dados: f(x) = 2|x + 1| - 4.\n\
Objetivo: v\xe9rtice, zeros e C.S. de f(x) > 2.\n\
1. V\xe9rtice: (-1, -4); a = 2 > 0, logo o m\xednimo \xe9 -4.\n\
2. Zeros: 2|x + 1| = 4 \u21d4 |x + 1| = 2 \u21d4 x = -3 \u2228 x = 1.\n\
3. f(x) > 2 \u21d4 |x + 1| > 3 \u21d4 x < -4 \u2228 x > 2.\n\
> Zeros -3 e 1; f(x) > 2 em ]-\u221e, -4[ \u222a ]2, +\u221e[.\n\
Verifica\xe7\xe3o: f(1) = 2 \xd7 2 - 4 = 0.\n\
@G\n\
O m\xf3dulo mede dist\xe2ncias: por isso aparece em erros, toler\xe2ncias e intervalos centrados num valor.\n\
@H\n\
- Escrever |x - 6| = x + 6.\n\
- Esquecer a segunda solu\xe7\xe3o de |x - h| = d.\n\
- Resolver |x| = -2 e dar solu\xe7\xf5es.\n\
- Trocar \"dentro\" (<) com \"fora\" (>) nas inequa\xe7\xf5es.\n\
@I\n\
- |x| \xe9 a dist\xe2ncia a 0.\n\
- a|x - h| + k: v\xe9rtice (h, k).\n\
- |x - h| = d \u21d4 x = h \xb1 d.\n\
- < d: dentro; > d: fora.\n\
@J\n\
Resolve a equa\xe7\xe3o |x - 2| = 5.\n\
@R\n\
x - 2 = -5 \u2228 x - 2 = 5 \u21d4 x = -3 \u2228 x = 7.\n\
@L m6c|Ch\xe3o, teto, sinal e Heaviside (aprofundamento)|parte inteira chao teto funcao sinal heaviside\
 funcao em escada arredondamento estacionamento hora comecada||10|aprofundamento|m6a:Fun\xe7\xf5es definidas\
 por ramos||AE Mat A 10.\xba, Fun\xe7\xf5es (aprofundamento)\n\
@A\n\
- Conhecer as fun\xe7\xf5es ch\xe3o (parte inteira) e teto.\n\
- Conhecer as fun\xe7\xf5es sinal e de Heaviside.\n\
- Reconhecer gr\xe1ficos em escada.\n\
@B\n\
Num parque que cobra por hora come\xe7ada, 1 h 10 min paga-se como 2 h: \xe9 a fun\xe7\xe3o teto.\n\
@C\n\
- Ch\xe3o (parte inteira), ch\xe3o(x): o maior inteiro menor ou igual a x.\n\
- Teto, teto(x): o menor inteiro maior ou igual a x.\n\
- Sinal: sgn(x) = -1 se x < 0; 0 se x = 0; 1 se x > 0.\n\
- Heaviside: H(x) = 0 se x < 0 e H(x) = 1 se x \u2265 0.\n\
- S\xe3o fun\xe7\xf5es por ramos com gr\xe1ficos em escada.\n\
@D\n\
ch\xe3o(2,7) = 2 e ch\xe3o(-2,7) = -3.\n\
teto(2,1) = 3 e teto(-2,1) = -2.\n\
Para inteiros, ch\xe3o e teto coincidem: ch\xe3o(4) = teto(4) = 4.\n\
Estacionamento a 1,20 \u20ac por hora come\xe7ada, durante 2 h 15 min:\n\
1,20 \xd7 teto(2,25) = 1,20 \xd7 3 = 3,6 \u20ac.\n\
sgn(-5) = -1 e H(0) = 1.\n\
@F Ch\xe3o (parte inteira)|ch\xe3o(x) = maior inteiro menor ou igual a x|x real|gr\xe1fico em\
 escada|ch\xe3o(-2,7) = -3|\n\
@F Teto|teto(x) = menor inteiro maior ou igual a x|x real|gr\xe1fico em escada|teto(2,1) = 3|\n\
@F\n\
Dados: um parque cobra 1,20 \u20ac por hora come\xe7ada.\n\
Objetivo: pre\xe7o para 50 min e para 3 h 5 min.\n\
1. 50 min: teto(50 / 60) = 1 hora, ou seja, 1,20 \u20ac.\n\
2. 3 h 5 min: teto(3 + 5 / 60) = 4 horas: 4 \xd7 1,20 = 4,8 \u20ac.\n\
> Paga 1,20 \u20ac e 4,80 \u20ac.\n\
Verifica\xe7\xe3o: 3 h exatas pagariam 3 \xd7 1,20 = 3,6 \u20ac.\n\
@G\n\
Estas fun\xe7\xf5es aparecem em pre\xe7os por escal\xf5es e em programa\xe7\xe3o (arredondamentos).\n\
@H\n\
- Achar que ch\xe3o(-2,7) = -2 (\xe9 -3).\n\
- Confundir ch\xe3o com arredondamento ao inteiro mais pr\xf3ximo.\n\
- Esquecer que H(0) = 1 com esta defini\xe7\xe3o.\n\
@I\n\
- ch\xe3o: arredonda para baixo; teto: para cima.\n\
- sgn d\xe1 -1, 0 ou 1.\n\
- H: 0 antes de 0, 1 a partir de 0.\n\
@J\n\
Calcula ch\xe3o(-0,5) e teto(-0,5).\n\
@R\n\
ch\xe3o(-0,5) = -1 e teto(-0,5) = 0.\n\
@E 1|m6e1|Imagens numa fun\xe7\xe3o por ramos|c_matf.ramos|m6a\n\
Enunciado: f(x) = 3 - x se x < 2 e f(x) = x\xb2 - 3 se x \u2265 2. Calcula f(0), f(2) e f(4).\n\
Resolu\xe7\xe3o:\n\
1. 0 < 2: f(0) = 3 - 0 = 3\n\
2. 2 \u2265 2: f(2) = 4 - 3 = 1\n\
3. 4 \u2265 2: f(4) = 16 - 3 = 13\n\
Resultado: f(0) = 3, f(2) = 1 e f(4) = 13.\n\
Interpreta\xe7\xe3o: em x = 2 os dois ramos d\xe3o 1: o gr\xe1fico n\xe3o tem salto.\n\
Erros a evitar: usar o 1.\xba ramo em x = 2.\n\
@E 2|m6e2|Equa\xe7\xe3o com m\xf3dulo|c_matf.mod|m6b\n\
Enunciado: resolve 3|x - 1| - 2 = 7.\n\
Resolu\xe7\xe3o:\n\
1. 3|x - 1| = 9 \u21d4 |x - 1| = 3\n\
2. x - 1 = -3 \u2228 x - 1 = 3\n\
3. x = -2 \u2228 x = 4\n\
Resultado: C.S. = {-2, 4}.\n\
Interpreta\xe7\xe3o: os dois valores est\xe3o \xe0 dist\xe2ncia 3 de 1.\n\
Erros a evitar: tirar o m\xf3dulo antes de isolar |x - 1|.\n\
@E 3|m6e3|Tarif\xe1rio da \xe1gua por escal\xf5es|c_matf.ramos|m6a\n\
Enunciado: at\xe9 5 m\xb3 a \xe1gua custa 0,50 \u20ac por m\xb3; o que passar de 5 m\xb3 custa 1,20 \u20ac por m\xb3.\n\
Escreve o custo c(x) para x m\xb3 e calcula c(8) e o consumo com custo de 7,30 \u20ac.\n\
Resolu\xe7\xe3o:\n\
1. c(x) = 0,5x se 0 \u2264 x \u2264 5; c(x) = 2,5 + 1,2(x - 5) se x > 5.\n\
2. c(8) = 2,5 + 1,2 \xd7 3 = 6,1 \u20ac\n\
3. 7,30 > 2,50, logo \xe9 o 2.\xba ramo: 2,5 + 1,2(x - 5) = 7,3 \u21d4 x = 9 m\xb3\n\
Resultado: c(8) = 6,10 \u20ac e o custo de 7,30 \u20ac corresponde a 9 m\xb3.\n\
Interpreta\xe7\xe3o: os ramos ligam-se em x = 5 (c(5) = 2,5 \u20ac nos dois).\n\
Erros a evitar: aplicar 1,20 \u20ac a todos os m\xb3.\n\
"
