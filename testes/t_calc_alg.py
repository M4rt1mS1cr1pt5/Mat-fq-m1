# Testes dos resolvedores de Algebra (c_mexp, c_mpol, c_mprp): normal,
# limite e invalido.
import c_mexp
import c_mpol
import c_mprp
from base import calc, erro, tem, perto


def t_eq1_passos():
    r = calc(c_mexp, 'eq1', ['3(x - 2) + 4 = 2x - 1', ''])
    tem(r[0], 'Sem parênteses: 3x - 2 = 2x - 1',
        'Termos com x no 1.º membro: 3x - 2x = -1 + 2', '> x = 1 ; C.S. = {1}',
        'Verificação: 1.º membro = 1 e 2.º membro = 1 ✓')
    perto(r[2], 1)
    r = calc(c_mexp, 'eq1', ['(x - 1)/2 + x/3 = 4', ''])
    tem(r[0], '× 6 (m.m.c. dos denominadores): 5x - 3 = 24', '5x = 27',
        'x = 27/5 ; C.S. = {5,4}', '✓')


def t_eq1_casos():
    r = calc(c_mexp, 'eq1', ['2(x + 1) = 2x + 2', ''])
    tem(r[0], '0x = 0: equação possível e indeterminada; C.S. = ℝ')
    r = calc(c_mexp, 'eq1', ['2x + 1 = 2x + 5', ''])
    tem(r[0], '0x = 4: equação impossível; C.S. = ∅')
    assert 'Sem parênteses' not in r[0]
    r = calc(c_mexp, 'eq1', ['5 - 2x = 11', ''])
    tem(r[0], 'Dividindo por (-2): x = 6 : (-2)', '> x = -3')


def t_eq1_literal():
    r = calc(c_mexp, 'eq1', ['A = b*h/2', 'h'])
    tem(r[0], 'Simplificando: A = (1/2)bh',
        '× 2 (m.m.c. dos denominadores): 2A = bh',
        'Trocando os membros: bh = 2A', '> h = 2A / b (se b ≠ 0)')
    assert 'Reduzindo' not in r[0] and 'Multiplicando' not in r[0]
    r = calc(c_mexp, 'eq1', ['12 = 3x', ''])
    tem(r[0], 'Trocando os membros: 3x = 12', '> x = 4')
    r = calc(c_mexp, 'ineq', ['5 < 2x + 1', '', 0])
    tem(r[0], 'Trocando os membros: 2x + 1 > 5', 'C.S. = ]2, +∞[')
    r = calc(c_mexp, 'sis', ['x = 2y - 1', '3x + y = 11'])
    tem(r[0], 'x = 2 × 2 - 1 = 3')
    r = calc(c_mexp, 'eq1', ['a x + b = c', 'x'])
    tem(r[0], 'x = (-b + c) / a (se a ≠ 0)')


def t_eq1_invalido():
    assert 'incógnita' in erro(calc, c_mexp, 'eq1', ['A = b*h/2', ''])
    assert '2.º grau' in erro(calc, c_mexp, 'eq1', ['x^2 - 5x + 6 = 0', ''])
    assert 'um só sinal' in erro(calc, c_mexp, 'eq1', ['x + 1 < 3', ''])
    assert 'Falta um membro' in erro(calc, c_mexp, 'eq1', ['x + 1 = ', ''])
    assert 'nenhuma letra' in erro(calc, c_mexp, 'eq1', ['2 + 3 = 5', ''])


def t_ineq():
    r = calc(c_mexp, 'ineq', ['3 - 2x >= 7', '', 0])
    tem(r[0], '-2x ≥ 4', 'Dividindo por (-2) (negativo), o sinal inverte-se: '
        'x ≤ -2', '> C.S. = ]-∞, -2]')
    r = calc(c_mexp, 'ineq', ['-2 < 3x + 1 <= 7', '', 0])
    tem(r[0], 'Inequação dupla', '> C.S. = ]-1, 2]')


