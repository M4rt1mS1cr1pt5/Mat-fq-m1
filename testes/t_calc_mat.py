# Testes das calculadoras de Matematica (normal, limite e invalido).
import c_matq
import c_matt
import c_matf
import c_matg
import c_matv
import c_matc
import c_matd
import c_mate
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

# ------------------------------------------------------------ c_matf


def t_fx_quadratica():
    r = calc(c_matf, 'fx', ['x^2 - 4', '-5', '5', '3'])
    tem(r[0], 'f(3) = 5', 'x = -2,5: f(x) = 2,25', 'Zeros em [-5, 5]: -2, 2',
        'f > 0 em ]-5, -2[ ∪ ]2, 5[', 'f < 0 em ]-2, 2[',
        'Mínimo relativo = -4 em x = 0')
    perto(r[2], 5.0)
    assert r[4][0] == 'f(x) = x^2 - 4'


def t_fx_raizes_e_extremos():
    r = calc(c_matf, 'fx', ['x^3 - 3x', '-3', '3', ''])
    tem(r[0], 'Zeros em [-3, 3]: -√3, 0, √3', 'Máximo relativo = 2 em x = -1',
        'Mínimo relativo = -2 em x = 1')
    r = calc(c_matf, 'fx', ['(x-1)^2', '-4', '4', ''])
    tem(r[0], 'Zeros em [-4, 4]: 1', 'f < 0 em ∅')


def t_fx_dominio():
    r = calc(c_matf, 'fx', ['1/x', '-2', '2', ''])
    tem(r[0], 'x = 0: sem valor', 'não está definida em parte',
        'Zeros em [-2, 2]: nenhum')
    assert 'definida em x = 0' in erro(calc, c_matf, 'fx', ['1/x', '-2', '2', '0'])


def t_fx_invalido():
    assert 'a < b' in erro(calc, c_matf, 'fx', ['x', '5', '1', ''])
    assert 'não tem valores' in erro(calc, c_matf, 'fx', ['sqrt(x)', '-5', '-1', ''])


def t_afim_dois_pontos():
    r = calc(c_matf, 'afim', ['', '', '1 3', '3 7'])
    tem(r[0], 'm = 2', 'b = yA - m xA = 1', 'f(x) = 2x + 1', 'x = -b / m = -0,5',
        'f > 0 em ]-0,5; +∞[', 'Crescente')
    r = calc(c_matf, 'afim', ['', '', '0 0', '3 1'])
    tem(r[0], 'f(x) = (1/3)x')


def t_afim_outros_dados():
    r = calc(c_matf, 'afim', ['', '-1', '2 0', ''])
    tem(r[0], 'm = 0,5', 'f(x) = 0,5x - 1', 'x = -b / m = 2')
    r = calc(c_matf, 'afim', ['-0,5', '4', '', ''])
    tem(r[0], 'f(x) = -0,5x + 4', 'Decrescente', 'f > 0 em ]-∞, 8[')
    r = calc(c_matf, 'afim', ['0', '3', '', ''])
    tem(r[0], 'constante', 'Zeros: nenhum')


def t_afim_invalido():
    assert 'vertical' in erro(calc, c_matf, 'afim', ['', '', '2 1', '2 5'])
    assert 'Dá m e b' in erro(calc, c_matf, 'afim', ['2', '', '', ''])
    assert 'duas coordenadas' in erro(calc, c_matf, 'afim', ['', '', '1', '2 3'])
    assert 'deixa m e b' in erro(calc, c_matf, 'afim', ['1', '', '1 2', '2 3'])


def t_ramos_dois():
    r = calc(c_matf, 'ramos', ['-x', '0', 'x^2', '', '', 0, '-3'])
    tem(r[0], '-x, se x < 0', 'x^2, se x ≥ 0', 'f(-3) = 3 (ramo 1)', '(contínua)',
        'Zeros em [-10, 10]: 0')
    perto(r[2], 3.0)


def t_ramos_tres_e_esquerda():
    r = calc(c_matf, 'ramos', ['x+1', '1', '5-x', '3', '2', 0, ''])
    tem(r[0], '5-x, se 1 ≤ x < 3', '2, se x ≥ 3', '(salto)', 'Zeros em [-9, 13]: -1')
    r = calc(c_matf, 'ramos', ['x', '1', '2', '', '', 1, '1'])
    tem(r[0], 'x, se x ≤ 1', 'f(1) = 1 (ramo 1)')


