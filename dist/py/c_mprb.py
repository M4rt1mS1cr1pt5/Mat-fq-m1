# c_mprb.py - M1TR4M: resolvedores de dados e probabilidades do 7.o ao
# 9.o ano: tabela de frequencias (absoluta, relativa, percentagem, angulo
# do grafico circular, moda, media, mediana, amplitude) com grafico de
# barras; lei de Laplace com casos por categorias; dois dados ou moedas
# (tabela de dupla entrada); duas extracoes com e sem reposicao (diagrama
# em arvore).
#@ c_mprb.freq|Tabela de frequ\u00eancias e gr\u00e1fico de barras|tabela de frequ\u00eancias absoluta relativa percentagem gr\u00e1fico de barras gr\u00e1fico circular \u00e2ngulo do setor moda m\u00e9dia mediana amplitude dados qualitativos quantitativos|M|d7
#@ c_mprb.prob|Probabilidade: lei de Laplace|probabilidade lei de laplace casos favor\u00e1veis poss\u00edveis acontecimento contr\u00e1rio certo imposs\u00edvel prov\u00e1vel saco bolas cartas|M|d9
#@ c_mprb.dados|Dois dados ou moedas (dupla entrada)|probabilidade dois dados soma produto diferen\u00e7a moedas tabela de dupla entrada experi\u00eancia composta face europeia nacional|M|d9
#@ c_mprb.urna|Duas extra\u00e7\u00f5es com e sem reposi\u00e7\u00e3o (\u00e1rvore)|probabilidade extra\u00e7\u00e3o com reposi\u00e7\u00e3o sem reposi\u00e7\u00e3o diagrama em \u00e1rvore urna saco bolas experi\u00eancia composta|M|d9
# Casos-limite: dados vazios, frequencias negativas ou nao inteiras,
# valores repetidos com frequencias, todos com a mesma frequencia (sem
# moda), casos favoraveis > possiveis, nomes ambiguos ou desconhecidos,
# urna com uma so bola (sem reposicao), condicao mal escrita.

import m1_nucleo as N
import m1_q as Q


def toks(t):
    return t.replace(';', ' ').split()


def qnum(p):
    try:
        return Q.cte(Q.poli(Q.arvore(p)))
    except ValueError:
        return None


def ap(x, d):
    s, ex = N.fmt2(x, 0, d)
    return ('' if ex else N.AP + ' ') + s


def pr(a, b):
    # Probabilidade a/b: fracao, simplificada, decimal e percentagem.
    s = str(a) + '/' + str(b)
    if a == 0 or a == b:
        return s + ' = ' + ('0' if a == 0 else '1') + \
            (' = 0%' if a == 0 else ' = 100%')
    q = Q.R(a, b)
    if q != (a, b):
        s += ' = ' + Q.qs(q)
    x = a / b
    d, e1 = N.fmt2(x, 0, 2)
    p, e2 = N.fmt2(100 * x, 0, 1)
    return s + (' = ' if e1 else ' ' + N.AP + ' ') + d + \
        (' = ' if e2 else ' ' + N.AP + ' ') + p + '%'


def escala(a, b):
    if a == 0:
        return 'imposs\u00edvel'
    if a == b:
        return 'certo'
    return 'pouco prov\u00e1vel' if 2 * a < b else (
        't\u00e3o prov\u00e1vel como improv\u00e1vel' if 2 * a == b else 'muito prov\u00e1vel')

# ------------------------------------------------------------ frequencias


def freq():
    return ('Tabela de frequ\u00eancias',
            [N.fld('Dados (ou os valores diferentes)', '',
                   '3 5 4 3 2 5 3 4 1 3', 't'),
             N.fld('Frequ\u00eancias absolutas (opcional)', '', '', 't')], _freq)


