# Testes dos resolvedores de Geometria do 7.o ao 9.o ano (c_mgeo,
# c_msol, c_mgtr): normal, limite e invalido.
import c_mgeo
import c_msol
import c_mgtr
from base import calc, erro, tem, perto


def t_ang_complementar():
    r = calc(c_mgeo, 'ang', [0, '35', ''])
    tem(r[0], 'ângulo agudo', '> 90° - 35° = 55°', '> 180° - 35° = 145°')
    perto(r[2], 55)
    r = calc(c_mgeo, 'ang', [0, '54,5', ''])
    tem(r[0], '35,5° (= 35° 30\')', '125,5° (= 125° 30\')')
    r = calc(c_mgeo, 'ang', [0, '120', ''])
    tem(r[0], 'obtuso', 'Não tem complementar', '= 60°')
    tem(calc(c_mgeo, 'ang', [0, '90', ''])[0], 'reto', 'Não tem complementar')
    assert '180°' in erro(calc, c_mgeo, 'ang', [0, '180', ''])


def t_ang_triangulo():
    r = calc(c_mgeo, 'ang', [1, '35', '70'])
    tem(r[0], '> γ = 180° - 35° - 70° = 75°', 'acutângulo e escaleno',
        'Ângulos externos: 145°, 110°, 105°', 'Ao maior ângulo (75°)')
    tem(calc(c_mgeo, 'ang', [1, '90', '45'])[0], 'retângulo e isósceles')
    tem(calc(c_mgeo, 'ang', [1, '60', '60'])[0], 'equilátero')
    tem(calc(c_mgeo, 'ang', [1, '100', '30'])[0], 'obtusângulo')
    assert 'menor do que 180' in erro(calc, c_mgeo, 'ang', [1, '100', '80'])
    assert '2.º ângulo' in erro(calc, c_mgeo, 'ang', [1, '30', ''])


def t_ang_poligono():
    r = calc(c_mgeo, 'ang', [2, '7', ''])
    tem(r[0], 'heptágono', '> S = (7 - 2) × 180° = 900°',
        'ângulo interno = 900° : 7 = 900/7 ≈ 128,57°', '> d = 7 × 4 / 2 = 14',
        '5 triângulos', '7 eixos de simetria')
    assert r[2] == 900
    tem(calc(c_mgeo, 'ang', [2, '3', ''])[0], 'não tem diagonais', '= 60°')
    assert 'pelo menos 3' in erro(calc, c_mgeo, 'ang', [2, '2', ''])
    assert 'inteiro' in erro(calc, c_mgeo, 'ang', [2, '4,5', ''])


def t_ang_n_regular():
    r = calc(c_mgeo, 'ang', [3, '150', ''])
    tem(r[0], '180° - 150° = 30°', 'n = 360° : 30° = 12', 'dodecágono')
    tem(calc(c_mgeo, 'ang', [4, '72', ''])[0], '= 5', 'pentágono', '108°')
    tem(calc(c_mgeo, 'ang', [5, '1080', ''])[0], '= 8', 'octógono')
    tem(calc(c_mgeo, 'ang', [3, '100', ''])[0], 'Não há polígono regular')
    tem(calc(c_mgeo, 'ang', [5, '1000', ''])[0], 'Não há polígono assim')
    tem(calc(c_mgeo, 'ang', [3, '128,57', ''])[0], 'arredondado; uso n = 7')
    assert '120°' in erro(calc, c_mgeo, 'ang', [4, '150', ''])


def t_ang_paralelas():
    r = calc(c_mgeo, 'ang', [6, '35', ''])
    tem(r[0], '> 1 = 3 = 5 = 7 = 35°', '> 2 = 4 = 6 = 8 = 145°',
        'Alternos internos (iguais): 3 e 5, 4 e 6',
        'Internos do mesmo lado (somam 180°): 3 e 6, 4 e 5')
    g = r[4]
    assert g[6] == '1=3=5=7: 35°; 2=4=6=8: 145°'
    assert len(g[1][2][1]) == 4 and len(g[1][3][1]) == 4
    tem(calc(c_mgeo, 'ang', [6, '90', ''])[0], 'os 8 ângulos são retos')
    assert len(calc(c_mgeo, 'ang', [6, '5', ''])) == 4   # sem desenho
    assert '0°' in erro(calc, c_mgeo, 'ang', [6, '0', ''])