def t_ramos_invalido():
    assert 'dois primeiros' in erro(calc, c_matf, 'ramos', ['x', '0', '', '', '', 0, ''])
    assert 'maior do que a' in erro(calc, c_matf, 'ramos', ['x', '2', '1', '1', '0', 0, ''])
    assert '3.º ramo' in erro(calc, c_matf, 'ramos', ['x', '0', '1', '3', '', 0, ''])


def t_mod_ramos_zeros():
    r = calc(c_matf, 'mod', ['-4', '0', '2', 0, ''])
    tem(r[0], 'f(x) = -4|x| + 2', '-4x + 2, se x ≥ 0', '4x + 2, se x < 0',
        'máximo 2', 'D′f = ]-∞, 2]', 'C.S. = {-0,5; 0,5}')
    r = calc(c_matf, 'mod', ['1', '6', '0', 0, ''])
    tem(r[0], 'x - 6, se x ≥ 6', '-x + 6, se x < 6', 'C.S. = {6}')


def t_mod_condicoes():
    r = calc(c_matf, 'mod', ['1', '6', '0', 1, '3'])
    tem(r[0], 'f(x) < 3: C.S. = ]3, 9[')
    r = calc(c_matf, 'mod', ['2', '-1', '-4', 2, '2'])
    tem(r[0], 'C.S. = {-3, 1}', 'f(x) > 2: C.S. = ]-∞, -4[ ∪ ]2, +∞[')
    r = calc(c_matf, 'mod', ['-1', '0', '0', 2, '1'])
    tem(r[0], 'f(x) > 1: C.S. = ∅')
    r = calc(c_matf, 'mod', ['1', '0', '0', 2, '0'])
    tem(r[0], 'C.S. = ℝ \\ {0}')
    assert 'a = 0' in erro(calc, c_matf, 'mod', ['0', '1', '2', 0, ''])

# ------------------------------------------------------------ c_matg


def t_dist_plano_espaco():
    r = calc(c_matg, 'dist', ['1 2', '4 6'])
    tem(r[0], 'AB = √(9 + 16)', 'AB = 5', 'M = (2,5; 4)')
    perto(r[2], 5.0)
    r = calc(c_matg, 'dist', ['1 2 3', '2 0 1'])
    tem(r[0], '(zB - zA)²', 'AB = 3', 'M = (1,5; 1; 2)')
    r = calc(c_matg, 'dist', ['0 0', '1 1'])
    tem(r[0], 'AB = √2')


def t_dist_invalido():
    assert 'mesmo número' in erro(calc, c_matg, 'dist', ['1 2', '1 2 3'])
    assert 'coordenadas' in erro(calc, c_matg, 'dist', ['1', '1 2'])
    assert 'coordenadas' in erro(calc, c_matg, 'dist', ['', '1 2'])


def t_reta_dois_pontos():
    r = calc(c_matg, 'reta', ['1 3', '3 7', '', '0 0'])
    tem(r[0], 'm = 2', 'y = 2x + 1', 'Corta Ox em (-0,5; 0)', 'Paralela por P: y = 2x')
    perto(r[2], 2.0)


def t_reta_vertical_e_declive():
    r = calc(c_matg, 'reta', ['2 1', '2 5', '', ''])
    tem(r[0], 'reta vertical', 'x = 2', 'não está definido')
    r = calc(c_matg, 'reta', ['-1 2', '', '-0,5', '4 4'])
    tem(r[0], 'y = -0,5x + 1,5', 'Paralela por P: y = -0,5x + 6')
    r = calc(c_matg, 'reta', ['0 5', '3 5', '', ''])
    tem(r[0], 'y = 5', 'horizontal')


def t_reta_invalido():
    assert 'só um dos dois' in erro(calc, c_matg, 'reta', ['1 1', '2 2', '3', ''])
    assert 'só um dos dois' in erro(calc, c_matg, 'reta', ['1 1', '', '', ''])
    assert 'mesmo ponto' in erro(calc, c_matg, 'reta', ['1 1', '1 1', '', ''])


def t_medz_plano():
    r = calc(c_matg, 'medz', ['1 1', '5 3'])
    tem(r[0], '(x - 1)² + (y - 1)² =', 'Simplificando: 2x + y = 8',
        'Mediatriz: y = -2x + 8', 'M = (3, 2)')
    r = calc(c_matg, 'medz', ['1 1', '1 5'])
    tem(r[0], 'Mediatriz: y = 3')
    r = calc(c_matg, 'medz', ['0 0', '4 0'])
    tem(r[0], 'x = 2 (reta vertical)')


