# p_q2.py - M1TR4M: Energia dos eletr\u00f5es nos \u00e1tomos (gerado pelo build).
D = "@V 1\n\
@N 5\n\
@T Energia dos eletr\u00f5es nos \u00e1tomos\n\
@L q2a|Espetros e radia\u00e7\u00e3o eletromagn\u00e9tica|espetro continuo descontinuo emissao absorcao\
 radiacao eletromagnetica fotao frequencia comprimento de onda e = h f c = lambda f teste de\
 chama|c_fqel.fot|10|n\u00facleo|||AE FQ A 10.\u00ba, Energia dos eletr\u00f5es nos \u00e1tomos\n\
@A\n\
- Distinguir espetros cont\u00ednuos de descont\u00ednuos (de riscas).\n\
- Distinguir espetros de emiss\u00e3o de espetros de absor\u00e7\u00e3o.\n\
- Ordenar as regi\u00f5es do espetro eletromagn\u00e9tico.\n\
- Relacionar energia, frequ\u00eancia e comprimento de onda.\n\
- Usar E = h f e c = \u03bb f.\n\
@B\n\
A luz branca, num prisma, abre-se num arco-\u00edris cont\u00ednuo: \u00e9 um espetro cont\u00ednuo.\n\
A luz de um g\u00e1s aquecido s\u00f3 tem algumas cores: \u00e9 um espetro de riscas.\n\
Cada elemento tem as suas riscas, como uma impress\u00e3o digital. Assim se identificam elementos nas estrelas.\n\
@C\n\
- Radia\u00e7\u00e3o eletromagn\u00e9tica: energia transportada por fot\u00f5es.\n\
- Espetro cont\u00ednuo: todas as cores (s\u00f3lido incandescente).\n\
- Espetro descont\u00ednuo (de riscas): s\u00f3 algumas cores (gases).\n\
- Emiss\u00e3o: riscas coloridas; absor\u00e7\u00e3o: riscas escuras.\n\
- E = h f, com h = 6,63 \u00d7 10\u207b\u00b3\u2074 J s (constante de Planck).\n\
- c = \u03bb f, com c = 3,00 \u00d7 10\u2078 m s\u207b\u00b9 no v\u00e1cuo.\n\
@D\n\
Por ordem crescente de energia (e de frequ\u00eancia):\n\
- ondas de r\u00e1dio, micro-ondas, infravermelho (IV);\n\
- vis\u00edvel (de cerca de 700 nm a 400 nm);\n\
- ultravioleta (UV), raios X e raios gama.\n\
O comprimento de onda segue a ordem contr\u00e1ria.\n\
A luz vis\u00edvel vai do vermelho (menos energia) ao violeta (mais energia).\n\
Para o mesmo elemento, as riscas de emiss\u00e3o e de absor\u00e7\u00e3o est\u00e3o nas mesmas posi\u00e7\u00f5es.\n\
O \u00e1tomo absorve e emite fot\u00f5es com as mesmas energias.\n\
No teste de chama, os eletr\u00f5es excitados emitem luz ao regressar a n\u00edveis mais baixos.\n\
A cor da chama identifica o elemento: o s\u00f3dio d\u00e1 amarelo-alaranjado.\n\
Os limites das regi\u00f5es s\u00e3o aproximados e variam um pouco entre livros.\n\
@F Energia de um fot\u00e3o|E = h f|E: energia do fot\u00e3o (J);h: constante de Planck, 6,63 \u00d7\
 10\u207b\u00b3\u2074 J s;f: frequ\u00eancia (Hz)|qualquer radia\u00e7\u00e3o eletromagn\u00e9tica|f = 5,00\
 \u00d7 10\u00b9\u2074 Hz: E = 3,32 \u00d7 10\u207b\u00b9\u2079 J|c_fqel.fot\n\
@F Velocidade da luz|c = \u03bb f|c: 3,00 \u00d7 10\u2078 m s\u207b\u00b9 (v\u00e1cuo);\u03bb: comprimento de\
 onda (m);f: frequ\u00eancia (Hz)|radia\u00e7\u00e3o no v\u00e1cuo (no ar, quase igual)|\u03bb = 600 nm: f =\
 5,00 \u00d7 10\u00b9\u2074 Hz|c_fqel.fot\n\
@F\n\
Dados: a luz amarela do s\u00f3dio tem \u03bb = 589 nm.\n\
Objetivo: frequ\u00eancia e energia de um fot\u00e3o.\n\
1. \u03bb = 589 nm = 5,89 \u00d7 10\u207b\u2077 m\n\
2. f = c / \u03bb = 3,00 \u00d7 10\u2078 / 5,89 \u00d7 10\u207b\u2077 = 5,09 \u00d7 10\u00b9\u2074 Hz\n\
3. E = h f = h c / \u03bb = 6,63 \u00d7 10\u207b\u00b3\u2074 \u00d7 3,00 \u00d7 10\u2078 / 5,89 \u00d7\
 10\u207b\u2077 = 3,38 \u00d7 10\u207b\u00b9\u2079 J\n\
> f = 5,09 \u00d7 10\u00b9\u2074 Hz e E = 3,38 \u00d7 10\u207b\u00b9\u2079 J\n\
Verifica\u00e7\u00e3o: est\u00e1 entre o vermelho e o violeta (vis\u00edvel).\n\
@G\n\
Um fot\u00e3o de UV tem mais energia do que um de luz vis\u00edvel. Por isso o UV pode danificar a pele.\n\
A energia de um fot\u00e3o depende s\u00f3 da frequ\u00eancia, n\u00e3o da intensidade da luz.\n\
Uma luz mais intensa tem mais fot\u00f5es, n\u00e3o fot\u00f5es mais energ\u00e9ticos.\n\
@H\n\
- Esquecer de passar nm para m (1 nm = 10\u207b\u2079 m).\n\
- Achar que maior comprimento de onda d\u00e1 mais energia: d\u00e1 menos.\n\
- Trocar emiss\u00e3o (riscas claras) com absor\u00e7\u00e3o (riscas escuras).\n\
- Confundir intensidade da luz com energia de cada fot\u00e3o.\n\
- Usar c = \u03bb f com \u03bb em nm e c em m s\u207b\u00b9.\n\
@I\n\
- Cont\u00ednuo: todas as cores; de riscas: s\u00f3 algumas.\n\
- Emiss\u00e3o: riscas claras; absor\u00e7\u00e3o: riscas escuras.\n\
- Energia crescente: r\u00e1dio, micro-ondas, IV, vis\u00edvel, UV, X, gama.\n\
- E = h f e c = \u03bb f.\n\
- Maior frequ\u00eancia: mais energia, menor \u03bb.\n\
@J\n\
Um fot\u00e3o tem \u03bb = 400 nm. Calcula a sua energia.\n\
@R\n\
f = 3,00 \u00d7 10\u2078 / 4,00 \u00d7 10\u207b\u2077 = 7,50 \u00d7 10\u00b9\u2074 Hz.\n\
E = 6,63 \u00d7 10\u207b\u00b3\u2074 \u00d7 7,50 \u00d7 10\u00b9\u2074 = 4,97 \u00d7 10\u207b\u00b9\u2079 J.\n\
@L q2b|Quantiza\u00e7\u00e3o da energia e \u00e1tomo de hidrog\u00e9nio|quantizacao niveis de energia modelo\
 de bohr atomo de hidrogenio transicao excitacao desexcitacao ionizacao lyman balmer paschen estado\
 fundamental|c_fqel.hid|10|n\u00facleo|q2a:Espetros e radia\u00e7\u00e3o eletromagn\u00e9tica||AE FQ A\
 10.\u00ba, Energia dos eletr\u00f5es nos \u00e1tomos\n\
@A\n\
- Explicar que a energia do eletr\u00e3o est\u00e1 quantizada.\n\
- Calcular a energia de um n\u00edvel do \u00e1tomo de hidrog\u00e9nio.\n\
- Relacionar transi\u00e7\u00f5es com emiss\u00e3o ou absor\u00e7\u00e3o de fot\u00f5es.\n\
- Associar as s\u00e9ries de Lyman, Balmer e Paschen a regi\u00f5es do espetro.\n\
- Calcular a energia de ioniza\u00e7\u00e3o a partir de um n\u00edvel.\n\
@B\n\
Imagina uma escada: s\u00f3 podes estar num degrau, nunca entre dois.\n\
No \u00e1tomo, o eletr\u00e3o s\u00f3 pode ter certas energias: os n\u00edveis.\n\
Para subir um degrau, absorve energia; ao descer, emite um fot\u00e3o.\n\
Como os degraus s\u00e3o fixos, os fot\u00f5es s\u00f3 t\u00eam certas energias: da\u00ed as riscas.\n\
@C\n\
- Energia quantizada: s\u00f3 pode ter certos valores.\n\
- N\u00edvel n (n = 1, 2, 3...): E\u2099 = -2,18 \u00d7 10\u207b\u00b9\u2078 / n\u00b2 J.\n\
- Estado fundamental: n = 1 (energia m\u00ednima).\n\
- Estados excitados: n \u2265 2.\n\
- Energia do fot\u00e3o: E = |E final - E inicial|.\n\
- Ioniza\u00e7\u00e3o: o eletr\u00e3o vai para n = \u221e, onde E = 0.\n\
@D\n\
As energias dos n\u00edveis s\u00e3o negativas: o eletr\u00e3o est\u00e1 ligado ao n\u00facleo.\n\
E\u2081 = -2,18 \u00d7 10\u207b\u00b9\u2078 J; E\u2082 = -5,45 \u00d7 10\u207b\u00b9\u2079 J; E\u2083 = -2,42\
 \u00d7 10\u207b\u00b9\u2079 J.\n\
Os n\u00edveis ficam mais pr\u00f3ximos \u00e0 medida que n aumenta.\n\
Desexcita\u00e7\u00e3o (descer de n\u00edvel): emite um fot\u00e3o.\n\
Excita\u00e7\u00e3o (subir de n\u00edvel): absorve um fot\u00e3o com a energia exata.\n\
S\u00e9ries de riscas de emiss\u00e3o, conforme o n\u00edvel final:\n\
- Lyman: final n = 1, no ultravioleta;\n\
- Balmer: final n = 2, no vis\u00edvel (e algum UV);\n\
- Paschen: final n = 3, no infravermelho.\n\
A risca vermelha de Balmer vem da transi\u00e7\u00e3o 3 \u2192 2.\n\
A energia de ioniza\u00e7\u00e3o a partir de n = 1 \u00e9 2,18 \u00d7 10\u207b\u00b9\u2078 J.\n\
Um fot\u00e3o com energia entre dois n\u00edveis n\u00e3o \u00e9 absorvido.\n\
@F Energia de um n\u00edvel (H)|E\u2099 = -2,18 \u00d7 10\u207b\u00b9\u2078 / n\u00b2 J|n: n\u00famero do\
 n\u00edvel (1, 2, 3...);E\u2099: energia do eletr\u00e3o no n\u00edvel n|s\u00f3 para o \u00e1tomo de\
 hidrog\u00e9nio|E\u2082 = -2,18 \u00d7 10\u207b\u00b9\u2078 / 4 = -5,45 \u00d7 10\u207b\u00b9\u2079 J|c_fqel.hid\n\
@F Energia do fot\u00e3o numa transi\u00e7\u00e3o|E fot\u00e3o = \u2223E final - E inicial\u2223|E final, E\
 inicial: energias dos n\u00edveis|emiss\u00e3o (desce) ou absor\u00e7\u00e3o (sobe)|3 \u2192 2: 3,03 \u00d7\
 10\u207b\u00b9\u2079 J|c_fqel.hid\n\
@F\n\
Dados: transi\u00e7\u00e3o do eletr\u00e3o de n = 4 para n = 2 no hidrog\u00e9nio.\n\
Objetivo: energia e comprimento de onda do fot\u00e3o emitido.\n\
1. E\u2084 = -2,18 \u00d7 10\u207b\u00b9\u2078 / 16 = -1,363 \u00d7 10\u207b\u00b9\u2079 J\n\
2. E\u2082 = -2,18 \u00d7 10\u207b\u00b9\u2078 / 4 = -5,45 \u00d7 10\u207b\u00b9\u2079 J\n\
3. E fot\u00e3o = |E\u2082 - E\u2084| = 4,09 \u00d7 10\u207b\u00b9\u2079 J\n\
4. \u03bb = h c / E = 4,87 \u00d7 10\u207b\u2077 m = 487 nm\n\
> Fot\u00e3o de 4,09 \u00d7 10\u207b\u00b9\u2079 J (487 nm): risca azul-esverdeada de Balmer.\n\
Verifica\u00e7\u00e3o: o n\u00edvel final \u00e9 n = 2 (s\u00e9rie de Balmer, vis\u00edvel).\n\
O valor medido \u00e9 486 nm: o modelo de Bohr acerta muito bem.\n\
@G\n\
As riscas provam que a energia no \u00e1tomo est\u00e1 quantizada.\n\
O modelo de Bohr explica bem o hidrog\u00e9nio, mas falha em \u00e1tomos com mais eletr\u00f5es.\n\
Hoje usa-se o modelo da nuvem eletr\u00f3nica.\n\
@H\n\
- Esquecer o sinal menos das energias dos n\u00edveis.\n\
- Dizer que o \u00e1tomo absorve qualquer fot\u00e3o: s\u00f3 os de energia exata.\n\
- Trocar emiss\u00e3o (desce) com absor\u00e7\u00e3o (sobe).\n\
- Usar a f\u00f3rmula de E\u2099 para \u00e1tomos que n\u00e3o s\u00e3o o hidrog\u00e9nio.\n\
- Esquecer que E = 0 corresponde a n = \u221e (eletr\u00e3o livre).\n\
@I\n\
- Energia quantizada: s\u00f3 certos n\u00edveis.\n\
- E\u2099 = -2,18 \u00d7 10\u207b\u00b9\u2078 / n\u00b2 J (hidrog\u00e9nio).\n\
- Descer emite; subir absorve: E fot\u00e3o = |\u0394E|.\n\
- Lyman (UV), Balmer (vis\u00edvel), Paschen (IV).\n\
- Ioniza\u00e7\u00e3o a partir de n = 1: 2,18 \u00d7 10\u207b\u00b9\u2078 J.\n\
@J\n\
Calcula a energia do fot\u00e3o emitido na transi\u00e7\u00e3o n = 3 \u2192 n = 1.\n\
@R\n\
E = |E\u2081 - E\u2083| = 2,18 \u00d7 10\u207b\u00b9\u2078 \u00d7 (1 - 1/9) = 1,94 \u00d7\
 10\u207b\u00b9\u2078 J (s\u00e9rie de Lyman, UV).\n\
@L q2c|Espetroscopia fotoeletr\u00f3nica e energia de remo\u00e7\u00e3o|espetroscopia fotoeletronica pes\
 energia de remocao eletroes niveis subniveis energia de ionizacao||10|n\u00facleo|q2b:Quantiza\u00e7\u00e3o\
 da energia e \u00e1tomo de hidrog\u00e9nio||AE FQ A 10.\u00ba, Energia dos eletr\u00f5es nos \u00e1tomos\n\
@A\n\
- Definir energia de remo\u00e7\u00e3o de um eletr\u00e3o.\n\
- Interpretar um espetro fotoeletr\u00f3nico simples.\n\
- Relacionar picos com n\u00edveis e subn\u00edveis de energia.\n\
- Relacionar a altura de um pico com o n\u00famero de eletr\u00f5es.\n\
@B\n\
Num \u00e1tomo com muitos eletr\u00f5es, nem todos est\u00e3o igualmente presos.\n\
Os mais perto do n\u00facleo precisam de muita energia para sair.\n\
A espetroscopia fotoeletr\u00f3nica \"pesa\" essa energia, eletr\u00e3o a eletr\u00e3o.\n\
@C\n\
- Energia de remo\u00e7\u00e3o: energia m\u00ednima para retirar um eletr\u00e3o de um \u00e1tomo.\n\
- Espetroscopia fotoeletr\u00f3nica: mede as energias de remo\u00e7\u00e3o.\n\
- Cada pico corresponde a um subn\u00edvel (1s, 2s, 2p...).\n\
- A altura do pico \u00e9 proporcional ao n\u00famero de eletr\u00f5es do subn\u00edvel.\n\
- Energia de ioniza\u00e7\u00e3o: energia de remo\u00e7\u00e3o do eletr\u00e3o mais f\u00e1cil de retirar.\n\
@D\n\
O n\u00e9on (1s\u00b2 2s\u00b2 2p\u2076) tem tr\u00eas picos, com energias aproximadas de:\n\
- 1s: 84,0 MJ mol\u207b\u00b9 (2 eletr\u00f5es);\n\
- 2s: 4,68 MJ mol\u207b\u00b9 (2 eletr\u00f5es);\n\
- 2p: 2,08 MJ mol\u207b\u00b9 (6 eletr\u00f5es, o pico mais alto).\n\
O s\u00f3dio tem um pico a mais, 3s, a cerca de 0,50 MJ mol\u207b\u00b9.\n\
O eletr\u00e3o 3s do s\u00f3dio \u00e9 o mais f\u00e1cil de remover.\n\
Os picos agrupam-se por n\u00edveis (n = 1, 2, 3) e, dentro destes, por subn\u00edveis.\n\
Os eletr\u00f5es de um mesmo subn\u00edvel t\u00eam a mesma energia de remo\u00e7\u00e3o.\n\
No mesmo n\u00edvel, os eletr\u00f5es p s\u00e3o removidos com menos energia do que os s.\n\
Este m\u00e9todo confirma a exist\u00eancia de n\u00edveis e subn\u00edveis.\n\
@F Energia de remo\u00e7\u00e3o por eletr\u00e3o|E (J) = E (J mol\u207b\u00b9) / NA|NA: 6,02 \u00d7\
 10\u00b2\u00b3 mol\u207b\u00b9|passar de valor por mole a valor por eletr\u00e3o|0,50 MJ mol\u207b\u00b9 =\
 8,3 \u00d7 10\u207b\u00b9\u2079 J por eletr\u00e3o|c_comu.sci\n\
@F\n\
Dados: picos de um espetro a 104, 6,84, 3,67 e 0,50 MJ mol\u207b\u00b9.\n\
Alturas relativas 2 : 2 : 6 : 1.\n\
Objetivo: identificar o elemento.\n\
1. H\u00e1 4 picos: subn\u00edveis 1s, 2s, 2p e 3s.\n\
2. N\u00famero de eletr\u00f5es: 2 + 2 + 6 + 1 = 11\n\
3. Z = 11: \u00e9 o s\u00f3dio, Na.\n\
4. Configura\u00e7\u00e3o: 1s\u00b2 2s\u00b2 2p\u2076 3s\u00b9.\n\
> O elemento \u00e9 o s\u00f3dio (11 eletr\u00f5es).\n\
Verifica\u00e7\u00e3o: o pico de menor energia, 0,50 MJ mol\u207b\u00b9 = 500 kJ mol\u207b\u00b9, est\u00e1\
 perto da energia de ioniza\u00e7\u00e3o do Na (496 kJ mol\u207b\u00b9).\n\
@G\n\
Quanto mais perto do n\u00facleo, mais energia \u00e9 preciso para remover o eletr\u00e3o.\n\
Os eletr\u00f5es de val\u00eancia s\u00e3o os mais f\u00e1ceis de remover: s\u00e3o os que participam nas\
 rea\u00e7\u00f5es.\n\
@H\n\
- Achar que todos os eletr\u00f5es de um \u00e1tomo t\u00eam a mesma energia.\n\
- Ler a altura do pico como energia: a energia est\u00e1 no eixo horizontal.\n\
- Esquecer que o pico mais alto \u00e9 o subn\u00edvel com mais eletr\u00f5es.\n\
- Confundir energia de remo\u00e7\u00e3o com energia do n\u00edvel (sinal oposto).\n\
@I\n\
- Energia de remo\u00e7\u00e3o: energia para retirar um eletr\u00e3o.\n\
- Um pico por subn\u00edvel; altura proporcional ao n.\u00ba de eletr\u00f5es.\n\
- Mais perto do n\u00facleo: maior energia de remo\u00e7\u00e3o.\n\
- O pico de menor energia \u00e9 a energia de ioniza\u00e7\u00e3o.\n\
@J\n\
Um espetro tem picos de alturas 2 : 2 : 4. Que elemento \u00e9?\n\
@R\n\
2 + 2 + 4 = 8 eletr\u00f5es (1s\u00b2 2s\u00b2 2p\u2074): \u00e9 o oxig\u00e9nio, O.\n\
@L q2d|Modelo da nuvem eletr\u00f3nica: n\u00edveis, subn\u00edveis, orbitais e spin|nuvem eletronica orbital\
 nivel subnivel spin modelo quantico s p d||10|n\u00facleo|q2c:Espetroscopia fotoeletr\u00f3nica e energia de\
 remo\u00e7\u00e3o||AE FQ A 10.\u00ba, Energia dos eletr\u00f5es nos \u00e1tomos\n\
@A\n\
- Descrever o modelo da nuvem eletr\u00f3nica.\n\
- Definir orbital, n\u00edvel e subn\u00edvel.\n\
- Indicar quantas orbitais tem cada subn\u00edvel.\n\
- Explicar o que \u00e9 o spin do eletr\u00e3o.\n\
@B\n\
N\u00e3o sabemos onde est\u00e1 o eletr\u00e3o a cada instante.\n\
Sabemos onde \u00e9 mais prov\u00e1vel encontr\u00e1-lo.\n\
A nuvem eletr\u00f3nica \u00e9 mais densa onde essa probabilidade \u00e9 maior.\n\
\u00c9 como uma fotografia com tempo de exposi\u00e7\u00e3o longo de uma abelha \u00e0 volta de uma flor.\n\
@C\n\
- Orbital: zona onde \u00e9 muito prov\u00e1vel encontrar o eletr\u00e3o.\n\
- Cada orbital tem, no m\u00e1ximo, 2 eletr\u00f5es.\n\
- N\u00edvel n: conjunto de orbitais com o mesmo n (1, 2, 3...).\n\
- Subn\u00edveis: s (1 orbital), p (3 orbitais), d (5 orbitais).\n\
- O n\u00edvel n tem n subn\u00edveis: n = 2 tem 2s e 2p.\n\
- Spin: propriedade do eletr\u00e3o com dois valores (\u2191 e \u2193).\n\
@D\n\
As orbitais s s\u00e3o esf\u00e9ricas.\n\
As orbitais p t\u00eam dois l\u00f3bulos e s\u00e3o tr\u00eas: px, py e pz.\n\
O n\u00edvel 1 s\u00f3 tem a orbital 1s (m\u00e1ximo de 2 eletr\u00f5es).\n\
O n\u00edvel 2 tem 2s e 2p: 4 orbitais e at\u00e9 8 eletr\u00f5es.\n\
O n\u00edvel 3 tem 3s, 3p e 3d: 9 orbitais e at\u00e9 18 eletr\u00f5es.\n\
Num \u00e1tomo com v\u00e1rios eletr\u00f5es, a energia depende do n\u00edvel e do subn\u00edvel.\n\
A ordem de energia \u00e9 1s < 2s < 2p < 3s < 3p < 4s < 3d.\n\
Orbitais do mesmo subn\u00edvel t\u00eam a mesma energia (orbitais degeneradas).\n\
Dois eletr\u00f5es na mesma orbital t\u00eam spins opostos.\n\
@F Eletr\u00f5es por n\u00edvel|m\u00e1ximo = 2n\u00b2|n: n\u00famero do n\u00edvel|cada n\u00edvel\
 completo|n = 3: 2 \u00d7 9 = 18 eletr\u00f5es|\n\
@F Orbitais por subn\u00edvel|s: 1; p: 3; d: 5|cada orbital: no m\u00e1ximo 2 eletr\u00f5es|todos os\
 \u00e1tomos|subn\u00edvel p: at\u00e9 6 eletr\u00f5es|c_fqel.conf\n\
@F\n\
Dados: n\u00edvel n = 2.\n\
Objetivo: subn\u00edveis, orbitais e n\u00famero m\u00e1ximo de eletr\u00f5es.\n\
1. Subn\u00edveis: 2s e 2p (n = 2 tem 2 subn\u00edveis).\n\
2. Orbitais: 1 (2s) + 3 (2p) = 4\n\
3. Eletr\u00f5es: 2 \u00d7 4 = 8\n\
> O n\u00edvel 2 tem 4 orbitais e at\u00e9 8 eletr\u00f5es.\n\
Verifica\u00e7\u00e3o: 2n\u00b2 = 2 \u00d7 2\u00b2 = 8.\n\
@G\n\
O modelo da nuvem eletr\u00f3nica substituiu as \u00f3rbitas de Bohr.\n\
O eletr\u00e3o n\u00e3o percorre uma trajet\u00f3ria: tem uma probabilidade de estar em cada zona.\n\
@H\n\
- Desenhar orbitais como \u00f3rbitas circulares.\n\
- P\u00f4r 3 eletr\u00f5es na mesma orbital.\n\
- Dizer que o subn\u00edvel p tem 2 orbitais: tem 3.\n\
- Esquecer que 4s tem menos energia do que 3d.\n\
@I\n\
- Orbital: zona de probabilidade, at\u00e9 2 eletr\u00f5es.\n\
- s: 1 orbital; p: 3; d: 5.\n\
- N\u00edvel n: n subn\u00edveis, at\u00e9 2n\u00b2 eletr\u00f5es.\n\
- Spin: dois valores; na mesma orbital, opostos.\n\
@J\n\
Quantos eletr\u00f5es cabem, no m\u00e1ximo, no subn\u00edvel 3p?\n\
@R\n\
3 orbitais \u00d7 2 = 6 eletr\u00f5es.\n\
@L q2e|Configura\u00e7\u00e3o eletr\u00f3nica|configuracao eletronica principio da construcao aufbau exclusao\
 de pauli regra de hund diagrama de caixas eletroes de valencia|c_fqel.conf|10|n\u00facleo|q2d:Modelo da\
 nuvem eletr\u00f3nica: n\u00edveis, subn\u00edveis, orbitais e spin||AE FQ A 10.\u00ba, Energia dos\
 eletr\u00f5es nos \u00e1tomos\n\
@A\n\
- Escrever configura\u00e7\u00f5es eletr\u00f3nicas at\u00e9 Z = 20 (at\u00e9 4s).\n\
- Aplicar o Princ\u00edpio da Constru\u00e7\u00e3o.\n\
- Aplicar o Princ\u00edpio de Exclus\u00e3o de Pauli.\n\
- Aplicar a Regra de Hund nos diagramas de caixas.\n\
- Identificar os eletr\u00f5es de val\u00eancia.\n\
@B\n\
Encher as orbitais \u00e9 como encher um pr\u00e9dio: primeiro os andares de baixo.\n\
Em cada quarto (orbital) s\u00f3 cabem duas pessoas, viradas ao contr\u00e1rio.\n\
Em quartos iguais, cada pessoa fica sozinha antes de partilhar.\n\
@C\n\
- Princ\u00edpio da Constru\u00e7\u00e3o: as orbitais enchem-se por ordem crescente de energia.\n\
- Ordem: 1s 2s 2p 3s 3p 4s.\n\
- Exclus\u00e3o de Pauli: cada orbital tem, no m\u00e1ximo, 2 eletr\u00f5es, com spins opostos.\n\
- Regra de Hund: em orbitais com a mesma energia, primeiro um eletr\u00e3o em cada uma, com o mesmo spin.\n\
- Eletr\u00f5es de val\u00eancia: os do \u00faltimo n\u00edvel.\n\
@D\n\
Escreve-se cada subn\u00edvel com o n\u00famero de eletr\u00f5es em expoente.\n\
Exemplo: oxig\u00e9nio, Z = 8: 1s\u00b2 2s\u00b2 2p\u2074.\n\
No diagrama de caixas, os 4 eletr\u00f5es 2p ficam: [\u2191\u2193][\u2191 ][\u2191 ].\n\
Pela Regra de Hund, h\u00e1 2 eletr\u00f5es desemparelhados.\n\
Exemplo: pot\u00e1ssio, Z = 19: 1s\u00b2 2s\u00b2 2p\u2076 3s\u00b2 3p\u2076 4s\u00b9.\n\
O 4s enche-se antes do 3d, porque tem menos energia.\n\
Os eletr\u00f5es de val\u00eancia do pot\u00e1ssio: 1 (o 4s\u00b9).\n\
O \u00faltimo n\u00edvel indica o per\u00edodo: pot\u00e1ssio no 4.\u00ba per\u00edodo.\n\
Nos grupos 1 e 2, o n\u00famero de eletr\u00f5es de val\u00eancia \u00e9 o do grupo.\n\
Nos grupos 13 a 18, \u00e9 o n\u00famero do grupo menos 10.\n\
I\u00f5es: Na\u207a (10 eletr\u00f5es) fica 1s\u00b2 2s\u00b2 2p\u2076, como o n\u00e9on.\n\
@F Ordem de preenchimento|1s 2s 2p 3s 3p 4s (3d 4p)|s: at\u00e9 2 eletr\u00f5es;p: at\u00e9 6;d: at\u00e9\
 10|Princ\u00edpio da Constru\u00e7\u00e3o (estado fundamental)|Z = 12: 1s\u00b2 2s\u00b2 2p\u2076\
 3s\u00b2|c_fqel.conf\n\
@F Eletr\u00f5es de val\u00eancia e grupo|grupos 1-2: n.\u00ba do grupo; grupos 13-18: grupo -\
 10|eletr\u00f5es de val\u00eancia: os do \u00faltimo n\u00edvel|elementos dos blocos s e p|cloro, grupo 17:\
 7 eletr\u00f5es de val\u00eancia|c_fqel.conf\n\
@F\n\
Dados: f\u00f3sforo, P, Z = 15.\n\
Objetivo: configura\u00e7\u00e3o, diagrama de caixas e val\u00eancia.\n\
1. 15 eletr\u00f5es: 1s\u00b2 2s\u00b2 2p\u2076 3s\u00b2 3p\u00b3 (soma: 2 + 2 + 6 + 2 + 3 = 15)\n\
2. 3p\u00b3 pela Regra de Hund: [\u2191 ][\u2191 ][\u2191 ] (3 desemparelhados)\n\
3. \u00daltimo n\u00edvel n = 3: 3s\u00b2 3p\u00b3, logo 5 eletr\u00f5es de val\u00eancia.\n\
4. Per\u00edodo 3, grupo 5 + 10 = 15.\n\
> P: 1s\u00b2 2s\u00b2 2p\u2076 3s\u00b2 3p\u00b3; 5 eletr\u00f5es de val\u00eancia.\n\
Verifica\u00e7\u00e3o: o grupo 15 tem 5 eletr\u00f5es de val\u00eancia.\n\
@G\n\
A configura\u00e7\u00e3o eletr\u00f3nica explica a posi\u00e7\u00e3o na tabela peri\u00f3dica.\n\
Os eletr\u00f5es de val\u00eancia explicam as propriedades qu\u00edmicas.\n\
Elementos do mesmo grupo t\u00eam configura\u00e7\u00f5es de val\u00eancia semelhantes.\n\
@H\n\
- Encher 3d antes de 4s.\n\
- P\u00f4r dois eletr\u00f5es numa orbital p antes de ocupar as outras (viola Hund).\n\
- P\u00f4r os dois eletr\u00f5es da mesma orbital com o mesmo spin (viola Pauli).\n\
- Contar como val\u00eancia eletr\u00f5es de n\u00edveis interiores.\n\
- Esquecer de somar os eletr\u00f5es para confirmar Z.\n\
@I\n\
- Ordem: 1s 2s 2p 3s 3p 4s.\n\
- Pauli: m\u00e1ximo de 2 por orbital, spins opostos.\n\
- Hund: um por orbital antes de emparelhar.\n\
- Val\u00eancia: eletr\u00f5es do \u00faltimo n\u00edvel.\n\
- \u00daltimo n\u00edvel = per\u00edodo.\n\
@J\n\
Escreve a configura\u00e7\u00e3o eletr\u00f3nica do enxofre, S (Z = 16).\n\
@R\n\
1s\u00b2 2s\u00b2 2p\u2076 3s\u00b2 3p\u2074 (2 + 2 + 6 + 2 + 4 = 16 eletr\u00f5es; 6 de val\u00eancia).\n\
@E 1|q2e1|Energia de um fot\u00e3o de luz vermelha|c_fqel.fot|q2a\n\
Enunciado: um laser vermelho emite luz com \u03bb = 650 nm.\n\
Calcula a energia de um fot\u00e3o.\n\
Dados: \u03bb = 650 nm = 6,50 \u00d7 10\u207b\u2077 m; h = 6,63 \u00d7 10\u207b\u00b3\u2074 J s; c = 3,00\
 \u00d7 10\u2078 m s\u207b\u00b9.\n\
M\u00e9todo: f = c / \u03bb e depois E = h f.\n\
Resolu\u00e7\u00e3o:\n\
1. f = 3,00 \u00d7 10\u2078 / 6,50 \u00d7 10\u207b\u2077 = 4,62 \u00d7 10\u00b9\u2074 Hz\n\
2. E = 6,63 \u00d7 10\u207b\u00b3\u2074 \u00d7 4,62 \u00d7 10\u00b9\u2074 = 3,06 \u00d7 10\u207b\u00b9\u2079 J\n\
Resultado: cada fot\u00e3o tem 3,06 \u00d7 10\u207b\u00b9\u2079 J.\n\
Interpreta\u00e7\u00e3o: \u00e9 pouca energia; um laser emite muitos fot\u00f5es por segundo.\n\
Erros a evitar: usar \u03bb em nan\u00f3metros na f\u00f3rmula.\n\
@E 2|q2e2|Risca de Balmer do hidrog\u00e9nio|c_fqel.hid|q2b\n\
Enunciado: calcula o comprimento de onda da risca emitida na transi\u00e7\u00e3o 3 \u2192 2.\n\
Dados: E\u2099 = -2,18 \u00d7 10\u207b\u00b9\u2078 / n\u00b2 J.\n\
M\u00e9todo: diferen\u00e7a de energias e \u03bb = h c / E.\n\
Resolu\u00e7\u00e3o:\n\
1. E\u2083 = -2,18 \u00d7 10\u207b\u00b9\u2078 / 9 = -2,42 \u00d7 10\u207b\u00b9\u2079 J\n\
2. E\u2082 = -2,18 \u00d7 10\u207b\u00b9\u2078 / 4 = -5,45 \u00d7 10\u207b\u00b9\u2079 J\n\
3. E fot\u00e3o = E\u2083 - E\u2082 = 3,03 \u00d7 10\u207b\u00b9\u2079 J\n\
4. \u03bb = 6,63 \u00d7 10\u207b\u00b3\u2074 \u00d7 3,00 \u00d7 10\u2078 / 3,03 \u00d7 10\u207b\u00b9\u2079 =\
 6,56 \u00d7 10\u207b\u2077 m\n\
Resultado: \u03bb \u2248 656 nm, a risca vermelha de Balmer.\n\
Interpreta\u00e7\u00e3o: o valor medido \u00e9 656 nm; o modelo de Bohr acerta bem no hidrog\u00e9nio.\n\
Erros a evitar: fazer E\u2082 - E\u2083 e obter energia negativa para o fot\u00e3o.\n\
@E 3|q2e3|Energia para ionizar uma mole de \u00e1tomos de hidrog\u00e9nio|c_fqel.hid|q2b\n\
Enunciado: que energia \u00e9 preciso para ionizar 1,00 mol de \u00e1tomos de H no estado fundamental?\n\
E qual o maior comprimento de onda de um fot\u00e3o capaz de ionizar um \u00e1tomo?\n\
Dados: E\u2081 = -2,18 \u00d7 10\u207b\u00b9\u2078 J; NA = 6,02 \u00d7 10\u00b2\u00b3 mol\u207b\u00b9.\n\
Resolu\u00e7\u00e3o:\n\
1. Por \u00e1tomo: E = 0 - E\u2081 = 2,18 \u00d7 10\u207b\u00b9\u2078 J\n\
2. Por mole: 2,18 \u00d7 10\u207b\u00b9\u2078 \u00d7 6,02 \u00d7 10\u00b2\u00b3 = 1,31 \u00d7 10\u2076 J\
 mol\u207b\u00b9\n\
3. \u03bb m\u00e1ximo = h c / E = 6,63 \u00d7 10\u207b\u00b3\u2074 \u00d7 3,00 \u00d7 10\u2078 / 2,18 \u00d7\
 10\u207b\u00b9\u2078 = 9,12 \u00d7 10\u207b\u2078 m\n\
Resultado: 1,31 \u00d7 10\u2076 J (1312 kJ) por mole; \u03bb m\u00e1ximo de 91,2 nm (UV).\n\
Interpreta\u00e7\u00e3o: fot\u00f5es com \u03bb maior n\u00e3o t\u00eam energia para ionizar o \u00e1tomo.\n\
Erros a evitar: esquecer que a energia final do eletr\u00e3o livre \u00e9 0.\n\
"
