# c_matq.py - M1TR4M: calculadoras da funcao quadratica (equacao do
# 2.o grau e estudo da funcao, inequacoes do 2.o grau, transformacoes
# de funcoes). Forma exata (fracoes e radicais) quando os coeficientes
# sao racionais; senao, valores aproximados.
#@ c_matq.q2|Equa\u00e7\u00e3o do 2.\u00ba grau e fun\u00e7\u00e3o quadr\u00e1tica|f\u00f3rmula resolvente bin\u00f3mio discriminante zeros v\u00e9rtice eixo concavidade par\u00e1bola|M|m5
#@ c_matq.iq|Inequa\u00e7\u00f5es do 2.\u00ba grau|inequa\u00e7\u00e3o conjunto-solu\u00e7\u00e3o intervalos sinal par\u00e1bola|M|m5
#@ c_matq.tf|Transforma\u00e7\u00f5es de fun\u00e7\u00f5es|transla\u00e7\u00e3o dilata\u00e7\u00e3o contra\u00e7\u00e3o reflex\u00e3o gr\u00e1fico f(x-a)+b c f(x)|M|m5
# Casos-limite: a = 0 (equacao do 1.o grau), delta = 0 (um zero), delta < 0
# (sem zeros), coeficientes com fracoes (1/2) ou raizes (sqrt 2, so
# aproximado), inequacao sem solucao (conjunto vazio) ou com R como
# solucao, expressao com simbolos desconhecidos.

import math
import m1_nucleo as N

X = N.X
INF = '+\u221e'
MINF = '-\u221e'

# ------------------------------------------------------------ racionais


