# c_mgeo.py - M1TR4M: resolvedores de geometria do 7.o ao 9.o ano:
# angulos (complementar, suplementar, triangulo, poligonos, retas
# paralelas cortadas por uma secante, com desenho) e areas e perimetros
# de figuras planas. A medida em falta calcula-se a partir da area ou
# do perimetro conhecidos (os solidos estao em c_msol).
#@ c_mgeo.ang|\u00c2ngulos, tri\u00e2ngulos e pol\u00edgonos|\u00e2ngulos complementares suplementares verticalmente opostos soma dos \u00e2ngulos internos externos tri\u00e2ngulo pol\u00edgono diagonais pol\u00edgono regular retas paralelas secante correspondentes alternos internos|M|g7
#@ c_mgeo.area|\u00c1reas e per\u00edmetros de figuras planas|\u00e1rea per\u00edmetro quadrado ret\u00e2ngulo paralelogramo tri\u00e2ngulo losango trap\u00e9zio pol\u00edgono regular ap\u00f3tema c\u00edrculo setor circular coroa medida em falta|M|g7
# Casos-limite: angulos nulos, retos ou rasos, soma dos angulos do
# triangulo >= 180, n nao inteiro ou menor do que 3, poligono regular
# inexistente, medidas a mais ou em falta, dados incompativeis (medida
# calculada nao positiva), setor com mais de 360 graus.

import math
import m1_nucleo as N

G = '\u00b0'
X = N.X


def nv(x):
    # Medida escrita: decimal quando e exato, senao forma exata.
    s, ex = N.fmt2(x, 0, -1)
    if ex:
        return s
    e = N.exact(x)
    return e if e is not None else s


def eq(a, b):
    return abs(a - b) < 1e-9 * max(1.0, abs(a), abs(b))


def gms(x):
    # Graus e minutos (e segundos) quando a amplitude nao e inteira.
    if eq(x, round(x)):
        return ''
    t = abs(x) * 3600
    s = int(round(t))
    d, m, r = s // 3600, s // 60 % 60, s % 60
    return ' (' + ('= ' if abs(t - s) < 1e-6 else N.AP + ' ') + str(d) + \
        G + ' ' + str(m) + "'" + (' ' + str(r) + '"' if r else '') + ')'


def ga(x):
    # "= 55\u00b0", "= 900/7 \u2248 128,57\u00b0 (\u2248 128\u00b0 34' 17")".
    return N.rhs(x, 2) + G + gms(x)

# ------------------------------------------------------------ angulos


OPA = ['Complementar e suplementar', 'Tri\u00e2ngulo: 3.\u00ba \u00e2ngulo',
       'Pol\u00edgono de n lados', 'n pelo \u00e2ngulo interno (regular)',
       'n pelo \u00e2ngulo externo (regular)', 'n pela soma dos \u00e2ngulos internos',
       'Paralelas e secante (desenho)']
NOMES = {3: 'tri\u00e2ngulo', 4: 'quadril\u00e1tero', 5: 'pent\u00e1gono', 6: 'hex\u00e1gono',
         7: 'hept\u00e1gono', 8: 'oct\u00f3gono', 9: 'ene\u00e1gono', 10: 'dec\u00e1gono',
         11: 'undec\u00e1gono', 12: 'dodec\u00e1gono', 15: 'pentadec\u00e1gono',
         20: 'icos\u00e1gono'}


def ang():
    return ('\u00c2ngulos e pol\u00edgonos',
            [N.fld('Calcular', '', '', 'c', OPA),
             N.fld('Dado: \u00e2ngulo (graus), n ou soma', '', '35', 'o'),
             N.fld('2.\u00ba \u00e2ngulo (s\u00f3 no tri\u00e2ngulo)', '', '', 'o')], _ang)


