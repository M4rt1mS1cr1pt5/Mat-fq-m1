# c_fqen.py - M1TR4M: calculadoras de energia e movimentos: energia
# mecanica, conservacao, trabalho, teorema da energia cinetica, potencia
# e rendimento.
#@ c_fqen.em|Energia cin\u00e9tica, potencial e mec\u00e2nica|energia cin\u00e9tica energia potencial grav\u00edtica energia mec\u00e2nica massa velocidade altura n\u00edvel de refer\u00eancia|F|f1
#@ c_fqen.cons|Conserva\u00e7\u00e3o da energia mec\u00e2nica|conserva\u00e7\u00e3o da energia mec\u00e2nica altura velocidade queda subida ressalto energia dissipada|F|f1
#@ c_fqen.tr|Trabalho de uma for\u00e7a constante|trabalho for\u00e7a deslocamento \u00e2ngulo potente resistente nulo componente eficaz|F|f1
#@ c_fqen.wp|Trabalho do peso|trabalho do peso for\u00e7a conservativa energia potencial grav\u00edtica desn\u00edvel trajet\u00f3ria|F|f1
#@ c_fqen.tec|Teorema da energia cin\u00e9tica|teorema da energia cin\u00e9tica trabalho da resultante varia\u00e7\u00e3o da energia cin\u00e9tica for\u00e7a resultante|F|f1
#@ c_fqen.pot|Pot\u00eancia|pot\u00eancia energia intervalo de tempo watt quilowatt-hora|F|f1
#@ c_fqen.ren|Rendimento|rendimento energia \u00fatil energia fornecida energia dissipada pot\u00eancia \u00fatil|F|f1
# Casos-limite: massa ou deslocamento nulos ou negativos, velocidade
# negativa (pede-se o modulo), angulo fora de 0 a 180 graus, altura que
# o corpo nao atinge (v^2 < 0), campos a mais ou a menos, rendimento
# acima de 100 % (impossivel) e energia util maior do que a fornecida.

import math
import m1_nucleo as N

X = N.X
MS = 'kg g'
VS = 'm/s km/h'
HS = 'm cm km'
ES = 'J kJ MJ Wh kWh'


def g():
    return N.CF.get('g', 10.0)


def gtxt():
    return 'g = ' + N.fmt(g()) + ' m s\u207b\u00b2 (muda nas Defini\u00e7\u00f5es)'


def pq(x, sf, u):
    # Valor com unidade; entre parenteses se for negativo.
    s = N.q(x, sf, u)
    return '(' + s + ')' if x < 0 else s


def um(v, nome):
    # Exatamente um campo vazio; devolve o seu indice.
    f = [i for i in range(len(v)) if v[i] is None]
    N.need(len(f) == 1, 'Deixa vazio s\u00f3 o campo que queres calcular (' +
           nome + ')')
    return f[0]

# ------------------------------------------------------------ energias


def em():
    return ('Energia mec\u00e2nica',
            [N.fld('Massa m', MS, ''),
             N.fld('Velocidade v (opcional)', VS, '', 'o'),
             N.fld('Altura h (opcional)', HS, '', 'o')], _em)


