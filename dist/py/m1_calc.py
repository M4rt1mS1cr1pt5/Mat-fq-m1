# m1_calc.py - M1TR4M: catalogo das calculadoras gerado pelo build
# (id|nome|disciplina|tema; as palavras-chave estao no indice da pesquisa).
CALC = "c_alf1.plano|AL 1.1 Plano inclinado: Ec e dist\xe2ncia|F|af\n\
c_alf1.ress|AL 1.2 Queda e ressalto de uma bola|F|af\n\
c_alf1.pilha|AL 2.1 Caracter\xedsticas de uma pilha|F|af\n\
c_alf2.painel|AL 3.1 Painel fotovoltaico|F|af\n\
c_alf2.cap|AL 3.2 Capacidade t\xe9rmica m\xe1ssica|F|af\n\
c_alf2.fusao|AL 3.3 Balan\xe7o energ\xe9tico (fus\xe3o do gelo)|F|af\n\
c_alq1.gota|AL 1.1 Volume e mol\xe9culas de uma gota de \xe1gua|F|aq\n\
c_alq1.chama|AL 1.2 Teste de chama|F|aq\n\
c_alq1.dens|AL 1.3 Densidade relativa (picn\xf3metro)|F|aq\n\
c_alq2.misc|AL 2.1 Miscibilidade de l\xedquidos|F|aq\n\
c_alq2.sol|AL 2.2 Solu\xe7\xe3o a partir de soluto s\xf3lido|F|aq\n\
c_comd.cte|Constantes e dados|C|\n\
c_comd.exp|Dados experimentais|C|\n\
c_comd.reg|Regress\xe3o linear e gr\xe1fico|C|\n\
c_comu.sci|Calculadora cient\xedfica|C|\n\
c_comu.sf|Algarismos significativos|C|\n\
c_comu.uni|Conversor de unidades|C|\n\
c_comu.pre|Prefixos do SI|C|\n\
c_fqat.mm|Massa molar|F|q1\n\
c_fqat.qm|Quantidade de mat\xe9ria|F|q1\n\
c_fqat.ar|Massa at\xf3mica relativa m\xe9dia|F|q1\n\
c_fqat.fr|Fra\xe7\xe3o molar e fra\xe7\xe3o m\xe1ssica|F|q1\n\
c_fqci.ohm|Resist\xeancia el\xe9trica (U = R I)|F|f2\n\
c_fqci.rho|Resistividade (R = \u03c1 \u2113 / A)|F|f2\n\
c_fqci.assoc|Resist\xeancias em s\xe9rie e em paralelo|F|f2\n\
c_fqci.ger|Gerador: for\xe7a eletromotriz e resist\xeancia interna|F|f2\n\
c_fqci.pot|Pot\xeancia, energia e custo el\xe9tricos|F|f2\n\
c_fqel.fot|Espetros e fot\xf5es|F|q2\n\
c_fqel.hid|\xc1tomo de hidrog\xe9nio|F|q2\n\
c_fqel.conf|Configura\xe7\xe3o eletr\xf3nica|F|q2\n\
c_fqen.em|Energia cin\xe9tica, potencial e mec\xe2nica|F|f1\n\
c_fqen.cons|Conserva\xe7\xe3o da energia mec\xe2nica|F|f1\n\
c_fqen.tr|Trabalho de uma for\xe7a constante|F|f1\n\
c_fqen.wp|Trabalho do peso|F|f1\n\
c_fqen.tec|Teorema da energia cin\xe9tica|F|f1\n\
c_fqen.pot|Pot\xeancia|F|f1\n\
c_fqen.ren|Rendimento|F|f1\n\
c_fqlg.lew|Lewis, geometria e polaridade|F|q4\n\
c_fqlg.dh|Entalpia de rea\xe7\xe3o (energias de liga\xe7\xe3o)|F|q6\n\
c_fqlg.ace|Acerto de equa\xe7\xf5es qu\xedmicas|F|r8\n\
c_fqso.con|Concentra\xe7\xe3o de uma solu\xe7\xe3o|F|q5\n\
c_fqso.pes|Massa de soluto a pesar|F|q5\n\
c_fqso.per|Percentagem e partes por milh\xe3o|F|q5\n\
c_fqso.dil|Dilui\xe7\xe3o de solu\xe7\xf5es|F|q5\n\
c_fqso.gas|Gases (PTN)|F|q5\n\
c_fqte.cal|Capacidade t\xe9rmica m\xe1ssica (Q = m c \u0394T)|F|f3\n\
c_fqte.est|Mudan\xe7a de estado (Q = m \u0394H)|F|f3\n\
c_fqte.eq|Temperatura de equil\xedbrio de uma mistura|F|f3\n\
c_fqte.cond|Condu\xe7\xe3o t\xe9rmica (P = k A \u0394T / \u2113)|F|f3\n\
c_fqte.pl|Primeira Lei da Termodin\xe2mica|F|f3\n\
c_fqte.pv|Painel fotovoltaico e irradi\xe2ncia|F|f3\n\
c_mate.uni|Estat\xedstica de uma vari\xe1vel|M|m2\n\
c_mate.cls|Dados em classes e histograma|M|m2\n\
c_mate.caule|Caule-e-folhas|M|m2\n\
c_matf.fx|Fun\xe7\xe3o escrita por ti (tabela, zeros, gr\xe1fico)|M|m4\n\
c_matf.afim|Fun\xe7\xe3o afim|M|m4\n\
c_matf.ramos|Fun\xe7\xe3o definida por ramos|M|m6\n\
c_matf.mod|Fun\xe7\xe3o m\xf3dulo a\u2223x - h\u2223 + k|M|m6\n\
c_matg.dist|Dist\xe2ncia e ponto m\xe9dio|M|m7\n\
c_matg.reta|Equa\xe7\xe3o reduzida da reta|M|m7\n\
c_matg.medz|Mediatriz e plano mediador|M|m7\n\
c_matg.circ|Circunfer\xeancia e superf\xedcie esf\xe9rica|M|m7\n\
c_matg.cond|Condi\xe7\xf5es no plano (regi\xe3o)|M|m7\n\
c_matq.q2|Equa\xe7\xe3o do 2.\xba grau e fun\xe7\xe3o quadr\xe1tica|M|m5\n\
c_matq.iq|Inequa\xe7\xf5es do 2.\xba grau|M|m5\n\
c_matq.tf|Transforma\xe7\xf5es de fun\xe7\xf5es|M|m5\n\
c_matr.tri|Tri\xe2ngulo ret\xe2ngulo: seno, cosseno e tangente|M|g9\n\
c_matr.rad|Graus, radianos e valores exatos|M|g9\n\
c_matr.res|Leis dos senos e dos cossenos (extens\xe3o)|M|g9\n\
c_matt.pn|Pontos not\xe1veis do tri\xe2ngulo (com desenho)|M|m3\n\
c_matt.insc|Circunfer\xeancias inscrita e circunscrita|M|m3\n\
c_matt.euler|Reta de Euler e nove pontos|M|m3\n\
c_matt.pit|Teorema de Pit\xe1goras e rec\xedproco|M|g8\n\
c_matt.sem|Semelhan\xe7a de figuras|M|g7\n\
c_matv.vet|Opera\xe7\xf5es com vetores|M|m8\n\
c_matv.retav|Equa\xe7\xe3o vetorial da reta|M|m8\n\
c_matv.bar|Baricentro com vetores|M|m8\n\
c_mexp.eq1|Equa\xe7\xe3o do 1.\xba grau (passo a passo)|M|a7\n\
c_mexp.ineq|Inequa\xe7\xe3o do 1.\xba grau|M|a9\n\
c_mexp.sis|Sistema de duas equa\xe7\xf5es (substitui\xe7\xe3o)|M|a8\n\
c_mgeo.ang|\xc2ngulos, tri\xe2ngulos e pol\xedgonos|M|g7\n\
c_mgeo.area|\xc1reas e per\xedmetros de figuras planas|M|g7\n\
c_mgtr.iso|Isometrias: transla\xe7\xe3o, reflex\xe3o e rota\xe7\xe3o|M|g8\n\
c_mgtr.circ|\xc2ngulos na circunfer\xeancia|M|g9\n\
c_mnum.frac|Fra\xe7\xf5es e n\xfameros racionais (passo a passo)|M|n7\n\
c_mnum.pot|Pot\xeancias e regras das pot\xeancias|M|n7\n\
c_mnum.mdc|Fatores primos, m.d.c. e m.m.c.|M|n7\n\
c_mnum.dec|D\xedzimas e fra\xe7\xf5es|M|n8\n\
c_mpol.pol|Polin\xf3mios: desenvolver e simplificar|M|a8\n\
c_mpol.fat|Fatorizar e resolver por fatoriza\xe7\xe3o|M|a8\n\
c_mpol.ruf|Divis\xe3o de polin\xf3mios e regra de Ruffini|M|a8\n\
c_mprb.freq|Tabela de frequ\xeancias e gr\xe1fico de barras|M|d7\n\
c_mprb.prob|Probabilidade: lei de Laplace|M|d9\n\
c_mprb.dados|Dois dados ou moedas (dupla entrada)|M|d9\n\
c_mprb.urna|Duas extra\xe7\xf5es com e sem reposi\xe7\xe3o (\xe1rvore)|M|d9\n\
c_mprp.seq|Sequ\xeancias: termo geral|M|a7\n\
c_mprp.prop|Proporcionalidade direta|M|a7\n\
c_mprp.inv|Proporcionalidade inversa|M|a9\n\
c_mprp.perc|Percentagens|M|a7\n\
c_mrea.ncie|Nota\xe7\xe3o cient\xedfica|M|n8\n\
c_mrea.rad|Ra\xedzes e radicais|M|n9\n\
c_mrea.intv|Intervalos de n\xfameros reais|M|n9\n\
c_msol.sol|S\xf3lidos: \xe1reas e volumes|M|g9"