def t_ineq_ligacoes():
    r = calc(c_mexp, 'ineq', ['x + 1 > 3', '2x <= 10', 0])
    tem(r[0], 'Interseção (e):', '> C.S. = ]2, 5]')
    r = calc(c_mexp, 'ineq', ['x < -1', 'x > 2', 1])
    tem(r[0], '> C.S. = ]-∞, -1[ ∪ ]2, +∞[')
    r = calc(c_mexp, 'ineq', ['2x + 1 > 2x', '', 0])
    tem(r[0], '0 > -1 é sempre verdade')
    r = calc(c_mexp, 'ineq', ['x > 3', 'x < 1', 0])
    tem(r[0], '> C.S. = ∅')


def t_ineq_invalido():
    assert '<, >' in erro(calc, c_mexp, 'ineq', ['2x = 4', '', 0])
    assert 'letras x, y' in erro(calc, c_mexp, 'ineq', ['x < y', '', 0])
    assert 'Escreve' in erro(calc, c_mexp, 'ineq', ['', '', 0])


def t_sis():
    r = calc(c_mexp, 'sis', ['x + y = 5', '2x - y = 1'])
    tem(r[0], 'Da 1.ª equação: x = -y + 5', 'Substituindo na 2.ª: 2(-y + 5) - y = 1',
        'Reduzindo: -3y = -9', '> (x, y) = (2, 3); possível e determinado',
        'Verificação nas duas equações: ✓ e ✓')
    assert r[4][0] == 'Sistema: as duas retas'
    r = calc(c_mexp, 'sis', ['2x + 3y = 12', '3x - 2y = 5'])
    tem(r[0], 'x = -(3/2)y + 6', '(x, y) = (3, 2)', '✓ e ✓')
    r = calc(c_mexp, 'sis', ['3x + 2y = 7', '-x + y = 1'])
    tem(r[0], 'Da 2.ª equação: x = y - 1', '(x, y) = (1, 2)')


def t_sis_casos():
    r = calc(c_mexp, 'sis', ['x + y = 2', '2x + 2y = 4'])
    tem(r[0], 'possível e indeterminado')
    r = calc(c_mexp, 'sis', ['x + y = 2', 'x + y = 5'])
    tem(r[0], 'sistema impossível (as retas são paralelas)')
    r = calc(c_mexp, 'sis', ['y = 2x - 1', 'x = 3'])
    tem(r[0], '(x, y) = (3, 5)', '✓ e ✓')
    r = calc(c_mexp, 'sis', ['x/2 + y/3 = 1', 'x - y = 2'])
    tem(r[0], '1.ª: 3x + 2y = 6', '(x, y) = (2, 0)')


def t_sis_invalido():
    assert 'duas incógnitas' in erro(calc, c_mexp, 'sis', ['x = 2', 'x + 1 = 3'])
    assert '1.º grau' in erro(calc, c_mexp, 'sis', ['xy = 2', 'x + y = 3'])
    assert 'um só' in erro(calc, c_mexp, 'sis', ['x + y', 'x - y = 1'])
    assert 'Escreve a 2.ª' in erro(calc, c_mexp, 'sis', ['x + y = 1', ''])


def t_pol():
    r = calc(c_mpol, 'pol', ['(2x - 3)^2 - (x + 1)(x - 1)', ''])
    tem(r[0], '(2x - 3)^2 = 4x² - 12x + 9  (quadrado do binómio',
        '(x + 1)(x - 1) = x² - 1  (diferença de quadrados', '> 3x² - 12x + 10',
        'Grau: 2; termo independente: 10')
    r = calc(c_mpol, 'pol', ['3x(x - 2) + (x + 4)^2', '2'])
    tem(r[0], '3x(x - 2) = 3x² - 6x  (propriedade distributiva)',
        '> 4x² + 2x + 16', 'Valor para x = 2: 36')
    perto(r[2], 36)


def t_pol_limites():
    r = calc(c_mpol, 'pol', ['(a + b)(a - b) + 2ab', ''])
    tem(r[0], '> a² + 2ab - b²')
    r = calc(c_mpol, 'pol', ['x - x', ''])
    tem(r[0], '> 0', 'polinómio nulo')
    assert 'uma letra' in erro(calc, c_mpol, 'pol', ['a + b', '2'])
    assert 'polinómio' in erro(calc, c_mpol, 'pol', ['1/x', ''])


