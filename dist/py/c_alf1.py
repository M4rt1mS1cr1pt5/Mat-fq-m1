# c_alf1.py - M1TR4M: assistentes das AL de Fisica 1.1 (plano
# inclinado), 1.2 (queda e ressalto de uma bola) e 2.1 (caracteristicas
# de uma pilha). Cada um faz a regressao linear e o grafico.
#@ c_alf1.plano|AL 1.1 Plano inclinado: Ec e dist\u00e2ncia|al 1.1 plano inclinado carrinho velocidade tempo de passagem c\u00e9lula fotoel\u00e9trica energia cin\u00e9tica regress\u00e3o for\u00e7a resultante|F|af
#@ c_alf1.ress|AL 1.2 Queda e ressalto de uma bola|al 1.2 queda ressalto bola altura energia dissipada coeficiente de restitui\u00e7\u00e3o regress\u00e3o|F|af
#@ c_alf1.pilha|AL 2.1 Caracter\u00edsticas de uma pilha|al 2.1 pilha for\u00e7a eletromotriz resist\u00eancia interna curva caracter\u00edstica u(i) regress\u00e3o re\u00f3stato|F|af
# Casos-limite: listas com tamanhos diferentes, menos de 3 pontos,
# tempos ou alturas nulos ou negativos, todos os x iguais (sem reta),
# declive com sinal inesperado (aviso), ressalto mais alto do que a queda.

import math
import m1_nucleo as N

X = N.X


def fit(xs, ys):
    # Reta dos minimos quadrados: (m, b, r); r e None se nao definido.
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum([(x - mx) ** 2 for x in xs])
    syy = sum([(y - my) ** 2 for y in ys])
    sxy = sum([(xs[i] - mx) * (ys[i] - my) for i in range(n)])
    N.need(max(xs) > min(xs), 'Todos os x s\u00e3o iguais: n\u00e3o h\u00e1 reta de '
           'regress\u00e3o')
    m = sxy / sxx
    return m, my - m * mx, (sxy / math.sqrt(sxx * syy) if syy > 0 else None)


def pares(a, b, na, nb):
    N.need(len(a) == len(b), 'H\u00e1 ' + str(len(a)) + ' valores de ' + na +
           ' e ' + str(len(b)) + ' de ' + nb + ': tem de haver o mesmo '
           'n\u00famero')
    N.need(len(a) >= 3, 'S\u00e3o precisos pelo menos 3 pontos')
    return [x[0] for x in a], [x[0] for x in b]


def reta(m, b, r, ux, uy):
    # Linhas da reta de regressao.
    o = ['= ' + uy + ' = m ' + ux + ' + b (m\u00ednimos quadrados)',
         'm = ' + N.fmt(m, 4) + '; b = ' + N.fmt(b, 4)]
    if r is not None:
        o.append('r = ' + N.fix(r, 4) + (' (bom ajuste)' if abs(r) >= 0.99
                                             else ' (pontos dispersos)'))
    return o


def gr(t, xs, ys, m, b, leg):
    x0, x1 = min(xs + [0.0]), max(xs)
    y0, y1 = min(ys + [0.0]), max(ys)
    dx = (x1 - x0) * 0.1 or 1.0
    dy = (y1 - y0) * 0.1 or 1.0
    return (t, [('p', list(zip(xs, ys)), 5), ('f', lambda x: m * x + b, 2)],
            x0 - dx, x1 + dx, y0 - dy, y1 + dy, leg)

# ------------------------------------------------------------ AL 1.1


def plano():
    return ('AL 1.1 Plano inclinado',
            [N.fld('Massa do carrinho m', 'g kg', ''),
             N.fld('Largura da tira L (cm)', '', '1,00'),
             N.fld('Dist\u00e2ncias percorridas d (m)', '', '', 'l'),
             N.fld('Tempos de passagem na c\u00e9lula (ms)', '', '', 'l')],
            _plano)


