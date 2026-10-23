# Testes dos resolvedores de Dados e Probabilidades do 7.o ao 9.o ano
# (c_mprb): normal, limite e invalido.
import c_mprb
from base import calc, erro, tem, perto


def t_freq_numericos():
    r = calc(c_mprb, 'freq', ['3 5 4 3 2 5 3 4 1 3', ''])
    tem(r[0], 'n = 10 dados quantitativos; 5 valores diferentes',
        '3 → 4; 4/10 = 2/5 = 0,4 = 40%; 144°; acumulada 6',
        '> Moda: 3 (frequência 4)',
        '> Média = (1 × 1 + 2 × 1 + 3 × 4 + 4 × 2 + 5 × 2) / 10 = 33 / 10 = 3,3',
        '> Mediana: (3 + 3) / 2 = 3 (n par: posições 5 e 6)',
        '> Amplitude: 5 - 1 = 4')
    perto(r[2], 3.3)
    assert r[4][0] == 'Gráfico de barras'


def t_freq_com_frequencias():
    r = calc(c_mprb, 'freq', ['1 2 3 4', '4 6 5 2'])
    tem(r[0], 'n = 17', '1 → 4; 4/17 ≈ 0,24 ≈ 23,5%; ≈ 84,7°',
        '= 39 / 17 ≈ 2,29', '> Mediana: 2 (n ímpar: valor na posição 9)')
    r = calc(c_mprb, 'freq', ['2,5 1', '1 3'])
    tem(r[0], '1 → 3', '2,5 → 1', '> Média = (1 × 3 + 2,5 × 1) / 4 = 5,5 / 4 ='
        ' 1,375')


def t_freq_qualitativos_moda():
    r = calc(c_mprb, 'freq', ['futebol tenis futebol basquete natacao futebol',
                              ''])
    tem(r[0], 'qualitativos', 'futebol → 3; 3/6 = 1/2 = 0,5 = 50%; 180°',
        '> Moda: futebol', 'não há média nem mediana')
    assert r[2] is None
    tem(calc(c_mprb, 'freq', ['A B C', '2 2 2'])[0], 'Não há moda')
    tem(calc(c_mprb, 'freq', ['2 4 4 2 7', ''])[0], '> Moda: 2, 4',
        'bimodal', '> Mediana: 4')


def t_freq_invalidos():
    assert 'espaços' in erro(calc, c_mprb, 'freq', ['  ', ''])
    assert 'inteiros' in erro(calc, c_mprb, 'freq', ['1 2', '1 x'])
    assert 'inteiros' in erro(calc, c_mprb, 'freq', ['1 2', '1 -1'])
    assert '2 valores e 3' in erro(calc, c_mprb, 'freq', ['1 2', '1 2 3'])
    assert 'é 0' in erro(calc, c_mprb, 'freq', ['1 2', '0 0'])
    assert 'repetidos' in erro(calc, c_mprb, 'freq', ['A A', '1 2'])


def t_freq_muitos_valores_sem_grafico():
    r = calc(c_mprb, 'freq', [' '.join([str(i) for i in range(1, 15)]), ''])
    assert len(r) == 4
    tem(r[0], '> Média = soma / n = 105 / 14 = 7,5', 'Não há moda')


def t_prob_categorias():
    r = calc(c_mprb, 'prob', ['3 azuis 5 vermelhas 2 verdes', 'azuis'])
    tem(r[0], 'Casos possíveis: 3 + 5 + 2 = 10',
        'P(vermelhas) = 5/10 = 1/2 = 0,5 = 50%', '> P(A) = 3/10 = 0,3 = 30%',
        'P(não A) = 1 - P(A) = 7/10', 'pouco provável')
    perto(r[2], 0.3)
    r = calc(c_mprb, 'prob', ['3 azuis 5 vermelhas 2 verdes', 'azul verde'])
    tem(r[0], 'azuis ou verdes', '> P(A) = (3 + 2)/10 = 5/10 = 1/2',
        'tão provável como improvável')
    r = calc(c_mprb, 'prob', ['3 azuis 5 vermelhas 2 verdes', 'não vermelhas'])
    tem(r[0], 'azuis ou verdes')
    r = calc(c_mprb, 'prob', ['4 ases 48 outras cartas', 'ases'])
    tem(r[0], 'P(outras cartas) = 48/52 = 12/13', '> P(A) = 4/52 = 1/13')


def t_prob_numeros():
    r = calc(c_mprb, 'prob', ['3 10', ''])
    tem(r[0], '> P(A) = 3/10 = 0,3 = 30%', '7/10')
    tem(calc(c_mprb, 'prob', ['12 13', ''])[0], '12/13 ≈ 0,92 ≈ 92,3%',
        'muito provável')
    tem(calc(c_mprb, 'prob', ['0 6', ''])[0], '0/6 = 0', 'impossível')
    tem(calc(c_mprb, 'prob', ['6 6', ''])[0], '6/6 = 1 = 100%', 'certo')
    assert r[2] == 0.3


def t_prob_invalidos():
    assert 'mais do que os possíveis' in erro(calc, c_mprb, 'prob',
                                              ['12 10', ''])
    assert 'mais letras' in erro(calc, c_mprb, 'prob',
                                 ['3 azuis 5 vermelhas 2 verdes', 'ver'])
    assert 'Não conheço' in erro(calc, c_mprb, 'prob', ['3 azuis 2 verdes',
                                                       'amarelas'])
    assert 'Começa por um número' in erro(calc, c_mprb, 'prob', ['azuis 3', ''])
    assert 'inteiro' in erro(calc, c_mprb, 'prob', ['2,5 azuis 3 verdes', ''])
    assert 'Dá um nome' in erro(calc, c_mprb, 'prob', ['3 4 5', ''])


