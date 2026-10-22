# p_af.py - M1TR4M: Atividades laboratoriais de F\xedsica (gerado pelo build).
D = "@V 1\n\
@N 6\n\
@T Atividades laboratoriais de F\xedsica\n\
@L af11|AL 1.1 Movimento num plano inclinado: energia cin\xe9tica e dist\xe2ncia|al 1.1 plano inclinado\
 carrinho celula fotoeletrica tempo de passagem velocidade energia cinetica distancia regressao forca\
 resultante|c_alf1.plano|10|n\xfacleo|f1c:Teorema da energia cin\xe9tica|m2h:Dados bivariados:\
 correla\xe7\xe3o e reta dos m\xednimos quadrados|Programa e AE FQ A 10.\xba, AL 1.1\n\
@A\n\
- Medir velocidades com uma c\xe9lula fotoel\xe9trica.\n\
- Calcular a energia cin\xe9tica em v\xe1rios pontos.\n\
- Relacionar Ec com a dist\xe2ncia percorrida (gr\xe1fico e regress\xe3o).\n\
- Interpretar o declive como a intensidade da resultante.\n\
@B\n\
Um carrinho que desce uma rampa ganha velocidade.\n\
Quanto mais desce, mais energia cin\xe9tica tem.\n\
@C\n\
- Material: calha inclinada, carrinho, tira opaca de largura L, c\xe9lula fotoel\xe9trica com cron\xf3metro\
 digital, fita m\xe9trica, balan\xe7a.\n\
- Velocidade na c\xe9lula: v \u2248 L / \u0394t (\u0394t: tempo de passagem da tira).\n\
- Ec = \xbd m v\xb2.\n\
- Partindo do repouso, Ec = F(R) d: o gr\xe1fico Ec(d) \xe9 uma reta de declive F(R).\n\
@D\n\
1. Mede a massa do carrinho e a largura da tira.\n\
2. Larga o carrinho sempre da mesma posi\xe7\xe3o, sem o empurrar.\n\
3. Coloca a c\xe9lula a v\xe1rias dist\xe2ncias d do ponto de partida.\n\
4. Regista o tempo de passagem (tr\xeas ensaios por posi\xe7\xe3o; usa a m\xe9dia).\n\
5. Calcula v e Ec para cada dist\xe2ncia.\n\
6. Faz o gr\xe1fico Ec(d) e a reta de regress\xe3o: o declive \xe9 F(R).\n\
Cuidados: a tira passa perpendicular ao feixe; mede as dist\xe2ncias sempre ao mesmo ponto do carrinho.\n\
L pequena: L / \u0394t aproxima bem a velocidade no ponto.\n\
@F Velocidade com c\xe9lula fotoel\xe9trica|v = L / \u0394t|L: largura da tira (m);\u0394t: tempo de passagem\
 (s)|L pequena|1,00 cm em 10,6 ms: v = 0,943 m s\u207b\xb9|c_alf1.plano\n\
@F Energia cin\xe9tica e dist\xe2ncia|Ec = F(R) d|F(R): intensidade da resultante (N);d: dist\xe2ncia\
 percorrida (m)|partida do repouso, F(R) constante|declive de Ec(d) = 0,554 N|c_alf1.plano\n\
@F\n\
Dados: m = 0,500 kg; L = 1,00 cm; d = 0,20, 0,40, 0,60 e 0,80 m; \u0394t = 15,0, 10,6, 8,7 e 7,5 ms.\n\
Objetivo: Ec a 0,40 m e resultante das for\xe7as.\n\
1. v = 0,0100 / 0,0106 = 0,943 m s\u207b\xb9\n\
2. Ec = \xbd \xd7 0,500 \xd7 0,943\xb2 = 0,222 J\n\
3. Regress\xe3o Ec(d) com os quatro pontos: declive = 0,554 N\n\
> F(R) \u2248 0,55 N.\n\
Verifica\xe7\xe3o: r \u2248 1: a energia cin\xe9tica \xe9 proporcional \xe0 dist\xe2ncia.\n\
@G\n\
O declive mede a resultante, que n\xe3o depende da massa da tira nem de d.\n\
Com mais atrito, o declive seria menor.\n\
@H\n\
- Usar \u0394t em ms ou L em cm sem converter.\n\
- Empurrar o carrinho ao largar.\n\
- Medir d a pontos diferentes do carrinho.\n\
- Ler o declive como uma energia.\n\
@I\n\
- v = L / \u0394t.\n\
- Ec = \xbd m v\xb2.\n\
- Ec(d): reta; declive = F(R).\n\
@J\n\
Se o declive de Ec(d) for 0,30 N, qual \xe9 a intensidade da resultante das for\xe7as?\n\
@R\n\
F(R) = 0,30 N: o declive de Ec(d) \xe9 a resultante (teorema da energia cin\xe9tica).\n\
@L af12|AL 1.2 Movimento vertical de queda e de ressalto de uma bola|al 1.2 queda ressalto bola altura\
 energia mecanica energia dissipada grafico regressao coeficiente|c_alf1.ress|10|n\xfacleo|f1e:For\xe7as\
 n\xe3o conservativas, pot\xeancia e rendimento|m2h:Dados bivariados: correla\xe7\xe3o e reta dos m\xednimos\
 quadrados|Programa e AE FQ A 10.\xba, AL 1.2\n\
@A\n\
- Medir alturas de queda e de ressalto.\n\
- Relacionar a altura de ressalto com a de queda (gr\xe1fico).\n\
- Calcular a percentagem de energia dissipada no ressalto.\n\
@B\n\
Uma bola nunca volta \xe0 altura de onde caiu: em cada ressalto perde energia mec\xe2nica.\n\
@C\n\
- Material: bola, fita m\xe9trica ou r\xe9gua de 2 m, c\xe2mara de v\xeddeo ou telem\xf3vel.\n\
- No ponto mais alto, Ec = 0 e Em = Epg = m g h.\n\
- Fra\xe7\xe3o de energia que fica: h(r) / h(q).\n\
- Energia dissipada = (1 - h(r) / h(q)) \xd7 100 %.\n\
- Gr\xe1fico h(r) em fun\xe7\xe3o de h(q): uma reta que passa quase na origem.\n\
@D\n\
1. Larga a bola de v\xe1rias alturas, sem a empurrar.\n\
2. Mede a altura do primeiro ressalto (filmar ajuda).\n\
3. Faz tr\xeas ensaios por altura e usa a m\xe9dia.\n\
4. Faz o gr\xe1fico h(r) = k h(q) e determina o declive k.\n\
5. Calcula a energia dissipada: (1 - k) \xd7 100 %.\n\
A percentagem depende da bola e do ch\xe3o (relva, cimento, madeira).\n\
A energia dissipada passa a energia interna da bola e do ch\xe3o e a som.\n\
@F Energia dissipada no ressalto|Ed (%) = (1 - h(r) / h(q)) \xd7 100 %|h(q): altura de queda;h(r): altura de\
 ressalto|resist\xeancia do ar desprez\xe1vel|h(q) = 1,00 m e h(r) = 0,72 m: 28 %|c_alf1.ress\n\
@F\n\
Dados: uma bola de 57 g cai de 1,00 m e ressalta at\xe9 0,72 m; g = 10 m s\u207b\xb2.\n\
Objetivo: energia mec\xe2nica antes e depois e percentagem dissipada.\n\
1. Em(antes) = 0,057 \xd7 10 \xd7 1,00 = 0,57 J\n\
2. Em(depois) = 0,057 \xd7 10 \xd7 0,72 = 0,41 J\n\
3. Dissipada: (1 - 0,72 / 1,00) \xd7 100 = 28 %\n\
> Dissipam-se 28 % da energia em cada ressalto.\n\
Verifica\xe7\xe3o: 0,57 - 0,41 = 0,16 J, que \xe9 28 % de 0,57 J.\n\
@G\n\
O declive k \xe9 o mesmo para todas as alturas: a fra\xe7\xe3o dissipada \xe9 constante.\n\
Uma bola de t\xe9nis e uma de pingue-pongue t\xeam k diferentes.\n\
@H\n\
- Medir a altura do ressalto pelo topo da bola numa vez e pela base noutra.\n\
- Empurrar a bola ao largar.\n\
- Achar que a energia dissipada desaparece.\n\
- Usar s\xf3 um ensaio por altura.\n\
@I\n\
- Em no ponto mais alto = m g h.\n\
- h(r) = k h(q).\n\
- Dissipada = (1 - k) \xd7 100 %.\n\
@J\n\
Uma bola cai de 2,00 m e ressalta at\xe9 1,50 m. Que percentagem de energia se dissipa?\n\
@R\n\
(1 - 1,50 / 2,00) \xd7 100 = 25 %.\n\
@L af21|AL 2.1 Caracter\xedsticas de uma pilha|al 2.1 pilha forca eletromotriz resistencia interna curva\
 caracteristica reostato amperimetro voltimetro regressao linear|c_alf1.pilha|10|n\xfacleo|f2d:Geradores:\
 for\xe7a eletromotriz e resist\xeancia interna|m4c:Fun\xe7\xe3o afim;m5c:Sinal, monotonia, extremos e\
 inequa\xe7\xf5es|Programa e AE FQ A 10.\xba, AL 2.1\n\
@A\n\
- Montar um circuito para medir a tens\xe3o e a corrente de uma pilha.\n\
- Tra\xe7ar a curva caracter\xedstica U(I).\n\
- Determinar a for\xe7a eletromotriz e a resist\xeancia interna por regress\xe3o.\n\
@B\n\
Uma pilha \"cansa-se\" quando lhe pedimos muita corrente: a tens\xe3o nos terminais desce.\n\
@C\n\
- Material: pilha, re\xf3stato, amper\xedmetro, volt\xedmetro, interruptor e fios.\n\
- U = \u03b5 - r I: reta de declive -r e ordenada na origem \u03b5.\n\
- Amper\xedmetro em s\xe9rie; volt\xedmetro em paralelo com a pilha.\n\
@D\n\
1. Monta em s\xe9rie a pilha, o interruptor, o amper\xedmetro e o re\xf3stato.\n\
2. Liga o volt\xedmetro aos terminais da pilha.\n\
3. Varia o re\xf3stato e regista pares (I, U).\n\
4. Fecha o circuito s\xf3 durante as leituras, para a pilha n\xe3o aquecer.\n\
5. Faz o gr\xe1fico U(I) e a reta de regress\xe3o.\n\
6. \u03b5 = ordenada na origem; r = sim\xe9trico do declive.\n\
Nunca ligues a pilha em curto-circuito.\n\
@F Curva caracter\xedstica de um gerador|U = \u03b5 - r I|\u03b5: for\xe7a eletromotriz (V);r: resist\xeancia\
 interna (\u03a9)|gerador de tens\xe3o cont\xednua|U = -1,44 I + 4,47: \u03b5 = 4,47 V e r = 1,44 \u03a9|c_alf1.pilha\n\
@F\n\
Dados (I em mA; U em V): (50; 4,40), (100; 4,32), (150; 4,26), (200; 4,18), (250; 4,11).\n\
Objetivo: for\xe7a eletromotriz e resist\xeancia interna.\n\
1. Regress\xe3o com I em A: U = -1,44 I + 4,47\n\
2. \u03b5 = 4,47 V e r = 1,4 \u03a9\n\
> \u03b5 \u2248 4,47 V e r \u2248 1,4 \u03a9.\n\
Verifica\xe7\xe3o: os pontos est\xe3o todos perto da reta (r de correla\xe7\xe3o pr\xf3ximo de -1).\n\
@G\n\
A resist\xeancia interna explica a descida da tens\xe3o quando a corrente aumenta.\n\
Uma pilha gasta tem r maior.\n\
@H\n\
- Ligar o volt\xedmetro em s\xe9rie.\n\
- Deixar o circuito fechado muito tempo (a pilha aquece e r muda).\n\
- Usar I em mA no declive sem converter.\n\
- Ler r como o declive (\xe9 o sim\xe9trico).\n\
@I\n\
- U = \u03b5 - r I.\n\
- \u03b5: ordenada na origem.\n\
- r: sim\xe9trico do declive.\n\
@J\n\
A reta de regress\xe3o de uma pilha \xe9 U = -0,50 I + 1,52 (SI). Quais s\xe3o \u03b5 e r?\n\
@R\n\
\u03b5 = 1,52 V e r = 0,50 \u03a9.\n\
@L af31|AL 3.1 Radia\xe7\xe3o e pot\xeancia el\xe9trica de um painel fotovoltaico|al 3.1 painel fotovoltaico\
 potencia eletrica resistencia de carga potencia maxima irradiancia rendimento angulo de\
 incidencia|c_alf2.painel|10|n\xfacleo|f3b:Calor, trabalho e radia\xe7\xe3o; irradi\xe2ncia e pain\xe9is\
 fotovoltaicos||Programa e AE FQ A 10.\xba, AL 3.1\n\
@A\n\
- Medir a pot\xeancia el\xe9trica de um painel para v\xe1rias resist\xeancias.\n\
- Encontrar a resist\xeancia para a qual a pot\xeancia \xe9 m\xe1xima.\n\
- Calcular o rendimento do painel.\n\
- Investigar o efeito do \xe2ngulo de incid\xeancia da radia\xe7\xe3o.\n\
@B\n\
Um painel solar n\xe3o d\xe1 sempre a mesma pot\xeancia: depende da luz e do que se lhe liga.\n\
@C\n\
- Material: pequeno painel fotovoltaico, l\xe2mpada (ou Sol), re\xf3stato, amper\xedmetro, volt\xedmetro,\
 r\xe9gua e transferidor.\n\
- P = U I.\n\
- Pot\xeancia da radia\xe7\xe3o: P(rad) = Er A.\n\
- \u03b7 = P(el) / P(rad) \xd7 100 %.\n\
@D\n\
1. Ilumina o painel sempre da mesma maneira (dist\xe2ncia e \xe2ngulo fixos).\n\
2. Liga o re\xf3stato ao painel, com o amper\xedmetro em s\xe9rie e o volt\xedmetro em paralelo.\n\
3. Varia a resist\xeancia e regista U e I.\n\
4. Calcula P = U I e encontra o valor m\xe1ximo.\n\
5. Com Er e a \xe1rea do painel, calcula o rendimento.\n\
6. Muda o \xe2ngulo de incid\xeancia e compara as pot\xeancias.\n\
A pot\xeancia \xe9 maior com a radia\xe7\xe3o perpendicular ao painel.\n\
@F Pot\xeancia el\xe9trica|P = U I|U: tens\xe3o (V);I: corrente (A)|qualquer resist\xeancia de carga|2,50 V e\
 54,0 mA: P = 0,135 W|c_alf2.painel\n\
@F Rendimento do painel|\u03b7 = P(el) / (Er A) \xd7 100 %|Er: irradi\xe2ncia (W m\u207b\xb2);A: \xe1rea\
 (m\xb2)|\u03b7 < 100 %|0,135 W de 4,0 W: \u03b7 = 3,4 %|c_alf2.painel\n\
@F\n\
Dados: no ponto de pot\xeancia m\xe1xima, U = 2,50 V e I = 54,0 mA; Er = 800 W m\u207b\xb2; A = 50 cm\xb2.\n\
Objetivo: pot\xeancia el\xe9trica e rendimento.\n\
1. P = 2,50 \xd7 0,0540 = 0,135 W\n\
2. P(rad) = 800 \xd7 50 \xd7 10\u207b\u2074 = 4,0 W\n\
3. \u03b7 = 0,135 / 4,0 \xd7 100 = 3,4 %\n\
> \u03b7 \u2248 3,4 %.\n\
Verifica\xe7\xe3o: os pain\xe9is de laborat\xf3rio, iluminados com l\xe2mpadas, t\xeam rendimentos baixos.\n\
@G\n\
H\xe1 uma resist\xeancia de carga que torna a pot\xeancia m\xe1xima.\n\
Nas casas, os inversores procuram esse ponto automaticamente.\n\
@H\n\
- Mudar a dist\xe2ncia da l\xe2mpada a meio das medi\xe7\xf5es.\n\
- Esquecer de passar a \xe1rea de cm\xb2 para m\xb2.\n\
- Calcular o rendimento com a pot\xeancia de um ponto que n\xe3o \xe9 o m\xe1ximo.\n\
- Trocar os aparelhos de medida.\n\
@I\n\
- P = U I.\n\
- P(rad) = Er A.\n\
- \u03b7 = P(el) / P(rad) \xd7 100 %.\n\
- Pot\xeancia m\xe1xima com radia\xe7\xe3o perpendicular.\n\
@J\n\
Porque \xe9 que a pot\xeancia de um painel diminui quando a radia\xe7\xe3o incide obliquamente?\n\
@R\n\
A mesma \xe1rea do painel recebe menos radia\xe7\xe3o por segundo: a irradi\xe2ncia efetiva \xe9 menor.\n\
@L af32|AL 3.2 Capacidade t\xe9rmica m\xe1ssica|al 3.2 capacidade termica massica bloco calorimetrico\
 resistencia de aquecimento fonte termometro grafico temperatura tempo regressao erro\
 percentual|c_alf2.cap|10|n\xfacleo|f3d:Capacidade t\xe9rmica m\xe1ssica e mudan\xe7as de estado|m2h:Dados\
 bivariados: correla\xe7\xe3o e reta dos m\xednimos quadrados|Programa e AE FQ A 10.\xba, AL 3.2\n\
@A\n\
- Aquecer um bloco met\xe1lico com uma resist\xeancia el\xe9trica.\n\
- Registar \u03b8(t) e fazer a regress\xe3o linear.\n\
- Determinar a capacidade t\xe9rmica m\xe1ssica do metal e o erro percentual.\n\
@B\n\
Para aquecer 1 kg de alum\xednio 1 \xb0C \xe9 preciso muito menos energia do que para 1 kg de \xe1gua.\n\
@C\n\
- Material: bloco calorim\xe9trico (por exemplo, alum\xednio, 1,00 kg), resist\xeancia de aquecimento, fonte,\
 amper\xedmetro, volt\xedmetro, term\xf3metro, cron\xf3metro, isolante.\n\
- E = P \u0394t = U I \u0394t.\n\
- Sem perdas: U I \u0394t = m c \u0394\u03b8.\n\
- Se \u03b8(t) for uma reta de declive a: c = P / (m a).\n\
@D\n\
1. Mede a massa do bloco e isola-o termicamente.\n\
2. Coloca a resist\xeancia e o term\xf3metro nos orif\xedcios (com um pouco de \xf3leo, para melhor contacto).\n\
3. Liga a fonte e regista U, I e \u03b8 de 30 s em 30 s.\n\
4. Faz o gr\xe1fico \u03b8(t) e a reta de regress\xe3o (s\xf3 a zona linear).\n\
5. Calcula c = P / (m a) e o erro percentual.\n\
As perdas para a vizinhan\xe7a fazem o c obtido maior do que o tabelado.\n\
@F Capacidade t\xe9rmica m\xe1ssica (AL)|c = P / (m a)|P = U I (W);m: massa (kg);a: declive de \u03b8(t)\
 (\xb0C s\u207b\xb9)|\u03b8(t) linear, sem perdas|60,0 W, 1,00 kg e a = 0,0670 \xb0C s\u207b\xb9: c = 896 J\
 kg\u207b\xb9 K\u207b\xb9|c_alf2.cap\n\
@F\n\
Dados: m = 1,00 kg; U = 12,0 V; I = 5,00 A; declive de \u03b8(t): a = 0,0670 \xb0C s\u207b\xb9.\n\
Objetivo: c do metal e erro (valor tabelado do alum\xednio: 9,0 \xd7 10\xb2 J kg\u207b\xb9 K\u207b\xb9).\n\
1. P = 12,0 \xd7 5,00 = 60,0 W\n\
2. c = 60,0 / (1,00 \xd7 0,0670) = 896 J kg\u207b\xb9 K\u207b\xb9\n\
3. Erro: |896 - 900| / 900 \xd7 100 = 0,5 %\n\
> c \u2248 896 J kg\u207b\xb9 K\u207b\xb9.\n\
Verifica\xe7\xe3o: valor pr\xf3ximo do alum\xednio, como esperado.\n\
@G\n\
O m\xe9todo sup\xf5e que toda a energia el\xe9trica aquece o bloco.\n\
Um bom isolamento torna o resultado mais exato.\n\
@H\n\
- Usar a parte inicial, n\xe3o linear, do gr\xe1fico.\n\
- Esquecer o isolamento t\xe9rmico.\n\
- Usar a massa em gramas.\n\
- Confundir o declive com a varia\xe7\xe3o total de temperatura.\n\
@I\n\
- E = U I \u0394t.\n\
- U I \u0394t = m c \u0394\u03b8.\n\
- c = P / (m a).\n\
@J\n\
O bloco perde energia para a vizinhan\xe7a. O valor de c obtido fica maior ou menor do que o real?\n\
@R\n\
Maior: a temperatura sobe menos do que devia. O declive a fica menor, logo c = P / (m a) aumenta.\n\
@L af33|AL 3.3 Balan\xe7o energ\xe9tico num sistema termodin\xe2mico|al 3.3 balanco energetico sistema\
 isolado calorimetro gelo fusao entalpia de fusao temperatura de equilibrio erro\
 percentual|c_alf2.fusao|10|n\xfacleo|f3d:Capacidade t\xe9rmica m\xe1ssica e mudan\xe7as de estado||Programa\
 e AE FQ A 10.\xba, AL 3.3\n\
@A\n\
- Medir a temperatura de equil\xedbrio de \xe1gua com gelo num calor\xedmetro.\n\
- Fazer o balan\xe7o energ\xe9tico do sistema.\n\
- Determinar a varia\xe7\xe3o de entalpia de fus\xe3o do gelo e o erro percentual.\n\
@B\n\
P\xf4r gelo num sumo arrefece-o muito: fundir gelo gasta muita energia.\n\
@C\n\
- Material: calor\xedmetro (ou copo de esferovite com tampa), term\xf3metro, balan\xe7a, \xe1gua morna e gelo\
 a 0 \xb0C.\n\
- Sistema isolado: energia cedida = energia recebida.\n\
- m(a) c (\u03b8i - \u03b8f) = m(g) \u0394Hf + m(g) c \u03b8f.\n\
- \u0394Hf tabelado: 3,34 \xd7 10\u2075 J kg\u207b\xb9.\n\
@D\n\
1. Mede a massa de \xe1gua morna e a sua temperatura inicial.\n\
2. Junta gelo a 0 \xb0C, bem escorrido, e tapa.\n\
3. Agita e regista a temperatura m\xednima (equil\xedbrio).\n\
4. Mede a massa final: a massa de gelo \xe9 a diferen\xe7a.\n\
5. Faz o balan\xe7o e calcula \u0394Hf e o erro percentual.\n\
A \xe1gua do gelo fundido tamb\xe9m aquece at\xe9 \u03b8f: n\xe3o esque\xe7as essa parcela.\n\
@F Entalpia de fus\xe3o (balan\xe7o)|\u0394Hf = [m(a) c (\u03b8i - \u03b8f) - m(g) c \u03b8f] / m(g)|m(a):\
 \xe1gua;m(g): gelo (kg);c = 4,18 \xd7 10\xb3 J kg\u207b\xb9 K\u207b\xb9|sistema isolado, gelo a 0\
 \xb0C|250,0 g a 40,0 \xb0C, 60,0 g de gelo, \u03b8f = 16,0 \xb0C: \u0394Hf = 3,51 \xd7 10\u2075 J\
 kg\u207b\xb9|c_alf2.fusao\n\
@F\n\
Dados: 250,0 g de \xe1gua a 40,0 \xb0C; 60,0 g de gelo a 0 \xb0C; \u03b8f = 16,0 \xb0C.\n\
Objetivo: \u0394Hf e erro percentual.\n\
1. Cedida: 0,2500 \xd7 4180 \xd7 24,0 = 2,51 \xd7 10\u2074 J\n\
2. Aquecer o gelo fundido: 0,0600 \xd7 4180 \xd7 16,0 = 4,01 \xd7 10\xb3 J\n\
3. \u0394Hf = (25 080 - 4013) / 0,0600 = 3,51 \xd7 10\u2075 J kg\u207b\xb9\n\
4. Erro: (3,51 - 3,34) / 3,34 \xd7 100 = 5,1 %\n\
> \u0394Hf \u2248 3,51 \xd7 10\u2075 J kg\u207b\xb9 (erro de cerca de 5 %).\n\
Verifica\xe7\xe3o: o valor obtido \xe9 maior do que o tabelado, como acontece quando h\xe1 trocas com a vizinhan\xe7a.\n\
@G\n\
O calor\xedmetro nunca \xe9 perfeito: troca alguma energia com a vizinhan\xe7a.\n\
Gelo mal escorrido traz \xe1gua l\xedquida e falseia a massa de gelo.\n\
@H\n\
- Esquecer a energia para aquecer a \xe1gua do gelo fundido.\n\
- Usar gelo que n\xe3o est\xe1 a 0 \xb0C.\n\
- N\xe3o tapar o calor\xedmetro.\n\
- Ler a temperatura antes do equil\xedbrio.\n\
@I\n\
- Energia cedida = energia recebida.\n\
- Fundir o gelo e depois aquecer a \xe1gua que dele resulta.\n\
- Erro percentual em rela\xe7\xe3o a 3,34 \xd7 10\u2075 J kg\u207b\xb9.\n\
@J\n\
Porque se deve escorrer bem o gelo antes de o juntar \xe0 \xe1gua?\n\
@R\n\
A \xe1gua l\xedquida agarrada ao gelo n\xe3o precisa de fundir: contaria como gelo e falsearia \u0394Hf.\n\
@E 1|afe1|Energia dissipada num ressalto|c_alf1.ress|af12\n\
Enunciado: uma bola cai de 2,00 m e ressalta at\xe9 1,30 m. Que percentagem de energia se dissipa?\n\
Dados: h(q) = 2,00 m; h(r) = 1,30 m.\n\
Resolu\xe7\xe3o:\n\
1. Fra\xe7\xe3o que fica: 1,30 / 2,00 = 0,650\n\
2. Dissipada: (1 - 0,650) \xd7 100 = 35,0 %\n\
Resultado: dissipam-se 35,0 % da energia mec\xe2nica.\n\
Interpreta\xe7\xe3o: no ressalto seguinte, a bola subiria s\xf3 cerca de 0,650 \xd7 1,30 = 0,845 m.\n\
Erros a evitar: dividir h(q) por h(r).\n\
@E 2|afe2|Pot\xeancia m\xe1xima de um painel|c_alf2.painel|af31\n\
Enunciado: um painel deu (U; I) = (1,0 V; 60 mA), (2,0 V; 55 mA), (2,8 V; 45 mA) e (3,2 V; 25 mA).\n\
Determina a pot\xeancia m\xe1xima e a resist\xeancia de carga correspondente.\n\
Resolu\xe7\xe3o:\n\
1. Pot\xeancias: 60 mW, 110 mW, 126 mW e 80 mW\n\
2. M\xe1xima: 126 mW, com U = 2,8 V e I = 45 mA\n\
3. R = 2,8 / 0,045 = 62 \u03a9\n\
Resultado: P(m\xe1x.) \u2248 126 mW, com R \u2248 62 \u03a9.\n\
Interpreta\xe7\xe3o: com resist\xeancias maiores ou menores, a pot\xeancia baixa.\n\
Erros a evitar: escolher o ponto com mais corrente ou com mais tens\xe3o.\n\
@E 3|afe3|Capacidade t\xe9rmica m\xe1ssica do cobre por regress\xe3o|c_alf2.cap|af32\n\
Enunciado: um bloco de cobre de 0,500 kg \xe9 aquecido com 20,0 W.\n\
t (s): 0, 30, 60, 90, 120; \u03b8 (\xb0C): 20,0; 23,2; 26,1; 29,4; 32,5.\n\
Calcula c e o erro percentual (valor tabelado: 385 J kg\u207b\xb9 K\u207b\xb9).\n\
Resolu\xe7\xe3o:\n\
1. Regress\xe3o \u03b8(t): declive a = 0,104 \xb0C s\u207b\xb9\n\
2. c = 20,0 / (0,500 \xd7 0,104) = 385 J kg\u207b\xb9 K\u207b\xb9\n\
3. Erro: |385 - 385| / 385 \xd7 100 \u2248 0,1 %\n\
Resultado: c \u2248 385 J kg\u207b\xb9 K\u207b\xb9.\n\
Interpreta\xe7\xe3o: o isolamento foi muito bom (erro pequeno).\n\
Erros a evitar: usar s\xf3 o primeiro e o \xfaltimo ponto em vez da reta.\n\
"
