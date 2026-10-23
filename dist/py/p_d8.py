# p_d8.py - M1TR4M: Dados (8.\xba ano) (gerado pelo build).
D = "@V 1\n\
@N 2\n\
@T Dados (8.\xba ano)\n\
@L d8a|Quartis e diagrama de extremos e quartis|quartis primeiro quartil terceiro quartil mediana amplitude\
 interquartil diagrama de extremos e quartis caixa com bigodes outliers|c_mate.uni|8|n\xfacleo|||AE\
 Matem\xe1tica 8.\xba ano, Dados (quartis)\n\
@A\n\
- Calcular os quartis de um conjunto de dados.\n\
- Construir e ler um diagrama de extremos e quartis.\n\
- Calcular a amplitude interquartil.\n\
@C\n\
- Ordena os dados; a mediana divide-os em duas metades.\n\
- Q1: mediana da metade de baixo; Q3: mediana da metade de cima.\n\
- Com n \xedmpar, a mediana n\xe3o entra em nenhuma metade.\n\
- Diagrama: m\xednimo, Q1, mediana, Q3 e m\xe1ximo.\n\
- Amplitude interquartil: AIQ = Q3 - Q1 (onde est\xe3o os 50% centrais).\n\
@F Amplitude interquartil|AIQ = Q3 - Q1|Q1, Q3: 1.\xba e 3.\xba quartis|mede a dispers\xe3o dos 50%\
 centrais|Q1 = 6, Q3 = 10: AIQ = 4|c_mate.uni\n\
@F\n\
Dados: 3, 5, 6, 6, 7, 8, 9, 10, 12, 20 (j\xe1 ordenados).\n\
Objetivo: os cinco n\xfameros do diagrama e a AIQ.\n\
1. n = 10 \xe9 par: mediana = (7 + 8) / 2 = 7,5.\n\
2. Metade de baixo: 3, 5, 6, 6, 7, logo Q1 = 6.\n\
3. Metade de cima: 8, 9, 10, 12, 20, logo Q3 = 10.\n\
4. AIQ = 10 - 6 = 4\n\
> M\xednimo 3; Q1 = 6; mediana 7,5; Q3 = 10; m\xe1ximo 20.\n\
Verifica\xe7\xe3o: 20 est\xe1 muito acima de Q3 + 1,5 \xd7 AIQ = 16: \xe9 um valor at\xedpico.\n\
@J\n\
Num diagrama, Q1 = 12 e Q3 = 20. Que percentagem dos dados est\xe1 entre 12 e 20?\n\
@R\n\
Cerca de 50% (os dados entre Q1 e Q3).\n\
@L d8b|Dados em classes e histograma|classes amplitude da classe histograma ponto medio classe modal\
 frequencia acumulada tabela de frequencias agrupadas dados continuos|c_mate.cls|8|n\xfacleo|||AE\
 Matem\xe1tica 8.\xba ano, Dados (classes e histogramas)\n\
@A\n\
- Agrupar dados em classes.\n\
- Construir e ler um histograma.\n\
- Calcular a m\xe9dia aproximada com os pontos m\xe9dios.\n\
@C\n\
- Classes [a, b[: o limite de baixo entra, o de cima n\xe3o.\n\
- Histograma: ret\xe2ngulos juntos; a altura \xe9 a frequ\xeancia.\n\
- Classe modal: a de maior frequ\xeancia.\n\
- Ponto m\xe9dio de [a, b[: (a + b) / 2.\n\
- M\xe9dia aproximada: \u03a3(ponto m\xe9dio \xd7 frequ\xeancia) / n.\n\
@F M\xe9dia de dados agrupados|x\u0304 \u2248 \u03a3(x\u1d62 \xd7 n\u1d62) / n|x\u1d62: ponto m\xe9dio da\
 classe;n\u1d62: frequ\xeancia|valor aproximado|[0, 10[ com 3 e [10, 20[ com 7: x\u0304 \u2248 12|c_mate.cls\n\
@F\n\
Dados: alturas (cm) de 20 alunos: [150, 155[ 3; [155, 160[ 7; [160, 165[ 6; [165, 170[ 4.\n\
Objetivo: classe modal e m\xe9dia aproximada.\n\
1. Classe modal: [155, 160[ (7 alunos).\n\
2. Pontos m\xe9dios: 152,5; 157,5; 162,5; 167,5.\n\
3. \u03a3 = 152,5 \xd7 3 + 157,5 \xd7 7 + 162,5 \xd7 6 + 167,5 \xd7 4 = 3205.\n\
4. M\xe9dia \u2248 3205 / 20 = 160,25 cm.\n\
> Classe modal [155, 160[; m\xe9dia \u2248 160,25 cm.\n\
Verifica\xe7\xe3o: 3 + 7 + 6 + 4 = 20 alunos \u2713.\n\
@J\n\
Qual \xe9 o ponto m\xe9dio da classe [40, 50[?\n\
@R\n\
(40 + 50) / 2 = 45.\n\
@E 1|d8e1|Quartis com n \xedmpar|c_mate.uni|d8a\n\
Enunciado: tempos (min) de 9 alunos a ir para a escola: 9, 11, 12, 13, 14, 15, 16, 18, 20. Calcula Q1, a mediana e Q3.\n\
Resolu\xe7\xe3o:\n\
1. Mediana: o 5.\xba dado, 14.\n\
2. Metade de baixo: 9, 11, 12, 13, logo Q1 = (11 + 12) / 2 = 11,5.\n\
3. Metade de cima: 15, 16, 18, 20, logo Q3 = (16 + 18) / 2 = 17.\n\
Resultado: Q1 = 11,5; mediana 14; Q3 = 17.\n\
Interpreta\xe7\xe3o: metade dos alunos demora entre 11,5 e 17 minutos.\n\
Erros a evitar: p\xf4r a mediana dentro das metades quando n \xe9 \xedmpar.\n\
@E 2|d8e2|Comparar duas turmas|c_mate.uni|d8a\n\
Enunciado: no teste, a turma A tem mediana 14 e AIQ 3; a turma B tem mediana 14 e AIQ 7. O que se conclui?\n\
Resolu\xe7\xe3o:\n\
1. As medianas s\xe3o iguais: o centro das notas \xe9 o mesmo.\n\
2. A AIQ da turma B \xe9 maior: 7 - 3 = 4 valores a mais.\n\
3. As notas centrais da turma A est\xe3o mais concentradas.\n\
Resultado: a turma A \xe9 mais homog\xe9nea.\n\
Interpreta\xe7\xe3o: a AIQ mede a dispers\xe3o; a mediana mede o centro.\n\
Erros a evitar: concluir que as turmas s\xe3o iguais s\xf3 pelas medianas.\n\
@E 3|d8e3|Tempo de estudo agrupado|c_mate.cls|d8b\n\
Enunciado: tempo de estudo semanal (h) de 25 alunos: [0, 2[ 4; [2, 4[ 9; [4, 6[ 8; [6, 8[ 4. Calcula a\
 m\xe9dia aproximada e a percentagem que estuda pelo menos 4 h.\n\
Resolu\xe7\xe3o:\n\
1. Pontos m\xe9dios: 1, 3, 5 e 7.\n\
2. M\xe9dia \u2248 (1 \xd7 4 + 3 \xd7 9 + 5 \xd7 8 + 7 \xd7 4) / 25 = 3,96 h.\n\
3. Pelo menos 4 h: 8 + 4 = 12 alunos, ou seja, 12 / 25 = 48%.\n\
Resultado: m\xe9dia \u2248 3,96 h; 48% estudam pelo menos 4 h.\n\
Interpreta\xe7\xe3o: a m\xe9dia \xe9 aproximada porque n\xe3o se sabem os dados exatos.\n\
Erros a evitar: usar os limites das classes em vez dos pontos m\xe9dios.\n\
"