def t_medz_espaco_e_invalido():
    r = calc(c_matg, 'medz', ['1 2 3', '3 2 1'])
    tem(r[0], 'Plano mediador: x - z = 0', 'M = (2, 2, 2)')
    assert 'mesmo ponto' in erro(calc, c_matg, 'medz', ['1 1', '1 1'])


def t_circ_plano():
    r = calc(c_matg, 'circ', [0, '1 -2', '3', '', ''])
    tem(r[0], '(x - 1)² + (y + 2)² = 9', 'Círculo: (x - 1)² + (y + 2)² ≤ 9')
    r = calc(c_matg, 'circ', [1, '0 0', '', '3 4', '1 1'])
    tem(r[0], 'x² + y² = 25', 'dentro')
    r = calc(c_matg, 'circ', [2, '1 1', '', '5 1', '3 3'])
    tem(r[0], 'Centro (3, 1)', '(x - 3)² + (y - 1)² = 4', 'sobre a circunferência')
    r = calc(c_matg, 'circ', [0, '0 0', '2', '', '3 0'])
    tem(r[0], 'fora')


def t_circ_espaco_e_invalido():
    r = calc(c_matg, 'circ', [0, '1 2 -3', '3', '', ''])
    tem(r[0], 'Superfície esférica: (x - 1)² + (y - 2)² + (z + 3)² = 9',
        'Tangente ao(s) plano(s) xOy')
    assert 'raio' in erro(calc, c_matg, 'circ', [0, '1 1', '-2', '', ''])
    assert 'iguais' in erro(calc, c_matg, 'circ', [1, '1 1', '', '1 1', ''])
    assert 'raio vazio' in erro(calc, c_matg, 'circ', [1, '1 1', '2', '3 3', ''])


def t_cond_conjuncao():
    r = calc(c_matg, 'cond', ['y >= x - 1 e x <= 2', '1 1'])
    tem(r[0], 'y ≥ x - 1 ∧ x ≤ 2', 'y ≥ x - 1: 1 ≥ 0 ✓', 'verifica a condição')
    assert r[2] is True
    r = calc(c_matg, 'cond', ['y >= x - 1 e x <= 2', '3 1'])
    tem(r[0], 'x ≤ 2: 3 ≤ 2 ✗', 'não verifica')


def t_cond_disjuncao_e_igualdade():
    r = calc(c_matg, 'cond', ['x^2 + y^2 <= 4 ou y > 2', '3 0'])
    tem(r[0], 'x^2 + y^2 ≤ 4 ∨ y > 2', 'não verifica')
    r = calc(c_matg, 'cond', ['x^2 + y^2 <= 4 ou y > 2', '0 3'])
    assert r[2] is True
    r = calc(c_matg, 'cond', ['y = 2x + 1', '1 3'])
    tem(r[0], '3 = 3 ✓')


def t_cond_invalido():
    assert 'Falta um sinal' in erro(calc, c_matg, 'cond', ['y + x', ''])
    assert 'Falta um membro' in erro(calc, c_matg, 'cond', ['y >', ''])
    assert 'condição' in erro(calc, c_matg, 'cond', ['', ''])


def t_vet_operacoes():
    r = calc(c_matv, 'vet', ['3 -4', '-6 8', '2', '1 1', ''])
    tem(r[0], '‖u‖ = √(9 + 16) = 5', 'u + v = (-3, 4)', 'u - v = (9, -12)',
        'Colineares: v = (-2) u (sentidos opostos)', '2 u = (6, -8)',
        '‖2 u‖ = |2| × ‖u‖ = 10', 'A + u = (4, -3)')
    perto(r[2], 5)


def t_vet_ab_espaco():
    r = calc(c_matv, 'vet', ['', '', '', '1 2 3', '4 6 3'])
    tem(r[0], 'u = AB = B - A', 'u = (3, 4, 0)', '= 5')
    r = calc(c_matv, 'vet', ['1 2', '3 1', '-1/2', '', ''])
    tem(r[0], '√5 ≈ 2,2361', 'Não são colineares', '(-0,5) u = (-0,5; -1)')


def t_vet_nulo():
    r = calc(c_matv, 'vet', ['0 0', '1 2', '', '', ''])
    tem(r[0], 'vetor nulo', 'u + v = (1, 2)')
    assert 'colinear' not in r[0]
    assert r[2] == 0


