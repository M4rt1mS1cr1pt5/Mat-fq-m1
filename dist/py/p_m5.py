# p_m5.py - M1TR4M: Fun\u00e7\u00e3o quadr\u00e1tica (gerado pelo build).
D = "@V 1\n\
@N 4\n\
@T Fun\u00e7\u00e3o quadr\u00e1tica\n\
@L m5a|A fun\u00e7\u00e3o quadr\u00e1tica e o seu gr\u00e1fico|funcao quadratica parabola concavidade vertice\
 eixo de simetria forma canonica a(x-h)^2+k|c_matq.q2|10|n\u00facleo|||AE Mat A 10.\u00ba, Fun\u00e7\u00f5es:\
 fun\u00e7\u00e3o quadr\u00e1tica\n\
@A\n\
- Reconhecer uma fun\u00e7\u00e3o quadr\u00e1tica f(x) = ax\u00b2 + bx + c, com a \u2260 0.\n\
- Relacionar o sinal de a com a concavidade da par\u00e1bola.\n\
- Determinar o v\u00e9rtice e o eixo de simetria.\n\
- Escrever f na forma can\u00f3nica a(x - h)\u00b2 + k.\n\
- Obter o gr\u00e1fico a partir do de y = x\u00b2.\n\
@B\n\
O gr\u00e1fico de uma fun\u00e7\u00e3o quadr\u00e1tica \u00e9 uma par\u00e1bola, como o jato de \u00e1gua de\
 uma fonte.\n\
Se a > 0, abre para cima, como um sorriso; se a < 0, abre para baixo. O v\u00e9rtice \u00e9 o ponto mais\
 baixo (ou mais alto). A par\u00e1bola \u00e9 sim\u00e9trica em rela\u00e7\u00e3o a uma reta vertical: o eixo.\n\
@C\n\
- Fun\u00e7\u00e3o quadr\u00e1tica: f(x) = ax\u00b2 + bx + c, com a, b, c \u2208 \u211d e a \u2260 0.\n\
- Df = \u211d. O gr\u00e1fico chama-se par\u00e1bola.\n\
- Forma can\u00f3nica: f(x) = a(x - h)\u00b2 + k.\n\
- V\u00e9rtice: V(h, k). Eixo de simetria: x = h.\n\
- a > 0: concavidade voltada para cima; k \u00e9 o m\u00ednimo.\n\
- a < 0: concavidade voltada para baixo; k \u00e9 o m\u00e1ximo.\n\
- Na forma geral: h = -b/(2a) e k = f(h).\n\
@D\n\
Parte-se do gr\u00e1fico de y = x\u00b2, com v\u00e9rtice em (0, 0).\n\
y = ax\u00b2 estica (|a| > 1) ou encolhe (0 < |a| < 1) na vertical.\n\
Se a < 0, h\u00e1 tamb\u00e9m reflex\u00e3o no eixo Ox.\n\
y = a(x - h)\u00b2 + k \u00e9 y = ax\u00b2 transladada.\n\
A transla\u00e7\u00e3o leva o v\u00e9rtice de (0, 0) para (h, k).\n\
Exemplo: f(x) = 2(x - 1)\u00b2 + 3.\n\
Tem v\u00e9rtice V(1, 3) e eixo x = 1.\n\
Como a = 2 > 0, o m\u00ednimo \u00e9 3.\n\
Para passar da forma geral \u00e0 can\u00f3nica, calcula-se h e k.\n\
Exemplo: f(x) = x\u00b2 - 4x + 1.\n\
h = -(-4)/(2 \u00d7 1) = 2 e k = f(2) = 4 - 8 + 1 = -3.\n\
Logo f(x) = (x - 2)\u00b2 - 3.\n\
Aten\u00e7\u00e3o ao sinal: (x - 2)\u00b2 d\u00e1 h = 2 e (x + 2)\u00b2 d\u00e1 h = -2.\n\
@F Forma can\u00f3nica|f(x) = a(x - h)\u00b2 + k|a: abertura e concavidade (a \u2260 0);(h, k): v\u00e9rtice\
 da par\u00e1bola|qualquer fun\u00e7\u00e3o quadr\u00e1tica|f(x) = 2(x - 1)\u00b2 + 3 tem v\u00e9rtice (1,\
 3)|c_matq.q2\n\
@F Abcissa do v\u00e9rtice|h = -b / (2a)|a, b: coeficientes de f(x) = ax\u00b2 + bx + c|a \u2260 0|f(x) =\
 x\u00b2 - 4x + 1: h = 2|c_matq.q2\n\
@F Ordenada do v\u00e9rtice|k = f(h) = c - b\u00b2 / (4a)|h: abcissa do v\u00e9rtice;a, b, c: coeficientes|a\
 \u2260 0|f(x) = x\u00b2 - 4x + 1: k = -3|c_matq.q2\n\
@F\n\
Dados: f(x) = -2x\u00b2 + 8x - 5.\n\
Objetivo: v\u00e9rtice, eixo, concavidade e forma can\u00f3nica.\n\
1. a = -2, b = 8, c = -5.\n\
2. h = -8 / (2 \u00d7 (-2)) = 2\n\
3. k = f(2) = -2 \u00d7 4 + 16 - 5 = 3\n\
4. V\u00e9rtice V(2, 3); eixo de simetria x = 2.\n\
5. a < 0: concavidade voltada para baixo; m\u00e1ximo 3.\n\
> f(x) = -2(x - 2)\u00b2 + 3\n\
Verifica\u00e7\u00e3o: f(0) = -2 \u00d7 4 + 3 = -5, igual a c.\n\
@G\n\
A forma can\u00f3nica mostra logo o v\u00e9rtice.\n\
A forma geral mostra logo a ordenada na origem, c.\n\
O m\u00e1ximo ou o m\u00ednimo de uma grandeza est\u00e1 no v\u00e9rtice.\n\
Exemplos: altura m\u00e1xima de um lan\u00e7amento, \u00e1rea m\u00e1xima de um terreno.\n\
@H\n\
- Ler h com o sinal trocado: em (x + 3)\u00b2, h = -3.\n\
- Esquecer o a ao calcular k = f(h).\n\
- Achar que a > 0 d\u00e1 um m\u00e1ximo: d\u00e1 um m\u00ednimo.\n\
- Dizer que o eixo de simetria \u00e9 y = h: \u00e9 x = h.\n\
- Esquecer que a = 0 n\u00e3o d\u00e1 uma fun\u00e7\u00e3o quadr\u00e1tica.\n\
@I\n\
- f(x) = ax\u00b2 + bx + c, com a \u2260 0; gr\u00e1fico: par\u00e1bola.\n\
- Forma can\u00f3nica a(x - h)\u00b2 + k; v\u00e9rtice (h, k).\n\
- Eixo de simetria: x = h, com h = -b/(2a).\n\
- a > 0: concavidade para cima e m\u00ednimo k.\n\
- a < 0: concavidade para baixo e m\u00e1ximo k.\n\
@J\n\
Determina o v\u00e9rtice de f(x) = x\u00b2 + 6x + 5.\n\
@R\n\
h = -6 / (2 \u00d7 1) = -3; k = f(-3) = 9 - 18 + 5 = -4.\n\
V\u00e9rtice: V(-3, -4).\n\
@L m5b|Zeros e f\u00f3rmula resolvente|zeros equacao do 2.o grau formula resolvente discriminante delta\
 binomio discriminante fatorizacao|c_matq.q2|10|n\u00facleo|m5a:A fun\u00e7\u00e3o quadr\u00e1tica e o seu\
 gr\u00e1fico||AE Mat A 10.\u00ba, Fun\u00e7\u00f5es: fun\u00e7\u00e3o quadr\u00e1tica\n\
@A\n\
- Calcular o discriminante \u0394 = b\u00b2 - 4ac.\n\
- Relacionar o sinal de \u0394 com o n\u00famero de zeros.\n\
- Resolver equa\u00e7\u00f5es do 2.\u00ba grau com a f\u00f3rmula resolvente.\n\
- Resolver equa\u00e7\u00f5es incompletas sem a f\u00f3rmula.\n\
- Fatorizar ax\u00b2 + bx + c usando os zeros.\n\
@B\n\
Os zeros s\u00e3o os pontos onde a par\u00e1bola corta o eixo Ox.\n\
Uma par\u00e1bola pode cort\u00e1-lo duas vezes, toc\u00e1-lo uma vez, ou n\u00e3o o tocar.\n\
O discriminante diz qual destes casos acontece.\n\
A f\u00f3rmula resolvente d\u00e1 os zeros em qualquer caso.\n\
@C\n\
- Equa\u00e7\u00e3o do 2.\u00ba grau: ax\u00b2 + bx + c = 0, com a \u2260 0.\n\
- Discriminante: \u0394 = b\u00b2 - 4ac.\n\
- F\u00f3rmula resolvente: x = (-b \u00b1 \u221a\u0394) / (2a).\n\
- \u0394 > 0: dois zeros diferentes.\n\
- \u0394 = 0: um zero (duplo), que \u00e9 a abcissa do v\u00e9rtice.\n\
- \u0394 < 0: n\u00e3o h\u00e1 zeros; a equa\u00e7\u00e3o \u00e9 imposs\u00edvel em \u211d.\n\
- Fatoriza\u00e7\u00e3o (\u0394 \u2265 0): ax\u00b2 + bx + c = a(x - x\u2081)(x - x\u2082).\n\
@D\n\
Exemplo: x\u00b2 - 5x + 6 = 0.\n\
\u0394 = 25 - 24 = 1, logo h\u00e1 dois zeros.\n\
x = (5 \u00b1 1) / 2, ou seja, x = 2 \u2228 x = 3.\n\
C.S. = {2, 3}.\n\
Equa\u00e7\u00f5es incompletas resolvem-se mais depressa:\n\
- c = 0: x(ax + b) = 0, logo x = 0 \u2228 x = -b/a.\n\
- b = 0: x\u00b2 = -c/a, que s\u00f3 tem solu\u00e7\u00e3o se -c/a \u2265 0.\n\
Exemplo: 2x\u00b2 - 8 = 0 d\u00e1 x\u00b2 = 4, logo x = -2 \u2228 x = 2.\n\
Exemplo: 3x\u00b2 + 6x = 0 d\u00e1 3x(x + 2) = 0, logo x = 0 \u2228 x = -2.\n\
Quando \u221a\u0394 n\u00e3o \u00e9 inteira, deixa-se a forma exata.\n\
Exemplo: x\u00b2 - 2x - 1 = 0 d\u00e1 x = 1 - \u221a2 \u2228 x = 1 + \u221a2.\n\
A soma dos zeros \u00e9 -b/a e o produto \u00e9 c/a.\n\
@F Discriminante|\u0394 = b\u00b2 - 4ac|a, b, c: coeficientes de ax\u00b2 + bx + c|a \u2260 0|x\u00b2 - 5x +\
 6: \u0394 = 25 - 24 = 1|c_matq.q2\n\
@F F\u00f3rmula resolvente|x = (-b \u00b1 \u221a\u0394) / (2a)|\u0394: discriminante;a, b:\
 coeficientes|\u0394 \u2265 0 (sen\u00e3o n\u00e3o h\u00e1 zeros)|x\u00b2 - 5x + 6 = 0: x = (5 \u00b1 1)/2|c_matq.q2\n\
@F Fatoriza\u00e7\u00e3o|ax\u00b2 + bx + c = a(x - x\u2081)(x - x\u2082)|x\u2081, x\u2082: zeros (iguais se\
 \u0394 = 0)|\u0394 \u2265 0|x\u00b2 - 5x + 6 = (x - 2)(x - 3)|c_matq.q2\n\
@F\n\
Dados: 2x\u00b2 - 5x + 2 = 0.\n\
Objetivo: resolver a equa\u00e7\u00e3o.\n\
1. a = 2, b = -5, c = 2.\n\
2. \u0394 = (-5)\u00b2 - 4 \u00d7 2 \u00d7 2 = 9\n\
3. \u0394 > 0: h\u00e1 dois zeros.\n\
4. x = (5 \u00b1 3) / 4\n\
5. x = 2/4 = 1/2 \u2228 x = 8/4 = 2\n\
> C.S. = {1/2, 2}\n\
Verifica\u00e7\u00e3o: 2 \u00d7 (1/2)\u00b2 - 5 \u00d7 1/2 + 2 = 0.\n\
@G\n\
O sinal de \u0394 resume a posi\u00e7\u00e3o da par\u00e1bola face ao eixo Ox.\n\
\u0394 = 0 quer dizer que o v\u00e9rtice est\u00e1 em cima do eixo.\n\
Num problema, cada zero tem de fazer sentido no contexto.\n\
Um tempo ou um comprimento negativo rejeita-se.\n\
@H\n\
- Esquecer o sinal de b: com b = -5, -b = 5.\n\
- Dividir s\u00f3 \u221a\u0394 por 2a, e n\u00e3o -b \u00b1 \u221a\u0394.\n\
- Escrever \u221a\u0394 com \u0394 negativo.\n\
- Usar a f\u00f3rmula com a equa\u00e7\u00e3o por igualar a zero.\n\
- Perder solu\u00e7\u00f5es ao dividir por x: fatoriza em vez disso.\n\
@I\n\
- \u0394 = b\u00b2 - 4ac.\n\
- \u0394 > 0: 2 zeros; \u0394 = 0: 1 zero; \u0394 < 0: nenhum.\n\
- x = (-b \u00b1 \u221a\u0394) / (2a).\n\
- Incompletas: fatorizar (c = 0) ou isolar x\u00b2 (b = 0).\n\
- Fatoriza\u00e7\u00e3o: a(x - x\u2081)(x - x\u2082).\n\
- Deixa a forma exata quando \u221a\u0394 n\u00e3o \u00e9 inteira.\n\
@J\n\
Resolve x\u00b2 - 6x + 5 = 0.\n\
@R\n\
\u0394 = 36 - 20 = 16; x = (6 \u00b1 4) / 2.\n\
x = 1 \u2228 x = 5. C.S. = {1, 5}.\n\
@L m5c|Sinal, monotonia, extremos e inequa\u00e7\u00f5es|sinal monotonia crescente decrescente maximo minimo\
 extremo contradominio inequacao do 2.o grau conjunto-solucao|c_matq.iq|10|n\u00facleo|m5b:Zeros e\
 f\u00f3rmula resolvente||AE Mat A 10.\u00ba, Fun\u00e7\u00f5es: fun\u00e7\u00e3o quadr\u00e1tica\n\
@A\n\
- Estudar o sinal de uma fun\u00e7\u00e3o quadr\u00e1tica.\n\
- Indicar intervalos de monotonia e o extremo.\n\
- Indicar o contradom\u00ednio.\n\
- Resolver inequa\u00e7\u00f5es do 2.\u00ba grau.\n\
- Escrever o conjunto-solu\u00e7\u00e3o com intervalos.\n\
@B\n\
O sinal diz onde a par\u00e1bola est\u00e1 acima ou abaixo do eixo Ox.\n\
A monotonia diz onde sobe e onde desce.\n\
Tudo depende de duas coisas: a concavidade e os zeros.\n\
Um esbo\u00e7o r\u00e1pido resolve quase tudo.\n\
@C\n\
- f \u00e9 positiva onde o gr\u00e1fico est\u00e1 acima de Ox; negativa abaixo.\n\
- Com a > 0: f decresce em ]-\u221e, h] e cresce em [h, +\u221e[.\n\
- Com a > 0: m\u00ednimo k e D'f = [k, +\u221e[.\n\
- Com a < 0: f cresce em ]-\u221e, h], decresce em [h, +\u221e[.\n\
- Com a < 0: m\u00e1ximo k e D'f = ]-\u221e, k].\n\
- Inequa\u00e7\u00e3o do 2.\u00ba grau: ax\u00b2 + bx + c > 0 (ou \u2265, <, \u2264).\n\
@D\n\
M\u00e9todo para resolver uma inequa\u00e7\u00e3o:\n\
1. Passa tudo para um membro: ax\u00b2 + bx + c ? 0.\n\
2. Calcula os zeros.\n\
3. Esbo\u00e7a a par\u00e1bola com a concavidade certa.\n\
4. L\u00ea onde o gr\u00e1fico est\u00e1 acima (> 0) ou abaixo (< 0).\n\
Exemplo: x\u00b2 - 5x + 6 \u2264 0.\n\
Zeros 2 e 3; a = 1 > 0, a par\u00e1bola abre para cima.\n\
Fica abaixo do eixo entre os zeros.\n\
C.S. = [2, 3] (fechado, porque \u2264 inclui os zeros).\n\
Exemplo: -x\u00b2 + 4 > 0.\n\
Zeros -2 e 2; a = -1 < 0, abre para baixo.\n\
Fica acima do eixo entre os zeros: C.S. = ]-2, 2[.\n\
Sem zeros, o sinal \u00e9 sempre o de a.\n\
Exemplo: x\u00b2 + 1 > 0 \u00e9 verdade para todo o x: C.S. = \u211d.\n\
E x\u00b2 + 1 < 0 nunca acontece: C.S. = \u2205.\n\
@F Sinal com dois zeros (a > 0)|f(x) > 0 em ]-\u221e, x\u2081[ \u222a ]x\u2082, +\u221e[; f(x) < 0 em\
 ]x\u2081, x\u2082[|x\u2081 < x\u2082: zeros|a > 0 (com a < 0 os sinais trocam)|x\u00b2 - 5x + 6 < 0 em ]2,\
 3[|c_matq.iq\n\
@F Contradom\u00ednio|a > 0: D'f = [k, +\u221e[; a < 0: D'f = ]-\u221e, k]|k: ordenada do\
 v\u00e9rtice|fun\u00e7\u00e3o quadr\u00e1tica com Df = \u211d|f(x) = (x - 1)\u00b2 + 2: D'f = [2, +\u221e[|c_matq.q2\n\
@F\n\
Dados: inequa\u00e7\u00e3o x\u00b2 + 2x - 3 > 0.\n\
Objetivo: conjunto-solu\u00e7\u00e3o.\n\
1. \u0394 = 4 + 12 = 16\n\
2. x = (-2 \u00b1 4) / 2, logo x = -3 \u2228 x = 1\n\
3. a = 1 > 0: par\u00e1bola com concavidade para cima.\n\
4. Est\u00e1 acima do eixo fora dos zeros.\n\
> C.S. = ]-\u221e, -3[ \u222a ]1, +\u221e[\n\
Verifica\u00e7\u00e3o: x = 2 d\u00e1 4 + 4 - 3 = 5 > 0 (est\u00e1 no C.S.).\n\
E x = 0 d\u00e1 -3 < 0 (n\u00e3o est\u00e1 no C.S.).\n\
@G\n\
As inequa\u00e7\u00f5es respondem a perguntas como \"quando \u00e9 que o lucro \u00e9 positivo?\".\n\
O v\u00e9rtice d\u00e1 o lucro m\u00e1ximo; os zeros d\u00e3o os limites.\n\
Se o sinal for \u2265 ou \u2264, os zeros entram no conjunto-solu\u00e7\u00e3o.\n\
@H\n\
- Usar par\u00eanteses retos fechados com > ou <.\n\
- Esquecer de olhar para a concavidade.\n\
- Escrever o C.S. como pontos em vez de intervalos.\n\
- Trocar o sentido da inequa\u00e7\u00e3o ao passar termos de membro.\n\
- Escrever ]1, -3[ em vez de ]-3, 1[: o menor vem primeiro.\n\
@I\n\
- Sinal: depende de a e dos zeros.\n\
- a > 0: negativa entre os zeros; positiva fora deles.\n\
- a < 0: positiva entre os zeros; negativa fora deles.\n\
- Extremo no v\u00e9rtice: m\u00ednimo se a > 0, m\u00e1ximo se a < 0.\n\
- Inequa\u00e7\u00e3o: zeros, esbo\u00e7o, leitura do sinal.\n\
@J\n\
Resolve a inequa\u00e7\u00e3o x\u00b2 - 4 \u2264 0.\n\
@R\n\
Zeros: x\u00b2 = 4, logo x = -2 \u2228 x = 2.\n\
a > 0, logo a par\u00e1bola est\u00e1 abaixo do eixo entre os zeros.\n\
C.S. = [-2, 2].\n\
@L m5d|Transforma\u00e7\u00f5es de gr\u00e1ficos de fun\u00e7\u00f5es|transformacoes translacao dilatacao\
 contracao reflexao f(x-a) f(x)+b c f(x) grafico|c_matq.tf|10|n\u00facleo|m5a:A fun\u00e7\u00e3o\
 quadr\u00e1tica e o seu gr\u00e1fico||AE Mat A 10.\u00ba, Fun\u00e7\u00f5es: transforma\u00e7\u00f5es f(x -\
 a), f(x) + b e c f(x)\n\
@A\n\
- Obter o gr\u00e1fico de f(x) + b a partir do de f.\n\
- Obter o gr\u00e1fico de f(x - a) a partir do de f.\n\
- Obter o gr\u00e1fico de c \u00d7 f(x) a partir do de f.\n\
- Relacionar estas transforma\u00e7\u00f5es com a forma can\u00f3nica.\n\
@B\n\
Transformar um gr\u00e1fico \u00e9 como mexer num desenho.\n\
Podes desliz\u00e1-lo para cima ou para baixo, para a esquerda ou para a direita.\n\
Tamb\u00e9m podes estic\u00e1-lo ou encolh\u00ea-lo na vertical.\n\
Com um sinal menos, ele vira ao contr\u00e1rio (reflex\u00e3o).\n\
@C\n\
- f(x) + b: transla\u00e7\u00e3o vertical de b unidades.\n\
- f(x - a): transla\u00e7\u00e3o horizontal de a unidades (a > 0: direita; a < 0: esquerda).\n\
- c \u00d7 f(x), c > 1: dilata\u00e7\u00e3o vertical de coeficiente c.\n\
- c \u00d7 f(x), 0 < c < 1: contra\u00e7\u00e3o vertical de coeficiente c.\n\
- c < 0: h\u00e1 tamb\u00e9m reflex\u00e3o no eixo Ox.\n\
- O ponto (x, y) do gr\u00e1fico de f passa a (x + a, c y + b).\n\
@D\n\
Partimos de f(x) = x\u00b2, com v\u00e9rtice (0, 0).\n\
g(x) = x\u00b2 + 3 sobe 3 unidades: v\u00e9rtice (0, 3).\n\
g(x) = (x - 2)\u00b2 desliza 2 para a direita: v\u00e9rtice (2, 0).\n\
g(x) = (x + 2)\u00b2 desliza 2 para a esquerda: (x + 2) = (x - (-2)).\n\
g(x) = 3x\u00b2 fica mais \"fechada\": as ordenadas triplicam.\n\
g(x) = 0,5x\u00b2 fica mais \"aberta\": as ordenadas passam a metade.\n\
g(x) = -x\u00b2 \u00e9 a reflex\u00e3o de x\u00b2 no eixo Ox.\n\
Juntando tudo: g(x) = 2(x - 1)\u00b2 + 3.\n\
Primeiro dilata\u00e7\u00e3o de coeficiente 2.\n\
Depois transla\u00e7\u00e3o de 1 para a direita e 3 para cima.\n\
O v\u00e9rtice passa de (0, 0) para (1, 3).\n\
Os zeros de f(x - a) s\u00e3o os zeros de f somados com a.\n\
@F Transla\u00e7\u00e3o vertical|g(x) = f(x) + b|b > 0: para cima; b < 0: para baixo|qualquer\
 fun\u00e7\u00e3o f|x\u00b2 + 3: v\u00e9rtice (0, 3)|c_matq.tf\n\
@F Transla\u00e7\u00e3o horizontal|g(x) = f(x - a)|a > 0: para a direita; a < 0: para a esquerda|qualquer\
 fun\u00e7\u00e3o f|(x - 2)\u00b2: v\u00e9rtice (2, 0)|c_matq.tf\n\
@F Dilata\u00e7\u00e3o ou contra\u00e7\u00e3o vertical|g(x) = c \u00d7 f(x)|c > 1: dilata\u00e7\u00e3o; 0 < c\
 < 1: contra\u00e7\u00e3o; c < 0: com reflex\u00e3o em Ox|c \u2260 0|3x\u00b2: as ordenadas triplicam|c_matq.tf\n\
@F\n\
Dados: o gr\u00e1fico de f passa em A(1, 4).\n\
g(x) = 2 f(x - 3) - 1.\n\
Objetivo: o ponto do gr\u00e1fico de g que corresponde a A.\n\
1. Transla\u00e7\u00e3o horizontal: x passa a 1 + 3 = 4.\n\
2. Dilata\u00e7\u00e3o: y passa a 2 \u00d7 4 = 8.\n\
3. Transla\u00e7\u00e3o vertical: 8 - 1 = 7.\n\
> O ponto correspondente \u00e9 (4, 7).\n\
Verifica\u00e7\u00e3o: g(4) = 2 f(1) - 1 = 2 \u00d7 4 - 1 = 7.\n\
@G\n\
As transforma\u00e7\u00f5es explicam a forma can\u00f3nica a(x - h)\u00b2 + k.\n\
Toda a par\u00e1bola \u00e9 x\u00b2 dilatada, refletida e transladada.\n\
O mesmo vale para outras fun\u00e7\u00f5es, como o m\u00f3dulo |x|.\n\
@H\n\
- Achar que f(x - 2) desloca para a esquerda: desloca para a direita.\n\
- Aplicar o b dentro do par\u00eantese: f(x) + b n\u00e3o \u00e9 f(x + b).\n\
- Multiplicar as abcissas em vez das ordenadas em c f(x).\n\
- Esquecer a reflex\u00e3o quando c < 0.\n\
@I\n\
- f(x) + b: transla\u00e7\u00e3o vertical de b.\n\
- f(x - a): transla\u00e7\u00e3o horizontal de a (a > 0: direita).\n\
- c f(x): dilata\u00e7\u00e3o (c > 1) ou contra\u00e7\u00e3o (0 < c < 1); c < 0 reflete.\n\
- (x, y) passa a (x + a, c y + b).\n\
@J\n\
O gr\u00e1fico de f passa em B(-2, 5).\n\
Que ponto do gr\u00e1fico de g(x) = f(x + 1) + 2 lhe corresponde?\n\
@R\n\
f(x + 1) = f(x - (-1)): desloca 1 para a esquerda: -2 - 1 = -3.\n\
Sobe 2: 5 + 2 = 7. O ponto \u00e9 (-3, 7).\n\
@E 1|m5e1|V\u00e9rtice e eixo de uma par\u00e1bola|c_matq.q2|m5a\n\
Enunciado: indica o v\u00e9rtice, o eixo e a concavidade de f(x) = 3(x + 2)\u00b2 - 1.\n\
Dados: forma can\u00f3nica a(x - h)\u00b2 + k.\n\
Objetivo: v\u00e9rtice, eixo de simetria e concavidade.\n\
M\u00e9todo: ler h e k; aten\u00e7\u00e3o ao sinal de h.\n\
Resolu\u00e7\u00e3o:\n\
1. x + 2 = x - (-2), logo h = -2.\n\
2. k = -1.\n\
3. a = 3 > 0: concavidade voltada para cima.\n\
Resultado: V(-2, -1); eixo x = -2; m\u00ednimo -1.\n\
Interpreta\u00e7\u00e3o: \u00e9 a par\u00e1bola de y = 3x\u00b2 com o v\u00e9rtice em (-2, -1).\n\
Erros a evitar: escrever h = 2.\n\
@E 2|m5e2|Equa\u00e7\u00e3o do 2.\u00ba grau com fra\u00e7\u00e3o|c_matq.q2|m5b\n\
Enunciado: resolve 3x\u00b2 - 7x + 2 = 0.\n\
Dados: a = 3, b = -7, c = 2.\n\
Objetivo: conjunto-solu\u00e7\u00e3o.\n\
M\u00e9todo: discriminante e f\u00f3rmula resolvente.\n\
Resolu\u00e7\u00e3o:\n\
1. \u0394 = 49 - 24 = 25\n\
2. x = (7 \u00b1 5) / 6\n\
3. x = 2/6 = 1/3 \u2228 x = 12/6 = 2\n\
Resultado: C.S. = {1/3, 2}.\n\
Interpreta\u00e7\u00e3o: a par\u00e1bola corta o eixo Ox em x = 1/3 e em x = 2.\n\
Erros a evitar: dividir s\u00f3 o 5 por 6.\n\
Verifica\u00e7\u00e3o: 3 \u00d7 (1/3)\u00b2 - 7 \u00d7 (1/3) + 2 = 0.\n\
@E 3|m5e3|Altura m\u00e1xima de um lan\u00e7amento|c_matq.q2|m5c\n\
Enunciado: a altura de uma bola, em metros, \u00e9 h(t) = -5t\u00b2 + 20t + 1.\n\
t \u00e9 o tempo, em segundos, desde o lan\u00e7amento.\n\
Objetivo: altura m\u00e1xima e instante em que a bola chega ao ch\u00e3o.\n\
M\u00e9todo: v\u00e9rtice da par\u00e1bola e zero positivo.\n\
Resolu\u00e7\u00e3o:\n\
1. t do v\u00e9rtice: -20 / (2 \u00d7 (-5)) = 2 s\n\
2. h(2) = -20 + 40 + 1 = 21 m (altura m\u00e1xima)\n\
3. Ch\u00e3o: -5t\u00b2 + 20t + 1 = 0, com \u0394 = 400 + 20 = 420.\n\
4. t = (-20 - \u221a420) / (-10) = 2 + \u221a105/5 \u2248 4,05 s\n\
5. O outro zero \u00e9 negativo e rejeita-se.\n\
Resultado: altura m\u00e1xima 21 m aos 2 s; chega ao ch\u00e3o aos 4,05 s.\n\
Interpreta\u00e7\u00e3o: a = -5 < 0 garante que o v\u00e9rtice \u00e9 um m\u00e1ximo.\n\
Erros a evitar: aceitar o tempo negativo.\n\
"
