# Testes das calculadoras de Fisica (normal, limite e invalido).
import m1_nucleo as N
import c_fqen
import c_fqci
import c_fqte
from base import calc, erro, tem, perto


def g10():
    N.CF['g'] = 10.0

# ------------------------------------------------------------ c_fqen


def t_em_normal():
    g10()
    r = calc(c_fqen, 'em', ['2,0', '3,0', '5,0'])
    tem(r[0], 'Ec = 9,0 J', 'Epg = 1,0 × 10² J', 'Em ≈ 1,1 × 10² J')
    perto(r[2], 109.0)


def t_em_unidades():
    g10()
    # 500 g e 36 km/h = 10 m/s
    r = calc(c_fqen, 'em', ['500', '36', ''], {0: 1, 1: 1})
    tem(r[0], '0,500 kg', 'Ec = 25 J')
    perto(r[2], 25.0)


def t_em_g98():
    N.CF['g'] = 9.8
    r = calc(c_fqen, 'em', ['2,00', '', '1,50'])
    tem(r[0], 'Epg = 29,4 J', '9,8 m s⁻²')
    g10()


def t_em_abaixo():
    g10()
    r = calc(c_fqen, 'em', ['1,50', '', '-2,0'])
    tem(r[0], '× (-2,0 m)', 'Epg = -30 J', 'abaixo do nível')


def t_em_invalido():
    assert 'massa' in erro(calc, c_fqen, 'em', ['0', '2', '1'])
    assert 'velocidade' in erro(calc, c_fqen, 'em', ['1', '', ''])
    assert 'negativ' in erro(calc, c_fqen, 'em', ['1', '-2', ''])


def t_cons_queda():
    g10()
    r = calc(c_fqen, 'cons', ['20', '0', '0', ''])
    tem(r[0], 'corta-se', 'vB = 20 m s⁻¹')
    perto(r[2], 20.0)


def t_cons_altura():
    g10()
    r = calc(c_fqen, 'cons', ['', '0', '0', '12'])
    tem(r[0], 'hA = 7,2 m')
    perto(r[2], 7.2)


def t_cons_dissipada():
    g10()
    # bola que cai de 1,20 m e ressalta ate 0,90 m (m = 57,0 g)
    r = calc(c_fqen, 'cons', ['1,20', '0', '0,90', '0', '57,0'], {4: 1})
    tem(r[0], 'Dissipada = 25 %', 'Ed ≈ 0,17 J')
    perto(r[2], 3.0)


def t_cons_com_ed():
    g10()
    r = calc(c_fqen, 'cons', ['20,0', '0', '0', '', '2,0', '100'])
    tem(r[0], '- Ed', 'vB ≈ 17 m s⁻¹')
    perto(r[2], 300 ** 0.5)


def t_cons_invalido():
    g10()
    assert 'só o campo' in erro(calc, c_fqen, 'cons', ['', '5', '0', ''])
    assert 'não chega' in erro(calc, c_fqen, 'cons', ['1,0', '0', '3,0', ''])
    assert 'massa' in erro(calc, c_fqen, 'cons', ['5', '0', '0', '', '', '10'])
    assert 'resultado' in erro(calc, c_fqen, 'cons',
                               ['5', '0', '0', '9', '1', '10'])


def t_tr_normal():
    r = calc(c_fqen, 'tr', ['10', '5,0', '60'])
    tem(r[0], 'cos 60°', 'W = 25 J', 'potente', 'F cos α = 5,0 N')
    perto(r[2], 25.0)


def t_tr_limites():
    r = calc(c_fqen, 'tr', ['10', '5,0', '90'])
    tem(r[0], 'nulo')
    assert r[2] == 0.0
    r = calc(c_fqen, 'tr', ['25', '2,0', '180'])
    tem(r[0], 'W = -50 J', 'resistente')


def t_tr_invalido():
    assert '180' in erro(calc, c_fqen, 'tr', ['10', '2', '200'])
    assert 'desloca' in erro(calc, c_fqen, 'tr', ['10', '0', '30'])
    assert 'força' in erro(calc, c_fqen, 'tr', ['-3', '2', '30'])


