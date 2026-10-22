# c_matg.py - M1TR4M: calculadoras de geometria analitica: distancia e
# ponto medio (plano e espaco), equacao reduzida da reta e paralela,
# mediatriz e plano mediador, circunferencia e superficie esferica,
# condicoes no plano com conjuncao e disjuncao (com desenho).
#@ c_matg.dist|Dist\u00e2ncia e ponto m\u00e9dio|dist\u00e2ncia entre dois pontos ponto m\u00e9dio plano espa\u00e7o coordenadas|M|m7
#@ c_matg.reta|Equa\u00e7\u00e3o reduzida da reta|equa\u00e7\u00e3o reduzida da reta declive ordenada na origem reta vertical horizontal paralela|M|m7
#@ c_matg.medz|Mediatriz e plano mediador|mediatriz plano mediador equidistante equa\u00e7\u00e3o|M|m7
#@ c_matg.circ|Circunfer\u00eancia e superf\u00edcie esf\u00e9rica|circunfer\u00eancia c\u00edrculo superf\u00edcie esf\u00e9rica esfera centro raio equa\u00e7\u00e3o reduzida di\u00e2metro|M|m7
#@ c_matg.cond|Condi\u00e7\u00f5es no plano (regi\u00e3o)|condi\u00e7\u00e3o conjun\u00e7\u00e3o disjun\u00e7\u00e3o semiplano regi\u00e3o do plano desenhar ponto verifica|M|m7
# Casos-limite: numero de coordenadas diferente nos dois pontos, pontos
# iguais (nao ha reta nem mediatriz), reta vertical, raio nulo ou
# negativo, condicao sem sinal de comparacao ou com expressao invalida.

import math
import m1_nucleo as N

X = N.X
SQ = '\u00b2'


def ex(v):
    s, ok = N.fmt2(v, 0, -1)
    if ok:
        return s
    e = N.exact(v)
    return e if e is not None else s


def sep(*ts):
    for t in ts:
        if ',' in t:
            return '; '
    return ', '


def ptx(p):
    ts = [ex(x) for x in p]
    return '(' + sep(*ts).join(ts) + ')'


def ponto(t, nm, dims=(2, 3)):
    N.need(t, 'Escreve as coordenadas de ' + nm + ', por exemplo 2 3')
    ps = N.lst(t)
    N.need(len(ps) in dims, nm + ': escreve ' + ' ou '.join(
        [str(d) for d in dims]) + ' coordenadas, separadas por espa\u00e7os')
    return [N.num(p)[0] for p in ps]


def termo(v, nm):
    # "(x - 2)\u00b2", "(y + 1)\u00b2" ou "x\u00b2".
    if v == 0:
        return nm + SQ
    return '(' + nm + (' - ' + ex(v) if v > 0 else ' + ' + ex(-v)) + ')' + SQ


def lin(m, b):
    if m == 0:
        return ex(b)
    c = ex(abs(m))
    if '/' in c:
        c = '(' + c + ')'
    s = ('' if m > 0 else '-') + ('' if abs(m) == 1 else c) + 'x'
    if b > 0:
        s += ' + ' + ex(b)
    elif b < 0:
        s += ' - ' + ex(-b)
    return s


def janela(ps, extra=1.0):
    xs = [p[0] for p in ps]
    ys = [p[1] for p in ps]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w = max(x1 - x0, 2.1 * (y1 - y0), 2.0) * 1.3 + extra
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return cx - w / 2, cx + w / 2, cy - w / 4.2, cy + w / 4.2

# ------------------------------------------------------------ distancia


def dist():
    return ('Dist\u00e2ncia e ponto m\u00e9dio',
            [N.fld('Ponto A (x y ou x y z)', '', '1 2', 't'),
             N.fld('Ponto B (x y ou x y z)', '', '4 6', 't')], _dist)


