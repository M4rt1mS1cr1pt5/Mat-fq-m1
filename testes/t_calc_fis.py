# Testes das calculadoras de Fisica (normal, limite e invalido).
import m1_nucleo as N
import c_fqen
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
