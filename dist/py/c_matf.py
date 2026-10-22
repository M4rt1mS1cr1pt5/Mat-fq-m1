# c_matf.py - M1TR4M: calculadoras de funcoes: funcao escrita pelo
# aluno (valores, tabela, zeros, sinal, extremos e grafico), funcao afim,
# funcoes definidas por ramos e funcao modulo a|x - h| + k.
#@ c_matf.fx|Fun\u00e7\u00e3o escrita por ti (tabela, zeros, gr\u00e1fico)|fun\u00e7\u00e3o express\u00e3o imagem tabela de valores zeros sinal extremos m\u00e1ximo m\u00ednimo monotonia gr\u00e1fico|M|m4
#@ c_matf.afim|Fun\u00e7\u00e3o afim|fun\u00e7\u00e3o afim declive ordenada na origem zero reta dois pontos sinal monotonia|M|m4
#@ c_matf.ramos|Fun\u00e7\u00e3o definida por ramos|fun\u00e7\u00e3o definida por ramos ramo fronteira continuidade salto zeros imagem|M|m6
#@ c_matf.mod|Fun\u00e7\u00e3o m\u00f3dulo a\u2223x - h\u2223 + k|fun\u00e7\u00e3o m\u00f3dulo valor absoluto v\u00e9rtice ramos equa\u00e7\u00e3o inequa\u00e7\u00e3o com m\u00f3dulo|M|m6
# Casos-limite: expressao invalida ou sem valores no intervalo,
# intervalo vazio, dois pontos com a mesma abcissa (reta vertical),
# dados insuficientes ou a mais na afim, a = 0 no modulo, ramo vazio.

import math
import m1_nucleo as N

X = N.X
INF = '+\u221e'
MINF = '-\u221e'
UN = ' \u222a '


def ex(v):
    # Decimal quando e exato e curto (0,5); senao a forma exata (1/3,
    # raiz de 2) quando existe; senao o decimal arredondado.
    s, ok = N.fmt2(v, 0, -1)
    if ok:
        return s
    e = N.exact(v)
    return e if e is not None else s


def lista(xs):
    # Valores separados por ", " (ou "; " se algum tiver virgula).
    ts = [ex(x) for x in xs]
    return sep(*ts).join(ts)


def sep(*ts):
    for t in ts:
        if ',' in t:
            return '; '
    return ', '


def pt(a, b):
    return '(' + a + sep(a, b) + b + ')'


def iv(a, b, ca=0, cb=0):
    # Intervalo com extremos a, b (None = infinito); ca, cb: fechado.
    sa = MINF if a is None else ex(a)
    sb = INF if b is None else ex(b)
    return ('[' if ca and a is not None else ']') + sa + sep(sa, sb) + sb + \
        (']' if cb and b is not None else '[')


def lin(m, b):
    # "m x + b" escrito como na escola: 2x - 1, -x + 3, x, 5.
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


def safe(f, x):
    try:
        y = f(x)
        if y != y or abs(y) > 1e300:
            return None
        return y
    except Exception:
        return None


def zeros(f, a, b, n=400):
    # Zeros de f em [a, b]: mudancas de sinal (bissecao) e pontos onde
    # |f| tem um minimo muito perto de 0 (zeros duplos).
    h = (b - a) / n
    xs = [a + i * h for i in range(n + 1)]
    ys = [safe(f, x) for x in xs]
    vs = [abs(y) for y in ys if y is not None]
    if not vs:
        return [], 0
    sc = max(vs) or 1.0
    zs = []
    for i in range(n + 1):
        y = ys[i]
        if y is None:
            continue
        if abs(y) <= 1e-12 * max(1.0, sc):
            zs.append(xs[i])
            continue
        if i < n and ys[i + 1] is not None and y * ys[i + 1] < 0:
            lo, hi = xs[i], xs[i + 1]
            for k in range(60):
                m = (lo + hi) / 2
                fm = safe(f, m)
                if fm is None:
                    break
                if (fm < 0) == (y < 0):
                    lo = m
                else:
                    hi = m
            zs.append((lo + hi) / 2)
        elif 0 < i < n and ys[i - 1] is not None and ys[i + 1] is not None \
                and abs(y) <= abs(ys[i - 1]) and abs(y) <= abs(ys[i + 1]) \
                and abs(y) < 1e-3 * sc:
            lo, hi = xs[i - 1], xs[i + 1]
            for k in range(80):
                m1 = lo + (hi - lo) / 3
                m2 = hi - (hi - lo) / 3
                if abs(safe(f, m1) or 0) < abs(safe(f, m2) or 0):
                    hi = m2
                else:
                    lo = m1
            xm = (lo + hi) / 2
            if abs(safe(f, xm) or 1) < 1e-9 * max(1.0, sc):
                zs.append(xm)
    out = []
    for z in sorted(zs):
        if not out or abs(z - out[-1]) > 1e-6 * (b - a):
            out.append(z)
    return [limpa(z) for z in out], len(vs) < n + 1


