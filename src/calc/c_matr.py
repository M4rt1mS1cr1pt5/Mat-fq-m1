# c_matr.py - M1TR4M: calculadoras de trigonometria: triangulo retangulo
# (revisao do 9.o ano), graus, radianos e valores exatos, e resolucao de
# triangulos quaisquer pelas leis dos senos e dos cossenos (extensao).
#@ c_matr.tri|Tri\u00e2ngulo ret\u00e2ngulo: seno, cosseno e tangente|trigonometria seno cosseno tangente cateto oposto adjacente hipotenusa \u00e2ngulo agudo resolver tri\u00e2ngulo ret\u00e2ngulo eleva\u00e7\u00e3o|M|m9
#@ c_matr.rad|Graus, radianos e valores exatos|graus radianos convers\u00e3o pi valores exatos \u00e2ngulos not\u00e1veis 30 45 60 seno cosseno tangente|M|m9
#@ c_matr.res|Resolver tri\u00e2ngulos: leis dos senos e dos cossenos|lei dos senos lei dos cossenos tri\u00e2ngulo qualquer resolver \u00e1rea caso amb\u00edguo|M|m9
# Casos-limite: dados a mais ou a menos, angulo fora de ]0, 90[, cateto
# maior do que a hipotenusa, lados que nao formam triangulo, angulos que
# somam 180 ou mais, caso ambiguo (lado, lado, angulo) com 0, 1 ou 2
# triangulos.

import math
import m1_nucleo as N

X = N.X
MS = '\u00b7'
G = math.pi / 180
NOT = {0: ('0', '1', '0'), 30: ('1/2', '\u221a3/2', '\u221a3/3'),
       45: ('\u221a2/2', '\u221a2/2', '1'), 60: ('\u221a3/2', '1/2', '\u221a3'),
       90: ('1', '0', None)}


def ex(v):
    s, ok = N.fmt2(v, 0, -1)
    if ok:
        return s
    e = N.exact(v)
    return e if e is not None else s


def gr(v):
    # Angulo em graus: 1 casa decimal (ou exato).
    s, ok = N.fmt2(v, 0, 1)
    return ('= ' if ok else N.AP + ' ') + s + '\u00b0'


def janela(ps):
    xs = [p[0] for p in ps]
    ys = [p[1] for p in ps]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w = max(x1 - x0, 2.1 * (y1 - y0)) * 1.3 or 1.0
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return cx - w / 2, cx + w / 2, cy - w / 4.2, cy + w / 4.2


def desenho(t, A, B, C, nomes, leg):
    x0, x1, y0, y1 = janela([A, B, C])
    sg = [(A[0], A[1], B[0], B[1]), (B[0], B[1], C[0], C[1]),
          (C[0], C[1], A[0], A[1])]
    return (t, [('s', sg, 4), ('t', [(A[0], A[1], nomes[0]),
                                     (B[0], B[1], nomes[1]),
                                     (C[0], C[1], nomes[2])], 0)],
            x0, x1, y0, y1, leg)

# ------------------------------------------------------------ retangulo


def tri():
    return ('Tri\u00e2ngulo ret\u00e2ngulo',
            [N.fld('Cateto oposto a \u03b1 (a)', '', '3', 'o'),
             N.fld('Cateto adjacente a \u03b1 (b)', '', '4', 'o'),
             N.fld('Hipotenusa (c)', '', '', 'o'),
             N.fld('\u00c2ngulo \u03b1 (graus)', '', '', 'o')], _tri)


