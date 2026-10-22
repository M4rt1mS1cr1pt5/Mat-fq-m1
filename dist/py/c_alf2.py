# c_alf2.py - M1TR4M: assistentes das AL de Fisica 3.1 (painel
# fotovoltaico), 3.2 (capacidade termica massica) e 3.3 (balanco
# energetico: entalpia de fusao do gelo).
#@ c_alf2.painel|AL 3.1 Painel fotovoltaico|al 3.1 painel fotovoltaico pot\u00eancia el\u00e9trica m\u00e1xima resist\u00eancia de carga irradi\u00e2ncia rendimento|F|af
#@ c_alf2.cap|AL 3.2 Capacidade t\u00e9rmica m\u00e1ssica|al 3.2 capacidade t\u00e9rmica m\u00e1ssica bloco calorim\u00e9trico resist\u00eancia de aquecimento temperatura tempo regress\u00e3o erro percentual|F|af
#@ c_alf2.fusao|AL 3.3 Balan\u00e7o energ\u00e9tico (fus\u00e3o do gelo)|al 3.3 balan\u00e7o energ\u00e9tico sistema isolado gelo entalpia de fus\u00e3o calor\u00edmetro erro percentual|F|af
# Casos-limite: listas com tamanhos diferentes ou curtas, potencia ou
# massa nulas, temperatura que nao sobe (declive <= 0), temperatura
# final fora do intervalo, energia de fusao negativa (dados incoerentes).

import math
import m1_nucleo as N

X = N.X
CA = 4.18e3          # J/(kg K), agua liquida
HF = 3.34e5          # J/kg, fusao do gelo (valor tabelado)