def t_dados_soma():
    r = calc(c_mprb, 'dados', [0, '7'])
    tem(r[0], '1 | 2 3 4 5 6 7', '6 | 7 8 9 10 11 12', '36 casos possíveis',
        '7: 6', 'Casos favoráveis: (1,6) (2,5) (3,4) (4,3) (5,2) (6,1) → 6',
        '> P(A) = 6/36 = 1/6 ≈ 0,17 ≈ 16,7%')
    g = r[4]
    assert g[0] == 'Tabela de dupla entrada: soma'
    assert len(g[1][-1][1]) == 6     # casos favoraveis a vermelho
    tem(calc(c_mprb, 'dados', [0, '> 9'])[0], 'soma > 9', '6/36')
    tem(calc(c_mprb, 'dados', [0, 'primo'])[0], 'é número primo', '15/36 = '
        '5/12')
    tem(calc(c_mprb, 'dados', [0, 'múltiplo de 5'])[0], '7/36')
    tem(calc(c_mprb, 'dados', [0, '13'])[0], '0/36 = 0')


def t_dados_produto_diferenca():
    r = calc(c_mprb, 'dados', [1, 'par'])
    tem(r[0], '6 | 6 12 18 24 30 36', 'produto é par',
        'Casos favoráveis: 27 (a vermelho na tabela)', '27/36 = 3/4 = 0,75')
    tem(calc(c_mprb, 'dados', [1, '<= 6'])[0], 'produto ≤ 6', '14/36 = 7/18')
    tem(calc(c_mprb, 'dados', [2, '0'])[0], '0: 6; 1: 10; 2: 8', '6/36')
    tem(calc(c_mprb, 'dados', [2, 'ímpar'])[0], 'diferença é ímpar', '18/36')


def t_dados_moedas():
    r = calc(c_mprb, 'dados', [3, 'pelo menos 1 E'])
    tem(r[0], 'EE, EN, NE, NN', 'n.º de E ≥ 1', 'EE EN NE → 3',
        '> P(A) = 3/4 = 0,75 = 75%')
    assert len(r) == 4
    tem(calc(c_mprb, 'dados', [4, '2'])[0], '8 casos', '0: 1; 1: 3; 2: 3; 3: 1',
        'EEN ENE NEE → 3', '3/8 ≈ 0,38 = 37,5%')
    r = calc(c_mprb, 'dados', [4, ''])
    assert r[2] is None and 'Acontecimento' not in r[0]


def t_dados_invalidos():
    assert 'Não percebi' in erro(calc, c_mprb, 'dados', [0, 'abc'])
    assert 'Não percebi' in erro(calc, c_mprb, 'dados', [0, '> x'])
    assert 'depois de' in erro(calc, c_mprb, 'dados', [0, 'múltiplo de'])
    assert c_mprb.primo(2) and c_mprb.primo(11) and not c_mprb.primo(1) \
        and not c_mprb.primo(9)


def t_urna_sem_reposicao():
    r = calc(c_mprb, 'urna', ['3 azuis 2 brancas', 0, ''])
    tem(r[0], '2.ª extração com 4', 'azuis → azuis: 3/5 × 2/4 = 3/10',
        'brancas → brancas: 2/5 × 1/4 = 1/10', 'Soma de todos os ramos: 1 ✓',
        '> Do mesmo tipo (ex.: mesma cor): 8/20 = 2/5',
        '> De tipos diferentes: 12/20 = 3/5')
    assert r[4][0] == 'Diagrama em árvore'
    r = calc(c_mprb, 'urna', ['3 azuis 2 brancas', 0, 'azul'])
    tem(r[0], '> P(duas azuis) = 6/20 = 3/10',
        '> P(exatamente uma azuis) = 12/20 = 3/5',
        '> P(pelo menos uma azuis) = 1 - P(nenhuma) = 18/20 = 9/10')
    perto(r[2], 0.9)


def t_urna_com_reposicao():
    r = calc(c_mprb, 'urna', ['3 azuis 2 brancas', 1, 'azul branca'])
    tem(r[0], 'com reposição.', 'azuis → azuis: 3/5 × 3/5 = 9/25',
        '> P(1.ª azuis e 2.ª brancas) = 6/25 = 0,24 = 24%',
        'por qualquer ordem) = 12/25')
    perto(r[2], 0.24)


def t_urna_tres_grupos_e_limites():
    r = calc(c_mprb, 'urna', ['2 vermelhas 3 verdes 1 preta', 0,
                              'preta preta'])
    tem(r[0], 'preta → preta: 1/6 × 0/5 = 0', '0/30 = 0')
    assert len(r) == 5
    r = calc(c_mprb, 'urna', ['1 azul 1 branca', 0, 'azul'])
    tem(r[0], '> P(duas azul) = 0/2 = 0', 'exatamente uma azul) = 2/2 = 1')
    r = calc(c_mprb, 'urna', ['1 a 1 b 1 c 1 d', 0, ''])
    assert len(r) == 4     # sem desenho com 4 grupos


def t_urna_invalidos():
    assert 'dois grupos' in erro(calc, c_mprb, 'urna', ['5 azuis', 0, ''])
    assert 'vazia' in erro(calc, c_mprb, 'urna', ['0 azuis 0 brancas', 1, ''])
    assert 'pelo menos 2' in erro(calc, c_mprb, 'urna', ['1 azul 0 branca', 0,
                                                        ''])
    assert 'um ou dois nomes' in erro(calc, c_mprb, 'urna',
                                      ['3 azuis 2 brancas', 0, 'a b c'])
    assert 'No máximo 6' in erro(calc, c_mprb, 'urna',
                                 ['1 a 1 b 1 c 1 d 1 e 1 f 1 g', 0, ''])