def _em(v):
    m, vv, h = v
    N.pos(m[0], 'A massa')
    N.need(vv is not None or h is not None, 'Escreve a velocidade, a altura '
           'ou as duas')
    o = []
    r = None
    ec = ep = 0.0
    if vv is not None:
        N.nneg(vv[0], 'A velocidade (m\u00f3dulo)')
        ec = 0.5 * m[0] * vv[0] ** 2
        o += ['= Ec = \u00bd m v\u00b2 = \u00bd ' + X + ' ' + N.q(m[0], m[1], 'kg') + ' ' +
              X + ' (' + N.q(vv[0], vv[1], 'm s\u207b\u00b9') + ')\u00b2',
              N.res('Ec', ec, 'J', N.sfv(m, vv))]
        r = ec
    if h is not None:
        ep = m[0] * g() * h[0]
        o += ['= Epg = m g h = ' + N.q(m[0], m[1], 'kg') + ' ' + X + ' ' +
              N.q(g(), 0, 'm s\u207b\u00b2') + ' ' + X + ' ' + pq(h[0], h[1], 'm'),
              N.res('Epg', ep, 'J', N.sfv(m, h))]
        r = ep
    if vv is not None and h is not None:
        r = ec + ep
        o += ['= Em = Ec + Epg', N.res('Em', r, 'J', N.sfv(m, vv, h))]
    if h is not None and h[0] < 0:
        o.append('h < 0: o corpo est\u00e1 abaixo do n\u00edvel de refer\u00eancia.')
    st = 'Ec = \u00bd m v\u00b2 (m em kg, v em m/s).\nEpg = m g h, com h medida a ' \
        'partir do n\u00edvel de refer\u00eancia (Epg = 0).\nEm = Ec + Epg.\n' + gtxt()
    return ('\n'.join(o), st, r, 'J')


def cons():
    return ('Conserva\u00e7\u00e3o da energia mec\u00e2nica',
            [N.fld('Altura inicial hA', HS, '', 'o'),
             N.fld('Velocidade inicial vA', VS, '0', 'o'),
             N.fld('Altura final hB', HS, '0', 'o'),
             N.fld('Velocidade final vB', VS, '', 'o'),
             N.fld('Massa m (s\u00f3 com energia dissipada)', MS, '', 'o'),
             N.fld('Energia dissipada Ed (opcional)', 'J kJ', '', 'o')], _cons)


def _cons(v):
    ha, va, hb, vb, m, ed = v
    falta = [i for i in range(4) if v[i] is None]
    N.need(len(falta) <= 1, 'Deixa vazio s\u00f3 o campo que queres calcular '
           '(ou nenhum, para calcular a energia dissipada)')
    for x, nm in ((va, 'A velocidade inicial'), (vb, 'A velocidade final')):
        if x is not None:
            N.nneg(x[0], nm + ' (m\u00f3dulo)')
    if m is not None:
        N.pos(m[0], 'A massa')
    s = N.sfv(*v)
    gg = g()
    o = []
    if not falta:
        N.need(ed is None, 'Com os quatro campos preenchidos, a energia '
               'dissipada \u00e9 o resultado: deixa-a vazia')
        ea = 0.5 * va[0] ** 2 + gg * ha[0]
        eb = 0.5 * vb[0] ** 2 + gg * hb[0]
        o += ['= Em/m = \u00bd v\u00b2 + g h (por kg)',
              'A: ' + N.fmt(ea, s) + ' J/kg; B: ' + N.fmt(eb, s) + ' J/kg']
        d = ea - eb
        if ea > 0:
            o.append(N.res('Dissipada', d / ea * 100, '% de Em(A)', s))
        if m is not None:
            o.append(N.res('Ed', d * m[0], 'J', s))
        if d < 0:
            o.append('! A energia mec\u00e2nica aumentou: houve uma for\u00e7a a '
                     'fornecer energia (por exemplo, um motor).')
        st = 'Ed = Em(A) - Em(B). Sem a massa, a app d\u00e1 a energia por kg ' \
            'e a percentagem.\n' + gtxt()
        return ('\n'.join(o), st, d, 'J/kg')
    w = 0.0
    if ed is not None:
        N.nneg(ed[0], 'A energia dissipada')
        N.need(m is not None, 'Com energia dissipada, escreve tamb\u00e9m a massa')
        w = ed[0] / m[0]
        o.append('= \u00bd m vA\u00b2 + m g hA - Ed = \u00bd m vB\u00b2 + m g hB')
    else:
        o.append('= \u00bd m vA\u00b2 + m g hA = \u00bd m vB\u00b2 + m g hB')
        o.append('A massa aparece nos dois membros e corta-se.')
    k = falta[0]
    if k == 3:
        q = va[0] ** 2 + 2 * gg * (ha[0] - hb[0]) - 2 * w
        N.need(q >= 0, 'Com estes dados o corpo n\u00e3o chega \u00e0 altura final')
        r = math.sqrt(q)
        o += ['vB = \u221a(vA\u00b2 + 2 g (hA - hB)' + (' - 2 Ed/m' if w else '') + ')',
              N.res('vB', r, 'm s\u207b\u00b9', s)]
        u = 'm/s'
    elif k == 1:
        q = vb[0] ** 2 + 2 * gg * (hb[0] - ha[0]) + 2 * w
        N.need(q >= 0, 'Com estes dados n\u00e3o h\u00e1 velocidade inicial poss\u00edvel')
        r = math.sqrt(q)
        o += ['vA = \u221a(vB\u00b2 + 2 g (hB - hA)' + (' + 2 Ed/m' if w else '') + ')',
              N.res('vA', r, 'm s\u207b\u00b9', s)]
        u = 'm/s'
    elif k == 2:
        r = ha[0] + (va[0] ** 2 - vb[0] ** 2) / (2 * gg) - w / gg
        o += ['hB = hA + (vA\u00b2 - vB\u00b2) / (2 g)' + (' - Ed/(m g)' if w else ''),
              N.res('hB', r, 'm', s)]
        u = 'm'
    else:
        r = hb[0] + (vb[0] ** 2 - va[0] ** 2) / (2 * gg) + w / gg
        o += ['hA = hB + (vB\u00b2 - vA\u00b2) / (2 g)' + (' + Ed/(m g)' if w else ''),
              N.res('hA', r, 'm', s)]
        u = 'm'
    st = 'S\u00f3 atuam for\u00e7as conservativas (ou for\u00e7as que n\u00e3o realizam ' \
        'trabalho): Em(A) = Em(B).\nCom for\u00e7as n\u00e3o conservativas: ' \
        'Em(B) = Em(A) - Ed.\n' + gtxt()
    return ('\n'.join(o), st, r, u)

