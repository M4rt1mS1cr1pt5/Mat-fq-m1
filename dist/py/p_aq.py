# p_aq.py - M1TR4M: Atividades laboratoriais de Qu\xedmica (gerado pelo build).
D = "@V 1\n\
@N 7\n\
@T Atividades laboratoriais de Qu\xedmica\n\
@L aq11|AL 1.1 Volume e n\xfamero de mol\xe9culas de uma gota de \xe1gua|al 1.1 gota de agua volume numero de\
 moleculas massa media ensaios incerteza absoluta relativa bureta balanca\
 precisao|c_alq1.gota|10|n\xfacleo|q1d:Quantidade de mat\xe9ria e massa molar||Programa e AE FQ A 10.\xba, AL 1.1\n\
@A\n\
- Medir a massa de um n\xfamero conhecido de gotas.\n\
- Calcular a massa e o volume m\xe9dios de uma gota, com incerteza.\n\
- Calcular a quantidade de mat\xe9ria e o n\xfamero de mol\xe9culas de uma gota.\n\
- Avaliar a precis\xe3o das medi\xe7\xf5es.\n\
@B\n\
Uma gota parece pouca coisa, mas tem um n\xfamero enorme de mol\xe9culas.\n\
Uma gota tem pouca massa: mede-se a massa de muitas gotas e divide-se.\n\
@C\n\
- Material: bureta (ou conta-gotas), gobel\xe9, balan\xe7a (0,01 g), \xe1gua destilada.\n\
- Massa de uma gota: m(gota) = m(n gotas) / n.\n\
- Volume: V = m / \u03c1, com \u03c1(\xe1gua) = 1,00 g cm\u207b\xb3.\n\
- n = m / M, com M(H\u2082O) = 18,02 g mol\u207b\xb9; N = n NA.\n\
- Incerteza absoluta: maior desvio em rela\xe7\xe3o \xe0 m\xe9dia.\n\
@D\n\
1. Coloca o gobel\xe9 na balan\xe7a e tara.\n\
2. Deixa cair 20 gotas da bureta e regista a massa.\n\
3. Repete pelo menos tr\xeas vezes (ensaios).\n\
4. Calcula a massa de uma gota em cada ensaio e a m\xe9dia.\n\
5. Calcula a incerteza absoluta (maior desvio) e a relativa.\n\
6. Calcula o volume, a quantidade de mat\xe9ria e o n\xfamero de mol\xe9culas.\n\
Cuidados: n\xe3o mexas na torneira entre ensaios, para as gotas terem o mesmo tamanho.\n\
Pesa logo, para a \xe1gua n\xe3o evaporar.\n\
Medir 20 gotas divide por 20 a incerteza da balan\xe7a em cada gota.\n\
Incerteza com 1 algarismo significativo, arredondada por excesso.\n\
@F Massa de uma gota|m(gota) = m(n gotas) / n|n: n\xfamero de gotas|gotas do mesmo tamanho|1,01 g em 20\
 gotas: 0,0505 g|c_alq1.gota\n\
@F N\xfamero de mol\xe9culas|N = (m / M) NA|M(H\u2082O) = 18,02 g mol\u207b\xb9;NA = 6,02 \xd7 10\xb2\xb3\
 mol\u207b\xb9|amostra pura|0,0503 g de \xe1gua: N = 1,68 \xd7 10\xb2\xb9|c_alq1.gota\n\
@F\n\
Dados: tr\xeas ensaios de 20 gotas: 0,99 g; 1,02 g; 1,01 g.\n\
Objetivo: massa de uma gota com incerteza e n\xfamero de mol\xe9culas.\n\
1. Uma gota em cada ensaio: 0,0495 g; 0,0510 g; 0,0505 g\n\
2. M\xe9dia: m = 0,0503 g; maior desvio: 0,0008 g\n\
3. Incerteza arredondada por excesso: 0,0009 g, ou seja 1,8 %\n\
4. n = 0,0503 / 18,02 = 2,79 \xd7 10\u207b\xb3 mol\n\
5. N = 2,79 \xd7 10\u207b\xb3 \xd7 6,02 \xd7 10\xb2\xb3 = 1,68 \xd7 10\xb2\xb9 mol\xe9culas\n\
> m(gota) = (0,0503 \xb1 0,0009) g; N \u2248 1,68 \xd7 10\xb2\xb9 mol\xe9culas.\n\
Verifica\xe7\xe3o: o volume de uma gota \xe9 cerca de 0,05 cm\xb3, um valor plaus\xedvel.\n\
@G\n\
Mesmo uma gota tem cerca de 10\xb2\xb9 mol\xe9culas: as mol\xe9culas s\xe3o min\xfasculas.\n\
A incerteza relativa de cerca de 2 % mostra uma boa precis\xe3o.\n\
@H\n\
- Contar mal as gotas.\n\
- Esquecer de tarar a balan\xe7a.\n\
- Mexer na torneira e mudar o tamanho das gotas.\n\
- Esquecer de dividir pelo n\xfamero de gotas.\n\
@I\n\
- m(gota) = m / n.\n\
- V = m / \u03c1; n = m / M; N = n NA.\n\
- Incerteza: maior desvio em rela\xe7\xe3o \xe0 m\xe9dia.\n\
- Medir muitas gotas reduz a incerteza de cada uma.\n\
@J\n\
Porque se mede a massa de 20 gotas e n\xe3o a de uma s\xf3?\n\
@R\n\
Uma gota tem massa muito pequena: com 20 gotas, a incerteza da balan\xe7a fica 20 vezes menor em cada gota.\n\
@L aq12|AL 1.2 Teste de chama|al 1.2 teste de chama cor da chama emissao desexcitacao sodio potassio litio\
 calcio estroncio bario cobre vidro de cobalto|c_alq1.chama|10|n\xfacleo|q2b:Quantiza\xe7\xe3o da energia e\
 \xe1tomo de hidrog\xe9nio||Programa e AE FQ A 10.\xba, AL 1.2\n\
@A\n\
- Identificar elementos met\xe1licos pela cor da chama.\n\
- Relacionar a cor com a emiss\xe3o de radia\xe7\xe3o por \xe1tomos excitados.\n\
- Reconhecer as limita\xe7\xf5es do teste de chama.\n\
@B\n\
O fogo de artif\xedcio tem cores diferentes porque cont\xe9m sais de metais diferentes.\n\
@C\n\
- Material: bico de Bunsen, fio de n\xedquel-cr\xf3mio (ou vareta de madeira), sais (cloretos), \xe1cido\
 clor\xeddrico dilu\xeddo, vidro de cobalto.\n\
- Na chama, os eletr\xf5es dos \xe1tomos excitam-se.\n\
- Ao voltarem a n\xedveis de menor energia, emitem radia\xe7\xe3o.\n\
- Cada elemento emite radia\xe7\xf5es pr\xf3prias: a cor \xe9 uma \"impress\xe3o digital\".\n\
@D\n\
1. Limpa o fio no \xe1cido e na chama, at\xe9 a chama n\xe3o mudar de cor.\n\
2. Toca no sal com o fio e leva-o \xe0 chama.\n\
3. Regista a cor observada.\n\
4. Repete para cada sal, limpando sempre o fio.\n\
5. Observa o pot\xe1ssio atrav\xe9s do vidro de cobalto, que filtra o amarelo do s\xf3dio.\n\
Cores habituais:\n\
- l\xedtio: vermelho carmim; s\xf3dio: amarelo-alaranjado;\n\
- pot\xe1ssio: violeta (lil\xe1s); c\xe1lcio: vermelho-alaranjado;\n\
- estr\xf4ncio: vermelho intenso; b\xe1rio: verde-amarelado;\n\
- cobre: verde-azulado.\n\
Seguran\xe7a: \xf3culos, cabelo apanhado e cuidado com o \xe1cido e com a chama.\n\
@F Energia de um fot\xe3o emitido|E = h c / \u03bb|h = 6,63 \xd7 10\u207b\xb3\u2074 J s;c = 3,00 \xd7\
 10\u2078 m s\u207b\xb9;\u03bb: comprimento de onda (m)|um fot\xe3o|\u03bb = 589 nm: E = 3,38 \xd7\
 10\u207b\xb9\u2079 J|c_fqel.fot\n\
@F\n\
Dados: o s\xf3dio emite sobretudo radia\xe7\xe3o com \u03bb = 589 nm.\n\
Objetivo: energia de cada fot\xe3o emitido.\n\
1. \u03bb = 589 \xd7 10\u207b\u2079 m = 5,89 \xd7 10\u207b\u2077 m\n\
2. E = 6,63 \xd7 10\u207b\xb3\u2074 \xd7 3,00 \xd7 10\u2078 / (5,89 \xd7 10\u207b\u2077) = 3,38 \xd7\
 10\u207b\xb9\u2079 J\n\
> E \u2248 3,38 \xd7 10\u207b\xb9\u2079 J por fot\xe3o (luz vis\xedvel, amarela).\n\
Verifica\xe7\xe3o: est\xe1 entre a energia do vermelho e a do violeta.\n\
@G\n\
O teste identifica o elemento met\xe1lico, n\xe3o o composto: NaCl e Na\u2082SO\u2084 d\xe3o a mesma cor.\n\
\xc9 um teste qualitativo; para confirmar usa-se um espetrosc\xf3pio.\n\
@H\n\
- N\xe3o limpar o fio entre amostras.\n\
- Confundir o amarelo do s\xf3dio (impureza frequente) com outra cor.\n\
- Concluir que se identificou o composto.\n\
- Usar demasiado sal.\n\
@I\n\
- Cor da chama: identifica o elemento met\xe1lico.\n\
- A emiss\xe3o vem da desexcita\xe7\xe3o dos eletr\xf5es.\n\
- Limpa sempre o fio; vidro de cobalto para o pot\xe1ssio.\n\
@J\n\
Uma amostra d\xe1 uma chama vermelho carmim. Que elemento cont\xe9m provavelmente?\n\
@R\n\
L\xedtio: \xe9 o elemento com chama vermelho carmim.\n\
@L aq13|AL 1.3 Densidade relativa de metais|al 1.3 densidade relativa picnometro metal massa volumica agua\
 deslocada erro percentual exatidao identificar metal|c_alq1.dens|10|n\xfacleo|q3c:Forma\xe7\xe3o de i\xf5es\
 e propriedades dos elementos;r7b:Materiais: subst\xe2ncias, misturas e massa vol\xfamica||Programa e AE FQ A\
 10.\xba, AL 1.3\n\
@A\n\
- Determinar a densidade relativa de um metal pelo m\xe9todo do picn\xf3metro.\n\
- Calcular o erro percentual em rela\xe7\xe3o ao valor tabelado.\n\
- Identificar um metal pela densidade relativa.\n\
@B\n\
Um peda\xe7o de metal desloca um volume de \xe1gua igual ao seu.\n\
Comparar a massa do metal com a da \xe1gua deslocada d\xe1 a densidade relativa.\n\
@C\n\
- Material: picn\xf3metro, balan\xe7a (0,01 g), \xe1gua destilada, pequenos peda\xe7os de metal, papel absorvente.\n\
- Densidade relativa: d = \u03c1(metal) / \u03c1(\xe1gua) (sem unidades).\n\
- d = m / (m + m1 - m2).\n\
- m: metal; m1: picn\xf3metro cheio de \xe1gua; m2: picn\xf3metro com o metal e cheio de \xe1gua.\n\
- Erro percentual = |d - d(tab)| / d(tab) \xd7 100 %.\n\
@D\n\
1. Mede a massa do metal, m.\n\
2. Enche o picn\xf3metro com \xe1gua, tapa, seca por fora e mede m1.\n\
3. P\xf5e o metal dentro, completa com \xe1gua, tapa, seca e mede m2.\n\
4. A massa de \xe1gua deslocada \xe9 m + m1 - m2.\n\
5. Calcula d e o erro percentual.\n\
Cuidados: sem bolhas de ar; secar bem o exterior; \xe1gua \xe0 temperatura ambiente.\n\
Valores tabelados a 20 \xb0C: alum\xednio 2,70; zinco 7,14; ferro 7,87; cobre 8,96; chumbo 11,34.\n\
@F Densidade relativa (picn\xf3metro)|d = m / (m + m1 - m2)|m: massa do metal;m1: picn\xf3metro com\
 \xe1gua;m2: picn\xf3metro com metal e \xe1gua (g)|picn\xf3metro bem cheio, sem bolhas|20,15 g de metal e\
 2,27 g de \xe1gua deslocada: d = 8,88|c_alq1.dens\n\
@F\n\
Dados: m = 20,15 g; m1 = 82,40 g; m2 = 100,28 g; cobre: d(tab) = 8,96.\n\
Objetivo: densidade relativa e erro percentual.\n\
1. \xc1gua deslocada: 20,15 + 82,40 - 100,28 = 2,27 g\n\
2. d = 20,15 / 2,27 = 8,88\n\
3. Erro: |8,88 - 8,96| / 8,96 \xd7 100 = 0,9 %\n\
> d \u2248 8,88; erro de cerca de 0,9 %: o metal deve ser cobre.\n\
Verifica\xe7\xe3o: o erro \xe9 pequeno, por isso a exatid\xe3o \xe9 boa.\n\
@G\n\
A densidade relativa \xe9 uma propriedade caracter\xedstica: ajuda a identificar materiais.\n\
Um erro grande indica bolhas de ar, picn\xf3metro mal cheio ou metal oco ou impuro.\n\
@H\n\
- Deixar bolhas de ar no picn\xf3metro.\n\
- N\xe3o secar o exterior antes de pesar.\n\
- Trocar m1 com m2 na f\xf3rmula.\n\
- Usar peda\xe7os de metal grandes demais para o picn\xf3metro.\n\
@I\n\
- d = m / (m + m1 - m2).\n\
- A massa de \xe1gua deslocada d\xe1 o volume do metal.\n\
- Erro percentual mede a exatid\xe3o.\n\
@J\n\
Porque \xe9 que a densidade relativa n\xe3o tem unidades?\n\
@R\n\
\xc9 o quociente entre duas massas vol\xfamicas (ou duas massas de igual volume): as unidades cortam-se.\n\
@L aq21|AL 2.1 Miscibilidade de l\xedquidos|al 2.1 miscibilidade liquidos misciveis imisciveis fases\
 interacoes intermoleculares polar apolar agua etanol hexano\
 propanona|c_alq2.misc|10|n\xfacleo|q4f:Intera\xe7\xf5es intermoleculares, solubilidade e\
 miscibilidade||Programa e AE FQ A 10.\xba, AL 2.1\n\
@A\n\
- Verificar se pares de l\xedquidos s\xe3o misc\xedveis.\n\
- Relacionar a miscibilidade com as intera\xe7\xf5es intermoleculares.\n\
- Prever qual dos l\xedquidos fica por cima quando n\xe3o se misturam.\n\
@B\n\
O azeite e o vinagre separam-se; o \xe1lcool e a \xe1gua misturam-se.\n\
A diferen\xe7a est\xe1 nas intera\xe7\xf5es entre as mol\xe9culas.\n\
@C\n\
- Material: tubos de ensaio com rolha, suporte, pipetas, \xe1gua, etanol, propanona, hexano e \xf3leo.\n\
- Misc\xedveis: formam uma s\xf3 fase; imisc\xedveis: formam duas fases.\n\
- \"Semelhante dissolve semelhante\": intera\xe7\xf5es do mesmo tipo favorecem a mistura.\n\
- \xc1gua: liga\xe7\xf5es de hidrog\xe9nio; hexano: s\xf3 for\xe7as de London.\n\
@D\n\
1. Num tubo, junta 2 mL de cada l\xedquido.\n\
2. Tapa, agita e deixa repousar.\n\
3. Regista se h\xe1 uma ou duas fases.\n\
4. Com duas fases, regista qual fica por cima (o menos denso).\n\
Resultados esperados:\n\
- \xe1gua e etanol: misc\xedveis;\n\
- \xe1gua e propanona: misc\xedveis;\n\
- \xe1gua e hexano: imisc\xedveis (hexano por cima);\n\
- hexano e \xf3leo: misc\xedveis.\n\
Seguran\xe7a: o hexano e a propanona s\xe3o inflam\xe1veis e vol\xe1teis; trabalha longe de chamas.\n\
@F Massa vol\xfamica|\u03c1 = m / V|m: massa (g);V: volume (cm\xb3)|com duas fases, fica por cima a de menor\
 \u03c1|2,0 mL de hexano com 1,3 g: \u03c1 = 0,66 g cm\u207b\xb3|\n\
@F\n\
Dados: \xe1gua (\u03c1 = 1,00 g cm\u207b\xb3) e hexano (\u03c1 = 0,66 g cm\u207b\xb3), 2,0 mL de cada.\n\
Objetivo: prever o resultado e a massa de hexano usada.\n\
1. \xc1gua: liga\xe7\xf5es de hidrog\xe9nio; hexano: s\xf3 London: imisc\xedveis.\n\
2. Fica por cima o hexano, que tem menor massa vol\xfamica.\n\
3. Massa de hexano: m = 0,66 \xd7 2,0 = 1,3 g\n\
> Duas fases: hexano por cima e \xe1gua por baixo.\n\
Verifica\xe7\xe3o: o \xf3leo, tamb\xe9m apolar, comporta-se como o hexano.\n\
@G\n\
A miscibilidade explica porque a \xe1gua n\xe3o lava a gordura sem detergente.\n\
A regra \xe9 uma previs\xe3o: para \xe1lcoois com l\xedquidos apolares, s\xf3 a experi\xeancia decide.\n\
@H\n\
- Achar que dois l\xedquidos incolores se misturam sempre.\n\
- N\xe3o esperar que as fases se separem.\n\
- Confundir \"mais denso\" com \"mais viscoso\".\n\
- Esquecer a seguran\xe7a com l\xedquidos inflam\xe1veis.\n\
@I\n\
- Misc\xedveis: uma fase; imisc\xedveis: duas.\n\
- Semelhante dissolve semelhante.\n\
- A fase de cima \xe9 a menos densa.\n\
@J\n\
Prev\xea se a propanona e a \xe1gua s\xe3o misc\xedveis e explica.\n\
@R\n\
S\xe3o misc\xedveis: a propanona \xe9 polar e aceita liga\xe7\xf5es de hidrog\xe9nio da \xe1gua.\n\
@L aq22|AL 2.2 Solu\xe7\xf5es a partir de solutos s\xf3lidos|al 2.2 preparar solucao soluto solido massa a\
 pesar balao volumetrico concentracao incerteza menisco paralaxe|c_alq2.sol|10|n\xfacleo|q5d:Composi\xe7\xe3o\
 quantitativa de solu\xe7\xf5es||Programa e AE FQ A 10.\xba, AL 2.2\n\
@A\n\
- Calcular a massa de soluto para uma concentra\xe7\xe3o pedida.\n\
- Preparar uma solu\xe7\xe3o num bal\xe3o volum\xe9trico.\n\
- Estimar a incerteza relativa da concentra\xe7\xe3o.\n\
@B\n\
Para fazer uma solu\xe7\xe3o rigorosa n\xe3o basta \"p\xf4r um pouco de sal\".\n\
\xc9 preciso pesar o soluto e medir o volume com instrumentos de precis\xe3o.\n\
@C\n\
- Material: balan\xe7a (0,01 g), gobel\xe9, esp\xe1tula, funil, bal\xe3o volum\xe9trico, esguicho, conta-gotas.\n\
- m = c V M (V em dm\xb3).\n\
- Bal\xe3o volum\xe9trico: mede um \xfanico volume com rigor (tra\xe7o de refer\xeancia).\n\
- Incerteza relativa de c \u2248 u(m) / m + u(V) / V.\n\
@D\n\
1. Calcula a massa a pesar: m = c V M.\n\
2. Pesa o soluto num gobel\xe9.\n\
3. Dissolve com um pouco de \xe1gua destilada.\n\
4. Transfere para o bal\xe3o; lava o gobel\xe9 v\xe1rias vezes para o bal\xe3o.\n\
5. Completa com \xe1gua at\xe9 ao tra\xe7o, com o conta-gotas no fim.\n\
6. Tapa, homogene\xedza e rotula.\n\
L\xea o tra\xe7o ao n\xedvel dos olhos (sem erro de paralaxe).\n\
O menisco fica tangente ao tra\xe7o.\n\
@F Massa de soluto a pesar|m = c V M|c: concentra\xe7\xe3o (mol dm\u207b\xb3);V: volume (dm\xb3);M: massa\
 molar (g mol\u207b\xb9)|soluto puro|0,100 mol dm\u207b\xb3 em 0,10000 dm\xb3 (M = 249,71): m = 2,50 g|c_alq2.sol\n\
@F\n\
Dados: preparar 100,00 mL de CuSO\u2084\xb75H\u2082O 0,100 mol dm\u207b\xb3 (M = 249,71 g mol\u207b\xb9).\n\
Objetivo: massa a pesar e incerteza relativa (balan\xe7a 0,01 g; bal\xe3o 0,10 mL).\n\
1. n = 0,100 \xd7 0,10000 = 0,0100 mol\n\
2. m = 0,0100 \xd7 249,71 = 2,50 g\n\
3. Incerteza relativa: 0,01 / 2,50 + 0,10 / 100,00 = 0,005, ou seja 0,5 %\n\
> Pesa 2,50 g; a concentra\xe7\xe3o fica com cerca de 0,5 % de incerteza.\n\
Verifica\xe7\xe3o: a maior parte da incerteza vem da balan\xe7a.\n\
@G\n\
Quanto mais rigorosos os instrumentos, menor a incerteza da concentra\xe7\xe3o.\n\
@H\n\
- Encher o bal\xe3o acima do tra\xe7o.\n\
- N\xe3o lavar o gobel\xe9 para dentro do bal\xe3o.\n\
- Usar o volume em mL na f\xf3rmula com c em mol dm\u207b\xb3.\n\
- Dissolver diretamente no bal\xe3o um s\xf3lido que dissolve mal.\n\
@I\n\
- m = c V M.\n\
- Dissolver, transferir, lavar, completar e homogeneizar.\n\
- Incerteza relativa \u2248 u(m)/m + u(V)/V.\n\
@J\n\
Porque se lava v\xe1rias vezes o gobel\xe9 para dentro do bal\xe3o?\n\
@R\n\
Para n\xe3o perder soluto: o que ficasse no gobel\xe9 baixaria a concentra\xe7\xe3o.\n\
@L aq23|AL 2.3 Dilui\xe7\xe3o de solu\xe7\xf5es|al 2.3 diluicao solucao-mae pipeta volumetrica pompete balao\
 volumetrico fator de diluicao volume a medir|c_fqso.dil|10|n\xfacleo|q5e:Dilui\xe7\xe3o de\
 solu\xe7\xf5es||Programa e AE FQ A 10.\xba, AL 2.3\n\
@A\n\
- Calcular o volume de solu\xe7\xe3o-m\xe3e a medir.\n\
- Preparar uma solu\xe7\xe3o dilu\xedda com pipeta e bal\xe3o volum\xe9trico.\n\
- Calcular o fator de dilui\xe7\xe3o.\n\
@B\n\
Diluir \xe9 juntar solvente: a quantidade de soluto mant\xe9m-se e a concentra\xe7\xe3o diminui.\n\
@C\n\
- Material: pipeta volum\xe9trica, pompete, bal\xe3o volum\xe9trico, gobel\xe9, esguicho, solu\xe7\xe3o-m\xe3e.\n\
- ci \xd7 Vi = cf \xd7 Vf (a quantidade de soluto n\xe3o muda).\n\
- Fator de dilui\xe7\xe3o: f = Vf / Vi = ci / cf.\n\
- Pipeta volum\xe9trica: mede um \xfanico volume com rigor.\n\
@D\n\
1. Calcula Vi = cf \xd7 Vf / ci.\n\
2. Lava a pipeta com um pouco da solu\xe7\xe3o-m\xe3e (ambientar).\n\
3. Mede Vi com a pipeta e a pompete (nunca com a boca).\n\
4. Transfere para o bal\xe3o de volume Vf.\n\
5. Completa com \xe1gua at\xe9 ao tra\xe7o e homogene\xedza.\n\
Na pipeta volum\xe9trica n\xe3o se sopra a \xfaltima gota.\n\
@F Dilui\xe7\xe3o|ci \xd7 Vi = cf \xd7 Vf|i: solu\xe7\xe3o-m\xe3e;f: solu\xe7\xe3o dilu\xedda|a mesma\
 quantidade de soluto|0,500 mol dm\u207b\xb3 para 0,100 em 100,0 mL: Vi = 20,0 mL|c_fqso.dil\n\
@F Fator de dilui\xe7\xe3o|f = Vf / Vi = ci / cf|f > 1|dilui\xe7\xe3o|100,0 mL / 20,0 mL: f = 5,00|c_fqso.dil\n\
@F\n\
Dados: solu\xe7\xe3o-m\xe3e 0,500 mol dm\u207b\xb3; preparar 100,0 mL de 0,100 mol dm\u207b\xb3.\n\
Objetivo: volume a medir e fator de dilui\xe7\xe3o.\n\
1. Vi = 0,100 \xd7 100,0 / 0,500 = 20,0 mL\n\
2. f = 100,0 / 20,0 = 5,00\n\
> Mede 20,0 mL com a pipeta; f = 5,00.\n\
Verifica\xe7\xe3o: ci / cf = 0,500 / 0,100 = 5,00, o mesmo valor.\n\
@G\n\
Diluir em v\xe1rios passos permite obter concentra\xe7\xf5es muito pequenas com rigor.\n\
@H\n\
- Medir Vi com uma proveta em vez de uma pipeta.\n\
- N\xe3o ambientar a pipeta.\n\
- Soprar a \xfaltima gota da pipeta volum\xe9trica.\n\
- Juntar Vf de \xe1gua em vez de completar at\xe9 Vf.\n\
@I\n\
- ci Vi = cf Vf.\n\
- f = Vf / Vi = ci / cf.\n\
- Pipeta volum\xe9trica e bal\xe3o volum\xe9trico.\n\
@J\n\
Para diluir uma solu\xe7\xe3o 10 vezes, num bal\xe3o de 50,0 mL, que volume de solu\xe7\xe3o-m\xe3e deves medir?\n\
@R\n\
Vi = 50,0 / 10 = 5,00 mL.\n\
@L aq24|AL 2.4 Rea\xe7\xe3o fotoqu\xedmica|al 2.4 reacao fotoquimica cloreto de prata nitrato de prata luz\
 precipitado escurecimento tubo de controlo filtros fotografia|c_fqel.fot|10|n\xfacleo|q6b:Rea\xe7\xf5es\
 fotoqu\xedmicas e radicais livres||Programa e AE FQ A 10.\xba, AL 2.4\n\
@A\n\
- Observar uma rea\xe7\xe3o provocada pela luz.\n\
- Comparar com um tubo protegido da luz (controlo).\n\
- Relacionar a rapidez da rea\xe7\xe3o com a energia dos fot\xf5es.\n\
@B\n\
O cloreto de prata \xe9 branco, mas \xe0 luz escurece: forma-se prata.\n\
Era assim que funcionava a fotografia antiga.\n\
@C\n\
- Material: tubos de ensaio, solu\xe7\xf5es de nitrato de prata e de cloreto de s\xf3dio, alum\xednio, luz e filtros.\n\
- Precipita\xe7\xe3o: Ag\u207a + Cl\u207b \u2192 AgCl (s\xf3lido branco).\n\
- Fotodecomposi\xe7\xe3o: 2 AgCl \u2192 2 Ag + Cl\u2082 (com luz).\n\
- A prata formada, em part\xedculas finas, \xe9 escura.\n\
@D\n\
1. Em dois tubos, junta NaCl e AgNO\u2083: forma-se AgCl, branco.\n\
2. Embrulha um dos tubos em papel de alum\xednio (controlo).\n\
3. Exp\xf5e os dois tubos \xe0 luz durante alguns minutos.\n\
4. Compara: o exposto escurece; o tapado fica branco.\n\
5. Com filtros: a luz azul escurece mais depressa do que a vermelha.\n\
O registo \xe9 qualitativo: cor, tempo e tipo de luz.\n\
Seguran\xe7a: o nitrato de prata mancha a pele; usa luvas e \xf3culos.\n\
@F Energia de um fot\xe3o|E = h c / \u03bb|\u03bb: comprimento de onda (m)|um fot\xe3o|\u03bb = 450 nm: E =\
 4,42 \xd7 10\u207b\xb9\u2079 J|c_fqel.fot\n\
@F\n\
Dados: luz azul (450 nm) e vermelha (700 nm).\n\
Objetivo: comparar a energia dos fot\xf5es.\n\
1. E(azul) = 6,63 \xd7 10\u207b\xb3\u2074 \xd7 3,00 \xd7 10\u2078 / (450 \xd7 10\u207b\u2079) = 4,42 \xd7\
 10\u207b\xb9\u2079 J\n\
2. E(vermelho) = 6,63 \xd7 10\u207b\xb3\u2074 \xd7 3,00 \xd7 10\u2078 / (700 \xd7 10\u207b\u2079) = 2,84 \xd7\
 10\u207b\xb9\u2079 J\n\
3. Raz\xe3o: 4,42 / 2,84 = 1,56\n\
> Os fot\xf5es azuis t\xeam cerca de 1,56 vezes mais energia.\n\
Verifica\xe7\xe3o: menor \u03bb, maior energia.\n\
@G\n\
A luz de maior energia (azul, violeta, UV) decomp\xf5e o AgCl mais depressa.\n\
O tubo de controlo prova que o escurecimento se deve \xe0 luz.\n\
@H\n\
- N\xe3o usar um tubo de controlo.\n\
- Tirar conclus\xf5es sem expor os tubos o mesmo tempo.\n\
- Achar que a luz vermelha \xe9 mais energ\xe9tica por ser \"quente\".\n\
- Tocar no nitrato de prata sem luvas.\n\
@I\n\
- AgCl escurece com a luz: forma-se prata.\n\
- Controlo: tubo tapado.\n\
- Fot\xf5es de menor \u03bb t\xeam mais energia.\n\
@J\n\
Para que serve o tubo embrulhado em papel de alum\xednio?\n\
@R\n\
\xc9 o controlo: mostra que, sem luz, o AgCl n\xe3o escurece.\n\
@E 1|aqe1|Massa e volume de uma gota|c_alq1.gota|aq11\n\
Enunciado: 25 gotas de \xe1gua t\xeam 1,30 g. Calcula a massa e o volume de uma gota.\n\
Dados: m = 1,30 g; n = 25; \u03c1 = 1,00 g cm\u207b\xb3.\n\
Resolu\xe7\xe3o:\n\
1. m(gota) = 1,30 / 25 = 0,0520 g\n\
2. V = 0,0520 / 1,00 = 0,0520 cm\xb3\n\
Resultado: m(gota) = 0,0520 g e V = 0,0520 cm\xb3.\n\
Interpreta\xe7\xe3o: 1 cm\xb3 de \xe1gua tem cerca de 19 gotas.\n\
Erros a evitar: dividir 25 pela massa.\n\
@E 2|aqe2|Que metal \xe9?|c_alq1.dens|aq13\n\
Enunciado: m = 10,80 g; m1 = 80,00 g; m2 = 86,74 g. Identifica o metal (Al 2,70; Zn 7,14; Fe 7,87; Cu 8,96).\n\
Resolu\xe7\xe3o:\n\
1. \xc1gua deslocada: 10,80 + 80,00 - 86,74 = 4,06 g\n\
2. d = 10,80 / 4,06 = 2,66\n\
3. O mais pr\xf3ximo \xe9 o alum\xednio: erro = |2,66 - 2,70| / 2,70 \xd7 100 = 1,5 %\n\
Resultado: d \u2248 2,66; deve ser alum\xednio.\n\
Interpreta\xe7\xe3o: um erro de 1,5 % \xe9 aceit\xe1vel nesta atividade.\n\
Erros a evitar: usar m1 - m2 em vez de m + m1 - m2.\n\
@E 3|aqe3|Preparar e diluir, com incerteza|c_alq2.sol|aq23\n\
Enunciado: dissolvem-se 0,585 g de NaCl (M = 58,44 g mol\u207b\xb9) num bal\xe3o de 100,00 mL.\n\
Depois, 10,00 mL desta solu\xe7\xe3o s\xe3o dilu\xeddos num bal\xe3o de 50,00 mL.\n\
Calcula a concentra\xe7\xe3o final e a sua incerteza relativa (balan\xe7a 0,001 g; bal\xf5es 0,10 mL e 0,06\
 mL; pipeta 0,02 mL).\n\
Resolu\xe7\xe3o:\n\
1. c(m\xe3e) = 0,585 / (58,44 \xd7 0,10000) = 0,100 mol dm\u207b\xb3\n\
2. c(final) = 0,100 \xd7 10,00 / 50,00 = 0,0200 mol dm\u207b\xb3\n\
3. Incerteza relativa: 0,001/0,585 + 0,10/100,00 + 0,02/10,00 + 0,06/50,00 = 0,0059\n\
Resultado: c \u2248 0,0200 mol dm\u207b\xb3, com cerca de 0,6 % de incerteza.\n\
Interpreta\xe7\xe3o: cada instrumento acrescenta incerteza; a balan\xe7a \xe9 a parcela maior.\n\
Erros a evitar: esquecer as incertezas da pipeta e do segundo bal\xe3o.\n\
"