def _ang(v):
    k, a, b = v
    N.need(a is not None, 'Escreve o dado (\u00e2ngulo, n ou soma)')
    a = a[0]
    if k == 0:
        return compl(a)
    if k == 1:
        N.need(b is not None, 'Escreve o 2.\u00ba \u00e2ngulo do tri\u00e2ngulo')
        return triang(a, b[0])
    if k == 6:
        return paralelas(a)
    o = []
    if k == 2:
        N.need(eq(a, round(a)), 'O n\u00famero de lados n tem de ser inteiro')
        n = int(round(a))
    else:
        N.pos(a, 'O dado')
        if k == 3:
            N.need(a < 180, 'O \u00e2ngulo interno de um pol\u00edgono convexo \u00e9 '
                   'menor do que 180\u00b0')
            e = 180 - a
            o += ['= \u00e2ngulo externo = 180\u00b0 - \u00e2ngulo interno',
                  '180\u00b0 - ' + nv(a) + '\u00b0 ' + ga(e)]
        else:
            e = a
        if k == 5:
            x = a / 180 + 2
            o += ['= S = (n - 2) ' + X + ' 180\u00b0  \u21d4  n = S : 180\u00b0 + 2',
                  'n = ' + nv(a) + ' : 180 + 2 ' + N.rhs(x, 2)]
        else:
            N.need(e <= 120, 'O \u00e2ngulo externo de um pol\u00edgono regular \u00e9 '
                   'no m\u00e1ximo 120\u00b0 (tri\u00e2ngulo)')
            x = 360 / e
            o += ['= n = 360\u00b0 : \u00e2ngulo externo',
                  'n = 360\u00b0 : ' + nv(e) + '\u00b0 ' + N.rhs(x, 2)]
        n = int(round(x))
        if not eq(x, n):
            if abs(x - n) < 0.01 and n >= 3:
                o.append('n ' + N.AP + ' ' + str(n) + ': o dado parece '
                         'arredondado; uso n = ' + str(n) + '.')
            else:
                o.append('> N\u00e3o h\u00e1 pol\u00edgono ' + ('' if k == 5 else 'regular ')
                         + 'assim: n tem de ser um n\u00famero inteiro.')
                return ('\n'.join(o), ST_POL, None, '')
    N.need(3 <= n <= 10 ** 6, 'Um pol\u00edgono tem pelo menos 3 lados')
    poligono(n, o)
    return ('\n'.join(o), ST_POL, (n - 2) * 180, '')