def t_area_figuras():
    r = calc(c_mgeo, 'area', [5, '8', '5', '4', '', '', 0])
    tem(r[0], 'A = (8 + 5) / 2 × 4', '> A = 26 u.a.',
        'são precisos os comprimentos')
    r = calc(c_mgeo, 'area', [7, '5', '', '', '', '', 2])
    tem(r[0], '> A = 25π ≈ 78,54 m²', '> P = 10π ≈ 31,42 m')
    r = calc(c_mgeo, 'area', [4, '8', '6', '', '', '', 0])
    tem(r[0], '> A = 24 u.a.', '> P = 20 u.c.')
    r = calc(c_mgeo, 'area', [9, '5', '3', '', '', '', 0])
    tem(r[0], '> A = 16π', '> P = 16π')
    r = calc(c_mgeo, 'area', [8, '3', '60', '', '', '', 1])
    tem(r[0], 'Setor circular: r = 3, α = 60°', '> A = 3π/2 ≈ 4,71 cm²',
        'Arco: α/360 × 2πr = π ≈ 3,14')


def t_area_medida_em_falta():
    r = calc(c_mgeo, 'area', [0, '', '', '', '36', '', 1])
    tem(r[0], '36 = l²', '⇔ l = √A', '> l = 6 cm', '> P = 24 cm')
    r = calc(c_mgeo, 'area', [5, '8', '5', '', '26', '', 0])
    tem(r[0], '26 = (8 + 5) / 2 × h', '⇔ h = 2 × A / (B + b)', '> h = 4 u.c.')
    r = calc(c_mgeo, 'area', [7, '', '', '', '', '12π', 1])
    tem(r[0], '12π = 2 × π × r', '> r = 6 cm', '> A = 36π')
    r = calc(c_mgeo, 'area', [9, '5', '', '', '9π', '', 0])
    tem(r[0], '> r = 4 u.c.')
    r = calc(c_mgeo, 'area', [8, '3', '', '', '3π/2', '', 0])
    tem(r[0], '> α = 60°')
    r = calc(c_mgeo, 'area', [6, '', '4', '2,75', '', '24', 0])
    tem(r[0], '> n = 6', '> A = 33 u.a.')


def t_area_apotema_trig():
    r = calc(c_mgeo, 'area', [6, '6', '4', '', '', '', 0])
    tem(r[0], 'ap = l / (2 tan(180°/n)) = 2√3', '> A = 24√3 ≈ 41,57 u.a.')
    r = calc(c_mgeo, 'area', [6, '4', '6', '', '', '', 1])
    tem(r[0], '= 3 (trigonometria', '> A = 36 cm²')


def t_area_invalidos():
    assert 'só usa 2 medidas' in erro(calc, c_mgeo, 'area',
                                     [3, '6', '4', '5', '', '', 0])
    assert 'mais do que uma' in erro(calc, c_mgeo, 'area',
                                     [2, '', '', '', '10', '', 0])
    assert 'Já deste' in erro(calc, c_mgeo, 'area', [0, '5', '', '', '25', '',
                                                    0])
    assert 'R tem de ser maior' in erro(calc, c_mgeo, 'area',
                                        [9, '3', '5', '', '', '', 0])
    assert 'não são compatíveis' in erro(calc, c_mgeo, 'area',
                                         [5, '8', '', '2', '5', '', 0])
    assert 'positivo' in erro(calc, c_mgeo, 'area', [0, '-2', '', '', '', '',
                                                    0])
    assert 'usa a área' in erro(calc, c_mgeo, 'area', [3, '', '4', '', '',
                                                      '12', 0])
    assert '360' in erro(calc, c_mgeo, 'area', [8, '2', '400', '', '', '', 0])


def t_sol_volumes():
    r = calc(c_msol, 'sol', [0, '3', '', '', '', '', 1])
    tem(r[0], '> V = 27 cm³', '> At = 54 cm²', '27 cm³ = 0,027 L')
    r = calc(c_msol, 'sol', [1, '5', '4', '3', '', '', 2])
    tem(r[0], '> V = 60 m³', 'At = 2 × (5 × 4 + 5 × 3 + 4 × 3)', '> At = 94 m²',
        '60000 L')
    r = calc(c_msol, 'sol', [3, '5', '4', '', '', '', 1])
    tem(r[0], '> V = 100π ≈ 314,16 cm³', 'Al = 2πrh = 40π', '> At = 90π')
    r = calc(c_msol, 'sol', [6, '3', '4', '', '', '', 0])
    tem(r[0], '> V = 12π ≈ 37,7 u.v.', 'g = √(r² + h²) = 5', 'Al = πrg = 15π',
        '> At = 24π')
    r = calc(c_msol, 'sol', [7, '3', '', '', '', '', 1])
    tem(r[0], '> V = 36π ≈ 113,1 cm³', 'A = 4π × 3²', '> A = 36π')