def _dist(v):
    A = ponto(v[0], 'A')
    B = ponto(v[1], 'B')
    N.need(len(A) == len(B), 'A e B t\u00eam de ter o mesmo n\u00famero de '
           'coordenadas')
    ds = [(B[i] - A[i]) ** 2 for i in range(len(A))]
    d = math.sqrt(sum(ds))
    M = [(A[i] + B[i]) / 2 for i in range(len(A))]
    nm = ('x', 'y', 'z')
    o = ['= AB = \u221a(' + ' + '.join(['(' + nm[i] + 'B - ' + nm[i] + 'A)' + SQ
                                      for i in range(len(A))]) + ')',
         'AB = \u221a(' + ' + '.join([ex(x) for x in ds]) + ')',
         '> AB ' + N.rhs(d),
         '= M = m\u00e9dia das coordenadas de A e de B',
         '> M = ' + ptx(M)]
    st = 'No espa\u00e7o junta-se a coordenada z da mesma forma.\nO ponto ' \
        'm\u00e9dio de [AB] est\u00e1 \u00e0 mesma dist\u00e2ncia de A e de B.'
    if len(A) == 2:
        g = ('[AB] e ponto m\u00e9dio', [('s', [(A[0], A[1], B[0], B[1])], 0),
                                     ('p', [M], 5),
                                     ('t', [(A[0], A[1], 'A'), (B[0], B[1], 'B'),
                                            (M[0], M[1], 'M')], 2)]) + \
            janela([A, B]) + ('AB ' + N.rhs(d),)
        return ('\n'.join(o), st, d, '', g)
    return ('\n'.join(o), st, d, '')

# ------------------------------------------------------------ reta


def reta():
    return ('Equa\u00e7\u00e3o reduzida da reta',
            [N.fld('Ponto A (x y)', '', '1 3', 't'),
             N.fld('Ponto B (x y), ou deixa vazio', '', '3 7', 't'),
             N.fld('Declive m (se n\u00e3o deres B)', '', '', 'o'),
             N.fld('Ponto P para a paralela (opcional)', '', '', 't')], _reta)


def _reta(v):
    A = ponto(v[0], 'A', (2,))
    B = ponto(v[1], 'B', (2,)) if v[1] else None
    m = v[2]
    P = ponto(v[3], 'P', (2,)) if v[3] else None
    N.need((B is None) != (m is None), 'D\u00e1 o ponto B ou o declive m '
           '(s\u00f3 um dos dois)')
    o = []
    items = []
    if B is not None:
        N.need(A != B, 'A e B s\u00e3o o mesmo ponto: h\u00e1 infinitas retas')
        if A[0] == B[0]:
            o += ['A e B t\u00eam a mesma abcissa: reta vertical.',
                  '> x = ' + ex(A[0]), 'O declive n\u00e3o est\u00e1 definido.']
            if P:
                o.append('Paralela por P: x = ' + ex(P[0]))
            items.append(('s', [(A[0], -1e6, A[0], 1e6)], 4))
            ps = [A, B] + ([P] if P else [])
            g = ('Reta vertical', items + [('p', ps, 5)]) + janela(ps) + \
                ('x = ' + ex(A[0]),)
            return ('\n'.join(o), '', None, '', g)
        m = (B[1] - A[1]) / (B[0] - A[0])
        o += ['= m = (yB - yA) / (xB - xA)', 'm ' + N.rhs(m)]
    else:
        m = m[0]
    b = A[1] - m * A[0]
    o += ['b = yA - m xA ' + N.rhs(b), '> y = ' + lin(m, b)]
    if m == 0:
        o.append('Reta horizontal (declive 0).')
    else:
        o.append('Corta Ox em ' + ptx([-b / m, 0]) + ' e Oy em ' +
                 ptx([0, b]) + '.')
    items.append(('f', lambda x: m * x + b, 4))
    ps = [A] + ([B] if B else [])
    if P:
        b2 = P[1] - m * P[0]
        o.append('> Paralela por P: y = ' + lin(m, b2) + ' (mesmo declive)')
        items.append(('f', lambda x: m * x + b2, 6))
        ps.append(P)
    st = 'Equa\u00e7\u00e3o reduzida: y = mx + b. Retas paralelas t\u00eam o mesmo ' \
        'declive.\nVerticais: x = a (sem declive); horizontais: y = b.'
    g = ('y = ' + lin(m, b), items + [('p', ps, 5)]) + janela(ps) + \
        ('azul: reta' + (' \u00b7 verde: paralela' if P else ''),)
    return ('\n'.join(o), st, m, '', g)

# ------------------------------------------------------------ mediatriz