def limpa(z):
    # Arredonda para a forma exata quando ela e muito proxima.
    r = round(z * 1e6) / 1e6
    return r if abs(r - z) < 1e-9 else z


def extremos(f, a, b, n=400):
    h = (b - a) / n
    xs = [a + i * h for i in range(n + 1)]
    ys = [safe(f, x) for x in xs]
    out = []
    for i in range(1, n):
        y0, y1, y2 = ys[i - 1], ys[i], ys[i + 1]
        if y0 is None or y1 is None or y2 is None:
            continue
        mx = y1 > y0 and y1 >= y2
        mn = y1 < y0 and y1 <= y2
        if not (mx or mn):
            continue
        lo, hi = xs[i - 1], xs[i + 1]
        for k in range(60):
            m1 = lo + (hi - lo) / 3
            m2 = hi - (hi - lo) / 3
            f1, f2 = safe(f, m1), safe(f, m2)
            if f1 is None or f2 is None:
                break
            if (f1 > f2) == mx:
                hi = m2
            else:
                lo = m1
        xm = (lo + hi) / 2
        ym = safe(f, xm)
        xr = round(xm * 1e6) / 1e6
        yr = safe(f, xr)
        if yr is not None and ym is not None and abs(xr - xm) < 1e-6 and \
                (yr - ym) * (1 if mx else -1) >= -1e-12 * max(1.0, abs(ym)):
            xm, ym = xr, yr
        out.append((mx, xm, ym))
    return out


