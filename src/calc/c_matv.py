# c_matv.py - M1TR4M: calculadoras de vetores: operacoes (norma, soma,
# diferenca, produto por um numero, colinearidade, ponto + vetor),
# equacao vetorial da reta (ponto pertence?, declive) e baricentro com
# vetores. No plano e no espaco.
#@ c_matv.vet|Opera\u00e7\u00f5es com vetores|vetor norma soma diferen\u00e7a produto por um n\u00famero real colinearidade ponto mais vetor coordenadas ab = b - a produto escalar \u00e2ngulo|M|m8
#@ c_matv.retav|Equa\u00e7\u00e3o vetorial da reta|equa\u00e7\u00e3o vetorial da reta vetor diretor ponto pertence declive m = u2/u1 par\u00e2metro|M|m8
#@ c_matv.bar|Baricentro com vetores|baricentro vetores mediana g = a + 2/3 am ponto m\u00e9dio|M|m8
# Casos-limite: numeros de coordenadas diferentes, vetor diretor nulo,
# pontos iguais, vetor vertical (sem declive), dados a mais ou a menos.

import math
import m1_nucleo as N

X = N.X


def ex(v):
    s, ok = N.fmt2(v, 0, -1)
    if ok:
        return s
    e = N.exact(v)
    return e if e is not None else s


def tup(p):
    ts = [ex(x) for x in p]
    for t in ts:
        if ',' in t:
            return '(' + '; '.join(ts) + ')'
    return '(' + ', '.join(ts) + ')'


def par(x):
    # Numero entre parenteses quando e negativo: 2 u, (-3) u.
    s = ex(x)
    return '(' + s + ')' if x < 0 else s


def lin(m, b):
    # "m x + b" escrito como na escola: 2x - 1, -x + 3, (1/3)x, 5.
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


def coords(t, nm):
    ps = N.lst(t)
    N.need(len(ps) in (2, 3), nm + ': escreve 2 ou 3 coordenadas, separadas '
           'por espa\u00e7os')
    return [N.num(p)[0] for p in ps]


def mesma(a, b, nm):
    N.need(len(a) == len(b), nm + ' t\u00eam de ter o mesmo n\u00famero de '
           'coordenadas')


def norma(u):
    return math.sqrt(sum([x * x for x in u]))


def colin(u, v):
    # v = k u para algum k (devolve k, ou None se nao forem colineares).
    k = None
    for i in range(len(u)):
        if u[i] == 0:
            if v[i] != 0:
                return None
            continue
        r = v[i] / u[i]
        if k is None:
            k = r
        elif abs(r - k) > 1e-12 * max(1.0, abs(k)):
            return None
    return k

# ------------------------------------------------------------ operacoes


def vet():
    return ('Opera\u00e7\u00f5es com vetores',
            [N.fld('Vetor u (ou vazio para u = AB)', '', '3 -4', 't'),
             N.fld('Vetor v (opcional)', '', '', 't'),
             N.fld('N\u00famero real k (opcional)', '', '', 'o'),
             N.fld('Ponto A (opcional)', '', '', 't'),
             N.fld('Ponto B (com A e u vazio: u = AB)', '', '', 't')], _vet)


def _vet(v):
    tu, tv, k, ta, tb = v
    A = coords(ta, 'A') if ta else None
    o = []
    if tu:
        u = coords(tu, 'u')
        N.need(not tb, 'Com u escrito, deixa B vazio')
    else:
        N.need(A is not None and tb, 'Escreve u, ou os pontos A e B')
        B = coords(tb, 'B')
        mesma(A, B, 'A e B')
        u = [B[i] - A[i] for i in range(len(A))]
        o += ['= u = AB = B - A', '> u = ' + tup(u)]
        A = None
    n = norma(u)
    o.append('> \u2016u\u2016 = \u221a(' + ' + '.join([ex(x * x) for x in u]) +
             ') ' + N.rhs(n))
    if n == 0:
        o.append('u \u00e9 o vetor nulo (sem dire\u00e7\u00e3o nem sentido).')
    if tv:
        w = coords(tv, 'v')
        mesma(u, w, 'u e v')
        o += ['u + v = ' + tup([u[i] + w[i] for i in range(len(u))]),
              'u - v = ' + tup([u[i] - w[i] for i in range(len(u))]),
              '\u2016v\u2016 ' + N.rhs(norma(w))]
        c = colin(u, w) if n else None
        if c is not None:
            o.append('Colineares: v = ' + par(c) + ' u (' + (
                'mesmo sentido' if c > 0 else 'sentidos opostos') + ').')
        elif n:
            o.append('N\u00e3o s\u00e3o colineares (coordenadas n\u00e3o '
                     'proporcionais).')
        pe = sum([u[i] * w[i] for i in range(len(u))])
        o.append('Produto escalar (11.\u00ba ano): u \u00b7 v = ' + ex(pe))
        if n and norma(w):
            if c is None:
                cs = max(-1.0, min(1.0, pe / (n * norma(w))))
                g = math.acos(cs) * 180 / math.pi
            else:
                g = 0.0 if c > 0 else 180.0
            a, e = N.fmt2(g, 0, 1)
            o.append('\u00c2ngulo de u com v ' + ('= ' if e else N.AP + ' ') +
                     a + '\u00b0')
    if k is not None:
        k = k[0]
        o += [par(k) + ' u = ' + tup([k * x for x in u]),
              '\u2016' + par(k) + ' u\u2016 = |' + ex(k) + '| ' + X +
              ' \u2016u\u2016 ' + N.rhs(abs(k) * n)]
    if A is not None:
        mesma(A, u, 'A e u')
        o.append('A + u = ' + tup([A[i] + u[i] for i in range(len(u))]) +
                 ' (o ponto onde chega a seta de u aplicada em A)')
    st = 'As opera\u00e7\u00f5es fazem-se coordenada a coordenada.\n' \
        '\u2016u\u2016 = \u221a(u1\u00b2 + u2\u00b2 + u3\u00b2); \u2016k u\u2016 = |k| ' + X + \
        ' \u2016u\u2016.\nColineares: v = k u (coordenadas proporcionais).'
    return ('\n'.join(o), st, n, '')

