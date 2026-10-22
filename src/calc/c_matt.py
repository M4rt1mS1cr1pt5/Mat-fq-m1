# c_matt.py - M1TR4M: calculadoras de geometria sintetica: pontos
# notaveis com desenho, circunferencias inscrita e circunscrita, reta
# de Euler e circunferencia dos nove pontos, Pitagoras e semelhanca.
# Notacao das aulas: I incentro, C circuncentro, O ortocentro,
# B baricentro; o triangulo chama-se [PQR] para nao haver confusao.
#@ c_matt.pn|Pontos not\u00e1veis do tri\u00e2ngulo (com desenho)|pontos not\u00e1veis incentro circuncentro ortocentro baricentro reta de euler nove pontos tri\u00e2ngulo coordenadas|M|m3
#@ c_matt.insc|Circunfer\u00eancias inscrita e circunscrita|raio da circunfer\u00eancia inscrita r = 2a/p circunscrita tri\u00e2ngulo ret\u00e2ngulo hipotenusa incentro|M|m3
#@ c_matt.euler|Reta de Euler e nove pontos|reta de euler ob = 2bc circunfer\u00eancia dos nove pontos raio r/2 centro|M|m3
#@ c_matt.pit|Teorema de Pit\u00e1goras|pit\u00e1goras hipotenusa catetos tri\u00e2ngulo ret\u00e2ngulo|M|mr
#@ c_matt.sem|Semelhan\u00e7a de figuras|semelhan\u00e7a raz\u00e3o de semelhan\u00e7a amplia\u00e7\u00e3o redu\u00e7\u00e3o \u00e1reas lados correspondentes|M|mr
# Casos-limite: pontos repetidos ou colineares (nao ha triangulo),
# coordenadas a mais ou a menos, triangulo equilatero (sem reta de
# Euler), hipotenusa menor do que um cateto, medidas nulas ou negativas.

import math
import m1_nucleo as N

X = N.X
PI = '\u03c0'


def ok3(v):
    for x in v:
        if x is not None:
            N.pos(x[0], 'Cada medida')


def um(v, nome):
    f = [i for i in range(len(v)) if v[i] is None]
    N.need(len(f) == 1, 'Deixa vazio s\u00f3 o campo que queres calcular (' +
           nome + ')')
    return f[0]


def fx(v):
    # Coordenada: forma exata quando existe, senao decimal.
    e = N.exact(v)
    return e if e is not None else N.fmt(v, 0, -1)


def ptx(p):
    a, b = fx(p[0]), fx(p[1])
    return '(' + a + ('; ' if ',' in a + b else ', ') + b + ')'


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def lado(nm, v):
    return nm + ' ' + N.rhs(v)

# ------------------------------------------------------------ pontos


def pn():
    return ('Pontos not\u00e1veis',
            [N.fld('V\u00e9rtice P (x y)', '', '0 0', 'l'),
             N.fld('V\u00e9rtice Q (x y)', '', '6 0', 'l'),
             N.fld('V\u00e9rtice R (x y)', '', '2 4', 'l')], _pn)


def onde(p, a, b, c, e):
    # 'i' interior, 'f' fronteira, 'v' vertice, 'e' exterior.
    for q in (a, b, c):
        if dist(p, q) < e:
            return 'v'
    s = []
    for u, w in ((a, b), (b, c), (c, a)):
        s.append((w[0] - u[0]) * (p[1] - u[1]) - (w[1] - u[1]) * (p[0] - u[0]))
    k = max([abs(x) for x in s]) * 1e-9 + 1e-12
    if min(s) > k or max(s) < -k:
        return 'i'
    if min(s) >= -k or max(s) <= k:
        return 'f'
    return 'e'