def fit(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum([(x - mx) ** 2 for x in xs])
    syy = sum([(y - my) ** 2 for y in ys])
    sxy = sum([(xs[i] - mx) * (ys[i] - my) for i in range(n)])
    N.need(max(xs) > min(xs), 'Todos os x s\u00e3o iguais: n\u00e3o h\u00e1 reta de '
           'regress\u00e3o')
    m = sxy / sxx
    return m, my - m * mx, (sxy / math.sqrt(sxx * syy) if syy > 0 else None)


def pares(a, b, na, nb):
    N.need(len(a) == len(b), 'H\u00e1 ' + str(len(a)) + ' valores de ' + na +
           ' e ' + str(len(b)) + ' de ' + nb + ': tem de haver o mesmo '
           'n\u00famero')
    N.need(len(a) >= 3, 'S\u00e3o precisos pelo menos 3 pontos')
    return [x[0] for x in a], [x[0] for x in b]


def erro(x, ref):
    e = abs(x - ref) / ref * 100
    return '> Erro percentual = ' + N.fmt(e if e > 1e-9 else 0.0, 2) + ' %'

# ------------------------------------------------------------ AL 3.1


def painel():
    return ('AL 3.1 Painel fotovoltaico',
            [N.fld('Tens\u00f5es U (V)', '', '', 'l'),
             N.fld('Correntes I (mA)', '', '', 'l'),
             N.fld('Irradi\u00e2ncia Er (W/m\u00b2, opcional)', '', '', 'o'),
             N.fld('\u00c1rea do painel (cm\u00b2, opcional)', '', '', 'o')],
            _painel)


def _painel(v):
    us, iss = pares(v[0], v[1], 'U', 'I')
    er, A = v[2], v[3]
    for x in us + iss:
        N.nneg(x, 'Cada valor de U e de I')
    ps = [us[i] * iss[i] / 1000 for i in range(len(us))]
    k = ps.index(max(ps))
    o = ['P = U I em cada ponto:']
    for i in range(len(us)):
        o.append(N.fmt(us[i], 3) + ' V; ' + N.fmt(iss[i], 3) + ' mA: P = ' +
                 N.fmt(ps[i] * 1000, 3) + ' mW' + (' (m\u00e1x.)' if i == k else ''))
    rk = us[k] / (iss[k] / 1000) if iss[k] > 0 else None
    o.append('> P(m\u00e1x.) \u2248 ' + N.fmt(ps[k] * 1000, 3) + ' mW')
    if rk is not None:
        o.append('Resist\u00eancia de carga nesse ponto: R = U / I \u2248 ' +
                 N.fmt(rk, 2) + ' \u03a9')
    if er is not None and A is not None:
        N.pos(er[0], 'A irradi\u00e2ncia')
        N.pos(A[0], 'A \u00e1rea')
        pr = er[0] * A[0] / 1e4
        o += ['P(radia\u00e7\u00e3o) = Er A = ' + N.fmt(pr, 2) + ' W',
              '> \u03b7(m\u00e1x.) = P(m\u00e1x.) / P(rad) ' + X + ' 100 % \u2248 ' +
              N.fmt(ps[k] / pr * 100, 2) + ' %']
    st = 'A pot\u00eancia el\u00e9trica depende da resist\u00eancia ligada ao ' \
        'painel: h\u00e1 um valor de R que a torna m\u00e1xima.\nO rendimento ' \
        'compara a pot\u00eancia el\u00e9trica com a da radia\u00e7\u00e3o que chega.'
    return ('\n'.join(o), st, ps[k], 'W',
            ('P (mW) em fun\u00e7\u00e3o de U (V)',
             [('p', [(us[i], ps[i] * 1000) for i in range(len(us))], 5)],
             0.0, max(us) * 1.1 or 1.0, 0.0, max(ps) * 1100 or 1.0,
             'pontos: medidos'))

# ------------------------------------------------------------ AL 3.2


def cap():
    return ('AL 3.2 Capacidade t\u00e9rmica m\u00e1ssica',
            [N.fld('Massa do bloco m', 'g kg', ''),
             N.fld('Pot\u00eancia P (ou U ' + X + ' I) em W', '', ''),
             N.fld('Tempos t (s)', '', '', 'l'),
             N.fld('Temperaturas \u03b8 (\u00b0C)', '', '', 'l'),
             N.fld('Valor tabelado de c (opcional)', '', '', 'o')], _cap)


def _cap(v):
    m, P, ts, ths, ref = v
    N.pos(m[0], 'A massa')
    N.pos(P[0], 'A pot\u00eancia')
    xs, ys = pares(ts, ths, 't', '\u03b8')
    a, b, r = fit(xs, ys)
    N.need(a > 0, 'A temperatura n\u00e3o sobe: confirma os dados')
    mk = m[0] / 1000
    c = P[0] / (mk * a)
    o = ['= \u03b8 = a t + b (m\u00ednimos quadrados)',
         'a = ' + N.fmt(a, 4) + ' \u00b0C/s; b = ' + N.fmt(b, 4) + ' \u00b0C']
    if r is not None:
        o.append('r = ' + N.fix(r, 4))
    o += ['P = m c a, logo c = P / (m a)',
          '> c ' + N.eq(c, 3) + ' J kg\u207b\u00b9 K\u207b\u00b9']
    if ref is not None:
        N.pos(ref[0], 'O valor tabelado')
        o.append(erro(c, ref[0]))
        if c > ref[0]:
            o.append('c maior do que o tabelado: parte da energia foi '
                     'para a vizinhan\u00e7a (isolamento imperfeito).')
    st = 'Toda a energia el\u00e9trica (P \u0394t) aqueceria o bloco se n\u00e3o ' \
        'houvesse perdas: P \u0394t = m c \u0394\u03b8.\nUsa s\u00f3 a parte em que ' \
        '\u03b8(t) \u00e9 uma reta.'
    return ('\n'.join(o), st, c, 'J/(kg K)',
            ('\u03b8 (\u00b0C) em fun\u00e7\u00e3o de t (s)',
             [('p', list(zip(xs, ys)), 5), ('f', lambda x: a * x + b, 2)],
             min(xs) - 5, max(xs) + 5, min(ys) - 2, max(ys) + 2,
             'pontos: medidos \u00b7 linha: regress\u00e3o'))

# ------------------------------------------------------------ AL 3.3


def fusao():
    return ('AL 3.3 Fus\u00e3o do gelo',
            [N.fld('Massa de \u00e1gua m(\u00e1gua)', 'g kg', ''),
             N.fld('Temperatura inicial da \u00e1gua (\u00b0C)', '', ''),
             N.fld('Massa de gelo a 0 \u00b0C m(gelo)', 'g kg', ''),
             N.fld('Temperatura final de equil\u00edbrio (\u00b0C)', '', '')], _fusao)


def _fusao(v):
    ma, ti, mg, tf = v
    N.pos(ma[0], 'A massa de \u00e1gua')
    N.pos(mg[0], 'A massa de gelo')
    N.need(0 <= tf[0] < ti[0], 'A temperatura final tem de estar entre 0 '
           '\u00b0C e a inicial')
    a = ma[0] / 1000
    g = mg[0] / 1000
    s = N.sfv(ma, ti, mg, tf)
    q1 = a * CA * (ti[0] - tf[0])
    q2 = g * CA * tf[0]
    h = (q1 - q2) / g
    N.need(h > 0, 'Dados incoerentes: a energia para fundir o gelo d\u00e1 '
           'negativa')
    o = ['Cedida pela \u00e1gua: m c (\u03b8i - \u03b8f) = ' + N.q(q1, s, 'J'),
         'Para aquecer o gelo fundido at\u00e9 \u03b8f: ' + N.q(q2, s, 'J'),
         '= \u0394Hf = (cedida - aquecimento) / m(gelo)',
         N.res('\u0394Hf', h, 'J kg\u207b\u00b9', s),
         'Valor tabelado: 3,34 ' + X + ' 10\u2075 J kg\u207b\u00b9', erro(h, HF)]
    st = 'Sistema isolado: a energia cedida pela \u00e1gua quente funde o ' \
        'gelo e aquece a \u00e1gua que dele resulta.\nc(\u00e1gua) = 4,18 ' + \
        X + ' 10\u00b3 J kg\u207b\u00b9 K\u207b\u00b9.'
    return ('\n'.join(o), st, h, 'J/kg')