def t_fat():
    r = calc(c_mpol, 'fat', ['x^3 - 4x'])
    tem(r[0], 'Fator comum: x, logo x³ - 4x = x(x² - 4)', '> x³ - 4x = x(x - 2)(x + 2)')
    r = calc(c_mpol, 'fat', ['x^2 - 6x + 9'])
    tem(r[0], '> x² - 6x + 9 = (x - 3)²')
    r = calc(c_mpol, 'fat', ['-x^2 + 4'])
    tem(r[0], 'Sinal - em evidência', '> -x² + 4 = -(x - 2)(x + 2)')
    r = calc(c_mpol, 'fat', ['6a^2b + 9ab^2'])
    tem(r[0], '> 3ab(2a + 3b)')


def t_fat_equacoes():
    r = calc(c_mpol, 'fat', ['2x^2 - 3x - 2 = 0'])
    tem(r[0], '> 2x² - 3x - 2 = (x - 2)(2x + 1)', '> C.S. = {-0,5; 2}')
    r = calc(c_mpol, 'fat', ['x^2 = 5x'])
    tem(r[0], 'x(x - 5)', '> C.S. = {0; 5}')
    r = calc(c_mpol, 'fat', ['6x^3 - 7x^2 - x + 2 = 0'])
    tem(r[0], 'x = -1/2 é zero', '(2x + 1)(x - 1)(3x - 2)', 'C.S. = {-0,5; 2/3; 1}')
    r = calc(c_mpol, 'fat', ['x^2 - 2x - 1 = 0'])
    tem(r[0], '(x - (1 + √2))(x - (1 - √2))', 'C.S. = {1 - √2; 1 + √2}')
    r = calc(c_mpol, 'fat', ['x^2 + 1 = 0'])
    tem(r[0], 'não tem zeros reais', 'C.S. = ∅')


def t_fat_invalido():
    assert 'nulo' in erro(calc, c_mpol, 'fat', ['x - x'])
    assert 'uma letra' in erro(calc, c_mpol, 'fat', ['a + b = 0'])
    assert 'Só um sinal' in erro(calc, c_mpol, 'fat', ['x = 1 = 2'])
    assert 'Escreve' in erro(calc, c_mpol, 'fat', [''])


def t_ruf():
    r = calc(c_mpol, 'ruf', ['2x^3 - 3x^2 + 4', 'x - 2'])
    tem(r[0], 'Coeficientes de D (os que faltam são 0): 2, -3, 0, 4',
        '-3 + 2 × 2 = 1', '4 + 2 × 2 = 8 (resto)', 'Teorema do resto: D(2) = 8',
        '> Quociente: 2x² + x + 2 ; resto: 8', 'Confirmação: ✓')
    r = calc(c_mpol, 'ruf', ['x^3 - 1', 'x - 1'])
    tem(r[0], 'resto: 0', 'x - 1 é um fator de x³ - 1')


def t_ruf_outros():
    r = calc(c_mpol, 'ruf', ['4x^3 - 2x + 1', '2x + 1'])
    tem(r[0], 'Regra de Ruffini com -1/2', 'divide-se o quociente por 2',
        '> Quociente: 2x² - x - 1/2 ; resto: 3/2', 'Confirmação: ✓')
    r = calc(c_mpol, 'ruf', ['x^4 + x^2 + 1', 'x^2 + x + 1'])
    tem(r[0], '> Quociente: x² - x + 1 ; resto: 0', 'Confirmação: ✓')
    r = calc(c_mpol, 'ruf', ['x + 1', 'x^2 + 1'])
    tem(r[0], '> Quociente: 0 ; resto: x + 1')


def t_ruf_invalido():
    assert 'nulo' in erro(calc, c_mpol, 'ruf', ['x^2', '0'])
    assert 'uma letra' in erro(calc, c_mpol, 'ruf', ['x^2 + 1', 'y - 1'])
    assert 'Escreve' in erro(calc, c_mpol, 'ruf', ['x', ''])


def t_seq():
    r = calc(c_mprp, 'seq', ['3 7 11 15', '10', '39'])
    tem(r[0], 'Diferenças entre termos seguidos: 4, 4, 4', 'u(n+1) = u(n) + 4',
        '> Termo geral: u(n) = 4n - 1', 'u₁₀ = 39', '39 é termo: é o termo de ordem 10')
    r = calc(c_mprp, 'seq', ['5 2 -1', '', '-12'])
    tem(r[0], 'u(n) = -3n + 8', '-12 não é termo')