def nr(n, d):
    g = N.gcd(n, d) or 1
    if d < 0:
        n, d = -n, -d
    return (n // g, d // g)


def rat(x):
    return N.frac(x, 100000)


def radd(a, b):
    return nr(a[0] * b[1] + b[0] * a[1], a[1] * b[1])


def rmul(a, b):
    return nr(a[0] * b[0], a[1] * b[1])


def rs(a):
    return N.fstr(a[0], a[1])


def rv(a):
    return 1.0 * a[0] / a[1]


def num(x, ex=None):
    # Texto de um valor: exato quando ha forma exata, senao aproximado.
    if ex is not None:
        return ex
    return N.fmt(x)


def coef(c, first=0, var='x\u00b2'):
    # Termo de um polinomio: coeficiente c (racional ou float) e variavel.
    v = rv(c) if isinstance(c, tuple) else c
    if v == 0:
        return ''
    s = rs((abs(c[0]), c[1])) if isinstance(c, tuple) else N.fmt(abs(v))
    if '/' in s and var:
        s = '(' + s + ')'
    if s == '1' and var:
        s = ''
    sg = '-' if v < 0 else ('' if first else '+')
    return (sg + ('' if first else ' ') if not first else sg) + s + var


def poly(a, b, c):
    t = [x for x in (coef(a, 1, 'x\u00b2'), coef(b, 0, 'x'), coef(c, 0, ''))
         if x]
    s = t[0]
    for x in t[1:]:
        s = s + ' ' + x
    return s.replace('+ -', '- ')


def roots(a, b, c, ra, rb, rc):
    # Zeros de ax^2+bx+c: lista de (valor, texto exato ou None), o
    # discriminante e o seu texto.
    d = b * b - 4 * a * c
    ex = ra is not None and rb is not None and rc is not None
    dt = rs(radd(rmul(rb, rb), rmul((-4, 1), rmul(ra, rc)))) if ex else \
        N.fmt(d)
    if ex:
        D = radd(rmul(rb, rb), rmul((-4, 1), rmul(ra, rc)))
        d = rv(D)
    if d < 0:
        return [], d, dt
    if not ex:
        if d == 0:
            return [(-b / (2 * a), None)], d, dt
        s = math.sqrt(d)
        r = sorted([(-b - s) / (2 * a), (-b + s) / (2 * a)])
        return [(r[0], None), (r[1], None)], d, dt
    P = nr(-rb[0] * ra[1], 2 * rb[1] * ra[0])
    if D[0] == 0:
        return [(rv(P), rs(P))], 0.0, dt
    k, m = N.rad(D[0] * D[1])
    Q = nr(k * ra[1], D[1] * 2 * abs(ra[0]))
    Q = (abs(Q[0]), Q[1])
    if m == 1:
        r1 = radd(P, (-Q[0], Q[1]))
        r2 = radd(P, Q)
        return [(rv(r1), rs(r1)), (rv(r2), rs(r2))], d, dt
    L = P[1] * Q[1] // N.gcd(P[1], Q[1])
    A = P[0] * L // P[1]
    B = Q[0] * L // Q[1]
    g = N.gcd(N.gcd(A, B), L)
    A, B, L = A // g, B // g, L // g
    sq = ('' if B == 1 else str(B)) + '\u221a' + str(m)
    out = []
    for sg in (-1, 1):
        if A == 0:
            t = ('-' if sg < 0 else '') + sq
        else:
            t = str(A) + (' - ' if sg < 0 else ' + ') + sq
        if L != 1:
            t = '(' + t + ')/' + str(L) if A != 0 else t + '/' + str(L)
        out.append(((A + sg * B * math.sqrt(m)) / L, t))
    out.sort(key=lambda x: x[0])
    return out, d, dt


def sep(*ts):
    # Separador ", " ou "; " (quando algum valor tem virgula decimal).
    for t in ts:
        if ',' in t:
            return '; '
    return ', '


def pt(a, b):
    return '(' + a + sep(a, b) + b + ')'


def iv(a, b, ca, cb):
    # Intervalo "]a, b[" (a, b: textos; None = infinito).
    sa = MINF if a is None else a
    sb = INF if b is None else b
    return ('[' if ca and a is not None else ']') + sa + sep(sa, sb) + sb + \
        (']' if cb and b is not None else '[')


def reads(v):
    # Coeficientes: (a, b, c) em float e em racional (ou None).
    a, b, c = v[0][0], v[1][0], v[2][0]
    ra = rat(a)
    rb = rat(b)
    rc = rat(c)
    return a, b, c, ra, rb, rc


def fields():
    return [N.fld('a (coeficiente de x\u00b2)', '', '1'),
            N.fld('b (coeficiente de x)', '', '0'),
            N.fld('c (termo independente)', '', '0')]


def window(a, b, c, zs):
    # Janela do grafico: centrada no vertice, com os zeros bem visiveis.
    h = -b / (2 * a) if a else 0
    k = c - b * b / (4 * a) if a else c
    if zs:
        s = max([abs(z[0] - h) for z in zs])
    else:
        s = math.sqrt(abs(k / a)) if a else 1.0
    w = max(1.0, 1.6 * s)
    x0 = h - w
    x1 = h + w
    ys = [a * x * x + b * x + c for x in (x0, x1, h)]
    y0 = min(ys + [0])
    y1 = max(ys + [0])
    dy = (y1 - y0) * 0.1 or 1.0
    return x0, x1, y0 - dy, y1 + dy

# ------------------------------------------------------------ 2.o grau


def q2():
    return ('Equa\u00e7\u00e3o do 2.\u00ba grau', fields(), _q2)


def lin(b, c, rb, rc):
    # bx + c = 0 (quando a = 0).
    if b == 0:
        return 'a = 0 e b = 0: n\u00e3o \u00e9 uma equa\u00e7\u00e3o do 1.\u00ba nem do 2.\u00ba ' \
            'grau (' + ('imposs\u00edvel' if c != 0 else 'poss\u00edvel e ' +
                        'indeterminada') + ').'
    x = -c / b
    ex = rs(nr(-rc[0] * rb[1], rc[1] * rb[0])) if rb and rc else None
    r = N.rhs(x)
    if ex is not None and '= ' + ex not in r:
        r = '= ' + ex + ' ' + r
    return 'a = 0: a equa\u00e7\u00e3o \u00e9 do 1.\u00ba grau.\n= x = -c / b\n> x ' + r


def _q2(v):
    a, b, c, ra, rb, rc = reads(v)
    if a == 0:
        return (lin(b, c, rb, rc), '', None, '')
    zs, d, dt = roots(a, b, c, ra, rb, rc)
    o = ['f(x) = ' + poly(ra or a, rb or b, rc or c),
         '= \u0394 = b\u00b2 - 4ac = ' + dt]
    if d > 0:
        o.append('\u0394 > 0: dois zeros')
    elif d == 0:
        o.append('\u0394 = 0: um zero (duplo)')
    else:
        o.append('\u0394 < 0: n\u00e3o h\u00e1 zeros (a equa\u00e7\u00e3o \u00e9 imposs\u00edvel em \u211d)')
    if zs:
        o.append('= x = (-b \u00b1 \u221a\u0394) / (2a)')
        o.append('> ' + ' \u2228 '.join(['x = ' + z[1] if z[1] is not None
                                         else 'x ' + N.eq(z[0]) for z in zs]))
        if zs[0][1] is not None and '\u221a' in zs[0][1]:
            o.append('  (' + ' \u2228 '.join(['x ' + N.AP + ' ' + N.fmt(z[0])
                                         for z in zs]) + ')')
        ts = [num(z[0], z[1]) for z in zs]
        o.append('C.S. = {' + sep(*ts).join(ts) + '}')
    else:
        o.append('C.S. = \u2205')
    h = -b / (2 * a)
    k = c - b * b / (4 * a)
    hx = kx = None
    if ra and rb and rc:
        H = nr(-rb[0] * ra[1], 2 * rb[1] * ra[0])
        K = radd(rc, rmul((-1, 1), rmul(rmul(rb, rb), nr(ra[1], 4 * ra[0]))))
        hx, kx = rs(H), rs(K)
        h, k = rv(H), rv(K)
    sh = num(h, hx)
    sk = num(k, kx)
    up = a > 0
    o += ['V\u00e9rtice: V' + pt(sh, sk), 'Eixo de simetria: x = ' + sh,
          'Concavidade voltada para ' + ('cima' if up else 'baixo') +
          ' (a ' + ('>' if up else '<') + ' 0)',
          ('M\u00ednimo' if up else 'M\u00e1ximo') + ': ' + sk + ' (em x = ' + sh + ')',
          "D\u2032f = " + (iv(sk, None, 1, 0) if up else iv(None, sk, 0, 1)),
          ('Decrescente' if up else 'Crescente') + ' em ' + iv(None, sh, 0, 1) +
          '; ' + ('crescente' if up else 'decrescente') + ' em ' +
          iv(sh, None, 1, 0)]
    if hx is not None:
        # forma canonica a(x - h)^2 + k
        sa = '' if ra == (1, 1) else ('-' if ra == (-1, 1) else
                                      (rs(ra) if ra[1] == 1 else
                                       '(' + rs(ra) + ')'))
        if H[0] == 0:
            fc = sa + 'x\u00b2'
        else:
            fc = sa + '(x ' + ('- ' + rs(H) if H[0] > 0 else
                               '+ ' + rs((-H[0], H[1]))) + ')\u00b2'
        if K[0] != 0:
            fc = fc + (' + ' if K[0] > 0 else ' - ') + rs((abs(K[0]), K[1]))
        o.append('Forma can\u00f3nica: f(x) = ' + fc)
    o.append(sign(a, zs))
    x0, x1, y0, y1 = window(a, b, c, zs)
    g = ('f(x) = ' + poly(ra or a, rb or b, rc or c),
         [('f', lambda x: a * x * x + b * x + c, 2),
          ('p', [(z[0], 0) for z in zs] + [(h, k)], 5)],
         x0, x1, y0, y1, 'pontos: zeros e v\u00e9rtice')
    st = 'F\u00f3rmula resolvente: x = (-b \u00b1 \u221a(b\u00b2 - 4ac)) / (2a).\n' \
        'V\u00e9rtice: x = -b/(2a) e y = f(-b/(2a)).\n' \
        'Na forma a(x - h)\u00b2 + k, o v\u00e9rtice \u00e9 (h; k).'
    return ('\n'.join(o), st, zs[0][0] if zs else None, '', g)


def sign(a, zs):
    up = a > 0
    p, n = ('positiva', 'negativa') if up else ('negativa', 'positiva')
    t = [num(z[0], z[1]) for z in zs]
    if len(zs) == 2:
        return 'Sinal: ' + p + ' em ' + iv(None, t[0], 0, 0) + ' \u222a ' + \
            iv(t[1], None, 0, 0) + '; ' + n + ' em ' + iv(t[0], t[1], 0, 0) + \
            '; nula em ' + t[0] + ' e ' + t[1]
    if len(zs) == 1:
        return 'Sinal: ' + p + ' em \u211d \\ {' + t[0] + '}; nula em ' + t[0]
    return 'Sinal: ' + p + ' em \u211d (sem zeros)'

# ------------------------------------------------------------ inequacoes
OPS = ('>', '\u2265', '<', '\u2264')


def iq():
    return ('Inequa\u00e7\u00e3o do 2.\u00ba grau', fields() +
            [N.fld('Sinal: a x\u00b2 + b x + c ... 0', '', '', 'c', list(OPS))],
            _iq)


def _iq(v):
    a, b, c, ra, rb, rc = reads(v)
    op = v[3]
    P = poly(ra or a, rb or b, rc or c)
    o = [P + ' ' + OPS[op] + ' 0']
    if a == 0:
        o.append('a = 0: a inequa\u00e7\u00e3o \u00e9 do 1.\u00ba grau (resolve bx + c ' +
                 OPS[op] + ' 0).')
        return ('\n'.join(o), '', None, '')
    zs, d, dt = roots(a, b, c, ra, rb, rc)
    t = [num(z[0], z[1]) for z in zs]
    o.append('Zeros: ' + (' e '.join(t) if t else 'n\u00e3o h\u00e1 (\u0394 = ' + dt +
                                               ' < 0)'))
    pos = op < 2                     # queremos f(x) > 0 ou >= 0
    eq = op in (1, 3)                # inclui os zeros
    want_out = (a > 0) == pos        # fora dos zeros
    if len(zs) == 2:
        if want_out:
            cs = iv(None, t[0], 0, eq) + ' \u222a ' + iv(t[1], None, eq, 0)
            seg = [(zs[0][0] - 1e6, zs[0][0]), (zs[1][0], zs[1][0] + 1e6)]
        else:
            cs = iv(t[0], t[1], eq, eq)
            seg = [(zs[0][0], zs[1][0])]
    elif len(zs) == 1:
        if want_out:
            cs = '\u211d' if eq else '\u211d \\ {' + t[0] + '}'
            seg = [(-1e6, 1e6)]
        else:
            cs = '{' + t[0] + '}' if eq else '\u2205'
            seg = [(zs[0][0], zs[0][0])] if eq else []
    else:
        cs = '\u211d' if want_out else '\u2205'
        seg = [(-1e6, 1e6)] if want_out else []
    o.append('Par\u00e1bola com concavidade para ' + ('cima' if a > 0 else 'baixo') +
             ': ' + sign(a, zs)[7:])
    o.append('> C.S. = ' + cs)
    x0, x1, y0, y1 = window(a, b, c, zs)
    sg = [(max(s[0], x0), 0, min(s[1], x1), 0) for s in seg]
    g = (P + ' ' + OPS[op] + ' 0', [('f', lambda x: a * x * x + b * x + c, 2),
                                    ('s', sg, 6), ('p', [(z[0], 0) for z in zs],
                                                   5)],
         x0, x1, y0, y1, 'verde: conjunto-solu\u00e7\u00e3o no eixo dos x')
    return ('\n'.join(o), 'Calculam-se os zeros, esbo\u00e7a-se a par\u00e1bola e '
            'l\u00ea-se onde fica acima (> 0) ou abaixo (< 0) do eixo dos x.',
            None, '', g)

# ------------------------------------------------------------ transformacoes
TT = ('g(x) = f(x - a)', 'g(x) = f(x) + b', 'g(x) = c ' + X + ' f(x)',
      'g(x) = f(x - a) + b')


def tf():
    return ('Transforma\u00e7\u00f5es de fun\u00e7\u00f5es',
            [N.fld('f(x) =', '', 'x^2', 't'),
             N.fld('Transforma\u00e7\u00e3o', '', '', 'c', list(TT)),
             N.fld('a', '', '0', 'o'), N.fld('b', '', '0', 'o'),
             N.fld('c', '', '1', 'o')], _tf)


def _tf(v):
    fx, tp, a, b, c = v
    code = N.comp(fx)
    a = a[0] if a else 0.0
    b = b[0] if b else 0.0
    c = c[0] if c else 1.0

    def f(x):
        return N.ev(code, x)
    if tp == 0:
        b, c = 0.0, 1.0
    elif tp == 1:
        a, c = 0.0, 1.0
    elif tp == 2:
        a, b = 0.0, 0.0
    else:
        c = 1.0

    def g(x):
        return c * f(x - a) + b
    o = ['f(x) = ' + fx, TT[tp].replace('a', N.fmt(a)).replace(
        'b', N.fmt(b)).replace('c ', N.fmt(c) + ' ')]
    if a:
        o.append('- Transla\u00e7\u00e3o horizontal de ' + N.fmt(abs(a)) +
                 (' para a direita' if a > 0 else ' para a esquerda'))
    if b:
        o.append('- Transla\u00e7\u00e3o vertical de ' + N.fmt(abs(b)) +
                 (' para cima' if b > 0 else ' para baixo'))
    if c != 1:
        N.need(c != 0, 'Com c = 0 o gr\u00e1fico de g \u00e9 o eixo dos x')
        ac = abs(c)
        if ac > 1:
            o.append('- Dilata\u00e7\u00e3o vertical de coeficiente ' + N.fmt(ac))
        elif ac < 1:
            o.append('- Contra\u00e7\u00e3o vertical de coeficiente ' + N.fmt(ac))
        if c < 0:
            o.append('- Reflex\u00e3o no eixo dos x (c < 0)')
    o.append('Cada ponto (x; y) de f passa a (x + a; c' + X + 'y + b).')
    xs = [-10 + i * 0.5 for i in range(41)]
    ys = []
    for x in xs:
        for h in (f, g):
            try:
                ys.append(h(x))
            except Exception:
                pass
    N.need(ys, 'A fun\u00e7\u00e3o n\u00e3o tem valores entre -10 e 10')
    ys.sort()
    lo = ys[len(ys) // 10]
    hi = ys[len(ys) * 9 // 10]
    d = (hi - lo) * 0.3 or 2.0
    gr = ('f (azul) e g (vermelho)', [('f', f, 4), ('f', g, 5)], -10.0, 10.0,
          lo - d, hi + d, 'azul: f \u00b7 vermelho: g')
    return ('\n'.join(o), '', None, '', gr)
