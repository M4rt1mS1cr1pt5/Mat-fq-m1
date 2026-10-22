# m1_idxm.py - M1TR4M: indice da pesquisa (Mat, parte 1 de 1) gerado pelo build.
# Cada linha: etiqueta|titulo|palavras|alvo
D = "@V 1\n\
@N 365\n\
L|Elei\xe7\xf5es: maioria simples e maioria absoluta|eleicao votacao tabela preferencias relativa votantes empate|m1a\n\
L|M\xe9todo de Borda|pontos ordenacao preferencias pontuacao ranking eleicao concurso|m1b\n\
L|Segunda volta e elimina\xe7\xe3o sucessiva|dois mais votados transferencia votos analise sistemas|m1c\n\
L|M\xe9todo de Condorcet (aprofundamento)|duelos dois vencedor paradoxo ciclo preferencias teorema|m1d\n\
L|M\xe9todo de Hondt|mandatos deputados divisores quocientes circulo eleitoral assembleia|m1e\n\
L|M\xe9todo de Sainte-Lagu\xeb e compara\xe7\xe3o com Hondt|divisores impares proporcionalidade partidos\
 pequenos percentagem mandatos|m1f\n\
L|Sal\xe1rio: bruto, l\xedquido e valor por hora|salario bruto seguranca social 11% entidade empregadora|m1g\n\
L|IRS: escal\xf5es e progressividade|irs imposto taxa marginal media rendimento coletavel eficiencia|m1h\n\
L|Juro simples e juro composto|capital taxa capitalizacao mensal trimestral deposito prazo juros|m1i\n\
L|Presta\xe7\xf5es constantes e valor atual (aprofundamento)|prestacao constante emprestimo credito\
 amortizacao plano pagamentos|m1j\n\
F|Maioria absoluta||m1:0\n\
F|Percentagem de votos||m1:1\n\
F|Pontos de Borda||m1:2\n\
F|Total de pontos||m1:3\n\
F|Segunda volta||m1:4\n\
F|Elimina\xe7\xe3o sucessiva||m1:5\n\
F|Duelo de Condorcet||m1:6\n\
F|N\xfamero de duelos||m1:7\n\
F|Quociente de Hondt|mandatos|m1:8\n\
F|Empate (Lei n.\xba 14/79, art. 16.\xba)||m1:9\n\
F|Quociente de Sainte-Lagu\xeb||m1:10\n\
F|Percentagem de mandatos|hondt|m1:11\n\
F|Sal\xe1rio l\xedquido||m1:12\n\
F|Valor da hora||m1:13\n\
F|Coleta por escal\xf5es||m1:14\n\
F|Taxa m\xe9dia||m1:15\n\
F|Juro simples|juros|m1:16\n\
F|Juro composto|juros|m1:17\n\
F|Presta\xe7\xe3o constante||m1:18\n\
F|Valor atual||m1:19\n\
E|Hondt com empate no \xfaltimo mandato|mandatos|m1:0\n\
E|IRS de 25 000 \u20ac por escal\xf5es||m1:1\n\
E|Quatro m\xe9todos, tr\xeas vencedores||m1:2\n\
X|Numa vota\xe7\xe3o com 37 votos||m1:0\n\
X|Um candidato tem mais votos||m1:1\n\
X|Com 4 candidatos, quantos||m1:2\n\
X|Com os mesmos votos, a||m1:3\n\
X|Quantos duelos de Condorcet||m1:4\n\
X|Pelo m\xe9todo de Hondt, com 3||m1:5\n\
X|Num empate no \xfaltimo mandato||m1:6\n\
X|Quais s\xe3o os divisores do||m1:7\n\
X|Qual \xe9 o desconto para a||m1:8\n\
X|Com a tabela de IRS de 2026||m1:9\n\
X|O que \xe9 a taxa marginal de||m1:10\n\
X|Qual \xe9 o juro, em euros, de 2|energia mecanica|m1:11\n\
X|Quanto vale, em euros, um|energia mecanica|m1:12\n\
L|O problema estat\xedstico: popula\xe7\xe3o, amostra e vari\xe1veis|estatistico variabilidade populacao\
 censo unidade estatistica variavel|m2a\n\
L|Tabelas de frequ\xeancias, gr\xe1ficos e caule-e-folhas|frequencia absoluta relativa acumulada tabela\
 frequencias grafico|m2b\n\
L|Dados agrupados em classes e histograma|amplitude classe ponto medio modal mediana continuos energia mecanica|m2c\n\
L|M\xe9dia, mediana e moda|medidas localizacao media ordenar dados valor central|m2d\n\
L|Quartis, percentis e diagrama de extremos e quartis|q1 q3 caixa bigodes amplitude interquartil outliers aiq|m2e\n\
L|Medidas de dispers\xe3o: amplitude, vari\xe2ncia e desvio padr\xe3o|dispersao amplitude interquartil\
 desvios amostral n - aiq dp|m2f\n\
L|Transforma\xe7\xf5es lineares e efeito dos outliers|transformacao linear y = ax + b|m2g\n\
L|Dados bivariados: correla\xe7\xe3o e reta dos m\xednimos quadrados|bivariados diagrama dispersao nuvem\
 pontos coeficiente linear pmq reta de regressao|m2h\n\
L|Projeto de Estat\xedstica|trabalho pergunta questionario recolha dados relatorio conclusoes|m2i\n\
F|Amostra estratificada||m2:0\n\
F|Percentagem da amostra||m2:1\n\
F|Frequ\xeancia relativa||m2:2\n\
F|Frequ\xeancia acumulada||m2:3\n\
F|Ponto m\xe9dio de uma classe||m2:4\n\
F|M\xe9dia de dados agrupados||m2:5\n\
F|M\xe9dia||m2:6\n\
F|Mediana||m2:7\n\
F|Amplitude interquartil|aiq|m2:8\n\
F|Barreiras dos outliers||m2:9\n\
F|Vari\xe2ncia amostral||m2:10\n\
F|Desvio padr\xe3o amostral|dp|m2:11\n\
F|M\xe9dia de y = a x + b||m2:12\n\
F|Desvio padr\xe3o de y = a x + b|dp|m2:13\n\
F|Reta dos m\xednimos quadrados|pmq reta de regressao|m2:14\n\
F|Coeficiente de correla\xe7\xe3o linear||m2:15\n\
F|Tamanho relativo da amostra||m2:16\n\
F|M\xe9dia||m2:17\n\
E|M\xe9dia, mediana e moda de notas||m2:0\n\
E|Quartis e outliers com n \xedmpar||m2:1\n\
E|Reta de regress\xe3o e previs\xe3o|minimos quadrados|m2:2\n\
X|Qual \xe9 a m\xe9dia de 4, 7, 7 e||m2:0\n\
X|Qual \xe9 a mediana de 5, 1, 9||m2:1\n\
X|Qual destas vari\xe1veis \xe9||m2:2\n\
X|Dados: 2, 3, 5, 6, 8, 9, 12 e||m2:3\n\
X|Com Q1 = 20 e Q3 = 30, acima||m2:4\n\
X|Qual \xe9 a amplitude de 3, 9||m2:5\n\
X|Qual \xe9 a vari\xe2ncia amostral||m2:6\n\
X|Se somarmos 5 a todos os||m2:7\n\
X|A m\xe9dia das temperaturas \xe9 10||m2:8\n\
X|Um coeficiente de correla\xe7\xe3o||m2:9\n\
X|Uma correla\xe7\xe3o forte entre x||m2:10\n\
X|Classes [0, 10[, [10, 20[ e||m2:11\n\
X|Em 50 respostas, 12 foram|energia mecanica|m2:12\n\
L|Revis\xf5es de tri\xe2ngulos; mediatriz e bissetriz|classificacao triangulos congruencia semelhanca\
 criterio aa pitagoras|m3a\n\
L|Incentro e circunfer\xeancia inscrita|bissetrizes tangente raio r = 2a/p triangulo tg|m3b\n\
L|Circuncentro e ortocentro|mediatrizes circunferencia circunscrita raio r alturas triangulo|m3c\n\
L|Medianas e baricentro|mediana centro massa centroide dois tercos seis|m3d\n\
L|Pontos not\xe1veis, reta de Euler e circunfer\xeancia dos nove pontos|localizacao notaveis ob = 2bc oc 3bc|m3e\n\
L|Pontos de Fermat e de Nagel (aprofundamento)|ponto torricelli soma minima distancias 120 graus|m3f\n\
F|Teorema de Pit\xe1goras||m3:0\n\
F|Soma dos \xe2ngulos internos||m3:1\n\
F|\xc1rea do tri\xe2ngulo||m3:2\n\
F|Raio da circunfer\xeancia inscrita||m3:3\n\
F|Inscrita no tri\xe2ngulo ret\xe2ngulo||m3:4\n\
F|\xc2ngulo com v\xe9rtice no incentro||m3:5\n\
F|Circunscrita no tri\xe2ngulo ret\xe2ngulo||m3:6\n\
F|Propriedade dos 2/3||m3:7\n\
F|\xc1reas definidas pelas medianas||m3:8\n\
F|Baricentro em coordenadas|energia mecanica|m3:9\n\
F|Reta de Euler||m3:10\n\
F|Circunfer\xeancia dos nove pontos||m3:11\n\
F|Ponto de Nagel||m3:12\n\
E|Raio da circunfer\xeancia inscrita||m3:0\n\
E|\xc2ngulos com v\xe9rtice no incentro||m3:1\n\
E|Pontos not\xe1veis em coordenadas e reta de Euler|energia mecanica|m3:2\n\
X|Um tri\xe2ngulo tem 30 cm\xb2 de||m3:0\n\
X|Qual ponto not\xe1vel \xe9 o centro||m3:1\n\
X|Uma mediana mede 12 cm. A que||m3:2\n\
X|O incentro pode ficar fora do||m3:3\n\
X|Um tri\xe2ngulo ret\xe2ngulo tem||m3:4\n\
X|Num tri\xe2ngulo obtus\xe2ngulo||m3:5\n\
X|Na reta de Euler de um|avogadro|m3:6\n\
X|A circunfer\xeancia circunscrita||m3:7\n\
X|No tri\xe2ngulo [ABC], de||m3:8\n\
X|Um tri\xe2ngulo tem 42 cm\xb2 de||m3:9\n\
X|Num tri\xe2ngulo is\xf3sceles n\xe3o||m3:10\n\
L|Conceito de fun\xe7\xe3o e formas de a representar|dominio conjunto chegada contradominio objeto imagem variavel|m4a\n\
L|Estudo de uma fun\xe7\xe3o: zeros, sinal, monotonia e extremos|zeros sinal crescente decrescente maximo\
 minimo absoluto|m4b\n\
L|Fun\xe7\xe3o afim|linear declive ordenada origem zero sinal monotonia|m4c\n\
L|Condi\xe7\xf5es, conjun\xe7\xe3o, disjun\xe7\xe3o e intervalos|logica conjuntos condicao conjuncao\
 intervalo conjunto-solucao uniao|m4d\n\
F|Fun\xe7\xe3o||m4:0\n\
F|Contradom\xednio||m4:1\n\
F|Zeros||m4:2\n\
F|Interse\xe7\xe3o de gr\xe1ficos||m4:3\n\
F|Fun\xe7\xe3o afim||m4:4\n\
F|Declive||m4:5\n\
F|Zero da fun\xe7\xe3o afim||m4:6\n\
F|Conjun\xe7\xe3o||m4:7\n\
F|Disjun\xe7\xe3o||m4:8\n\
E|Imagens e contradom\xednio||m4:0\n\
E|Fun\xe7\xe3o afim a partir de dois pontos||m4:1\n\
E|Interse\xe7\xe3o de uma par\xe1bola com uma reta||m4:2\n\
X|Qual destas correspond\xeancias||m4:0\n\
X|Sendo f(x) = 3x - 2, quanto||m4:1\n\
X|f(x) = x\xb2, com Df = {-2, -1||m4:2\n\
X|Qual \xe9 o declive da reta que||m4:3\n\
X|Qual \xe9 o zero de f(x) = 4x -||m4:4\n\
X|Se o declive de uma fun\xe7\xe3o||m4:5\n\
X|Qual \xe9 o conjunto-solu\xe7\xe3o de||m4:6\n\
X|Quantos n\xfameros inteiros||m4:7\n\
X|Qual \xe9 o zero positivo de||m4:8\n\
X|O contradom\xednio de uma fun\xe7\xe3o||m4:9\n\
L|A fun\xe7\xe3o quadr\xe1tica e o seu gr\xe1fico|parabola concavidade vertice eixo simetria forma canonica|m5a\n\
L|Zeros e f\xf3rmula resolvente|equacao 2.o grau discriminante delta binomio fatorizacao|m5b\n\
L|Sinal, monotonia, extremos e inequa\xe7\xf5es|sinal monotonia crescente decrescente maximo minimo extremo|m5c\n\
L|Transforma\xe7\xf5es de gr\xe1ficos de fun\xe7\xf5es|translacao dilatacao contracao reflexao f(x-a) f(x)+b c|m5d\n\
F|Forma can\xf3nica||m5:0\n\
F|Abcissa do v\xe9rtice||m5:1\n\
F|Ordenada do v\xe9rtice||m5:2\n\
F|Discriminante||m5:3\n\
F|F\xf3rmula resolvente||m5:4\n\
F|Fatoriza\xe7\xe3o||m5:5\n\
F|Sinal com dois zeros (a > 0)||m5:6\n\
F|Contradom\xednio||m5:7\n\
F|Transla\xe7\xe3o vertical||m5:8\n\
F|Transla\xe7\xe3o horizontal||m5:9\n\
F|Dilata\xe7\xe3o ou contra\xe7\xe3o vertical||m5:10\n\
E|V\xe9rtice e eixo de uma par\xe1bola||m5:0\n\
E|Equa\xe7\xe3o do 2.\xba grau com fra\xe7\xe3o||m5:1\n\
E|Altura m\xe1xima de um lan\xe7amento||m5:2\n\
X|Qual \xe9 o v\xe9rtice da par\xe1bola||m5:0\n\
X|Calcula o discriminante de x\xb2||m5:1\n\
X|Quantos zeros tem f(x) = 3x\xb2||m5:2\n\
X|Qual \xe9 o zero positivo de||m5:3\n\
X|Se a < 0, a par\xe1bola de f(x)||m5:4\n\
X|Qual \xe9 o conjunto-solu\xe7\xe3o de||m5:5\n\
X|Qual \xe9 o valor m\xe1ximo de f(x)||m5:6\n\
X|O gr\xe1fico de g(x) = f(x - 3)||m5:7\n\
X|Determina o zero positivo de||m5:8\n\
X|O eixo de simetria do gr\xe1fico||m5:9\n\
L|Fun\xe7\xf5es definidas por ramos|funcao definida ramo fronteira intervalo imagem grafico|m6a\n\
L|Fun\xe7\xe3o m\xf3dulo|valor absoluto distancia vertice ramos equacao inequacao|m6b\n\
L|Ch\xe3o, teto, sinal e Heaviside (aprofundamento)|parte inteira chao teto funcao escada arredondamento|m6c\n\
F|Fun\xe7\xe3o definida por ramos||m6:0\n\
F|M\xf3dulo||m6:1\n\
F|Fun\xe7\xe3o m\xf3dulo||m6:2\n\
F|Equa\xe7\xe3o com m\xf3dulo||m6:3\n\
F|Ch\xe3o (parte inteira)||m6:4\n\
F|Teto||m6:5\n\
E|Imagens numa fun\xe7\xe3o por ramos||m6:0\n\
E|Equa\xe7\xe3o com m\xf3dulo||m6:1\n\
E|Tarif\xe1rio da \xe1gua por escal\xf5es||m6:2\n\
X|f(x) = 2x se x < 0 e f(x) = x||m6:0\n\
X|f(x) = 2x se x < 0 e f(x) = x||m6:1\n\
X|Quanto vale |-7| + |3|?||m6:2\n\
X|Qual \xe9 o v\xe9rtice do gr\xe1fico||m6:3\n\
X|Qual \xe9 a solu\xe7\xe3o positiva de||m6:4\n\
X|A fun\xe7\xe3o f(x) = -|x| tem||m6:5\n\
X|Qual \xe9 o conjunto-solu\xe7\xe3o de||m6:6\n\
X|Quanto vale teto(4,2)?||m6:7\n\
L|Referenciais: quadrantes, octantes, planos e simetrias|referencial cartesiano quadrantes octantes\
 coordenados paralelos retas|m7a\n\
L|Dist\xe2ncia e ponto m\xe9dio|entre dois pontos plano espaco pitagoras diametro|m7b\n\
L|Mediatriz e plano mediador|equidistante equacao lugar geometrico perpendicular ponto medio|m7c\n\
L|Equa\xe7\xe3o reduzida da reta e semiplanos|declive ordenada origem retas paralelas vertical horizontal|m7d\n\
L|Condi\xe7\xf5es no plano com conjun\xe7\xe3o e disjun\xe7\xe3o|regiao intersecao uniao semiplano faixa\
 quadrante circulo|m7e\n\
L|Circunfer\xeancia, c\xedrculo, superf\xedcie esf\xe9rica e esfera|circunferencia circulo centro raio\
 equacao reduzida diametro|m7f\n\
F|Sim\xe9tricos no plano||m7:0\n\
F|Planos paralelos aos coordenados||m7:1\n\
F|Dist\xe2ncia entre dois pontos||m7:2\n\
F|Ponto m\xe9dio||m7:3\n\
F|Mediatriz||m7:4\n\
F|Plano mediador||m7:5\n\
F|Equa\xe7\xe3o reduzida da reta||m7:6\n\
F|Semiplanos||m7:7\n\
F|Regi\xe3o definida por \u2227||m7:8\n\
F|Regi\xe3o definida por \u2228||m7:9\n\
F|Circunfer\xeancia||m7:10\n\
F|Superf\xedcie esf\xe9rica||m7:11\n\
E|Dist\xe2ncia e ponto m\xe9dio||m7:0\n\
E|Equa\xe7\xe3o de uma mediatriz||m7:1\n\
E|Circunfer\xeancia de di\xe2metro dado e um ponto||m7:2\n\
X|Qual \xe9 a dist\xe2ncia entre A(1||m7:0\n\
X|Qual \xe9 o sim\xe9trico de P(3||m7:1\n\
X|M(2, 3) \xe9 o ponto m\xe9dio de||m7:2\n\
X|Qual \xe9 a ordenada na origem|avogadro|m7:3\n\
X|Duas retas com declives 2 e||m7:4\n\
X|Qual \xe9 o centro da||m7:5\n\
X|Qual \xe9 o raio da superf\xedcie||m7:6\n\
X|Que condi\xe7\xe3o define o 1.\xba||m7:7\n\
X|No espa\xe7o, a condi\xe7\xe3o x = 3||m7:8\n\
X|Uma esfera tem centro (2, -5||m7:9\n\
L|Vetores: dire\xe7\xe3o, sentido e norma|vetor segmento orientado direcao vetores iguais simetrico|m8a\n\
L|Opera\xe7\xf5es com vetores|soma regra triangulo paralelogramo diferenca ponto mais vetor|m8b\n\
L|Coordenadas e norma de um vetor|ab = b - posicao operacoes plano vetores|m8c\n\
L|Vetores colineares|mesma direcao v = ku coordenadas proporcionais vetor|m8d\n\
L|Equa\xe7\xe3o vetorial da reta|vetor diretor parametro ponto pertence declive m vetores|m8e\n\
L|Vetores em problemas de geometria (aprofundamento)|quarto vertice paralelogramo ponto medio baricentro\
 medianas energia mecanica vetor|m8f\n\
L|Produto escalar (extens\xe3o, 11.\xba)|angulo dois vetores perpendiculares cosseno trabalho forca cos vetor|m8g\n\
F|Vetor sim\xe9trico|vetores|m8:0\n\
F|Transla\xe7\xe3o||m8:1\n\
F|Regra do tri\xe2ngulo||m8:2\n\
F|Produto por um n\xfamero real||m8:3\n\
F|Vetor definido por dois pontos|vetores|m8:4\n\
F|Norma de um vetor|vetores|m8:5\n\
F|Vetores colineares|vetor|m8:6\n\
F|Pontos alinhados||m8:7\n\
F|Equa\xe7\xe3o vetorial da reta||m8:8\n\
F|Declive e vetor diretor|vetores|m8:9\n\
F|Quarto v\xe9rtice do paralelogramo||m8:10\n\
F|Baricentro||m8:11\n\
F|Produto escalar (11.\xba)||m8:12\n\
F|\xc2ngulo de dois vetores (11.\xba)|vetor|m8:13\n\
E|Vetor, norma e ponto m\xe9dio||m8:0\n\
E|Tr\xeas pontos alinhados||m8:1\n\
E|Da equa\xe7\xe3o vetorial \xe0 reduzida||m8:2\n\
X|Qual \xe9 a norma do vetor u =|vetores|m8:0\n\
X|Num paralelogramo [ABCD], que||m8:1\n\
X|A(2, -1) e AB = (3, 4). Qual||m8:2\n\
X|Se \u2016u\u2016 = 3 e \u2016v\u2016 = 4, ent\xe3o||m8:3\n\
X|Para que valor de a s\xe3o u =||m8:4\n\
X|Qual destes \xe9 um vetor|vetores|m8:5\n\
X|O ponto P(3, 1) pertence \xe0||m8:6\n\
X|\u2016u\u2016 = 2,5. Qual \xe9 a norma de||m8:7\n\
X|Tri\xe2ngulo de v\xe9rtices A(1||m8:8\n\
X|A(1, 0, 2) e B(3, -2, 3).||m8:9\n\
X|Qual \xe9 o produto escalar de u||m8:10\n\
L|Raz\xf5es trigonom\xe9tricas de um \xe2ngulo agudo|trigonometria seno cosseno tangente cateto oposto\
 adjacente sen cos tg|m9a\n\
L|Resolver tri\xe2ngulos ret\xe2ngulos|triangulo retangulo angulo elevacao depressao altura sombra|m9b\n\
L|Rela\xe7\xf5es entre as raz\xf5es e valores exatos|formula fundamental sen^2 + cos^2 = 1|m9c\n\
L|Radianos (extens\xe3o, 11.\xba)|radiano graus conversao pi comprimento arco angulo|m9d\n\
L|Leis dos senos e dos cossenos (extens\xe3o, 11.\xba)|lei triangulo qualquer resolver area caso ambiguo|m9e\n\
F|Seno|sen|m9:0\n\
F|Cosseno e tangente|cos tg|m9:1\n\
F|Lados a partir da hipotenusa||m9:2\n\
F|Oposto a partir do adjacente||m9:3\n\
F|F\xf3rmula fundamental||m9:4\n\
F|Tangente a partir do seno e do cosseno|sen cos tg|m9:5\n\
F|Graus em radianos|energia mecanica|m9:6\n\
F|Comprimento de arco||m9:7\n\
F|Lei dos senos||m9:8\n\
F|Lei dos cossenos||m9:9\n\
E|Altura de um pr\xe9dio||m9:0\n\
E|Das outras raz\xf5es a partir do cosseno|cos|m9:1\n\
E|O caso amb\xedguo||m9:2\n\
X|O cateto oposto a \u03b1 mede 5 e||m9:0\n\
X|Num tri\xe2ngulo ret\xe2ngulo, o||m9:1\n\
X|Uma escada de 6 m faz 60\xb0 com||m9:2\n\
X|Com a calculadora em graus|energia mecanica|m9:3\n\
X|Para qualquer \xe2ngulo agudo \u03b1||m9:4\n\
X|\u03b1 \xe9 agudo e sen \u03b1 = 0,8.|seno|m9:5\n\
X|Qual \xe9 o valor exato de cos|cosseno|m9:6\n\
X|Quantos graus tem \u03c0/6 rad?||m9:7\n\
X|Num tri\xe2ngulo, b = 5, c = 8 e||m9:8\n\
X|Com A = 90\xb0, a lei dos||m9:9\n\
L|N\xfameros: fra\xe7\xf5es, pot\xeancias e nota\xe7\xe3o cient\xedfica|fracoes operacoes regras expoente\
 negativo raiz quadrada|mra\n\
L|Percentagens, aumentos e descontos|percentagem aumento desconto iva variacao percentual fator|mrb\n\
L|Proporcionalidade direta e inversa|constante y = kx k/x hiperbole regra|mrc\n\
L|Equa\xe7\xf5es do 1.\xba grau e sistemas|equacao resolver solucao denominadores sistema duas metodo|mrd\n\
L|Intervalos e inequa\xe7\xf5es do 1.\xba grau|numeros reais inequacao conjunto-solucao inverter sinal reta|mre\n\
L|Teorema de Pit\xe1goras|hipotenusa catetos triangulo retangulo reciproco diagonal ternos|mrf\n\
L|Semelhan\xe7a de figuras|razao ampliacao reducao criterios aa lal lll|mrg\n\
L|\xc1reas e volumes|circulo perimetro prisma cilindro cone piramide esfera|mrh\n\
F|Produto de pot\xeancias com a mesma base||mr:0\n\
F|Nota\xe7\xe3o cient\xedfica||mr:1\n\
F|Aumento percentual||mr:2\n\
F|Varia\xe7\xe3o percentual||mr:3\n\
F|Proporcionalidade direta||mr:4\n\
F|Proporcionalidade inversa||mr:5\n\
F|Equa\xe7\xe3o do 1.\xba grau||mr:6\n\
F|M\xe9todo de substitui\xe7\xe3o||mr:7\n\
F|Inverter o sinal||mr:8\n\
F|Intervalo fechado||mr:9\n\
F|Teorema de Pit\xe1goras||mr:10\n\
F|Diagonal de um paralelep\xedpedo||mr:11\n\
F|Raz\xe3o de semelhan\xe7a||mr:12\n\
F|\xc1reas e volumes||mr:13\n\
F|Volume do cilindro||mr:14\n\
F|Volume da esfera||mr:15\n\
E|Desconto em percentagem|energia mecanica|mr:0\n\
E|Uma vara dentro de uma caixa||mr:1\n\
E|Um sistema num problema||mr:2\n\
X|Quanto vale 2\u207b\xb3, em forma|energia mecanica|mr:0\n\
X|Quanto \xe9 15% de 80?||mr:1\n\
X|Um pre\xe7o de 50 \u20ac sobe 20% e||mr:2\n\
X|Se x \xd7 y = 36 em todos os|energia mecanica|mr:3\n\
X|Resolve 5x + 3 = 2x - 9.||mr:4\n\
X|Qual \xe9 o conjunto-solu\xe7\xe3o de||mr:5\n\
X|Os catetos de um tri\xe2ngulo||mr:6\n\
X|Duas figuras semelhantes t\xeam||mr:7\n\
X|Qual \xe9 o volume, em m\xb3, de um|energia mecanica|mr:8\n\
C|Constantes e dados|avogadro planck velocidade luz volume molar na vm|c_comd.cte\n\
C|Dados experimentais|media incerteza absoluta relativa erro percentual|c_comd.exp\n\
C|Regress\xe3o linear e gr\xe1fico|reta declive ordenada coeficiente correlacao interpolar|c_comd.reg\n\
C|Calculadora cient\xedfica|expressao potencia raiz seno cosseno tangente sen cos tg|c_comu.sci\n\
C|Algarismos significativos|arredondar soma produto regra|c_comu.sf\n\
C|Conversor de unidades|conversao comprimento massa volume temperatura energia|c_comu.uni\n\
C|Prefixos do SI|quilo mili micro nano mega giga|c_comu.pre\n\
C|Sistemas de vota\xe7\xe3o|maioria simples relativa absoluta borda segunda|c_matc.vot\n\
C|Mandatos: Hondt e Sainte-Lagu\xeb|metodo mandatos deputados divisores quocientes partilha|c_matc.mand\n\
C|Sal\xe1rio: bruto e l\xedquido|salario mensal anual valor hora horas|c_matd.sal\n\
C|IRS por escal\xf5es|imposto taxa marginal media progressividade rendimento eficiencia|c_matd.irs\n\
C|Juros simples e compostos|juro composto capital taxa anual capitalizacao|c_matd.jur\n\
C|Presta\xe7\xf5es e valor atual|prestacao constante emprestimo credito amortizacao juros juro|c_matd.prest\n\
C|Estat\xedstica de uma vari\xe1vel|media moda mediana quartis percentil amplitude|c_mate.uni\n\
C|Dados em classes e histograma|tabela frequencias absoluta relativa acumulada ponto energia mecanica|c_mate.cls\n\
C|Caule-e-folhas|caule folhas diagrama ordenar dados comparar|c_mate.caule\n\
C|Fun\xe7\xe3o escrita por ti (tabela, zeros, gr\xe1fico)|expressao imagem tabela valores zeros sinal|c_matf.fx\n\
C|Fun\xe7\xe3o afim|declive ordenada origem zero reta dois|c_matf.afim\n\
C|Fun\xe7\xe3o definida por ramos|ramo fronteira continuidade salto zeros imagem|c_matf.ramos\n\
C|Fun\xe7\xe3o m\xf3dulo a\u2223x - h\u2223 + k|valor absoluto vertice ramos equacao inequacao|c_matf.mod\n\
C|Dist\xe2ncia e ponto m\xe9dio|entre dois pontos plano espaco coordenadas|c_matg.dist\n\
C|Equa\xe7\xe3o reduzida da reta|declive ordenada origem vertical horizontal paralela|c_matg.reta\n\
C|Mediatriz e plano mediador|equidistante equacao|c_matg.medz\n\
C|Circunfer\xeancia e superf\xedcie esf\xe9rica|circulo esfera centro raio equacao reduzida|c_matg.circ\n\
C|Condi\xe7\xf5es no plano (regi\xe3o)|condicao conjuncao disjuncao semiplano regiao desenhar|c_matg.cond\n\
C|Equa\xe7\xe3o do 2.\xba grau e fun\xe7\xe3o quadr\xe1tica|formula resolvente binomio discriminante zeros\
 vertice|c_matq.q2\n\
C|Inequa\xe7\xf5es do 2.\xba grau|inequacao conjunto-solucao intervalos sinal parabola|c_matq.iq\n\
C|Transforma\xe7\xf5es de fun\xe7\xf5es|translacao dilatacao contracao reflexao grafico f(x-a)+b|c_matq.tf\n\
C|Tri\xe2ngulo ret\xe2ngulo: seno, cosseno e tangente|trigonometria seno cateto oposto adjacente hipotenusa\
 sen cos tg|c_matr.tri\n\
C|Graus, radianos e valores exatos|graus conversao pi angulos notaveis 30|c_matr.rad\n\
C|Resolver tri\xe2ngulos: leis dos senos e dos cossenos|lei triangulo qualquer area caso ambiguo|c_matr.res\n\
C|Pontos not\xe1veis do tri\xe2ngulo (com desenho)|incentro circuncentro ortocentro baricentro reta euler|c_matt.pn\n\
C|Circunfer\xeancias inscrita e circunscrita|raio circunferencia r = 2a/p triangulo|c_matt.insc\n\
C|Reta de Euler e nove pontos|ob = 2bc circunferencia raio r/2|c_matt.euler\n\
C|Teorema de Pit\xe1goras|hipotenusa catetos triangulo retangulo|c_matt.pit\n\
C|Semelhan\xe7a de figuras|razao ampliacao reducao areas lados correspondentes|c_matt.sem\n\
C|Opera\xe7\xf5es com vetores|vetor norma soma diferenca produto numero|c_matv.vet\n\
C|Equa\xe7\xe3o vetorial da reta|vetor diretor ponto pertence declive m vetores|c_matv.retav\n\
C|Baricentro com vetores|mediana g = + 2/3 am vetor|c_matv.bar"
