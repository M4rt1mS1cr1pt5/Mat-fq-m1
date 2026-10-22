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
