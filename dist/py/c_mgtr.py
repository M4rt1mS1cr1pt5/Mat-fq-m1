# c_mgtr.py - M1TR4M: resolvedores de geometria do 8.o e 9.o anos:
# isometrias no plano com coordenadas (translacao, reflexoes, rotacoes de
# 90 e 180 graus), com a regra (x, y) -> (x', y') e o desenho da figura e
# da imagem, e angulos na circunferencia (ao centro, inscrito, de
# vertice interior ou exterior, quadrilatero e poligono inscritos,
# comprimento do arco), com desenho.
#@ c_mgtr.iso|Isometrias: transla\u00e7\u00e3o, reflex\u00e3o e rota\u00e7\u00e3o|isometria transla\u00e7\u00e3o vetor reflex\u00e3o eixo de reflex\u00e3o simetria rota\u00e7\u00e3o centro meia-volta imagem de uma figura coordenadas|M|g8
#@ c_mgtr.circ|\u00c2ngulos na circunfer\u00eancia|circunfer\u00eancia \u00e2ngulo ao centro \u00e2ngulo inscrito arco \u00e2ngulo de segmento v\u00e9rtice no interior exterior quadril\u00e1tero inscrito pol\u00edgono regular inscrito comprimento do arco|M|g9
# Casos-limite: vertices mal escritos ou repetidos, parametro em falta,
# arcos que somam mais de 360 graus, arco exterior menor do que o
# interior, poligono com n nao inteiro, quadrilatero com angulo >= 180.

import math
import m1_nucleo as N
import m1_q as Q

G = '\u00b0'

# ------------------------------------------------------------ isometrias


OPI = ['Transla\u00e7\u00e3o (vetor a b)', 'Reflex\u00e3o no eixo Ox',
       'Reflex\u00e3o no eixo Oy', 'Reflex\u00e3o na reta x = k',
       'Reflex\u00e3o na reta y = k', 'Reflex\u00e3o na reta y = x',
       'Reflex\u00e3o na reta y = -x', 'Rota\u00e7\u00e3o de 90\u00b0 (sentido +)',
       'Rota\u00e7\u00e3o de 180\u00b0 (meia-volta)', 'Rota\u00e7\u00e3o de 90\u00b0 (sentido -)']


def iso():
    return ('Isometrias',
            [N.fld('V\u00e9rtices (ex.: 1 1; 4 1; 2 3)', '', '1 1; 4 1; 2 3', 't'),
             N.fld('Isometria', '', '', 'c', OPI),
             N.fld('Vetor (a b), centro (x y) ou k', '', '3 2', 't')], _iso)


def qn(t, nm):
    c = Q.cte(Q.poli(Q.arvore(t)))
    N.need(c is not None, nm + ': s\u00f3 n\u00fameros')
    return c


def nums(t, nm):
    return [qn(p, nm) for p in t.replace(';', ' ').split()]


def lin(a, b, c):
    # Polinomio a x + b y + c.
    p = {}
    for k, q in (((('x', 1),), a), ((('y', 1),), b), ((), c)):
        if q[0]:
            p[k] = q
    return p


def pts(t):
    ps = []
    for p in t.split(';'):
        if p.strip():
            c = nums(p, 'Os v\u00e9rtices')
            N.need(len(c) == 2, 'Escreve cada v\u00e9rtice com duas coordenadas, '
                   'separados por ; (ex.: 1 1; 4 1; 2 3)')
            ps.append(tuple(c))
    N.need(ps, 'Escreve pelo menos um ponto')
    N.need(len(ps) <= 12, 'No m\u00e1ximo 12 v\u00e9rtices')
    return ps


def ptx(p):
    return '(' + Q.vstr(p[0]) + Q.sepr(p[0], p[1]) + Q.vstr(p[1]) + ')'


