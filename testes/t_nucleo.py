# Testes do nucleo: formatacao, leitura de numeros, expressoes, exatos,
# unidades e verificacao de respostas.
import m1_nucleo as N
from base import erro, perto


def t_fmt_sig():
    assert N.fmt2(2.675, 3) == ('2,68', False)
    assert N.fmt2(0.025, 3) == ('0,0250', True)
    assert N.fmt(6.02214076e23, 3) == '6,02 × 10²³'
    assert N.fmt(1534, 2) == '1,5 × 10³'
    assert N.fmt(1534, 4) == '1534'
    assert N.fmt(9.996, 3) == '10,0'
    assert N.fmt(0.00025, 2) == '2,5 × 10⁻⁴'
    assert N.fmt(-2.5, 2) == '-2,5'
    assert N.fmt(0, 3) == '0,00'


def t_fmt_dec():
    assert N.fmt(1 / 3) == '0,3333'
    assert N.fmt(2.5) == '2,5'
    assert N.fmt(0.1 + 0.2) == '0,3'
    assert N.fmt(1e13) == '1 × 10¹³'
    assert N.fmt(3.0) == '3'
    assert N.fix(2.5, 2) == '2,50'
    assert N.eq(98.08000000000001, 0, 2) == '= 98,08'
    assert N.eq(1 / 3, 0, 2) == '≈ 0,33'
    assert N.fmt(2.5, 0, 12) == '2,5'


def t_num_ok():
    assert N.num('2,5') == (2.5, 2)
    assert N.num('0,0250') == (0.025, 3)
    assert N.num('6,02e23')[1] == 3
    perto(N.num('6,02x10^23')[0], 6.02e23)
    perto(N.num('6,02×10²³')[0], 6.02e23)
    perto(N.num('1,60 × 10⁻¹⁹')[0], 1.6e-19)
    assert N.num('3/4') == (0.75, 0)
    assert N.num('+0,50') == (0.5, 2)
    assert N.num('-3')[0] == -3.0
    perto(N.num('2π')[0], 6.283185307179586)


def t_num_erros():
    assert 'Escreve' in erro(N.num, '')
    assert 'mal escrito' in erro(N.num, '2..3')
    assert 'mal escrito' in erro(N.num, '3,')
    assert 'desconhecido: a' in erro(N.num, 'a')
    assert 'expoente' in erro(N.num, '1e')
    assert 'grande' in erro(N.num, '1e400')
    assert 'grande' in erro(N.num, '1e300*1e300')


def t_expr():
    def v(s, x=0.0):
        return N.ev(N.comp(s), x)
    perto(v('2x^2-3x+1', 2.0), 3.0)
    perto(v('-x^2', 3.0), -9.0)
    perto(v('2^-1'), 0.5)
    perto(v('sin(30)^2'), 0.25)
    perto(v('sen 30 + cos 60'), 1.0)
    perto(v('|x-5|', 2.0), 3.0)
    perto(v('2|x|+1', -3.0), 7.0)
    perto(v('x²+1', 3.0), 10.0)
    perto(v('3(x+1)(x-1)', 2.0), 9.0)
    perto(v('√(x+7)', 2.0), 3.0)
    perto(v('2^3^2'), 512.0)
    perto(v('8/2/2'), 2.0)
    perto(v('(-8)^(1/3)'), -2.0)
    perto(v('tg 45'), 1.0)
    perto(v('2,5x', 2.0), 5.0)
    perto(v('2×3÷4'), 1.5)


def t_expr_erros():
    assert 'fechar' in erro(N.comp, '(2+3')
    assert 'a mais' in erro(N.comp, '2+3)')
    assert 'desconhecido: y' in erro(N.comp, 'y+1')
    assert 'no fim' in erro(N.comp, '2+')
    assert 'longa' in erro(N.comp, '1+' * 101)
    assert 'parênteses'.replace('ê', 'ê') in erro(N.comp, '(' * 21 + '1' + ')' * 21) \
        or 'Demasiados' in erro(N.comp, '(' * 21 + '1' + ')' * 21)
    assert 'zero' in erro(N.ev, N.comp('1/x'), 0.0)
    assert 'negativo' in erro(N.ev, N.comp('sqrt(x)'), -1.0)
    assert 'Tangente' in erro(N.ev, N.comp('tan(x)'), 90.0)


def t_exatos():
    assert N.exact(2 / 3) == '2/3'
    assert N.exact(2 * 3 ** 0.5 / 3) == '2√3/3'
    assert N.exact(3.141592653589793 / 2) == 'π/2'
    assert N.exact(1.234567) is None
    assert N.exact(1025.4142135623731) is None
    assert N.rad(72) == (6, 2)
    assert N.rhs(2.0 ** 0.5) == '= √2 ≈ 1,4142'
    assert N.rhs(0.5) == '= 0,5'


def t_unidades():
    perto(N.conv(25, '°C', 'K'), 298.15)
    perto(N.conv(1, 'kWh', 'J'), 3.6e6)
    perto(N.conv(250, 'mL', 'dm³'), 0.25)
    perto(N.conv(36, 'km/h', 'm/s'), 10.0)
    perto(N.conv(2, 'g/cm³', 'kg/m³'), 2000.0)
    perto(N.conv(1, 'atm', 'hPa'), 1013.25)
    assert 'diferentes' in erro(N.conv, 1, 'm', 'kg')
    assert 'desconhecida' in erro(N.tobase, 1, 'xpto', 'L')


def t_check():
    assert N.check('0,5', 0.5)
    assert N.check('1/2', 0.5)
    assert N.check('5e-1', 0.5)
    assert N.check('5x10^-1', 0.5)
    assert N.check('5 × 10⁻¹', 0.5)
    assert not N.check('0,51', 0.5)
    assert N.check('2,46', 2.4567, 'd2')
    assert not N.check('2,45', 2.4567, 'd2')
    assert N.check('6,02e23', 6.0221e23, 's3')
    assert N.check('0', 0.0)


def t_lista():
    assert N.lst('2,5; 3,1;4') == ['2,5', '3,1', '4']
    assert N.lst('2,5 3,1') == ['2,5', '3,1']
    assert N.lst('6,02 × 10²³; 1') == ['6,02 × 10²³', '1']