def _tri(v):
    a, b, c, al = [None if x is None else x[0] for x in v]
    N.need(len([x for x in v if x is not None]) == 2, 'Preenche exatamente '
           'dois dados (pelo menos um lado)')
    for x, nm in ((a, 'O cateto a'), (b, 'O cateto b'), (c, 'A hipotenusa')):
        if x is not None:
            N.pos(x, nm)
    o = []
    if al is not None:
        N.need(0 < al < 90, 'O \u00e2ngulo agudo tem de estar entre 0\u00b0 e 90\u00b0')
        r = al * G
        if a is not None:
            b, c = a / math.tan(r), a / math.sin(r)
            o += ['= tg \u03b1 = a / b, logo b = a / tg \u03b1',
                  '= sen \u03b1 = a / c, logo c = a / sen \u03b1']
        elif b is not None:
            a, c = b * math.tan(r), b / math.cos(r)
            o += ['= tg \u03b1 = a / b, logo a = b ' + X + ' tg \u03b1',
                  '= cos \u03b1 = b / c, logo c = b / cos \u03b1']
        else:
            a, b = c * math.sin(r), c * math.cos(r)
            o += ['= a = c ' + X + ' sen \u03b1', '= b = c ' + X + ' cos \u03b1']
    else:
        if c is None:
            c = math.sqrt(a * a + b * b)
            o.append('= c\u00b2 = a\u00b2 + b\u00b2 (Pit\u00e1goras)')
            al = math.atan(a / b) / G
            o.append('= tg \u03b1 = a / b = ' + ex(a / b))
        elif a is not None:
            N.need(c > a, 'A hipotenusa tem de ser maior do que os catetos')
            b = math.sqrt(c * c - a * a)
            al = math.asin(a / c) / G
            o += ['= b\u00b2 = c\u00b2 - a\u00b2', '= sen \u03b1 = a / c = ' + ex(a / c)]
        else:
            N.need(c > b, 'A hipotenusa tem de ser maior do que os catetos')
            a = math.sqrt(c * c - b * b)
            al = math.acos(b / c) / G
            o += ['= a\u00b2 = c\u00b2 - b\u00b2', '= cos \u03b1 = b / c = ' + ex(b / c)]
    o += ['> a ' + N.rhs(a) + ' ' + MS + ' b ' + N.rhs(b) + ' ' + MS +
          ' c ' + N.rhs(c),
          '> \u03b1 ' + gr(al) + ' e \u03b2 = 90\u00b0 - \u03b1 ' + gr(90 - al),
          'sen \u03b1 = a / c ' + N.rhs(a / c) + '; cos \u03b1 = b / c ' +
          N.rhs(b / c) + '; tg \u03b1 = a / b ' + N.rhs(a / b),
          '\u00c1rea = a b / 2 ' + N.rhs(a * b / 2) + '; per\u00edmetro ' +
          N.rhs(a + b + c)]
    g = desenho('Tri\u00e2ngulo ret\u00e2ngulo', (0, 0), (b, 0), (b, a),
                ('\u03b1', '90\u00b0', '\u03b2'), 'a: vertical; b: horizontal; '
                'c: hipotenusa')
    st = 'SOH-CAH-TOA: sen = oposto / hipotenusa; cos = adjacente / ' \
        'hipotenusa; tg = oposto / adjacente.\n\u03b1 + \u03b2 = 90\u00b0 e ' \
        'a\u00b2 + b\u00b2 = c\u00b2.\nNa calculadora, o \u00e2ngulo a partir de uma ' \
        'raz\u00e3o: sen\u207b\u00b9, cos\u207b\u00b9 ou tg\u207b\u00b9 (em graus).'
    return ('\n'.join(o), st, al, '\u00b0', g)


# ------------------------------------------------------------ radianos


def rad():
    return ('Graus, radianos e valores exatos',
            [N.fld('\u00c2ngulo', '', '60', 'n'),
             N.fld('Unidade', '', '', 'c', ['graus', 'radianos (extens\u00e3o)'])],
            _rad)