def t_sol_piramides():
    r = calc(c_msol, 'sol', [4, '20', '9', '', '', '', 0])
    tem(r[0], 'V = 20 × 9 / 3', '> V = 60 u.v.', 'é preciso o apótema')
    r = calc(c_msol, 'sol', [5, '4', '6', '4', '', '', 1])
    tem(r[0], '= 3 (metade do lado)', 'Ab = n × l × a / 2 = 36 cm²',
        '> V = 48 cm³', '√(h² + a²) = 5', 'Al = n × l × ap / 2 = 60 cm²',
        '> At = Ab + Al = 96 cm²')
    r = calc(c_msol, 'sol', [5, '3', '6', '4', '', '', 1])
    tem(r[0], '= √3 ≈ 1,73', '> V = 12√3 ≈ 20,78 cm³')
    tem(calc(c_msol, 'sol', [5, '5', '2', '3', '', '', 1])[0],
        'trigonometria: 9.º ano')
    assert 'inteiro' in erro(calc, c_msol, 'sol', [5, '4,5', '2', '3', '', '',
                                                  1])


def t_sol_inversos():
    r = calc(c_msol, 'sol', [0, '', '', '', '64', '', 1])
    tem(r[0], '64 = a³', '⇔ a = ∛V', '> a = 4 cm', '> At = 96 cm²')
    r = calc(c_msol, 'sol', [3, '5', '', '', '100π', '', 1])
    tem(r[0], '100π = π × 5² × h', '> h = 4 cm')
    r = calc(c_msol, 'sol', [3, '5', '', '', '', '90π', 1])
    tem(r[0], '⇔ h = (At - 2πr²) / (2πr)', '> h = 4 cm', '> V = 100π')
    r = calc(c_msol, 'sol', [7, '', '', '', '36π', '', 1])
    tem(r[0], '⇔ r = ∛(3V / (4π))', '> r = 3 cm')
    r = calc(c_msol, 'sol', [7, '', '', '', '', '100π', 1])
    tem(r[0], '> r = 5 cm', '> V = 500π/3 ≈ 523,6 cm³')
    r = calc(c_msol, 'sol', [0, '', '', '', '', '54', 0])
    tem(r[0], '> a = 3 u.c.')


def t_sol_invalidos():
    assert 'só usa 2 medidas' in erro(calc, c_msol, 'sol',
                                     [3, '5', '4', '6', '', '', 1])
    assert 'usa o volume' in erro(calc, c_msol, 'sol',
                                  [6, '3', '', '', '', '24π', 1])
    assert 'três medidas' in erro(calc, c_msol, 'sol',
                                  [5, '4', '6', '', '48', '', 1])
    assert 'não são compatíveis' in erro(calc, c_msol, 'sol',
                                         [3, '5', '', '', '', '10', 1])
    assert 'Já deste' in erro(calc, c_msol, 'sol', [7, '3', '', '', '36π',
                                                   '', 1])


def t_iso_translacao_reflexoes():
    r = calc(c_mgtr, 'iso', ['1 1; 4 1; 2 3', 0, '3 2'])
    tem(r[0], '= (x, y) → (x + 3, y + 2)', "> A(1, 1) → A'(4, 3)",
        "> C(2, 3) → C'(5, 5)", 'Mantém o sentido')
    assert len(r[4][1]) == 7   # figura, imagem, pontos, rotulos, vetores
    r = calc(c_mgtr, 'iso', ['1 1; 4 1; 2 3', 1, ''])
    tem(r[0], '(x, y) → (x, -y)', "C'(2, -3)", 'troca o sentido')
    r = calc(c_mgtr, 'iso', ['1 1; 4 1; 2 3', 3, '5'])
    tem(r[0], 'Reflexão na reta x = 5', '(x, y) → (-x + 10, y)', "A'(9, 1)")
    r = calc(c_mgtr, 'iso', ['1 1; 4 1; 2 3', 5, ''])
    tem(r[0], '(x, y) → (y, x)', "B'(1, 4)")
    r = calc(c_mgtr, 'iso', ['2 3', 4, '-1/2'])
    tem(r[0], 'y = -0,5', '(x, y) → (x, -y - 1)', "A'(2, -4)")