def _iso(v):
    ps = pts(v[0])
    k = v[1]
    c = nums(v[2], 'O vetor, o centro ou k') if v[2].strip() else []
    um, z = Q.UM, Q.Z
    m = Q.neg(um)
    cen = None
    if k == 0:
        N.need(len(c) == 2, 'Escreve o vetor com duas coordenadas (ex.: 3 2)')
        T = (lin(um, z, c[0]), lin(z, um, c[1]))
        nm = 'Transla\u00e7\u00e3o associada ao vetor (' + Q.vstr(c[0]) + \
            Q.sepr(c[0], c[1]) + Q.vstr(c[1]) + ')'
    elif k in (3, 4):
        N.need(len(c) == 1, 'Escreve s\u00f3 o valor de k (ex.: 2)')
        d = Q.mul((2, 1), c[0])
        T = (lin(m, z, d), lin(z, um, z)) if k == 3 else \
            (lin(um, z, z), lin(z, m, d))
        nm = 'Reflex\u00e3o na reta ' + ('x' if k == 3 else 'y') + ' = ' + \
            Q.vstr(c[0])
    elif k in (1, 2, 5, 6):
        T = {1: (lin(um, z, z), lin(z, m, z)), 2: (lin(m, z, z), lin(z, um, z)),
             5: (lin(z, um, z), lin(um, z, z)),
             6: (lin(z, m, z), lin(m, z, z))}[k]
        nm = OPI[k]
    else:
        N.need(len(c) in (0, 2), 'Escreve o centro com duas coordenadas '
               '(vazio = origem)')
        cx, cy = c if c else (z, z)
        cen = (cx, cy)
        if k == 8:
            T = (lin(m, z, Q.mul((2, 1), cx)), lin(z, m, Q.mul((2, 1), cy)))
        elif k == 7:
            T = (lin(z, m, Q.add(cx, cy)), lin(um, z, Q.sub(cy, cx)))
        else:
            T = (lin(z, um, Q.sub(cx, cy)), lin(m, z, Q.add(cy, cx)))
        nm = OPI[k].split(' (')[0] + (' (sentido ' + ('positivo' if k == 7
                                                      else 'negativo') + ')'
                                      if k != 8 else '') + \
            ' de centro ' + ('O' if not c else ptx(cen))
    o = [nm + ':', '= (x, y) \u2192 (' + Q.pstr(T[0], ['x', 'y']) + ', ' +
         Q.pstr(T[1], ['x', 'y']) + ')']
    im = []
    for i in range(len(ps)):
        p = ps[i]
        d = {'x': p[0], 'y': p[1]}
        q = (Q.valor(T[0], d), Q.valor(T[1], d))
        im.append(q)
        L = chr(65 + i)
        o.append('> ' + L + ptx(p) + ' \u2192 ' + L + "'" + ptx(q))
    if k == 8:
        o.append('Rota\u00e7\u00e3o de 180\u00b0 = simetria central (reflex\u00e3o central).')
    o.append('Isometria: mant\u00e9m comprimentos e amplitudes; a imagem \u00e9 '
             'congruente com a figura.')
    o.append('Reflex\u00e3o: troca o sentido dos v\u00e9rtices.' if 1 <= k <= 6 else
             'Mant\u00e9m o sentido (a orienta\u00e7\u00e3o) dos v\u00e9rtices.')
    st = 'Transla\u00e7\u00e3o: soma-se o vetor. Reflex\u00e3o no eixo Ox: (x, -y); no ' \
        'eixo Oy: (-x, y).\nRota\u00e7\u00e3o de 90\u00b0 (sentido positivo, centro O): ' \
        '(-y, x); de 180\u00b0: (-x, -y).'
    return ('\n'.join(o), st, None, '', desenho(ps, im, k, c, cen, nm))


