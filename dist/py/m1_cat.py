# m1_cat.py - M1TR4M: catalogo gerado pelo build (nao editar).
# TEMAS: id|disc|grupo|titulo|pacote|exercicios|n licoes|1.a licao|n exerc.|1.o exerc.|n cartoes|1.o cartao|calculadoras|licoes
# As calculadoras estao em m1_calc (carregado a pedido).
NLIC = 155
NEX = 313
NCART = 425
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
    "r7|F|r|Revis\xf5es do 7.\xba ano|p_r7|x_r7|3|56|8|114|8|154|c_comu.uni c_comu.sci|r7a r7b r7c",
    "r8|F|r|Revis\xf5es do 8.\xba ano|p_r8|x_r8|5|59|8|122|12|162|c_fqlg.ace c_fqat.mm c_fqel.fot|r8a r8b r8c r8d r8e",
    "r9|F|r|Revis\xf5es do 9.\xba ano|p_r9|x_r9|4|64|8|130|12|174|c_fqci.ohm c_fqci.pot c_fqel.conf c_comu.uni|r9a r9b r9c r9d",
    "n7|M|7|N\xfameros (7.\xba ano)|p_n7|x_n7|5|68|9|138|14|186|c_mnum.frac c_mnum.pot c_mnum.mdc c_mrea.rad|n7a n7b n7c n7d n7e",
    "a7|M|7|\xc1lgebra (7.\xba ano)|p_a7|x_a7|5|73|9|147|11|200|c_mprp.seq c_mpol.pol c_mexp.eq1 c_mprp.prop c_mprp.perc|a7a a7b a7c a7d a7e",
    "g7|M|7|Geometria e Medida (7.\xba ano)|p_g7|x_g7|5|78|9|156|14|211|c_mgeo.ang c_mgeo.area c_matt.sem|g7a g7b g7c g7d g7e",
    "d7|M|7|Dados (7.\xba ano)|p_d7|x_d7|3|83|8|165|8|225|c_mprb.freq c_mate.uni c_mate.caule|d7a d7b d7c",
    "n8|M|8|N\xfameros (8.\xba ano)|p_n8|x_n8|3|86|8|173|8|233|c_mnum.pot c_mrea.ncie c_mnum.dec c_comu.sci|n8a n8b n8c",
    "a8|M|8|\xc1lgebra (8.\xba ano)|p_a8|x_a8|5|89|9|181|12|241|c_mpol.pol c_mpol.fat c_mexp.eq1 c_mexp.sis c_matf.afim c_mpol.ruf|a8a a8b a8c a8d a8e",
    "g8|M|8|Geometria e Medida (8.\xba ano)|p_g8|x_g8|4|94|8|190|10|253|c_matt.pit c_mgtr.iso c_matg.dist c_matv.vet|g8a g8b g8c g8d",
    "d8|M|8|Dados (8.\xba ano)|p_d8|x_d8|2|98|8|198|4|263|c_mate.uni c_mate.cls c_mprb.freq|d8a d8b",
    "n9|M|9|N\xfameros (9.\xba ano)|p_n9|x_n9|3|100|8|206|6|267|c_mrea.rad c_mrea.intv c_mrea.ncie|n9a n9b n9c",
    "a9|M|9|\xc1lgebra (9.\xba ano)|p_a9|x_a9|4|103|8|214|8|273|c_mexp.ineq c_matq.q2 c_mpol.fat c_mprp.inv c_matf.fx|a9a a9b a9c a9d",
    "g9|M|9|Geometria e Medida (9.\xba ano)|p_g9|x_g9|6|107|10|222|15|281|c_mgtr.circ c_matr.tri c_matr.rad c_msol.sol c_matr.res|g9a g9b g9c g9d g9e g9f",
    "d9|M|9|Probabilidades (9.\xba ano)|p_d9|x_d9|3|113|8|232|7|296|c_mprb.prob c_mprb.dados c_mprb.urna|d9a d9b d9c",
    "m2|M|t|Estat\xedstica|p_m2|x_m2|9|116|13|240|27|303|c_mate.uni c_mate.cls c_mate.caule c_comd.reg|m2a m2b m2c m2d m2e m2f m2g m2h m2i",
    "m3|M|t|Geometria sint\xe9tica no plano|p_m3|x_m3|6|125|11|253|19|330|c_matt.pn c_matt.insc c_matt.euler c_matt.pit c_matt.sem|m3a m3b m3c m3d m3e m3f",
    "m4|M|t|Fun\xe7\xf5es: generalidades, fun\xe7\xe3o afim e condi\xe7\xf5es|p_m4|x_m4|4|131|10|264|13|349|c_matf.fx c_matf.afim c_comd.reg|m4a m4b m4c m4d",
    "m5|M|t|Fun\xe7\xe3o quadr\xe1tica|p_m5|x_m5|4|135|10|274|15|362|c_matq.q2 c_matq.iq c_matq.tf c_comu.sci|m5a m5b m5c m5d",
    "m6|M|t|Fun\xe7\xf5es definidas por ramos e fun\xe7\xe3o m\xf3dulo|p_m6|x_m6|3|139|8|284|9|377|c_matf.ramos c_matf.mod c_matf.fx|m6a m6b m6c",
    "m7|M|t|Geometria anal\xedtica no plano e no espa\xe7o|p_m7|x_m7|6|142|10|292|18|386|c_matg.dist c_matg.reta c_matg.medz c_matg.circ c_matg.cond|m7a m7b m7c m7d m7e m7f",
    "m8|M|t|Vetores no plano e no espa\xe7o|p_m8|x_m8|7|148|11|302|21|404|c_matv.vet c_matv.retav c_matv.bar|m8a m8b m8c m8d m8e m8f m8g",
)
BUILD = "2026-10-24"
# Partes do indice da pesquisa: modulo:disciplina
IDX = "m1_idx:F m1_idx2:F m1_idxm:M m1_idxm2:M"
LIMITES = "- Tempos e mem\xf3ria medidos s\xf3 no computador (MicroPython 1.12 de 32 bits). No aparelho, v\xea o Diagn\xf3stico.\n\
- S\xf3 n\xfameros reais: n\xe3o h\xe1 n\xfameros complexos.\n\
- Configura\xe7\xe3o eletr\xf3nica: Z de 1 a 36. Raio at\xf3mico e energia de ioniza\xe7\xe3o: Z de 1 a 54.\n\
- Lewis, geometria e polaridade: s\xf3 as mol\xe9culas da tabela do programa.\n\
- Acerto de equa\xe7\xf5es qu\xedmicas: at\xe9 8 esp\xe9cies.\n\
- Constantes do exame (IAVE): confirma o ano da tabela que vais usar.\n\
- A pesquisa procura o texto escrito: n\xe3o corrige erros de escrita.\n\
- AL 2.3 e AL 2.4 de Qu\xedmica: usam as calculadoras gerais (dilui\xe7\xe3o e fot\xf5es).\n\
- Edi\xe7\xf5es de reserva: s\xf3 FQ do 10.\xba ano ou Matem\xe1tica do 7.\xba ao 9.\xba ano, sem pesquisa."