def t_vet_invalido():
    assert 'mesmo número' in erro(calc, c_matv, 'vet', ['1 2', '1 2 3', '', '', ''])
    assert 'Escreve u' in erro(calc, c_matv, 'vet', ['', '', '', '1 1', ''])
    assert 'deixa B vazio' in erro(calc, c_matv, 'vet', ['1 2', '', '', '0 0', '1 1'])
    assert '2 ou 3' in erro(calc, c_matv, 'vet', ['1 2 3 4', '', '', '', ''])


def t_retav_pertence():
    r = calc(c_matv, 'retav', ['1 2', '2 3', '', '5 8'])
    tem(r[0], '(x, y) = (1, 2) + k (2, 3), k ∈ ℝ', 'm = u2 / u1 = 3 / 2 = 1,5',
        'y = 1,5x + 0,5', 'P pertence à reta (k = 2)')
    perto(r[2], 1.5)
    r = calc(c_matv, 'retav', ['0 1', '3 1', '', '6 4'])
    tem(r[0], '1 / 3 = 1/3 ≈ 0,3333', 'y = (1/3)x + 1', 'P não pertence')


def t_retav_dois_pontos_vertical():
    r = calc(c_matv, 'retav', ['1 2', '', '4 2', '0 0'])
    tem(r[0], 'k (3, 0)', 'y = 2', 'AP = (-1, -2) não é colinear')
    r = calc(c_matv, 'retav', ['1 2', '0 3', '', '1 -7'])
    tem(r[0], 'Reta vertical: x = 1 (sem declive)', 'P = A + (-3) u')
    assert r[2] is None
    r = calc(c_matv, 'retav', ['2 1', '-2 4', '', '2 1'])
    tem(r[0], '4 / (-2) = -2', 'y = -2x + 5', 'k = 0')


def t_retav_espaco():
    r = calc(c_matv, 'retav', ['1 2 3', '1 -1 2', '', '3 0 7'])
    tem(r[0], '(x, y, z) = (1, 2, 3) + k (1, -1, 2)', 'P pertence à reta (k = 2)')
    assert 'Declive' not in r[0]


def t_retav_invalido():
    assert 'nulo' in erro(calc, c_matv, 'retav', ['1 2', '0 0', '', ''])
    assert 'nulo' in erro(calc, c_matv, 'retav', ['1 2', '', '1 2', ''])
    assert 'não os dois' in erro(calc, c_matv, 'retav', ['1 2', '1 1', '3 3', ''])
    assert 'segundo ponto' in erro(calc, c_matv, 'retav', ['1 2', '', '', ''])
    assert 'mesmo número' in erro(calc, c_matv, 'retav', ['1 2', '1 1 1', '', ''])


def t_bar():
    r = calc(c_matv, 'bar', ['0 0', '6 0', '3 6'])
    tem(r[0], 'M (ponto médio de [BC]) = (4,5; 3)', 'G = A + 2/3 AM',
        '> G = (3, 2)', '(A + B + C) / 3 = (3, 2)')
    r = calc(c_matv, 'bar', ['0 0 0', '3 0 0', '0 3 3'])
    tem(r[0], 'G = (1, 1, 1)')


def t_bar_invalido():
    assert 'alinhados' in erro(calc, c_matv, 'bar', ['0 0', '1 1', '2 2'])
    assert 'alinhados' in erro(calc, c_matv, 'bar', ['1 1', '1 1', '2 3'])
    assert 'mesmo número' in erro(calc, c_matv, 'bar', ['0 0', '1 1 1', '2 3'])


def t_vot_todos():
    r = calc(c_matc, 'vot', ['10 8 7 4', 'ABC BCA CBA CAB', 0])
    tem(r[0], '29 votantes', 'Votos em 1.º lugar: A 10 · B 8 · C 11',
        'Maioria simples (relativa): C (11 votos)', 'mais de metade dos votos (14,5)',
        'A 53 · B 62 · C 59', 'Borda: B (62 pontos)',
        'Segunda volta entre C e A: C 19 · A 10', '1.ª contagem: A 10 · B 8 · C 11 → sai B',
        'Eliminação sucessiva: C (maioria absoluta)', 'A vs B: 14 - 15 → B',
        'Vencedor de Condorcet: B', 'vencedores diferentes')


def t_vot_maioria_absoluta():
    r = calc(c_matc, 'vot', ['60 40', 'AB BA', 0])
    tem(r[0], 'Maioria absoluta: A (60 > 50)', 'não é precisa', 'Borda: A (160 pontos)')
    assert 'diferentes' not in r[0]


