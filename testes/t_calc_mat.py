# Testes das calculadoras de Matematica (normal, limite e invalido).
import c_matq
import c_matt
from base import calc, erro, tem, perto


def t_q2_racional():
    r = calc(c_matq, 'q2', ['2', '-3', '1'])
    tem(r[0], 'x = 1/2 ∨ x = 1', 'V(3/4, -1/8)',
        'f(x) = 2(x - 3/4)² - 1/8', "D′f = [-1/8, +∞[", 'C.S. = {1/2, 1}')


def t_q2_radical():
    r = calc(c_matq, 'q2', ['1', '-2', '-1'])
    tem(r[0], 'x = 1 - √2 ∨ x = 1 + √2', '(x - 1)² - 2')
    r = calc(c_matq, 'q2', ['2', '-2', '-1'])
    tem(r[0], '(1 - √3)/2')


def t_q2_delta_zero():
    r = calc(c_matq, 'q2', ['1', '-4', '4'])
    tem(r[0], 'um zero', 'x = 2', '(x - 2)²')


def t_q2_sem_zeros():
    r = calc(c_matq, 'q2', ['1/2', '1', '5'])
    tem(r[0], 'não há zeros', 'C.S. = ∅', 'V(-1, 9/2)')


def t_q2_a_zero():
    r = calc(c_matq, 'q2', ['0', '2', '-4'])
    tem(r[0], '1.º grau', 'x = 2')
    r = calc(c_matq, 'q2', ['0', '0', '3'])
    tem(r[0], 'impossível')


def t_q2_aproximado():
    r = calc(c_matq, 'q2', ['sqrt(2)', '1', '-1'])
    tem(r[0], 'x ≈')


def t_q2_invalido():
    assert 'Escreve' in erro(calc, c_matq, 'q2', ['', '1', '1'])
    assert 'desconhecido' in erro(calc, c_matq, 'q2', ['a', '1', '1'])


def t_iq_dentro():
    r = calc(c_matq, 'iq', ['1', '-5', '6', 3])
    tem(r[0], 'C.S. = [2, 3]')


def t_iq_fora():
    r = calc(c_matq, 'iq', ['1', '-5', '6', 0])
    tem(r[0], 'C.S. = ]-∞, 2[ ∪ ]3, +∞[')


def t_iq_baixo():
    r = calc(c_matq, 'iq', ['-1', '0', '4', 0])
    tem(r[0], 'C.S. = ]-2, 2[')


def t_iq_limites():
    r = calc(c_matq, 'iq', ['1', '0', '1', 2])
    tem(r[0], 'C.S. = ∅')
    r = calc(c_matq, 'iq', ['1', '-2', '1', 1])
    tem(r[0], 'C.S. = ℝ')
    r = calc(c_matq, 'iq', ['1', '-2', '1', 0])
    tem(r[0], 'ℝ \\ {1}')
    r = calc(c_matq, 'iq', ['1', '-2', '1', 3])
    tem(r[0], 'C.S. = {1}')


def t_iq_decimal():
    r = calc(c_matq, 'iq', ['2', '-3', '1', 2])
    tem(r[0], ']1/2, 1[')


def t_tf_normal():
    r = calc(c_matq, 'tf', ['x^2', 3, '2', '-1', ''])
    tem(r[0], 'direita', 'baixo')
    perto(r[4][1][1][1](3.0), 0.0)


def t_tf_reflexao():
    r = calc(c_matq, 'tf', ['x^2', 2, '', '', '-2'])
    tem(r[0], 'Dilatação vertical de coeficiente 2', 'Reflexão')


def t_tf_invalido():
    assert 'desconhecido' in erro(calc, c_matq, 'tf', ['y+1', 0, '1', '', ''])
    assert 'c = 0' in erro(calc, c_matq, 'tf', ['x', 2, '', '', '0'])

# ------------------------------------------------------------ c_matt


def t_pn_acutangulo():
    r = calc(c_matt, 'pn', ['0 0', '6 0', '2 4'])
    tem(r[0], 'QR = 4√2', 'escaleno e acutângulo', 'B (baricentro) = (8/3, 4/3)',
        'C (circuncentro) = (3, 1)', 'R = √10', 'O (ortocentro) = (2, 2)',
        'OB = 2√2/3', 'BC = √2/3', 'N = (5/2, 3/2)')
    perto(r[2], 10 ** 0.5)
    assert r[4][0].startswith('Triângulo')


