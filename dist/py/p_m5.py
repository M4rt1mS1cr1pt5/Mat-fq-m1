# p_m5.py - M1TR4M: Fun\xe7\xe3o quadr\xe1tica (gerado pelo build).
D = "@V 1\n\
@N 4\n\
@T Fun\xe7\xe3o quadr\xe1tica\n\
@L m5a|A fun\xe7\xe3o quadr\xe1tica e o seu gr\xe1fico|funcao quadratica parabola concavidade vertice eixo de\
 simetria forma canonica a(x-h)^2+k|c_matq.q2|10|n\xfacleo||f1a:Energia cin\xe9tica, potencial grav\xedtica e\
 mec\xe2nica|AE Mat A 10.\xba, Fun\xe7\xf5es: fun\xe7\xe3o quadr\xe1tica\n\
@A\n\
- Reconhecer uma fun\xe7\xe3o quadr\xe1tica f(x) = ax\xb2 + bx + c, com a \u2260 0.\n\
- Relacionar o sinal de a com a concavidade da par\xe1bola.\n\
- Determinar o v\xe9rtice e o eixo de simetria.\n\
- Escrever f na forma can\xf3nica a(x - h)\xb2 + k.\n\
- Obter o gr\xe1fico a partir do de y = x\xb2.\n\
@B\n\
O gr\xe1fico de uma fun\xe7\xe3o quadr\xe1tica \xe9 uma par\xe1bola, como o jato de \xe1gua de uma fonte.\n\
Se a > 0, abre para cima, como um sorriso; se a < 0, abre para baixo. O v\xe9rtice \xe9 o ponto mais baixo\
 (ou mais alto). A par\xe1bola \xe9 sim\xe9trica em rela\xe7\xe3o a uma reta vertical: o eixo.\n\
@C\n\
- Fun\xe7\xe3o quadr\xe1tica: f(x) = ax\xb2 + bx + c, com a, b, c \u2208 \u211d e a \u2260 0.\n\
- Df = \u211d. O gr\xe1fico chama-se par\xe1bola.\n\
- Forma can\xf3nica: f(x) = a(x - h)\xb2 + k.\n\
- V\xe9rtice: V(h, k). Eixo de simetria: x = h.\n\
- a > 0: concavidade voltada para cima; k \xe9 o m\xednimo.\n\
- a < 0: concavidade voltada para baixo; k \xe9 o m\xe1ximo.\n\
- Na forma geral: h = -b/(2a) e k = f(h).\n\
@D\n\
Parte-se do gr\xe1fico de y = x\xb2, com v\xe9rtice em (0, 0).\n\
y = ax\xb2 estica (|a| > 1) ou encolhe (0 < |a| < 1) na vertical.\n\
Se a < 0, h\xe1 tamb\xe9m reflex\xe3o no eixo Ox.\n\
y = a(x - h)\xb2 + k \xe9 y = ax\xb2 transladada.\n\
A transla\xe7\xe3o leva o v\xe9rtice de (0, 0) para (h, k).\n\
Exemplo: f(x) = 2(x - 1)\xb2 + 3.\n\
Tem v\xe9rtice V(1, 3) e eixo x = 1.\n\
Como a = 2 > 0, o m\xednimo \xe9 3.\n\
Para passar da forma geral \xe0 can\xf3nica, calcula-se h e k.\n\
Exemplo: f(x) = x\xb2 - 4x + 1.\n\
h = -(-4)/(2 \xd7 1) = 2 e k = f(2) = 4 - 8 + 1 = -3.\n\
Logo f(x) = (x - 2)\xb2 - 3.\n\
Aten\xe7\xe3o ao sinal: (x - 2)\xb2 d\xe1 h = 2 e (x + 2)\xb2 d\xe1 h = -2.\n\
@F Forma can\xf3nica|f(x) = a(x - h)\xb2 + k|a: abertura e concavidade (a \u2260 0);(h, k): v\xe9rtice da\
 par\xe1bola|qualquer fun\xe7\xe3o quadr\xe1tica|f(x) = 2(x - 1)\xb2 + 3 tem v\xe9rtice (1, 3)|c_matq.q2\n\
@F Abcissa do v\xe9rtice|h = -b / (2a)|a, b: coeficientes de f(x) = ax\xb2 + bx + c|a \u2260 0|f(x) = x\xb2 -\
 4x + 1: h = 2|c_matq.q2\n\
@F Ordenada do v\xe9rtice|k = f(h) = c - b\xb2 / (4a)|h: abcissa do v\xe9rtice;a, b, c: coeficientes|a \u2260\
 0|f(x) = x\xb2 - 4x + 1: k = -3|c_matq.q2\n\
@F\n\
Dados: f(x) = -2x\xb2 + 8x - 5.\n\
Objetivo: v\xe9rtice, eixo, concavidade e forma can\xf3nica.\n\
1. a = -2, b = 8, c = -5.\n\
2. h = -8 / (2 \xd7 (-2)) = 2\n\
3. k = f(2) = -2 \xd7 4 + 16 - 5 = 3\n\
4. V\xe9rtice V(2, 3); eixo de simetria x = 2.\n\
5. a < 0: concavidade voltada para baixo; m\xe1ximo 3.\n\
> f(x) = -2(x - 2)\xb2 + 3\n\
Verifica\xe7\xe3o: f(0) = -2 \xd7 4 + 3 = -5, igual a c.\n\
@G\n\
A forma can\xf3nica mostra logo o v\xe9rtice.\n\
A forma geral mostra logo a ordenada na origem, c.\n\
O m\xe1ximo ou o m\xednimo de uma grandeza est\xe1 no v\xe9rtice.\n\
Exemplos: altura m\xe1xima de um lan\xe7amento, \xe1rea m\xe1xima de um terreno.\n\
@H\n\
- Ler h com o sinal trocado: em (x + 3)\xb2, h = -3.\n\
- Esquecer o a ao calcular k = f(h).\n\
- Achar que a > 0 d\xe1 um m\xe1ximo: d\xe1 um m\xednimo.\n\
- Dizer que o eixo de simetria \xe9 y = h: \xe9 x = h.\n\
- Esquecer que a = 0 n\xe3o d\xe1 uma fun\xe7\xe3o quadr\xe1tica.\n\
@I\n\
- f(x) = ax\xb2 + bx + c, com a \u2260 0; gr\xe1fico: par\xe1bola.\n\
- Forma can\xf3nica a(x - h)\xb2 + k; v\xe9rtice (h, k).\n\
- Eixo de simetria: x = h, com h = -b/(2a).\n\
- a > 0: concavidade para cima e m\xednimo k.\n\
- a < 0: concavidade para baixo e m\xe1ximo k.\n\
@J\n\
Determina o v\xe9rtice de f(x) = x\xb2 + 6x + 5.\n\
@R\n\
h = -6 / (2 \xd7 1) = -3; k = f(-3) = 9 - 18 + 5 = -4.\n\
V\xe9rtice: V(-3, -4).\n\
@L m5b|Zeros e f\xf3rmula resolvente|zeros equacao do 2.o grau formula resolvente discriminante delta binomio\
 discriminante fatorizacao|c_matq.q2|10|n\xfacleo|m5a:A fun\xe7\xe3o quadr\xe1tica e o seu\
 gr\xe1fico;a9b:Equa\xe7\xf5es do 2.\xba grau||AE Mat A 10.\xba, Fun\xe7\xf5es: fun\xe7\xe3o quadr\xe1tica\n\
@A\n\
- Calcular o discriminante \u0394 = b\xb2 - 4ac.\n\
- Relacionar o sinal de \u0394 com o n\xfamero de zeros.\n\
- Resolver equa\xe7\xf5es do 2.\xba grau com a f\xf3rmula resolvente.\n\
- Resolver equa\xe7\xf5es incompletas sem a f\xf3rmula.\n\
- Fatorizar ax\xb2 + bx + c usando os zeros.\n\
@B\n\
Os zeros s\xe3o os pontos onde a par\xe1bola corta o eixo Ox.\n\
Uma par\xe1bola pode cort\xe1-lo duas vezes, toc\xe1-lo uma vez, ou n\xe3o o tocar.\n\
O discriminante diz qual destes casos acontece.\n\
A f\xf3rmula resolvente d\xe1 os zeros em qualquer caso.\n\
@C\n\
- Equa\xe7\xe3o do 2.\xba grau: ax\xb2 + bx + c = 0, com a \u2260 0.\n\
- Discriminante: \u0394 = b\xb2 - 4ac.\n\
- F\xf3rmula resolvente: x = (-b \xb1 \u221a\u0394) / (2a).\n\
- \u0394 > 0: dois zeros diferentes.\n\
- \u0394 = 0: um zero (duplo), que \xe9 a abcissa do v\xe9rtice.\n\
- \u0394 < 0: n\xe3o h\xe1 zeros; a equa\xe7\xe3o \xe9 imposs\xedvel em \u211d.\n\
- Fatoriza\xe7\xe3o (\u0394 \u2265 0): ax\xb2 + bx + c = a(x - x\u2081)(x - x\u2082).\n\
@D\n\
Exemplo: x\xb2 - 5x + 6 = 0.\n\
\u0394 = 25 - 24 = 1, logo h\xe1 dois zeros.\n\
x = (5 \xb1 1) / 2, ou seja, x = 2 \u2228 x = 3.\n\
C.S. = {2, 3}.\n\
Equa\xe7\xf5es incompletas resolvem-se mais depressa:\n\
- c = 0: x(ax + b) = 0, logo x = 0 \u2228 x = -b/a.\n\
- b = 0: x\xb2 = -c/a, que s\xf3 tem solu\xe7\xe3o se -c/a \u2265 0.\n\
Exemplo: 2x\xb2 - 8 = 0 d\xe1 x\xb2 = 4, logo x = -2 \u2228 x = 2.\n\
Exemplo: 3x\xb2 + 6x = 0 d\xe1 3x(x + 2) = 0, logo x = 0 \u2228 x = -2.\n\
Quando \u221a\u0394 n\xe3o \xe9 inteira, deixa-se a forma exata.\n\
Exemplo: x\xb2 - 2x - 1 = 0 d\xe1 x = 1 - \u221a2 \u2228 x = 1 + \u221a2.\n\
A soma dos zeros \xe9 -b/a e o produto \xe9 c/a.\n\
@F Discriminante|\u0394 = b\xb2 - 4ac|a, b, c: coeficientes de ax\xb2 + bx + c|a \u2260 0|x\xb2 - 5x + 6:\
 \u0394 = 25 - 24 = 1|c_matq.q2\n\
@F F\xf3rmula resolvente|x = (-b \xb1 \u221a\u0394) / (2a)|\u0394: discriminante;a, b: coeficientes|\u0394\
 \u2265 0 (sen\xe3o n\xe3o h\xe1 zeros)|x\xb2 - 5x + 6 = 0: x = (5 \xb1 1)/2|c_matq.q2\n\
@F Fatoriza\xe7\xe3o|ax\xb2 + bx + c = a(x - x\u2081)(x - x\u2082)|x\u2081, x\u2082: zeros (iguais se \u0394\
 = 0)|\u0394 \u2265 0|x\xb2 - 5x + 6 = (x - 2)(x - 3)|c_matq.q2\n\
@F\n\
Dados: 2x\xb2 - 5x + 2 = 0.\n\
Objetivo: resolver a equa\xe7\xe3o.\n\
1. a = 2, b = -5, c = 2.\n\
2. \u0394 = (-5)\xb2 - 4 \xd7 2 \xd7 2 = 9\n\
3. \u0394 > 0: h\xe1 dois zeros.\n\
4. x = (5 \xb1 3) / 4\n\
5. x = 2/4 = 1/2 \u2228 x = 8/4 = 2\n\
> C.S. = {1/2, 2}\n\
Verifica\xe7\xe3o: 2 \xd7 (1/2)\xb2 - 5 \xd7 1/2 + 2 = 0.\n\
@G\n\
O sinal de \u0394 resume a posi\xe7\xe3o da par\xe1bola face ao eixo Ox.\n\
\u0394 = 0 quer dizer que o v\xe9rtice est\xe1 em cima do eixo.\n\
Num problema, cada zero tem de fazer sentido no contexto.\n\
Um tempo ou um comprimento negativo rejeita-se.\n\
@H\n\
- Esquecer o sinal de b: com b = -5, -b = 5.\n\
- Dividir s\xf3 \u221a\u0394 por 2a, e n\xe3o -b \xb1 \u221a\u0394.\n\
- Escrever \u221a\u0394 com \u0394 negativo.\n\
- Usar a f\xf3rmula com a equa\xe7\xe3o por igualar a zero.\n\
- Perder solu\xe7\xf5es ao dividir por x: fatoriza em vez disso.\n\
@I\n\
- \u0394 = b\xb2 - 4ac.\n\
- \u0394 > 0: 2 zeros; \u0394 = 0: 1 zero; \u0394 < 0: nenhum.\n\
- x = (-b \xb1 \u221a\u0394) / (2a).\n\
- Incompletas: fatorizar (c = 0) ou isolar x\xb2 (b = 0).\n\
- Fatoriza\xe7\xe3o: a(x - x\u2081)(x - x\u2082).\n\
- Deixa a forma exata quando \u221a\u0394 n\xe3o \xe9 inteira.\n\
@J\n\
Resolve x\xb2 - 6x + 5 = 0.\n\
@R\n\
\u0394 = 36 - 20 = 16; x = (6 \xb1 4) / 2.\n\
x = 1 \u2228 x = 5. C.S. = {1, 5}.\n\
@L m5c|Sinal, monotonia, extremos e inequa\xe7\xf5es|sinal monotonia crescente decrescente maximo minimo\
 extremo contradominio inequacao do 2.o grau conjunto-solucao|c_matq.iq|10|n\xfacleo|m5b:Zeros e f\xf3rmula\
 resolvente|af21:AL 2.1 Caracter\xedsticas de uma pilha|AE Mat A 10.\xba, Fun\xe7\xf5es: fun\xe7\xe3o quadr\xe1tica\n\
@A\n\
- Estudar o sinal de uma fun\xe7\xe3o quadr\xe1tica.\n\
- Indicar intervalos de monotonia e o extremo.\n\
- Indicar o contradom\xednio.\n\
- Resolver inequa\xe7\xf5es do 2.\xba grau.\n\
- Escrever o conjunto-solu\xe7\xe3o com intervalos.\n\
@B\n\
O sinal diz onde a par\xe1bola est\xe1 acima ou abaixo do eixo Ox.\n\
A monotonia diz onde sobe e onde desce.\n\
Tudo depende de duas coisas: a concavidade e os zeros.\n\
Um esbo\xe7o r\xe1pido resolve quase tudo.\n\
@C\n\
- f \xe9 positiva onde o gr\xe1fico est\xe1 acima de Ox; negativa abaixo.\n\
- Com a > 0: f decresce em ]-\u221e, h] e cresce em [h, +\u221e[.\n\
- Com a > 0: m\xednimo k e D'f = [k, +\u221e[.\n\
- Com a < 0: f cresce em ]-\u221e, h], decresce em [h, +\u221e[.\n\
- Com a < 0: m\xe1ximo k e D'f = ]-\u221e, k].\n\
- Inequa\xe7\xe3o do 2.\xba grau: ax\xb2 + bx + c > 0 (ou \u2265, <, \u2264).\n\
@D\n\
M\xe9todo para resolver uma inequa\xe7\xe3o:\n\
1. Passa tudo para um membro: ax\xb2 + bx + c ? 0.\n\
2. Calcula os zeros.\n\
3. Esbo\xe7a a par\xe1bola com a concavidade certa.\n\
4. L\xea onde o gr\xe1fico est\xe1 acima (> 0) ou abaixo (< 0).\n\
Exemplo: x\xb2 - 5x + 6 \u2264 0.\n\
Zeros 2 e 3; a = 1 > 0, a par\xe1bola abre para cima.\n\
Fica abaixo do eixo entre os zeros.\n\
C.S. = [2, 3] (fechado, porque \u2264 inclui os zeros).\n\
Exemplo: -x\xb2 + 4 > 0.\n\
Zeros -2 e 2; a = -1 < 0, abre para baixo.\n\
Fica acima do eixo entre os zeros: C.S. = ]-2, 2[.\n\
Sem zeros, o sinal \xe9 sempre o de a.\n\
Exemplo: x\xb2 + 1 > 0 \xe9 verdade para todo o x: C.S. = \u211d.\n\
E x\xb2 + 1 < 0 nunca acontece: C.S. = \u2205.\n\
@F Sinal com dois zeros (a > 0)|f(x) > 0 em ]-\u221e, x\u2081[ \u222a ]x\u2082, +\u221e[; f(x) < 0 em\
 ]x\u2081, x\u2082[|x\u2081 < x\u2082: zeros|a > 0 (com a < 0 os sinais trocam)|x\xb2 - 5x + 6 < 0 em ]2, 3[|c_matq.iq\n\
@F Contradom\xednio|a > 0: D'f = [k, +\u221e[; a < 0: D'f = ]-\u221e, k]|k: ordenada do\
 v\xe9rtice|fun\xe7\xe3o quadr\xe1tica com Df = \u211d|f(x) = (x - 1)\xb2 + 2: D'f = [2, +\u221e[|c_matq.q2\n\
@F\n\
Dados: inequa\xe7\xe3o x\xb2 + 2x - 3 > 0.\n\
Objetivo: conjunto-solu\xe7\xe3o.\n\
1. \u0394 = 4 + 12 = 16\n\
2. x = (-2 \xb1 4) / 2, logo x = -3 \u2228 x = 1\n\
3. a = 1 > 0: par\xe1bola com concavidade para cima.\n\
4. Est\xe1 acima do eixo fora dos zeros.\n\
> C.S. = ]-\u221e, -3[ \u222a ]1, +\u221e[\n\
Verifica\xe7\xe3o: x = 2 d\xe1 4 + 4 - 3 = 5 > 0 (est\xe1 no C.S.).\n\
E x = 0 d\xe1 -3 < 0 (n\xe3o est\xe1 no C.S.).\n\
@G\n\
As inequa\xe7\xf5es respondem a perguntas como \"quando \xe9 que o lucro \xe9 positivo?\".\n\
O v\xe9rtice d\xe1 o lucro m\xe1ximo; os zeros d\xe3o os limites.\n\
Se o sinal for \u2265 ou \u2264, os zeros entram no conjunto-solu\xe7\xe3o.\n\
@H\n\
- Usar par\xeanteses retos fechados com > ou <.\n\
- Esquecer de olhar para a concavidade.\n\
- Escrever o C.S. como pontos em vez de intervalos.\n\
- Trocar o sentido da inequa\xe7\xe3o ao passar termos de membro.\n\
- Escrever ]1, -3[ em vez de ]-3, 1[: o menor vem primeiro.\n\
@I\n\
- Sinal: depende de a e dos zeros.\n\
- a > 0: negativa entre os zeros; positiva fora deles.\n\
- a < 0: positiva entre os zeros; negativa fora deles.\n\
- Extremo no v\xe9rtice: m\xednimo se a > 0, m\xe1ximo se a < 0.\n\
- Inequa\xe7\xe3o: zeros, esbo\xe7o, leitura do sinal.\n\
@J\n\
Resolve a inequa\xe7\xe3o x\xb2 - 4 \u2264 0.\n\
@R\n\
Zeros: x\xb2 = 4, logo x = -2 \u2228 x = 2.\n\
a > 0, logo a par\xe1bola est\xe1 abaixo do eixo entre os zeros.\n\
C.S. = [-2, 2].\n\
@L m5d|Transforma\xe7\xf5es de gr\xe1ficos de fun\xe7\xf5es|transformacoes translacao dilatacao contracao\
 reflexao f(x-a) f(x)+b c f(x) grafico|c_matq.tf|10|n\xfacleo|m5a:A fun\xe7\xe3o quadr\xe1tica e o seu\
 gr\xe1fico||AE Mat A 10.\xba, Fun\xe7\xf5es: transforma\xe7\xf5es f(x - a), f(x) + b e c f(x)\n\
@A\n\
- Obter o gr\xe1fico de f(x) + b a partir do de f.\n\
- Obter o gr\xe1fico de f(x - a) a partir do de f.\n\
- Obter o gr\xe1fico de c \xd7 f(x) a partir do de f.\n\
- Relacionar estas transforma\xe7\xf5es com a forma can\xf3nica.\n\
@B\n\
Transformar um gr\xe1fico \xe9 como mexer num desenho.\n\
Podes desliz\xe1-lo para cima ou para baixo, para a esquerda ou para a direita.\n\
Tamb\xe9m podes estic\xe1-lo ou encolh\xea-lo na vertical.\n\
Com um sinal menos, ele vira ao contr\xe1rio (reflex\xe3o).\n\
@C\n\
- f(x) + b: transla\xe7\xe3o vertical de b unidades.\n\
- f(x - a): transla\xe7\xe3o horizontal de a unidades (a > 0: direita; a < 0: esquerda).\n\
- c \xd7 f(x), c > 1: dilata\xe7\xe3o vertical de coeficiente c.\n\
- c \xd7 f(x), 0 < c < 1: contra\xe7\xe3o vertical de coeficiente c.\n\
- c < 0: h\xe1 tamb\xe9m reflex\xe3o no eixo Ox.\n\
- O ponto (x, y) do gr\xe1fico de f passa a (x + a, c y + b).\n\
@D\n\
Partimos de f(x) = x\xb2, com v\xe9rtice (0, 0).\n\
g(x) = x\xb2 + 3 sobe 3 unidades: v\xe9rtice (0, 3).\n\
g(x) = (x - 2)\xb2 desliza 2 para a direita: v\xe9rtice (2, 0).\n\
g(x) = (x + 2)\xb2 desliza 2 para a esquerda: (x + 2) = (x - (-2)).\n\
g(x) = 3x\xb2 fica mais \"fechada\": as ordenadas triplicam.\n\
g(x) = 0,5x\xb2 fica mais \"aberta\": as ordenadas passam a metade.\n\
g(x) = -x\xb2 \xe9 a reflex\xe3o de x\xb2 no eixo Ox.\n\
Juntando tudo: g(x) = 2(x - 1)\xb2 + 3.\n\
Primeiro dilata\xe7\xe3o de coeficiente 2.\n\
Depois transla\xe7\xe3o de 1 para a direita e 3 para cima.\n\
O v\xe9rtice passa de (0, 0) para (1, 3).\n\
Os zeros de f(x - a) s\xe3o os zeros de f somados com a.\n\
@F Transla\xe7\xe3o vertical|g(x) = f(x) + b|b > 0: para cima; b < 0: para baixo|qualquer fun\xe7\xe3o\
 f|x\xb2 + 3: v\xe9rtice (0, 3)|c_matq.tf\n\
@F Transla\xe7\xe3o horizontal|g(x) = f(x - a)|a > 0: para a direita; a < 0: para a esquerda|qualquer\
 fun\xe7\xe3o f|(x - 2)\xb2: v\xe9rtice (2, 0)|c_matq.tf\n\
@F Dilata\xe7\xe3o ou contra\xe7\xe3o vertical|g(x) = c \xd7 f(x)|c > 1: dilata\xe7\xe3o; 0 < c < 1:\
 contra\xe7\xe3o; c < 0: com reflex\xe3o em Ox|c \u2260 0|3x\xb2: as ordenadas triplicam|c_matq.tf\n\
@F\n\
Dados: o gr\xe1fico de f passa em A(1, 4).\n\
g(x) = 2 f(x - 3) - 1.\n\
Objetivo: o ponto do gr\xe1fico de g que corresponde a A.\n\
1. Transla\xe7\xe3o horizontal: x passa a 1 + 3 = 4.\n\
2. Dilata\xe7\xe3o: y passa a 2 \xd7 4 = 8.\n\
3. Transla\xe7\xe3o vertical: 8 - 1 = 7.\n\
> O ponto correspondente \xe9 (4, 7).\n\
Verifica\xe7\xe3o: g(4) = 2 f(1) - 1 = 2 \xd7 4 - 1 = 7.\n\
@G\n\
As transforma\xe7\xf5es explicam a forma can\xf3nica a(x - h)\xb2 + k.\n\
Toda a par\xe1bola \xe9 x\xb2 dilatada, refletida e transladada.\n\
O mesmo vale para outras fun\xe7\xf5es, como o m\xf3dulo |x|.\n\
@H\n\
- Achar que f(x - 2) desloca para a esquerda: desloca para a direita.\n\
- Aplicar o b dentro do par\xeantese: f(x) + b n\xe3o \xe9 f(x + b).\n\
- Multiplicar as abcissas em vez das ordenadas em c f(x).\n\
- Esquecer a reflex\xe3o quando c < 0.\n\
@I\n\
- f(x) + b: transla\xe7\xe3o vertical de b.\n\
- f(x - a): transla\xe7\xe3o horizontal de a (a > 0: direita).\n\
- c f(x): dilata\xe7\xe3o (c > 1) ou contra\xe7\xe3o (0 < c < 1); c < 0 reflete.\n\
- (x, y) passa a (x + a, c y + b).\n\
@J\n\
O gr\xe1fico de f passa em B(-2, 5).\n\
Que ponto do gr\xe1fico de g(x) = f(x + 1) + 2 lhe corresponde?\n\
@R\n\
f(x + 1) = f(x - (-1)): desloca 1 para a esquerda: -2 - 1 = -3.\n\
Sobe 2: 5 + 2 = 7. O ponto \xe9 (-3, 7).\n\
@E 1|m5e1|V\xe9rtice e eixo de uma par\xe1bola|c_matq.q2|m5a\n\
Enunciado: indica o v\xe9rtice, o eixo e a concavidade de f(x) = 3(x + 2)\xb2 - 1.\n\
Dados: forma can\xf3nica a(x - h)\xb2 + k.\n\
Objetivo: v\xe9rtice, eixo de simetria e concavidade.\n\
M\xe9todo: ler h e k; aten\xe7\xe3o ao sinal de h.\n\
Resolu\xe7\xe3o:\n\
1. x + 2 = x - (-2), logo h = -2.\n\
2. k = -1.\n\
3. a = 3 > 0: concavidade voltada para cima.\n\
Resultado: V(-2, -1); eixo x = -2; m\xednimo -1.\n\
Interpreta\xe7\xe3o: \xe9 a par\xe1bola de y = 3x\xb2 com o v\xe9rtice em (-2, -1).\n\
Erros a evitar: escrever h = 2.\n\
@E 2|m5e2|Equa\xe7\xe3o do 2.\xba grau com fra\xe7\xe3o|c_matq.q2|m5b\n\
Enunciado: resolve 3x\xb2 - 7x + 2 = 0.\n\
Dados: a = 3, b = -7, c = 2.\n\
Objetivo: conjunto-solu\xe7\xe3o.\n\
M\xe9todo: discriminante e f\xf3rmula resolvente.\n\
Resolu\xe7\xe3o:\n\
1. \u0394 = 49 - 24 = 25\n\
2. x = (7 \xb1 5) / 6\n\
3. x = 2/6 = 1/3 \u2228 x = 12/6 = 2\n\
Resultado: C.S. = {1/3, 2}.\n\
Interpreta\xe7\xe3o: a par\xe1bola corta o eixo Ox em x = 1/3 e em x = 2.\n\
Erros a evitar: dividir s\xf3 o 5 por 6.\n\
Verifica\xe7\xe3o: 3 \xd7 (1/3)\xb2 - 7 \xd7 (1/3) + 2 = 0.\n\
@E 3|m5e3|Altura m\xe1xima de um lan\xe7amento|c_matq.q2|m5c\n\
Enunciado: a altura de uma bola, em metros, \xe9 h(t) = -5t\xb2 + 20t + 1.\n\
t \xe9 o tempo, em segundos, desde o lan\xe7amento.\n\
Objetivo: altura m\xe1xima e instante em que a bola chega ao ch\xe3o.\n\
M\xe9todo: v\xe9rtice da par\xe1bola e zero positivo.\n\
Resolu\xe7\xe3o:\n\
1. t do v\xe9rtice: -20 / (2 \xd7 (-5)) = 2 s\n\
2. h(2) = -20 + 40 + 1 = 21 m (altura m\xe1xima)\n\
3. Ch\xe3o: -5t\xb2 + 20t + 1 = 0, com \u0394 = 400 + 20 = 420.\n\
4. t = (-20 - \u221a420) / (-10) = 2 + \u221a105/5 \u2248 4,05 s\n\
5. O outro zero \xe9 negativo e rejeita-se.\n\
Resultado: altura m\xe1xima 21 m aos 2 s; chega ao ch\xe3o aos 4,05 s.\n\
Interpreta\xe7\xe3o: a = -5 < 0 garante que o v\xe9rtice \xe9 um m\xe1ximo.\n\
Erros a evitar: aceitar o tempo negativo.\n\
"
