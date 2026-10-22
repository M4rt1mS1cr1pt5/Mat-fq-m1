# c_mate.py - M1TR4M: calculadoras de estatistica: dados univariados
# (media, moda, mediana, quartis pelo metodo das metades, percentis,
# amplitude, AIQ, variancia e desvio padrao amostrais, outliers, efeito de
# y = a x + b e diagrama de extremos e quartis), dados agrupados em
# classes (tabela de frequencias e histograma) e caule-e-folhas.
#@ c_mate.uni|Estat\u00edstica de uma vari\u00e1vel|m\u00e9dia moda mediana quartis percentil amplitude interquartil vari\u00e2ncia desvio padr\u00e3o outliers diagrama de extremos e quartis transforma\u00e7\u00e3o linear frequ\u00eancias|M|m2
#@ c_mate.cls|Dados em classes e histograma|classes histograma tabela de frequ\u00eancias absoluta relativa acumulada ponto m\u00e9dio classe modal classe mediana|M|m2
#@ c_mate.caule|Caule-e-folhas|caule e folhas diagrama ordenar dados comparar dois conjuntos|M|m2
# Casos-limite: menos de 2 dados, frequencias nao inteiras, todos os dados
# iguais (AIQ e s nulos), dados fora das classes, folhas com mais de um
# algarismo, valores negativos no caule-e-folhas.

import math
import m1_nucleo as N

MS = '\u00b7'


def nums(t, nm):
    out = []
    for p in N.lst(t):
        out.append(N.num(p)[0])
    N.need(out, 'Escreve ' + nm + ' separados por espa\u00e7os')
    return out


def lista(xs):
    return ' '.join([N.fmt(x) for x in xs])


def med(xs):
    # Mediana de uma lista ordenada.
    n = len(xs)
    h = n // 2
    return xs[h] if n % 2 else (xs[h - 1] + xs[h]) / 2


def quartis(xs):
    # Metodo das metades: Q1 e Q3 sao as medianas da metade de baixo e da
    # de cima; com n impar, a mediana fica de fora das metades.
    n = len(xs)
    h = n // 2
    return med(xs[:h]), med(xs[n - h:])


def percentil(xs, k):
    # Pk: calcula-se k% de n; se nao for inteiro, e o dado da posicao
    # seguinte; se for inteiro, e a media desse dado e do seguinte.
    n = len(xs)
    p = k * n / 100
    i = int(p + 1e-9)
    if abs(p - i) < 1e-9:
        return (xs[i - 1] + xs[min(i, n - 1)]) / 2 if i > 0 else xs[0], p
    return xs[i], p


def modas(xs):
    vs = []
    fs = []
    for x in xs:
        if vs and vs[-1] == x:
            fs[-1] += 1
        else:
            vs.append(x)
            fs.append(1)
    m = max(fs)
    if len(vs) > 1 and min(fs) == m:
        return [], m
    return [vs[i] for i in range(len(vs)) if fs[i] == m], m

# ------------------------------------------------------------ univariada


def uni():
    return ('Estat\u00edstica de uma vari\u00e1vel',
            [N.fld('Dados (ou valores, se h\u00e1 frequ\u00eancias)', '',
                   '2 4 4 5 7 8 9 9 9 25', 'l'),
             N.fld('Frequ\u00eancias absolutas (opcional)', '', '', 't'),
             N.fld('Percentil k (opcional, 0 < k < 100)', '', '', 'o'),
             N.fld('Transforma\u00e7\u00e3o y = a x + b: a (opcional)', '', '', 'o'),
             N.fld('b (opcional)', '', '', 'o')], _uni)