def janela(f, a, b):
    ys = [safe(f, a + (b - a) * i / 80) for i in range(81)]
    ys = sorted([y for y in ys if y is not None])
    N.need(ys, 'A fun\u00e7\u00e3o n\u00e3o tem valores neste intervalo')
    lo, hi = ys[len(ys) // 20], ys[len(ys) * 19 // 20]
    d = (hi - lo) * 0.15 or 1.0
    return min(lo, 0.0) - d, max(hi, 0.0) + d

# ------------------------------------------------------------ f(x)


def fx():
    return ('Fun\u00e7\u00e3o escrita por ti',
            [N.fld('f(x) =', '', 'x^2 - 4', 't'),
             N.fld('Intervalo: de', '', '-5'),
             N.fld('at\u00e9', '', '5'),
             N.fld('Calcular f em x = (opcional)', '', '', 'o')], _fx)


def _fx(v):
    s, a, b, x0 = v
    code = N.comp(s)
    a, b = a[0], b[0]
    N.need(b > a, 'O intervalo tem de ter a < b')

    def f(x):
        return N.ev(code, x)
    o = ['f(x) = ' + s]
    r = None
    if x0 is not None:
        y = safe(f, x0[0])
        N.need(y is not None, 'f n\u00e3o est\u00e1 definida em x = ' + ex(x0[0]))
        o.append('> f(' + ex(x0[0]) + ') ' + N.rhs(y))
        r = y
    o.append('Tabela:')
    for i in range(5):
        x = a + (b - a) * i / 4
        y = safe(f, x)
        o.append('x = ' + ex(x) + ': ' + ('sem valor' if y is None else
                                         'f(x) ' + N.rhs(y)))
    zs, falha = zeros(f, a, b)
    if falha:
        o.append('! f n\u00e3o est\u00e1 definida em parte do intervalo.')
    o.append('Zeros em ' + iv(a, b, 1, 1) + ': ' + (lista(zs) if zs else
                                                  'nenhum'))
    if not falha:
        cs = [a] + zs + [b]
        pos, neg = [], []
        for i in range(len(cs) - 1):
            if cs[i + 1] - cs[i] < 1e-12:
                continue
            y = safe(f, (cs[i] + cs[i + 1]) / 2)
            if y is None:
                continue
            (pos if y > 0 else neg).append(iv(cs[i], cs[i + 1]))
        o.append('f > 0 em ' + (UN.join(pos) if pos else '\u2205') +
                 '; f < 0 em ' + (UN.join(neg) if neg else '\u2205'))
    for mx, xm, ym in extremos(f, a, b):
        o.append(('M\u00e1ximo' if mx else 'M\u00ednimo') + ' relativo ' +
                 N.rhs(ym) + ' em x ' + N.rhs(xm))
    lo, hi = janela(f, a, b)
    g = ('f(x) = ' + s, [('f', f, 4)], a, b, lo, hi, 'f(x) = ' + s)
    st = 'Zeros e extremos procurados numericamente no intervalo ' \
        'escolhido (aproximados; a forma exata aparece quando \u00e9 ' \
        'reconhecida).\nMuda o intervalo para ver mais do gr\u00e1fico.'
    return ('\n'.join(o), st, r, '', g)

# ------------------------------------------------------------ afim


def afim():
    return ('Fun\u00e7\u00e3o afim',
            [N.fld('Declive m (opcional)', '', '', 'o'),
             N.fld('Ordenada na origem b (opcional)', '', '', 'o'),
             N.fld('Ponto A (x y), opcional', '', '1 3', 't'),
             N.fld('Ponto B (x y), opcional', '', '3 7', 't')], _afim)


def ponto(t, nm):
    ps = N.lst(t)
    N.need(len(ps) == 2, 'Escreve as duas coordenadas de ' + nm +
           ', por exemplo 2 3')
    return N.num(ps[0])[0], N.num(ps[1])[0]


def _afim(v):
    m, b, ta, tb = v
    A = ponto(ta, 'A') if ta else None
    B = ponto(tb, 'B') if tb else None
    o = []
    if A and B:
        N.need(m is None and b is None, 'Com dois pontos, deixa m e b '
               'vazios')
        N.need(A[0] != B[0], 'Os pontos t\u00eam a mesma abcissa: a reta \u00e9 '
               'vertical (x = ' + ex(A[0]) + ') e n\u00e3o \u00e9 uma fun\u00e7\u00e3o')
        m = (B[1] - A[1]) / (B[0] - A[0])
        b = A[1] - m * A[0]
        o += ['= m = (yB - yA) / (xB - xA)', 'm ' + N.rhs(m),
              'b = yA - m xA ' + N.rhs(b)]
    elif m is not None and A and b is None:
        m = m[0]
        b = A[1] - m * A[0]
        o += ['= b = yA - m xA', 'b ' + N.rhs(b)]
    elif b is not None and A and m is None:
        b = b[0]
        N.need(A[0] != 0, 'Com b e um ponto de abcissa 0 n\u00e3o d\u00e1 para '
               'saber o declive')
        m = (A[1] - b) / A[0]
        o += ['= m = (yA - b) / xA', 'm ' + N.rhs(m)]
    elif m is not None and b is not None and not A:
        m, b = m[0], b[0]
    else:
        N.need(0, 'D\u00e1 m e b, ou m e um ponto, ou b e um ponto, ou dois '
               'pontos')
    o.append('> f(x) = ' + lin(m, b))
    if m == 0:
        o += ['Fun\u00e7\u00e3o constante: D\u2032f = {' + ex(b) + '}.',
              'Zeros: ' + ('todos os x' if b == 0 else 'nenhum') + '.']
    else:
        z = -b / m
        o += ['Zero: x = -b / m ' + N.rhs(z),
              'f > 0 em ' + (iv(z, None) if m > 0 else iv(None, z)) +
              '; f < 0 em ' + (iv(None, z) if m > 0 else iv(z, None)),
              ('Crescente' if m > 0 else 'Decrescente') + ' em \u211d (m ' +
              ('> 0' if m > 0 else '< 0') + '); D\u2032f = \u211d']
    c = 0.0 if m == 0 else -b / m
    w = max(5.0, abs(c) * 1.5, abs(b) / max(abs(m), 0.1))
    g = ('f(x) = ' + lin(m, b), [('f', lambda x: m * x + b, 4),
                                  ('p', [p for p in (A, B) if p], 5)],
         c - w, c + w, min(-w, b - w), max(w, b + w), 'y = ' + lin(m, b))
    st = 'Declive: m = (y2 - y1) / (x2 - x1); ordenada na origem: b = f(0).' \
        '\nm > 0: crescente; m < 0: decrescente; m = 0: constante.'
    return ('\n'.join(o), st, m, '', g)

# ------------------------------------------------------------ ramos


def ramos():
    return ('Fun\u00e7\u00e3o definida por ramos',
            [N.fld('Ramo 1: f(x) =', '', '-x', 't'),
             N.fld('Fronteira a', '', '0'),
             N.fld('Ramo 2: f(x) =', '', 'x^2', 't'),
             N.fld('Fronteira c (s\u00f3 com 3 ramos)', '', '', 'o'),
             N.fld('Ramo 3: f(x) = (opcional)', '', '', 't'),
             N.fld('Cada fronteira pertence ao ramo', '', '', 'c',
                   ['da direita (x \u2265 a)', 'da esquerda (x \u2264 a)']),
             N.fld('Calcular f em x = (opcional)', '', '', 'o')], _ramos)


def _ramos(v):
    r1, a, r2, c, r3, k, x0 = v
    N.need(r1 and r2, 'Escreve pelo menos os dois primeiros ramos')
    a = a[0]
    cs = [N.comp(r1), N.comp(r2)]
    fs = [a]
    nm = [r1, r2]
    if c is not None or r3:
        N.need(c is not None and r3, 'Com 3 ramos, escreve a fronteira c e o '
               '3.\u00ba ramo')
        N.need(c[0] > a, 'A fronteira c tem de ser maior do que a')
        fs.append(c[0])
        cs.append(N.comp(r3))
        nm.append(r3)
    esq = k == 1

    def qual(x):
        for i in range(len(fs)):
            if x < fs[i] or (esq and x == fs[i]):
                return i
        return len(fs)

    def f(x):
        return N.ev(cs[qual(x)], x)
    lt, le, ge, gt = ' < ', ' \u2264 ', ' \u2265 ', ' > '
    o = ['f(x) =']
    for i in range(len(cs)):
        if i == 0:
            cond = 'x' + (le if esq else lt) + ex(fs[0])
        elif i == len(cs) - 1:
            cond = 'x' + (gt if esq else ge) + ex(fs[-1])
        else:
            cond = ex(fs[i - 1]) + (lt if esq else le) + 'x' + \
                (le if esq else lt) + ex(fs[i])
        o.append('  ' + nm[i] + ', se ' + cond)
    r = None
    if x0 is not None:
        y = safe(f, x0[0])
        N.need(y is not None, 'f n\u00e3o est\u00e1 definida em x = ' + ex(x0[0]))
        o.append('> f(' + ex(x0[0]) + ') ' + N.rhs(y) + ' (ramo ' +
                 str(qual(x0[0]) + 1) + ')')
        r = y
    for i in range(len(fs)):
        e = safe(lambda x: N.ev(cs[i], x), fs[i])
        d = safe(lambda x: N.ev(cs[i + 1], x), fs[i])
        if e is None or d is None:
            continue
        o.append('Em x = ' + ex(fs[i]) + ': ramo ' + str(i + 1) + ' d\u00e1 ' +
                 ex(e) + ', ramo ' + str(i + 2) + ' d\u00e1 ' + ex(d) +
                 (' (cont\u00ednua)' if abs(e - d) < 1e-12 else ' (salto)'))
    lo_x, hi_x = fs[0] - 10, fs[-1] + 10
    zs, fa = zeros(f, lo_x, hi_x, 800)
    o.append('Zeros em ' + iv(lo_x, hi_x, 1, 1) + ': ' + (lista(zs) if zs
                                                          else 'nenhum'))
    its = []
    bs = [lo_x] + fs + [hi_x]
    for i in range(len(cs)):
        def g(x, i=i):
            N.need(bs[i] <= x <= bs[i + 1], '')
            return N.ev(cs[i], x)
        its.append(('f', g, (4, 5, 6)[i]))
    y0, y1 = janela(f, lo_x, hi_x)
    gr = ('Fun\u00e7\u00e3o por ramos', its, lo_x, hi_x, y0, y1,
          'cada cor \u00e9 um ramo')
    st = 'Para calcular f(x), escolhe-se primeiro o ramo a que x ' \
        'pertence.\nEqua\u00e7\u00f5es: resolve-se ramo a ramo e s\u00f3 se ficam ' \
        'as solu\u00e7\u00f5es que est\u00e3o no intervalo desse ramo.'
    return ('\n'.join(o), st, r, '', gr)

# ------------------------------------------------------------ modulo


def mod():
    return ('Fun\u00e7\u00e3o m\u00f3dulo',
            [N.fld('a (em a|x - h| + k)', '', '1'),
             N.fld('h', '', '0'),
             N.fld('k', '', '0'),
             N.fld('Condi\u00e7\u00e3o (opcional)', '', '', 'c',
                   ['f(x) = c', 'f(x) < c', 'f(x) > c']),
             N.fld('c (opcional)', '', '', 'o')], _mod)


def _mod(v):
    a, h, k, t, c = v
    a, h, k = a[0], h[0], k[0]
    N.need(a != 0, 'Com a = 0 a fun\u00e7\u00e3o \u00e9 constante (k)')

    def f(x):
        return a * abs(x - h) + k
    o = ['f(x) = ' + ('' if a == 1 else ('-' if a == -1 else ex(a))) +
         '|x' + (' - ' + ex(h) if h > 0 else (' + ' + ex(-h) if h < 0 else '')) +
         '|' + (' + ' + ex(k) if k > 0 else (' - ' + ex(-k) if k < 0 else '')),
         'Ramos:',
         '  ' + lin(a, k - a * h) + ', se x \u2265 ' + ex(h),
         '  ' + lin(-a, k + a * h) + ', se x < ' + ex(h),
         'V\u00e9rtice: ' + pt(ex(h), ex(k)) + '; ' + (
             'm\u00ednimo ' if a > 0 else 'm\u00e1ximo ') + ex(k),
         'D\u2032f = ' + (iv(k, None, 1) if a > 0 else iv(None, k, 0, 1)),
         ('Decrescente em ' + iv(None, h, 0, 1) + ' e crescente em ' +
          iv(h, None, 1)) if a > 0 else ('Crescente em ' + iv(None, h, 0, 1) +
                                         ' e decrescente em ' + iv(h, None, 1))]

    def resolve(cc, rel):
        # |x - h| rel d, com d = (cc - k) / a (rel troca se a < 0)
        d = (cc - k) / a
        if a < 0 and rel != '=':
            rel = '>' if rel == '<' else '<'
        if rel == '=':
            if d < 0:
                return '\u2205'
            if d == 0:
                return '{' + ex(h) + '}'
            return '{' + lista([h - d, h + d]) + '}'
        if rel == '<':
            return iv(h - d, h + d) if d > 0 else '\u2205'
        if d < 0:
            return '\u211d'
        if d == 0:
            return '\u211d \\ {' + ex(h) + '}'
        return iv(None, h - d) + UN + iv(h + d, None)
    o.append('Zeros: C.S. = ' + resolve(0.0, '='))
    r = None
    if c is not None:
        rel = ('=', '<', '>')[t]
        o.append('> ' + ('f(x) = ', 'f(x) < ', 'f(x) > ')[t] + ex(c[0]) +
                 ': C.S. = ' + resolve(c[0], rel))
        r = c[0]
    lo, hi = h - 6, h + 6
    y0, y1 = janela(f, lo, hi)
    g = ('Fun\u00e7\u00e3o m\u00f3dulo', [('f', f, 4), ('p', [(h, k)], 5)],
         lo, hi, y0, y1, 'v\u00e9rtice em ' + pt(ex(h), ex(k)))
    st = '|x - h| = x - h se x \u2265 h e |x - h| = -(x - h) se x < h.\n' \
        'O gr\u00e1fico \u00e9 o de |x| transladado para o v\u00e9rtice (h, k) e ' \
        'multiplicado por a.'
    return ('\n'.join(o), st, r, '', g)