def _pn(v):
    ps = []
    for i in range(3):
        N.need(len(v[i]) == 2, 'Escreve as duas coordenadas de cada '
               'v\u00e9rtice, por exemplo 2 3')
        ps.append((v[i][0][0], v[i][1][0]))
    P, Q, R = ps
    a = dist(Q, R)
    b = dist(P, R)
    c = dist(P, Q)
    ar = abs((Q[0] - P[0]) * (R[1] - P[1]) - (Q[1] - P[1]) * (R[0] - P[0])) / 2
    s = max(a, b, c)
    N.need(s > 0 and ar > 1e-9 * s * s, 'Os tr\u00eas pontos est\u00e3o alinhados '
           '(ou repetidos): n\u00e3o h\u00e1 tri\u00e2ngulo')
    pe = a + b + c
    e = 1e-7 * s
    G = ((P[0] + Q[0] + R[0]) / 3, (P[1] + Q[1] + R[1]) / 3)
    I = ((a * P[0] + b * Q[0] + c * R[0]) / pe,
         (a * P[1] + b * Q[1] + c * R[1]) / pe)
    d = 2 * (P[0] * (Q[1] - R[1]) + Q[0] * (R[1] - P[1]) + R[0] * (P[1] - Q[1]))
    s1 = P[0] ** 2 + P[1] ** 2
    s2 = Q[0] ** 2 + Q[1] ** 2
    s3 = R[0] ** 2 + R[1] ** 2
    C = ((s1 * (Q[1] - R[1]) + s2 * (R[1] - P[1]) + s3 * (P[1] - Q[1])) / d,
         (s1 * (R[0] - Q[0]) + s2 * (P[0] - R[0]) + s3 * (Q[0] - P[0])) / d)
    O = (P[0] + Q[0] + R[0] - 2 * C[0], P[1] + Q[1] + R[1] - 2 * C[1])
    rr = dist(C, P)
    r = 2 * ar / pe
    ls = sorted([a, b, c])
    iguais = (abs(ls[0] - ls[1]) < e) + (abs(ls[1] - ls[2]) < e)
    tl = 'equil\u00e1tero' if iguais == 2 else ('is\u00f3sceles' if iguais else
                                            'escaleno')
    q2 = ls[2] ** 2 - ls[0] ** 2 - ls[1] ** 2
    ta = 'ret\u00e2ngulo' if abs(q2) < 1e-7 * ls[2] ** 2 else (
        'obtus\u00e2ngulo' if q2 > 0 else 'acut\u00e2ngulo')
    o = [lado('PQ', c), lado('QR', a), lado('PR', b),
         'Tri\u00e2ngulo ' + tl + ' e ' + ta + '.',
         '\u00c1rea ' + N.rhs(ar) + '; per\u00edmetro ' + N.rhs(pe),
         '> B (baricentro) = ' + ptx(G),
         '> I (incentro) = ' + ptx(I), 'r = 2A / P ' + N.rhs(r),
         '> C (circuncentro) = ' + ptx(C), 'R ' + N.rhs(rr),
         '> O (ortocentro) = ' + ptx(O)]
    nm = {'i': 'interior', 'f': 'num lado', 'v': 'num v\u00e9rtice',
          'e': 'exterior'}
    o.append('Posi\u00e7\u00e3o: C ' + nm[onde(C, P, Q, R, e)] + ', O ' +
             nm[onde(O, P, Q, R, e)] + '; I e B interiores.')
    if tl == 'equil\u00e1tero':
        o.append('Equil\u00e1tero: os quatro pontos coincidem; n\u00e3o h\u00e1 '
                 'reta de Euler.')
    else:
        ob = dist(O, G)
        bc = dist(G, C)
        o += ['Reta de Euler: OB ' + N.rhs(ob) + '; BC ' + N.rhs(bc),
              '(OB = 2 BC e OC = 3 BC)']
        if tl == 'is\u00f3sceles':
            o.append('Is\u00f3sceles: I tamb\u00e9m est\u00e1 na reta de Euler '
                     '(mediatriz da base).')
    Nn = ((O[0] + C[0]) / 2, (O[1] + C[1]) / 2)
    o.append('Nove pontos: centro N = ' + ptx(Nn) + ' (meio de [OC]); raio '
             'R/2 ' + N.rhs(rr / 2))
    xs = [p[0] for p in (P, Q, R, G, I, C, O)]
    ys = [p[1] for p in (P, Q, R, G, I, C, O)]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w = max(x1 - x0, 2.1 * (y1 - y0), 1e-9) * 1.2
    h = w / 2.1
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    g = ('Tri\u00e2ngulo [PQR] e pontos not\u00e1veis',
         [('s', [(P[0], P[1], Q[0], Q[1]), (Q[0], Q[1], R[0], R[1]),
                 (R[0], R[1], P[0], P[1])], 0),
          ('s', [(O[0], O[1], C[0], C[1])] if tl != 'equil\u00e1tero' else [], 6),
          ('p', [G, I, C, O], 5),
          ('t', [(P[0], P[1], 'P'), (Q[0], Q[1], 'Q'), (R[0], R[1], 'R')], 2),
          ('t', [(G[0], G[1], 'B'), (I[0], I[1], 'I'), (C[0], C[1], 'C'),
                 (O[0], O[1], 'O')], 5)],
         cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2,
         'verde: reta de Euler')
    st = 'B: interse\u00e7\u00e3o das medianas; I: das bissetrizes; C: das ' \
        'mediatrizes; O: das alturas.\nB = (P + Q + R) / 3; O, B e C ' \
        'est\u00e3o na reta de Euler, com OB = 2 BC.'
    return ('\n'.join(o), st, rr, '', g)