def t_wp_desce_sobe():
    g10()
    r = calc(c_fqen, 'wp', ['2,0', '5,0', '0'])
    tem(r[0], 'W(P) = 1,0 × 10² J', 'ΔEpg = -1,0 × 10² J', 'desce')
    r = calc(c_fqen, 'wp', ['2,0', '0', '3,0'])
    tem(r[0], 'W(P) = -60 J', 'sobe')
    perto(r[2], -60.0)


def t_wp_mesma_altura():
    g10()
    r = calc(c_fqen, 'wp', ['2,0', '1,5', '1,5'])
    tem(r[0], 'nulo')
    assert 'massa' in erro(calc, c_fqen, 'wp', ['0', '1', '0'])


def t_tec_trabalho():
    r = calc(c_fqen, 'tec', ['1000', '10', '20', '', ''])
    tem(r[0], 'W = 1,5 × 10⁵ J', 'aumenta')
    perto(r[2], 150000.0)


def t_tec_velocidades():
    r = calc(c_fqen, 'tec', ['2,0', '4,0', '', '-16', ''])
    perto(r[2], 0.0)
    r = calc(c_fqen, 'tec', ['2,0', '', '0', '-16', '4,0'])
    tem(r[0], 'vi = 4,0 m s⁻¹', 'F(R) = 4,0 N')


def t_tec_invalido():
    assert 'para antes' in erro(calc, c_fqen, 'tec', ['2', '1', '', '-50', ''])
    assert 'só o campo' in erro(calc, c_fqen, 'tec', ['2', '', '', '10', ''])
    assert 'massa' in erro(calc, c_fqen, 'tec', ['-1', '1', '2', '', ''])


def t_pot_energia():
    # 1500 W durante 2,0 h
    r = calc(c_fqen, 'pot', ['', '2,0', '1500'], {1: 2})
    tem(r[0], 'E ≈ 1,1 × 10⁷ J', '3,0 kWh')
    perto(r[2], 1.08e7)


def t_pot_tempo_potencia():
    r = calc(c_fqen, 'pot', ['3,6', '', '1000'], {0: 1})
    tem(r[0], 'Δt = 3,6 s')
    r = calc(c_fqen, 'pot', ['1200', '60', ''])
    tem(r[0], 'P = 20 W')
    perto(r[2], 20.0)


def t_pot_invalido():
    assert 'só o campo' in erro(calc, c_fqen, 'pot', ['', '', '5'])
    assert 'tempo' in erro(calc, c_fqen, 'pot', ['10', '0', ''])


def t_ren_normal():
    r = calc(c_fqen, 'ren', ['30', '100', ''])
    tem(r[0], 'η = 30 %', 'Dissipada: 70 (70 %')
    r = calc(c_fqen, 'ren', ['', '2000', '25'])
    tem(r[0], 'E(útil) = 5,0 × 10²')
    r = calc(c_fqen, 'ren', ['600', '', '40'])
    perto(r[2], 1500.0)


def t_ren_invalido():
    assert 'impossível' in erro(calc, c_fqen, 'ren', ['120', '100', ''])
    assert 'impossível' in erro(calc, c_fqen, 'ren', ['', '100', '120'])
    assert 'só o campo' in erro(calc, c_fqen, 'ren', ['1', '2', '3'])

# ------------------------------------------------------------ c_fqci


def t_ohm_normal():
    r = calc(c_fqci, 'ohm', ['12', '', '0,50'])
    tem(r[0], 'R = 24 Ω', 'P = U I = 6,0 W')
    perto(r[2], 24.0)
    r = calc(c_fqci, 'ohm', ['230', '46', ''])
    tem(r[0], 'I = 5,0 A')


def t_ohm_unidades():
    # 2,0 mA numa resistencia de 220 ohm
    r = calc(c_fqci, 'ohm', ['', '220', '2,0'], {2: 1})
    tem(r[0], '0,0020 A', 'U = 0,44 V')
    perto(r[2], 0.44)
    # 4,7 kOhm com 12 V
    r = calc(c_fqci, 'ohm', ['12', '4,7', ''], {1: 1})
    perto(r[2], 12 / 4700.0)


