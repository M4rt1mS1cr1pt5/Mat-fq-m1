# Testes das calculadoras comuns (normal, limite e invalido).
import c_comu
import c_comd
from base import calc, erro, tem, perto


def t_sci_normal():
    r = calc(c_comu, 'sci', ['2^10+sqrt(2)'])
    tem(r[0], '1025,414213562')
    perto(r[2], 1025.4142135623731)


def t_sci_exato():
    r = calc(c_comu, 'sci', ['1/3+1/6'])
    tem(r[0], '= 0,5')


def t_sci_invalido():
    assert 'desconhecido' in erro(calc, c_comu, 'sci', ['2y'])
    assert 'Escreve' in erro(calc, c_comu, 'sci', [''])
    assert 'zero' in erro(calc, c_comu, 'sci', ['1/0'])


def t_sci_limite():
    assert 'grande' in erro(calc, c_comu, 'sci', ['10^400'])
    r = calc(c_comu, 'sci', ['sin(90)'])
    tem(r[0], '= 1')


def t_sci_trig():
    r = calc(c_comu, 'sci', ['cos(60)'])
    tem(r[0], '= 0,5')


def t_sf_contar():
    r = calc(c_comu, 'sf', [0, '0,0250; 1500', '2'])
    tem(r[0], '0,0250: 3 alg. sig.', '1500: 4 alg. sig.', '1,5 × 10³')


def t_sf_soma():
    r = calc(c_comu, 'sf', [1, '12,3; 0,456; 2', ''])
    tem(r[0], '> 15')
    r = calc(c_comu, 'sf', [1, '12,31; 0,456', ''])
    tem(r[0], '> 12,77')


def t_sf_produto():
    r = calc(c_comu, 'sf', [3, '2,5; 3,14159', ''])
    tem(r[0], '> 7,9')
    r = calc(c_comu, 'sf', [4, '10,0; 3,0', ''])
    tem(r[0], '> 3,3')


def t_sf_limite():
    r = calc(c_comu, 'sf', [1, '1,2e3; 25', ''])
    tem(r[0], '1,2 × 10³')
    r = calc(c_comu, 'sf', [2, '100,0; 99,95', ''])
    tem(r[0], '> 0,1')


def t_sf_invalido():
    assert 'decimais' in erro(calc, c_comu, 'sf', [3, '1/3; 2', ''])
    assert 'dois' in erro(calc, c_comu, 'sf', [3, '2,5', ''])
    assert 'zero' in erro(calc, c_comu, 'sf', [4, '2,5; 0', ''])


def t_uni():
    f = c_comu._uni
    us = ['m³', 'dm³', 'L', 'cm³', 'mL', 'dL', 'cL', 'mm³', 'hL']
    fld = [0, 0, 0, 4]
    r = f([(250e-6, 3), 1], 'V', us, fld)
    tem(r[0], '250 mL = 0,25 dm³')
    us = ['K', '°C']
    r = f([(300.0, 3), 1], 'T', us, [0, 0, 0, 0])
    tem(r[0], '300 K = 26,85 °C')


def t_pre():
    r = c_comu._pre([])
    tem(r[0], 'mili (m) = 10⁻³', 'quilo (k) = 10³')


def t_exp_normal():
    r = calc(c_comd, 'exp', ['2,35; 2,41; 2,38; 2,40', 's', '', '2,45'])
    tem(r[0], '(2,39 ± 0,04) s', 'Erro percentual = 2,65 %')


def t_exp_leitura():
    r = calc(c_comd, 'exp', ['2,35; 2,36', 's', '0,05', ''])
    tem(r[0], 'incerteza de leitura', '(2,36 ± 0,05) s')


def t_exp_um_valor():
    r = calc(c_comd, 'exp', ['2,35', 's', '', ''])
    tem(r[0], 'um só valor')


def t_exp_ref_zero():
    r = calc(c_comd, 'exp', ['0,1; 0,2', '', '', '0'])
    tem(r[0], 'não há erro percentual')


def t_exp_invalido():
    assert 'Escreve' in erro(calc, c_comd, 'exp', ['', '', '', ''])
    assert 'mal escrito' in erro(calc, c_comd, 'exp', ['2,,3', '', '', ''])


def t_reg_normal():
    r = calc(c_comd, 'reg', ['1;2;3;4', '2,1;3,9;6,2;7,8', 'A', 'V', '2,5'])
    tem(r[0], 'm = 1,940 V/A', 'Interpolação')
    perto(r[2], 1.94)


def t_reg_extrapola():
    r = calc(c_comd, 'reg', ['1;2;3', '2;4;6', '', '', '10'])
    tem(r[0], 'Extrapolação', 'r = 1')


def t_reg_horizontal():
    r = calc(c_comd, 'reg', ['1;2;3', '5;5;5', '', '', ''])
    tem(r[0], 'r não está definido')


def t_reg_invalido():
    assert 'iguais' in erro(calc, c_comd, 'reg', ['2;2;2', '1;2;3', '', '', ''])
    assert 'tantos' in erro(calc, c_comd, 'reg', ['1;2;3', '1;2', '', '', ''])
    assert 'pelo menos 2' in erro(calc, c_comd, 'reg', ['1', '1', '', '', ''])


def t_reg_dois_pontos():
    r = calc(c_comd, 'reg', ['0;1', '1;3', '', '', ''])
    tem(r[0], 'dois pontos')