def desenho(ps, im, k, c, cen, nm):
    f = [(Q.qf(p[0]), Q.qf(p[1])) for p in ps]
    g = [(Q.qf(p[0]), Q.qf(p[1])) for p in im]
    xs = [p[0] for p in f + g]
    ys = [p[1] for p in f + g]
    if cen or 1 <= k <= 6:
        xs.append(Q.qf(cen[0]) if cen else 0.0)
        ys.append(Q.qf(cen[1]) if cen else 0.0)
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w = max(x1 - x0, 2.1 * (y1 - y0), 2.0) * 1.3
    h = w / 2.1
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    X0, X1, Y0, Y1 = mx - w / 2, mx + w / 2, my - h / 2, my + h / 2

    def poli(q):
        if len(q) < 2:
            return []
        n = len(q) if len(q) > 2 else 1
        return [(q[i][0], q[i][1], q[(i + 1) % len(q)][0],
                 q[(i + 1) % len(q)][1]) for i in range(n)]
    its = [('s', poli(f), 0), ('s', poli(g), 5), ('p', f, 0), ('p', g, 5),
           ('t', [(f[i][0], f[i][1], chr(65 + i)) for i in range(len(f))], 0),
           ('t', [(g[i][0], g[i][1], chr(65 + i) + "'") for i in
                  range(len(g))], 5)]
    if k == 0:
        its.append(('s', [(f[i][0], f[i][1], g[i][0], g[i][1]) for i in
                          range(len(f))], 7))
    elif k in (1, 4):
        y = 0.0 if k == 1 else Q.qf(c[0])
        its.append(('s', [(X0, y, X1, y)], 6))
    elif k in (2, 3):
        x = 0.0 if k == 2 else Q.qf(c[0])
        its.append(('s', [(x, Y0, x, Y1)], 6))
    elif k in (5, 6):
        s = 1 if k == 5 else -1
        a = max(abs(X0), abs(X1), abs(Y0), abs(Y1))
        its.append(('s', [(-a, -s * a, a, s * a)], 6))
    else:
        q = (Q.qf(cen[0]), Q.qf(cen[1]))
        its += [('p', [q], 6), ('t', [(q[0], q[1], 'O' if not c else 'C')],
                                6)]
    return (nm, its, X0, X1, Y0, Y1, 'preto: figura; vermelho: imagem')

# ------------------------------------------------------------ circunferencia


OPC = ['Dado o arco AB', 'Dado o \u00e2ngulo inscrito',
       'V\u00e9rtice interior (arcos a, b)', 'V\u00e9rtice exterior (arcos a, b)',
       'Quadril\u00e1tero inscrito (\u03b1, \u03b2)', 'Pol\u00edgono regular inscrito (n)',
       'Comprimento do arco (r, \u03b1)']


def circ():
    return ('\u00c2ngulos na circunfer\u00eancia',
            [N.fld('Calcular', '', '', 'c', OPC),
             N.fld('1.\u00ba dado (graus, n ou raio)', '', '80', 'o'),
             N.fld('2.\u00ba dado (graus)', '', '', 'o')], _circ)


def gt(x):
    # Amplitude em graus, exata quando possivel.
    return N.rhs(x, 2) + G


def nv(x):
    s, ex = N.fmt2(x, 0, -1)
    e = None if ex else N.exact(x)
    return (e or s) + G


def pc(t, r=3.0):
    # Ponto da circunferencia de centro (10, 10) no angulo t (graus).
    t = t * math.pi / 180
    return (10 + r * math.cos(t), 10 + r * math.sin(t))


def janela(nm, its, ps, leg):
    xs = [p[0] for p in ps] + [6.5, 13.5]
    ys = [p[1] for p in ps] + [6.5, 13.5]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w = max(x1 - x0, 2.1 * (y1 - y0)) * 1.1
    h = w / 2.1
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    cs = [pc(7.5 * i) for i in range(49)]
    its = [('s', [(cs[i][0], cs[i][1], cs[i + 1][0], cs[i + 1][1]) for i in
                  range(48)], 7)] + its
    return (nm, its, mx - w / 2, mx + w / 2, my - h / 2, my + h / 2, leg)


def segs(*ps):
    return [(ps[i][0], ps[i][1], ps[i + 1][0], ps[i + 1][1])
            for i in range(len(ps) - 1)]


def rot(ls):
    return [(p[0], p[1], t) for p, t in ls]


