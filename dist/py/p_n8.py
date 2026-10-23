# p_n8.py - M1TR4M: N\xfameros (8.\xba ano) (gerado pelo build).
D = "@V 1\n\
@N 3\n\
@T N\xfameros (8.\xba ano)\n\
@L n8a|Pot\xeancias de expoente inteiro|potencia expoente negativo expoente zero inverso regras das potencias\
 fracoes potencias de 10|c_mnum.pot|8|n\xfacleo|||AE Matem\xe1tica 8.\xba ano, Pot\xeancias de expoente inteiro\n\
@A\n\
- Calcular pot\xeancias com expoente negativo ou nulo.\n\
- Aplicar as regras das pot\xeancias com expoentes inteiros.\n\
- Escrever um n\xfamero como pot\xeancia de base 10.\n\
@C\n\
- a\u2070 = 1 (a \u2260 0).\n\
- Expoente negativo: a\u207b\u207f = 1 / a^n; por exemplo, 2\u207b\xb3 = 1/8.\n\
- (a/b)\u207b\u207f = (b/a)^n: inverte-se a base e o sinal do expoente.\n\
- As regras das pot\xeancias valem para expoentes inteiros.\n\
- 10\u207b\xb3 = 0,001; 10\u207b\xb9 = 0,1.\n\
@F Expoente negativo|a\u207b\u207f = 1 / a^n|a \u2260 0;n: inteiro positivo|a base n\xe3o pode ser\
 0|5\u207b\xb2 = 1/25|c_mnum.pot\n\
@F Base fracion\xe1ria com expoente negativo|(a/b)\u207b\u207f = (b/a)^n|a e b diferentes de 0|inverte-se a\
 base|(2/3)\u207b\xb2 = 9/4|c_mnum.pot\n\
@F\n\
Dados: 2\u207b\xb3 \xd7 2\u2075 e (2/3)\u207b\xb2 \xd7 (3/2)\xb3.\n\
Objetivo: calcular as duas express\xf5es.\n\
1. Mesma base: 2\u207b\xb3 \xd7 2\u2075 = 2\u207b\xb3\u207a\u2075 = 2\xb2 = 4\n\
2. (2/3)\u207b\xb2 = (3/2)\xb2 = 9/4\n\
3. Mesma base 3/2: (3/2)\xb2 \xd7 (3/2)\xb3 = (3/2)\u2075 = 243/32\n\
> 4 e 243/32 (\u2248 7,59).\n\
Verifica\xe7\xe3o: 0,125 \xd7 32 = 4 \u2713.\n\
@J\n\
Escreve 0,0001 como pot\xeancia de base 10.\n\
@R\n\
1 / 10 000 = 1/10000, ou seja, 10\u207b\u2074.\n\
@L n8b|Nota\xe7\xe3o cient\xedfica|notacao cientifica mantissa ordem de grandeza potencia de 10 multiplicar\
 dividir somar numeros muito grandes muito pequenos|c_mrea.ncie|8|n\xfacleo||q1b:Tamanho dos \xe1tomos:\
 ordens de grandeza e escalas|AE Matem\xe1tica 8.\xba ano, Nota\xe7\xe3o cient\xedfica\n\
@A\n\
- Escrever n\xfameros em nota\xe7\xe3o cient\xedfica.\n\
- Multiplicar e dividir n\xfameros em nota\xe7\xe3o cient\xedfica.\n\
- Somar e subtrair, igualando as pot\xeancias de 10.\n\
@C\n\
- Nota\xe7\xe3o cient\xedfica: a \xd7 10^n, com 1 \u2264 a < 10 e n inteiro.\n\
- V\xedrgula para a esquerda: o expoente aumenta; para a direita, diminui.\n\
- Multiplicar: multiplicam-se os n\xfameros e somam-se os expoentes.\n\
- Dividir: dividem-se os n\xfameros e subtraem-se os expoentes.\n\
- Somar: primeiro a mesma pot\xeancia de 10.\n\
- No fim, acerta a para ficar entre 1 e 10.\n\
@F Nota\xe7\xe3o cient\xedfica|a \xd7 10^n|1 \u2264 a < 10;n: inteiro|n\xfameros positivos (com sinal, -a\
 \xd7 10^n)|0,00052 = 5,2 \xd7 10\u207b\u2074|c_mrea.ncie\n\
@F Produto em nota\xe7\xe3o cient\xedfica|(a \xd7 10^n)(b \xd7 10^m) = (a b) \xd7 10^(n + m)|a, b:\
 mantissas|acertar a mantissa no fim|(3 \xd7 10\u2075)(4 \xd7 10\u207b\xb2) = 1,2 \xd7 10\u2074|c_mrea.ncie\n\
@F\n\
Dados: A = 3 \xd7 10\u2075 e B = 4 \xd7 10\u207b\xb2.\n\
Objetivo: A \xd7 B e A : B em nota\xe7\xe3o cient\xedfica.\n\
1. A \xd7 B = (3 \xd7 4) \xd7 10\u2075\u207b\xb2 = 12 \xd7 10\xb3 = 1,2 \xd7 10\u2074\n\
2. A : B = (3 : 4) \xd7 10\u2075\u207a\xb2 = 0,75 \xd7 10\u2077 = 7,5 \xd7 10\u2076\n\
> A \xd7 B = 1,2 \xd7 10\u2074 e A : B = 7,5 \xd7 10\u2076.\n\
Verifica\xe7\xe3o: 300 000 \xd7 0,04 = 12 000 \u2713.\n\
@J\n\
Escreve 0,000 038 em nota\xe7\xe3o cient\xedfica.\n\
@R\n\
3,8 \xd7 10\u207b\u2075 (vale 0,000038).\n\
@L n8c|D\xedzimas finitas e infinitas peri\xf3dicas|dizima finita dizima infinita periodica periodo fracao\
 geratriz converter fracao em dizima denominador 2 e 5|c_mnum.dec|8|n\xfacleo|||AE Matem\xe1tica 8.\xba ano,\
 N\xfameros racionais (d\xedzimas)\n\
@A\n\
- Saber se uma fra\xe7\xe3o d\xe1 d\xedzima finita ou peri\xf3dica.\n\
- Escrever uma d\xedzima peri\xf3dica com per\xedodo.\n\
- Encontrar a fra\xe7\xe3o geratriz de uma d\xedzima peri\xf3dica.\n\
@C\n\
- Fra\xe7\xe3o irredut\xedvel com denominador s\xf3 com fatores 2 e 5: d\xedzima finita.\n\
- Outros fatores no denominador: d\xedzima infinita peri\xf3dica.\n\
- 1/3 d\xe1 0,333..., que se escreve 0,(3); o per\xedodo \xe9 3.\n\
- Fra\xe7\xe3o geratriz: multiplica d por pot\xeancias de 10 e subtrai para o per\xedodo desaparecer.\n\
- Todas as d\xedzimas finitas e peri\xf3dicas s\xe3o n\xfameros racionais.\n\
@F Fra\xe7\xe3o geratriz (per\xedodo de k algarismos)|10^k d - d = parte inteira (sem d\xedzima infinita)|d:\
 d\xedzima peri\xf3dica pura|com anteper\xedodo, multiplica primeiro por 10|0,(36): 99d = 36, d = 4/11|c_mnum.dec\n\
@F\n\
Dados: d = 0,(36) e a fra\xe7\xe3o 7/12.\n\
Objetivo: fra\xe7\xe3o de d e d\xedzima de 7/12.\n\
1. 100d = 36,(36); 100d - d = 36, logo 99d = 36.\n\
2. d = 36/99 = 4/11\n\
3. 7/12: 12 = 2\xb2 \xd7 3 tem o fator 3, logo \xe9 peri\xf3dica.\n\
4. 7 : 12 = 0,58333... = 0,58(3) \u2248 0,583.\n\
> 0,(36) = 4/11 e 7/12 = 0,58(3).\n\
Verifica\xe7\xe3o: 4 : 11 = 0,3636... \u2248 0,364 \u2713.\n\
@J\n\
A fra\xe7\xe3o 9/40 d\xe1 uma d\xedzima finita ou peri\xf3dica?\n\
@R\n\
Finita: 40 = 2\xb3 \xd7 5 (9/40 = 0,225).\n\
@E 1|n8e1|Massa de um \xe1tomo|c_mrea.ncie|n8b\n\
Enunciado: um \xe1tomo de hidrog\xe9nio tem massa 1,67 \xd7 10\u207b\xb2\u2077 kg. Qual \xe9 a massa de 3\
 \xd7 10\xb2\u2070 \xe1tomos?\n\
Resolu\xe7\xe3o:\n\
1. Multiplica as mantissas: 1,67 \xd7 3 = 5,01.\n\
2. Soma os expoentes: -27 + 20 = -7.\n\
3. Massa: 5,01 \xd7 10\u207b\u2077 kg.\n\
Resultado: cerca de 5,01 \xd7 10\u207b\u2077 kg (0,5 mg).\n\
Interpreta\xe7\xe3o: mesmo muit\xedssimos \xe1tomos t\xeam uma massa min\xfascula.\n\
Erros a evitar: multiplicar os expoentes em vez de os somar.\n\
@E 2|n8e2|Soma em nota\xe7\xe3o cient\xedfica|c_mrea.ncie|n8b\n\
Enunciado: calcula 2,5 \xd7 10\u2074 + 3 \xd7 10\xb3 e escreve o resultado em nota\xe7\xe3o cient\xedfica.\n\
Resolu\xe7\xe3o:\n\
1. A mesma pot\xeancia de 10: 3 \xd7 10\xb3 escreve-se 0,3 \xd7 10\u2074.\n\
2. Soma: (2,5 + 0,3) \xd7 10\u2074 = 2,8 \xd7 10\u2074.\n\
Resultado: 2,8 \xd7 10\u2074.\n\
Interpreta\xe7\xe3o: 25 000 + 3000 = 28 000 \u2713.\n\
Erros a evitar: somar os expoentes, como na multiplica\xe7\xe3o.\n\
@E 3|n8e3|Fra\xe7\xe3o de uma d\xedzima com anteper\xedodo|c_mnum.dec|n8c\n\
Enunciado: escreve d = 1,2(5) como fra\xe7\xe3o irredut\xedvel.\n\
Resolu\xe7\xe3o:\n\
1. 10d = 12,(5) e 100d = 125,(5).\n\
2. Subtraindo: 100d - 10d = 125 - 12, ou seja, 90d = 113.\n\
3. d = 113/90\n\
Resultado: 1,2(5) = 113/90.\n\
Interpreta\xe7\xe3o: 113 : 90 = 1,2555... \u2713.\n\
Erros a evitar: tratar o 2 como parte do per\xedodo.\n\
"