def t_ohm_invalido():
    assert 'só o campo' in erro(calc, c_fqci, 'ohm', ['12', '', ''])
    assert 'só o campo' in erro(calc, c_fqci, 'ohm', ['12', '3', '4'])
    assert 'resistência' in erro(calc, c_fqci, 'ohm', ['', '-5', '2'])


def t_rho_cobre():
    # fio de cobre: 100 m, 1,5 mm2 -> 1,1 ohm
    r = calc(c_fqci, 'rho', [1, '', '100', '1,5', ''])
    tem(r[0], 'ρ(cobre) = 1,7 × 10⁻⁸ Ω m', '(1,5 × 10⁻⁶ m²)', 'R ≈ 1,1 Ω')
    perto(r[2], 1.7e-8 * 100 / 1.5e-6)


def t_rho_incognitas():
    r = calc(c_fqci, 'rho', [1, '', '', '1,5', '5,0'])
    perto(r[2], 5.0 * 1.5e-6 / 1.7e-8)
    r = calc(c_fqci, 'rho', [0, '', '2,0', '0,50', '0,10'])
    tem(r[0], 'ρ = 2,5 × 10⁻⁸ Ω m')
    r = calc(c_fqci, 'rho', [6, '', '1,0', '', '10'])
    tem(r[0], 'mm²')
    perto(r[2], 1.1e-6 * 1.0 / 10)


def t_rho_invalido():
    assert 'deixa ρ vazio' in erro(calc, c_fqci, 'rho', [1, '2e-8', '1', '1', ''])
    assert 'só o campo' in erro(calc, c_fqci, 'rho', [0, '', '2', '', '1'])
    assert 'comprimento' in erro(calc, c_fqci, 'rho', [1, '', '-2', '1', ''])


def t_assoc_serie():
    r = calc(c_fqci, 'assoc', [0, '10; 20; 30', '12'])
    tem(r[0], 'Req = 60 Ω', 'I total = 0,20 A', 'R3: I = 0,20 A; U = 6,0 V')
    perto(r[2], 60.0)


def t_assoc_paralelo():
    r = calc(c_fqci, 'assoc', [1, '10; 20; 20', '10'])
    tem(r[0], 'Req = 5,0 Ω', 'I total = 2,0 A', 'R2: U = 10 V; I = 0,50 A')
    r = calc(c_fqci, 'assoc', [1, '6; 3', ''])
    perto(r[2], 2.0)


def t_assoc_invalido():
    assert 'duas' in erro(calc, c_fqci, 'assoc', [0, '10', ''])
    assert 'positiv' in erro(calc, c_fqci, 'assoc', [1, '10; 0', ''])
    assert 'positiv' in erro(calc, c_fqci, 'assoc', [0, '10; 5', '-3'])


def t_ger_tensao():
    r = calc(c_fqci, 'ger', ['9,0', '1,5', '0,40', ''])
    tem(r[0], 'U = 8,4 V', 'gerada ε I = 3,6 W', 'dissipada r I² = 0,24 W',
        'η = U / ε = 93 %', 'I = ε / r = 6,0 A')
    perto(r[2], 8.4)


def t_ger_incognitas():
    r = calc(c_fqci, 'ger', ['', '0,50', '2,0', '11'])
    tem(r[0], 'ε = 12 V')
    r = calc(c_fqci, 'ger', ['4,5', '', '0,30', '4,2'])
    tem(r[0], 'r = 1,0 Ω')
    r = calc(c_fqci, 'ger', ['4,5', '1,0', '', '4,2'])
    perto(r[2], 0.3)


def t_ger_invalido():
    assert 'curto-circuito' in erro(calc, c_fqci, 'ger', ['9', '1', '12', ''])
    assert 'maior do que ε' in erro(calc, c_fqci, 'ger', ['9', '', '1', '10'])
    assert 'r = 0' in erro(calc, c_fqci, 'ger', ['9', '0', '', '8'])


def t_pot_joule():
    r = calc(c_fqci, 'pot', ['', '', '2,0', '10'])
    tem(r[0], 'efeito Joule', 'P = 40 W')
    perto(r[2], 40.0)