def _rad(v):
    x, u = v[0][0], v[1]
    if u == 0:
        d = x
        r = x * G
        o = ['= rad = graus ' + X + ' \u03c0 / 180',
             '> ' + N.fmt(d) + '\u00b0 = ' + pi_txt(d) + ' rad ' + N.AP + ' ' +
             N.fmt(r, 0, 4) + ' rad']
    else:
        r = x
        d = x / G
        o = ['= graus = rad ' + X + ' 180 / \u03c0',
             '> ' + N.fmt(r) + ' rad ' + gr(d)]
    k = round(d)
    if abs(d - k) < 1e-9 and k in NOT:
        s, c, t = NOT[k]
        o.append('Valores exatos: sen = ' + s + ', cos = ' + c + ', tg = ' +
                 (t if t else 'n\u00e3o existe'))
    o.append('sen ' + N.rhs(math.sin(r)) + '; cos ' + N.rhs(math.cos(r)) +
             ('; tg ' + N.rhs(math.tan(r)) if abs(math.cos(r)) > 1e-12 else
              '; tg n\u00e3o existe'))
    if not 0 <= d <= 90:
        o.append('(\u00c2ngulos fora de 0\u00b0 a 90\u00b0: trigonometria do 11.\u00ba '
                 'ano.)')
    st = '180\u00b0 = \u03c0 rad (os radianos s\u00e3o do 11.\u00ba ano: extens\u00e3o).\n' \
        'Valores exatos: sen 30\u00b0 = cos 60\u00b0 = 1/2; sen 45\u00b0 = cos 45\u00b0 = ' \
        '\u221a2/2; sen 60\u00b0 = cos 30\u00b0 = \u221a3/2.\nsen\u00b2 \u03b1 + cos\u00b2 ' \
        '\u03b1 = 1 e tg \u03b1 = sen \u03b1 / cos \u03b1.'
    return ('\n'.join(o), st, r if u == 0 else d, 'rad' if u == 0 else '\u00b0')


def pi_txt(d):
    # d graus em fracao de pi: 60 -> pi/3, 135 -> 3pi/4; senao decimal.
    for q in range(1, 181):
        p = d * q / 180
        if abs(p - round(p)) < 1e-9:
            p = int(round(p))
            if p == 0:
                return '0'
            s = ('' if abs(p) == 1 else str(abs(p))) + '\u03c0'
            return ('-' if p < 0 else '') + s + ('' if q == 1 else '/' + str(q))
    return N.fmt(d / 180, 0, 4) + '\u03c0'

# ------------------------------------------------------------ qualquer


def res():
    return ('Resolver tri\u00e2ngulos (extens\u00e3o)',
            [N.fld('Lado a', '', '7', 'o'),
             N.fld('Lado b', '', '5', 'o'),
             N.fld('Lado c', '', '', 'o'),
             N.fld('\u00c2ngulo A, oposto a a (graus)', '', '', 'o'),
             N.fld('\u00c2ngulo B, oposto a b (graus)', '', '', 'o'),
             N.fld('\u00c2ngulo C, oposto a c (graus)', '', '60', 'o')], _res)


def lc(b, c, A):
    # Lei dos cossenos: lado oposto ao angulo A.
    return math.sqrt(max(0.0, b * b + c * c - 2 * b * c * math.cos(A * G)))


def ang(a, b, c):
    # Angulo oposto a a, pela lei dos cossenos.
    return math.acos(max(-1.0, min(1.0, (b * b + c * c - a * a) / (2 * b * c)))) / G


