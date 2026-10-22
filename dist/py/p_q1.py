# p_q1.py - M1TR4M: Massa e tamanho dos \u00e1tomos (gerado pelo build).
D = "@V 1\n\
@N 5\n\
@T Massa e tamanho dos \u00e1tomos\n\
@L q1a|Constitui\u00e7\u00e3o do \u00e1tomo e is\u00f3topos|atomo nucleo protao neutrao eletrao numero\
 atomico numero de massa isotopo iao catiao aniao|c_fqat.ar|10|n\u00facleo|||AE FQ A 10.\u00ba, Massa e\
 tamanho dos \u00e1tomos\n\
@A\n\
- Descrever o \u00e1tomo: n\u00facleo com prot\u00f5es e neutr\u00f5es, e eletr\u00f5es.\n\
- Definir n\u00famero at\u00f3mico (Z) e n\u00famero de massa (A).\n\
- Calcular o n\u00famero de neutr\u00f5es a partir de Z e de A.\n\
- Distinguir is\u00f3topos de um mesmo elemento.\n\
- Relacionar a carga de um i\u00e3o com os eletr\u00f5es ganhos ou perdidos.\n\
@B\n\
Imagina um est\u00e1dio com uma ervilha no centro. A ervilha \u00e9 o n\u00facleo, com quase toda a massa. Os\
 eletr\u00f5es ocupam o resto, quase vazio.\n\
O n\u00famero de prot\u00f5es \u00e9 o \"cart\u00e3o de cidad\u00e3o\" do elemento. Outro n\u00famero de\
 neutr\u00f5es d\u00e1 outro is\u00f3topo. Outro n\u00famero de eletr\u00f5es d\u00e1 um i\u00e3o.\n\
@C\n\
- Prot\u00e3o (carga +1) e neutr\u00e3o (sem carga) est\u00e3o no n\u00facleo.\n\
- Eletr\u00e3o: carga -1; massa 1840 vezes menor que a do prot\u00e3o.\n\
- N\u00famero at\u00f3mico, Z: n\u00famero de prot\u00f5es.\n\
- N\u00famero de massa, A: prot\u00f5es + neutr\u00f5es.\n\
- Is\u00f3topos: \u00e1tomos com o mesmo Z e diferente A.\n\
- Representa\u00e7\u00e3o: \u00b3\u2075\u2081\u2087Cl (A em cima, Z em baixo).\n\
@D\n\
O n\u00famero de neutr\u00f5es obt\u00e9m-se por N = A - Z.\n\
Num \u00e1tomo neutro h\u00e1 tantos eletr\u00f5es como prot\u00f5es.\n\
Um i\u00e3o positivo (cati\u00e3o) perdeu eletr\u00f5es.\n\
Um i\u00e3o negativo (ani\u00e3o) ganhou eletr\u00f5es.\n\
Exemplo: Na\u207a tem 11 prot\u00f5es e 10 eletr\u00f5es.\n\
Exemplo: Cl\u207b tem 17 prot\u00f5es e 18 eletr\u00f5es.\n\
Os is\u00f3topos do carbono s\u00e3o \u00b9\u00b2C, \u00b9\u00b3C e \u00b9\u2074C.\n\
T\u00eam 6, 7 e 8 neutr\u00f5es, mas todos t\u00eam 6 prot\u00f5es.\n\
T\u00eam o mesmo comportamento qu\u00edmico, porque t\u00eam os mesmos eletr\u00f5es.\n\
Diferem na massa e na estabilidade do n\u00facleo.\n\
Caso especial: o \u00b9H n\u00e3o tem neutr\u00f5es.\n\
O n\u00facleo \u00e9 cerca de 100 000 vezes menor do que o \u00e1tomo.\n\
O \u00e1tomo tem di\u00e2metro da ordem de 10\u207b\u00b9\u2070 m.\n\
@F N\u00famero de neutr\u00f5es|N = A - Z|N: n\u00famero de neutr\u00f5es;A: n\u00famero de massa;Z:\
 n\u00famero at\u00f3mico|qualquer n\u00facleo|\u00b3\u2075Cl: N = 35 - 17 = 18|\n\
@F Eletr\u00f5es de um i\u00e3o|n.\u00ba de eletr\u00f5es = Z - carga|Z: n\u00famero at\u00f3mico;carga:\
 carga do i\u00e3o, com sinal (+2, -1...)|i\u00f5es monoat\u00f3micos|Mg\u00b2\u207a: 12 - 2 = 10 eletr\u00f5es|\n\
@F\n\
Dados: i\u00e3o \u00b3\u00b2\u2081\u2086S\u00b2\u207b (enxofre).\n\
Objetivo: prot\u00f5es, neutr\u00f5es e eletr\u00f5es.\n\
1. Prot\u00f5es: Z = 16.\n\
2. Neutr\u00f5es: N = A - Z = 32 - 16 = 16.\n\
3. A carga 2- indica que ganhou 2 eletr\u00f5es.\n\
4. Eletr\u00f5es: 16 + 2 = 18.\n\
> 16 prot\u00f5es, 16 neutr\u00f5es e 18 eletr\u00f5es.\n\
Verifica\u00e7\u00e3o: carga = 16 - 18 = -2.\n\
@G\n\
Z identifica o elemento: se Z muda, muda o elemento. A carga de um i\u00e3o vem s\u00f3 dos eletr\u00f5es\
 ganhos ou perdidos.\n\
O n\u00facleo n\u00e3o muda numa rea\u00e7\u00e3o qu\u00edmica. O modelo das \"bolinhas\" \u00e9 uma\
 simplifica\u00e7\u00e3o: os eletr\u00f5es n\u00e3o t\u00eam trajet\u00f3rias definidas.\n\
@H\n\
- Confundir A com o n\u00famero de neutr\u00f5es: N = A - Z.\n\
- Achar que um cati\u00e3o ganhou eletr\u00f5es: perdeu.\n\
- Pensar que is\u00f3topos s\u00e3o elementos diferentes: t\u00eam o mesmo Z.\n\
- Esquecer que a massa est\u00e1 quase toda no n\u00facleo.\n\
- Trocar A e Z na representa\u00e7\u00e3o: A fica em cima.\n\
@I\n\
- \u00c1tomo: n\u00facleo (prot\u00f5es e neutr\u00f5es) e eletr\u00f5es.\n\
- Z = n.\u00ba de prot\u00f5es; A = prot\u00f5es + neutr\u00f5es.\n\
- N = A - Z.\n\
- Is\u00f3topos: mesmo Z, diferente A.\n\
- Cati\u00e3o perdeu eletr\u00f5es; ani\u00e3o ganhou.\n\
- O n\u00facleo \u00e9 cerca de 10\u2075 vezes menor que o \u00e1tomo.\n\
@J\n\
Quantos neutr\u00f5es e quantos eletr\u00f5es tem o i\u00e3o \u2075\u2076\u2082\u2086Fe\u00b3\u207a?\n\
@R\n\
Neutr\u00f5es: N = 56 - 26 = 30.\n\
Eletr\u00f5es: 26 - 3 = 23.\n\
@L q1b|Tamanho dos \u00e1tomos: ordens de grandeza e escalas|ordem de grandeza notacao cientifica escala\
 nanometro picometro tamanho raio atomico nanotecnologia|c_comu.uni|10|n\u00facleo|||AE FQ A 10.\u00ba, Massa\
 e tamanho dos \u00e1tomos\n\
@A\n\
- Escrever n\u00fameros em nota\u00e7\u00e3o cient\u00edfica.\n\
- Determinar a ordem de grandeza de um valor.\n\
- Comparar tamanhos dividindo ordens de grandeza.\n\
- Converter entre m, nm e pm.\n\
- Situar objetos nas escalas, do metro ao n\u00facleo.\n\
@B\n\
Os \u00e1tomos s\u00e3o muito pequenos para os n\u00fameros do dia a dia.\n\
Escrever 0,000 000 000 1 m cansa e engana.\n\
1 \u00d7 10\u207b\u00b9\u2070 m diz o mesmo de forma curta.\n\
A ordem de grandeza \u00e9 a pot\u00eancia de 10 mais pr\u00f3xima.\n\
Serve para comparar sem contas finas.\n\
@C\n\
- Nota\u00e7\u00e3o cient\u00edfica: a \u00d7 10\u207f, com 1 \u2264 a < 10 e n inteiro.\n\
- Ordem de grandeza: pot\u00eancia de 10 mais pr\u00f3xima do valor.\n\
- Regra: se a < 5, a ordem \u00e9 10\u207f; se a \u2265 5, \u00e9 10\u207f\u207a\u00b9.\n\
- Alguns livros usam 3,16 (raiz de 10) em vez de 5.\n\
- 1 nm = 10\u207b\u2079 m e 1 pm = 10\u207b\u00b9\u00b2 m.\n\
@D\n\
O raio do \u00e1tomo de hidrog\u00e9nio \u00e9 5,3 \u00d7 10\u207b\u00b9\u00b9 m.\n\
Como 5,3 \u2265 5, a ordem de grandeza \u00e9 10\u207b\u00b9\u2070 m.\n\
Um cabelo tem cerca de 8 \u00d7 10\u207b\u2075 m de largura.\n\
A sua ordem de grandeza \u00e9 10\u207b\u2074 m.\n\
Para comparar, divide-se: 10\u207b\u2074 / 10\u207b\u00b9\u2070 = 10\u2076.\n\
O cabelo \u00e9 cerca de um milh\u00e3o de vezes mais largo.\n\
Escalas de tamanho:\n\
- objetos vis\u00edveis: 10\u207b\u2074 m ou mais;\n\
- c\u00e9lulas: cerca de 10\u207b\u2075 m;\n\
- nanoescala: 1 nm a 100 nm;\n\
- \u00e1tomos: cerca de 10\u207b\u00b9\u2070 m;\n\
- n\u00facleos: 10\u207b\u00b9\u2075 m a 10\u207b\u00b9\u2074 m.\n\
A nanotecnologia usa materiais com 1 nm a 100 nm.\n\
@F Nota\u00e7\u00e3o cient\u00edfica|x = a \u00d7 10\u207f, com 1 \u2264 a < 10|a: mantissa;n: expoente\
 (inteiro)|qualquer n\u00famero diferente de 0|0,00052 = 5,2 \u00d7 10\u207b\u2074|c_comu.sci\n\
@F Ordem de grandeza|OG = 10\u207f se a < 5; OG = 10\u207f\u207a\u00b9 se a \u2265 5|a e n: da\
 nota\u00e7\u00e3o cient\u00edfica a \u00d7 10\u207f|comparar tamanhos|5,3 \u00d7 10\u207b\u00b9\u00b9 m tem\
 OG 10\u207b\u00b9\u2070 m|\n\
@F Nan\u00f3metro e pic\u00f3metro|1 nm = 10\u207b\u2079 m; 1 pm = 10\u207b\u00b9\u00b2 m|nm:\
 nan\u00f3metro;pm: pic\u00f3metro|comprimentos \u00e0 escala at\u00f3mica|154 pm = 1,54 \u00d7\
 10\u207b\u00b9\u2070 m|c_comu.uni\n\
@F\n\
Dados: um \u00e1tomo de ouro tem 0,288 nm de di\u00e2metro.\n\
Uma folha de ouro tem 1,0 \u00d7 10\u207b\u2077 m de espessura.\n\
Objetivo: quantos \u00e1tomos cabem na espessura.\n\
1. 0,288 nm = 2,88 \u00d7 10\u207b\u00b9\u2070 m.\n\
2. n = 1,0 \u00d7 10\u207b\u2077 m / 2,88 \u00d7 10\u207b\u00b9\u2070 m = 347\n\
3. Com 2 algarismos significativos: n \u2248 3,5 \u00d7 10\u00b2.\n\
4. Como 3,5 < 5, a ordem de grandeza \u00e9 10\u00b2.\n\
> Cabem cerca de 350 \u00e1tomos (ordem 10\u00b2).\n\
Verifica\u00e7\u00e3o: 350 \u00d7 2,88 \u00d7 10\u207b\u00b9\u2070 m \u2248 1,0 \u00d7 10\u207b\u2077 m.\n\
@G\n\
A ordem de grandeza d\u00e1 a escala, n\u00e3o o valor exato. Chega para comparar objetos muito diferentes.\n\
Os \u00e1tomos n\u00e3o t\u00eam uma fronteira n\u00edtida. Por isso, o raio depende do m\u00e9todo de medida\
 e as tabelas d\u00e3o valores um pouco diferentes.\n\
@H\n\
- Escrever 34 \u00d7 10\u00b3 em vez de 3,4 \u00d7 10\u2074.\n\
- Errar o sinal do expoente ao passar de pm para m.\n\
- Aplicar a regra do 5 sem passar para nota\u00e7\u00e3o cient\u00edfica.\n\
- Somar expoentes ao dividir: subtraem-se.\n\
- Confundir nm (10\u207b\u2079 m) com \u00b5m (10\u207b\u2076 m).\n\
@I\n\
- Nota\u00e7\u00e3o cient\u00edfica: a \u00d7 10\u207f, com 1 \u2264 a < 10.\n\
- Ordem de grandeza: 10\u207f se a < 5; 10\u207f\u207a\u00b9 se a \u2265 5.\n\
- 1 nm = 10\u207b\u2079 m; 1 pm = 10\u207b\u00b9\u00b2 m.\n\
- \u00c1tomo: cerca de 10\u207b\u00b9\u2070 m; n\u00facleo: 10\u207b\u00b9\u2075 m a 10\u207b\u00b9\u2074 m.\n\
- Para comparar, divide-se (subtraem-se expoentes).\n\
@J\n\
O raio do \u00e1tomo de hidrog\u00e9nio \u00e9 53 pm.\n\
Escreve-o em metros, em nota\u00e7\u00e3o cient\u00edfica.\n\
Indica a sua ordem de grandeza.\n\
@R\n\
53 pm = 5,3 \u00d7 10\u207b\u00b9\u00b9 m.\n\
Como 5,3 \u2265 5, a ordem de grandeza \u00e9 10\u207b\u00b9\u2070 m.\n\
@L q1c|Massa at\u00f3mica relativa|unidade de massa atomica massa atomica relativa media isotopos abundancia\
 massa molecular relativa mr ar|c_fqat.ar|10|n\u00facleo|q1a:Constitui\u00e7\u00e3o do \u00e1tomo e\
 is\u00f3topos||AE FQ A 10.\u00ba, Massa e tamanho dos \u00e1tomos\n\
@A\n\
- Definir a unidade de massa at\u00f3mica (u).\n\
- Definir massa at\u00f3mica relativa, Ar.\n\
- Calcular Ar m\u00e9dia a partir dos is\u00f3topos e abund\u00e2ncias.\n\
- Calcular a massa molecular relativa, Mr.\n\
- Explicar porque Ar n\u00e3o \u00e9 um n\u00famero inteiro.\n\
@B\n\
Os \u00e1tomos s\u00e3o leves demais para se pesarem em gramas. Usa-se uma \"unidade de \u00e1tomo\": 1/12 da\
 massa do carbono-12.\n\
Um elemento \u00e9 uma mistura de is\u00f3topos. Ar \u00e9 uma m\u00e9dia pesada, como uma m\u00e9dia de\
 testes com pesos diferentes. O is\u00f3topo mais abundante pesa mais na m\u00e9dia.\n\
@C\n\
- Unidade de massa at\u00f3mica: 1 u = 1/12 da massa de um \u00e1tomo de \u00b9\u00b2C.\n\
- 1 u \u2248 1,66 \u00d7 10\u207b\u00b2\u2077 kg.\n\
- Massa isot\u00f3pica relativa: massa do is\u00f3topo a dividir por 1 u.\n\
- Abund\u00e2ncia: percentagem de \u00e1tomos de cada is\u00f3topo na natureza.\n\
- Ar: m\u00e9dia das massas isot\u00f3picas, pesada pelas abund\u00e2ncias.\n\
- Mr: soma das Ar de todos os \u00e1tomos da f\u00f3rmula.\n\
- Ar e Mr n\u00e3o t\u00eam unidades.\n\
@D\n\
O cloro tem dois is\u00f3topos est\u00e1veis.\n\
O \u00b3\u2075Cl tem massa 34,97 e abund\u00e2ncia 75,76 %.\n\
O \u00b3\u2077Cl tem massa 36,97 e abund\u00e2ncia 24,24 %.\n\
Ar = (34,97 \u00d7 75,76 + 36,97 \u00d7 24,24) / 100 = 35,45.\n\
O valor fica perto de 35 porque o \u00b3\u2075Cl \u00e9 o mais abundante.\n\
Nenhum \u00e1tomo de cloro tem massa 35,45: \u00e9 uma m\u00e9dia.\n\
Para mol\u00e9culas, somam-se as Ar de todos os \u00e1tomos.\n\
Mr(H\u2082O) = 2 \u00d7 1,01 + 16,00 = 18,02.\n\
Mr(CO\u2082) = 12,01 + 2 \u00d7 16,00 = 44,01.\n\
Os valores de Ar est\u00e3o na tabela peri\u00f3dica.\n\
O exame usa Ar com duas casas decimais.\n\
@F Massa at\u00f3mica relativa m\u00e9dia|Ar = \u03a3 (Ar,i \u00d7 %i) / 100|Ar,i: massa isot\u00f3pica\
 relativa do is\u00f3topo i;%i: abund\u00e2ncia do is\u00f3topo i, em %|as abund\u00e2ncias somam 100 %|Cl:\
 (34,97 \u00d7 75,76 + 36,97 \u00d7 24,24) / 100 = 35,45|c_fqat.ar\n\
@F Massa molecular relativa|Mr = \u03a3 (n.\u00ba de \u00e1tomos \u00d7 Ar)|Ar: massa at\u00f3mica relativa\
 de cada elemento|qualquer f\u00f3rmula qu\u00edmica|Mr(H\u2082O) = 2 \u00d7 1,01 + 16,00 = 18,02|c_fqat.mm\n\
@F Unidade de massa at\u00f3mica|1 u = m(\u00b9\u00b2C) / 12 \u2248 1,66 \u00d7 10\u207b\u00b2\u2077\
 kg|m(\u00b9\u00b2C): massa de um \u00e1tomo de carbono-12|massas de \u00e1tomos e mol\u00e9culas|um\
 \u00e1tomo de \u00b9H tem cerca de 1,0 u|\n\
@F\n\
Dados: is\u00f3topos do magn\u00e9sio.\n\
- \u00b2\u2074Mg: 23,99 e 78,99 %\n\
- \u00b2\u2075Mg: 24,99 e 10,00 %\n\
- \u00b2\u2076Mg: 25,98 e 11,01 %\n\
Objetivo: Ar(Mg).\n\
1. Multiplica cada massa pela abund\u00e2ncia.\n\
2. Ar = (23,99 \u00d7 78,99 + 24,99 \u00d7 10,00 + 25,98 \u00d7 11,01) / 100\n\
3. Ar = 2430,9 / 100 = 24,31\n\
> Ar(Mg) = 24,31\n\
Verifica\u00e7\u00e3o: 24,31 est\u00e1 entre 23,99 e 25,98 e perto de 24.\n\
O \u00b2\u2074Mg \u00e9 o mais abundante, logo a m\u00e9dia fica perto de 24.\n\
@G\n\
Ar \u00e9 uma m\u00e9dia: diz quanto pesa, em m\u00e9dia, um \u00e1tomo do elemento.\n\
O is\u00f3topo mais abundante \"puxa\" a m\u00e9dia.\n\
Os valores da tabela v\u00eam de muitas medi\u00e7\u00f5es (espectrometria de massa).\n\
As abund\u00e2ncias podem variar um pouco de amostra para amostra.\n\
@H\n\
- Fazer a m\u00e9dia simples (dividir por 2) sem usar as abund\u00e2ncias.\n\
- Esquecer de dividir por 100 quando as abund\u00e2ncias est\u00e3o em %.\n\
- Dar unidades a Ar ou a Mr: s\u00e3o n\u00fameros sem unidades.\n\
- Confundir o n\u00famero de massa A (inteiro) com a massa isot\u00f3pica.\n\
- Pensar que todos os \u00e1tomos de cloro t\u00eam 35,45 u.\n\
@I\n\
- 1 u = 1/12 da massa do \u00b9\u00b2C \u2248 1,66 \u00d7 10\u207b\u00b2\u2077 kg.\n\
- Ar = \u03a3 (Ar,i \u00d7 %i) / 100.\n\
- Ar \u00e9 a m\u00e9dia pesada das massas dos is\u00f3topos.\n\
- Mr = soma das Ar dos \u00e1tomos da f\u00f3rmula.\n\
- Ar e Mr n\u00e3o t\u00eam unidades.\n\
@J\n\
O boro tem os is\u00f3topos \u00b9\u2070B (10,01; 19,9 %) e \u00b9\u00b9B (11,01; 80,1 %).\n\
Calcula Ar(B).\n\
@R\n\
Ar = (10,01 \u00d7 19,9 + 11,01 \u00d7 80,1) / 100 = 10,81.\n\
@L q1d|Quantidade de mat\u00e9ria e massa molar|quantidade de materia mol mole constante de avogadro massa\
 molar numero de particulas n m m n na|c_fqat.qm|10|n\u00facleo|q1c:Massa at\u00f3mica relativa||AE FQ A\
 10.\u00ba, Massa e tamanho dos \u00e1tomos\n\
@A\n\
- Definir quantidade de mat\u00e9ria e a sua unidade, a mole.\n\
- Usar a constante de Avogadro para contar part\u00edculas.\n\
- Definir massa molar e relacion\u00e1-la com Ar e Mr.\n\
- Calcular n, m e N com n = m / M e N = n \u00d7 NA.\n\
- Apresentar resultados com os algarismos significativos certos.\n\
@B\n\
H\u00e1 bili\u00f5es de \u00e1tomos em qualquer gr\u00e3o de areia.\n\
Contar um a um \u00e9 imposs\u00edvel.\n\
A qu\u00edmica conta \"\u00e0s d\u00fazias\", mas com uma d\u00fazia gigante: a mole.\n\
Uma mole tem 6,02 \u00d7 10\u00b2\u00b3 part\u00edculas.\n\
A massa de uma mole \u00e9 a massa molar.\n\
Em gramas, tem o mesmo valor que Mr.\n\
@C\n\
- Quantidade de mat\u00e9ria, n: conta part\u00edculas; unidade SI: mole (mol).\n\
- Constante de Avogadro: NA = 6,02 \u00d7 10\u00b2\u00b3 mol\u207b\u00b9.\n\
- NA \u00e9 o n\u00famero de part\u00edculas numa mole.\n\
- Massa molar, M: massa de uma mole; unidade g mol\u207b\u00b9.\n\
- M em g mol\u207b\u00b9 tem o valor num\u00e9rico de Mr (ou de Ar).\n\
@D\n\
O n\u00famero de part\u00edculas \u00e9 N = n \u00d7 NA.\n\
A massa e a quantidade ligam-se por n = m / M.\n\
Juntando: N = (m / M) \u00d7 NA.\n\
Diz sempre de que part\u00edculas falas.\n\
1 mol de H\u2082O tem 1 mol de mol\u00e9culas.\n\
Tem tamb\u00e9m 2 mol de \u00e1tomos de H e 1 mol de \u00e1tomos de O.\n\
Ao todo, s\u00e3o 3 mol de \u00e1tomos.\n\
Com M em g mol\u207b\u00b9, a massa tem de estar em gramas.\n\
NA tem 3 algarismos significativos (6,02).\n\
O resultado n\u00e3o pode ter mais algarismos do que os dados.\n\
Desde 2019, NA vale exatamente 6,022 140 76 \u00d7 10\u00b2\u00b3 mol\u207b\u00b9.\n\
O exame usa o valor arredondado 6,02 \u00d7 10\u00b2\u00b3 mol\u207b\u00b9.\n\
@F Quantidade de mat\u00e9ria e massa|n = m / M|n: quantidade de mat\u00e9ria (mol);m: massa (g);M: massa\
 molar (g mol\u207b\u00b9)|subst\u00e2ncia pura|n = 36,04 g / 18,02 g mol\u207b\u00b9 = 2,000 mol|c_fqat.qm\n\
@F N\u00famero de part\u00edculas|N = n \u00d7 NA|N: n\u00famero de part\u00edculas;n: quantidade de\
 mat\u00e9ria (mol);NA: 6,02 \u00d7 10\u00b2\u00b3 mol\u207b\u00b9|qualquer tipo de part\u00edcula|0,50 mol\
 t\u00eam 3,0 \u00d7 10\u00b2\u00b3 part\u00edculas|c_fqat.qm\n\
@F Massa molar|M = m / n|M: massa molar (g mol\u207b\u00b9);m: massa (g);n: quantidade de mat\u00e9ria\
 (mol)|M em g mol\u207b\u00b9 tem o valor de Mr|M(CO\u2082) = 44,01 g mol\u207b\u00b9|c_fqat.mm\n\
@F\n\
Pergunta: quantas mol\u00e9culas e quantos \u00e1tomos h\u00e1 em 9,0 g de \u00e1gua?\n\
Dados: m = 9,0 g; M(H\u2082O) = 18,02 g mol\u207b\u00b9.\n\
1. n = m / M = 9,0 g / 18,02 g mol\u207b\u00b9 = 0,50 mol\n\
2. N = n \u00d7 NA = 0,50 mol \u00d7 6,02 \u00d7 10\u00b2\u00b3 mol\u207b\u00b9\n\
3. N = 3,0 \u00d7 10\u00b2\u00b3 mol\u00e9culas\n\
4. Cada mol\u00e9cula tem 3 \u00e1tomos: 3 \u00d7 3,0 \u00d7 10\u00b2\u00b3 = 9,0 \u00d7 10\u00b2\u00b3\n\
> 3,0 \u00d7 10\u00b2\u00b3 mol\u00e9culas e 9,0 \u00d7 10\u00b2\u00b3 \u00e1tomos.\n\
O resultado tem 2 algarismos significativos, como a massa.\n\
Verifica\u00e7\u00e3o: 9,0 g \u00e9 metade de 18 g, logo \u00e9 meia mole.\n\
@G\n\
A mole liga o mundo dos \u00e1tomos \u00e0 balan\u00e7a do laborat\u00f3rio.\n\
Massas iguais de subst\u00e2ncias diferentes t\u00eam n\u00fameros de part\u00edculas diferentes.\n\
1 g de H\u2082 tem muito mais mol\u00e9culas do que 1 g de O\u2082.\n\
Uma mole de qualquer subst\u00e2ncia tem o mesmo n\u00famero de part\u00edculas.\n\
@H\n\
- Usar NA para passar de massa a mole: \u00e9 preciso M.\n\
- Esquecer quantos \u00e1tomos tem cada mol\u00e9cula.\n\
- Escrever M em g em vez de g mol\u207b\u00b9.\n\
- Arredondar n cedo demais e perder algarismos.\n\
- Dar mais algarismos significativos do que os dados.\n\
@I\n\
- n em mol; 1 mol = 6,02 \u00d7 10\u00b2\u00b3 part\u00edculas.\n\
- n = m / M e N = n \u00d7 NA.\n\
- M em g mol\u207b\u00b9 tem o valor de Mr.\n\
- Diz sempre de que part\u00edculas falas.\n\
- O resultado tem os alg. sig. do dado com menos.\n\
@J\n\
Calcula n e o n\u00famero de mol\u00e9culas em 22,0 g de CO\u2082.\n\
Usa M(CO\u2082) = 44,01 g mol\u207b\u00b9.\n\
@R\n\
n = 22,0 g / 44,01 g mol\u207b\u00b9 = 0,500 mol.\n\
N = 0,500 \u00d7 6,02 \u00d7 10\u00b2\u00b3 = 3,01 \u00d7 10\u00b2\u00b3 mol\u00e9culas.\n\
@L q1e|Fra\u00e7\u00e3o molar e fra\u00e7\u00e3o m\u00e1ssica|fracao molar fracao massica composicao mistura\
 percentagem em massa|c_fqat.fr|10|n\u00facleo|q1d:Quantidade de mat\u00e9ria e massa molar||AE FQ A\
 10.\u00ba, Massa e tamanho dos \u00e1tomos\n\
@A\n\
- Definir fra\u00e7\u00e3o molar e fra\u00e7\u00e3o m\u00e1ssica.\n\
- Calcular a composi\u00e7\u00e3o de uma mistura.\n\
- Passar uma fra\u00e7\u00e3o a percentagem.\n\
- Verificar que as fra\u00e7\u00f5es de uma mistura somam 1.\n\
@B\n\
Numa mistura, cada componente tem a sua \"fatia\".\n\
A fatia pode contar part\u00edculas: \u00e9 a fra\u00e7\u00e3o molar.\n\
Tamb\u00e9m pode contar massa: \u00e9 a fra\u00e7\u00e3o m\u00e1ssica.\n\
As duas fatias diferem quando as part\u00edculas t\u00eam massas diferentes.\n\
@C\n\
- Fra\u00e7\u00e3o molar de A: x_A = n_A / n_total.\n\
- Fra\u00e7\u00e3o m\u00e1ssica de A: w_A = m_A / m_total.\n\
- As fra\u00e7\u00f5es n\u00e3o t\u00eam unidades.\n\
- Em percentagem, multiplica-se por 100.\n\
- A soma das fra\u00e7\u00f5es de todos os componentes \u00e9 1.\n\
@D\n\
Para a fra\u00e7\u00e3o molar, todas as quantidades v\u00eam em mol.\n\
Se tens massas, passa-as primeiro a mol com n = m / M.\n\
Para a fra\u00e7\u00e3o m\u00e1ssica, todas as massas v\u00eam na mesma unidade.\n\
Exemplo: 1,0 mol de N\u2082 e 3,0 mol de H\u2082.\n\
x(H\u2082) = 3,0 / 4,0 = 0,75 e x(N\u2082) = 0,25.\n\
As massas s\u00e3o 28 g de N\u2082 e 6,1 g de H\u2082.\n\
Assim, w(H\u2082) \u00e9 s\u00f3 cerca de 0,18.\n\
O H\u2082 tem mais mol\u00e9culas, mas menos massa.\n\
@F Fra\u00e7\u00e3o molar|x_A = n_A / n_total|x_A: fra\u00e7\u00e3o molar de A;n_A: quantidade de A\
 (mol);n_total: quantidade total (mol)|misturas|1 mol de A em 4 mol: x_A = 0,25|c_fqat.fr\n\
@F Fra\u00e7\u00e3o m\u00e1ssica|w_A = m_A / m_total|w_A: fra\u00e7\u00e3o m\u00e1ssica de A;m_A: massa de\
 A;m_total: massa total, na mesma unidade|misturas e compostos|20 g de sal em 200 g: w = 0,10|c_fqat.fr\n\
@F\n\
Mistura: 36,0 g de \u00e1gua (M = 18,02 g mol\u207b\u00b9).\n\
Mais 46,0 g de etanol (M = 46,08 g mol\u207b\u00b9).\n\
Objetivo: fra\u00e7\u00e3o molar e fra\u00e7\u00e3o m\u00e1ssica da \u00e1gua.\n\
1. n(\u00e1gua) = 36,0 / 18,02 = 2,00 mol\n\
2. n(etanol) = 46,0 / 46,08 = 0,998 mol\n\
3. x(\u00e1gua) = 2,00 / (2,00 + 0,998) = 0,667\n\
4. w(\u00e1gua) = 36,0 / (36,0 + 46,0) = 0,439\n\
> x(\u00e1gua) = 0,667 (66,7 %); w(\u00e1gua) = 0,439 (43,9 %)\n\
Verifica\u00e7\u00e3o: x(etanol) = 1 - 0,667 = 0,333\n\
@G\n\
A \u00e1gua tem mais mol\u00e9culas, logo maior fra\u00e7\u00e3o molar.\n\
Tem menos massa, logo menor fra\u00e7\u00e3o m\u00e1ssica.\n\
As mol\u00e9culas de \u00e1gua s\u00e3o mais leves do que as de etanol.\n\
As fra\u00e7\u00f5es n\u00e3o dependem do tamanho da amostra.\n\
@H\n\
- Juntar massas e quantidades no mesmo total.\n\
- Dar unidades \u00e0s fra\u00e7\u00f5es.\n\
- Usar x quando o enunciado pede w, ou o contr\u00e1rio.\n\
- Esquecer de multiplicar por 100 para obter %.\n\
- Arredondar cedo e as fra\u00e7\u00f5es n\u00e3o somarem 1.\n\
@I\n\
- x_A = n_A / n_total; w_A = m_A / m_total.\n\
- Sem unidades; as fra\u00e7\u00f5es somam 1.\n\
- Em %: multiplica por 100.\n\
- x e w diferem quando as massas molares diferem.\n\
@J\n\
Um lat\u00e3o tem 70 g de cobre e 30 g de zinco.\n\
Qual \u00e9 a fra\u00e7\u00e3o m\u00e1ssica do zinco?\n\
@R\n\
w(Zn) = 30 g / (70 g + 30 g) = 0,30, ou seja, 30 %.\n\
@E 1|q1e1|\u00c1tomos numa amostra de ferro|c_fqat.qm|q1d\n\
Enunciado: quantos \u00e1tomos h\u00e1 em 2,0 mol de ferro?\n\
Dados: n = 2,0 mol; NA = 6,02 \u00d7 10\u00b2\u00b3 mol\u207b\u00b9.\n\
Objetivo: n\u00famero de \u00e1tomos, N.\n\
M\u00e9todo: N = n \u00d7 NA.\n\
Resolu\u00e7\u00e3o:\n\
1. N = 2,0 mol \u00d7 6,02 \u00d7 10\u00b2\u00b3 mol\u207b\u00b9\n\
2. N = 1,204 \u00d7 10\u00b2\u2074\n\
3. Com 2 algarismos significativos: N = 1,2 \u00d7 10\u00b2\u2074\n\
Resultado: h\u00e1 1,2 \u00d7 10\u00b2\u2074 \u00e1tomos de ferro.\n\
Interpreta\u00e7\u00e3o: duas moles t\u00eam o dobro das part\u00edculas de uma mole.\n\
Erros a evitar: dar o resultado com 4 algarismos (o dado tem 2).\n\
@E 2|q1e2|Massa at\u00f3mica relativa do cobre|c_fqat.ar|q1c\n\
Enunciado: calcula Ar(Cu) a partir dos is\u00f3topos.\n\
Dados: \u2076\u00b3Cu, massa 62,93, abund\u00e2ncia 69,15 %.\n\
\u2076\u2075Cu, massa 64,93, abund\u00e2ncia 30,85 %.\n\
Objetivo: massa at\u00f3mica relativa m\u00e9dia.\n\
M\u00e9todo: Ar = \u03a3 (Ar,i \u00d7 %i) / 100.\n\
Resolu\u00e7\u00e3o:\n\
1. 62,93 \u00d7 69,15 = 4351,6\n\
2. 64,93 \u00d7 30,85 = 2003,1\n\
3. Ar = (4351,6 + 2003,1) / 100 = 63,55\n\
Resultado: Ar(Cu) = 63,55.\n\
Interpreta\u00e7\u00e3o: o valor fica mais perto de 63, o is\u00f3topo mais abundante.\n\
Erros a evitar: fazer a m\u00e9dia simples, (62,93 + 64,93) / 2 = 63,93.\n\
@E 3|q1e3|\u00c1tomos de oxig\u00e9nio num sal hidratado|c_fqat.mm|q1d\n\
Enunciado: quantos \u00e1tomos de oxig\u00e9nio h\u00e1 em 5,00 g de CuSO\u2084\u00b75H\u2082O?\n\
Dados: m = 5,00 g; NA = 6,02 \u00d7 10\u00b2\u00b3 mol\u207b\u00b9.\n\
Objetivo: n\u00famero de \u00e1tomos de O.\n\
M\u00e9todo: M, depois n, depois part\u00edculas, depois \u00e1tomos de O.\n\
Resolu\u00e7\u00e3o:\n\
1. M = 63,55 + 32,06 + 4 \u00d7 16,00 + 5 \u00d7 18,02 = 249,71 g mol\u207b\u00b9\n\
2. n = 5,00 / 249,71 = 0,0200 mol\n\
3. Cada unidade tem 4 + 5 = 9 \u00e1tomos de O.\n\
4. n(O) = 9 \u00d7 0,0200 = 0,180 mol\n\
5. N(O) = 0,180 \u00d7 6,02 \u00d7 10\u00b2\u00b3 = 1,08 \u00d7 10\u00b2\u00b3\n\
Resultado: 1,08 \u00d7 10\u00b2\u00b3 \u00e1tomos de oxig\u00e9nio.\n\
Interpreta\u00e7\u00e3o: a \u00e1gua de hidrata\u00e7\u00e3o tamb\u00e9m tem oxig\u00e9nio e conta.\n\
Erros a evitar: contar s\u00f3 os 4 O do sulfato.\n\
"
