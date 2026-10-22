# Testes dos assistentes das atividades laboratoriais (normal, limite e
# invalido).
import c_alq1
import c_alq2
import c_alf1
import c_alf2
from base import calc, erro, tem, perto

# ------------------------------------------------------------ AL Q1.1


def t_gota_normal():
    r = calc(c_alq1, 'gota', ['0,99; 1,02; 1,01', '20', '0,01'])
    tem(r[0], '0,0495; 0,0510; 0,0505 g', 'm(gota) = (0,0503 ± 0,0009) g',
        'V = (0,0503 ± 0,0009) cm³', 'N = (1,68 ± 0,03) × 10²¹')
    perto(r[2], 1.01 / 20 / 18.02 * 6.02e23 * (0.99 + 1.02 + 1.01) / 3.03)


def t_gota_um_ensaio():
    # um so ensaio: a incerteza vem da balanca (0,01 g / 20 gotas)
    r = calc(c_alq1, 'gota', ['1,00', '20', '0,01'])
    tem(r[0], '(0,0500 ± 0,0005) g', 'Incerteza relativa: 1,0 %')


def t_gota_invalido():
    assert 'inteiro' in erro(calc, c_alq1, 'gota', ['1', '2,5', '0,01'])
    assert 'inteiro' in erro(calc, c_alq1, 'gota', ['1', '0', '0,01'])
    assert 'massa' in erro(calc, c_alq1, 'gota', ['1; -1', '20', '0,01'])
    assert 'incerteza' in erro(calc, c_alq1, 'gota', ['1', '20', '-1'])

# ------------------------------------------------------------ AL Q1.2


def t_chama_tabela():
    r = calc(c_alq1, 'chama', [1])
    tem(r[0], 'sódio (Na)', '589 nm')
    r = calc(c_alq1, 'chama', [0])
    tem(r[0], 'lítio (Li)', '671 nm')
    r = calc(c_alq1, 'chama', [2])
    tem(r[0], 'potássio (K)', 'cobalto')


def t_chama_todas():
    for k in range(7):
        r = calc(c_alq1, 'chama', [k])
        tem(r[0], 'Elemento provável: ', 'nm')
        assert r[2] is None

# ------------------------------------------------------------ AL Q1.3


def t_dens_cobre():
    r = calc(c_alq1, 'dens', ['20,15', '82,40', '100,30', 4])
    tem(r[0], 'm + m1 - m2 = 2,25 g', 'd ≈ 8,96', 'cobre', 'Boa exatidão')
    perto(r[2], 20.15 / 2.25)


def t_dens_aluminio():
    r = calc(c_alq1, 'dens', ['5,40', '82,40', '85,80', 1])
    tem(r[0], '= 2,00 g', 'd = 2,70', 'Erro percentual = 0,0 %')
    r = calc(c_alq1, 'dens', ['20,15', '82,40', '100,30', 3])
    tem(r[0], 'zinco', 'Erro grande')


def t_dens_invalido():
    assert 'incoerentes' in erro(calc, c_alq1, 'dens', ['5', '80', '90', 0])
    assert 'massa do metal' in erro(calc, c_alq1, 'dens', ['0', '80', '90', 0])

# ------------------------------------------------------------ AL Q2.1


def t_misc_agua():
    r = calc(c_alq2, 'misc', [0, 3])
    tem(r[0], 'imiscíveis', 'Fica por cima o menos denso: hexano')
    assert r[2] == 0
    r = calc(c_alq2, 'misc', [5, 0])
    tem(r[0], 'imiscíveis', 'óleo alimentar')


def t_misc_semelhantes():
    assert calc(c_alq2, 'misc', [0, 1])[2] == 1
    assert calc(c_alq2, 'misc', [3, 5])[2] == 1
    assert calc(c_alq2, 'misc', [0, 2])[2] == 1


def t_misc_incerta():
    r = calc(c_alq2, 'misc', [1, 3])
    tem(r[0], 'Previsão incerta', 'etanol')
    assert r[2] is None
    assert 'diferentes' in erro(calc, c_alq2, 'misc', [2, 2])

# ------------------------------------------------------------ AL Q2.2


def t_sol_massa():
    r = calc(c_alq2, 'sol', ['58,44', '100,00', '0,10', '0,100', '', '0,01'])
    tem(r[0], '0,100 × 0,10000 dm³ × 58,44', 'm a pesar ≈ 0,584 g')
    perto(r[2], 0.5844)


def t_sol_incerteza():
    r = calc(c_alq2, 'sol', ['58,44', '100,00', '0,10', '0,100', '0,59',
                             '0,01'])
    tem(r[0], 'c = (0,101 ± 0,002) mol dm⁻³', '1,8 %', 'pretendida: 0,96 %')
    r = calc(c_alq2, 'sol', ['249,7', '250,0', '0,15', '', '6,25', '0,01'])
    tem(r[0], '(0,1001 ± 0,0003)')
    perto(r[2], 6.25 / (249.7 * 0.25))


def t_sol_invalido():
    assert 'pretendida ou a massa' in erro(calc, c_alq2, 'sol',
                                          ['58', '100', '0,1', '', '', '0,01'])
    assert 'massa molar' in erro(calc, c_alq2, 'sol',
                                 ['0', '100', '0,1', '0,1', '', '0,01'])