def medz():
    return ('Mediatriz e plano mediador',
            [N.fld('Ponto A (x y ou x y z)', '', '1 1', 't'),
             N.fld('Ponto B (x y ou x y z)', '', '5 3', 't')], _medz)


def inteiros(cs):
    # Divide coeficientes inteiros pelo maior divisor comum.
    if all([c == int(c) for c in cs]):
        g = 0
        for c in cs:
            a, b = abs(int(c)), g
            while b:
                a, b = b, a % b
            g = a
        if g > 1:
            return [c / g for c in cs]
    return cs


def _medz(v):
    A = ponto(v[0], 'A')
    B = ponto(v[1], 'B')
    N.need(len(A) == len(B), 'A e B t\u00eam de ter o mesmo n\u00famero de '
           'coordenadas')
    N.need(A != B, 'A e B s\u00e3o o mesmo ponto: n\u00e3o h\u00e1 mediatriz')
    n = len(A)
    nm = ('x', 'y', 'z')
    M = [(A[i] + B[i]) / 2 for i in range(n)]
    o = ['= PA = PB, com P(' + ', '.join(nm[:n]) + '):',
         ' + '.join([termo(A[i], nm[i]) for i in range(n)]) + ' =',
         ' + '.join([termo(B[i], nm[i]) for i in range(n)])]
    cs = [2 * (B[i] - A[i]) for i in range(n)]
    d = sum([B[i] ** 2 - A[i] ** 2 for i in range(n)])
    cs = inteiros(cs + [d])
    d = cs[-1]
    cs = cs[:-1]
    eq = ''
    for i in range(n):
        c = cs[i]
        if c == 0:
            continue
        s = ('' if abs(c) == 1 else ex(abs(c))) + nm[i]
        eq += (' - ' if c < 0 else (' + ' if eq else '')) + s if eq else \
            ('-' if c < 0 else '') + s
    o.append('Simplificando: ' + eq + ' = ' + ex(d))
    if n == 3:
        o += ['> Plano mediador: ' + eq + ' = ' + ex(d),
              'Passa no ponto m\u00e9dio M = ' + ptx(M) + '.']
        return ('\n'.join(o), '', None, '')
    if cs[1] != 0:
        mm = -cs[0] / cs[1]
        bb = d / cs[1]
        o.append('> Mediatriz: y = ' + lin(mm, bb))
        it = ('f', lambda x: mm * x + bb, 4)
    else:
        o.append('> Mediatriz: x = ' + ex(d / cs[0]) + ' (reta vertical)')
        it = ('s', [(d / cs[0], -1e6, d / cs[0], 1e6)], 4)
    o.append('Passa no ponto m\u00e9dio M = ' + ptx(M) + ' e \u00e9 '
             'perpendicular a [AB].')
    g = ('Mediatriz de [AB]', [('s', [(A[0], A[1], B[0], B[1])], 0), it,
                               ('p', [M], 5),
                               ('t', [(A[0], A[1], 'A'), (B[0], B[1], 'B')],
                                2)]) + janela([A, B]) + ('azul: mediatriz',)
    st = 'Mediatriz: pontos P com PA = PB. Igualam-se os quadrados das ' \
        'dist\u00e2ncias e os termos x\u00b2 e y\u00b2 cortam-se.'
    return ('\n'.join(o), st, None, '', g)

# ------------------------------------------------------------ circunferencia


def circ():
    return ('Circunfer\u00eancia e superf\u00edcie esf\u00e9rica',
            [N.fld('Dados', '', '', 'c', ['centro e raio', 'centro e um ponto',
                                         'extremos de um di\u00e2metro']),
             N.fld('Centro C (ou extremo A)', '', '1 -2', 't'),
             N.fld('Raio r (s\u00f3 com centro e raio)', '', '3', 'o'),
             N.fld('Ponto (ou extremo B)', '', '', 't'),
             N.fld('Ponto a testar (opcional)', '', '', 't')], _circ)


