# Testes do nucleo exato (m1_q) e dos resolvedores de Numeros
# (c_mnum, c_mrea): normal, limite e invalido.
import m1_q as Q
import c_mnum
import c_mrea
from base import calc, erro, tem, perto


def ok_erro(f, *a):
    try:
        f(*a)
    except ValueError as e:
        return str(e)
    raise AssertionError('esperava um erro')


def t_q_racionais():
    assert Q.R(6, -4) == (-3, 2)
    assert Q.add((1, 2), (1, 3)) == (5, 6)
    assert Q.div((1, 2), (-1, 4)) == (-2, 1)
    assert Q.pw((2, 3), -2) == (9, 4)
    assert Q.numq('2,5') == (5, 2) and Q.numq('1e-3') == (1, 1000)
    assert Q.dizima((1, 6)) == '0,1(6)' and Q.dizima((-22, 7)) == '-3,(142857)'
    assert Q.fstr(Q.fatores(360)) == '2³ × 3² × 5'
    assert 'zero' in ok_erro(Q.div, (1, 2), (0, 1))


def t_q_polinomios():
    p = Q.poli(Q.arvore('(2x - 3)^2 - (x + 1)(x - 1)'))
    assert Q.pstr(p) == '3x² - 12x + 10'
    assert Q.pstr(Q.poli(Q.arvore('(x-1)/2 + x/3'))) == '(5/6)x - 1/2'
    assert Q.pstr(Q.poli(Q.arvore('(a+b)^3'))) == 'a³ + 3a²b + 3ab² + b³'
    assert Q.pstr(Q.poli(Q.arvore('x - x'))) == '0'
    assert Q.raizes_rac([Q.R(-2), Q.R(-3), Q.R(2)]) == [(-1, 2), (2, 1)]
    assert Q.valor(p, {'x': (1, 1)}) == (1, 1)


def t_q_leitura_invalida():
    assert 'sinal' in ok_erro(Q.arvore, '2 3')
    assert 'parêntese' in ok_erro(Q.arvore, '(x+1')
    assert 'desconhecido' in ok_erro(Q.arvore, 'x$2')
    assert 'acaba' in ok_erro(Q.arvore, '3+')
    assert 'polinómio' in ok_erro(Q.poli, Q.arvore('1/x'))
    assert 'longa' in ok_erro(Q.arvore, '1+' * 120 + '1')


def t_frac_passos():
    r = calc(c_mnum, 'frac', ['1/2 + 3/4 × (2/3 - 1)', ''])
    tem(r[0], '1. 2/3 - 1 = 2/3 - 3/3 = -1/3', '3/4 × (-1/3) = -3/12 = -1/4',
        '1/2 + (-1/4) = 2/4 + (-1/4) = 1/4', '> = 1/4', 'Em dízima: 0,25')
    perto(r[2], 0.25)
    r = calc(c_mnum, 'frac', ['3 : 2/5 - 1/2 × 4', ''])
    tem(r[0], '3 : 2/5 = 3 × 5/2 = 15/2', '15/2 - 2 = 15/2 - 4/2 = 11/2',
        'Numeral misto: 5 e 1/2')


def t_frac_sinais_potencias():
    r = calc(c_mnum, 'frac', ['-2/3 - (-5/6) : 1/2 + (1/2)^2', ''])
    tem(r[0], '-5/6 : 1/2 = -5/6 × 2 = -5/3', '(1/2)² = 1/4', '> = 5/4')
    r = calc(c_mnum, 'frac', ['7/3', ''])
    tem(r[0], '> = 7/3', '2,(3)', 'Numeral misto: 2 e 1/3')
    assert 'Pela ordem' not in r[0]


def t_frac_ordenar():
    r = calc(c_mnum, 'frac', ['', '-1/2 0,4 -0,5 2/5 1/3'])
    tem(r[0], 'Por ordem crescente: -1/2 = -0,5 < 1/3 < 0,4 = 2/5')
    assert r[2] is None


def t_frac_invalido():
    assert 'só para números' in erro(calc, c_mnum, 'frac', ['2x + 1', ''])
    assert 'zero' in erro(calc, c_mnum, 'frac', ['1/2 : (1 - 1)', ''])
    assert 'Escreve' in erro(calc, c_mnum, 'frac', ['', ''])
    assert 'dois números' in erro(calc, c_mnum, 'frac', ['', '3'])


