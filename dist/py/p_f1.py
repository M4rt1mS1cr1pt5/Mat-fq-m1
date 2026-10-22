# p_f1.py - M1TR4M: Energia e movimentos (gerado pelo build).
D = "@V 1\n\
@N 5\n\
@T Energia e movimentos\n\
@L f1a|Energia cin\xe9tica, potencial grav\xedtica e mec\xe2nica|energia cinetica energia potencial gravitica\
 energia mecanica sistema mecanico modelo da particula material centro de massa nivel de\
 referencia|c_fqen.em|10|n\xfacleo|r9a:Movimentos: rapidez, acelera\xe7\xe3o e gr\xe1ficos;r9b:For\xe7as:\
 Leis de Newton, atrito e impuls\xe3o||AE FQ A 10.\xba, Energia e movimentos\n\
@A\n\
- Distinguir energia cin\xe9tica de energia potencial grav\xedtica.\n\
- Calcular Ec, Epg e Em.\n\
- Usar o modelo da part\xedcula material.\n\
- Escolher um n\xedvel de refer\xeancia para a Epg.\n\
@B\n\
Um carro em andamento, um livro numa prateleira e uma bola a cair t\xeam energia.\n\
A energia associada ao movimento \xe9 a cin\xe9tica; a associada \xe0 posi\xe7\xe3o \xe9 a potencial.\n\
Somadas, d\xe3o a energia mec\xe2nica.\n\
@C\n\
- Energia cin\xe9tica: Ec = \xbd m v\xb2 (m em kg, v em m s\u207b\xb9, Ec em J).\n\
- Energia potencial grav\xedtica do sistema corpo + Terra: Epg = m g h.\n\
- h: altura acima do n\xedvel de refer\xeancia, onde Epg = 0.\n\
- Energia mec\xe2nica: Em = Ec + Epg.\n\
- Part\xedcula material: o corpo reduz-se ao centro de massa, com toda a massa.\n\
- O modelo serve quando s\xf3 interessa a transla\xe7\xe3o do corpo.\n\
@D\n\
Exemplo: m = 2,0 kg, v = 3,0 m s\u207b\xb9, h = 5,0 m e g = 10 m s\u207b\xb2.\n\
Ec = \xbd \xd7 2,0 \xd7 3,0\xb2 = 9,0 J.\n\
Epg = 2,0 \xd7 10 \xd7 5,0 = 1,0 \xd7 10\xb2 J.\n\
Em = 9,0 + 100 = 1,1 \xd7 10\xb2 J.\n\
Ec nunca \xe9 negativa; Epg \xe9 negativa abaixo do n\xedvel de refer\xeancia.\n\
Duplicar a velocidade quadruplica a energia cin\xe9tica.\n\
Duplicar a massa duplica Ec e Epg.\n\
O n\xedvel de refer\xeancia escolhe-se; a varia\xe7\xe3o de Epg n\xe3o depende dele.\n\
A energia interna (agita\xe7\xe3o e liga\xe7\xf5es das part\xedculas) n\xe3o faz parte da energia mec\xe2nica.\n\
@F Energia cin\xe9tica|Ec = \xbd m v\xb2|m: massa (kg);v: m\xf3dulo da velocidade (m s\u207b\xb9)|Ec \u2265\
 0|m = 2,0 kg e v = 3,0 m s\u207b\xb9: Ec = 9,0 J|c_fqen.em\n\
@F Energia potencial grav\xedtica|Epg = m g h|g: acelera\xe7\xe3o grav\xedtica (m s\u207b\xb2);h: altura\
 acima do n\xedvel de refer\xeancia (m)|perto da superf\xedcie da Terra|m = 2,0 kg e h = 5,0 m: Epg = 1,0\
 \xd7 10\xb2 J|c_fqen.em\n\
@F Energia mec\xe2nica|Em = Ec + Epg|Ec e Epg em J|sistema corpo + Terra|Em = 9,0 + 100 = 1,1 \xd7 10\xb2 J|c_fqen.em\n\
@F\n\
Dados: bola de 0,45 kg a 12 m s\u207b\xb9, a 2,0 m do ch\xe3o; g = 10 m s\u207b\xb2.\n\
Objetivo: Ec, Epg (refer\xeancia no ch\xe3o) e Em.\n\
1. Ec = \xbd \xd7 0,45 \xd7 12\xb2 = 32 J\n\
2. Epg = 0,45 \xd7 10 \xd7 2,0 = 9,0 J\n\
3. Em = 32,4 + 9,0 = 41 J\n\
> Em \u2248 41 J.\n\
Verifica\xe7\xe3o: Ec > Epg, porque a velocidade \xe9 grande e a altura \xe9 pequena.\n\
@G\n\
A energia mec\xe2nica explica montanhas-russas, quedas e saltos.\n\
Muitos problemas resolvem-se sem conhecer as for\xe7as: basta comparar energias.\n\
@H\n\
- Esquecer o quadrado da velocidade em Ec.\n\
- Usar a massa em gramas ou a velocidade em km/h.\n\
- Medir as alturas a partir de n\xedveis diferentes.\n\
- Achar que a Epg tem de ser positiva.\n\
@I\n\
- Ec = \xbd m v\xb2 (depende de v\xb2).\n\
- Epg = m g h (depende do n\xedvel de refer\xeancia).\n\
- Em = Ec + Epg.\n\
- Part\xedcula material: o corpo reduz-se ao centro de massa.\n\
@J\n\
Um carro de 1,2 \xd7 10\xb3 kg passa de 10 m s\u207b\xb9 para 20 m s\u207b\xb9. Por quanto se multiplica a\
 sua energia cin\xe9tica?\n\
@R\n\
Por 4: a velocidade duplica e Ec \xe9 proporcional a v\xb2 (passa de 6,0 \xd7 10\u2074 J para 2,4 \xd7 10\u2075 J).\n\
@L f1b|Trabalho de uma for\xe7a constante|trabalho forca constante deslocamento angulo componente eficaz\
 trabalho potente resistente nulo joule|c_fqen.tr|10|n\xfacleo|f1a:Energia cin\xe9tica, potencial\
 grav\xedtica e mec\xe2nica|m8a:Vetores: dire\xe7\xe3o, sentido e norma;m8g:Produto escalar (extens\xe3o,\
 11.\xba);m9a:Raz\xf5es trigonom\xe9tricas de um \xe2ngulo agudo|AE FQ A 10.\xba, Energia e movimentos\n\
@A\n\
- Definir trabalho como transfer\xeancia de energia por a\xe7\xe3o de uma for\xe7a.\n\
- Calcular o trabalho de uma for\xe7a constante.\n\
- Classificar o trabalho como potente, resistente ou nulo.\n\
- Identificar a componente eficaz da for\xe7a.\n\
@B\n\
Empurrar um carrinho transfere-lhe energia; segurar uma mala parado n\xe3o.\n\
Em F\xedsica, s\xf3 h\xe1 trabalho quando a for\xe7a tem componente na dire\xe7\xe3o do deslocamento.\n\
@C\n\
- Trabalho, W: energia transferida por uma for\xe7a cujo ponto de aplica\xe7\xe3o se desloca.\n\
- W = F d cos \u03b1 (F em N, d em m, W em J).\n\
- \u03b1: \xe2ngulo entre a for\xe7a e o deslocamento.\n\
- Componente eficaz: F cos \u03b1, na dire\xe7\xe3o do deslocamento.\n\
- \u03b1 < 90\xb0: potente (W > 0); \u03b1 = 90\xb0: nulo; \u03b1 > 90\xb0: resistente (W < 0).\n\
- 1 J = 1 N \xd7 1 m.\n\
@D\n\
Exemplo: puxa-se um caixote 5,0 m com uma for\xe7a de 10 N a 60\xb0 do ch\xe3o.\n\
W = 10 \xd7 5,0 \xd7 cos 60\xb0 = 25 J (potente).\n\
S\xf3 a componente eficaz, 10 \xd7 cos 60\xb0 = 5,0 N, realiza trabalho.\n\
A componente perpendicular, F sen \u03b1, n\xe3o realiza trabalho.\n\
Num plano horizontal, o peso e a rea\xe7\xe3o normal s\xe3o perpendiculares ao deslocamento: W = 0.\n\
O atrito op\xf5e-se ao movimento: \u03b1 = 180\xb0.\n\
Exemplo: atrito de 4,0 N ao longo de 3,0 m: W = 4,0 \xd7 3,0 \xd7 cos 180\xb0 = -12 J.\n\
Com v\xe1rias for\xe7as, o trabalho total \xe9 a soma dos trabalhos de cada for\xe7a.\n\
O trabalho total \xe9 igual ao trabalho da resultante.\n\
@F Trabalho de uma for\xe7a constante|W = F d cos \u03b1|F: intensidade da for\xe7a (N);d: deslocamento\
 (m);\u03b1: \xe2ngulo entre a for\xe7a e o deslocamento|for\xe7a constante e trajet\xf3ria retil\xednea|F =\
 10 N, d = 5,0 m e \u03b1 = 60\xb0: W = 25 J|c_fqen.tr\n\
@F\n\
Dados: empurra-se um carrinho 8,0 m com 50 N a 30\xb0 do deslocamento; o atrito vale 15 N.\n\
Objetivo: trabalho de cada for\xe7a e trabalho total.\n\
1. W(F) = 50 \xd7 8,0 \xd7 cos 30\xb0 = 3,5 \xd7 10\xb2 J\n\
2. W(Fa) = 15 \xd7 8,0 \xd7 cos 180\xb0 = -1,2 \xd7 10\xb2 J\n\
3. W(P) = W(N) = 0 (for\xe7as perpendiculares ao deslocamento)\n\
4. W(total) = 346 - 120 = 2,3 \xd7 10\xb2 J\n\
> W(total) \u2248 2,3 \xd7 10\xb2 J (potente).\n\
Verifica\xe7\xe3o: a for\xe7a aplicada transfere mais energia do que o atrito retira.\n\
@G\n\
O trabalho mede a energia que uma for\xe7a transfere.\n\
Liga as for\xe7as, do 9.\xba ano, \xe0 energia, do 10.\xba ano.\n\
@H\n\
- Usar o \xe2ngulo com a vertical em vez do \xe2ngulo com o deslocamento.\n\
- Esquecer que o atrito tem \u03b1 = 180\xb0.\n\
- Achar que segurar um peso parado realiza trabalho.\n\
- Calcular o cosseno com a calculadora em radianos.\n\
@I\n\
- W = F d cos \u03b1.\n\
- \u03b1 < 90\xb0: potente; 90\xb0: nulo; \u03b1 > 90\xb0: resistente.\n\
- S\xf3 a componente eficaz realiza trabalho.\n\
- Trabalho total = soma dos trabalhos.\n\
@J\n\
Uma for\xe7a de 20 N, perpendicular a um deslocamento de 4,0 m, realiza que trabalho?\n\
@R\n\
Nenhum: W = 20 \xd7 4,0 \xd7 cos 90\xb0 = 0 J.\n\
@L f1c|Teorema da energia cin\xe9tica|teorema da energia cinetica trabalho da resultante soma dos trabalhos\
 variacao da energia cinetica travagem|c_fqen.tec|10|n\xfacleo|f1b:Trabalho de uma for\xe7a\
 constante|m8b:Opera\xe7\xf5es com vetores|AE FQ A 10.\xba, Energia e movimentos\n\
@A\n\
- Enunciar o teorema da energia cin\xe9tica.\n\
- Calcular o trabalho da resultante a partir da varia\xe7\xe3o de Ec.\n\
- Calcular velocidades a partir do trabalho das for\xe7as.\n\
- Relacionar o sinal do trabalho total com a varia\xe7\xe3o de Ec.\n\
@B\n\
Quando v\xe1rias for\xe7as atuam num corpo, o efeito na velocidade depende do trabalho de todas.\n\
Se o trabalho total \xe9 positivo, o corpo acelera; se \xe9 negativo, trava.\n\
@C\n\
- Teorema da energia cin\xe9tica: W(R) = \u0394Ec = Ec,f - Ec,i.\n\
- W(R): trabalho da resultante, igual \xe0 soma dos trabalhos de todas as for\xe7as.\n\
- W(R) > 0: Ec aumenta; W(R) < 0: Ec diminui.\n\
- W(R) = 0: Ec n\xe3o varia.\n\
- Vale para todas as for\xe7as, conservativas ou n\xe3o.\n\
@D\n\
Exemplo: um carro de 1000 kg passa de 10 m s\u207b\xb9 para 20 m s\u207b\xb9.\n\
W(R) = \xbd \xd7 1000 \xd7 (20\xb2 - 10\xb2) = 1,5 \xd7 10\u2075 J.\n\
Exemplo: um bloco de 2,0 kg a 4,0 m s\u207b\xb9 para ao fim de 4,0 m, travado pelo atrito.\n\
\u0394Ec = 0 - \xbd \xd7 2,0 \xd7 4,0\xb2 = -16 J, logo W(Fa) = -16 J.\n\
Como W(Fa) = -Fa d, o atrito vale 16 / 4,0 = 4,0 N.\n\
Para obter a velocidade final: vf = \u221a(vi\xb2 + 2 W(R) / m).\n\
O teorema dispensa o c\xe1lculo da acelera\xe7\xe3o.\n\
@F Teorema da energia cin\xe9tica|W(R) = \u0394Ec = \xbd m vf\xb2 - \xbd m vi\xb2|W(R): trabalho da\
 resultante (J);vi e vf: velocidades inicial e final|for\xe7as de qualquer tipo|1000 kg de 10 para 20 m\
 s\u207b\xb9: W(R) = 1,5 \xd7 10\u2075 J|c_fqen.tec\n\
@F\n\
Dados: um tren\xf3 de 50 kg parte do repouso. Puxa-se com 120 N, na dire\xe7\xe3o do movimento, ao longo de\
 10 m. O atrito vale 40 N.\n\
Objetivo: velocidade final.\n\
1. W(F) = 120 \xd7 10 = 1,2 \xd7 10\xb3 J\n\
2. W(Fa) = -40 \xd7 10 = -4,0 \xd7 10\xb2 J\n\
3. W(R) = 1200 - 400 = 8,0 \xd7 10\xb2 J\n\
4. vf = \u221a(2 \xd7 800 / 50) = 5,7 m s\u207b\xb9\n\
> vf \u2248 5,7 m s\u207b\xb9.\n\
Verifica\xe7\xe3o: Ec final = \xbd \xd7 50 \xd7 5,66\xb2 \u2248 8,0 \xd7 10\xb2 J = W(R).\n\
@G\n\
O teorema liga o trabalho das for\xe7as \xe0 varia\xe7\xe3o da velocidade.\n\
\xc9 muito \xfatil quando se conhecem as for\xe7as e as dist\xe2ncias, mas n\xe3o o tempo.\n\
@H\n\
- Usar o trabalho de uma s\xf3 for\xe7a em vez do trabalho total.\n\
- Esquecer o sinal negativo do trabalho do atrito.\n\
- Calcular vf\xb2 e esquecer a raiz quadrada.\n\
- Somar velocidades em vez de energias.\n\
@I\n\
- W(R) = \u0394Ec.\n\
- W(R) = soma dos trabalhos de todas as for\xe7as.\n\
- W(R) > 0: acelera; W(R) < 0: trava.\n\
@J\n\
Um corpo de 4,0 kg tem Ec = 50 J. Que trabalho total \xe9 preciso para o parar?\n\
@R\n\
W(R) = 0 - 50 = -50 J (trabalho resistente).\n\
@L f1d|For\xe7as conservativas e conserva\xe7\xe3o da energia mec\xe2nica|forca conservativa nao conservativa\
 trabalho do peso trajetoria conservacao da energia mecanica queda livre escorrega altura\
 maxima|c_fqen.cons|10|n\xfacleo|f1c:Teorema da energia cin\xe9tica|m9b:Resolver tri\xe2ngulos\
 ret\xe2ngulos|AE FQ A 10.\xba, Energia e movimentos\n\
@A\n\
- Distinguir for\xe7as conservativas de n\xe3o conservativas.\n\
- Relacionar o trabalho do peso com a varia\xe7\xe3o de Epg.\n\
- Aplicar a conserva\xe7\xe3o da energia mec\xe2nica.\n\
- Calcular velocidades e alturas pela conserva\xe7\xe3o.\n\
@B\n\
Uma bola atirada ao ar perde velocidade a subir e recupera-a a descer.\n\
Sem resist\xeancia do ar, volta \xe0 m\xe3o com a mesma velocidade: a energia mec\xe2nica conserva-se.\n\
@C\n\
- For\xe7a conservativa: o trabalho entre dois pontos n\xe3o depende da trajet\xf3ria (ex.: peso).\n\
- Trabalho do peso: W(P) = -\u0394Epg = m g (hi - hf).\n\
- N\xe3o conservativas: atrito, resist\xeancia do ar, for\xe7as de motores.\n\
- Se s\xf3 as for\xe7as conservativas realizam trabalho: Em,i = Em,f.\n\
- Nesse caso, \u0394Ec = -\u0394Epg.\n\
@D\n\
Exemplo: um corpo cai 20 m a partir do repouso, sem resist\xeancia do ar (g = 10 m s\u207b\xb2).\n\
m g h = \xbd m v\xb2 e a massa corta-se: v = \u221a(2 \xd7 10 \xd7 20) = 20 m s\u207b\xb9.\n\
A velocidade final n\xe3o depende da massa.\n\
Num escorrega sem atrito, a velocidade no fundo s\xf3 depende do desn\xedvel.\n\
A rea\xe7\xe3o normal \xe9 perpendicular ao deslocamento: W(N) = 0 e n\xe3o altera a Em.\n\
Lan\xe7amento vertical com 12 m s\u207b\xb9: h m\xe1x = 12\xb2 / (2 \xd7 10) = 7,2 m.\n\
Um corpo de 2,0 kg desce 5,0 m: W(P) = 2,0 \xd7 10 \xd7 5,0 = 1,0 \xd7 10\xb2 J.\n\
A subir, o trabalho do peso \xe9 negativo e a Epg aumenta.\n\
@F Trabalho do peso|W(P) = -\u0394Epg = m g (hi - hf)|hi e hf: alturas inicial e final (m)|peso constante\
 (perto da Terra)|2,0 kg desce 5,0 m: W(P) = 1,0 \xd7 10\xb2 J|c_fqen.wp\n\
@F Conserva\xe7\xe3o da energia mec\xe2nica|\xbd m vi\xb2 + m g hi = \xbd m vf\xb2 + m g hf|i e f: estados\
 inicial e final|s\xf3 for\xe7as conservativas realizam trabalho|queda de 20 m a partir do repouso: v = 20 m\
 s\u207b\xb9|c_fqen.cons\n\
@F\n\
Dados: um skater parte do repouso no topo de uma rampa com 3,2 m de altura. Sem atrito; g = 10 m s\u207b\xb2.\n\
Objetivo: velocidade no fundo e a 1,4 m de altura.\n\
1. No fundo: v = \u221a(2 \xd7 10 \xd7 3,2) = 8,0 m s\u207b\xb9\n\
2. A 1,4 m: v = \u221a(2 \xd7 10 \xd7 (3,2 - 1,4)) = 6,0 m s\u207b\xb9\n\
> v = 8,0 m s\u207b\xb9 no fundo e 6,0 m s\u207b\xb9 a 1,4 m.\n\
Verifica\xe7\xe3o: a 1,4 m ainda h\xe1 Epg, por isso a velocidade \xe9 menor.\n\
@G\n\
A conserva\xe7\xe3o da energia mec\xe2nica resolve movimentos complicados comparando s\xf3 dois estados.\n\
Na realidade h\xe1 sempre algum atrito: a conserva\xe7\xe3o \xe9 um modelo.\n\
@H\n\
- Achar que a velocidade de queda depende da massa.\n\
- Usar a conserva\xe7\xe3o quando h\xe1 atrito ou resist\xeancia do ar.\n\
- Medir alturas a partir de n\xedveis diferentes.\n\
- Trocar o sinal em W(P) = -\u0394Epg.\n\
@I\n\
- O peso \xe9 uma for\xe7a conservativa.\n\
- W(P) = -\u0394Epg.\n\
- S\xf3 for\xe7as conservativas: Em constante.\n\
- Queda a partir do repouso: v = \u221a(2 g h).\n\
@J\n\
Duas bolas, de 1 kg e de 5 kg, caem da mesma altura sem resist\xeancia do ar. Qual chega ao ch\xe3o mais depressa?\n\
@R\n\
Chegam com a mesma velocidade: v = \u221a(2 g h) n\xe3o depende da massa.\n\
@L f1e|For\xe7as n\xe3o conservativas, pot\xeancia e rendimento|forcas nao conservativas atrito resistencia\
 do ar energia dissipada variacao da energia mecanica potencia watt rendimento\
 quilowatt-hora|c_fqen.ren|10|n\xfacleo|f1d:For\xe7as conservativas e conserva\xe7\xe3o da energia\
 mec\xe2nica||AE FQ A 10.\xba, Energia e movimentos\n\
@A\n\
- Relacionar o trabalho das for\xe7as n\xe3o conservativas com \u0394Em.\n\
- Calcular a energia dissipada.\n\
- Calcular a pot\xeancia.\n\
- Calcular o rendimento de um processo.\n\
@B\n\
Um carro trava e para: a energia cin\xe9tica passa para energia interna dos trav\xf5es e do ar.\n\
Nenhuma m\xe1quina aproveita toda a energia que recebe.\n\
@C\n\
- W(Fnc) = \u0394Em: trabalho das for\xe7as n\xe3o conservativas.\n\
- Com atrito ou resist\xeancia do ar, W(Fnc) < 0 e a Em diminui.\n\
- Energia dissipada: Ed = -\u0394Em (aumenta a energia interna).\n\
- Pot\xeancia: P = E / \u0394t (em W; 1 W = 1 J s\u207b\xb9).\n\
- Rendimento: \u03b7 = E(\xfatil) / E(fornecida) \xd7 100 %.\n\
- 1 kWh = 3,6 \xd7 10\u2076 J.\n\
@D\n\
Exemplo: uma bola de 57 g cai de 1,20 m e ressalta at\xe9 0,90 m (g = 10 m s\u207b\xb2).\n\
Em,i = 0,057 \xd7 10 \xd7 1,20 = 0,68 J; Em,f = 0,057 \xd7 10 \xd7 0,90 = 0,51 J.\n\
Dissipada: 0,684 - 0,513 = 0,17 J, isto \xe9, 25 % da inicial.\n\
Exemplo: um motor eleva 50 kg a 6,0 m em 10 s e recebe 4,0 kJ.\n\
E(\xfatil) = 50 \xd7 10 \xd7 6,0 = 3,0 \xd7 10\xb3 J; P(\xfatil) = 3000 / 10 = 3,0 \xd7 10\xb2 W.\n\
\u03b7 = 3000 / 4000 \xd7 100 = 75 %.\n\
A energia total conserva-se sempre: a dissipada n\xe3o desaparece.\n\
Dissipar \xe9 tornar a energia menos \xfatil, mais \"espalhada\".\n\
@F For\xe7as n\xe3o conservativas|W(Fnc) = \u0394Em|W(Fnc): trabalho das for\xe7as n\xe3o conservativas\
 (J)|atrito, resist\xeancia do ar, motores|bola de 57 g de 1,20 m a 0,90 m: \u0394Em = -0,17 J|c_fqen.cons\n\
@F Pot\xeancia|P = E / \u0394t|E: energia transferida (J);\u0394t: intervalo de tempo (s)|pot\xeancia\
 m\xe9dia|3,0 kJ em 10 s: P = 3,0 \xd7 10\xb2 W|c_fqen.pot\n\
@F Rendimento|\u03b7 = E(\xfatil) / E(fornecida) \xd7 100 %|tamb\xe9m com pot\xeancias \xfateis e\
 fornecidas|\u03b7 < 100 %|3,0 kJ \xfateis de 4,0 kJ: \u03b7 = 75 %|c_fqen.ren\n\
@F\n\
Dados: uma grua de 2,0 kW eleva 400 kg a 15 m em 40 s; g = 10 m s\u207b\xb2.\n\
Objetivo: energia \xfatil, energia fornecida e rendimento.\n\
1. E(\xfatil) = 400 \xd7 10 \xd7 15 = 6,0 \xd7 10\u2074 J\n\
2. E(fornecida) = 2,0 \xd7 10\xb3 \xd7 40 = 8,0 \xd7 10\u2074 J\n\
3. \u03b7 = 6,0 \xd7 10\u2074 / (8,0 \xd7 10\u2074) \xd7 100 = 75 %\n\
> \u03b7 = 75 %; dissipam-se 2,0 \xd7 10\u2074 J.\n\
Verifica\xe7\xe3o: \u03b7 < 100 %, como tem de ser.\n\
@G\n\
A energia que uma m\xe1quina recebe vai toda para algum lado: parte \xe9 \xfatil, o resto \xe9 dissipada.\n\
Aumentar o rendimento poupa energia e dinheiro.\n\
@H\n\
- Esquecer que W(Fnc) \xe9 negativo quando h\xe1 dissipa\xe7\xe3o.\n\
- Juntar pot\xeancia em kW com tempo em s sem converter.\n\
- Trocar a energia \xfatil com a fornecida (d\xe1 \u03b7 > 100 %).\n\
- Dizer que a energia dissipada desaparece.\n\
@I\n\
- W(Fnc) = \u0394Em.\n\
- Ed = -\u0394Em.\n\
- P = E / \u0394t.\n\
- \u03b7 = E(\xfatil) / E(fornecida) \xd7 100 %.\n\
@J\n\
Uma l\xe2mpada de 60 W transforma 6,0 J por segundo em luz. Qual \xe9 o seu rendimento?\n\
@R\n\
\u03b7 = 6,0 / 60 \xd7 100 = 10 %; o resto \xe9 dissipado como calor.\n\
@E 1|f1e1|Energia cin\xe9tica de um ciclista|c_fqen.em|f1a\n\
Enunciado: um ciclista e a bicicleta t\xeam 70 kg e seguem a 36 km/h. Qual \xe9 a energia cin\xe9tica?\n\
Dados: m = 70 kg; v = 36 km/h.\n\
Resolu\xe7\xe3o:\n\
1. v = 36 / 3,6 = 10 m s\u207b\xb9\n\
2. Ec = \xbd \xd7 70 \xd7 10\xb2 = 3,5 \xd7 10\xb3 J\n\
Resultado: Ec = 3,5 \xd7 10\xb3 J.\n\
Interpreta\xe7\xe3o: a 72 km/h a energia cin\xe9tica seria 4 vezes maior.\n\
Erros a evitar: usar 36 km/h diretamente na f\xf3rmula (d\xe1 um valor 13 vezes maior).\n\
@E 2|f1e2|Bloco num plano inclinado com atrito|c_fqen.cons|f1e\n\
Enunciado: um bloco de 2,0 kg parte do repouso e desce 5,0 m num plano inclinado a 30\xb0. Chega ao fundo a\
 6,0 m s\u207b\xb9 (g = 10 m s\u207b\xb2).\n\
Calcula a energia dissipada e a for\xe7a de atrito.\n\
Resolu\xe7\xe3o:\n\
1. Altura: h = 5,0 \xd7 sen 30\xb0 = 2,5 m\n\
2. Em,i = 2,0 \xd7 10 \xd7 2,5 = 50 J\n\
3. Em,f = \xbd \xd7 2,0 \xd7 6,0\xb2 = 36 J\n\
4. Ed = 50 - 36 = 14 J\n\
5. W(Fa) = -Fa d, logo Fa = 14 / 5,0 = 2,8 N\n\
Resultado: dissipam-se 14 J; o atrito vale 2,8 N.\n\
Interpreta\xe7\xe3o: sem atrito chegaria ao fundo a \u221a(2 \xd7 10 \xd7 2,5) \u2248 7,1 m s\u207b\xb9.\n\
Erros a evitar: usar d = 5,0 m como altura.\n\
@E 3|f1e3|Montanha-russa real|c_fqen.cons|f1e\n\
Enunciado: um carro de 500 kg parte do repouso a 30 m de altura. Passa a 10 m de altura com 18 m s\u207b\xb9\
 (g = 10 m s\u207b\xb2).\n\
Que percentagem da energia mec\xe2nica foi dissipada?\n\
Resolu\xe7\xe3o:\n\
1. Em,i = 500 \xd7 10 \xd7 30 = 1,5 \xd7 10\u2075 J\n\
2. Em,f = \xbd \xd7 500 \xd7 18\xb2 + 500 \xd7 10 \xd7 10 = 1,31 \xd7 10\u2075 J\n\
3. Ed = 150 000 - 131 000 = 1,9 \xd7 10\u2074 J\n\
4. Percentagem: 19 000 / 150 000 \xd7 100 = 13 %\n\
Resultado: dissipam-se cerca de 13 % da energia mec\xe2nica.\n\
Interpreta\xe7\xe3o: sem atrito, chegaria aos 10 m a \u221a(2 \xd7 10 \xd7 20) = 20 m s\u207b\xb9.\n\
Erros a evitar: esquecer a Epg no ponto a 10 m.\n\
"