# ------------------------------------------------------------ trabalho


def tr():
    return ('Trabalho de uma for\u00e7a constante',
            [N.fld('Intensidade da for\u00e7a F', 'N kN', ''),
             N.fld('Deslocamento d', HS, ''),
             N.fld('\u00c2ngulo \u03b1 entre F e d (graus)', '', '0')], _tr)


def _tr(v):
    F, d, a = v
    N.pos(F[0], 'A for\u00e7a')
    N.pos(d[0], 'O deslocamento')
    N.need(0 <= a[0] <= 180, 'O \u00e2ngulo tem de estar entre 0\u00b0 e 180\u00b0')
    c = math.cos(a[0] * math.pi / 180)
    if abs(c) < 1e-12:
        c = 0.0
    w = F[0] * d[0] * c
    s = N.sfv(F, d)
    o = ['= W = F d cos \u03b1 = ' + N.q(F[0], F[1], 'N') + ' ' + X + ' ' +
         N.q(d[0], d[1], 'm') + ' ' + X + ' cos ' + N.fmt(a[0]) + '\u00b0',
         N.res('W', w, 'J', s),
         'Componente eficaz: F cos \u03b1 = ' + N.q(F[0] * c, s, 'N')]
    if c > 0:
        o.append('Trabalho potente (W > 0): a for\u00e7a favorece o movimento.')
    elif c == 0:
        o.append('Trabalho nulo: a for\u00e7a \u00e9 perpendicular ao deslocamento.')
    else:
        o.append('Trabalho resistente (W < 0): a for\u00e7a op\u00f5e-se ao '
                 'movimento.')
    st = 'S\u00f3 a componente da for\u00e7a na dire\u00e7\u00e3o do deslocamento realiza ' \
        'trabalho.\n0\u00b0 \u2264 \u03b1 < 90\u00b0: potente; \u03b1 = 90\u00b0: nulo; 90\u00b0 < \u03b1 \u2264 180\u00b0: ' \
        'resistente.'
    return ('\n'.join(o), st, w, 'J')