def _plano(v):
    m, L, ds, ts = v
    N.pos(m[0], 'A massa')
    N.pos(L[0], 'A largura da tira')
    xs, tt = pares(ds, ts, 'd', 'tempos')
    for x in xs + tt:
        N.pos(x, 'Cada dist\u00e2ncia e cada tempo')
    mk = m[0] / 1000
    vs = [L[0] / 100 / (t / 1000) for t in tt]
    ec = [0.5 * mk * x * x for x in vs]
    k, b, r = fit(xs, ec)
    o = ['v = L / \u0394t; Ec = \u00bd m v\u00b2']
    for i in range(len(xs)):
        o.append('d = ' + N.fmt(xs[i], ds[i][1]) + ' m: v = ' + N.fmt(vs[i], 3) +
                 ' m/s; Ec = ' + N.fmt(ec[i], 3) + ' J')
    o += reta(k, b, r, 'd', 'Ec')
    o.append('> Declive = F(resultante) ' + N.eq(k, 3) + ' N')
    if k <= 0:
        o.append('! Declive n\u00e3o positivo: a Ec devia aumentar com d.')
    st = 'O declive de Ec(d) \u00e9 a intensidade da resultante das for\u00e7as ' \
        '(teorema da energia cin\u00e9tica: \u0394Ec = F d).\nComo L \u00e9 pequena, ' \
        'L / \u0394t \u00e9 uma boa aproxima\u00e7\u00e3o da velocidade no ponto.'
    return ('\n'.join(o), st, k, 'N',
            gr('Ec (J) em fun\u00e7\u00e3o de d (m)', xs, ec, k, b,
               'pontos: medidos \u00b7 linha: regress\u00e3o'))

# ------------------------------------------------------------ AL 1.2


def ress():
    return ('AL 1.2 Queda e ressalto',
            [N.fld('Alturas de queda (cm)', '', '', 'l'),
             N.fld('Alturas do 1.\u00ba ressalto (cm)', '', '', 'l')], _ress)


def _ress(v):
    xs, ys = pares(v[0], v[1], 'quedas', 'ressaltos')
    for i in range(len(xs)):
        N.pos(xs[i], 'Cada altura de queda')
        N.pos(ys[i], 'Cada altura de ressalto')
        N.need(ys[i] <= xs[i], 'O ressalto n\u00e3o pode ser mais alto do que '
               'a queda')
    k, b, r = fit(xs, ys)
    o = reta(k, b, r, 'h(queda)', 'h(ressalto)')
    fr = sum([ys[i] / xs[i] for i in range(len(xs))]) / len(xs)
    o += ['> h(ressalto) / h(queda) \u2248 ' + N.fmt(k, 2) + ' (declive)',
          'Em cada ressalto fica a fra\u00e7\u00e3o ' + N.fmt(fr, 2) +
          ' da energia (m\u00e9dia de h(r) / h(q)).',
          '> Energia dissipada no ressalto \u2248 ' + N.fmt((1 - fr) * 100, 2) +
          ' %']
    st = 'Em cada ponto mais alto s\u00f3 h\u00e1 Epg: Em \u00e9 proporcional \u00e0 ' \
        'altura.\nA percentagem dissipada \u00e9 (1 - h(r) / h(q)) ' + X + \
        ' 100 %; depende da bola e do ch\u00e3o.'
    return ('\n'.join(o), st, (1 - fr) * 100, '%',
            gr('h(ressalto) em fun\u00e7\u00e3o de h(queda) (cm)', xs, ys, k, b,
               'pontos: medidos \u00b7 linha: regress\u00e3o'))

# ------------------------------------------------------------ AL 2.1


def pilha():
    return ('AL 2.1 Caracter\u00edsticas de uma pilha',
            [N.fld('Correntes I (mA)', '', '', 'l'),
             N.fld('Tens\u00f5es nos terminais U (V)', '', '', 'l')], _pilha)


def _pilha(v):
    xs, ys = pares(v[0], v[1], 'I', 'U')
    for x in xs:
        N.nneg(x, 'Cada corrente')
    ia = [x / 1000 for x in xs]
    k, b, r = fit(ia, ys)
    o = reta(k, b, r, 'I', 'U')
    o += ['U = \u03b5 - r I: ordenada na origem = \u03b5; declive = -r',
          '> \u03b5 ' + N.eq(b, 3) + ' V', '> r ' + N.eq(-k, 2) + ' \u03a9']
    if k >= 0:
        o.append('! Declive n\u00e3o negativo: confirma as medidas e as '
                 'liga\u00e7\u00f5es.')
    else:
        o.append('Corrente de curto-circuito (extrapola\u00e7\u00e3o): ' +
                 N.fmt(b / -k, 2) + ' A')
    st = 'Varia-se a resist\u00eancia exterior (re\u00f3stato) e mede-se I e ' \
        'U.\nO volt\u00edmetro em paralelo com a pilha; o amper\u00edmetro em ' \
        's\u00e9rie.'
    return ('\n'.join(o), st, b, 'V',
            gr('U (V) em fun\u00e7\u00e3o de I (A)', ia, ys, k, b,
               'pontos: medidos \u00b7 linha: regress\u00e3o'))