def _circ(v):
    k, a, b = v
    N.need(a is not None, 'Escreve o 1.\u00ba dado')
    a = a[0]
    o = []
    gr = None
    O = (10.0, 10.0)
    if k in (0, 1):
        N.pos(a, 'O dado')
        x = a if k == 0 else 2 * a
        N.need(x < 360, 'O arco tem de ser menor do que 360\u00b0' if k == 0 else
               'O \u00e2ngulo inscrito tem de ser menor do que 180\u00b0')
        if k == 1:
            o += ['= arco = 2 ' + N.X + ' \u00e2ngulo inscrito',
                  '> Arco AB = 2 ' + N.X + ' ' + nv(a) + ' ' + gt(x)]
        else:
            o.append('Arco AB = ' + nv(x))
        o += ['> \u00c2ngulo ao centro AOB ' + gt(x) + ' (igual ao arco)',
              '> \u00c2ngulo inscrito AVB ' + gt(x / 2) + ' (metade do arco)',
              '\u00c2ngulo de segmento (corda AB e tangente em A) ' + gt(x / 2),
              'Com o v\u00e9rtice no pr\u00f3prio arco AB: (360\u00b0 - ' + nv(x) + ') / 2 '
              + gt((360 - x) / 2)]
        if abs(x - 180) < 1e-9:
            o.append('Arco de 180\u00b0: o \u00e2ngulo inscrito numa semicircunfer\u00eancia'
                     ' \u00e9 reto.')
        A, B, V = pc(270 - x / 2), pc(270 + x / 2), pc(90)
        gr = janela('\u00c2ngulo ao centro e inscrito',
                    [('s', segs(A, O, B), 2), ('s', segs(A, V, B), 5),
                     ('t', rot([(A, 'A'), (B, 'B'), (O, 'O'), (V, 'V')]), 0)],
                    [A, B, V], 'azul: ao centro ' + nv(x) + '; vermelho: ' +
                    'inscrito ' + nv(x / 2))
        r = x / 2
    elif k in (2, 3):
        N.need(b is not None, 'Escreve os dois arcos')
        b = b[0]
        N.need(a > 0 and b >= 0, 'Os arcos t\u00eam de ser positivos')
        N.need(a + b <= 360, 'Os dois arcos somam no m\u00e1ximo 360\u00b0')
        if k == 2:
            r = (a + b) / 2
            o += ['= \u00e2ngulo = (a + b) / 2 (semissoma dos arcos)',
                  '> (' + nv(a) + ' + ' + nv(b) + ') / 2 ' + gt(r),
                  'a: arco entre os lados do \u00e2ngulo; b: arco entre os '
                  'prolongamentos dos lados.']
            x = (360 - a - b) / 2
            A, B = pc(270 - a / 2), pc(270 + a / 2)
            C, D = pc(270 + a / 2 + x), pc(270 + a / 2 + x + b)
            gr = janela('V\u00e9rtice no interior',
                        [('s', segs(A, C) + segs(B, D), 5),
                         ('t', rot([(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D')]),
                          0)], [A, B, C, D],
                        'arco AB = ' + nv(a) + '; arco CD = ' + nv(b))
        else:
            N.need(a > b, 'O 1.\u00ba arco (o mais afastado do v\u00e9rtice) tem de ser'
                   ' o maior')
            r = (a - b) / 2
            o += ['= \u00e2ngulo = (a - b) / 2 (semidiferen\u00e7a dos arcos)',
                  '> (' + nv(a) + ' - ' + nv(b) + ') / 2 ' + gt(r),
                  'a: arco mais afastado do v\u00e9rtice; b: o mais pr\u00f3ximo.',
                  'Vale para duas secantes, secante e tangente ou duas '
                  'tangentes.']
            if a + b < 359.9 and r >= 8:
                A, B = pc(90 + b / 2), pc(90 - b / 2)
                D, C = pc(270 - a / 2), pc(270 + a / 2)
                P = corte(A, D, B, C)
                if P and abs(P[0] - 10) < 13 and abs(P[1] - 10) < 13:
                    gr = janela('V\u00e9rtice no exterior',
                                [('s', segs(P, D) + segs(P, C), 5),
                                 ('t', rot([(P, 'P'), (A, 'A'), (B, 'B'),
                                            (C, 'C'), (D, 'D')]), 0)],
                                [A, B, C, D, P], 'arco DC = ' + nv(a) +
                                '; arco AB = ' + nv(b))
    elif k == 4:
        N.need(b is not None, 'Escreve dois \u00e2ngulos consecutivos')
        b = b[0]
        N.need(0 < a < 180 and 0 < b < 180, 'Os \u00e2ngulos de um quadril\u00e1tero '
               'inscrito est\u00e3o entre 0\u00b0 e 180\u00b0')
        r = 180 - a
        o += ['Num quadril\u00e1tero inscrito, os \u00e2ngulos opostos s\u00e3o '
              'suplementares.', '> Oposto a ' + nv(a) + ': 180\u00b0 - ' + nv(a) +
              ' ' + gt(r), '> Oposto a ' + nv(b) + ': 180\u00b0 - ' + nv(b) + ' ' +
              gt(180 - b), 'Soma dos quatro: 360\u00b0 \u2713']
    elif k == 5:
        N.need(abs(a - round(a)) < 1e-9 and 3 <= a <= 1000, 'n tem de ser um '
               'inteiro maior ou igual a 3')
        n = int(round(a))
        r = 360 / n
        o += ['= \u00e2ngulo ao centro = 360\u00b0 : n', '> 360\u00b0 : ' + str(n) + ' ' +
              gt(r), 'Arco correspondente a cada lado ' + gt(r),
              '\u00c2ngulo interno = \u00e2ngulo inscrito que abrange n - 2 arcos: (n - '
              '2) ' + N.X + ' 180\u00b0 : n ' + gt((n - 2) * 180 / n),
              '\u00c2ngulo inscrito que abrange um lado ' + gt(r / 2)]
        if n <= 24:
            q = [pc(90 + r * i) for i in range(n + 1)]
            gr = janela('Pol\u00edgono regular inscrito',
                        [('s', segs(*q), 5), ('s', segs(q[0], O, q[1]), 2)],
                        q, 'azul: \u00e2ngulo ao centro ' + nv(r))
    else:
        N.need(b is not None, 'Escreve o raio r e a amplitude \u03b1')
        b = b[0]
        N.pos(a, 'O raio')
        N.need(0 < b <= 360, 'A amplitude tem de estar entre 0\u00b0 e 360\u00b0')
        r = b / 360 * 2 * math.pi * a
        o += ['= comprimento do arco: l = \u03b1/360 ' + N.X + ' 2\u03c0r',
              '> l = ' + N.fmt(b) + '/360 ' + N.X + ' 2\u03c0 ' + N.X + ' ' +
              N.fmt(a) + ' ' + N.rhs(r, 2),
              '= \u00e1rea do setor: A = \u03b1/360 ' + N.X + ' \u03c0r\u00b2',
              '> A = ' + N.fmt(b) + '/360 ' + N.X + ' \u03c0 ' + N.X + ' ' +
              N.fmt(a) + '\u00b2 ' + N.rhs(b / 360 * math.pi * a * a, 2)]
        q = [pc(270 - b / 2 + b * i / 24) for i in range(25)]
        gr = janela('Arco e setor', [('s', segs(*q), 5),
                                     ('s', segs(q[0], O, q[24]), 2)], q,
                    'vermelho: arco de ' + nv(b))
    st = '\u00c2ngulo ao centro = arco; \u00e2ngulo inscrito = metade do arco.\n' \
        'V\u00e9rtice interior: semissoma dos arcos; exterior: semidiferen\u00e7a.\n' \
        'Quadril\u00e1tero inscrito: \u00e2ngulos opostos suplementares.'
    return ('\n'.join(o), st, r, '', gr) if gr else ('\n'.join(o), st, r, '')


def corte(A, D, B, C):
    # Intersecao das retas AD e BC (None se forem paralelas).
    d1 = (D[0] - A[0], D[1] - A[1])
    d2 = (C[0] - B[0], C[1] - B[1])
    den = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(den) < 1e-12:
        return None
    t = ((B[0] - A[0]) * d2[1] - (B[1] - A[1]) * d2[0]) / den
    return (A[0] + t * d1[0], A[1] + t * d1[1])