def _uni(v):
    xs = [p[0] for p in v[0]]
    if v[1]:
        fs = nums(v[1], 'as frequ\u00eancias')
        N.need(len(fs) == len(xs), 'H\u00e1 ' + str(len(xs)) + ' valores e ' +
               str(len(fs)) + ' frequ\u00eancias')
        ys = []
        for i in range(len(xs)):
            N.need(fs[i] >= 0 and fs[i] == int(fs[i]), 'As frequ\u00eancias t\u00eam '
                   'de ser inteiros n\u00e3o negativos')
            ys += [xs[i]] * int(fs[i])
            N.need(len(ys) <= 2000, 'No m\u00e1ximo 2000 dados')
        xs = ys
    xs.sort()
    n = len(xs)
    N.need(n >= 2, 'S\u00e3o precisos pelo menos 2 dados')
    m = sum(xs) / n
    s2 = sum([(x - m) ** 2 for x in xs]) / (n - 1)
    s = math.sqrt(s2)
    me = med(xs)
    q1, q3 = quartis(xs)
    aiq = q3 - q1
    mo, fm = modas(xs)
    o = ['n = ' + str(n) + (': ' + lista(xs) if n <= 30 else
                            ' (ordenados: ' + lista(xs[:5]) + ' ...)')]
    o += ['= M\u00e9dia = soma / n = ' + N.fmt(sum(xs)) + ' / ' + str(n),
          '> M\u00e9dia ' + N.eq(m),
          'Moda: ' + ('n\u00e3o h\u00e1 (todos os valores com a mesma frequ\u00eancia)'
                      if not mo else lista(mo[:4]) + (' ...' if len(mo) > 4 else '') +
                      ' (frequ\u00eancia ' + str(fm) + ')'),
          '> Mediana ' + N.eq(me),
          '> Q1 ' + N.eq(q1) + ' ' + MS + ' Q3 ' + N.eq(q3) + ' (medianas das metades' +
          (', sem a mediana)' if n % 2 else ')'),
          'M\u00ednimo ' + N.fmt(xs[0]) + ' ' + MS + ' m\u00e1ximo ' + N.fmt(xs[-1]) +
          ' ' + MS + ' amplitude ' + N.fmt(xs[-1] - xs[0]),
          '> AIQ = Q3 - Q1 ' + N.eq(aiq),
          '= s\u00b2 = soma dos (x - m\u00e9dia)\u00b2 / (n - 1)',
          '> Vari\u00e2ncia ' + N.eq(s2) + ' ' + MS + ' desvio padr\u00e3o s ' + N.eq(s)]
    lo, hi = q1 - 1.5 * aiq, q3 + 1.5 * aiq
    out = [x for x in xs if x < lo or x > hi]
    o.append('Barreiras: Q1 - 1,5 AIQ = ' + N.fmt(lo) + ' e Q3 + 1,5 AIQ = ' +
             N.fmt(hi))
    o.append(('Outliers: ' + lista(out[:8]) + (' ...' if len(out) > 8 else ''))
             if out else 'Sem outliers.')
    if out:
        ok = [x for x in xs if lo <= x <= hi]
        m2 = sum(ok) / len(ok)
        o.append('Sem os outliers: m\u00e9dia ' + N.eq(m2) + ', mediana ' +
                 N.eq(med(ok)) + ' (a mediana \u00e9 mais resistente).')
    if v[2] is not None:
        k = v[2][0]
        N.need(0 < k < 100, 'O percentil k tem de estar entre 0 e 100')
        pk, p = percentil(xs, k)
        o.append('P' + N.fmt(k) + ': ' + N.fmt(k) + '% de ' + str(n) + ' = ' +
                 N.fmt(p) + (' (inteiro: m\u00e9dia de 2 dados)' if abs(p - round(p))
                             < 1e-9 else ' (posi\u00e7\u00e3o seguinte)') + '; P' +
                 N.fmt(k) + ' ' + N.eq(pk))
        if k in (25, 75) and abs(pk - (q1 if k == 25 else q3)) > 1e-12:
            o.append('(Aqui P' + N.fmt(k) + ' \u2260 Q' + ('1' if k == 25 else '3') +
                     ': as duas regras podem dar valores diferentes.)')
    if v[3] is not None or v[4] is not None:
        a = v[3][0] if v[3] is not None else 1.0
        b = v[4][0] if v[4] is not None else 0.0
        o += ['Com y = ' + N.fmt(a) + 'x + ' + N.fmt(b) + ':',
              ' m\u00e9dia ' + N.eq(a * m + b) + '; mediana ' + N.eq(a * me + b),
              ' s ' + N.eq(abs(a) * s) + '; AIQ ' + N.eq(abs(a) * aiq) +
              ' (o b n\u00e3o muda a dispers\u00e3o)']
    wl = min([x for x in xs if x >= lo])
    wh = max([x for x in xs if x <= hi])
    d = (xs[-1] - xs[0]) * 0.1 or 1.0
    sg = [(q1, 0.7, q3, 0.7), (q1, 1.3, q3, 1.3), (q1, 0.7, q1, 1.3),
          (q3, 0.7, q3, 1.3), (me, 0.7, me, 1.3), (wl, 1, q1, 1), (q3, 1, wh, 1),
          (wl, 0.85, wl, 1.15), (wh, 0.85, wh, 1.15)]
    its = [('s', sg, 2)]
    if out:
        its.append(('p', [(x, 1) for x in out], 5))
    gr = ('Diagrama de extremos e quartis', its, xs[0] - d, xs[-1] + d, 0, 2,
          'Q1 ' + N.fmt(q1) + ' ' + MS + ' Me ' + N.fmt(me) + ' ' + MS + ' Q3 ' +
          N.fmt(q3) + (' ' + MS + ' pontos: outliers' if out else ''))
    st = 'Mediana: valor do meio dos dados ordenados (m\u00e9dia dos dois do ' \
        'meio, se n for par).\nQ1 e Q3: medianas das metades de baixo e de ' \
        'cima.\nPk: k% de n; n\u00e3o inteiro: posi\u00e7\u00e3o seguinte; inteiro: ' \
        'm\u00e9dia desse dado e do seguinte.\nOutliers: abaixo de Q1 - 1,5 AIQ ou ' \
        'acima de Q3 + 1,5 AIQ (confirma a regra do teu manual).\nDesvio ' \
        'padr\u00e3o amostral: divide-se por n - 1.'
    return ('\n'.join(o), st, m, '', gr)

