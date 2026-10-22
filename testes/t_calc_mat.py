# Testes das calculadoras de Matematica (normal, limite e invalido).
import c_matq
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
