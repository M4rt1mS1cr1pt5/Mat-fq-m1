# m1_cat.py - M1TR4M: catalogo gerado pelo build (nao editar).
# TEMAS: id|disc|grupo|titulo|pacote|exercicios|n licoes|1.a licao|n exerc.|1.o exerc.|n cartoes|1.o cartao|calculadoras|licoes
# CALC: id|nome|disciplina|tema (as palavras-chave estao no indice da pesquisa)
NLIC = 72
NEX = 144
NCART = 201
TEMAS = (
    "q1|F|q|Massa e tamanho dos \xe1tomos|p_q1|x_q1|5|0|10|0|18|0|c_fqat.qm c_fqat.mm c_fqat.ar c_fqat.fr c_comu.sci c_comu.sf c_comu.uni|q1a q1b q1c q1d q1e",
    "q2|F|q|Energia dos eletr\xf5es nos \xe1tomos|p_q2|x_q2|5|5|10|10|14|18|c_fqel.fot c_fqel.hid c_fqel.conf c_comu.sci c_comu.uni|q2a q2b q2c q2d q2e",
    "q3|F|q|Tabela Peri\xf3dica|p_q3|x_q3|3|10|9|20|8|32|c_fqel.conf c_fqel.fot c_fqat.mm|q3a q3b q3c",
    "q4|F|q|Liga\xe7\xe3o qu\xedmica|p_q4|x_q4|6|13|10|29|13|40|c_fqlg.lew c_fqlg.dh c_fqel.conf c_fqat.mm|q4a q4b q4c q4d q4e q4f",
    "q5|F|q|Gases e dispers\xf5es|p_q5|x_q5|5|19|10|39|14|53|c_fqso.gas c_fqso.con c_fqso.pes c_fqso.per c_fqso.dil c_fqat.mm c_fqat.fr|q5a q5b q5c q5d q5e",
    "q6|F|q|Transforma\xe7\xf5es qu\xedmicas|p_q6|x_q6|3|24|9|49|9|67|c_fqlg.dh c_fqel.fot c_fqlg.ace|q6a q6b q6c",
    "f1|F|f|Energia e movimentos|p_f1|x_f1|5|27|10|58|15|76|c_fqen.em c_fqen.cons c_fqen.tr c_fqen.wp c_fqen.tec c_fqen.pot c_fqen.ren|f1a f1b f1c f1d f1e",
    "f2|F|f|Energia e fen\xf3menos el\xe9tricos|p_f2|x_f2|5|32|10|68|16|91|c_fqci.ohm c_fqci.rho c_fqci.assoc c_fqci.ger c_fqci.pot c_fqen.ren|f2a f2b f2c f2d f2e",
    "f3|F|f|Energia, fen\xf3menos t\xe9rmicos e radia\xe7\xe3o|p_f3|x_f3|6|37|10|78|17|107|c_fqte.cal c_fqte.est c_fqte.eq c_fqte.cond c_fqte.pl c_fqte.pv c_fqen.ren c_comu.uni|f3a f3b f3c f3d f3e f3f",
    "aq|F|a|Atividades laboratoriais de Qu\xedmica|p_aq|x_aq|7|43|14|88|16|124|c_alq1.gota c_alq1.chama c_alq1.dens c_alq2.misc c_alq2.sol c_fqso.dil c_comd.exp|aq11 aq12 aq13 aq21 aq22 aq23 aq24",
    "af|F|a|Atividades laboratoriais de F\xedsica|p_af|x_af|6|50|12|102|14|140|c_alf1.plano c_alf1.ress c_alf1.pilha c_alf2.painel c_alf2.cap c_alf2.fusao c_comd.reg c_comd.exp|af11 af12 af21 af31 af32 af33",
    "r7|F|r|Revis\xf5es do 7.\xba ano|p_r7|x_r7|3|56|6|114|8|154|c_comu.uni c_comu.sci|r7a r7b r7c",
    "r8|F|r|Revis\xf5es do 8.\xba ano|p_r8|x_r8|5|59|8|120|12|162|c_fqlg.ace c_fqat.mm c_fqel.fot|r8a r8b r8c r8d r8e",
    "r9|F|r|Revis\xf5es do 9.\xba ano|p_r9|x_r9|4|64|6|128|12|174|c_fqci.ohm c_fqci.pot c_fqel.conf c_comu.uni|r9a r9b r9c r9d",
    "m5|M|t|Fun\xe7\xe3o quadr\xe1tica|p_m5|x_m5|4|68|10|134|15|186|c_matq.q2 c_matq.iq c_matq.tf c_comu.sci|m5a m5b m5c m5d",
)
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
c_matq.q2|Equa\xe7\xe3o do 2.\xba grau e fun\xe7\xe3o quadr\xe1tica|M|m5\n\
c_matq.iq|Inequa\xe7\xf5es do 2.\xba grau|M|m5\n\
c_matq.tf|Transforma\xe7\xf5es de fun\xe7\xf5es|M|m5"
BUILD = "2026-10-22"
# Partes do indice da pesquisa: modulo:disciplina
IDX = "m1_idx:F m1_idx2:F m1_idxm:M"
LIMITES = "ver RELATORIO.md"