def t_iso_rotacoes():
    r = calc(c_mgtr, 'iso', ['1 1; 4 1; 2 3', 7, ''])
    tem(r[0], 'de centro O', '(x, y) → (-y, x)', "B'(-1, 4)", "C'(-3, 2)")
    r = calc(c_mgtr, 'iso', ['1 1; 4 1; 2 3', 7, '1 1'])
    tem(r[0], 'de centro (1, 1)', '(x, y) → (-y + 2, x)', "C'(-1, 2)")
    r = calc(c_mgtr, 'iso', ['1,5 1; 4 1', 8, ''])
    tem(r[0], '(x, y) → (-x, -y)', "A'(-1,5; -1)", 'simetria central')
    r = calc(c_mgtr, 'iso', ['1 1; 4 1; 2 3', 9, '2 -1'])
    tem(r[0], 'sentido negativo', '(x, y) → (y + 3, -x + 1)', "A'(4, 0)")


def t_iso_invalidos():
    assert 'duas coordenadas' in erro(calc, c_mgtr, 'iso',
                                      ['1 1; 4 1 2', 0, '3 2'])
    assert 'vetor' in erro(calc, c_mgtr, 'iso', ['1 1', 0, ''])
    assert 'só o valor de k' in erro(calc, c_mgtr, 'iso', ['1 1', 3, '1 2'])
    assert 'centro' in erro(calc, c_mgtr, 'iso', ['1 1', 7, '1'])
    assert 'só números' in erro(calc, c_mgtr, 'iso', ['1 a', 1, ''])
    assert 'pelo menos um ponto' in erro(calc, c_mgtr, 'iso', [' ; ', 1, ''])


def t_circ_arcos():
    r = calc(c_mgtr, 'circ', [0, '80', ''])
    tem(r[0], '> Ângulo ao centro AOB = 80°', '> Ângulo inscrito AVB = 40°',
        '(360° - 80°) / 2 = 140°')
    perto(r[2], 40)
    r = calc(c_mgtr, 'circ', [1, '35', ''])
    tem(r[0], '> Arco AB = 2 × 35° = 70°')
    tem(calc(c_mgtr, 'circ', [0, '180', ''])[0], 'semicircunferência é reto')
    assert '360' in erro(calc, c_mgtr, 'circ', [0, '360', ''])
    assert '180' in erro(calc, c_mgtr, 'circ', [1, '200', ''])


def t_circ_vertices():
    r = calc(c_mgtr, 'circ', [2, '100', '40'])
    tem(r[0], 'semissoma', '> (100° + 40°) / 2 = 70°')
    r = calc(c_mgtr, 'circ', [3, '200', '60'])
    tem(r[0], 'semidiferença', '> (200° - 60°) / 2 = 70°')
    assert len(r) == 5
    assert 'maior' in erro(calc, c_mgtr, 'circ', [3, '60', '100'])
    assert '360' in erro(calc, c_mgtr, 'circ', [2, '300', '100'])
    assert 'dois arcos' in erro(calc, c_mgtr, 'circ', [2, '100', ''])


def t_circ_poligonos_setor():
    r = calc(c_mgtr, 'circ', [4, '85', '70'])
    tem(r[0], '> Oposto a 85°: 180° - 85° = 95°', '> Oposto a 70°: 180° - 70°'
        ' = 110°')
    r = calc(c_mgtr, 'circ', [5, '7', ''])
    tem(r[0], '> 360° : 7 = 360/7 ≈ 51,43°', '= 900/7 ≈ 128,57°')
    r = calc(c_mgtr, 'circ', [6, '5', '60'])
    tem(r[0], '> l = 60/360 × 2π × 5 = 5π/3 ≈ 5,24',
        '> A = 60/360 × π × 5² = 25π/6 ≈ 13,09')
    assert 'inteiro' in erro(calc, c_mgtr, 'circ', [5, '2', ''])
    assert '180' in erro(calc, c_mgtr, 'circ', [4, '190', '20'])