# ------------------------------------------------------------ reta


def retav():
    return ('Equa\u00e7\u00e3o vetorial da reta',
            [N.fld('Ponto A da reta', '', '1 2', 't'),
             N.fld('Vetor diretor u (ou vazio)', '', '2 3', 't'),
             N.fld('Ponto B (com u vazio: u = AB)', '', '', 't'),
             N.fld('Ponto P a testar (opcional)', '', '', 't')], _retav)


def _retav(v):
    ta, tu, tb, tp = v
    A = coords(ta, 'A')
    if tu:
        N.need(not tb, 'Escreve o vetor diretor ou o ponto B, n\u00e3o os dois')
        u = coords(tu, 'u')
    else:
        N.need(tb, 'Escreve o vetor diretor u ou um segundo ponto B')
        B = coords(tb, 'B')
        mesma(A, B, 'A e B')
        u = [B[i] - A[i] for i in range(len(A))]
    mesma(A, u, 'A e u')
    N.need(norma(u) > 0, 'O vetor diretor n\u00e3o pode ser nulo')
    nm = ('x', 'y', 'z')[:len(A)]
    o = ['> (' + ', '.join(nm) + ') = ' + tup(A) + ' + k ' + tup(u) +
         ', k \u2208 \u211d']
    r = None
    if len(A) == 2:
        if u[0] == 0:
            o.append('Reta vertical: x = ' + ex(A[0]) + ' (sem declive).')
        else:
            m = u[1] / u[0]
            b = A[1] - m * A[0]
            o += ['Declive: m = u2 / u1 = ' + ex(u[1]) + ' / ' + par(u[0]) +
                  ' ' + N.rhs(m),
                  'Equa\u00e7\u00e3o reduzida: y = ' + lin(m, b)]
            r = m
    if tp:
        P = coords(tp, 'P')
        mesma(A, P, 'A e P')
        d = [P[i] - A[i] for i in range(len(A))]
        c = colin(u, d)
        if c is not None or norma(d) == 0:
            kk = 0.0 if norma(d) == 0 else c
            o.append('P = A + ' + par(kk) + ' u: P pertence \u00e0 reta (k = ' +
                     ex(kk) + ').')
        else:
            o.append('AP = ' + tup(d) + ' n\u00e3o \u00e9 colinear com u: P n\u00e3o '
                     'pertence \u00e0 reta.')
    st = 'Cada valor de k d\u00e1 um ponto da reta: k = 0 d\u00e1 A; k = 1 d\u00e1 ' \
        'A + u.\nNo plano, o declive \u00e9 m = u2 / u1 (se u1 \u2260 0).'
    return ('\n'.join(o), st, r, '')

# ------------------------------------------------------------ baricentro


def bar():
    return ('Baricentro com vetores',
            [N.fld('V\u00e9rtice A', '', '0 0', 't'),
             N.fld('V\u00e9rtice B', '', '6 0', 't'),
             N.fld('V\u00e9rtice C', '', '3 6', 't')], _bar)


def _bar(v):
    A = coords(v[0], 'A')
    B = coords(v[1], 'B')
    C = coords(v[2], 'C')
    mesma(A, B, 'A e B')
    mesma(A, C, 'A e C')
    n = len(A)
    M = [(B[i] + C[i]) / 2 for i in range(n)]
    am = [M[i] - A[i] for i in range(n)]
    G = [A[i] + 2 * am[i] / 3 for i in range(n)]
    ab = [B[i] - A[i] for i in range(n)]
    ac = [C[i] - A[i] for i in range(n)]
    N.need(colin(ab, ac) is None and norma(ab) > 0, 'Os tr\u00eas pontos est\u00e3o '
           'alinhados: n\u00e3o h\u00e1 tri\u00e2ngulo')
    o = ['M (ponto m\u00e9dio de [BC]) = ' + tup(M),
         'AM = M - A = ' + tup(am),
         '= G = A + 2/3 AM',
         '> G = ' + tup(G),
         'Confirma\u00e7\u00e3o: G = (A + B + C) / 3 = ' +
         tup([(A[i] + B[i] + C[i]) / 3 for i in range(n)])]
    st = 'O baricentro est\u00e1 a 2/3 da mediana a contar do v\u00e9rtice: ' \
        'G = A + 2/3 AM.\nEm coordenadas \u00e9 a m\u00e9dia dos tr\u00eas v\u00e9rtices.'
    return ('\n'.join(o), st, None, '')