def t_vot_empates():
    r = calc(c_matc, 'vot', ['5 5', 'AB BA', 0])
    tem(r[0], 'Maioria simples: empate entre A e B', 'Segunda volta: empate',
        'Borda: empate entre A e B', 'A vs B: 5 - 5 → empate', 'Não há vencedor de Condorcet')
    r = calc(c_matc, 'vot', ['1 1 1', 'ABC BCA CAB', 5])
    tem(r[0], 'A vs B: 2 - 1 → A', 'B vs C: 2 - 1 → B', 'A vs C: 1 - 2 → C',
        'Não há vencedor de Condorcet')
    r = calc(c_matc, 'vot', ['1 1 1', 'ABC BCA CAB', 4])
    tem(r[0], 'Eliminação sucessiva: empate entre A, B e C')


def t_vot_eliminacao():
    r = calc(c_matc, 'vot', ['6 4 2 2', 'ABCD BACD CBAD DCBA', 4])
    tem(r[0], 'sai C e D (empate no último lugar: saem todos)',
        '2.ª contagem: A 6 · B 8', 'Eliminação sucessiva: B')
    r = calc(c_matc, 'vot', ['6 4 2 2', 'abcd bacd cbad dcba', 3])
    tem(r[0], 'Segunda volta entre A e B: A 6 · B 8', 'Segunda volta: B')
    r = calc(c_matc, 'vot', ['5 4 4', 'ABC BAC CBA', 3])
    tem(r[0], 'empate no 2.º lugar da 1.ª volta (B e C)')


def t_vot_invalido():
    assert 'colunas' in erro(calc, c_matc, 'vot', ['10 8', 'ABC BCA CAB', 0])
    assert 'todos os candidatos' in erro(calc, c_matc, 'vot', ['1 1', 'ABC AB', 0])
    assert 'todos os candidatos' in erro(calc, c_matc, 'vot', ['1 1', 'ABC AAB', 0])
    assert 'inteiros' in erro(calc, c_matc, 'vot', ['2,5 1', 'AB BA', 0])
    assert 'Não há votantes' in erro(calc, c_matc, 'vot', ['0 0', 'AB BA', 0])
    assert 'pelo menos 2' in erro(calc, c_matc, 'vot', ['3', 'A', 0])
    assert 'letra' in erro(calc, c_matc, 'vot', ['3 2', 'A1 1A', 0])


def t_mand_hondt_empate_lei():
    r = calc(c_matc, 'mand', ['12000 9000 5000 3000', '7', '', 0])
    tem(r[0], 'A: 12 000; 6 000; 4 000; (3 000)', 'Ordem: A, B, A, C, B, A, D',
        'fica a lista com menos votos (Lei n.º 14/79, art. 16.º)',
        'Hondt: A 3 · B 2 · C 1 · D 1', 'A: 41,4% dos votos, 42,9% dos mandatos')
    r = calc(c_matc, 'mand', ['3000 1500', '2', '', 0])
    tem(r[0], 'Ordem: A, B', 'Hondt: A 1 · B 1', 'menos votos')


def t_mand_comparacao():
    r = calc(c_matc, 'mand', ['12000 8000 5000 2500', '7', '', 2])
    tem(r[0], 'Ordem: A, B, A, C, A, B, A', 'Hondt: A 4 · B 2 · C 1 · D 0',
        'Último mandato: A (3 000); quociente seguinte: 2 666,67',
        'A: 12 000; 4 000; 2 400; (1 714,29)', 'Ordem: A, B, C, A, B, D, A',
        'Sainte-Laguë: A 3 · B 2 · C 1 · D 1', 'resultados diferentes')
    assert 'Empate' not in r[0]


def t_mand_nomes_e_sem_solucao():
    r = calc(c_matc, 'mand', ['5100 3900 1000', '5', 'X Y Z', 1])
    tem(r[0], 'Sainte-Laguë (divisores 1, 3, 5, 7...)', 'Sainte-Laguë: X 3 · Y 2 · Z 0')
    r = calc(c_matc, 'mand', ['1000 1000', '1', '', 0])
    tem(r[0], 'a regra da lei não decide', 'Hondt: A 0 · B 0')