def _freq(v):
    ts = toks(v[0])
    N.need(ts, 'Escreve os dados separados por espa\u00e7os')
    if v[1].strip():
        fs = toks(v[1])
        N.need(len(fs) == len(ts), 'H\u00e1 ' + str(len(ts)) + ' valores e ' +
               str(len(fs)) + ' frequ\u00eancias')
        cs = []
        for f in fs:
            q = qnum(f)
            N.need(q is not None and q[1] == 1 and q[0] >= 0, 'As '
                   'frequ\u00eancias absolutas s\u00e3o n\u00fameros inteiros (0, 1, 2...)')
            cs.append(q[0])
        vs = ts
    else:
        vs, cs = [], []
        for t in ts:
            if t in vs:
                cs[vs.index(t)] += 1
            else:
                vs.append(t)
                cs.append(1)
    qs = [qnum(t) for t in vs]
    num = None not in qs
    if num:
        d = {}
        for i in range(len(qs)):
            d[qs[i]] = d.get(qs[i], 0) + cs[i]
        ks = sorted(d.keys(), key=Q.qf)
        cs = [d[k] for k in ks]
        vs = [Q.vstr(k) for k in ks]
    else:
        N.need(len(set([N.low(x) for x in vs])) == len(vs) or not v[1].strip(),
               'H\u00e1 valores repetidos: escreve cada valor uma s\u00f3 vez')
    n = sum(cs)
    N.need(n > 0, 'O total das frequ\u00eancias \u00e9 0')
    o = ['n = ' + str(n) + ' dados ' + ('quantitativos' if num else
                                       'qualitativos') + '; ' + str(len(vs)) +
         ' valores diferentes.',
         'Valor \u2192 freq. absoluta; relativa; \u00e2ngulo no gr\u00e1fico circular']
    ac = 0
    for i in range(len(vs)):
        ac += cs[i]
        o.append(vs[i] + ' \u2192 ' + str(cs[i]) + '; ' + pr(cs[i], n) + '; ' +
                 ap(360 * cs[i] / n, 1) + '\u00b0' +
                 ('; acumulada ' + str(ac) if num else ''))
    o.append('Soma das frequ\u00eancias relativas: 1 (100%); dos \u00e2ngulos: 360\u00b0.')
    m = max(cs)
    mo = [vs[i] for i in range(len(vs)) if cs[i] == m]
    if len(mo) == len(vs) and len(vs) > 1:
        o.append('> N\u00e3o h\u00e1 moda: todos os valores t\u00eam a mesma frequ\u00eancia.')
    else:
        o.append('> Moda: ' + ', '.join(mo) + ' (frequ\u00eancia ' + str(m) + ')' +
                 (' - bimodal' if len(mo) == 2 else ''))
    r = None
    if num:
        s = Q.Z
        for i in range(len(ks)):
            s = Q.add(s, Q.mul(ks[i], (cs[i], 1)))
        r = Q.div(s, (n, 1))
        if len(ks) <= 8:
            t = ' + '.join([Q.vstr(ks[i]) + ' ' + N.X + ' ' + str(cs[i])
                            for i in range(len(ks))])
            o.append('> M\u00e9dia = (' + t + ') / ' + str(n) + ' = ' + Q.vstr(s) +
                     ' / ' + str(n) + ' ' + rq(r, Q.R(s[0], s[1] * n)))
        else:
            o.append('> M\u00e9dia = soma / n = ' + Q.vstr(s) + ' / ' + str(n) +
                     ' ' + rq(r, Q.R(s[0], s[1] * n)))

        def pos(k):
            a = 0
            for i in range(len(ks)):
                a += cs[i]
                if a >= k:
                    return ks[i]
        if n % 2:
            me = pos((n + 1) // 2)
            o.append('> Mediana: ' + Q.vstr(me) + ' (n \u00edmpar: valor na posi\u00e7\u00e3o '
                     + str((n + 1) // 2) + ')')
        else:
            a, b = pos(n // 2), pos(n // 2 + 1)
            me = Q.div(Q.add(a, b), (2, 1))
            o.append('> Mediana: (' + Q.vstr(a) + ' + ' + Q.vstr(b) + ') / 2 ' +
                     rq(me) + ' (n par: posi\u00e7\u00f5es ' + str(n // 2) + ' e ' +
                     str(n // 2 + 1) + ')')
        o.append('> Amplitude: ' + Q.vstr(ks[-1]) + ' - ' + Q.vstr(ks[0]) +
                 ' = ' + Q.vstr(Q.sub(ks[-1], ks[0])))
        r = Q.qf(r)
    else:
        o.append('Dados qualitativos: n\u00e3o h\u00e1 m\u00e9dia nem mediana (s\u00f3 moda).')
    st = 'Frequ\u00eancia relativa = frequ\u00eancia absoluta / n.\n\u00c2ngulo do setor ' \
        'no gr\u00e1fico circular = frequ\u00eancia relativa ' + N.X + ' 360\u00b0.\n' \
        'Mediana: ordenam-se os dados e escolhe-se o do meio (ou a m\u00e9dia dos' \
        ' dois do meio).'
    gr = barras(vs, cs) if len(vs) <= 12 else None
    return ('\n'.join(o), st, r, '', gr) if gr else ('\n'.join(o), st, r, '')


def rq(q, d=None):
    # "= 3,3", "= 10/3 \u2248 3,33" ou so "\u2248 2,29" se q ja e d (a/b).
    s = Q.vstr(q)
    if '/' not in s:
        return '= ' + s
    a = N.AP + ' ' + N.fmt(Q.qf(q), 0, 2)
    return a if q == d else '= ' + s + ' ' + a


def barras(vs, cs):
    k = len(vs)
    m = max(cs)
    sg = []
    for i in range(k):
        x = i + 1
        sg += [(x - 0.3, 0, x - 0.3, cs[i]), (x - 0.3, cs[i], x + 0.3, cs[i]),
               (x + 0.3, cs[i], x + 0.3, 0)]
    w = 4 if k <= 6 else 2
    return ('Gr\u00e1fico de barras', [
        ('s', sg, 4),
        ('t', [(i + 0.75, cs[i] + 0.02 * m, str(cs[i])) for i in range(k)], 0),
        ('t', [(i + 0.7, -0.2 * m, vs[i][:w]) for i in range(k)], 2)],
        0.3, k + 0.7, -0.26 * m, 1.18 * m, 'barras: frequ\u00eancias absolutas')

# ------------------------------------------------------------ Laplace


def casos(t):
    # "3 azuis 5 vermelhas" -> [(3, 'azuis'), (5, 'vermelhas')];
    # "3 10" -> [(3, ''), (10, '')].
    out = []
    for p in toks(t):
        q = qnum(p)
        if q is not None:
            N.need(q[1] == 1 and q[0] >= 0, 'O n\u00famero de casos tem de ser um '
                   'inteiro: ' + p)
            out.append([q[0], ''])
        else:
            N.need(out, 'Come\u00e7a por um n\u00famero (ex.: 3 azuis 5 vermelhas)')
            out[-1][1] = (out[-1][1] + ' ' + p).strip()
    N.need(out, 'Escreve os casos (ex.: 3 azuis 5 vermelhas)')
    return out


def acha(w, nomes):
    # Indice do nome que melhor corresponde a w (prefixo comum).
    w = N.low(w)
    best, bi, dup = 0, -1, 0
    for i in range(len(nomes)):
        a = N.low(nomes[i])
        k = 0
        while k < min(len(a), len(w)) and a[k] == w[k]:
            k += 1
        if a == w:
            return i
        if k > best:
            best, bi, dup = k, i, 0
        elif k == best:
            dup = 1
    N.need(bi >= 0 and best >= min(3, len(w)), 'N\u00e3o conhe\u00e7o "' + w +
           '"; usa um dos nomes: ' + ', '.join(nomes))
    N.need(not dup, '"' + w + '" pode ser mais do que um nome; escreve '
           'mais letras (' + ', '.join(nomes) + ')')
    return bi


def prob():
    return ('Probabilidade (Laplace)',
            [N.fld('Casos (ex.: 3 azuis 5 vermelhas)', '',
                   '3 azuis 5 vermelhas 2 verdes', 't'),
             N.fld('Acontecimento (ex.: azuis verdes)', '', 'azuis', 't')],
            _prob)


def _prob(v):
    cs = casos(v[0])
    if len(cs) == 2 and not cs[0][1] and not cs[1][1]:
        a, b = cs[0][0], cs[1][0]
        N.need(b > 0, 'Os casos poss\u00edveis n\u00e3o podem ser 0')
        N.need(a <= b, 'Os casos favor\u00e1veis n\u00e3o podem ser mais do que os '
               'poss\u00edveis')
        o = ['= P(A) = casos favor\u00e1veis / casos poss\u00edveis',
             '> P(A) = ' + pr(a, b)]
    else:
        nomes = [c[1] for c in cs]
        N.need('' not in nomes, 'D\u00e1 um nome a cada grupo (ex.: 3 azuis 5 '
               'vermelhas)')
        b = sum([c[0] for c in cs])
        N.need(b > 0, 'N\u00e3o h\u00e1 casos poss\u00edveis')
        o = ['Casos poss\u00edveis: ' + ' + '.join([str(c[0]) for c in cs]) +
             ' = ' + str(b) + ' (igualmente prov\u00e1veis).']
        for c in cs:
            o.append('P(' + c[1] + ') = ' + pr(c[0], b))
        ws = toks(v[1])
        if not ws:
            return ('\n'.join(o), ST_LAP, None, '')
        neg = N.low(ws[0]) in ('nao', 'n')
        if neg:
            ws = ws[1:]
            N.need(ws, 'Escreve o que vem depois de "n\u00e3o"')
        ix = []
        for w in ws:
            i = acha(w, nomes)
            if i not in ix:
                ix.append(i)
        if neg:
            ix = [i for i in range(len(cs)) if i not in ix]
        a = sum([cs[i][0] for i in ix])
        nm = ' ou '.join([cs[i][1] for i in ix]) or 'nenhum'
        o += ['Acontecimento A: ' + nm, '= P(A) = casos favor\u00e1veis / casos '
              'poss\u00edveis', '> P(A) = ' + ('(' + ' + '.join(
                  [str(cs[i][0]) for i in ix]) + ')/' + str(b) + ' = ' if
                  len(ix) > 1 else '') + pr(a, b)]
    o += ['Contr\u00e1rio: P(n\u00e3o A) = 1 - P(A) = ' + pr(b - a, b),
          'A \u00e9 um acontecimento ' + escala(a, b) + '.']
    return ('\n'.join(o), ST_LAP, a / b, '')


ST_LAP = 'Lei de Laplace (casos igualmente prov\u00e1veis): P(A) = casos ' \
    'favor\u00e1veis / casos poss\u00edveis.\n0 \u2264 P(A) \u2264 1; P(n\u00e3o A) = 1 - P(A).'

# ------------------------------------------------------------ dados


OPD = ['Soma de dois dados', 'Produto de dois dados',
       'Diferen\u00e7a de dois dados', 'Duas moedas (n.\u00ba de E)',
       'Tr\u00eas moedas (n.\u00ba de E)']


def dados():
    return ('Dois dados ou moedas',
            [N.fld('Experi\u00eancia', '', '', 'c', OPD),
             N.fld('Acontecimento (ex.: 7, > 9, par, primo)', '', '7', 't')],
            _dados)


def primo(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def cond(t):
    # Texto -> (descricao, funcao). Vazio -> None.
    s = N.low(t).replace(' ', '')
    if not s:
        return None
    for a, b in (('pelomenos', '>='), ('nomaximo', '<='), ('maisde', '>'),
                 ('menosde', '<'), ('igual', '=')):
        if s.startswith(a):
            s = b + s[len(a):].lstrip('a')
    if s in ('par', 'pares'):
        return '\u00e9 par', lambda x: x % 2 == 0
    if s in ('impar', 'impares'):
        return '\u00e9 \u00edmpar', lambda x: x % 2 == 1
    if s in ('primo', 'primos'):
        return '\u00e9 n\u00famero primo', primo
    for a, nm in (('multiplode', '\u00e9 m\u00faltiplo de '),
                  ('divisorde', '\u00e9 divisor de ')):
        if s.startswith(a):
            k = qnum(s[len(a):])
            N.need(k is not None and k[1] == 1 and k[0] > 0, 'Escreve o n\u00famero'
                   ' depois de "' + nm[2:].strip() + '"')
            k = k[0]
            if a[0] == 'm':
                return nm + str(k), lambda x: x % k == 0
            return nm + str(k), lambda x: x > 0 and k % x == 0
    op = '='
    for p in ('>=', '<=', '!=', '=', '>', '<'):
        if s.startswith(p):
            op, s = p, s[len(p):]
            break
    j = 0
    while j < len(s) and s[j] in '0123456789,./-':
        j += 1
    k = qnum(s[:j]) if j and s[j:].isalpha() or j == len(s) else None
    N.need(k is not None, 'N\u00e3o percebi o acontecimento; exemplos: 7, > 9, '
           '<= 4, par, \u00edmpar, primo, m\u00faltiplo de 3, pelo menos 1')
    x = Q.qf(k)
    f = {'=': lambda y: y == x, '!=': lambda y: y != x, '>': lambda y: y > x,
         '<': lambda y: y < x, '>=': lambda y: y >= x, '<=': lambda y: y <= x}
    return {'>=': '\u2265 ', '<=': '\u2264 ', '!=': '\u2260 '}.get(
        op, op + ' ') + Q.vstr(k), f[op]


def _dados(v):
    k = v[0]
    c = cond(v[1])
    if k <= 2:
        fn = (lambda a, b: a + b, lambda a, b: a * b,
              lambda a, b: abs(a - b))[k]
        nm = ('soma', 'produto', 'diferen\u00e7a')[k]
        cs = [((a, b), fn(a, b)) for a in range(1, 7) for b in range(1, 7)]
        o = ['Tabela de dupla entrada (' + nm + '; 1.\u00ba dado nas linhas):']
        for a in range(1, 7):
            o.append(str(a) + ' | ' + ' '.join([str(fn(a, b)) for b in
                                                range(1, 7)]))

        def cx(p):
            return '(' + str(p[0]) + ',' + str(p[1]) + ')'
    else:
        m = 2 if k == 3 else 3
        nm = 'n.\u00ba de E'
        cs = [('',  0)]
        for i in range(m):
            cs = [(s + l, e + (l == 'E')) for s, e in cs for l in 'EN']
        o = ['E: face europeia; N: face nacional. Casos: ' +
             ', '.join([s for s, e in cs])]

        def cx(p):
            return p
    n = len(cs)
    vs = sorted(set([x for p, x in cs]))
    o += [str(n) + ' casos poss\u00edveis, todos igualmente prov\u00e1veis.',
          'Valores (' + nm + ') e n\u00famero de casos: ' + '; '.join(
              [str(x) + ': ' + str(len([1 for p, y in cs if y == x])) for x in
               vs])]
    r = None
    fav = []
    if c:
        fav = [p for p, x in cs if c[1](x)]
        a = len(fav)
        o.append('Acontecimento A: ' + nm + ' ' + c[0])
        if fav:
            o.append('Casos favor\u00e1veis: ' + (' '.join([cx(p) for p in fav]) +
                                             ' \u2192 ' + str(a) if a <= 12 else
                                             str(a) + ' (a vermelho na tabela)'))
        o.append('> P(A) = ' + pr(a, n))
        r = a / n
    if k <= 2:
        its = [('t', [(1.7 + b, 8, str(b)) for b in range(1, 7)] +
                [(0.7, 7 - a + 1, str(a)) for a in range(1, 7)], 2),
               ('t', [(0.7, 8, {0: '+', 1: N.X, 2: '-'}[k])], 0),
               ('s', [(0.5, 7.9, 8.4, 7.9), (1.5, 1.4, 1.5, 8.9)], 7)]
        for f in (0, 1):
            its.append(('t', [(1.7 + p[1], 8 - p[0], str(x)) for p, x in cs
                              if (p in fav) == bool(f)], 5 if f else 0))
        gr = ('Tabela de dupla entrada: ' + nm, its, 0.4, 8.4, 1.2, 9.0,
              'vermelho: casos favor\u00e1veis' if fav else '')
        return ('\n'.join(o), ST_DAD, r, '', gr)
    return ('\n'.join(o), ST_DAD, r, '')


ST_DAD = 'Experi\u00eancia composta: contam-se todos os pares de resultados ' \
    '(tabela de dupla entrada ou diagrama em \u00e1rvore).\nCom dois dados h\u00e1 ' \
    '6 ' + N.X + ' 6 = 36 casos igualmente prov\u00e1veis.'

# ------------------------------------------------------------ urna


def urna():
    return ('Duas extra\u00e7\u00f5es',
            [N.fld('Composi\u00e7\u00e3o (ex.: 3 azuis 2 brancas)', '',
                   '3 azuis 2 brancas', 't'),
             N.fld('Extra\u00e7\u00f5es', '', '', 'c', ['Sem reposi\u00e7\u00e3o',
                                             'Com reposi\u00e7\u00e3o']),
             N.fld('Acontecimento (ex.: azul branca)', '', '', 't')], _urna)


def _urna(v):
    cs = casos(v[0])
    nomes = [c[1] for c in cs]
    N.need('' not in nomes and len(cs) >= 2, 'Escreve pelo menos dois grupos'
           ' com nome (ex.: 3 azuis 2 brancas)')
    N.need(len(cs) <= 6, 'No m\u00e1ximo 6 grupos')
    sr = v[1] == 0
    T = sum([c[0] for c in cs])
    N.need(T >= 2 or not sr, 'Sem reposi\u00e7\u00e3o s\u00e3o precisas pelo menos 2 bolas')
    N.need(T > 0, 'A urna est\u00e1 vazia')
    T2 = T - 1 if sr else T
    o = ['Total: ' + str(T) + '; duas extra\u00e7\u00f5es ' + ('sem' if sr else 'com') +
         ' reposi\u00e7\u00e3o' + (' (2.\u00aa extra\u00e7\u00e3o com ' + str(T2) + ')' if sr else '')
         + '.']
    P = {}
    k = len(cs)
    for i in range(k):
        for j in range(k):
            a = cs[i][0]
            b = cs[j][0] - (1 if sr and i == j else 0)
            P[(i, j)] = (a * b, T * T2)
            o.append(nomes[i] + ' \u2192 ' + nomes[j] + ': ' + str(a) + '/' +
                     str(T) + ' ' + N.X + ' ' + str(b) + '/' + str(T2) + ' = ' +
                     Q.qs(Q.R(a * b, T * T2)))
    s = Q.Z
    for x in P.values():
        s = Q.add(s, Q.R(x[0], x[1]))
    o.append('Soma de todos os ramos: ' + Q.qs(s) + ' \u2713')
    ig = [P[(i, i)] for i in range(k)]
    a = sum([x[0] for x in ig])
    o += ['> Do mesmo tipo (ex.: mesma cor): ' + pr(a, T * T2),
          '> De tipos diferentes: ' + pr(T * T2 - a, T * T2)]
    ws = toks(v[2])
    r = None
    if len(ws) == 2:
        i, j = acha(ws[0], nomes), acha(ws[1], nomes)
        x = P[(i, j)]
        o.append('> P(1.\u00aa ' + nomes[i] + ' e 2.\u00aa ' + nomes[j] + ') = ' +
                 pr(x[0], x[1]))
        r = x[0] / x[1]
        if i != j:
            y = P[(j, i)]
            o.append('> P(uma ' + nomes[i] + ' e uma ' + nomes[j] + ', por '
                     'qualquer ordem) = ' + pr(x[0] + y[0], x[1]))
    elif len(ws) == 1:
        i = acha(ws[0], nomes)
        d = P[(i, i)][0]
        u = sum([P[(i, j)][0] + P[(j, i)][0] for j in range(k) if j != i])
        n = T * T2
        o += ['> P(duas ' + nomes[i] + ') = ' + pr(d, n),
              '> P(exatamente uma ' + nomes[i] + ') = ' + pr(u, n),
              '> P(pelo menos uma ' + nomes[i] + ') = 1 - P(nenhuma) = ' +
              pr(d + u, n)]
        r = (d + u) / n
    else:
        N.need(not ws, 'Escreve um ou dois nomes (ex.: azul branca)')
    st = 'Diagrama em \u00e1rvore: multiplica-se ao longo dos ramos e somam-se ' \
        'os caminhos favor\u00e1veis.\nSem reposi\u00e7\u00e3o, na 2.\u00aa extra\u00e7\u00e3o h\u00e1 menos ' \
        'uma bola (e menos uma da cor que saiu).'
    gr = arvore(cs, P, T, T2, sr) if k <= 3 else None
    return ('\n'.join(o), st, r, '', gr) if gr else ('\n'.join(o), st, r, '')


def arvore(cs, P, T, T2, sr):
    k = len(cs)
    ab = []
    for c in cs:
        w = N.low(c[1])
        n = 1
        while n < len(w) and [1 for d in cs if d is not c and
                              N.low(d[1])[:n] == w[:n]]:
            n += 1
        ab.append(c[1][:max(n, 3)])
    L = k * k
    x1, x2 = (3.6, 6.6) if k <= 2 else (3.3, 6.0)
    sg, rt, pb = [], [], []
    r0 = (0.8, (L + 1) / 2)
    for i in range(k):
        ys = [L - (i * k + j) for j in range(k)]
        n1 = (x1, sum(ys) / k)
        sg.append((r0[0], r0[1], n1[0], n1[1]))
        rt.append((n1[0], n1[1], ab[i]))
        pb.append(((r0[0] + n1[0]) / 2 - 0.4, (r0[1] + n1[1]) / 2 + 0.15,
                   str(cs[i][0]) + '/' + str(T)))
        for j in range(k):
            n2 = (x2, ys[j])
            sg.append((n1[0] + 0.2 + 0.25 * len(ab[i]), n1[1], n2[0], n2[1]))
            b = str(cs[j][0] - (1 if sr and i == j else 0)) + '/' + str(T2)
            q = Q.qs(Q.R(P[(i, j)][0], P[(i, j)][1]))
            if k <= 2:
                rt.append((n2[0], n2[1], ab[j] + '  ' + q))
                pb.append(((n1[0] + n2[0]) / 2 + 0.3, (n1[1] + n2[1]) / 2 +
                           0.15, b))
            else:
                rt.append((n2[0], n2[1], ab[j] + ' ' + b + ': ' + q))
    return ('Diagrama em \u00e1rvore', [('s', sg, 7), ('t', rt, 0), ('t', pb, 4)],
            0.5, 10.5, 0.3, L + 0.7, 'azul: probabilidade de cada ramo')