# ------------------------------------------------------------ inscrita


def insc():
    return ('Circunfer\u00eancias inscrita e circunscrita',
            [N.fld('Dados', '', '', 'c', ['\u00e1rea e per\u00edmetro (r = 2A/P)',
                                         'tri\u00e2ngulo ret\u00e2ngulo (catetos)']),
             N.fld('\u00c1rea A (ou cateto a)', '', '', 'o'),
             N.fld('Per\u00edmetro P (ou cateto b)', '', '', 'o'),
             N.fld('Raio da inscrita r (s\u00f3 com A e P)', '', '', 'o')], _insc)


def _insc(v):
    k, A, P, r = v
    ok3((A, P, r))
    if k == 0:
        j = um([A, P, r], 'A, P ou r')
        o = ['= r = 2A / P (unindo I aos v\u00e9rtices: tr\u00eas tri\u00e2ngulos '
             'de altura r)']
        if j == 2:
            x = 2 * A[0] / P[0]
            o.append('> r ' + N.rhs(x))
        elif j == 1:
            x = 2 * A[0] / r[0]
            o.append('> P = 2A / r ' + N.rhs(x))
        else:
            x = r[0] * P[0] / 2
            o.append('> A = r P / 2 ' + N.rhs(x))
        rr = x if j == 2 else r[0]
        o += ['Comprimento da inscrita: 2' + PI + 'r ' + N.rhs(2 * math.pi * rr),
              '\u00c1rea do c\u00edrculo inscrito: ' + PI + 'r\u00b2 ' +
              N.rhs(math.pi * rr * rr)]
        st = 'r = 2A / P vale para qualquer tri\u00e2ngulo.'
        return ('\n'.join(o), st, x, '')
    N.need(A is not None and P is not None and r is None, 'Escreve os dois '
           'catetos (nos dois primeiros campos)')
    a, b = A[0], P[0]
    c = math.sqrt(a * a + b * b)
    ar = a * b / 2
    ri = (a + b - c) / 2
    o = ['Hipotenusa: c = \u221a(a\u00b2 + b\u00b2) ' + N.rhs(c),
         '\u00c1rea ' + N.rhs(ar) + '; per\u00edmetro ' + N.rhs(a + b + c),
         '= r = (a + b - c) / 2', '> r ' + N.rhs(ri),
         '= R = c / 2 (C \u00e9 o ponto m\u00e9dio da hipotenusa)',
         '> R ' + N.rhs(c / 2),
         'Nove pontos: raio R/2 ' + N.rhs(c / 4),
         'Verifica\u00e7\u00e3o: 2A / P ' + N.rhs(2 * ar / (a + b + c))]
    st = 'No tri\u00e2ngulo ret\u00e2ngulo, o circuncentro \u00e9 o ponto m\u00e9dio ' \
        'da hipotenusa e o ortocentro \u00e9 o v\u00e9rtice do \u00e2ngulo reto.'
    return ('\n'.join(o), st, ri, '')

# ------------------------------------------------------------ Euler


def euler():
    return ('Reta de Euler e nove pontos',
            [N.fld('Conhe\u00e7o', '', '', 'c',
                   ['OB (ortocentro-baricentro)', 'BC (baricentro-circuncentro)',
                    'OC (ortocentro-circuncentro)', 'R (circunscrita)',
                    'r\u2089 (nove pontos)']),
             N.fld('Valor', '', '')], _euler)