def t_pot_custo():
    # 230 V, 46 ohm, 2,0 h, 0,16 euros por kWh
    r = calc(c_fqci, 'pot', ['', '230', '', '46', '2,0', '0,16'])
    tem(r[0], 'P ≈ 1,2 × 10³ W', '2,3 kWh', '0,16 €/kWh = 0,37 €')
    perto(r[2], 230 ** 2 / 46.0 * 7200)


def t_pot_corrente():
    # 2000 W a 230 V durante 30 min
    r = calc(c_fqci, 'pot', ['2000', '230', '', '', '30'], {4: 1})
    tem(r[0], 'I ≈ 8,70 A', '1,0 kWh')
    perto(r[2], 3.6e6)


def t_pot_invalido():
    assert 'dois' in erro(calc, c_fqci, 'pot', ['100', '', '', ''])
    assert 'dois' in erro(calc, c_fqci, 'pot', ['100', '10', '2', ''])
    assert 'tempo' in erro(calc, c_fqci, 'pot', ['100', '10', '', '', '0'])

# ------------------------------------------------------------ c_fqte


def t_cal_energia():
    # 0,500 kg de agua de 20 para 80 graus
    r = calc(c_fqte, 'cal', [1, '', '0,500', '', '20', '80'])
    tem(r[0], 'c(água) = 4,18 × 10³', 'ΔT = 60 K', 'Q ≈ 1,3 × 10⁵ J', 'recebe')
    perto(r[2], 0.5 * 4180 * 60)
    r = calc(c_fqte, 'cal', [1, '', '0,500', '', '20,0', '80,0'])
    tem(r[0], 'Q ≈ 1,25 × 10⁵ J')


def t_cal_incognitas():
    r = calc(c_fqte, 'cal', [0, '2,1e4', '0,500', '', '20', '30'])
    tem(r[0], 'c = 4,2 × 10³')
    r = calc(c_fqte, 'cal', [3, '4,5e3', '', '', '20', '70'])
    tem(r[0], 'c(alumínio) = 9,0 × 10²', 'm = 0,10 kg')
    r = calc(c_fqte, 'cal', [1, '-8,36e3', '0,200', '', '30', ''])
    tem(r[0], 'θf = 20 °C')
    r = calc(c_fqte, 'cal', [1, '2,09e4', '0,500', '', '', '30,0'])
    perto(r[2], 20.0)


def t_cal_kelvin():
    # temperaturas em kelvin: a diferenca e a mesma
    r = calc(c_fqte, 'cal', [1, '', '0,500', '', '293', '353'], {4: 1, 5: 1})
    perto(r[2], 0.5 * 4180 * 60, 1e-6)


def t_cal_invalido():
    assert 'deixa c vazio' in erro(calc, c_fqte, 'cal',
                                   [1, '', '1', '4000', '20', '30'])
    assert 'ΔT = 0' in erro(calc, c_fqte, 'cal', [0, '2e4', '0,5', '', '20', '20'])
    assert 'só o campo' in erro(calc, c_fqte, 'cal', [0, '', '2', '', '20', '25'])
    assert 'incoerentes' in erro(calc, c_fqte, 'cal',
                                 [1, '-100', '', '', '20', '30'])


def t_est_normal():
    r = calc(c_fqte, 'est', [0, '', '0,100', ''])
    tem(r[0], 'ΔH = 3,34 × 10⁵ J kg⁻¹ (a 0 °C)', 'Q = 3,34 × 10⁴ J',
        'não varia')
    r = calc(c_fqte, 'est', [1, '', '', '4,52e5'])
    tem(r[0], 'm = 0,200 kg')
    perto(r[2], 0.2)


def t_est_escrevo():
    r = calc(c_fqte, 'est', [2, '', '0,050', '1,7e4'])
    tem(r[0], 'ΔH = 3,4 × 10⁵ J kg⁻¹')
    assert 'deixa ΔH vazio' in erro(calc, c_fqte, 'est', [0, '1e4', '', '2'])
    assert 'massa' in erro(calc, c_fqte, 'est', [0, '', '-1', ''])