def t_pot_regras():
    r = calc(c_mnum, 'pot', ['2^3 × 2^4 : 2^5'])
    tem(r[0], '2^(3 + 4 - 5) = 2²', 'Valor: 128 : 32 = 4', '> = 4')
    r = calc(c_mnum, 'pot', ['(2^3)^2 × 5^6'])
    tem(r[0], '(2³)² = 2^(3 × 2) = 2⁶', '2⁶ × 5⁶ = (2 × 5)⁶ = 10⁶', '> = 1000000')
    r = calc(c_mnum, 'pot', ['(-3)^2 × (-3)^-4'])
    tem(r[0], '(-3)^(2 - 4) = (-3)⁻²', '> = 1/9')


def t_pot_letras_e_limites():
    r = calc(c_mnum, 'pot', ['a^5 × a^-2 : a'])
    tem(r[0], 'a^(5 - 2 - 1) = a²', '> a²')
    r = calc(c_mnum, 'pot', ['7^0'])
    tem(r[0], '> = 1')
    assert 'negativo' in erro(calc, c_mnum, 'pot', ['0^-2'])
    assert 'inteiro' in erro(calc, c_mnum, 'pot', ['2^(1/2)'])
    assert 'Escreve' in erro(calc, c_mnum, 'pot', [''])


def t_mdc():
    r = calc(c_mnum, 'mdc', ['84 120'])
    tem(r[0], '84 = 2² × 3 × 7', '> m.d.c. = 2² × 3 = 12',
        '> m.m.c. = 2³ × 3 × 5 × 7 = 840', '84/120 simplificada (: 12): 7/10')
    assert r[2] == 12
    r = calc(c_mnum, 'mdc', ['12 18 30'])
    tem(r[0], 'm.d.c. = 2 × 3 = 6', 'm.m.c. = 2² × 3² × 5 = 180')
    r = calc(c_mnum, 'mdc', ['97'])
    tem(r[0], '97 = 97 (primo)', 'Divisores (2): 1, 97')
    r = calc(c_mnum, 'mdc', ['8 15'])
    tem(r[0], 'primos entre si')


def t_mdc_invalido():
    assert 'inteiros positivos' in erro(calc, c_mnum, 'mdc', ['12 0'])
    assert 'inteiros positivos' in erro(calc, c_mnum, 'mdc', ['2,5 3'])
    assert 'máximo 6' in erro(calc, c_mnum, 'mdc', ['1 2 3 4 5 6 7'])


def t_dec():
    r = calc(c_mnum, 'dec', ['7/12'])
    tem(r[0], 'Dízima: 0,58(3)', 'Denominador 12 = 2² × 3', 'período 3')
    r = calc(c_mnum, 'dec', ['1,2(45)'])
    tem(r[0], '10 d = 12,(45)', '10³ d = 1245,(45)', '990 d = 1233',
        'd = 1233/990 = 137/110')
    r = calc(c_mnum, 'dec', ['0,375'])
    tem(r[0], '0,375 = 3/8', 'dízima finita')
    r = calc(c_mnum, 'dec', ['0,(9)'])
    tem(r[0], 'd = 9/9 = 1')
    r = calc(c_mnum, 'dec', ['-0,(3)'])
    tem(r[0], '10 d = -3,(3)', 'd = -3/9 = -1/3')


def t_dec_invalido():
    assert 'período entre' in erro(calc, c_mnum, 'dec', ['0,1(2'])
    assert 'Escreve' in erro(calc, c_mnum, 'dec', [''])
    assert 'mal escrita' in erro(calc, c_mnum, 'dec', ['0,a(3)'])


def t_ncie():
    r = calc(c_mrea, 'ncie', ['0,00052', '', 0])
    tem(r[0], 'A = 5,2 × 10⁻⁴')
    r = calc(c_mrea, 'ncie', ['52 300 000', '4 × 10^-3', 1])
    tem(r[0], 'A = 5,23 × 10⁷', '(5,23 × 4) × 10^(7 + (-3))', '= 20,92 × 10⁴',
        '> 2,092 × 10⁵')
    perto(r[2], 209200)
    r = calc(c_mrea, 'ncie', ['3,2e5', '8e-2', 2])
    tem(r[0], '= 0,4 × 10⁷', '> 4 × 10⁶')
    r = calc(c_mrea, 'ncie', ['4,5 × 10^6', '3,2 × 10^5', 3])
    tem(r[0], 'Mesma potência de 10: 4,5 × 10⁶ + 0,32 × 10⁶', '> 4,82 × 10⁶')


