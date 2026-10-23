# p_f2.py - M1TR4M: Energia e fen\xf3menos el\xe9tricos (gerado pelo build).
D = "@V 1\n\
@N 5\n\
@T Energia e fen\xf3menos el\xe9tricos\n\
@L f2a|Corrente el\xe9trica, diferen\xe7a de potencial e resist\xeancia|corrente eletrica carga eletrica\
 diferenca de potencial tensao resistencia eletrica lei de ohm condutor ohmico ampere volt ohm amperimetro\
 voltimetro|c_fqci.ohm|10|n\xfacleo|r9c:Eletricidade: circuitos, grandezas el\xe9tricas e\
 pot\xeancia|a7d:Proporcionalidade direta;m4c:Fun\xe7\xe3o afim|AE FQ A 10.\xba, Energia e fen\xf3menos el\xe9tricos\n\
@A\n\
- Definir corrente el\xe9trica e calcul\xe1-la a partir da carga.\n\
- Definir diferen\xe7a de potencial el\xe9trico.\n\
- Definir resist\xeancia el\xe9trica e usar R = U / I.\n\
- Identificar condutores \xf3hmicos.\n\
@B\n\
Num fio ligado a uma pilha, as cargas movem-se de forma organizada: h\xe1 corrente el\xe9trica.\n\
A pilha d\xe1 energia \xe0s cargas; os componentes do circuito recebem essa energia.\n\
A resist\xeancia mede a oposi\xe7\xe3o de um componente \xe0 passagem da corrente.\n\
@C\n\
- Corrente el\xe9trica: I = Q / \u0394t (em A; 1 A = 1 C s\u207b\xb9).\n\
- Sentido convencional: do polo + para o polo -, no circuito exterior.\n\
- Diferen\xe7a de potencial (tens\xe3o): U = E / Q, energia por unidade de carga (1 V = 1 J C\u207b\xb9).\n\
- Resist\xeancia el\xe9trica: R = U / I (em \u03a9; 1 \u03a9 = 1 V A\u207b\xb9).\n\
- Condutor \xf3hmico: R constante a temperatura constante; U(I) \xe9 uma reta pela origem.\n\
@D\n\
Exemplo: 30 C atravessam uma sec\xe7\xe3o de um fio em 1,0 min.\n\
I = 30 / 60 = 0,50 A.\n\
Num metal, quem se move s\xe3o os eletr\xf5es, em sentido contr\xe1rio ao convencional.\n\
Uma pilha de 1,5 V transfere 1,5 J para cada coulomb que a atravessa.\n\
Exemplo: uma l\xe2mpada a 6,0 V \xe9 percorrida por 0,25 A.\n\
R = 6,0 / 0,25 = 24 \u03a9.\n\
O amper\xedmetro liga-se em s\xe9rie; o volt\xedmetro liga-se em paralelo.\n\
Um filamento de l\xe2mpada n\xe3o \xe9 \xf3hmico: R aumenta quando aquece.\n\
Corrente cont\xednua: sentido constante (pilhas); alternada: o sentido muda (rede, 50 Hz).\n\
@F Corrente el\xe9trica|I = Q / \u0394t|Q: carga (C);\u0394t: intervalo de tempo (s)|corrente constante|30 C\
 em 60 s: I = 0,50 A|c_fqci.ohm\n\
@F Diferen\xe7a de potencial|U = E / Q|E: energia transferida (J);Q: carga (C)|entre dois pontos do\
 circuito|1,5 J por coulomb: U = 1,5 V|\n\
@F Resist\xeancia el\xe9trica|R = U / I|U: diferen\xe7a de potencial (V);I: corrente (A)|condutor \xf3hmico:\
 R constante|6,0 V e 0,25 A: R = 24 \u03a9|c_fqci.ohm\n\
@F\n\
Dados: um carregador fornece 2,0 A a uma bateria durante 30 min.\n\
Objetivo: carga transferida e n\xfamero de eletr\xf5es (e = 1,60 \xd7 10\u207b\xb9\u2079 C).\n\
1. \u0394t = 30 \xd7 60 = 1800 s\n\
2. Q = I \u0394t = 2,0 \xd7 1800 = 3,6 \xd7 10\xb3 C\n\
3. N = Q / e = 3600 / 1,60 \xd7 10\u207b\xb9\u2079 = 2,3 \xd7 10\xb2\xb2 eletr\xf5es\n\
> Q = 3,6 \xd7 10\xb3 C, cerca de 2,3 \xd7 10\xb2\xb2 eletr\xf5es.\n\
Verifica\xe7\xe3o: cada eletr\xe3o tem uma carga min\xfascula, por isso s\xe3o precisos muit\xedssimos.\n\
@G\n\
Corrente, tens\xe3o e resist\xeancia s\xe3o as tr\xeas grandezas b\xe1sicas de qualquer circuito.\n\
Saber relacion\xe1-las permite escolher pilhas, fios e componentes.\n\
@H\n\
- Confundir corrente (A) com tens\xe3o (V).\n\
- Ligar o amper\xedmetro em paralelo ou o volt\xedmetro em s\xe9rie.\n\
- Usar o tempo em minutos em I = Q / \u0394t.\n\
- Achar que todos os componentes s\xe3o \xf3hmicos.\n\
@I\n\
- I = Q / \u0394t.\n\
- U = E / Q.\n\
- R = U / I.\n\
- \xd3hmico: R constante; U(I) reta pela origem.\n\
@J\n\
Se a corrente num condutor \xf3hmico duplicar, o que acontece \xe0 diferen\xe7a de potencial nos seus terminais?\n\
@R\n\
Duplica: U = R I e R mant\xe9m-se.\n\
@L f2b|Resistividade e temperatura|resistividade comprimento area de seccao material temperatura fio condutor\
 metais semicondutores termistor|c_fqci.rho|10|n\xfacleo|f2a:Corrente el\xe9trica, diferen\xe7a de potencial\
 e resist\xeancia||AE FQ A 10.\xba, Energia e fen\xf3menos el\xe9tricos\n\
@A\n\
- Relacionar a resist\xeancia com o comprimento e a \xe1rea de um fio.\n\
- Usar a resistividade como propriedade do material.\n\
- Calcular a resist\xeancia de um fio.\n\
- Relacionar a resistividade com a temperatura.\n\
@B\n\
Um fio comprido e fino resiste mais \xe0 corrente do que um curto e grosso.\n\
O material tamb\xe9m conta: o cobre conduz muito melhor do que o ferro.\n\
@C\n\
- R = \u03c1 \u2113 / A.\n\
- \u2113: comprimento (m); A: \xe1rea da sec\xe7\xe3o (m\xb2).\n\
- \u03c1: resistividade, caracter\xedstica do material (\u03a9 m).\n\
- Bons condutores t\xeam \u03c1 pequena (cobre: 1,7 \xd7 10\u207b\u2078 \u03a9 m, a 20 \xb0C).\n\
- Nos metais, \u03c1 aumenta com a temperatura.\n\
- Nos semicondutores, \u03c1 diminui com a temperatura.\n\
@D\n\
Exemplo: fio de cobre com 100 m e sec\xe7\xe3o de 1,5 mm\xb2.\n\
A = 1,5 mm\xb2 = 1,5 \xd7 10\u207b\u2076 m\xb2.\n\
R = 1,7 \xd7 10\u207b\u2078 \xd7 100 / (1,5 \xd7 10\u207b\u2076) = 1,1 \u03a9.\n\
Duplicar o comprimento duplica R; duplicar a \xe1rea reduz R a metade.\n\
Os fios de cobre das casas s\xe3o grossos para R ser pequena e aquecerem pouco.\n\
O filamento quente de uma l\xe2mpada tem mais resist\xeancia do que frio.\n\
Term\xedstores: componentes cuja resist\xeancia varia muito com a temperatura (term\xf3metros eletr\xf3nicos).\n\
1 mm\xb2 = 10\u207b\u2076 m\xb2.\n\
@F Resistividade|R = \u03c1 \u2113 / A|\u03c1: resistividade (\u03a9 m);\u2113: comprimento (m);A: \xe1rea da\
 sec\xe7\xe3o (m\xb2)|fio homog\xe9neo, a temperatura constante|cobre, 100 m e 1,5 mm\xb2: R = 1,1 \u03a9|c_fqci.rho\n\
@F\n\
Dados: fio de n\xedquel-cr\xf3mio (\u03c1 = 1,1 \xd7 10\u207b\u2076 \u03a9 m) com 0,20 mm\xb2 de sec\xe7\xe3o.\n\
Objetivo: comprimento necess\xe1rio para ter R = 22 \u03a9.\n\
1. A = 0,20 \xd7 10\u207b\u2076 = 2,0 \xd7 10\u207b\u2077 m\xb2\n\
2. \u2113 = R A / \u03c1 = 22 \xd7 2,0 \xd7 10\u207b\u2077 / (1,1 \xd7 10\u207b\u2076) = 4,0 m\n\
> \u2113 = 4,0 m.\n\
Verifica\xe7\xe3o: o n\xedquel-cr\xf3mio tem \u03c1 grande, por isso basta pouco fio.\n\
@G\n\
A resistividade explica a escolha dos materiais: cobre para fios, n\xedquel-cr\xf3mio para aquecedores.\n\
@H\n\
- Esquecer de passar mm\xb2 para m\xb2.\n\
- Achar que a resist\xeancia s\xf3 depende do material.\n\
- Trocar \u2113 e A na f\xf3rmula.\n\
- Achar que todos os materiais aumentam R com a temperatura.\n\
@I\n\
- R = \u03c1 \u2113 / A.\n\
- \u03c1 depende do material e da temperatura.\n\
- Metais: \u03c1 aumenta com a temperatura.\n\
@J\n\
Dois fios do mesmo cobre t\xeam o mesmo comprimento; um tem o dobro da \xe1rea do outro. Qual tem menor\
 resist\xeancia?\n\
@R\n\
O de maior \xe1rea: R \xe9 inversamente proporcional a A, por isso tem metade da resist\xeancia.\n\
@L f2c|Circuitos em s\xe9rie e em paralelo|associacao em serie em paralelo resistencia equivalente corrente\
 tensao nos malhas instalacao domestica amperimetro voltimetro|c_fqci.assoc|10|n\xfacleo|f2a:Corrente\
 el\xe9trica, diferen\xe7a de potencial e resist\xeancia||AE FQ A 10.\xba, Energia e fen\xf3menos el\xe9tricos\n\
@A\n\
- Distinguir associa\xe7\xf5es em s\xe9rie e em paralelo.\n\
- Calcular a resist\xeancia equivalente.\n\
- Calcular correntes e tens\xf5es em cada componente.\n\
- Explicar porque \xe9 que as casas usam liga\xe7\xf5es em paralelo.\n\
@B\n\
Numa s\xe9rie, a corrente s\xf3 tem um caminho; em paralelo, divide-se por v\xe1rios.\n\
Em casa, desligar uma l\xe2mpada n\xe3o apaga as outras: est\xe3o em paralelo.\n\
@C\n\
- S\xe9rie: a mesma corrente em todos; U = U1 + U2 + ...\n\
- S\xe9rie: Req = R1 + R2 + ...\n\
- Paralelo: a mesma tens\xe3o em todos; I = I1 + I2 + ...\n\
- Paralelo: 1 / Req = 1 / R1 + 1 / R2 + ...\n\
- Em paralelo, Req \xe9 menor do que a menor das resist\xeancias.\n\
@D\n\
Exemplo em s\xe9rie: 10 \u03a9, 20 \u03a9 e 30 \u03a9 ligadas a 12 V.\n\
Req = 10 + 20 + 30 = 60 \u03a9 e I = 12 / 60 = 0,20 A.\n\
U1 = 10 \xd7 0,20 = 2,0 V; U2 = 4,0 V; U3 = 6,0 V; a soma d\xe1 12 V.\n\
Exemplo em paralelo: 6,0 \u03a9 e 3,0 \u03a9.\n\
1 / Req = 1 / 6,0 + 1 / 3,0 = 0,50 \u03a9\u207b\xb9, logo Req = 2,0 \u03a9.\n\
Em paralelo, a corrente maior passa na resist\xeancia menor.\n\
Nos n\xf3s, a soma das correntes que entram \xe9 igual \xe0 soma das que saem (conserva\xe7\xe3o da carga).\n\
Em casa, todos os aparelhos ficam a 230 V e funcionam de forma independente.\n\
@F Associa\xe7\xe3o em s\xe9rie|Req = R1 + R2 + ...|R1, R2: resist\xeancias (\u03a9)|mesma corrente em\
 todas|10 + 20 + 30 = 60 \u03a9|c_fqci.assoc\n\
@F Associa\xe7\xe3o em paralelo|1 / Req = 1 / R1 + 1 / R2 + ...|R1, R2: resist\xeancias (\u03a9)|mesma\
 tens\xe3o em todas|6,0 \u03a9 e 3,0 \u03a9: Req = 2,0 \u03a9|c_fqci.assoc\n\
@F\n\
Dados: duas l\xe2mpadas de 12 \u03a9 em paralelo, ligadas a 6,0 V.\n\
Objetivo: corrente em cada l\xe2mpada, corrente total e Req.\n\
1. Em cada l\xe2mpada: I = 6,0 / 12 = 0,50 A\n\
2. Corrente total: I = 0,50 + 0,50 = 1,0 A\n\
3. Req = 6,0 / 1,0 = 6,0 \u03a9\n\
> 0,50 A em cada l\xe2mpada; 1,0 A no total; Req = 6,0 \u03a9.\n\
Verifica\xe7\xe3o: duas resist\xeancias iguais em paralelo d\xe3o metade de uma: 12 / 2 = 6,0 \u03a9.\n\
@G\n\
As associa\xe7\xf5es explicam as instala\xe7\xf5es el\xe9tricas e os circuitos dos aparelhos.\n\
Juntar mais aparelhos em paralelo aumenta a corrente total: \xe9 por isso que h\xe1 disjuntores.\n\
@H\n\
- Somar resist\xeancias em paralelo como se fossem em s\xe9rie.\n\
- Esquecer de inverter 1 / Req no fim.\n\
- Achar que em s\xe9rie cada componente tem a tens\xe3o toda.\n\
- Achar que a corrente se \"gasta\" ao longo do circuito.\n\
@I\n\
- S\xe9rie: mesma I; Req = soma.\n\
- Paralelo: mesma U; 1/Req = soma dos inversos.\n\
- N\xf3s: correntes que entram = correntes que saem.\n\
@J\n\
Tr\xeas resist\xeancias de 30 \u03a9 est\xe3o em paralelo. Qual \xe9 a resist\xeancia equivalente?\n\
@R\n\
1 / Req = 3 / 30, logo Req = 10 \u03a9.\n\
@L f2d|Geradores: for\xe7a eletromotriz e resist\xeancia interna|gerador pilha forca eletromotriz resistencia\
 interna tensao nos terminais curto-circuito circuito aberto caracteristica\
 reta|c_fqci.ger|10|n\xfacleo|f2a:Corrente el\xe9trica, diferen\xe7a de potencial e\
 resist\xeancia|m4c:Fun\xe7\xe3o afim|AE FQ A 10.\xba, Energia e fen\xf3menos el\xe9tricos\n\
@A\n\
- Definir for\xe7a eletromotriz de um gerador.\n\
- Relacionar a tens\xe3o nos terminais com a corrente: U = \u03b5 - r I.\n\
- Interpretar o gr\xe1fico U(I) de um gerador.\n\
- Calcular a corrente de curto-circuito.\n\
@B\n\
Uma pilha nova perde um pouco de tens\xe3o quando fornece muita corrente.\n\
Parte da energia fica na pr\xf3pria pilha, que tem uma resist\xeancia interna.\n\
@C\n\
- For\xe7a eletromotriz, \u03b5: energia que o gerador fornece por unidade de carga (V).\n\
- Resist\xeancia interna, r: resist\xeancia do pr\xf3prio gerador (\u03a9).\n\
- Tens\xe3o nos terminais: U = \u03b5 - r I.\n\
- Circuito aberto (I = 0): U = \u03b5.\n\
- Curto-circuito (U = 0): I = \u03b5 / r.\n\
@D\n\
Exemplo: pilha com \u03b5 = 9,0 V e r = 1,5 \u03a9 a fornecer 0,40 A.\n\
U = 9,0 - 1,5 \xd7 0,40 = 8,4 V.\n\
Curto-circuito: I = 9,0 / 1,5 = 6,0 A (perigoso: a pilha aquece muito).\n\
O gr\xe1fico U(I) \xe9 uma reta: ordenada na origem \u03b5 e declive -r.\n\
Com pares (I, U) medidos, a regress\xe3o linear d\xe1 \u03b5 e r (AL 2.1).\n\
Ligando o gerador a uma resist\xeancia R: I = \u03b5 / (R + r).\n\
Um gerador ideal teria r = 0 e U = \u03b5 sempre.\n\
@F Gerador|U = \u03b5 - r I|\u03b5: for\xe7a eletromotriz (V);r: resist\xeancia interna (\u03a9);I: corrente\
 (A)|gerador de tens\xe3o cont\xednua|9,0 V, 1,5 \u03a9 e 0,40 A: U = 8,4 V|c_fqci.ger\n\
@F Corrente de curto-circuito|I = \u03b5 / r|\u03b5: for\xe7a eletromotriz (V);r: resist\xeancia interna\
 (\u03a9)|terminais ligados sem resist\xeancia|9,0 V e 1,5 \u03a9: I = 6,0 A|c_fqci.ger\n\
@F\n\
Dados: uma pilha d\xe1 U = 1,40 V com I = 0,20 A e U = 1,30 V com I = 0,60 A.\n\
Objetivo: for\xe7a eletromotriz e resist\xeancia interna.\n\
1. r = (1,40 - 1,30) / (0,60 - 0,20) = 0,25 \u03a9\n\
2. \u03b5 = U + r I = 1,40 + 0,25 \xd7 0,20 = 1,45 V\n\
> \u03b5 = 1,45 V e r = 0,25 \u03a9.\n\
Verifica\xe7\xe3o: 1,45 - 0,25 \xd7 0,60 = 1,30 V, como medido.\n\
@G\n\
A resist\xeancia interna explica porque \xe9 que uma pilha aquece e perde tens\xe3o quando lhe pedimos muita corrente.\n\
@H\n\
- Achar que a tens\xe3o nos terminais \xe9 sempre igual a \u03b5.\n\
- Trocar o sinal: U = \u03b5 + r I num gerador.\n\
- Ler o declive do gr\xe1fico como +r.\n\
- Esquecer a resist\xeancia interna em I = \u03b5 / (R + r).\n\
@I\n\
- U = \u03b5 - r I.\n\
- Circuito aberto: U = \u03b5.\n\
- Curto-circuito: I = \u03b5 / r.\n\
- Gr\xe1fico U(I): declive -r, ordenada \u03b5.\n\
@J\n\
Uma pilha tem \u03b5 = 4,5 V e r = 1,5 \u03a9. Qual \xe9 a tens\xe3o nos terminais quando a corrente \xe9 nula?\n\
@R\n\
U = \u03b5 = 4,5 V: sem corrente, n\xe3o h\xe1 perda na resist\xeancia interna.\n\
@L f2e|Efeito Joule, pot\xeancia e energia el\xe9trica|efeito joule potencia eletrica energia eletrica\
 quilowatt-hora custo conservacao da energia rendimento aquecimento\
 disjuntor|c_fqci.pot|10|n\xfacleo|f2d:Geradores: for\xe7a eletromotriz e resist\xeancia interna|m5a:A\
 fun\xe7\xe3o quadr\xe1tica e o seu gr\xe1fico|AE FQ A 10.\xba, Energia e fen\xf3menos el\xe9tricos\n\
@A\n\
- Calcular a pot\xeancia el\xe9trica: P = U I.\n\
- Explicar o efeito Joule e usar P = R I\xb2.\n\
- Calcular a energia el\xe9trica em J e em kWh e o seu custo.\n\
- Aplicar a conserva\xe7\xe3o da energia a um circuito.\n\
@B\n\
Um aquecedor, uma torradeira e um ferro de engomar aquecem porque a corrente passa numa resist\xeancia.\n\
A fatura da luz cobra a energia, em kWh, n\xe3o a pot\xeancia.\n\
@C\n\
- Pot\xeancia el\xe9trica: P = U I (em W).\n\
- Efeito Joule: P = R I\xb2 (energia el\xe9trica passa a energia interna).\n\
- Tamb\xe9m P = U\xb2 / R.\n\
- Energia: E = P \u0394t; 1 kWh = 3,6 \xd7 10\u2076 J.\n\
- Conserva\xe7\xe3o: a pot\xeancia do gerador, \u03b5 I, \xe9 igual \xe0 soma das pot\xeancias nos\
 componentes, incluindo r I\xb2.\n\
- Rendimento de um gerador: \u03b7 = U / \u03b5.\n\
@D\n\
Exemplo: aquecedor de 46 \u03a9 ligado a 230 V.\n\
P = 230\xb2 / 46 = 1,2 \xd7 10\xb3 W.\n\
Em 2,0 h: E = 1,15 \xd7 2,0 = 2,3 kWh.\n\
A 0,16 \u20ac por kWh, o custo \xe9 2,3 \xd7 0,16 = 0,37 \u20ac.\n\
Exemplo de conserva\xe7\xe3o: pilha com \u03b5 = 9,0 V, r = 1,5 \u03a9 e I = 0,40 A.\n\
\u03b5 I = 3,6 W; r I\xb2 = 0,24 W; U I = 8,4 \xd7 0,40 = 3,4 W.\n\
3,6 W = 0,24 W + 3,36 W: a energia conserva-se.\n\
O efeito Joule \xe9 \xfatil em aquecedores e indesejado nos fios e nos computadores.\n\
@F Pot\xeancia el\xe9trica|P = U I|U: tens\xe3o (V);I: corrente (A)|qualquer componente|230 V e 5,0 A: P =\
 1,2 \xd7 10\xb3 W|c_fqci.pot\n\
@F Efeito Joule|P = R I\xb2|R: resist\xeancia (\u03a9);I: corrente (A)|pot\xeancia dissipada numa\
 resist\xeancia|10 \u03a9 e 2,0 A: P = 40 W|c_fqci.pot\n\
@F Energia el\xe9trica|E = P \u0394t|P: pot\xeancia (W ou kW);\u0394t: tempo (s ou h)|1 kWh = 3,6 \xd7\
 10\u2076 J|1,15 kW durante 2,0 h: E = 2,3 kWh|c_fqci.pot\n\
@F\n\
Dados: uma resist\xeancia de 10 \u03a9 \xe9 percorrida por 2,0 A durante 5,0 min.\n\
Objetivo: pot\xeancia e energia dissipadas.\n\
1. P = R I\xb2 = 10 \xd7 2,0\xb2 = 40 W\n\
2. \u0394t = 5,0 \xd7 60 = 3,0 \xd7 10\xb2 s\n\
3. E = P \u0394t = 40 \xd7 300 = 1,2 \xd7 10\u2074 J\n\
> P = 40 W e E = 1,2 \xd7 10\u2074 J.\n\
Verifica\xe7\xe3o: em kWh, 12 000 / 3,6 \xd7 10\u2076 \u2248 0,0033 kWh, um valor pequeno.\n\
@G\n\
A pot\xeancia diz a rapidez com que a energia \xe9 transferida; a energia \xe9 o que se paga.\n\
Poupar energia \xe9 usar menos pot\xeancia ou durante menos tempo.\n\
@H\n\
- Confundir pot\xeancia (W) com energia (J ou kWh).\n\
- Usar \u0394t em minutos com P em W para obter J.\n\
- Esquecer o quadrado em R I\xb2.\n\
- Achar que o kWh \xe9 uma unidade de pot\xeancia.\n\
@I\n\
- P = U I = R I\xb2 = U\xb2 / R.\n\
- E = P \u0394t; 1 kWh = 3,6 \xd7 10\u2076 J.\n\
- \u03b5 I = r I\xb2 + U I.\n\
- \u03b7(gerador) = U / \u03b5.\n\
@J\n\
Uma l\xe2mpada de 10 W est\xe1 acesa 5,0 h por dia durante 30 dias. Quanta energia gasta, em kWh?\n\
@R\n\
E = 0,010 \xd7 5,0 \xd7 30 = 1,5 kWh.\n\
@E 1|f2e1|Resist\xeancia e pot\xeancia de uma l\xe2mpada|c_fqci.ohm|f2a\n\
Enunciado: uma l\xe2mpada ligada a 230 V \xe9 percorrida por 0,26 A. Calcula a resist\xeancia e a pot\xeancia.\n\
Dados: U = 230 V; I = 0,26 A.\n\
Resolu\xe7\xe3o:\n\
1. R = U / I = 230 / 0,26 = 8,8 \xd7 10\xb2 \u03a9\n\
2. P = U I = 230 \xd7 0,26 = 60 W\n\
Resultado: R \u2248 8,8 \xd7 10\xb2 \u03a9 e P \u2248 60 W.\n\
Interpreta\xe7\xe3o: \xe9 uma l\xe2mpada de cerca de 60 W.\n\
Erros a evitar: dar mais algarismos significativos do que os de 0,26 A (2).\n\
@E 2|f2e2|Pilha com resist\xeancia interna ligada a uma resist\xeancia|c_fqci.ger|f2d\n\
Enunciado: uma pilha com \u03b5 = 4,5 V e r = 1,5 \u03a9 alimenta uma resist\xeancia de 7,5 \u03a9.\n\
Calcula a corrente, a tens\xe3o nos terminais e o rendimento da pilha.\n\
Resolu\xe7\xe3o:\n\
1. I = \u03b5 / (R + r) = 4,5 / (7,5 + 1,5) = 0,50 A\n\
2. U = \u03b5 - r I = 4,5 - 1,5 \xd7 0,50 = 3,8 V\n\
3. \u03b7 = U / \u03b5 = 3,75 / 4,5 \xd7 100 = 83 %\n\
Resultado: I = 0,50 A, U \u2248 3,8 V e \u03b7 \u2248 83 %.\n\
Interpreta\xe7\xe3o: cerca de 17 % da energia fica na pilha (efeito Joule em r).\n\
Erros a evitar: usar I = \u03b5 / R, esquecendo a resist\xeancia interna.\n\
@E 3|f2e3|Quanto custa um aquecedor?|c_fqci.pot|f2e\n\
Enunciado: um aquecedor de 2,0 kW funciona 3,0 h por dia durante 30 dias. Considera 0,16 \u20ac por kWh.\n\
Calcula a energia gasta (em kWh e em J) e o custo.\n\
Resolu\xe7\xe3o:\n\
1. Tempo total: 3,0 \xd7 30 = 90 h\n\
2. E = 2,0 \xd7 90 = 1,8 \xd7 10\xb2 kWh\n\
3. Em joules: 180 \xd7 3,6 \xd7 10\u2076 = 6,5 \xd7 10\u2078 J\n\
4. Custo: 180 \xd7 0,16 = 29 \u20ac\n\
Resultado: 1,8 \xd7 10\xb2 kWh, cerca de 6,5 \xd7 10\u2078 J, e cerca de 29 \u20ac.\n\
Interpreta\xe7\xe3o: reduzir uma hora por dia poupa cerca de 9,6 \u20ac por m\xeas.\n\
Erros a evitar: multiplicar a pot\xeancia em W pelo tempo em horas e chamar-lhe kWh.\n\
"