def t_mand_invalido():
    assert 'inteiros' in erro(calc, c_matc, 'mand', ['100 -5', '3', '', 0])
    assert 'inteiros' in erro(calc, c_matc, 'mand', ['10,5 3', '3', '', 0])
    assert 'mandatos' in erro(calc, c_matc, 'mand', ['100 50', '0', '', 0])
    assert 'mandatos' in erro(calc, c_matc, 'mand', ['100 50', '2,5', '', 0])
    assert 'nome para cada lista' in erro(calc, c_matc, 'mand', ['100 50', '3', 'P Q R', 0])
    assert 'Nenhuma lista' in erro(calc, c_matc, 'mand', ['0 0', '3', '', 0])


def t_sal_basico():
    r = calc(c_matd, 'sal', ['1000', '14', '40', '10', '', ''])
    tem(r[0], 'Segurança Social (11%): 1 000,00 € × 0,11 = 110,00 €',
        'Retenção na fonte de IRS (10%): 100,00 €',
        'Salário líquido mensal: 1 000,00 € - 210,00 € = 790,00 €',
        'Bruto anual: 14 × 1 000,00 € = 14 000,00 €', 'custo mensal 1 237,50 €',
        '(52 × 40) = 5,77 €')
    perto(r[2], 790)


def t_sal_horas_extra_e_limites():
    r = calc(c_matd, 'sal', ['1000', '14', '40', '', '', '2,5'])
    tem(r[0], '7,21 € + 11,90 € = 19,11 €')
    r = calc(c_matd, 'sal', ['1000', '14', '40', '', '', '0,5'])
    tem(r[0], 'seguintes + 37,5%: 3,61 €')
    r = calc(c_matd, 'sal', ['1500', '12', '35', '', '3,5', ''])
    tem(r[0], 'Outros descontos (3,5%): 52,50 €', '1 500,00 € - 217,50 € = 1 282,50 €',
        'Bruto anual: 12 × 1 500,00 € = 18 000,00 €', '(52 × 35) = 9,89 €')


def t_sal_invalido():
    assert 'positivo' in erro(calc, c_matd, 'sal', ['0', '14', '40', '', '', '']) or \
        'maior' in erro(calc, c_matd, 'sal', ['0', '14', '40', '', '', ''])
    assert 'meses' in erro(calc, c_matd, 'sal', ['1000', '13,5', '40', '', '', ''])
    assert 'horas por semana' in erro(calc, c_matd, 'sal', ['1000', '14', '70', '', '', ''])
    assert 'entre 0 e 100' in erro(calc, c_matd, 'sal', ['1000', '14', '40', '120', '', ''])
    assert 'maiores do que o salário' in erro(calc, c_matd, 'sal',
                                              ['1000', '14', '40', '95', '', ''])


def t_irs_escaloes():
    r = calc(c_matd, 'irs', ['20000', 0, '', '3000'])
    tem(r[0], '1.º escalão: 8 342,00 € × 12,5% = 1 042,75 €',
        '4.º escalão: 2 162,00 € × 24,1% = 521,04 €', 'Coleta: 3 343,47 €',
        'Escalão: 4.º (17 838 a 23 089 €); taxa marginal 24,1%', 'Taxa média',
        '20 000,00 × 24,1% - 1 476,53 = 3 343,47 €', 'IRS 2026', 'Lei n.º 73-A/2025',
        '343,47 €: a pagar')
    perto(r[2], 3343.469)
    assert len(r) == 5


def t_irs_limites():
    r = calc(c_matd, 'irs', ['8342', 0, '', ''])
    tem(r[0], 'Escalão: 1.º (até 8 342 €)', 'Coleta: 1 042,75 €', '= 12,5%')
    r = calc(c_matd, 'irs', ['86634', 0, '', ''])
    tem(r[0], 'Escalão: 8.º', '= 34,856%')
    r = calc(c_matd, 'irs', ['0', 0, '', ''])
    tem(r[0], 'Coleta: 0,00 €')


def t_irs_alto_e_manual():
    r = calc(c_matd, 'irs', ['100000', 0, '', ''])
    tem(r[0], '9.º escalão: 13 366,00 € × 48% = 6 415,68 €', 'Coleta: 36 612,73 €',
        'mais de 86 634 €', 'taxa adicional de solidariedade')
    r = calc(c_matd, 'irs', ['15000', 1, '12', '2000'])
    tem(r[0], 'Coleta: 15 000,00 € × 12% = 1 800,00 €', '-200,00 €: reembolso')
    assert len(r) == 4


def t_irs_invalido():
    assert 'rendimento' in erro(calc, c_matd, 'irs', ['-5', 0, '', ''])
    assert 'taxa manual' in erro(calc, c_matd, 'irs', ['1000', 1, '', ''])
    assert 'entre 0 e 100' in erro(calc, c_matd, 'irs', ['1000', 1, '150', ''])