def t_eq_sem_mudanca():
    r = calc(c_fqte, 'eq', ['0,200', '4,18e3', '60', 0, '0,100', '4,18e3',
                            '15'])
    tem(r[0], 'θe = 45 °C', '1,3 × 10⁴ J')
    perto(r[2], 45.0)
    r = calc(c_fqte, 'eq', ['0,200', '4,18e3', '80', 0, '0,300', '9,0e2',
                            '20'])
    perto(r[2], (0.2 * 4180 * 80 + 0.3 * 900 * 20) / (0.2 * 4180 + 0.3 * 900))


def t_eq_gelo():
    r = calc(c_fqte, 'eq', ['0,300', '4,18e3', '40', 1, '0,050', '4,18e3', '0'])
    tem(r[0], 'θe ≈ 23 °C', 'fundir o gelo: 1,7 × 10⁴ J')
    perto(r[2], (0.3 * 4180 * 40 - 0.05 * 3.34e5) / (0.3 * 4180 + 0.05 * 4180))
    r = calc(c_fqte, 'eq', ['0,100', '4,18e3', '20', 1, '0,100', '4,18e3', '0'])
    tem(r[0], 'Nem todo o gelo funde', 'Funde ≈ 0,025 kg', 'Sobra 0,075 kg')
    assert r[2] == 0.0


def t_eq_invalido():
    assert 'massa do corpo 2' in erro(calc, c_fqte, 'eq',
                                     ['1', '4180', '20', 0, '0', '4180', '10'])
    assert 'acima de 0' in erro(calc, c_fqte, 'eq',
                                ['1', '4180', '-5', 1, '1', '4180', '0'])


def t_cond_potencia():
    # vidro: k = 0,80; 1,5 m2; 20 K; 4,0 mm
    r = calc(c_fqte, 'cond', ['0,80', '1,5', '20', '4,0', ''], {3: 2})
    tem(r[0], '0,0040 m', 'P = 6,0 × 10³ W')
    perto(r[2], 6000.0)


def t_cond_incognitas():
    r = calc(c_fqte, 'cond', ['', '2,0', '15', '0,10', '24'])
    tem(r[0], 'k = 0,080 W m⁻¹ K⁻¹')
    r = calc(c_fqte, 'cond', ['0,80', '2,0', '', '5,0', '480'], {3: 2})
    tem(r[0], 'ΔT = 1,5 K')
    r = calc(c_fqte, 'cond', ['400', '1,0e-4', '50', '', '2,0'])
    perto(r[2], 1.0)


def t_cond_invalido():
    assert 'só o campo' in erro(calc, c_fqte, 'cond', ['1', '1', '1', '1', '1'])
    assert 'espessura' in erro(calc, c_fqte, 'cond', ['1', '1', '1', '0', ''])


def t_pl_normal():
    r = calc(c_fqte, 'pl', ['0', '500', '0', ''])
    tem(r[0], 'ΔU = 500 J', 'aumenta')
    r = calc(c_fqte, 'pl', ['-200', '', '0', '300'])
    tem(r[0], 'Q = 500 J', 'recebe')
    r = calc(c_fqte, 'pl', ['', '-300', '0', '-500'])
    tem(r[0], 'W = -200 J', 'cede')


def t_pl_limites():
    r = calc(c_fqte, 'pl', ['100', '-100', '0', ''])
    tem(r[0], 'não varia')
    assert 'só o campo' in erro(calc, c_fqte, 'pl', ['100', '200', '300', '600'])


def t_pv_normal():
    r = calc(c_fqte, 'pv', ['1,0e3', '0,50', '80', '', ''])
    tem(r[0], 'P(rad) = 5,0 × 10² W', 'η = 16 %')
    perto(r[2], 16.0)
    r = calc(c_fqte, 'pv', ['800', '100', '', '5,0', '0,30'], {1: 1})
    tem(r[0], 'P(rad) = 8,00 W', 'P(el) = 1,5 W', 'η ≈ 19 %')


def t_pv_invalido():
    assert 'tensão e a corrente' in erro(calc, c_fqte, 'pv',
                                         ['1,0e3', '2,0', '', '', ''])
    assert '100 %' in erro(calc, c_fqte, 'pv', ['1,0e3', '0,50', '600', '', ''])
    assert 'não os três' in erro(calc, c_fqte, 'pv',
                                 ['1,0e3', '0,50', '60', '5', '2'])