def t_ncie_invalido():
    assert '0 não se escreve' in erro(calc, c_mrea, 'ncie', ['0', '', 0])
    assert 'letras' in erro(calc, c_mrea, 'ncie', ['2x', '', 0])
    assert 'O resultado é 0' in erro(calc, c_mrea, 'ncie', ['5', '5', 4])
    assert 'Escreve' in erro(calc, c_mrea, 'ncie', ['3', '', 1])


def t_rad_simplificar():
    r = calc(c_mrea, 'rad', ['√50 + 2√8 - √18'])
    tem(r[0], '√50 = √(25 × 2) = 5√2', '√8 = √(4 × 2) = 2√2', '> 6√2',
        'irracional')
    r = calc(c_mrea, 'rad', ['√40'])
    tem(r[0], '> 2√10', '6 < √40 < 7 (36 < 40 < 49)', '6,3 < √40 < 6,4')
    r = calc(c_mrea, 'rad', ['√(2/3)'])
    tem(r[0], '√(2/3) = √6/3', '> √6/3')
    assert '√6/3 = √6/3' not in r[0]


def t_rad_racionalizar_e_cubica():
    r = calc(c_mrea, 'rad', ['6/√3'])
    tem(r[0], 'por √3 (o denominador fica 3)', '> 2√3')
    r = calc(c_mrea, 'rad', ['2/(1 + √3)'])
    tem(r[0], 'por 1 - √3 (o denominador fica -2)', '> -1 + √3')
    r = calc(c_mrea, 'rad', ['(1 + √2)^2'])
    tem(r[0], '> 3 + 2√2')
    r = calc(c_mrea, 'rad', ['∛54'])
    tem(r[0], '∛54 = 3∛2')
    r = calc(c_mrea, 'rad', ['∛-27'])
    tem(r[0], '= -3 (cubo perfeito)')
    r = calc(c_mrea, 'rad', ['√49'])
    tem(r[0], '> 7')
    assert 'irracional' not in r[0]


def t_rad_invalido():
    assert 'negativo' in erro(calc, c_mrea, 'rad', ['√-4'])
    assert 'sozinha' in erro(calc, c_mrea, 'rad', ['2∛54'])
    assert 'letras' in erro(calc, c_mrea, 'rad', ['√x'])
    assert 'zero' in erro(calc, c_mrea, 'rad', ['1/(√2 - √2)'])


def t_intv():
    r = calc(c_mrea, 'intv', ['[-2, 5[', ']3, +inf['])
    tem(r[0], 'A = [-2, 5[: -2 ≤ x < 5', '> A ∩ B = ]3, 5[ (3 < x < 5)',
        '> A ∪ B = [-2, +∞[', 'Números inteiros em A ∩ B: 4 (1)')
    assert r[4][0] == 'Na reta real'
    r = calc(c_mrea, 'intv', [']-inf; 1,5]', '[1,5; 4]'])
    tem(r[0], 'A ∩ B = {1,5} (x = 1,5)', 'A ∪ B = ]-∞, 4]')
    r = calc(c_mrea, 'intv', ['[0, 2]', ']3, 5]'])
    tem(r[0], 'A ∩ B = ∅', 'A ∪ B = [0, 2] ∪ ]3, 5]')
    r = calc(c_mrea, 'intv', ['[-3, 3]', ''])
    tem(r[0], '-3, -2, -1, 0, 1, 2, 3 (7)', 'Amplitude: 6')
    r = calc(c_mrea, 'intv', ['[0, 2[', '[2, 3]'])
    tem(r[0], 'A ∩ B = ∅', 'A ∪ B = [0, 3]')


def t_intv_invalido():
    assert 'menor' in erro(calc, c_mrea, 'intv', ['[5, 2]', ''])
    assert 'assim' in erro(calc, c_mrea, 'intv', ['2 < x', ''])
    assert 'dois extremos' in erro(calc, c_mrea, 'intv', ['[1,5, 3]', ''])
    assert 'trocados' in erro(calc, c_mrea, 'intv', ['[+inf, 3]', ''])