def wp():
    return ('Trabalho do peso',
            [N.fld('Massa m', MS, ''),
             N.fld('Altura inicial hi', HS, ''),
             N.fld('Altura final hf', HS, '0')], _wp)


def _wp(v):
    m, hi, hf = v
    N.pos(m[0], 'A massa')
    s = N.sfv(m, hi, hf)
    w = m[0] * g() * (hi[0] - hf[0])
    o = ['= W(P) = m g (hi - hf) = -\u0394Epg',
         'P = m g = ' + N.q(m[0] * g(), m[1], 'N'),
         N.res('W(P)', w, 'J', s), N.res('\u0394Epg', -w, 'J', s)]
    if w > 0:
        o.append('O corpo desce: trabalho potente e a Epg diminui.')
    elif w < 0:
        o.append('O corpo sobe: trabalho resistente e a Epg aumenta.')
    else:
        o.append('Mesma altura: o trabalho do peso \u00e9 nulo.')
    st = 'O peso \u00e9 uma for\u00e7a conservativa: o trabalho s\u00f3 depende do ' \
        'desn\u00edvel, n\u00e3o da trajet\u00f3ria.\nW(P) = -\u0394Epg.\n' + gtxt()
    return ('\n'.join(o), st, w, 'J')


def tec():
    return ('Teorema da energia cin\u00e9tica',
            [N.fld('Massa m', MS, ''),
             N.fld('Velocidade inicial vi', VS, '', 'o'),
             N.fld('Velocidade final vf', VS, '', 'o'),
             N.fld('Trabalho da resultante W', 'J kJ', '', 'o'),
             N.fld('Deslocamento d (opcional)', HS, '', 'o')], _tec)


def _tec(v):
    m, vi, vf, w, d = v
    N.pos(m[0], 'A massa')
    k = um(v[1:4], 'vi, vf ou W') + 1
    for x, nm in ((vi, 'A velocidade inicial'), (vf, 'A velocidade final')):
        if x is not None:
            N.nneg(x[0], nm + ' (m\u00f3dulo)')
    s = N.sfv(*v[:4])
    o = ['= W(resultante) = \u0394Ec = \u00bd m vf\u00b2 - \u00bd m vi\u00b2']
    if k == 3:
        r = 0.5 * m[0] * (vf[0] ** 2 - vi[0] ** 2)
        wr = r
        o.append(N.res('W', r, 'J', s))
        u = 'J'
    elif k == 2:
        q = vi[0] ** 2 + 2 * w[0] / m[0]
        N.need(q >= 0, 'O corpo para antes: o trabalho resistente \u00e9 maior '
               'do que a energia cin\u00e9tica inicial')
        r = math.sqrt(q)
        wr = w[0]
        o += ['vf = \u221a(vi\u00b2 + 2 W / m)', N.res('vf', r, 'm s\u207b\u00b9', s)]
        u = 'm/s'
    else:
        q = vf[0] ** 2 - 2 * w[0] / m[0]
        N.need(q >= 0, 'N\u00e3o h\u00e1 velocidade inicial poss\u00edvel com estes dados')
        r = math.sqrt(q)
        wr = w[0]
        o += ['vi = \u221a(vf\u00b2 - 2 W / m)', N.res('vi', r, 'm s\u207b\u00b9', s)]
        u = 'm/s'
    if wr > 0:
        o.append('W > 0: a energia cin\u00e9tica aumenta.')
    elif wr < 0:
        o.append('W < 0: a energia cin\u00e9tica diminui.')
    if d is not None:
        N.pos(d[0], 'O deslocamento')
        o += ['Se a resultante tiver a dire\u00e7\u00e3o do deslocamento:',
              N.res('F(R)', abs(wr) / d[0], 'N', N.sfm(s, d[1]))]
    st = 'O trabalho da resultante das for\u00e7as \u00e9 igual \u00e0 varia\u00e7\u00e3o da ' \
        'energia cin\u00e9tica.\nW(R) = soma dos trabalhos de todas as for\u00e7as.'
    return ('\n'.join(o), st, r, u)

