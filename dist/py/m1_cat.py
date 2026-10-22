# m1_cat.py - M1TR4M: catalogo gerado pelo build (nao editar).
# TEMAS: id|disc|grupo|titulo|pacote|exercicios|n licoes|1.a licao|n exerc.|1.o exerc.|n cartoes|1.o cartao|calculadoras|licoes
# CALC: id|nome|disciplina|tema (as palavras-chave estao no indice da pesquisa)
NLIC = 36
NEX = 78
NCART = 106
TEMAS = (
    "q1|F|q|Massa e tamanho dos \xe1tomos|p_q1|x_q1|5|0|10|0|18|0|c_fqat.qm c_fqat.mm c_fqat.ar c_fqat.fr c_comu.sci c_comu.sf c_comu.uni|q1a q1b q1c q1d q1e",
    "q2|F|q|Energia dos eletr\xf5es nos \xe1tomos|p_q2|x_q2|5|5|10|10|14|18|c_fqel.fot c_fqel.hid c_fqel.conf c_comu.sci c_comu.uni|q2a q2b q2c q2d q2e",
    "q3|F|q|Tabela Peri\xf3dica|p_q3|x_q3|3|10|9|20|8|32|c_fqel.conf c_fqel.fot c_fqat.mm|q3a q3b q3c",
    "q4|F|q|Liga\xe7\xe3o qu\xedmica|p_q4|x_q4|6|13|10|29|13|40|c_fqlg.lew c_fqlg.dh c_fqel.conf c_fqat.mm|q4a q4b q4c q4d q4e q4f",
    "q5|F|q|Gases e dispers\xf5es|p_q5|x_q5|5|19|10|39|14|53|c_fqso.gas c_fqso.con c_fqso.pes c_fqso.per c_fqso.dil c_fqat.mm c_fqat.fr|q5a q5b q5c q5d q5e",
    "q6|F|q|Transforma\xe7\xf5es qu\xedmicas|p_q6|x_q6|3|24|9|49|9|67|c_fqlg.dh c_fqel.fot c_fqlg.ace|q6a q6b q6c",
    "f1|F|f|Energia e movimentos|p_f1|x_f1|5|27|10|58|15|76|c_fqen.em c_fqen.cons c_fqen.tr c_fqen.wp c_fqen.tec c_fqen.pot c_fqen.ren|f1a f1b f1c f1d f1e",
    "m5|M|t|Fun\xe7\xe3o quadr\xe1tica|p_m5|x_m5|4|32|10|68|15|91|c_matq.q2 c_matq.iq c_matq.tf c_comu.sci|m5a m5b m5c m5d",
)
CALC = "c_comd.cte|Constantes e dados|C|\n\
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
c_matq.q2|Equa\xe7\xe3o do 2.\xba grau e fun\xe7\xe3o quadr\xe1tica|M|m5\n\
c_matq.iq|Inequa\xe7\xf5es do 2.\xba grau|M|m5\n\
c_matq.tf|Transforma\xe7\xf5es de fun\xe7\xf5es|M|m5"
BUILD = "2026-10-22"
# Partes do indice da pesquisa: modulo:disciplina
IDX = "m1_idx:F m1_idxm:M"
LIMITES = "ver RELATORIO.md"