def _res(v):
    L = [None if x is None else x[0] for x in v[:3]]
    A = [None if x is None else x[0] for x in v[3:]]
    nl = len([x for x in L if x is not None])
    na = len([x for x in A if x is not None])
    N.need(nl + na == 3, 'Preenche exatamente 3 dados')
    N.need(nl >= 1, 'Escreve pelo menos um lado')
    for x in L:
        if x is not None:
            N.pos(x, 'Cada lado')
    for x in A:
        if x is not None:
            N.need(0 < x < 180, 'Cada \u00e2ngulo tem de estar entre 0\u00b0 e 180\u00b0')
    N.need(sum([x for x in A if x is not None]) < 180, 'Os \u00e2ngulos somam '
           '180\u00b0 ou mais')
    nm = 'abc'
    o = []
    sols = []
    if nl == 3:
        a, b, c = L
        s = sorted(L)
        N.need(s[2] < s[0] + s[1], 'Estes lados n\u00e3o formam um tri\u00e2ngulo '
               '(o maior tem de ser menor do que a soma dos outros)')
        o.append('Lei dos cossenos: cos A = (b\u00b2 + c\u00b2 - a\u00b2) / (2bc)')
        sols.append((L, [ang(a, b, c), ang(b, c, a), ang(c, a, b)]))
    elif nl == 2:
        i = [k for k in range(3) if L[k] is None][0]
        if A[i] is not None:
            j, k = [m for m in range(3) if m != i]
            x = lc(L[j], L[k], A[i])
            o.append('Lei dos cossenos: ' + nm[i] + '\u00b2 = ' + nm[j] + '\u00b2 + ' +
                     nm[k] + '\u00b2 - 2' + nm[j] + nm[k] + ' cos ' + nm[i].upper())
            Lx = list(L)
            Lx[i] = x
            sols.append((Lx, [ang(Lx[0], Lx[1], Lx[2]), ang(Lx[1], Lx[2], Lx[0]),
                              ang(Lx[2], Lx[0], Lx[1])]))
        else:
            # caso lado-lado-angulo (pode ser ambiguo)
            k = [m for m in range(3) if A[m] is not None][0]
            j = [m for m in range(3) if m != i and m != k][0]
            o.append('Lei dos senos: sen ' + nm[j].upper() + ' = ' + nm[j] +
                     ' sen ' + nm[k].upper() + ' / ' + nm[k])
            sj = L[j] * math.sin(A[k] * G) / L[k]
            if sj > 1 + 1e-12:
                N.need(False, 'N\u00e3o h\u00e1 tri\u00e2ngulo: sen ' + nm[j].upper() +
                       ' daria ' + N.fmt(sj, 0, 4) + ', maior do que 1')
            Aj = math.asin(min(1.0, sj)) / G
            for aj in ((Aj, 180 - Aj) if abs(Aj - 90) > 1e-9 else (Aj,)):
                if A[k] + aj < 180 - 1e-9:
                    An = [0.0, 0.0, 0.0]
                    An[k], An[j] = A[k], aj
                    An[i] = 180 - A[k] - aj
                    Lx = list(L)
                    Lx[i] = L[k] * math.sin(An[i] * G) / math.sin(A[k] * G)
                    sols.append((Lx, An))
            N.need(sols, 'N\u00e3o h\u00e1 tri\u00e2ngulo com estes dados')
            if len(sols) == 2:
                o.append('Caso amb\u00edguo: h\u00e1 dois tri\u00e2ngulos.')
    else:
        # um lado e dois angulos
        An = list(A)
        f = [m for m in range(3) if An[m] is None][0]
        An[f] = 180 - sum([x for x in A if x is not None])
        k = [m for m in range(3) if L[m] is not None][0]
        o.append('Soma dos \u00e2ngulos: ' + nm[f].upper() + ' = 180\u00b0 - ... ' +
                 gr(An[f]))
        o.append('Lei dos senos: a / sen A = b / sen B = c / sen C')
        r = L[k] / math.sin(An[k] * G)
        sols.append(([r * math.sin(x * G) for x in An], An))
    for q in range(len(sols)):
        Lx, An = sols[q]
        p = (str(q + 1) + '.\u00ba: ') if len(sols) > 1 else ''
        o.append('> ' + p + 'a ' + N.rhs(Lx[0]) + ', b ' + N.rhs(Lx[1]) + ', c ' +
                 N.rhs(Lx[2]))
        o.append('> ' + p + 'A ' + gr(An[0]) + ', B ' + gr(An[1]) + ', C ' +
                 gr(An[2]))
        o.append(' \u00e1rea = (1/2) a b sen C ' + N.rhs(0.5 * Lx[0] * Lx[1] *
                                                      math.sin(An[2] * G)))
    Lx, An = sols[0]
    Bp = (Lx[2], 0.0)
    Cp = (Lx[1] * math.cos(An[0] * G), Lx[1] * math.sin(An[0] * G))
    g = desenho('Tri\u00e2ngulo', (0.0, 0.0), Bp, Cp, ('A', 'B', 'C'),
                'lado a oposto a A, b a B, c a C' + (' (1.\u00ba tri\u00e2ngulo)'
                                                     if len(sols) > 1 else ''))
    st = 'Lei dos senos: a / sen A = b / sen B = c / sen C.\nLei dos cossenos: ' \
        'a\u00b2 = b\u00b2 + c\u00b2 - 2bc cos A.\nA + B + C = 180\u00b0. ' \
        '(Extens\u00e3o: 11.\u00ba ano.)'
    return ('\n'.join(o), st, None, '', g)