# ------------------------------------------------------------ classes


def cls():
    return ('Dados em classes e histograma',
            [N.fld('Limites das classes', '', '0 10 20 30 40', 'l'),
             N.fld('Frequ\u00eancias das classes (ou vazio)', '', '3 7 8 2', 't'),
             N.fld('Dados brutos (se n\u00e3o h\u00e1 frequ\u00eancias)', '', '', 't')],
            _cls)


def _cls(v):
    L = [p[0] for p in v[0]]
    k = len(L) - 1
    N.need(k >= 1, 'Escreve pelo menos 2 limites (ex.: 0 10 20)')
    for i in range(k):
        N.need(L[i + 1] > L[i], 'Os limites t\u00eam de estar por ordem crescente')
    if v[1]:
        N.need(not v[2], 'Escreve as frequ\u00eancias ou os dados brutos, n\u00e3o os '
               'dois')
        fs = nums(v[1], 'as frequ\u00eancias')
        N.need(len(fs) == k, 'H\u00e1 ' + str(k) + ' classes e ' + str(len(fs)) +
               ' frequ\u00eancias')
        for f in fs:
            N.need(f >= 0 and f == int(f), 'As frequ\u00eancias t\u00eam de ser '
                   'inteiros n\u00e3o negativos')
    else:
        N.need(v[2], 'Escreve as frequ\u00eancias ou os dados brutos')
        xs = nums(v[2], 'os dados')
        fs = [0] * k
        for x in xs:
            N.need(L[0] <= x <= L[-1], 'O dado ' + N.fmt(x) + ' est\u00e1 fora das '
                   'classes')
            i = 0
            while i < k - 1 and x >= L[i + 1]:
                i += 1
            fs[i] += 1
    n = sum(fs)
    N.need(n > 0, 'N\u00e3o h\u00e1 dados')
    hs = [L[i + 1] - L[i] for i in range(k)]
    iguais = max(hs) - min(hs) < 1e-9 * max(hs)
    pm = [(L[i] + L[i + 1]) / 2 for i in range(k)]
    o = ['Classe: ponto m\u00e9dio; ni; fi; Ni; Fi']
    F = 0
    for i in range(k):
        F += fs[i]
        o.append(('[' + N.fmt(L[i]) + ', ' + N.fmt(L[i + 1]) +
                  (']' if i == k - 1 else '[')) + ': ' + N.fmt(pm[i]) + '; ' +
                 str(int(fs[i])) + '; ' + N.fmt(100 * fs[i] / n, 0, 1) + '%; ' +
                 str(int(F)) + '; ' + N.fmt(100 * F / n, 0, 1) + '%')
    m = sum([pm[i] * fs[i] for i in range(k)]) / n
    o += ['n = ' + str(int(n)),
          '> M\u00e9dia (com os pontos m\u00e9dios) ' + N.eq(m)]
    if n > 1:
        s = math.sqrt(sum([fs[i] * (pm[i] - m) ** 2 for i in range(k)]) / (n - 1))
        o.append('> Desvio padr\u00e3o (aproximado) ' + N.eq(s))
    dens = [fs[i] / hs[i] for i in range(k)]
    dm = max(dens)
    o.append('Classe modal: ' + ', '.join(['[' + N.fmt(L[i]) + ', ' +
                                           N.fmt(L[i + 1]) + '[' for i in range(k)
                                           if dens[i] == dm]))
    F = 0
    for i in range(k):
        F += fs[i]
        if 2 * F == n and i < k - 1:
            o.append('A frequ\u00eancia acumulada \u00e9 50% no fim de [' +
                     N.fmt(L[i]) + ', ' + N.fmt(L[i + 1]) + '[: a mediana fica '
                     'no limite ' + N.fmt(L[i + 1]) + '.')
            break
        if 2 * F > n:
            o.append('Classe mediana: [' + N.fmt(L[i]) + ', ' + N.fmt(L[i + 1]) +
                     ('[' if i < k - 1 else ']') + ' (a frequ\u00eancia acumulada '
                     'passa os 50%)')
            break
    if not iguais:
        o.append('Classes com amplitudes diferentes: no histograma, a altura '
                 '\u00e9 ni / amplitude.')
    ys = fs if iguais else dens
    sg = []
    for i in range(k):
        sg += [(L[i], 0, L[i], ys[i]), (L[i], ys[i], L[i + 1], ys[i]),
               (L[i + 1], ys[i], L[i + 1], 0)]
    d = (L[-1] - L[0]) * 0.08
    rs = [(L[i], ys[i], str(int(fs[i]))) for i in range(k)]
    gr = ('Histograma', [('s', sg, 4), ('t', rs, 0)], L[0] - d, L[-1] + d, 0,
          max(ys) * 1.25, ('limites ' + ' '.join([N.fmt(x) for x in L]) + '; ' +
                           'n\u00fameros: ni' + ('' if iguais else
                                                ' (altura: ni / amplitude)')))
    st = 'ni: frequ\u00eancia absoluta; fi = ni / n; Ni e Fi: acumuladas.\n' \
        'Classes [a, b[: o limite de cima fica na classe seguinte (a \u00faltima ' \
        '\u00e9 fechada).\nM\u00e9dia de dados agrupados: usa os pontos m\u00e9dios ' \
        '(\u00e9 um valor aproximado).'
    return ('\n'.join(o), st, m, '', gr)

