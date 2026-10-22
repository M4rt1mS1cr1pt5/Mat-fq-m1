# p_m1.py - M1TR4M: Modelos matem\xe1ticos para a cidadania (gerado pelo build).
D = "@V 1\n\
@N 10\n\
@T Modelos matem\xe1ticos para a cidadania\n\
@L m1a|Elei\xe7\xf5es: maioria simples e maioria absoluta|eleicao votacao tabela de preferencias maioria\
 simples relativa maioria absoluta votantes empate metade|c_matc.vot|10|n\xfacleo|||AE Mat A 10.\xba, Modelos\
 matem\xe1ticos para a cidadania (elei\xe7\xf5es)\n\
@A\n\
- Ler uma tabela de prefer\xeancias.\n\
- Encontrar o vencedor por maioria simples.\n\
- Verificar se h\xe1 maioria absoluta.\n\
@B\n\
Numa elei\xe7\xe3o, cada votante ordena os candidatos.\n\
A tabela de prefer\xeancias junta numa coluna os votantes com a mesma ordem.\n\
@C\n\
- Cada coluna: n.\xba de votantes e ordem dos candidatos.\n\
- Maioria simples (relativa): mais votos em 1.\xba lugar.\n\
- Maioria absoluta: mais de metade dos votos.\n\
- Com n votos, \xe9 preciso ter mais de n / 2.\n\
- Pode haver maioria simples sem maioria absoluta.\n\
@D\n\
Exemplo: 29 votantes e tr\xeas candidatos.\n\
- 10 votantes: A, B, C (por esta ordem);\n\
- 8 votantes: B, C, A;\n\
- 7 votantes: C, B, A;\n\
- 4 votantes: C, A, B.\n\
- Votos em 1.\xba lugar: A 10, B 8 e C 7 + 4 = 11.\n\
- Maioria simples: ganha C.\n\
- Metade de 29 \xe9 14,5: ningu\xe9m tem maioria absoluta.\n\
- C precisava de 15 votos para a maioria absoluta.\n\
@F Maioria absoluta|votos > n / 2|n: total de votos|votos v\xe1lidos|29 votos: s\xe3o precisos 15|c_matc.vot\n\
@F Percentagem de votos|p = votos / n \xd7 100|n: total de votos|votos v\xe1lidos|C: 11 / 29 \xd7 100 \u2248\
 37,9%|c_matc.vot\n\
@F\n\
Dados: 21 votantes; 9 preferem A, B, C; 7 preferem B, C, A; 5 preferem C, B, A.\n\
Objetivo: vencedor por maioria simples; ver se h\xe1 maioria absoluta.\n\
1. Votos em 1.\xba lugar: A 9, B 7 e C 5.\n\
2. Maioria simples: ganha A.\n\
3. Metade de 21 \xe9 10,5 e A tem s\xf3 9.\n\
> A ganha por maioria simples, sem maioria absoluta.\n\
Verifica\xe7\xe3o: 9 + 7 + 5 = 21 votantes.\n\
@G\n\
Na elei\xe7\xe3o do Presidente da Rep\xfablica \xe9 preciso mais de metade dos votos v\xe1lidos.\n\
Se ningu\xe9m os tiver, h\xe1 uma segunda volta.\n\
@H\n\
- Confundir maioria simples com maioria absoluta.\n\
- Achar que metade dos votos chega (\xe9 preciso mais de metade).\n\
- Esquecer colunas onde o candidato tamb\xe9m est\xe1 em 1.\xba lugar.\n\
@I\n\
- Maioria simples: mais votos em 1.\xba lugar.\n\
- Maioria absoluta: mais de metade.\n\
- Somar todas as colunas do candidato.\n\
@J\n\
Com 40 votos, quantos s\xe3o precisos para a maioria absoluta?\n\
@R\n\
Mais de 20: pelo menos 21 votos.\n\
@L m1b|M\xe9todo de Borda|metodo de borda pontos ordenacao preferencias pontuacao ranking eleicao\
 concurso|c_matc.vot|10|n\xfacleo|m1a:Elei\xe7\xf5es: maioria simples e maioria absoluta||AE Mat A 10.\xba,\
 Modelos matem\xe1ticos para a cidadania (elei\xe7\xf5es)\n\
@A\n\
- Atribuir pontos pelo m\xe9todo de Borda.\n\
- Encontrar o vencedor de Borda.\n\
- Comparar com a maioria simples.\n\
@B\n\
O m\xe9todo de Borda conta a ordena\xe7\xe3o toda, e n\xe3o s\xf3 o 1.\xba lugar.\n\
@C\n\
- Com n candidatos: n pontos ao 1.\xba lugar, n - 1 ao 2.\xba, ..., 1 ao \xfaltimo.\n\
- Pontos de um candidato: soma de votantes \xd7 pontos, coluna a coluna.\n\
- Ganha quem tiver mais pontos.\n\
- Se o 1.\xba tiver n - 1 pontos e o \xfaltimo 0, o vencedor \xe9 o mesmo.\n\
@D\n\
Exemplo: a tabela de 29 votantes da li\xe7\xe3o anterior (10 ABC, 8 BCA, 7 CBA, 4 CAB).\n\
- A: 10 \xd7 3 + 8 \xd7 1 + 7 \xd7 1 + 4 \xd7 2 = 53 pontos.\n\
- B: 10 \xd7 2 + 8 \xd7 3 + 7 \xd7 2 + 4 \xd7 1 = 62 pontos.\n\
- C: 10 \xd7 1 + 8 \xd7 2 + 7 \xd7 3 + 4 \xd7 3 = 59 pontos.\n\
Ganha B, que s\xf3 tem 8 votos em 1.\xba lugar.\n\
Confirma\xe7\xe3o: 53 + 62 + 59 = 174, que \xe9 29 \xd7 6.\n\
@F Pontos de Borda|P = \u03a3 votantes \xd7 pontos|n: n.\xba de candidatos;pontos: n ao 1.\xba lugar, 1 ao\
 \xfaltimo|ordena\xe7\xf5es completas|3 candidatos: 3, 2 e 1 pontos|c_matc.vot\n\
@F Total de pontos|T = votantes \xd7 n (n + 1) / 2|n: n.\xba de candidatos|pontos n, ..., 1|29 votantes e 3\
 candidatos: T = 174|c_matc.vot\n\
@F\n\
Dados: 17 votantes; 7 ABCD, 6 BCDA, 4 CDBA.\n\
Objetivo: vencedor pelo m\xe9todo de Borda.\n\
1. Pontos: 4 ao 1.\xba, 3 ao 2.\xba, 2 ao 3.\xba e 1 ao 4.\xba.\n\
2. A: 7 \xd7 4 + 6 \xd7 1 + 4 \xd7 1 = 38.\n\
3. B: 7 \xd7 3 + 6 \xd7 4 + 4 \xd7 2 = 53.\n\
4. C: 7 \xd7 2 + 6 \xd7 3 + 4 \xd7 4 = 48 e D: 7 \xd7 1 + 6 \xd7 2 + 4 \xd7 3 = 31.\n\
> Ganha B, com 53 pontos (A teria a maioria simples).\n\
Verifica\xe7\xe3o: 38 + 53 + 48 + 31 = 170, que \xe9 17 \xd7 10.\n\
@G\n\
Concursos como o Festival da Eurovis\xe3o e alguns pr\xe9mios desportivos usam pontos parecidos com os de Borda.\n\
@H\n\
- Dar os pontos ao contr\xe1rio (n ao \xfaltimo).\n\
- Esquecer de multiplicar pelos votantes da coluna.\n\
- Concluir que o mais votado em 1.\xba lugar ganha sempre.\n\
@I\n\
- n pontos ao 1.\xba, ..., 1 ao \xfaltimo.\n\
- Pontos: \u03a3 votantes \xd7 pontos.\n\
- Total: votantes \xd7 (1 + ... + n).\n\
@J\n\
Com 3 candidatos e 10 votantes, quantos pontos se distribuem ao todo?\n\
@R\n\
10 \xd7 (3 + 2 + 1) = 60 pontos.\n\
@L m1c|Segunda volta e elimina\xe7\xe3o sucessiva|segunda volta eliminacao sucessiva dois mais votados\
 transferencia de votos analise de sistemas eleitorais comparar metodos|c_matc.vot|10|n\xfacleo|m1b:M\xe9todo\
 de Borda||AE Mat A 10.\xba, Modelos matem\xe1ticos para a cidadania (an\xe1lise de sistemas eleitorais)\n\
@A\n\
- Aplicar a segunda volta.\n\
- Aplicar a elimina\xe7\xe3o sucessiva.\n\
- Comparar os resultados de v\xe1rios m\xe9todos.\n\
@B\n\
Com os mesmos votos, m\xe9todos diferentes podem dar vencedores diferentes.\n\
@C\n\
- Segunda volta: sem maioria absoluta, os dois mais votados v\xe3o a nova vota\xe7\xe3o.\n\
- Cada votante escolhe o que prefere dos dois.\n\
- Elimina\xe7\xe3o sucessiva: sai o menos votado em 1.\xba lugar.\n\
- Os seus votos passam \xe0 prefer\xeancia seguinte.\n\
- Repete-se at\xe9 algu\xe9m ter maioria absoluta.\n\
@D\n\
Exemplo: a tabela de 29 votantes (10 ABC, 8 BCA, 7 CBA, 4 CAB).\n\
- Segunda volta entre C (11) e A (10).\n\
- A est\xe1 \xe0 frente de C s\xf3 na 1.\xaa coluna: 10 votos.\n\
- C fica com 8 + 7 + 4 = 19 votos: ganha C.\n\
- Elimina\xe7\xe3o: sai B e os seus 8 votos passam a C.\n\
- C fica com 11 + 8 = 19 votos, mais de 14,5: ganha C.\n\
Resumo: maioria simples C, segunda volta C, Borda B.\n\
@F Segunda volta|2.\xaa volta entre os dois mais votados|votos: prefer\xeancia entre os dois|sem maioria\
 absoluta na 1.\xaa volta|C (11) e A (10): C ganha por 19 a 10|c_matc.vot\n\
@F Elimina\xe7\xe3o sucessiva|sai o menos votado; os votos passam ao seguinte|menos votado: em 1.\xba\
 lugar|at\xe9 haver maioria absoluta|sai B: C passa de 11 para 19 votos|c_matc.vot\n\
@F\n\
Dados: 22 votantes; 9 ABC, 8 CBA, 5 BCA.\n\
Objetivo: vencedor por segunda volta, por elimina\xe7\xe3o e por Borda.\n\
1. 1.\xba lugar: A 9, C 8 e B 5; ningu\xe9m passa de 11.\n\
2. Segunda volta, A contra C: A 9 e C 8 + 5 = 13. Ganha C.\n\
3. Elimina\xe7\xe3o: sai B e os seus votos passam a C, que fica com 13. Ganha C.\n\
4. Borda: A 40, B 49 e C 43 pontos. Ganharia B.\n\
> Segunda volta e elimina\xe7\xe3o: C; Borda: B.\n\
Verifica\xe7\xe3o: 40 + 49 + 43 = 132, que \xe9 22 \xd7 6.\n\
@G\n\
Escolher o sistema eleitoral \xe9 uma decis\xe3o pol\xedtica: o mesmo eleitorado pode eleger candidatos diferentes.\n\
@H\n\
- Na 2.\xaa volta, contar s\xf3 os votos em 1.\xba lugar.\n\
- Na elimina\xe7\xe3o, esquecer de passar os votos do eliminado.\n\
- Achar que o m\xe9todo n\xe3o muda o vencedor.\n\
@I\n\
- 2.\xaa volta: os dois mais votados.\n\
- Elimina\xe7\xe3o: sai o \xfaltimo, at\xe9 haver maioria absoluta.\n\
- M\xe9todos diferentes, vencedores diferentes.\n\
@J\n\
Na elimina\xe7\xe3o sucessiva, para onde v\xe3o os votos do candidato eliminado?\n\
@R\n\
Para o candidato seguinte na ordem de prefer\xeancia de cada votante.\n\
@L m1d|M\xe9todo de Condorcet (aprofundamento)|condorcet duelos dois a dois vencedor de condorcet paradoxo de\
 condorcet ciclo preferencias teorema de arrow|c_matc.vot|10|aprofundamento|m1c:Segunda volta e\
 elimina\xe7\xe3o sucessiva||AE Mat A 10.\xba, Modelos matem\xe1ticos para a cidadania (aprofundamento)\n\
@A\n\
- Comparar candidatos dois a dois.\n\
- Encontrar o vencedor de Condorcet.\n\
- Reconhecer o paradoxo de Condorcet.\n\
@B\n\
O vencedor de Condorcet ganha todos os duelos.\n\
Uma maioria prefere-o a cada um dos outros.\n\
@C\n\
- Para cada par, conta-se quem prefere um ao outro.\n\
- Vencedor de Condorcet: ganha a todos, um a um.\n\
- Pode n\xe3o existir: as prefer\xeancias da maioria podem formar um ciclo.\n\
- Paradoxo: A vence B, B vence C e C vence A.\n\
- Com n candidatos h\xe1 n (n - 1) / 2 duelos.\n\
@D\n\
Exemplo: a tabela de 29 votantes (10 ABC, 8 BCA, 7 CBA, 4 CAB).\n\
- A contra B: 10 + 4 = 14 para A e 8 + 7 = 15 para B.\n\
- A contra C: 10 para A e 8 + 7 + 4 = 19 para C.\n\
- B contra C: 10 + 8 = 18 para B e 7 + 4 = 11 para C.\n\
B ganha os dois duelos: \xe9 o vencedor de Condorcet (e de Borda).\n\
Paradoxo: 3 votantes com ABC, BCA e CAB.\n\
- A vence B, B vence C e C vence A, sempre por 2 a 1.\n\
- N\xe3o h\xe1 vencedor de Condorcet.\n\
@F Duelo de Condorcet|X vence Y se mais votantes preferem X a Y|X, Y: candidatos|ordena\xe7\xf5es completas|A\
 contra B: 14 a 15, ganha B|c_matc.vot\n\
@F N\xfamero de duelos|n (n - 1) / 2|n: n.\xba de candidatos|um duelo por par|4 candidatos: 6 duelos|c_matc.vot\n\
@F\n\
Dados: 22 votantes; 9 ABC, 8 CBA, 5 BCA.\n\
Objetivo: vencedor de Condorcet.\n\
1. A contra B: A 9; B 8 + 5 = 13. Ganha B.\n\
2. A contra C: A 9; C 8 + 5 = 13. Ganha C.\n\
3. B contra C: B 9 + 5 = 14; C 8. Ganha B.\n\
> B \xe9 o vencedor de Condorcet.\n\
Verifica\xe7\xe3o: em cada duelo os votos somam 22.\n\
@G\n\
Aqui a 2.\xaa volta d\xe1 C, mas B ganha um duelo contra qualquer outro.\n\
O teorema de Arrow diz que nenhum m\xe9todo de vota\xe7\xe3o \xe9 perfeito.\n\
@H\n\
- Contar s\xf3 os votos em 1.\xba lugar num duelo.\n\
- Esquecer um dos pares.\n\
- Achar que h\xe1 sempre vencedor de Condorcet.\n\
@I\n\
- Duelos dois a dois.\n\
- Vencedor de Condorcet: ganha todos.\n\
- Pode n\xe3o existir (ciclo).\n\
@J\n\
Com 5 candidatos, quantos duelos h\xe1?\n\
@R\n\
5 \xd7 4 / 2 = 10 duelos.\n\
@L m1e|M\xe9todo de Hondt|metodo de hondt mandatos deputados divisores quocientes circulo eleitoral\
 assembleia da republica lei eleitoral empate ultimo mandato|c_matc.mand|10|n\xfacleo|m1a:Elei\xe7\xf5es:\
 maioria simples e maioria absoluta||AE Mat A 10.\xba, Modelos matem\xe1ticos para a cidadania (partilha de\
 mandatos); Lei n.\xba 14/79, art. 16.\xba\n\
@A\n\
- Distribuir mandatos pelo m\xe9todo de Hondt.\n\
- Aplicar a regra de empate da lei eleitoral.\n\
- Interpretar o \xfaltimo mandato.\n\
@B\n\
Os mandatos s\xe3o dados um a um \xe0 lista com o maior quociente nesse momento.\n\
@C\n\
- Divide-se o n.\xba de votos de cada lista por 1, 2, 3, 4, ...\n\
- Os mandatos v\xe3o para os maiores quocientes.\n\
- Empate no \xfaltimo mandato: fica a lista com menos votos (Lei n.\xba 14/79, art. 16.\xba).\n\
- \xc9 o m\xe9todo das elei\xe7\xf5es legislativas, em cada c\xedrculo.\n\
@D\n\
Exemplo: 7 mandatos; A 12 000, B 8 000, C 5 000 e D 2 500 votos.\n\
- A: 12 000; 6 000; 4 000; 3 000.\n\
- B: 8 000; 4 000; 2 666,67.\n\
- C: 5 000; 2 500. D: 2 500.\n\
- Por ordem: 12 000 (A), 8 000 (B), 6 000 (A), 5 000 (C), 4 000 (A e B) e 3 000 (A).\n\
- Resultado: A 4, B 2, C 1 e D 0.\n\
- O 7.\xba mandato foi para A (3 000); o seguinte seria de B (2 666,67).\n\
@F Quociente de Hondt|q = votos / d|d = 1, 2, 3, ...|um quociente por mandato|12 000 / 4 = 3 000|c_matc.mand\n\
@F Empate (Lei n.\xba 14/79, art. 16.\xba)|\xfaltimo mandato: lista com menos votos|quocientes iguais de\
 listas diferentes|resta um s\xf3 mandato|A 3 000 e B 1 500, 2 mandatos: 1 para cada|c_matc.mand\n\
@F\n\
Dados: 5 mandatos; X 6 000, Y 3 800 e Z 1 500 votos.\n\
Objetivo: mandatos de cada lista pelo m\xe9todo de Hondt.\n\
1. X: 6 000; 3 000; 2 000; 1 500.\n\
2. Y: 3 800; 1 900. Z: 1 500.\n\
3. Por ordem: 6 000 (X), 3 800 (Y), 3 000 (X), 2 000 (X) e 1 900 (Y).\n\
> X 3, Y 2 e Z 0.\n\
Verifica\xe7\xe3o: 3 + 2 + 0 = 5 mandatos.\n\
@G\n\
Os 230 deputados da Assembleia da Rep\xfablica s\xe3o eleitos em 22 c\xedrculos pelo m\xe9todo de Hondt.\n\
Nos c\xedrculos pequenos, os partidos mais votados ficam com quase todos os mandatos.\n\
@H\n\
- Dividir pelo n\xfamero de mandatos em vez de 1, 2, 3, ...\n\
- Dar o empate \xe0 lista mais votada.\n\
- Esquecer as listas com poucos votos.\n\
@I\n\
- Divisores 1, 2, 3, ...\n\
- Ganham os maiores quocientes.\n\
- Empate no \xfaltimo: lista com menos votos.\n\
@J\n\
A lista A tem 9 000 votos e j\xe1 tem 2 mandatos. Qual \xe9 o seu quociente seguinte?\n\
@R\n\
9 000 / 3 = 3 000.\n\
@L m1f|M\xe9todo de Sainte-Lagu\xeb e compara\xe7\xe3o com Hondt|sainte-lague divisores impares\
 proporcionalidade comparacao com hondt partidos pequenos percentagem de\
 mandatos|c_matc.mand|10|n\xfacleo|m1e:M\xe9todo de Hondt||AE Mat A 10.\xba, Modelos matem\xe1ticos para a\
 cidadania (partilha de mandatos)\n\
@A\n\
- Distribuir mandatos pelo m\xe9todo de Sainte-Lagu\xeb.\n\
- Comparar com o m\xe9todo de Hondt.\n\
- Comparar a % de votos com a % de mandatos.\n\
@B\n\
Com divisores mais afastados, as listas grandes perdem vantagem.\n\
@C\n\
- Divisores: 1, 3, 5, 7, ... (os \xedmpares).\n\
- Os mandatos v\xe3o para os maiores quocientes.\n\
- Tende a ser mais proporcional do que o Hondt.\n\
- O Hondt favorece as listas mais votadas.\n\
- Compara-se a % de votos com a % de mandatos.\n\
@D\n\
Exemplo: 7 mandatos; A 12 000, B 8 000, C 5 000 e D 2 500 votos.\n\
- A: 12 000; 4 000; 2 400. B: 8 000; 2 666,67.\n\
- C: 5 000. D: 2 500.\n\
- Por ordem: 12 000 (A), 8 000 (B), 5 000 (C), 4 000 (A), 2 666,67 (B), 2 500 (D) e 2 400 (A).\n\
- Resultado: A 3, B 2, C 1 e D 1 (no Hondt, D n\xe3o elegia).\n\
- A tem 43,6% dos votos.\n\
- A fica com 42,9% dos mandatos (no Hondt, 57,1%).\n\
@F Quociente de Sainte-Lagu\xeb|q = votos / (2k + 1)|k: mandatos j\xe1 obtidos pela lista|um quociente por\
 mandato|12 000 / 5 = 2 400|c_matc.mand\n\
@F Percentagem de mandatos|m / M \xd7 100|m: mandatos da lista;M: total de mandatos|compara-se com a % de\
 votos|A: 3 / 7 \xd7 100 \u2248 42,9%|c_matc.mand\n\
@F\n\
Dados: 5 mandatos; X 6 000, Y 3 800 e Z 1 500 votos.\n\
Objetivo: mandatos por Sainte-Lagu\xeb e compara\xe7\xe3o com o Hondt.\n\
1. X: 6 000; 2 000; 1 200.\n\
2. Y: 3 800; 1 266,67. Z: 1 500; 500.\n\
3. Por ordem: 6 000 (X), 3 800 (Y), 2 000 (X), 1 500 (Z) e 1 266,67 (Y).\n\
> X 2, Y 2 e Z 1 (no Hondt: X 3, Y 2 e Z 0).\n\
Verifica\xe7\xe3o: Z tem 13,3% dos votos e fica com 20% dos mandatos.\n\
@G\n\
V\xe1rios pa\xedses, como a Alemanha, a Noruega e a Su\xe9cia, usam variantes do m\xe9todo de Sainte-Lagu\xeb.\n\
@H\n\
- Usar divisores pares (2, 4, 6, ...).\n\
- Achar que os dois m\xe9todos d\xe3o sempre o mesmo resultado.\n\
- Comparar mandatos sem olhar para a % de votos.\n\
@I\n\
- Divisores 1, 3, 5, 7, ...\n\
- Mais proporcional do que o Hondt.\n\
- O Hondt favorece as listas grandes.\n\
@J\n\
No m\xe9todo de Sainte-Lagu\xeb, por que n\xfamero se divide para o 4.\xba quociente de uma lista?\n\
@R\n\
Pelo 4.\xba n\xfamero \xedmpar: 7.\n\
@L m1g|Sal\xe1rio: bruto, l\xedquido e valor por hora|salario bruto liquido seguranca social 11% entidade\
 empregadora 23,75% retencao na fonte 14 meses subsidios valor por hora horas extra trabalho\
 suplementar|c_matd.sal|10|n\xfacleo|||AE Mat A 10.\xba, Modelos matem\xe1ticos para a cidadania (finan\xe7as\
 pessoais); C\xf3digo do Trabalho, art. 268.\xba e 271.\xba\n\
@A\n\
- Calcular o sal\xe1rio l\xedquido a partir do bruto.\n\
- Calcular o sal\xe1rio anual e o valor da hora.\n\
- Calcular o pagamento de horas extra.\n\
@B\n\
O sal\xe1rio bruto \xe9 o combinado; o l\xedquido \xe9 o que chega \xe0 conta, depois dos descontos.\n\
@C\n\
- L\xedquido = bruto - descontos.\n\
- Seguran\xe7a Social: 11% do bruto (e a empresa paga 23,75%).\n\
- Reten\xe7\xe3o na fonte: adiantamento mensal do IRS.\n\
- 14 sal\xe1rios por ano (com os subs\xeddios de f\xe9rias e de Natal).\n\
- Valor da hora: (mensal \xd7 12) / (52 \xd7 horas por semana).\n\
- Horas extra em dia \xfatil: + 25% e + 37,5%.\n\
@D\n\
Exemplo: bruto de 1 200 \u20ac, 40 h por semana e reten\xe7\xe3o de 12%.\n\
- Seguran\xe7a Social: 0,11 \xd7 1 200 = 132 \u20ac.\n\
- Reten\xe7\xe3o de IRS: 0,12 \xd7 1 200 = 144 \u20ac.\n\
- L\xedquido: 1 200 - 132 - 144 = 924 \u20ac.\n\
- Bruto anual: 14 \xd7 1 200 = 16 800 \u20ac.\n\
- Valor da hora: 1 200 \xd7 12 / (52 \xd7 40) \u2248 6,92 \u20ac.\n\
- 2 horas extra num dia \xfatil: 1,25 e 1,375 vezes o valor da hora, ou seja, \u2248 18,17 \u20ac.\n\
- Custo para a empresa: 1,2375 \xd7 1 200 = 1 485 \u20ac.\n\
@F Sal\xe1rio l\xedquido|L = B - SS - IRS - outros|B: bruto;SS: Seguran\xe7a Social (0,11 B);IRS:\
 reten\xe7\xe3o na fonte|trabalho por conta de outrem|B = 1 200 \u20ac e reten\xe7\xe3o de 12%: L = 924\
 \u20ac|c_matd.sal\n\
@F Valor da hora|Rh = (Rm \xd7 12) / (52 \xd7 n)|Rm: sal\xe1rio mensal;n: horas por semana|C\xf3digo do\
 Trabalho, art. 271.\xba|1 200 \u20ac e 40 h: Rh \u2248 6,92 \u20ac|c_matd.sal\n\
@F\n\
Dados: bruto de 1 500 \u20ac; reten\xe7\xe3o de IRS de 15%; ADSE de 3,5%.\n\
Objetivo: sal\xe1rio l\xedquido mensal e anual.\n\
1. Seguran\xe7a Social: 0,11 \xd7 1 500 = 165 \u20ac.\n\
2. IRS: 0,15 \xd7 1 500 = 225 \u20ac.\n\
3. ADSE: 0,035 \xd7 1 500 = 52,50 \u20ac.\n\
4. L\xedquido: 1 500 - 165 - 225 - 52,50 = 1 057,50 \u20ac.\n\
> 1 057,50 \u20ac por m\xeas; 14 \xd7 1 057,50 = 14 805 \u20ac por ano.\n\
Verifica\xe7\xe3o: os descontos somam 442,50 \u20ac, 29,5% do bruto.\n\
@G\n\
Numa proposta de emprego, conv\xe9m saber se o valor \xe9 bruto ou l\xedquido e se s\xe3o 12 ou 14 meses.\n\
@H\n\
- Calcular as percentagens sobre o l\xedquido.\n\
- Esquecer os subs\xeddios (14 meses).\n\
- Dividir o sal\xe1rio mensal por 4 semanas: um m\xeas tem cerca de 4,33 semanas.\n\
@I\n\
- L = B - descontos.\n\
- Seguran\xe7a Social: 11% e 23,75% (empresa).\n\
- 14 sal\xe1rios por ano.\n\
- Rh = (Rm \xd7 12) / (52 \xd7 n).\n\
@J\n\
Qual \xe9 o desconto para a Seguran\xe7a Social de um sal\xe1rio bruto de 2 000 \u20ac?\n\
@R\n\
0,11 \xd7 2 000 = 220 \u20ac.\n\
@L m1h|IRS: escal\xf5es e progressividade|irs imposto escaloes taxa marginal taxa media progressividade\
 rendimento coletavel coleta parcela a abater reembolso artigo 68|c_matd.irs|10|n\xfacleo|m1g:Sal\xe1rio:\
 bruto, l\xedquido e valor por hora||AE Mat A 10.\xba, Modelos matem\xe1ticos para a cidadania (finan\xe7as\
 pessoais); CIRS, art. 68.\xba, Lei n.\xba 73-A/2025 (tabela de 2026, a confirmar no Portal das Finan\xe7as)\n\
@A\n\
- Calcular o IRS por escal\xf5es.\n\
- Distinguir taxa marginal de taxa m\xe9dia.\n\
- Perceber por que o IRS \xe9 progressivo.\n\
@B\n\
Quem ganha mais paga uma percentagem maior.\n\
Mas cada parte do rendimento s\xf3 paga a taxa do seu escal\xe3o.\n\
@C\n\
- Rendimento colet\xe1vel: o que fica depois das dedu\xe7\xf5es espec\xedficas.\n\
- Cada parte do rendimento paga a taxa do seu escal\xe3o.\n\
- Taxa marginal: a do \xfaltimo escal\xe3o atingido.\n\
- Taxa m\xe9dia = coleta / rendimento colet\xe1vel.\n\
- Coleta = R \xd7 taxa marginal - parcela a abater.\n\
@D\n\
Escal\xf5es de 2026 (CIRS, art. 68.\xba, Lei n.\xba 73-A/2025):\n\
- at\xe9 8 342 \u20ac: 12,5%;\n\
- at\xe9 12 587 \u20ac: 15,7%;\n\
- at\xe9 17 838 \u20ac: 21,2%;\n\
- at\xe9 23 089 \u20ac: 24,1%;\n\
- at\xe9 29 397 \u20ac: 31,1%;\n\
- at\xe9 43 090 \u20ac: 34,9%;\n\
- at\xe9 46 566 \u20ac: 43,1%;\n\
- at\xe9 86 634 \u20ac: 44,6%;\n\
- mais de 86 634 \u20ac: 48%.\n\
Exemplo: R = 20 000 \u20ac.\n\
- 8 342 \xd7 0,125 + 4 245 \xd7 0,157 + 5 251 \xd7 0,212 + 2 162 \xd7 0,241 \u2248 3 343,47 \u20ac.\n\
- Taxa marginal 24,1%; taxa m\xe9dia \u2248 16,7%.\n\
@F Coleta por escal\xf5es|C = \u03a3 parte em cada escal\xe3o \xd7 taxa do escal\xe3o|R: rendimento\
 colet\xe1vel|tabela do ano (CIRS, art. 68.\xba)|R = 20 000 \u20ac: C \u2248 3 343,47 \u20ac|c_matd.irs\n\
@F Taxa m\xe9dia|tm = C / R \xd7 100|C: coleta;R: rendimento colet\xe1vel|R > 0|3 343,47 / 20 000 \xd7 100\
 \u2248 16,7%|c_matd.irs\n\
@F\n\
Dados: rendimento colet\xe1vel de 15 000 \u20ac, tabela de 2026.\n\
Objetivo: coleta, taxa marginal e taxa m\xe9dia.\n\
1. 1.\xba escal\xe3o: 8 342 \xd7 0,125 = 1 042,75 \u20ac.\n\
2. 2.\xba escal\xe3o: 4 245 \xd7 0,157 = 666,465 \u20ac.\n\
3. 3.\xba escal\xe3o: (15 000 - 12 587) \xd7 0,212 = 511,556 \u20ac.\n\
4. Coleta: 1 042,75 + 666,465 + 511,556 \u2248 2 220,77 \u20ac.\n\
5. Taxa marginal 21,2%; taxa m\xe9dia \u2248 14,8%.\n\
> Coleta \u2248 2 220,77 \u20ac.\n\
Verifica\xe7\xe3o: parcela a abater do 3.\xba escal\xe3o = 12 587 \xd7 0,212 - 1 709,215 = 959,229 \u20ac, e\
 15 000 \xd7 0,212 - 959,229 = 2 220,771 \u20ac.\n\
@G\n\
Numa tabela por escal\xf5es, um aumento nunca faz baixar o rendimento depois do imposto.\n\
S\xf3 a parte acima do limite paga a taxa nova.\n\
@H\n\
- Aplicar a taxa marginal a todo o rendimento.\n\
- Confundir taxa marginal com taxa m\xe9dia.\n\
- Usar a tabela de outro ano.\n\
@I\n\
- Cada parte paga a taxa do seu escal\xe3o.\n\
- Taxa marginal: a do \xfaltimo escal\xe3o.\n\
- Taxa m\xe9dia = coleta / rendimento.\n\
- Coleta = R \xd7 taxa - parcela a abater.\n\
@J\n\
Com a tabela de 2026, qual \xe9 a taxa marginal de um rendimento colet\xe1vel de 30 000 \u20ac?\n\
@R\n\
34,9%: 30 000 \u20ac est\xe1 no 6.\xba escal\xe3o (de 29 397 \u20ac a 43 090 \u20ac).\n\
@L m1i|Juro simples e juro composto|juro simples juro composto capital taxa de juro capitalizacao mensal\
 trimestral deposito a prazo taxa anual efetiva poupanca imposto 28% regra dos\
 72|c_matd.jur|10|n\xfacleo|||AE Mat A 10.\xba, Modelos matem\xe1ticos para a cidadania (poupan\xe7a e cr\xe9dito)\n\
@A\n\
- Calcular juros simples.\n\
- Calcular juros compostos com v\xe1rios per\xedodos de capitaliza\xe7\xe3o.\n\
- Comparar dep\xf3sitos a prazo.\n\
@B\n\
No juro composto, os juros tamb\xe9m rendem juros.\n\
O capital cresce cada vez mais depressa.\n\
@C\n\
- Juro simples: J = C \xd7 r \xd7 t; Cn = C (1 + r t).\n\
- Composto anual: Cn = C (1 + r)^t.\n\
- k capitaliza\xe7\xf5es por ano: i = r / k; Cn = C (1 + i)^(k t).\n\
- Taxa anual efetiva: (1 + i)^k - 1.\n\
- Os juros dos dep\xf3sitos pagam IRS (taxa liberat\xf3ria de 28%).\n\
@D\n\
Exemplo: 2 000 \u20ac a 4% ao ano durante 3 anos.\n\
- Simples: J = 2 000 \xd7 0,04 \xd7 3 = 240 \u20ac; Cn = 2 240 \u20ac.\n\
- Composto anual: Cn = 2 000 \xd7 1,04\xb3 \u2248 2 249,73 \u20ac.\n\
- Composto trimestral: i = 1%; Cn = 2 000 \xd7 1,01\xb9\xb2 \u2248 2 253,65 \u20ac.\n\
- Taxa anual efetiva com 1% ao trimestre: 1,01\u2074 - 1 \u2248 4,06%.\n\
- Com imposto de 28% sobre o juro simples: 240 \xd7 0,72 = 172,80 \u20ac.\n\
@F Juro simples|J = C \xd7 r \xd7 t|C: capital;r: taxa anual (decimal);t: tempo em anos|o juro n\xe3o \xe9\
 capitalizado|2 000 \u20ac a 4% durante 3 anos: J = 240 \u20ac|c_matd.jur\n\
@F Juro composto|Cn = C \xd7 (1 + r / k)^(k t)|k: capitaliza\xe7\xf5es por ano;t: tempo em anos|i = r / k em\
 cada per\xedodo|2 000 \u20ac a 4%, trimestral, 3 anos: 2 253,65 \u20ac|c_matd.jur\n\
@F\n\
Dados: dep\xf3sito de 5 000 \u20ac, a 3% ao ano, capitaliza\xe7\xe3o mensal, durante 2 anos.\n\
Objetivo: capital final e juro.\n\
1. i = 0,03 / 12 = 0,0025 (0,25% ao m\xeas).\n\
2. n = 12 \xd7 2 = 24 meses.\n\
3. Cn = 5 000 \xd7 1,0025\xb2\u2074 \u2248 5 308,79 \u20ac.\n\
4. Juro \u2248 308,79 \u20ac.\n\
> Cn \u2248 5 308,79 \u20ac.\n\
Verifica\xe7\xe3o: em juro simples seria 5 000 \xd7 (1 + 0,03 \xd7 2) = 5 300 \u20ac, um pouco menos.\n\
@G\n\
Regra dos 72: em juro composto a r% ao ano, um capital duplica em cerca de 72 / r anos.\n\
@H\n\
- Usar r = 3 em vez de 0,03.\n\
- Esquecer de dividir a taxa anual pelo n.\xba de capitaliza\xe7\xf5es.\n\
- P\xf4r no expoente os anos, e n\xe3o os per\xedodos.\n\
@I\n\
- J = C r t (simples).\n\
- Cn = C (1 + i)^n (composto).\n\
- i = r / k; n = k t.\n\
- Taxa efetiva: (1 + i)^k - 1.\n\
@J\n\
Quanto vale 1 000 \u20ac ao fim de 2 anos a 5% ao ano, em juro composto anual?\n\
@R\n\
1 000 \xd7 1,05\xb2 = 1 102,50 \u20ac.\n\
@L m1j|Presta\xe7\xf5es constantes e valor atual (aprofundamento)|prestacao constante emprestimo credito\
 valor atual amortizacao plano de pagamentos juros taeg|c_matd.prest|10|aprofundamento|m1i:Juro simples e\
 juro composto||AE Mat A 10.\xba, Modelos matem\xe1ticos para a cidadania (aprofundamento)\n\
@A\n\
- Calcular a presta\xe7\xe3o constante de um empr\xe9stimo.\n\
- Calcular o valor atual de uma s\xe9rie de presta\xe7\xf5es.\n\
- Ler as primeiras linhas de um plano de pagamentos.\n\
@B\n\
Cada presta\xe7\xe3o paga os juros do m\xeas e amortiza (abate) uma parte da d\xedvida.\n\
@C\n\
- i = r / k (taxa por per\xedodo); n = k t.\n\
- Presta\xe7\xe3o: p = V i / (1 - (1 + i)^(-n)).\n\
- Valor atual: V = p (1 - (1 + i)^(-n)) / i.\n\
- Juro de cada presta\xe7\xe3o = d\xedvida \xd7 i.\n\
- Amortiza\xe7\xe3o = p - juro.\n\
- No in\xedcio paga-se mais juro; no fim, mais amortiza\xe7\xe3o.\n\
@D\n\
Exemplo: empr\xe9stimo de 10 000 \u20ac a 6% ao ano, 5 anos, presta\xe7\xf5es mensais.\n\
- i = 0,06 / 12 = 0,005 e n = 60.\n\
- p = 10 000 \xd7 0,005 / (1 - 1,005^(-60)) \u2248 193,33 \u20ac.\n\
- Total pago \u2248 11 599,68 \u20ac; juros \u2248 1 599,68 \u20ac.\n\
- 1.\xaa presta\xe7\xe3o: juro de 10 000 \xd7 0,005 = 50 \u20ac e amortiza\xe7\xe3o de \u2248 143,33 \u20ac.\n\
@F Presta\xe7\xe3o constante|p = V \xd7 i / (1 - (1 + i)^(-n))|V: valor emprestado;i: taxa por per\xedodo;n:\
 n.\xba de presta\xe7\xf5es|i > 0|10 000 \u20ac, 0,5% ao m\xeas, 60 meses: p \u2248 193,33 \u20ac|c_matd.prest\n\
@F Valor atual|V = p \xd7 (1 - (1 + i)^(-n)) / i|p: presta\xe7\xe3o;i: taxa por per\xedodo;n: n.\xba de\
 presta\xe7\xf5es|i > 0|200 \u20ac por m\xeas, 0,5%, 60 meses: V \u2248 10 345,11 \u20ac|c_matd.prest\n\
@F\n\
Dados: podes pagar 150 \u20ac por m\xeas durante 4 anos, a 4,8% ao ano.\n\
Objetivo: quanto podes pedir emprestado (valor atual).\n\
1. i = 0,048 / 12 = 0,004 e n = 12 \xd7 4 = 48.\n\
2. V = 150 \xd7 (1 - 1,004^(-48)) / 0,004 \u2248 6 539,14 \u20ac.\n\
3. Total pago: 48 \xd7 150 = 7 200 \u20ac.\n\
4. Juros: \u2248 660,86 \u20ac.\n\
> Podes pedir cerca de 6 539,14 \u20ac.\n\
Verifica\xe7\xe3o: com V = 6 539,14 \u20ac, a f\xf3rmula da presta\xe7\xe3o d\xe1 \u2248 150,00 \u20ac.\n\
@G\n\
Num cr\xe9dito, a TAEG junta os juros e os outros custos.\n\
\xc9 o n\xfamero a comparar entre propostas de bancos diferentes.\n\
@H\n\
- Usar a taxa anual em vez da taxa do per\xedodo.\n\
- Esquecer o sinal negativo do expoente.\n\
- Achar que a amortiza\xe7\xe3o \xe9 igual todos os meses.\n\
@I\n\
- i = r / k; n = k t.\n\
- p = V i / (1 - (1 + i)^(-n)).\n\
- V = p (1 - (1 + i)^(-n)) / i.\n\
@J\n\
Num empr\xe9stimo de 5 000 \u20ac a 0,5% ao m\xeas, qual \xe9 o juro da 1.\xaa presta\xe7\xe3o?\n\
@R\n\
5 000 \xd7 0,005 = 25 \u20ac.\n\
@E 1|m1e1|Hondt com empate no \xfaltimo mandato|c_matc.mand|m1e\n\
Enunciado: num c\xedrculo com 4 mandatos, as listas P, Q e R t\xeam 3 000, 1 500 e 1 000 votos. Distribui os\
 mandatos pelo m\xe9todo de Hondt.\n\
Resolu\xe7\xe3o:\n\
1. Quocientes: P: 3 000; 1 500; 1 000. Q: 1 500; 750. R: 1 000.\n\
2. Mandatos 1 a 3: 3 000 (P), 1 500 (P) e 1 500 (Q).\n\
3. 4.\xba mandato: empate a 1 000 entre P e R.\n\
4. Pela lei (art. 16.\xba), fica a lista com menos votos: R.\n\
Resultado: P 2, Q 1 e R 1.\n\
Interpreta\xe7\xe3o: o empate \xe9 decidido a favor da lista menos votada.\n\
Erros a evitar: dar o empate \xe0 lista mais votada.\n\
@E 2|m1e2|IRS de 25 000 \u20ac por escal\xf5es|c_matd.irs|m1h\n\
Enunciado: com a tabela de IRS de 2026, calcula a coleta de um rendimento colet\xe1vel de 25 000 \u20ac e a\
 taxa m\xe9dia.\n\
Resolu\xe7\xe3o:\n\
1. 1.\xba escal\xe3o: 8 342 \xd7 0,125 = 1 042,75 \u20ac\n\
2. 2.\xba: 4 245 \xd7 0,157 = 666,465 \u20ac\n\
3. 3.\xba: 5 251 \xd7 0,212 = 1 113,212 \u20ac\n\
4. 4.\xba: 5 251 \xd7 0,241 = 1 265,491 \u20ac\n\
5. 5.\xba: (25 000 - 23 089) \xd7 0,311 = 594,321 \u20ac\n\
6. Coleta \u2248 4 682,24 \u20ac; taxa m\xe9dia \u2248 18,7%.\n\
Resultado: cerca de 4 682,24 \u20ac de IRS, com taxa marginal de 31,1%.\n\
Interpreta\xe7\xe3o: a taxa m\xe9dia \xe9 muito menor do que a marginal.\n\
Erros a evitar: calcular 25 000 \xd7 0,311.\n\
@E 3|m1e3|Quatro m\xe9todos, tr\xeas vencedores|c_matc.vot|m1c\n\
Enunciado: 100 votantes: 40 preferem A, B, C; 35 preferem C, B, A; 25 preferem B, C, A. Quem ganha por\
 maioria simples, segunda volta, Borda e Condorcet?\n\
Resolu\xe7\xe3o:\n\
1. Maioria simples: A, com 40 votos (sem maioria absoluta).\n\
2. 2.\xaa volta, A contra C: A 40 e C 35 + 25 = 60. Ganha C.\n\
3. Borda: A 180, B 225 e C 195 pontos. Ganha B.\n\
4. Condorcet: B vence A por 60 a 40 e C por 65 a 35.\n\
Resultado: A (maioria simples), C (2.\xaa volta), B (Borda e Condorcet).\n\
Interpreta\xe7\xe3o: o vencedor depende do m\xe9todo escolhido.\n\
Erros a evitar: decidir s\xf3 pelo 1.\xba lugar.\n\
"