def _circ(v):
    k, tc, r, tp, tt = v
    C = ponto(tc, 'C')
    n = len(C)
    if k == 0:
        N.need(r is not None and not tp, 'Com centro e raio, deixa o ponto '
               'vazio')
        N.pos(r[0], 'O raio')
        r2 = r[0] ** 2
    else:
        N.need(r is None, 'Deixa o raio vazio: \u00e9 calculado')
        Pp = ponto(tp, 'o ponto')
        N.need(len(Pp) == n, 'Os pontos t\u00eam de ter o mesmo n\u00famero de '
               'coordenadas')
        N.need(Pp != C, 'Os dois pontos s\u00e3o iguais')
        r2 = sum([(Pp[i] - C[i]) ** 2 for i in range(n)])
        if k == 2:
            C = [(C[i] + Pp[i]) / 2 for i in range(n)]
            r2 = r2 / 4
    rr = math.sqrt(r2)
    nm = ('x', 'y', 'z')
    lhs = ' + '.join([termo(C[i], nm[i]) for i in range(n)])
    # (nome, nome com maiuscula) da linha e da regiao
    fig = (('circunfer\u00eancia', 'Circunfer\u00eancia'),
           ('c\u00edrculo', 'C\u00edrculo')) if n == 2 else (
        ('superf\u00edcie esf\u00e9rica', 'Superf\u00edcie esf\u00e9rica'),
        ('esfera', 'Esfera'))
    o = ['Centro ' + ptx(C) + '; raio r ' + N.rhs(rr),
         '> ' + fig[0][1] + ': ' + lhs + ' = ' + ex(r2),
         fig[1][1] + ': ' + lhs + ' \u2264 ' + ex(r2)]
    if n == 3:
        ts = [('x', 'y', 'z')[i] for i in range(3) if abs(abs(C[i]) - rr) <
              1e-12]
        if ts:
            o.append('Tangente ao(s) plano(s) ' + ', '.join(
                [{'x': 'yOz', 'y': 'xOz', 'z': 'xOy'}[t] for t in ts]) +
                ' (r = |coordenada do centro|).')
    if tt:
        T = ponto(tt, 'o ponto a testar')
        N.need(len(T) == n, 'O ponto a testar tem de ter ' + str(n) +
               ' coordenadas')
        dt = sum([(T[i] - C[i]) ** 2 for i in range(n)])
        e = 1e-12 * max(1.0, r2)
        o.append('Ponto ' + ptx(T) + ': ' + (
            'sobre a ' + fig[0][0] if abs(dt - r2) < e else (
                'dentro (pertence ' + ('ao ' if n == 2 else '\u00e0 ') +
                fig[1][0] + ')' if dt < r2 else 'fora')) +
            ' (dist\u00e2ncia\u00b2 = ' + ex(dt) + ')')
    st = '(x - a)\u00b2 + (y - b)\u00b2 = r\u00b2: pontos \u00e0 dist\u00e2ncia r do ' \
        'centro (a, b).\nCom \u2264 obt\u00e9m-se o c\u00edrculo (ou a esfera, no ' \
        'espa\u00e7o).'
    if n == 2:
        seg = []
        for i in range(48):
            a1 = 2 * math.pi * i / 48
            a2 = 2 * math.pi * (i + 1) / 48
            seg.append((C[0] + rr * math.cos(a1), C[1] + rr * math.sin(a1),
                        C[0] + rr * math.cos(a2), C[1] + rr * math.sin(a2)))
        g = ('Circunfer\u00eancia', [('s', seg, 4), ('p', [C], 5)]) + \
            janela([[C[0] - rr, C[1] - rr], [C[0] + rr, C[1] + rr]]) + \
            (lhs + ' = ' + ex(r2),)
        return ('\n'.join(o), st, rr, '', g)
    return ('\n'.join(o), st, rr, '')

# ------------------------------------------------------------ condicoes
OPS = ('\u2264', '\u2265', '<', '>', '=')


def atomo(s):
    # "expr op expr" -> (op, codigo esq, codigo dir, texto esq, texto dir)
    for op in OPS:
        k = s.find(op)
        if k > 0:
            a, b = s[:k].strip(), s[k + 1:].strip()
            N.need(a and b, 'Falta um membro em: ' + s)
            return op, N.comp(a, 2), N.comp(b, 2), a, b
    N.need(0, 'Falta um sinal (<, >, \u2264, \u2265 ou =) em: ' + s)