# ------------------------------------------------------------ AL F1.1


def t_plano_normal():
    r = calc(c_alf1, 'plano', ['500', '1,00', '0,20; 0,40; 0,60; 0,80',
                               '15,0; 10,6; 8,7; 7,5'])
    tem(r[0], 'd = 0,20 m: v = 0,667 m/s; Ec = 0,111 J', 'bom ajuste',
        'F(resultante) ≈ 0,554 N')
    assert r[4][0].startswith('Ec (J)')


def t_plano_invalido():
    assert 'mesmo número' in erro(calc, c_alf1, 'plano', ['500', '1', '0,2; 0,4',
                                                    '15; 10; 8'])
    assert '3 pontos' in erro(calc, c_alf1, 'plano', ['500', '1', '0,2; 0,4',
                                                      '15; 10'])
    assert 'tempo' in erro(calc, c_alf1, 'plano', ['500', '1', '0,2; 0,4; 0,6',
                                                   '15; 0; 8'])
    assert 'iguais' in erro(calc, c_alf1, 'plano', ['500', '1', '0,2; 0,2; 0,2',
                                                    '15; 10; 8'])

# ------------------------------------------------------------ AL F1.2


def t_ress_normal():
    r = calc(c_alf1, 'ress', ['100; 80; 60; 40', '72; 58; 43; 29'])
    tem(r[0], '≈ 0,72 (declive)', 'dissipada no ressalto ≈ 28 %')
    perto(r[2], (1 - (0.72 + 58 / 80.0 + 43 / 60.0 + 29 / 40.0) / 4) * 100)


def t_ress_invalido():
    assert 'mais alto' in erro(calc, c_alf1, 'ress', ['100; 80; 60',
                                                      '72; 90; 43'])
    assert 'queda' in erro(calc, c_alf1, 'ress', ['100; 0; 60', '72; 0; 43'])

# ------------------------------------------------------------ AL F2.1


def t_pilha_normal():
    r = calc(c_alf1, 'pilha', ['50; 100; 150; 200; 250',
                               '4,40; 4,32; 4,26; 4,18; 4,11'])
    tem(r[0], 'ε = 4,47 V', 'r ≈ 1,4 Ω', 'curto-circuito')
    perto(r[2], 4.47)


def t_pilha_avisos():
    r = calc(c_alf1, 'pilha', ['50; 100; 150', '4,0; 4,1; 4,2'])
    tem(r[0], 'Declive não negativo')
    assert '3 pontos' in erro(calc, c_alf1, 'pilha', ['50; 100', '4,4; 4,3'])
    assert 'corrente' in erro(calc, c_alf1, 'pilha', ['-5; 100; 150',
                                                      '4,4; 4,3; 4,2'])

# ------------------------------------------------------------ AL F3.1


def t_painel_normal():
    r = calc(c_alf2, 'painel', ['0,5; 1,5; 2,5; 3,0; 3,3',
                                '60; 58; 52; 40; 20', '800', '50'])
    tem(r[0], 'P = 130 mW (máx.)', 'R = U / I ≈ 48 Ω', 'P(radiação) = Er A = 4,0 W',
        '≈ 3,3 %')
    perto(r[2], 0.13)


def t_painel_sem_rad():
    r = calc(c_alf2, 'painel', ['1; 2; 3', '50; 40; 10', '', ''])
    assert 'η' not in r[0]
    perto(r[2], 0.08)
    assert 'mesmo número' in erro(calc, c_alf2, 'painel', ['1; 2; 3', '50; 40', '', ''])

# ------------------------------------------------------------ AL F3.2


def t_cap_normal():
    r = calc(c_alf2, 'cap', ['1000', '60', '0; 60; 120; 180; 240',
                             '20,0; 24,0; 28,1; 32,0; 36,1', '900'])
    tem(r[0], 'c ≈ 896 J kg⁻¹ K⁻¹', 'Erro percentual = 0,50 %')
    perto(r[2], 60 / 0.067, 1e-3)


def t_cap_invalido():
    assert 'não sobe' in erro(calc, c_alf2, 'cap', ['1000', '60', '0; 60; 120',
                                                    '20; 20; 20', ''])
    assert 'potência' in erro(calc, c_alf2, 'cap', ['1000', '0', '0; 60; 120',
                                                    '20; 21; 22', ''])

# ------------------------------------------------------------ AL F3.3


def t_fusao_normal():
    r = calc(c_alf2, 'fusao', ['250,0', '40,0', '60,0', '16,0'])
    tem(r[0], '2,51 × 10⁴ J', '4,01 × 10³ J', 'ΔHf ≈ 3,51 × 10⁵',
        'Erro percentual = 5,1 %')
    perto(r[2], (0.25 * 4180 * 24 - 0.06 * 4180 * 16) / 0.06)


def t_fusao_invalido():
    assert 'entre 0' in erro(calc, c_alf2, 'fusao', ['100', '20', '50', '30'])
    assert 'incoerentes' in erro(calc, c_alf2, 'fusao', ['100', '20', '500', '19'])