def t_jur_simples():
    r = calc(c_matd, 'jur', ['1000', '3', '5', 1, '1', '28'])
    tem(r[0], '1 000,00 € × 3% × 5 = 150,00 €', 'Capital final: 1 150,00 €',
        'Juro líquido (imposto de 28%): 108,00 €')
    perto(r[2], 1150)


def t_jur_composto():
    r = calc(c_matd, 'jur', ['1000', '3', '5', 0, '12', '28'])
    tem(r[0], 'i = 3% / 12 = 0,25%; n = 60 períodos', 'Capital final: 1 161,62 €',
        'após 1 período: 1 002,50 €', 'Taxa anual efetiva: (1 + i)^12 - 1 = 3,042%',
        'capital 1 113,94 €', 'Em juro simples seria: 1 150,00 €')
    r = calc(c_matd, 'jur', ['1000', '3', '5', 0, '1', ''])
    tem(r[0], 'Capital final: 1 159,27 €')
    assert 'efetiva' not in r[0]
    r = calc(c_matd, 'jur', ['500', '0', '2', 0, '4', ''])
    tem(r[0], 'Capital final: 500,00 €; juro 0,00 €')


def t_jur_invalido():
    assert 'inteiro de períodos' in erro(calc, c_matd, 'jur', ['1000', '3', '1,3', 0, '1', ''])
    assert 'capital' in erro(calc, c_matd, 'jur', ['0', '3', '5', 0, '1', ''])
    assert 'entre 0 e 100' in erro(calc, c_matd, 'jur', ['1000', '-1', '5', 0, '1', ''])
    assert 'capitalizações' in erro(calc, c_matd, 'jur', ['1000', '3', '5', 0, '0', ''])


def t_prest():
    r = calc(c_matd, 'prest', [0, '10000', '', '6', '5', '12'])
    tem(r[0], 'i = 6% / 12 = 0,5%; n = 60 prestações', 'Prestação: 193,33 €',
        'Juros pagos: 1 599,68 €', '1.ª: juro 50,00 € · amortiza 143,33 € · fica 9 856,67 €')
    r = calc(c_matd, 'prest', [1, '', '200', '6', '5', '12'])
    tem(r[0], 'Valor atual: 10 345,11 €', 'Juros pagos: 1 654,89 €')
    r = calc(c_matd, 'prest', [0, '1200', '', '0', '1', '12'])
    tem(r[0], 'Prestação: 100,00 €', 'Juros pagos: 0,00 €')


def t_prest_invalido():
    assert 'empréstimo' in erro(calc, c_matd, 'prest', [0, '', '', '6', '5', '12'])
    assert 'prestação' in erro(calc, c_matd, 'prest', [1, '1000', '', '6', '5', '12'])
    assert 'prazo' in erro(calc, c_matd, 'prest', [0, '1000', '', '6', '0', '12'])
    assert 'por ano' in erro(calc, c_matd, 'prest', [0, '1000', '', '6', '5', '0'])


def t_uni_resumo():
    r = calc(c_mate, 'uni', ['2 4 4 5 7 8 9 9 9 25', '', '25', '', ''])
    tem(r[0], 'n = 10: 2 4 4 5 7 8 9 9 9 25', 'Média = 8,2', 'Moda: 9 (frequência 3)',
        'Mediana = 7,5', 'Q1 = 4 · Q3 = 9 (medianas das metades)', 'amplitude 23',
        'AIQ = Q3 - Q1 = 5', 'Variância ≈ 41,0667 · desvio padrão s ≈ 6,4083',
        'Q1 - 1,5 AIQ = -3,5 e Q3 + 1,5 AIQ = 16,5', 'Outliers: 25',
        'média ≈ 6,3333, mediana = 7', 'P25: 25% de 10 = 2,5 (posição seguinte); P25 = 4')
    perto(r[2], 8.2)
    assert len(r) == 5


def t_uni_impar_e_transformacao():
    r = calc(c_mate, 'uni', ['1 2 3 4 5 6 7 8 9', '', '25', '2', '3'])
    tem(r[0], 'Q1 = 2,5 · Q3 = 7,5 (medianas das metades, sem a mediana)',
        'Moda: não há', 'P25 = 3', 'P25 ≠ Q1', 'Com y = 2x + 3:', 'média = 13',
        's ≈ 5,4772; AIQ = 10', 'Sem outliers')


