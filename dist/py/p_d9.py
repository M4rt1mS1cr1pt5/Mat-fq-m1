# p_d9.py - M1TR4M: Probabilidades (9.\xba ano) (gerado pelo build).
D = "@V 1\n\
@N 3\n\
@T Probabilidades (9.\xba ano)\n\
@L d9a|Experi\xeancias aleat\xf3rias e lei de Laplace|experiencia aleatoria espaco de resultados\
 acontecimento certo impossivel provavel probabilidade lei de laplace casos favoraveis casos possiveis\
 acontecimento contrario frequencia relativa|c_mprb.prob|9|n\xfacleo|||AE Matem\xe1tica 9.\xba ano, Probabilidades\n\
@A\n\
- Identificar experi\xeancias aleat\xf3rias e o espa\xe7o de resultados.\n\
- Calcular probabilidades com a lei de Laplace.\n\
- Usar o acontecimento contr\xe1rio.\n\
@C\n\
- Experi\xeancia aleat\xf3ria: n\xe3o se sabe o resultado antes de a fazer.\n\
- Lei de Laplace (resultados igualmente prov\xe1veis): P(A) = casos favor\xe1veis / casos poss\xedveis.\n\
- 0 \u2264 P(A) \u2264 1; imposs\xedvel: 0; certo: 1.\n\
- Contr\xe1rio: P(n\xe3o A) = 1 - P(A).\n\
- Com muitas repeti\xe7\xf5es, a frequ\xeancia relativa aproxima-se da probabilidade.\n\
@F Lei de Laplace|P(A) = casos favor\xe1veis / casos poss\xedveis|resultados igualmente prov\xe1veis|0 \u2264\
 P(A) \u2264 1|3 bolas azuis em 10: P = 0,3|c_mprb.prob\n\
@F Acontecimento contr\xe1rio|P(n\xe3o A) = 1 - P(A)|A: acontecimento|A e o contr\xe1rio n\xe3o acontecem\
 juntos|P(A) = 0,3: P(n\xe3o A) = 0,7|c_mprb.prob\n\
@F\n\
Dados: um saco tem 3 bolas azuis, 5 vermelhas e 2 verdes; tira-se uma ao acaso.\n\
Objetivo: P(azul), P(azul ou verde) e P(n\xe3o vermelha).\n\
1. Casos poss\xedveis: 3 + 5 + 2 = 10.\n\
2. P(azul) = 3/10 = 0,3.\n\
3. P(azul ou verde) = 5/10 = 0,5.\n\
4. P(n\xe3o vermelha) = 1 - 5/10 = 0,5.\n\
> 0,3; 0,5 e 0,5.\n\
Verifica\xe7\xe3o: 0,3 + 0,5 + 0,2 = 1 (todas as cores) \u2713.\n\
@J\n\
Lan\xe7a-se um dado. Qual \xe9 a probabilidade de sair um n\xfamero maior do que 4?\n\
@R\n\
Casos favor\xe1veis: 5 e 6; P = 2/6 = 1/3.\n\
@L d9b|Experi\xeancias compostas: tabelas de dupla entrada|experiencia composta dois dados duas moedas tabela\
 de dupla entrada soma produto casos possiveis igualmente provaveis|c_mprb.dados|9|n\xfacleo|||AE\
 Matem\xe1tica 9.\xba ano, Probabilidades (experi\xeancias compostas)\n\
@A\n\
- Organizar os resultados de duas experi\xeancias numa tabela.\n\
- Contar os casos poss\xedveis e os favor\xe1veis.\n\
- Calcular probabilidades em experi\xeancias compostas.\n\
@C\n\
- Dois dados: tabela 6 \xd7 6 com 36 casos igualmente prov\xe1veis.\n\
- Em cada c\xe9lula escreve-se o resultado (soma, produto...).\n\
- Contam-se as c\xe9lulas favor\xe1veis.\n\
- Duas moedas: EE, EN, NE, NN (4 casos); EN e NE s\xe3o diferentes.\n\
- N\xe3o confundir \"soma 7\" (6 casos) com \"par (3, 4)\" (2 casos).\n\
@F Probabilidade com a tabela|P(A) = c\xe9lulas favor\xe1veis / total de c\xe9lulas|tabela de dupla\
 entrada|c\xe9lulas igualmente prov\xe1veis|soma 7 com dois dados: 6/36 = 1/6|c_mprb.dados\n\
@F\n\
Dados: lan\xe7am-se dois dados e somam-se os pontos.\n\
Objetivo: P(soma 7) e P(soma > 9).\n\
1. Soma 7: (1,6) (2,5) (3,4) (4,3) (5,2) (6,1), ou seja, 6 casos.\n\
2. P(soma 7) = 6/36 = 1/6\n\
3. Soma > 9: 10 (3 casos), 11 (2) e 12 (1): 6 casos; P = 6/36 = 1/6.\n\
> As duas probabilidades valem 1/6.\n\
Verifica\xe7\xe3o: a soma 7 \xe9 a mais prov\xe1vel (6 casos em 36).\n\
@J\n\
Lan\xe7am-se duas moedas. Qual \xe9 a probabilidade de sa\xedrem faces diferentes?\n\
@R\n\
EN e NE: P = 2/4 = 0,5.\n\
@L d9c|Diagramas em \xe1rvore: com e sem reposi\xe7\xe3o|diagrama em arvore extracao com reposicao sem\
 reposicao duas extracoes multiplicar probabilidades ramos caminhos|c_mprb.urna|9|n\xfacleo|||AE\
 Matem\xe1tica 9.\xba ano, Probabilidades (diagramas em \xe1rvore)\n\
@A\n\
- Construir um diagrama em \xe1rvore.\n\
- Distinguir extra\xe7\xf5es com e sem reposi\xe7\xe3o.\n\
- Calcular probabilidades de caminhos e de acontecimentos.\n\
@C\n\
- Cada ramo leva a probabilidade desse passo.\n\
- Ao longo de um caminho, multiplicam-se as probabilidades.\n\
- V\xe1rios caminhos favor\xe1veis: somam-se as probabilidades.\n\
- Sem reposi\xe7\xe3o: na 2.\xaa extra\xe7\xe3o h\xe1 menos uma bola (e menos uma da cor que saiu).\n\
- A soma das probabilidades de todos os caminhos \xe9 1.\n\
@F Probabilidade de um caminho|P(1.\xaa A e 2.\xaa B) = P(A) \xd7 P(B depois de A)|ramos do\
 diagrama|multiplica-se ao longo do caminho|3 azuis e 2 brancas, sem reposi\xe7\xe3o: P(AA) = 3/5 \xd7 2/4|c_mprb.urna\n\
@F\n\
Dados: uma caixa tem 3 bolas azuis e 2 brancas; tiram-se duas, sem reposi\xe7\xe3o.\n\
Objetivo: P(duas azuis) e P(cores diferentes).\n\
1. P(AA) = 3/5 \xd7 2/4 = 3/10\n\
2. P(AB) = 3/5 \xd7 2/4 = 3/10 e P(BA) = 2/5 \xd7 3/4 = 3/10.\n\
3. Cores diferentes: 3/10 + 3/10 = 3/5\n\
> P(duas azuis) = 0,3 e P(cores diferentes) = 0,6.\n\
Verifica\xe7\xe3o: P(BB) = 2/5 \xd7 1/4 = 1/10 e 3/10 + 3/5 + 1/10 = 1 \u2713.\n\
@J\n\
E se a extra\xe7\xe3o fosse com reposi\xe7\xe3o, qual seria P(duas azuis)?\n\
@R\n\
3/5 \xd7 3/5 = 9/25 = 0,36.\n\
@E 1|d9e1|Escolher um aluno|c_mprb.prob|d9a\n\
Enunciado: uma turma tem 12 rapazes e 16 raparigas. Escolhe-se um aluno ao acaso. Qual \xe9 a probabilidade\
 de ser rapariga?\n\
Resolu\xe7\xe3o:\n\
1. Casos poss\xedveis: 12 + 16 = 28.\n\
2. P(rapariga) = 16/28 = 4/7 \u2248 0,57.\n\
Resultado: 4/7, cerca de 57%.\n\
Interpreta\xe7\xe3o: \xe9 mais prov\xe1vel sair uma rapariga do que um rapaz.\n\
Erros a evitar: dividir 16 por 12 (rapazes) em vez de 28 (todos).\n\
@E 2|d9e2|Produto de dois dados|c_mprb.dados|d9b\n\
Enunciado: lan\xe7am-se dois dados e multiplicam-se os pontos. Qual \xe9 a probabilidade de o produto ser par?\n\
Resolu\xe7\xe3o:\n\
1. O produto \xe9 \xedmpar s\xf3 se os dois forem \xedmpares: 3 \xd7 3 = 9 casos.\n\
2. Produto par: 36 - 9 = 27 casos.\n\
3. P(par) = 27/36 = 3/4\n\
Resultado: 3/4, ou seja, 75%.\n\
Interpreta\xe7\xe3o: basta um dos dados ser par para o produto ser par.\n\
Erros a evitar: pensar que par e \xedmpar t\xeam a mesma probabilidade.\n\
@E 3|d9e3|Pelo menos uma verde|c_mprb.urna|d9c\n\
Enunciado: um saco tem 2 bolas verdes e 4 amarelas. Tiram-se duas, sem reposi\xe7\xe3o. Qual \xe9 a\
 probabilidade de sair pelo menos uma verde?\n\
Resolu\xe7\xe3o:\n\
1. Contr\xe1rio: nenhuma verde, ou seja, duas amarelas.\n\
2. P(duas amarelas) = 4/6 \xd7 3/5 = 2/5\n\
3. P(pelo menos uma verde) = 1 - 2/5 = 3/5\n\
Resultado: 3/5, ou seja, 0,6.\n\
Interpreta\xe7\xe3o: com o contr\xe1rio evita-se somar tr\xeas caminhos.\n\
Erros a evitar: esquecer que, sem reposi\xe7\xe3o, ficam 5 bolas.\n\
"