def compila(s):
    t = s.replace('<=', '\u2264').replace('>=', '\u2265')
    for a, b in ((' ou ', '\u2228'), (' or ', '\u2228'), (' e ', '\u2227'),
                 (' and ', '\u2227'), ('&', '\u2227')):
        t = t.replace(a, b)
    return [[atomo(x.strip()) for x in d.split('\u2227')] for d in
            t.split('\u2228')]


def vale(at, x, y):
    op, a, b = at[0], N.ev(at[1], x, y), N.ev(at[2], x, y)
    if op == '<':
        return a < b
    if op == '>':
        return a > b
    if op == '\u2264':
        return a <= b + 1e-12
    if op == '\u2265':
        return a >= b - 1e-12
    return abs(a - b) < 1e-9 * max(1.0, abs(a), abs(b))


def ok(cs, x, y):
    for d in cs:
        try:
            if all([vale(at, x, y) for at in d]):
                return True
        except Exception:
            pass
    return False


def cond():
    return ('Condi\u00e7\u00f5es no plano',
            [N.fld('Condi\u00e7\u00e3o (\u2227 ou "e"; \u2228 ou "ou")', '',
                   'y >= x - 1 e x <= 2', 't'),
             N.fld('Ponto a testar (x y), opcional', '', '', 't')], _cond)


def _cond(v):
    s, tp = v
    N.need(s, 'Escreve a condi\u00e7\u00e3o, por exemplo y >= 2x - 1 e x < 3')
    cs = compila(s)
    o = ['Condi\u00e7\u00e3o: ' + ' \u2228 '.join(
        ['(' + ' \u2227 '.join([a[3] + ' ' + a[0] + ' ' + a[4] for a in d]) +
         ')' if len(d) > 1 and len(cs) > 1 else
         ' \u2227 '.join([a[3] + ' ' + a[0] + ' ' + a[4] for a in d])
         for d in cs])]
    r = None
    if tp:
        P = ponto(tp, 'o ponto', (2,))
        for d in cs:
            for a in d:
                try:
                    la, lb = N.ev(a[1], P[0], P[1]), N.ev(a[2], P[0], P[1])
                    o.append(a[3] + ' ' + a[0] + ' ' + a[4] + ': ' + ex(la) +
                             ' ' + a[0] + ' ' + ex(lb) + (
                                 ' \u2713' if vale(a, P[0], P[1]) else ' \u2717'))
                except Exception:
                    o.append(a[3] + ' ' + a[0] + ' ' + a[4] + ': sem valor')
        r = ok(cs, P[0], P[1])
        o.append('> ' + ptx(P) + (' verifica a condi\u00e7\u00e3o.' if r else
                                  ' n\u00e3o verifica a condi\u00e7\u00e3o.'))
    x0, x1, y0, y1 = -6.0, 6.0, -2.86, 2.86
    pts = []
    for i in range(49):
        for j in range(25):
            x = x0 + (x1 - x0) * i / 48
            y = y0 + (y1 - y0) * j / 24
            if ok(cs, x, y):
                pts.append((x, y))
    o.append('Regi\u00e3o: ' + ('pontos de ' + str(len(pts)) + ' de 1225 '
                               'da grelha' if pts else 'nenhum ponto da '
                               'grelha (pode ser uma linha)') +
             ' em [-6, 6] ' + X + ' [-2,86; 2,86].')
    its = [('p', pts, 8)]
    for d in cs:
        for a in d:
            if a[3].strip() in ('y', 'Y'):
                its.append(('f', lambda x, c=a[2]: N.ev(c, x, 0.0), 4))
            elif a[3].strip() in ('x', 'X'):
                try:
                    c = N.ev(a[2], 0.0, 0.0)
                    its.append(('s', [(c, -1e6, c, 1e6)], 4))
                except Exception:
                    pass
    if tp:
        its.append(('p', [P], 5))
    g = ('Regi\u00e3o do plano', its, x0, x1, y0, y1,
         'pontos claros: regi\u00e3o \u00b7 azul: fronteiras')
    st = '\u2227 (e): os pontos t\u00eam de verificar as duas condi\u00e7\u00f5es ' \
        '(interse\u00e7\u00e3o).\n\u2228 (ou): basta verificar uma (uni\u00e3o).\n' \
        'y > mx + b: semiplano acima da reta; y < mx + b: abaixo.'
    return ('\n'.join(o), st, r, '', g)