def t_uni_frequencias_e_limites():
    r = calc(c_mate, 'uni', ['10 20 30', '2 5 3', '90', '', ''])
    tem(r[0], 'n = 10: 10 10 20 20 20 20 20 30 30 30', 'Moda: 20 (frequência 5)',
        'Q1 = 20 · Q3 = 30', 'P90: 90% de 10 = 9 (inteiro: média de 2 dados); P90 = 30')
    r = calc(c_mate, 'uni', ['7 7', '', '', '', ''])
    tem(r[0], 'Moda: 7', 'AIQ = Q3 - Q1 = 0', 'desvio padrão s = 0', 'Sem outliers')


def t_uni_invalido():
    assert 'pelo menos 2' in erro(calc, c_mate, 'uni', ['5', '', '', '', ''])
    assert 'frequências' in erro(calc, c_mate, 'uni', ['1 2', '1', '', '', ''])
    assert 'inteiros' in erro(calc, c_mate, 'uni', ['1 2', '1 0,5', '', '', ''])
    assert 'entre 0 e 100' in erro(calc, c_mate, 'uni', ['1 2 3', '', '100', '', ''])


def t_cls_tabela():
    r = calc(c_mate, 'cls', ['0 10 20 30 40', '3 7 8 2', ''])
    tem(r[0], '[0, 10[: 5; 3; 15%; 3; 15%', '[30, 40]: 35; 2; 10%; 20; 100%', 'n = 20',
        'Média (com os pontos médios) = 19,5', 'Desvio padrão (aproximado) ≈ 8,8704',
        'Classe modal: [20, 30[', 'a mediana fica no limite 20')
    assert r[4][0] == 'Histograma'
    r = calc(c_mate, 'cls', ['0 10 20 30', '4 5 2', ''])
    tem(r[0], 'Classe mediana: [10, 20[')


def t_cls_dados_brutos_e_amplitudes():
    r = calc(c_mate, 'cls', ['0 10 20 40', '', '1 5 12 15 18 22 35 39 40'])
    tem(r[0], '[0, 10[: 5; 2; 22,2%', '[20, 40]: 30; 4; 44,4%; 9; 100%',
        'Classe modal: [10, 20[', 'amplitudes diferentes')
    r = calc(c_mate, 'cls', ['0 10 20', '', '10 10 0'])
    tem(r[0], '[0, 10[: 5; 1;', '[10, 20]: 15; 2;')


def t_cls_invalido():
    assert 'crescente' in erro(calc, c_mate, 'cls', ['0 20 10', '1 1', ''])
    assert 'classes e' in erro(calc, c_mate, 'cls', ['0 10 20', '1 2 3', ''])
    assert 'fora das classes' in erro(calc, c_mate, 'cls', ['0 10 20', '', '5 25'])
    assert 'não os dois' in erro(calc, c_mate, 'cls', ['0 10', '1', '5'])
    assert 'Não há dados' in erro(calc, c_mate, 'cls', ['0 10', '0', ''])


def t_caule():
    r = calc(c_mate, 'caule', ['12 15 21 23 23 30 38 41', '', 0])
    tem(r[0], '1 | 2 5', '2 | 1 3 3', '4 | 1', 'Legenda: 1 | 2 = 12',
        'A: n = 8, mínimo 12, mediana 23, máximo 41')
    r = calc(c_mate, 'caule', ['2,3 2,8 3,1 4,0 4,5', '', 1])
    tem(r[0], '2 | 3 8', '4 | 0 5', 'Legenda: 2 | 3 = 2,3')
    r = calc(c_mate, 'caule', ['5 31', '', 0])
    tem(r[0], '0 | 5', '1 | ', '3 | 1')


def t_caule_duplo():
    r = calc(c_mate, 'caule', ['12 15 21 23 23 30 38 41', '9 14 25 27 33 33 47', 0])
    tem(r[0], '  5 2 | 1 | 4', '3 3 1 | 2 | 5 7', 'B: n = 7, mínimo 9, mediana 27')


def t_caule_invalido():
    assert 'não negativos' in erro(calc, c_mate, 'caule', ['-3 5', '', 0])
    assert 'inteiros' in erro(calc, c_mate, 'caule', ['2,5 3', '', 0])
    assert 'uma casa decimal' in erro(calc, c_mate, 'caule', ['2,55 3', '', 1])
    assert 'Demasiados caules' in erro(calc, c_mate, 'caule', ['1 999', '', 0])