def poligono(n, o):
    nm = NOMES.get(n)
    s = (n - 2) * 180
    o += ['Pol\u00edgono de ' + str(n) + ' lados' + (' (' + nm + ')' if nm else '')
          + '.', '= Soma dos \u00e2ngulos internos: S = (n - 2) ' + X + ' 180\u00b0',
          '> S = (' + str(n) + ' - 2) ' + X + ' 180\u00b0 = ' + str(s) + G,
          'Soma dos \u00e2ngulos externos: 360\u00b0 (em qualquer pol\u00edgono convexo).',
          'Se for regular: \u00e2ngulo interno = ' + str(s) + '\u00b0 : ' + str(n) +
          ' ' + ga(s / n), '\u00e2ngulo externo = 360\u00b0 : ' + str(n) + ' ' +
          ga(360 / n)]
    if n == 3:
        o.append('O tri\u00e2ngulo n\u00e3o tem diagonais.')
    else:
        o += ['= Diagonais: d = n(n - 3) / 2', '> d = ' + str(n) + ' ' + X +
              ' ' + str(n - 3) + ' / 2 = ' + str(n * (n - 3) // 2),
              'De cada v\u00e9rtice saem ' + str(n - 3) + ' diagonais; dividem o '
              'pol\u00edgono em ' + str(n - 2) + ' tri\u00e2ngulos.']
    o.append('Regular: ' + str(n) + ' eixos de simetria e simetria de '
             'rota\u00e7\u00e3o de ordem ' + str(n) + '.')


ST_POL = 'S = (n - 2) ' + X + ' 180\u00b0: o pol\u00edgono divide-se em n - 2 ' \
    'tri\u00e2ngulos.\nNum pol\u00edgono regular, \u00e2ngulo interno + \u00e2ngulo externo = ' \
    '180\u00b0 e \u00e2ngulo externo = 360\u00b0 : n.'


def compl(a):
    N.need(0 < a < 180, 'O \u00e2ngulo tem de estar entre 0\u00b0 e 180\u00b0')
    t = 'agudo' if a < 90 else ('reto' if eq(a, 90) else 'obtuso')
    o = ['\u03b1 = ' + nv(a) + '\u00b0: \u00e2ngulo ' + t + '.']
    r = None
    if a < 90 and not eq(a, 90):
        r = 90 - a
        o += ['= Complementar: 90\u00b0 - \u03b1', '> 90\u00b0 - ' + nv(a) + '\u00b0 ' +
              ga(r)]
    else:
        o.append('N\u00e3o tem complementar (s\u00f3 os \u00e2ngulos agudos t\u00eam).')
    o += ['= Suplementar: 180\u00b0 - \u03b1', '> 180\u00b0 - ' + nv(a) + '\u00b0 ' +
          ga(180 - a), 'O verticalmente oposto tamb\u00e9m mede ' + nv(a) + '\u00b0.']
    st = 'Complementares: somam 90\u00b0. Suplementares: somam 180\u00b0.\n' \
        '\u00c2ngulos verticalmente opostos s\u00e3o iguais.'
    return ('\n'.join(o), st, 180 - a if r is None else r, '')


def triang(a, b):
    N.need(a > 0 and b > 0, 'Os \u00e2ngulos t\u00eam de ser positivos')
    N.need(a + b < 180 and not eq(a + b, 180), 'A soma dos dois \u00e2ngulos tem '
           'de ser menor do que 180\u00b0')
    c = 180 - a - b
    o = ['= \u03b1 + \u03b2 + \u03b3 = 180\u00b0', '> \u03b3 = 180\u00b0 - ' + nv(a) +
         '\u00b0 - ' + nv(b) + '\u00b0 ' + ga(c)]
    m = max(a, b, c)
    t = 'ret\u00e2ngulo' if eq(m, 90) else ('obtus\u00e2ngulo' if m > 90 else
                                       'acut\u00e2ngulo')
    k = eq(a, b) + eq(b, c) + eq(a, c)
    o += ['Tri\u00e2ngulo ' + t + ' e ' + ('equil\u00e1tero' if k == 3 else
                                      ('is\u00f3sceles' if k else 'escaleno')) +
          ' (\u00e2ngulos iguais \u2194 lados iguais).',
          '\u00c2ngulos externos: ' + ', '.join([nv(180 - x) + G for x in
                                            (a, b, c)]) + ' (soma 360\u00b0).',
          'Cada \u00e2ngulo externo = soma dos dois internos n\u00e3o adjacentes.',
          'Ao maior \u00e2ngulo (' + nv(m) + '\u00b0) op\u00f5e-se o maior lado.']
    st = 'A soma dos \u00e2ngulos internos de um tri\u00e2ngulo \u00e9 180\u00b0.\n' \
        'Num tri\u00e2ngulo, ao maior \u00e2ngulo op\u00f5e-se o maior lado.'
    return ('\n'.join(o), st, c, '')


def paralelas(a):
    N.need(0 < a < 180, 'O \u00e2ngulo tem de estar entre 0\u00b0 e 180\u00b0')
    s1 = nv(a) + G
    s2 = nv(180 - a) + G
    o = ['\u00c2ngulos 1 a 4 na reta de cima e 5 a 8 na de baixo (ver o '
         'desenho).', '> 1 = 3 = 5 = 7 = ' + s1, '> 2 = 4 = 6 = 8 = ' + s2,
         'Verticalmente opostos (iguais): 1 e 3, 2 e 4, 5 e 7, 6 e 8.',
         'Correspondentes (iguais): 1 e 5, 2 e 6, 3 e 7, 4 e 8.',
         'Alternos internos (iguais): 3 e 5, 4 e 6.',
         'Alternos externos (iguais): 1 e 7, 2 e 8.',
         'Internos do mesmo lado (somam 180\u00b0): 3 e 6, 4 e 5.']
    if eq(a, 90):
        o.append('Secante perpendicular: os 8 \u00e2ngulos s\u00e3o retos.')
    st = 'Duas retas paralelas cortadas por uma secante: \u00e2ngulos ' \
        'correspondentes, alternos internos e alternos externos s\u00e3o iguais;' \
        ' internos do mesmo lado s\u00e3o suplementares.'
    gr = None
    if 12 <= a <= 168:
        t = a * math.pi / 180
        ux, uy = math.cos(t), math.sin(t)
        # Figura em y = 10..14: o 0 fica fora da janela (sem eixo).
        B = (20.0, 11.0)
        T = (20.0 + 2 * ux / uy, 13.0)
        p0 = (B[0] - ux / uy, 10.0)
        p1 = (T[0] + ux / uy, 14.0)
        x0 = min(p0[0], p1[0]) - 1.5
        x1 = max(p0[0], p1[0]) + 1.5
        w = max(x1 - x0, 2.1 * 4.6)
        h = w / 2.1
        cx = (x0 + x1) / 2
        X0, X1 = cx - w / 2, cx + w / 2
        d = h / 130
        rot = []
        for P, j0 in ((T, 1), (B, 5)):
            for j in range(4):
                b = (a / 2 + 90 * j) * math.pi / 180
                rot.append((P[0] + 0.55 * math.cos(b) - 6 * d,
                            P[1] + 0.55 * math.sin(b) + 6 * d, str(j0 + j)))
        gr = ('Paralelas cortadas por uma secante',
              [('s', [(X0, 11.0, X1, 11.0), (X0, 13.0, X1, 13.0)], 0),
               ('s', [(p0[0], p0[1], p1[0], p1[1])], 6),
               ('t', rot[:4], 2), ('t', rot[4:], 5)],
              X0, X1, 12 - h / 2, 12 + h / 2,
              '1=3=5=7: ' + s1 + '; 2=4=6=8: ' + s2)
    return ('\n'.join(o), st, a, '', gr) if gr else ('\n'.join(o), st, a, '')

# ------------------------------------------------------------ medidas


UN = ['u.c.', 'cm', 'm', 'mm', 'dm', 'km']


def ue(u, k):
    # Unidade de comprimento (k = 1), area (2) ou volume (3).
    if u == 'u.c.':
        return ('u.c.', 'u.a.', 'u.v.')[k - 1]
    return u + ('', '\u00b2', '\u00b3')[k - 1]


def lermed(v, nms, conh, livre=-1):
    # Medidas dadas (None = em falta). Devolve (lista, indice em falta).
    # A medida "livre" pode faltar sem valor conhecido (calcula-se).
    k = len(nms)
    for i in range(k, len(v)):
        N.need(v[i] is None, 'Esta figura s\u00f3 usa ' + str(k) + ' medida' +
               ('s (' + ', '.join(nms) + ')' if k > 1 else ' (' + nms[0] +
                ')'))
    m = [None if x is None else N.pos(x[0], nms[i] + ' (' + str(i + 1) +
                                       '.\u00aa medida)')
         for i, x in enumerate(v[:k])]
    f = [i for i in range(k) if m[i] is None]
    dados = [c for c in conh if c is not None]
    if not f:
        N.need(not dados, 'J\u00e1 deste todas as medidas: deixa vazia a '
               '\u00e1rea, o per\u00edmetro ou o volume conhecido')
        return m, -1
    N.need(len(f) == 1, 'Falta mais do que uma medida (' +
           ', '.join([nms[i] for i in f]) + ')')
    if f[0] == livre and not dados:
        return m, f[0]
    N.need(len(dados) == 1, 'Para calcular ' + nms[f[0]] + ', escreve ' +
           'um valor conhecido (\u00e1rea, per\u00edmetro ou volume)')
    return m, f[0]


def subst(tp, m, nms):
    # Substitui as medidas no modelo; a que falta fica com a letra.
    return tp.format(*[nms[i] if m[i] is None else nv(m[i])
                       for i in range(len(nms))])


def resolve(m, i, nms, val, nm, tp, inv, o):
    # Resolve "valor conhecido = formula" em ordem a medida i.
    N.need(i in inv, 'Com ' + nm + ' n\u00e3o sei calcular ' + nms[i] +
           '; escreve outra medida')
    o += [nv(val) + ' = ' + subst(tp, m, nms),
          '\u21d4 ' + nms[i] + ' = ' + inv[i][0]]
    try:
        r = inv[i][1](m, val)
    except (ValueError, ZeroDivisionError):
        r = -1
    N.need(r > 1e-12, 'Os dados n\u00e3o s\u00e3o compat\u00edveis: ' + nms[i] +
           ' daria um valor n\u00e3o positivo')
    m[i] = r

# ------------------------------------------------------------ areas


FIG = ['Quadrado (lado l)', 'Ret\u00e2ngulo (c, l)', 'Paralelogramo (b, h)',
       'Tri\u00e2ngulo (b, h)', 'Losango (D, d)', 'Trap\u00e9zio (B, b, h)',
       'Pol\u00edgono regular (n, l, ap)', 'C\u00edrculo (raio r)',
       'Setor circular (r, \u03b1)', 'Coroa circular (R, r)']
sq = math.sqrt
PI = math.pi
# Por figura: medidas; area (formula, modelo, funcao); perimetro (idem
# ou None); inversas pela area e pelo perimetro {medida: (formula, f)}.
FA = (
    ('l', ('A = l\u00b2', '{0}\u00b2', lambda m: m[0] ** 2),
     ('P = 4 ' + X + ' l', '4 ' + X + ' {0}', lambda m: 4 * m[0]),
     {0: ('\u221aA', lambda m, A: sq(A))}, {0: ('P / 4', lambda m, P: P / 4)}),
    ('c l', ('A = c ' + X + ' l', '{0} ' + X + ' {1}', lambda m: m[0] * m[1]),
     ('P = 2 ' + X + ' c + 2 ' + X + ' l', '2 ' + X + ' {0} + 2 ' + X + ' {1}',
      lambda m: 2 * m[0] + 2 * m[1]),
     {0: ('A / l', lambda m, A: A / m[1]), 1: ('A / c', lambda m, A: A / m[0])},
     {0: ('P / 2 - l', lambda m, P: P / 2 - m[1]),
      1: ('P / 2 - c', lambda m, P: P / 2 - m[0])}),
    ('b h', ('A = b ' + X + ' h', '{0} ' + X + ' {1}', lambda m: m[0] * m[1]),
     None, {0: ('A / h', lambda m, A: A / m[1]),
            1: ('A / b', lambda m, A: A / m[0])}, {}),
    ('b h', ('A = b ' + X + ' h / 2', '{0} ' + X + ' {1} / 2',
             lambda m: m[0] * m[1] / 2), None,
     {0: ('2 ' + X + ' A / h', lambda m, A: 2 * A / m[1]),
      1: ('2 ' + X + ' A / b', lambda m, A: 2 * A / m[0])}, {}),
    ('D d', ('A = D ' + X + ' d / 2', '{0} ' + X + ' {1} / 2',
             lambda m: m[0] * m[1] / 2),
     ('P = 4 ' + X + ' \u221a((D/2)\u00b2 + (d/2)\u00b2)', '4 ' + X +
      ' \u221a(({0}/2)\u00b2 + ({1}/2)\u00b2)',
      lambda m: 4 * sq((m[0] / 2) ** 2 + (m[1] / 2) ** 2)),
     {0: ('2 ' + X + ' A / d', lambda m, A: 2 * A / m[1]),
      1: ('2 ' + X + ' A / D', lambda m, A: 2 * A / m[0])},
     {0: ('2\u221a((P/4)\u00b2 - (d/2)\u00b2)',
          lambda m, P: 2 * sq((P / 4) ** 2 - (m[1] / 2) ** 2)),
      1: ('2\u221a((P/4)\u00b2 - (D/2)\u00b2)',
          lambda m, P: 2 * sq((P / 4) ** 2 - (m[0] / 2) ** 2))}),
    ('B b h', ('A = (B + b) / 2 ' + X + ' h', '({0} + {1}) / 2 ' + X + ' {2}',
               lambda m: (m[0] + m[1]) / 2 * m[2]), None,
     {0: ('2 ' + X + ' A / h - b', lambda m, A: 2 * A / m[2] - m[1]),
      1: ('2 ' + X + ' A / h - B', lambda m, A: 2 * A / m[2] - m[0]),
      2: ('2 ' + X + ' A / (B + b)', lambda m, A: 2 * A / (m[0] + m[1]))}, {}),
    ('n l ap', ('A = P / 2 ' + X + ' ap = n ' + X + ' l ' + X + ' ap / 2',
                '{0} ' + X + ' {1} ' + X + ' {2} / 2',
                lambda m: m[0] * m[1] * m[2] / 2),
     ('P = n ' + X + ' l', '{0} ' + X + ' {1}', lambda m: m[0] * m[1]),
     {0: ('2 ' + X + ' A / (l ' + X + ' ap)', lambda m, A: 2 * A / m[1] / m[2]),
      1: ('2 ' + X + ' A / (n ' + X + ' ap)', lambda m, A: 2 * A / m[0] / m[2]),
      2: ('2 ' + X + ' A / (n ' + X + ' l)', lambda m, A: 2 * A / m[0] / m[1])},
     {0: ('P / l', lambda m, P: P / m[1]), 1: ('P / n', lambda m, P: P / m[0])}),
    ('r', ('A = \u03c0 ' + X + ' r\u00b2', '\u03c0 ' + X + ' {0}\u00b2',
           lambda m: PI * m[0] ** 2),
     ('P = 2 ' + X + ' \u03c0 ' + X + ' r', '2 ' + X + ' \u03c0 ' + X + ' {0}',
      lambda m: 2 * PI * m[0]),
     {0: ('\u221a(A / \u03c0)', lambda m, A: sq(A / PI))},
     {0: ('P / (2\u03c0)', lambda m, P: P / 2 / PI)}),
    ('r \u03b1', ('A = \u03b1/360 ' + X + ' \u03c0 ' + X + ' r\u00b2',
                  '{1}/360 ' + X + ' \u03c0 ' + X + ' {0}\u00b2',
                  lambda m: m[1] / 360 * PI * m[0] ** 2),
     ('P = 2r + \u03b1/360 ' + X + ' 2\u03c0r', '2 ' + X + ' {0} + {1}/360 ' +
      X + ' 2\u03c0 ' + X + ' {0}', lambda m: 2 * m[0] + m[1] / 180 * PI * m[0]),
     {0: ('\u221a(360A / (\u03b1\u03c0))',
          lambda m, A: sq(360 * A / m[1] / PI)),
      1: ('360A / (\u03c0r\u00b2)', lambda m, A: 360 * A / PI / m[0] ** 2)},
     {0: ('P / (2 + \u03b1\u03c0/180)',
          lambda m, P: P / (2 + m[1] * PI / 180)),
      1: ('(P - 2r) ' + X + ' 180 / (\u03c0r)',
          lambda m, P: (P - 2 * m[0]) * 180 / PI / m[0])}),
    ('R r', ('A = \u03c0R\u00b2 - \u03c0r\u00b2', '\u03c0 ' + X + ' {0}\u00b2 - '
             '\u03c0 ' + X + ' {1}\u00b2', lambda m: PI * (m[0] ** 2 - m[1] ** 2)),
     ('P = 2\u03c0R + 2\u03c0r', '2\u03c0 ' + X + ' {0} + 2\u03c0 ' + X + ' {1}',
      lambda m: 2 * PI * (m[0] + m[1])),
     {0: ('\u221a(A/\u03c0 + r\u00b2)', lambda m, A: sq(A / PI + m[1] ** 2)),
      1: ('\u221a(R\u00b2 - A/\u03c0)', lambda m, A: sq(m[0] ** 2 - A / PI))},
     {0: ('P / (2\u03c0) - r', lambda m, P: P / 2 / PI - m[1]),
      1: ('P / (2\u03c0) - R', lambda m, P: P / 2 / PI - m[0])}))


def area():
    return ('\u00c1reas e per\u00edmetros',
            [N.fld('Figura', '', '', 'c', FIG),
             N.fld('1.\u00aa medida', '', '5', 'o'),
             N.fld('2.\u00aa medida', '', '', 'o'),
             N.fld('3.\u00aa medida', '', '', 'o'),
             N.fld('\u00c1rea conhecida (opcional)', '', '', 'o'),
             N.fld('Per\u00edmetro conhecido (opcional)', '', '', 'o'),
             N.fld('Unidade de comprimento', '', '', 'c', UN)], _area)


def _area(v):
    k = v[0]
    u = UN[v[6]]
    nms = FA[k][0].split()
    fa, fp, ia, ip = FA[k][1:]
    Ak = None if v[4] is None else N.pos(v[4][0], 'A \u00e1rea')
    Pk = None if v[5] is None else N.pos(v[5][0], 'O per\u00edmetro')
    m, i = lermed(v[1:4], nms, (Ak, Pk), 2 if k == 6 else -1)
    o = []
    if k == 6 and i == 2 and Ak is None and Pk is None:
        n = m[0]
        N.need(eq(n, round(n)) and n >= 3, 'O n\u00famero de lados n tem de ser '
               'um inteiro maior ou igual a 3')
        m[2] = m[1] / 2 / math.tan(PI / n)
        o.append('ap = l / (2 tan(180\u00b0/n)) ' + N.rhs(m[2], 2) +
                 ' (trigonometria, 9.\u00ba ano)')
    elif i >= 0:
        if Ak is not None:
            o.append('= ' + fa[0])
            resolve(m, i, nms, Ak, 'a \u00e1rea', fa[1], ia, o)
        else:
            N.need(fp is not None, 'Esta figura n\u00e3o tem f\u00f3rmula do per\u00edmetro'
                   ' s\u00f3 com estas medidas; usa a \u00e1rea')
            o.append('= ' + fp[0])
            resolve(m, i, nms, Pk, 'o per\u00edmetro', fp[1], ip, o)
        o.append('> ' + nms[i] + ' ' + N.rhs(m[i], 2) + {'n': '', '\u03b1': G}
                 .get(nms[i], ' ' + ue(u, 1)))
    if k == 6:
        N.need(eq(m[0], round(m[0])) and m[0] >= 3, 'O n\u00famero de lados n '
               'tem de ser um inteiro maior ou igual a 3')
    if k == 8:
        N.need(m[1] <= 360 or eq(m[1], 360), 'A amplitude do setor \u00e9 no '
               'm\u00e1ximo 360\u00b0')
    if k == 9:
        N.need(m[0] > m[1], 'O raio exterior R tem de ser maior do que r')
    o.append(FIG[k].split(' (')[0] + ': ' + ', '.join(
        [nms[j] + ' = ' + nv(m[j]) + (G if j == 1 and k == 8 else '')
         for j in range(len(nms))]))
    A = fa[2](m)
    if i < 0 or Ak is None:
        o += ['= ' + fa[0], 'A = ' + subst(fa[1], m, nms),
              '> A ' + N.rhs(A, 2) + ' ' + ue(u, 2)]
    if fp is not None:
        P = fp[2](m)
        if i < 0 or Pk is None:
            o += ['= ' + fp[0], 'P = ' + subst(fp[1], m, nms),
                  '> P ' + N.rhs(P, 2) + ' ' + ue(u, 1)]
    else:
        o.append('Per\u00edmetro: s\u00e3o precisos os comprimentos de todos os lados.')
    if k == 0:
        o.append('Diagonal: l\u221a2 ' + N.rhs(m[0] * sq(2), 2))
    elif k == 1:
        o.append('Diagonal (Pit\u00e1goras): \u221a(c\u00b2 + l\u00b2) ' +
                 N.rhs(sq(m[0] ** 2 + m[1] ** 2), 2))
    elif k == 7:
        o.append('Di\u00e2metro: 2r = ' + nv(2 * m[0]))
    elif k == 8:
        o.append('Arco: \u03b1/360 ' + X + ' 2\u03c0r ' +
                 N.rhs(m[1] / 180 * PI * m[0], 2))
    st = '\u00c1reas em unidades quadradas (cm\u00b2, m\u00b2...); per\u00edmetros ' \
        'em unidades de comprimento.\nPara descobrir uma medida: escreve a ' \
        '\u00e1rea ou o per\u00edmetro e deixa essa medida vazia.'
    return ('\n'.join(o), st, A, ue(u, 2))