def t_pn_retangulo():
    r = calc(c_matt, 'pn', ['0 0', '4 0', '0 3'])
    tem(r[0], 'escaleno e retângulo', 'I (incentro) = (1, 1)', 'r = 2A / P = 1',
        'C num lado, O num vértice', 'R = 2,5')


def t_pn_obtusangulo_isosceles():
    r = calc(c_matt, 'pn', ['0 0', '10 0', '5 2'])
    tem(r[0], 'isósceles e obtusângulo', 'C exterior, O exterior',
        'C (circuncentro) = (5, -21/4)', 'I também está na reta de Euler')


def t_pn_equilatero():
    r = calc(c_matt, 'pn', ['0 0', '2 0', '1 ' + str(3 ** 0.5)])
    tem(r[0], 'equilátero', 'não há reta de Euler')


def t_pn_invalido():
    assert 'alinhados' in erro(calc, c_matt, 'pn', ['0 0', '1 1', '2 2'])
    assert 'alinhados' in erro(calc, c_matt, 'pn', ['1 1', '1 1', '3 0'])
    assert 'coordenadas' in erro(calc, c_matt, 'pn', ['0 0 1', '1 1', '2 0'])


def t_insc_area_perimetro():
    # exemplos das aulas: A = 96, P = 48 -> r = 4; r = 3, A = 24 -> P = 16
    r = calc(c_matt, 'insc', [0, '96', '48', ''])
    tem(r[0], 'r = 4', '8π')
    r = calc(c_matt, 'insc', [0, '24', '', '3'])
    tem(r[0], 'P = 2A / r = 16')
    r = calc(c_matt, 'insc', [0, '', '16', '3'])
    perto(r[2], 24.0)


def t_insc_retangulo():
    # catetos 5 e 12: c = 13, r = 2, R = 6,5, nove pontos 3,25
    r = calc(c_matt, 'insc', [1, '5', '12', ''])
    tem(r[0], '= 13', 'r = 2', 'R = 6,5', 'R/2 = 3,25')
    r = calc(c_matt, 'insc', [1, '8', '12', ''])
    tem(r[0], '4√13', 'R = 2√13')


def t_insc_invalido():
    assert 'só o campo' in erro(calc, c_matt, 'insc', [0, '96', '', ''])
    assert 'catetos' in erro(calc, c_matt, 'insc', [1, '5', '', ''])
    assert 'medida' in erro(calc, c_matt, 'insc', [0, '-4', '10', ''])


def t_euler_distancias():
    # BC = 1,4: OC = 4,2; ON = 2,1; OB = 2,8; NB = 0,7 (exemplo das aulas)
    r = calc(c_matt, 'euler', [1, '1,4'])
    tem(r[0], 'OB = 2 BC = 2,8', 'OC = 3 BC = 4,2', 'ON = 2,1; NB = 0,7')
    r = calc(c_matt, 'euler', [0, '4'])
    tem(r[0], 'BC = 2', 'OC = 3 BC = 6')
    r = calc(c_matt, 'euler', [2, '7,5'])
    perto(r[2], 2.5)


def t_euler_raios():
    # area da circunscrita 64 pi -> R = 8 -> r9 = 4, comprimento 8 pi
    r = calc(c_matt, 'euler', [3, '8'])
    tem(r[0], 'r₉ = R / 2 = 4', 'comprimento = 8π')
    r = calc(c_matt, 'euler', [4, '5'])
    tem(r[0], 'R = 10', '20π')
    assert 'valor' in erro(calc, c_matt, 'euler', [0, '0'])


def t_pit():
    r = calc(c_matt, 'pit', ['3', '4', ''])
    tem(r[0], 'c = √(a² + b²) = 5')
    r = calc(c_matt, 'pit', ['', '5', '13'])
    perto(r[2], 12.0)
    r = calc(c_matt, 'pit', ['1', '1', ''])
    tem(r[0], '√2')
    assert 'maior' in erro(calc, c_matt, 'pit', ['', '13', '5'])
    assert 'só o campo' in erro(calc, c_matt, 'pit', ['3', '4', '5'])


def t_sem():
    r = calc(c_matt, 'sem', ['4', '6', '5', '12'])
    tem(r[0], 'k = 1,5', 'ampliação', '= 7,5', '= 27')
    r = calc(c_matt, 'sem', ['6', '2', '', ''])
    tem(r[0], 'k = 1/3', 'redução')
    assert 'medida' in erro(calc, c_matt, 'sem', ['0', '2', '', ''])