# ------------------------------------------------------------ caule


def cauleset(t, dec, nm):
    xs = nums(t, nm)
    out = []
    for x in xs:
        N.need(x >= 0, 'O caule-e-folhas desta calculadora s\u00f3 aceita valores '
               'n\u00e3o negativos')
        y = x * 10 if dec else x
        N.need(abs(y - round(y)) < 1e-9, 'Os dados t\u00eam de ter ' + (
            'no m\u00e1ximo uma casa decimal' if dec else 'ser inteiros (usa as '
            'd\u00e9cimas como folhas)'))
        y = int(round(y))
        out.append((y // 10, y % 10))
    out.sort()
    return xs, out


def caule():
    return ('Caule-e-folhas',
            [N.fld('Dados A', '', '12 15 21 23 23 30 38 41', 't'),
             N.fld('Dados B (opcional, diagrama duplo)', '', '', 't'),
             N.fld('Folhas', '', '', 'c', ['unidades (caule: dezenas)',
                                           'd\u00e9cimas (caule: unidades)'])],
            _caule)


def _caule(v):
    ta, tb, dec = v
    xa, a = cauleset(ta, dec, 'os dados A')
    xb, b = cauleset(tb, dec, 'os dados B') if tb else ([], [])
    cs = [c for c, f in a + b]
    lo, hi = min(cs), max(cs)
    N.need(hi - lo <= 40, 'Demasiados caules: usa outra unidade para as folhas')
    o = []
    if b:
        rows = []
        for c in range(lo, hi + 1):
            fa = [str(f) for cc, f in a if cc == c]
            fa.reverse()
            rows.append((' '.join(fa), str(c), ' '.join([str(f) for cc, f in b
                                                          if cc == c])))
        w = max([len(r[0]) for r in rows])
        wc = max([len(r[1]) for r in rows])
        for r in rows:
            o.append(' ' * (w - len(r[0])) + r[0] + ' | ' + ' ' * (wc - len(r[1])) +
                     r[1] + ' | ' + r[2])
        o.append('Folhas de A \u00e0 esquerda, de B \u00e0 direita.')
    else:
        wc = len(str(hi))
        for c in range(lo, hi + 1):
            s = str(c)
            o.append(' ' * (wc - len(s)) + s + ' | ' + ' '.join(
                [str(f) for cc, f in a if cc == c]))
    c0, f0 = (a + b)[0]
    o.append('Legenda: ' + str(c0) + ' | ' + str(f0) + ' = ' +
             (str(c0) + ',' + str(f0) if dec else str(c0 * 10 + f0)))
    for nm, xs in (('A', xa), ('B', xb)):
        if xs:
            ys = sorted(xs)
            o.append(nm + ': n = ' + str(len(ys)) + ', m\u00ednimo ' + N.fmt(ys[0]) +
                     ', mediana ' + N.fmt(med(ys)) + ', m\u00e1ximo ' + N.fmt(ys[-1]))
    st = 'Caule: os algarismos da esquerda; folha: o \u00faltimo algarismo.\n' \
        'As folhas escrevem-se por ordem crescente a partir do caule.\nO ' \
        'diagrama mostra a forma da distribui\u00e7\u00e3o sem perder os dados.'
    return ('\n'.join(o), st, None, '')
