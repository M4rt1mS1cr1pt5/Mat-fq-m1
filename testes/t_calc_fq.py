# Testes das calculadoras de FQ (normal, limite e invalido).
import c_fqat
from base import calc, erro, tem, perto


def t_mm_normal():
    r = calc(c_fqat, 'mm', ['H2SO4'])
    tem(r[0], '= 98,08 g mol', 'O: 65,25 %')
    perto(r[2], 98.08)


def t_mm_hidrato():
    r = calc(c_fqat, 'mm', ['CuSO4.5H2O'])
    tem(r[0], '= 249,71', 'CuSO₄·5H₂O')


def t_mm_parenteses():
    r = calc(c_fqat, 'mm', ['Ca(OH)2'])
    tem(r[0], '= 74,10')
    r = calc(c_fqat, 'mm', ['Al2(SO4)3'])
    tem(r[0], '= 342,14')


def t_mm_iao():
    r = calc(c_fqat, 'mm', ['SO4^2-'])
    tem(r[0], '= 96,06', 'carga')
    r = calc(c_fqat, 'mm', ['NH4+'])
    tem(r[0], '= 18,05')


def t_mm_maiusculas():
    r = calc(c_fqat, 'mm', ['Co'])
    tem(r[0], '58,93')
    r = calc(c_fqat, 'mm', ['CO'])
    tem(r[0], '28,01')


def t_mm_invalido():
    assert 'desconhecido: Xy' in erro(calc, c_fqat, 'mm', ['Xy2'])
    assert 'maiúscula' in erro(calc, c_fqat, 'mm', ['co2'])
    assert 'fechar' in erro(calc, c_fqat, 'mm', ['Ca(OH2'])
    assert 'a mais' in erro(calc, c_fqat, 'mm', ['CaOH)2'])
    assert 'Escreve' in erro(calc, c_fqat, 'mm', [''])


def t_qm_massa():
    r = calc(c_fqat, 'qm', ['18,02', '10,0', '', '', ''])
    tem(r[0], 'n ≈ 0,555 mol', 'N ≈ 3,34 × 10²³')


def t_qm_volume():
    r = calc(c_fqat, 'qm', ['', '', '', '', '5,6'])
    tem(r[0], 'n = 0,25 mol')


def t_qm_particulas():
    r = calc(c_fqat, 'qm', ['44,01', '', '', '1,204e24', ''])
    tem(r[0], 'n = 2,00 mol', 'm ≈ 88,0 g')


def t_qm_unidades():
    r = calc(c_fqat, 'qm', ['18,02', '1,00', '', '', ''], {1: 1})
    tem(r[0], 'n ≈ 55,5 mol')


def t_qm_invalido():
    assert 'Preenche' in erro(calc, c_fqat, 'qm', ['', '1,0', '2', '', ''])
    assert 'Preenche' in erro(calc, c_fqat, 'qm', ['', '', '', '', ''])
    assert 'massa molar' in erro(calc, c_fqat, 'qm', ['', '1,0', '', '', ''])
    assert 'positiv' in erro(calc, c_fqat, 'qm', ['', '', '-2', '', ''])


def t_ar_normal():
    r = calc(c_fqat, 'ar', ['62,93; 64,93', '69,15; 30,85'])
    tem(r[0], 'Ar médio ≈ 63,55')


def t_ar_soma():
    r = calc(c_fqat, 'ar', ['10,01; 11,01', '20; 79'])
    tem(r[0], 'somam 99 %')


def t_ar_invalido():
    assert 'tantas' in erro(calc, c_fqat, 'ar', ['1;2', '100'])
    assert 'negativas' in erro(calc, c_fqat, 'ar', ['1;2', '-5;105'])


def t_fr_normal():
    r = calc(c_fqat, 'fr', [0, '1,0; 3,0', 'água; etanol'])
    tem(r[0], 'x(água) = 0,25', '75,00 %')


def t_fr_invalido():
    assert 'pelo menos 2' in erro(calc, c_fqat, 'fr', [0, '1,0', ''])
    assert 'zero' in erro(calc, c_fqat, 'fr', [1, '0; 0', ''])


# ---- c_fqel
import c_fqel


def t_fot_lambda():
    r = calc(c_fqel, 'fot', ['500'], {0: 0})
    tem(r[0], 'f = 6,00 × 10¹⁴ Hz', 'E ≈ 3,98 × 10⁻¹⁹ J', 'verde')


def t_fot_ev():
    r = calc(c_fqel, 'fot', ['3,00'], {0: 8})
    tem(r[0], 'λ = 414 nm', 'violeta')


def t_fot_freq():
    r = calc(c_fqel, 'fot', ['5,0e14'], {0: 4})
    tem(r[0], 'λ = 6,0 × 10⁻⁷ m')


def t_fot_limite():
    r = calc(c_fqel, 'fot', ['0,001'], {0: 0})
    tem(r[0], 'raios gama')
    r = calc(c_fqel, 'fot', ['1,0'], {0: 1})
    tem(r[0], 'ondas de rádio')


def t_fot_invalido():
    assert 'positivo' in erro(calc, c_fqel, 'fot', ['-500'], {0: 0})
    assert 'positivo' in erro(calc, c_fqel, 'fot', ['0'], {0: 0})


def t_hid_emissao():
    r = calc(c_fqel, 'hid', ['3', '2'])
    tem(r[0], 'Emissão', 'λ = 657 nm', 'Balmer')


def t_hid_absorcao():
    r = calc(c_fqel, 'hid', ['2', '4'])
    tem(r[0], 'Absorção', 'ΔE ≈ 4,09 × 10⁻¹⁹ J')


def t_hid_ionizacao():
    r = calc(c_fqel, 'hid', ['1', '0'])
    tem(r[0], 'ΔE = 2,18 × 10⁻¹⁸ J', 'ionização', 'λ = 91,2 nm')


def t_hid_invalido():
    assert 'iguais' in erro(calc, c_fqel, 'hid', ['2', '2'])
    assert 'inteiros' in erro(calc, c_fqel, 'hid', ['2,5', '1'])
    assert '1 ou mais' in erro(calc, c_fqel, 'hid', ['0', '2'])


def t_conf_oxigenio():
    r = calc(c_fqel, 'conf', ['8', '0'])
    tem(r[0], '1s² 2s² 2p⁴', '2p [↑↓][↑ ][↑ ]', 'desemparelhados: 2',
        'valência: 6', 'grupo 16')


def t_conf_calcio():
    r = calc(c_fqel, 'conf', ['20', '0'])
    tem(r[0], '3p⁶ 4s²', 'período 4, grupo 2')


def t_conf_excecao():
    r = calc(c_fqel, 'conf', ['29', '0'])
    tem(r[0], '4s¹ 3d¹⁰', 'Exceção')


def t_conf_ioes():
    r = calc(c_fqel, 'conf', ['11', '1'])
    tem(r[0], 'Na⁺', '1s² 2s² 2p⁶')
    r = calc(c_fqel, 'conf', ['26', '3'])
    tem(r[0], 'Fe³⁺', '3p⁶ 3d⁵', 'desemparelhados: 5')


def t_conf_invalido():
    assert '1 a 36' in erro(calc, c_fqel, 'conf', ['40', '0'])
    assert '1 a 36' in erro(calc, c_fqel, 'conf', ['1,5', '0'])
    assert 'teria' in erro(calc, c_fqel, 'conf', ['8', '-40'])