# ------------------------------------------------------------ potencia


def pot():
    return ('Pot\u00eancia',
            [N.fld('Energia E (vazio = calcular)', ES, '', 'o'),
             N.fld('Intervalo de tempo \u0394t', 's min h', '', 'o'),
             N.fld('Pot\u00eancia P', 'W kW mW MW', '', 'o')], _pot)


def _pot(v):
    e, t, p = v
    k = um(v, 'E, \u0394t ou P')
    for x, nm in ((e, 'A energia'), (t, 'O intervalo de tempo'),
                  (p, 'A pot\u00eancia')):
        if x is not None:
            N.pos(x[0], nm)
    s = N.sfv(*v)
    o = ['= P = E / \u0394t']
    if k == 0:
        r = p[0] * t[0]
        o += ['E = P \u0394t', N.res('E', r, 'J', s),
              '= ' + N.fmt(r / 3.6e6, s) + ' kWh (1 kWh = 3,6 ' + X +
              ' 10\u2076 J)']
        u = 'J'
    elif k == 1:
        r = e[0] / p[0]
        o += ['\u0394t = E / P', N.res('\u0394t', r, 's', s)]
        if r >= 60:
            o.append('= ' + N.fmt(r / 60, s) + ' min = ' +
                     N.fmt(r / 3600, s) + ' h')
        u = 's'
    else:
        r = e[0] / t[0]
        o += [N.res('P', r, 'W', s)]
        u = 'W'
    st = 'Pot\u00eancia: energia transferida por unidade de tempo.\n' \
        'Unidades SI: E em J, \u0394t em s, P em W (1 W = 1 J/s).'
    return ('\n'.join(o), st, r, u)


def ren():
    return ('Rendimento',
            [N.fld('Energia (ou pot\u00eancia) \u00fatil', '', '', 'o'),
             N.fld('Energia (ou pot\u00eancia) fornecida', '', '', 'o'),
             N.fld('Rendimento \u03b7 (%)', '', '', 'o')], _ren)


def _ren(v):
    eu, ef, n = v
    k = um(v, '\u00fatil, fornecida ou \u03b7')
    for x, nm in ((eu, 'A energia \u00fatil'), (ef, 'A energia fornecida'),
                  (n, 'O rendimento')):
        if x is not None:
            N.pos(x[0], nm)
    s = N.sfv(*v)
    o = ['= \u03b7 = E(\u00fatil) / E(fornecida) ' + X + ' 100 %']
    if k == 2:
        N.need(eu[0] <= ef[0], '\u03b7 > 100 % \u00e9 imposs\u00edvel: a energia \u00fatil n\u00e3o '
               'pode ser maior do que a fornecida (trocaste-as?)')
        r = eu[0] / ef[0] * 100
        o.append(N.res('\u03b7', r, '%', s))
        a, b = eu[0], ef[0]
    else:
        N.need(n[0] <= 100, '\u03b7 > 100 % \u00e9 imposs\u00edvel')
        if k == 0:
            r = n[0] / 100 * ef[0]
            o += ['E(\u00fatil) = \u03b7 ' + X + ' E(fornecida) / 100',
                  N.res('E(\u00fatil)', r, '', s)]
            a, b = r, ef[0]
        else:
            r = eu[0] * 100 / n[0]
            o += ['E(fornecida) = E(\u00fatil) ' + X + ' 100 / \u03b7',
                  N.res('E(fornecida)', r, '', s)]
            a, b = eu[0], r
    o.append('Dissipada: ' + N.fmt(b - a, s) + ' (' +
             N.fmt((b - a) / b * 100, s) + ' % da fornecida)')
    o.append('Unidades: as da energia (ou pot\u00eancia) que escreveste.')
    st = 'E(fornecida) = E(\u00fatil) + E(dissipada).\nO rendimento \u00e9 sempre ' \
        'menor do que 100 %: h\u00e1 sempre energia dissipada.'
    return ('\n'.join(o), st, r, '%' if k == 2 else '')
