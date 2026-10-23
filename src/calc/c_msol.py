# c_msol.py - M1TR4M: areas e volumes de solidos (cubo, paralelepipedo,
# prisma, cilindro, piramide, piramide regular, cone e esfera), com a
# medida em falta calculada a partir do volume ou da area total e a
# capacidade em litros.
#@ c_msol.sol|S\u00f3lidos: \u00e1reas e volumes|volume \u00e1rea lateral \u00e1rea total cubo paralelep\u00edpedo prisma cilindro pir\u00e2mide cone esfera geratriz ap\u00f3tema capacidade litros|M|g9
# Casos-limite: medidas a mais ou em falta, dados incompativeis (medida
# calculada nao positiva), piramide regular com n nao inteiro, cone sem
# inversa pela area total.

import math
import m1_nucleo as N

G = '\u00b0'
X = N.X
sq = math.sqrt
PI = math.pi
UN = ['u.c.', 'cm', 'm', 'mm', 'dm', 'km']


def nv(x):
    # Medida escrita: decimal quando e exato, senao forma exata.
    s, ex = N.fmt2(x, 0, -1)
    if ex:
        return s
    e = N.exact(x)
    return e if e is not None else s


def eq(a, b):
    return abs(a - b) < 1e-9 * max(1.0, abs(a), abs(b))


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
        N.need(v[i] is None, 'Este s\u00f3lido s\u00f3 usa ' + str(k) + ' medida' +
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


SOL = ['Cubo (aresta a)', 'Paralelep\u00edpedo (c, l, h)',
       'Prisma reto (Ab, Pb, h)', 'Cilindro (r, h)', 'Pir\u00e2mide (Ab, h)',
       'Pir\u00e2mide regular (n, l, h)', 'Cone (r, h)', 'Esfera (raio r)']
# Por solido: medidas; volume (formula, modelo, funcao); area total
# (idem, ou None); inversas pelo volume e pela area total.
FS = (
    ('a', ('V = a\u00b3', '{0}\u00b3', lambda m: m[0] ** 3),
     ('At = 6 ' + X + ' a\u00b2', '6 ' + X + ' {0}\u00b2',
      lambda m: 6 * m[0] ** 2),
     {0: ('\u221bV', lambda m, V: V ** (1 / 3))},
     {0: ('\u221a(At / 6)', lambda m, A: sq(A / 6))}),
    ('c l h', ('V = c ' + X + ' l ' + X + ' h', '{0} ' + X + ' {1} ' + X +
               ' {2}', lambda m: m[0] * m[1] * m[2]),
     ('At = 2 ' + X + ' (cl + ch + lh)', '2 ' + X + ' ({0} ' + X + ' {1} + '
      '{0} ' + X + ' {2} + {1} ' + X + ' {2})',
      lambda m: 2 * (m[0] * m[1] + m[0] * m[2] + m[1] * m[2])),
     {0: ('V / (l ' + X + ' h)', lambda m, V: V / m[1] / m[2]),
      1: ('V / (c ' + X + ' h)', lambda m, V: V / m[0] / m[2]),
      2: ('V / (c ' + X + ' l)', lambda m, V: V / m[0] / m[1])},
     {2: ('(At/2 - cl) / (c + l)',
          lambda m, A: (A / 2 - m[0] * m[1]) / (m[0] + m[1]))}),
    ('Ab Pb h', ('V = Ab ' + X + ' h', '{0} ' + X + ' {2}',
                 lambda m: m[0] * m[2]),
     ('At = Pb ' + X + ' h + 2 ' + X + ' Ab', '{1} ' + X + ' {2} + 2 ' + X +
      ' {0}', lambda m: m[1] * m[2] + 2 * m[0]),
     {0: ('V / h', lambda m, V: V / m[2]), 2: ('V / Ab', lambda m, V: V / m[0])},
     {2: ('(At - 2Ab) / Pb', lambda m, A: (A - 2 * m[0]) / m[1])}),
    ('r h', ('V = \u03c0 ' + X + ' r\u00b2 ' + X + ' h', '\u03c0 ' + X +
             ' {0}\u00b2 ' + X + ' {1}', lambda m: PI * m[0] ** 2 * m[1]),
     ('At = 2\u03c0r\u00b2 + 2\u03c0rh', '2\u03c0 ' + X + ' {0}\u00b2 + 2\u03c0 ' +
      X + ' {0} ' + X + ' {1}', lambda m: 2 * PI * m[0] * (m[0] + m[1])),
     {0: ('\u221a(V / (\u03c0h))', lambda m, V: sq(V / PI / m[1])),
      1: ('V / (\u03c0r\u00b2)', lambda m, V: V / PI / m[0] ** 2)},
     {1: ('(At - 2\u03c0r\u00b2) / (2\u03c0r)',
          lambda m, A: (A - 2 * PI * m[0] ** 2) / (2 * PI * m[0]))}),
    ('Ab h', ('V = Ab ' + X + ' h / 3', '{0} ' + X + ' {1} / 3',
              lambda m: m[0] * m[1] / 3), None,
     {0: ('3V / h', lambda m, V: 3 * V / m[1]),
      1: ('3V / Ab', lambda m, V: 3 * V / m[0])}, {}),
    ('n l h', None, None, {}, {}),
    ('r h', ('V = \u03c0 ' + X + ' r\u00b2 ' + X + ' h / 3', '\u03c0 ' + X +
             ' {0}\u00b2 ' + X + ' {1} / 3', lambda m: PI * m[0] ** 2 * m[1] / 3),
     ('At = \u03c0r\u00b2 + \u03c0rg', None,
      lambda m: PI * m[0] * (m[0] + sq(m[0] ** 2 + m[1] ** 2))),
     {0: ('\u221a(3V / (\u03c0h))', lambda m, V: sq(3 * V / PI / m[1])),
      1: ('3V / (\u03c0r\u00b2)', lambda m, V: 3 * V / PI / m[0] ** 2)}, {}),
    ('r', ('V = 4/3 ' + X + ' \u03c0 ' + X + ' r\u00b3', '4/3 ' + X + ' \u03c0 '
           + X + ' {0}\u00b3', lambda m: 4 * PI * m[0] ** 3 / 3),
     ('A = 4\u03c0r\u00b2', '4\u03c0 ' + X + ' {0}\u00b2',
      lambda m: 4 * PI * m[0] ** 2),
     {0: ('\u221b(3V / (4\u03c0))', lambda m, V: (3 * V / 4 / PI) ** (1 / 3))},
     {0: ('\u221a(A / (4\u03c0))', lambda m, A: sq(A / 4 / PI))}))


def sol():
    return ('S\u00f3lidos: \u00e1reas e volumes',
            [N.fld('S\u00f3lido', '', '', 'c', SOL),
             N.fld('1.\u00aa medida', '', '3', 'o'),
             N.fld('2.\u00aa medida', '', '', 'o'),
             N.fld('3.\u00aa medida', '', '', 'o'),
             N.fld('Volume conhecido (opcional)', '', '', 'o'),
             N.fld('\u00c1rea total conhecida (opcional)', '', '', 'o'),
             N.fld('Unidade de comprimento', '', '', 'c', UN)], _sol)


def _sol(v):
    k = v[0]
    u = UN[v[6]]
    nms = FS[k][0].split()
    fv, fa, iv, ia = FS[k][1:]
    Vk = None if v[4] is None else N.pos(v[4][0], 'O volume')
    Ak = None if v[5] is None else N.pos(v[5][0], 'A \u00e1rea')
    m, i = lermed(v[1:4], nms, (Vk, Ak))
    if k == 5:
        N.need(i < 0, 'Na pir\u00e2mide regular escreve as tr\u00eas medidas (n, l, h)')
        return piramide(m, u)
    o = []
    if i >= 0:
        if Vk is not None:
            o.append('= ' + fv[0])
            resolve(m, i, nms, Vk, 'o volume', fv[1], iv, o)
        else:
            N.need(ia, 'Com a \u00e1rea total n\u00e3o sei calcular esta medida; usa '
                   'o volume')
            o.append('= ' + fa[0])
            resolve(m, i, nms, Ak, 'a \u00e1rea', fa[1] or fa[0], ia, o)
        o.append('> ' + nms[i] + ' ' + N.rhs(m[i], 2) + ' ' +
                 ue(u, 2 if nms[i] == 'Ab' else 1))
    o.append(SOL[k].split(' (')[0] + ': ' + ', '.join(
        [nms[j] + ' = ' + nv(m[j]) for j in range(len(nms))]))
    V = fv[2](m)
    if i < 0 or Vk is None:
        o += ['= ' + fv[0], 'V = ' + subst(fv[1], m, nms),
              '> V ' + N.rhs(V, 2) + ' ' + ue(u, 3)]
    if k == 6:
        g = sq(m[0] ** 2 + m[1] ** 2)
        o += ['Geratriz (Pit\u00e1goras): g = \u221a(r\u00b2 + h\u00b2) ' +
              N.rhs(g, 2), 'Al = \u03c0rg ' + N.rhs(PI * m[0] * g, 2) + ' ' +
              ue(u, 2)]
    elif k == 3:
        o.append('Al = 2\u03c0rh ' + N.rhs(2 * PI * m[0] * m[1], 2) + ' ' +
                 ue(u, 2))
    elif k == 2:
        o.append('Al = Pb ' + X + ' h ' + N.rhs(m[1] * m[2], 2) + ' ' +
                 ue(u, 2))
    elif k == 0:
        o.append('Diagonal espacial: a\u221a3 ' + N.rhs(m[0] * sq(3), 2))
    elif k == 1:
        o.append('Diagonal espacial: \u221a(c\u00b2 + l\u00b2 + h\u00b2) ' +
                 N.rhs(sq(m[0] ** 2 + m[1] ** 2 + m[2] ** 2), 2))
    if fa is None:
        o.append('\u00c1rea: \u00e9 preciso o ap\u00f3tema (usa a pir\u00e2mide regular).')
    elif i < 0 or Ak is None:
        A = fa[2](m)
        t = fa[0].split(' =')[0]
        o += ['= ' + fa[0]] + ([t + ' = ' + subst(fa[1], m, nms)] if fa[1]
                               else []) + \
            ['> ' + t + ' ' + N.rhs(A, 2) + ' ' + ue(u, 2)]
    litros(V, u, o)
    return ('\n'.join(o), ST_SOL, V, ue(u, 3))


ST_SOL = 'Prisma e cilindro: V = \u00e1rea da base ' + X + ' altura.\n' \
    'Pir\u00e2mide e cone: V = \u00e1rea da base ' + X + ' altura / 3.\n' \
    'Esfera: V = 4/3 \u03c0r\u00b3; \u00e1rea 4\u03c0r\u00b2.'


def litros(V, u, o):
    f = {'mm': 1e-6, 'cm': 1e-3, 'dm': 1.0, 'm': 1e3, 'km': 1e12}.get(u)
    if f:
        o.append('Capacidade: 1 dm\u00b3 = 1 L, logo ' + N.fmt(V) + ' ' +
                 ue(u, 3) + ' = ' + N.fmt(V * f) + ' L')


def piramide(m, u):
    n, l, h = m
    N.need(eq(n, round(n)) and n >= 3, 'O n\u00famero de lados da base n tem de '
           'ser um inteiro maior ou igual a 3')
    n = int(round(n))
    a = l / 2 / math.tan(PI / n)
    Ab = n * l * a / 2
    ap = sq(h * h + a * a)
    Al = n * l * ap / 2
    V = Ab * h / 3
    o = ['Pir\u00e2mide regular: base com ' + str(n) + ' lados de ' + nv(l) +
         '; altura ' + nv(h) + '.',
         'Ap\u00f3tema da base: a = l / (2 tan(180\u00b0/n)) ' + N.rhs(a, 2) +
         (' (metade do lado)' if n == 4 else ''),
         'Ab = n ' + X + ' l ' + X + ' a / 2 ' + N.rhs(Ab, 2) + ' ' + ue(u, 2),
         '= V = Ab ' + X + ' h / 3', '> V ' + N.rhs(V, 2) + ' ' + ue(u, 3),
         'Ap\u00f3tema da pir\u00e2mide (Pit\u00e1goras): \u221a(h\u00b2 + a\u00b2) ' +
         N.rhs(ap, 2),
         'Al = n ' + X + ' l ' + X + ' ap / 2 ' + N.rhs(Al, 2) + ' ' + ue(u, 2),
         '> At = Ab + Al ' + N.rhs(Ab + Al, 2) + ' ' + ue(u, 2)]
    if n not in (3, 4, 6):
        o.append('(O ap\u00f3tema da base usa trigonometria: 9.\u00ba ano.)')
    litros(V, u, o)
    return ('\n'.join(o), ST_SOL, V, ue(u, 3))