def t_seq_outras():
    r = calc(c_mprp, 'seq', ['1 4 9 16 25', '12', '100'])
    tem(r[0], 'Segundas diferenças constantes (2)', 'u(n) = n²', 'u₁₂ = 144',
        'termo de ordem 10')
    r = calc(c_mprp, 'seq', ['2 6 18 54', '6', '486'])
    tem(r[0], 'Razão constante 3', 'u(n) = 2 × 3^(n - 1)', 'u₆ = 486')
    r = calc(c_mprp, 'seq', ['1 2 4 7', '', ''])
    tem(r[0], 'u(n) = (1/2)n² - (1/2)n + 1', 'Confirmação com os termos dados: ✓')


def t_seq_invalido():
    assert 'regra simples' in erro(calc, c_mprp, 'seq', ['1 5 2 8', '', ''])
    assert 'pelo menos 3' in erro(calc, c_mprp, 'seq', ['1 2', '', ''])
    assert 'inteiro positivo' in erro(calc, c_mprp, 'seq', ['1 2 3', '0', ''])
    assert 'só números' in erro(calc, c_mprp, 'seq', ['1 2 x', '', ''])


def t_prop():
    r = calc(c_mprp, 'prop', ['2 3 5 ?', '6 9 ? 21'])
    tem(r[0], 'k = y/x = 3; y = 3x', 'y = k × x = 3 × 5 = 15', 'x = y : k = 21 : 3 = 7',
        'Tabela: (2, 6); (3, 9); (5, 15); (7, 21)')
    perto(r[2], 3)
    r = calc(c_mprp, 'prop', ['1 2 3', '2 5 6'])
    tem(r[0], 'não são diretamente proporcionais')
    r = calc(c_mprp, 'prop', ['4 ?', '1 2,5'])
    tem(r[0], 'k = y/x = 1/4', 'x = y : k = 5/2 : 1/4 = 10')


def t_prop_invalido():
    assert 'x = 0' in erro(calc, c_mprp, 'prop', ['0 1', '2 3'])
    assert 'par (x, y) completo' in erro(calc, c_mprp, 'prop', ['? 2', '3 ?'])
    assert 'valores de x e' in erro(calc, c_mprp, 'prop', ['1 2', '3'])
    assert 'faltam os dois' in erro(calc, c_mprp, 'prop', ['1 ?', '2 ?'])


def t_inv():
    r = calc(c_mprp, 'inv', ['2 4 5 ?', '10 5 ? 2'])
    tem(r[0], 'k = x × y = 20; y = 20/x', 'y = k : x = 20 : 5 = 4',
        'x = k : y = 20 : 2 = 10')
    perto(r[2], 20)
    r = calc(c_mprp, 'inv', ['1 2', '6 4'])
    tem(r[0], 'não são inversamente proporcionais')
    assert 'y = 0' in erro(calc, c_mprp, 'inv', ['2 ?', '3 0'])


def t_perc():
    tem(calc(c_mprp, 'perc', [0, '80', '', '15'])[0], '15% de 80 = 0,15 × 80 = 12')
    tem(calc(c_mprp, 'perc', [1, '12', '48', ''])[0], '12 é 25% de 48')
    tem(calc(c_mprp, 'perc', [2, '50', '', '20'])[0], '50 × 1,2 = 60')
    tem(calc(c_mprp, 'perc', [3, '120', '', '25'])[0], '120 × 0,75 = 90')
    tem(calc(c_mprp, 'perc', [4, '61,5', '', '23'])[0], '61,5 : 1,23 = 50')
    tem(calc(c_mprp, 'perc', [5, '90', '', '25'])[0], '90 : 0,75 = 120')
    tem(calc(c_mprp, 'perc', [6, '300', '255', ''])[0], 'Variação: -15% (diminuição)')
    tem(calc(c_mprp, 'perc', [1, '1', '3', ''])[0], '≈ 33,33%')


def t_perc_invalido():
    assert 'menor do que 100%' in erro(calc, c_mprp, 'perc', [3, '50', '', '100'])
    assert 'não pode ser 0' in erro(calc, c_mprp, 'perc', [6, '0', '5', ''])
    assert 'b não pode ser 0' in erro(calc, c_mprp, 'perc', [1, '5', '0', ''])
    assert 'Escreve' in erro(calc, c_mprp, 'perc', [0, '', '', '15'])