def _euler(v):
    k, x = v
    N.pos(x[0], 'O valor')
    x = x[0]
    o = []
    if k <= 2:
        bc = (x / 2, x, x / 3)[k]
        o += ['Ordem na reta: O, N, B, C, com ON : NB : BC = 3 : 1 : 2',
              'BC ' + N.rhs(bc), 'OB = 2 BC ' + N.rhs(2 * bc),
              'OC = 3 BC ' + N.rhs(3 * bc),
              'N (centro dos nove pontos) \u00e9 o ponto m\u00e9dio de [OC]:',
              'ON ' + N.rhs(1.5 * bc) + '; NB ' + N.rhs(0.5 * bc)]
        r = bc
    else:
        R = x if k == 3 else 2 * x
        o += ['R ' + N.rhs(R) + '; r\u2089 = R / 2 ' + N.rhs(R / 2),
              'Circunscrita: comprimento 2' + PI + 'R ' + N.rhs(2 * math.pi * R) +
              '; \u00e1rea ' + N.rhs(math.pi * R * R),
              'Nove pontos: comprimento ' + N.rhs(math.pi * R) + '; \u00e1rea ' +
              N.rhs(math.pi * R * R / 4)]
        r = R / 2
    st = 'A circunfer\u00eancia dos nove pontos passa pelos p\u00e9s das alturas, ' \
        'pelos pontos m\u00e9dios dos lados e pelos pontos m\u00e9dios de [OP], ' \
        '[OQ] e [OR].\nCentro: ponto m\u00e9dio de [OC]; raio: R / 2.'
    return ('\n'.join(o), st, r, '')

# ------------------------------------------------------------ Pitagoras


def pit():
    return ('Teorema de Pit\u00e1goras',
            [N.fld('Cateto a', '', '', 'o'),
             N.fld('Cateto b', '', '', 'o'),
             N.fld('Hipotenusa c', '', '', 'o')], _pit)


def _pit(v):
    a, b, c = v
    k = um(v, 'a, b ou c')
    ok3(v)
    o = ['= c\u00b2 = a\u00b2 + b\u00b2']
    if k == 2:
        r = math.sqrt(a[0] ** 2 + b[0] ** 2)
        o.append('> c = \u221a(a\u00b2 + b\u00b2) ' + N.rhs(r))
    else:
        o2 = b if k == 0 else a
        N.need(c[0] > o2[0], 'A hipotenusa tem de ser maior do que cada '
               'cateto')
        r = math.sqrt(c[0] ** 2 - o2[0] ** 2)
        o.append('> ' + ('a' if k == 0 else 'b') + ' = \u221a(c\u00b2 - ' +
                 ('b' if k == 0 else 'a') + '\u00b2) ' + N.rhs(r))
    st = 'S\u00f3 vale em tri\u00e2ngulos ret\u00e2ngulos; a hipotenusa \u00e9 o lado ' \
        'oposto ao \u00e2ngulo reto (o maior).'
    return ('\n'.join(o), st, r, '')

# ------------------------------------------------------------ semelhanca


def sem():
    return ('Semelhan\u00e7a',
            [N.fld('Lado da figura original', '', ''),
             N.fld('Lado correspondente na nova figura', '', ''),
             N.fld('Outro comprimento da original (opcional)', '', '', 'o'),
             N.fld('\u00c1rea da original (opcional)', '', '', 'o')], _sem)


def _sem(v):
    a, b, x, s = v
    ok3(v)
    k = b[0] / a[0]
    o = ['= k = lado novo / lado original', '> k ' + N.rhs(k),
         'k > 1: amplia\u00e7\u00e3o.' if k > 1 else ('k < 1: redu\u00e7\u00e3o.' if k < 1
                                                 else 'k = 1: figuras '
                                                 'congruentes.')]
    if x is not None:
        o.append('Comprimento correspondente: k ' + X + ' ' + N.fmt(x[0]) + ' ' +
                 N.rhs(k * x[0]))
    if s is not None:
        o.append('\u00c1rea da nova figura: k\u00b2 ' + X + ' ' + N.fmt(s[0]) + ' ' +
                 N.rhs(k * k * s[0]))
    st = 'Em figuras semelhantes, os comprimentos multiplicam-se por k e ' \
        'as \u00e1reas por k\u00b2.\nCrit\u00e9rio AA: dois \u00e2ngulos iguais bastam ' \
        'para dois tri\u00e2ngulos serem semelhantes.'
    return ('\n'.join(o), st, k, '')
