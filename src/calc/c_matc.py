# c_matc.py - M1TR4M: modelos matematicos para a cidadania - eleicoes:
# sistemas de votacao com uma tabela de preferencias (maioria simples e
# absoluta, Borda, segunda volta, eliminacao sucessiva e Condorcet, este
# como aprofundamento) e partilha de mandatos (Hondt e Sainte-Lague, com
# a regra de empate da lei eleitoral da Assembleia da Republica).
#@ c_matc.vot|Sistemas de vota\u00e7\u00e3o|maioria simples relativa absoluta borda segunda volta elimina\u00e7\u00e3o sucessiva condorcet tabela de prefer\u00eancias elei\u00e7\u00e3o votantes|M|m1
#@ c_matc.mand|Mandatos: Hondt e Sainte-Lagu\u00eb|m\u00e9todo de hondt sainte-lagu\u00eb mandatos deputados divisores quocientes partilha proporcional listas votos empate|M|m1
# Casos-limite: empates (1.o lugar, passagem a 2.a volta, ultimo lugar
# na eliminacao, ultimo mandato), preferencias incompletas ou repetidas,
# colunas sem votantes, listas sem votos.

import m1_nucleo as N

MS = '\u00b7'


def grp(s):
    # Separa os milhares com espacos: "12000,5" -> "12 000,5".
    neg = s.startswith('-')
    if neg:
        s = s[1:]
    k = s.find(',')
    i, d = (s, '') if k < 0 else (s[:k], s[k:])
    g = ''
    while len(i) > 3:
        g = ' ' + i[-3:] + g
        i = i[:-3]
    return ('-' if neg else '') + i + g + d


def num(x, d=2):
    # Inteiro sem casas; senao d casas decimais (quocientes, percentagens).
    if x == int(x):
        return grp(str(int(x)))
    return grp(N.fmt(x, 0, d))


def inteiros(xs, nm):
    out = []
    for v in xs:
        v = v[0]
        N.need(v >= 0 and v == int(v), nm + ' t\u00eam de ser n\u00fameros inteiros '
               'n\u00e3o negativos')
        out.append(int(v))
    return out


def e_lista(ns):
    # "A", "A e B", "A, B e C"
    if len(ns) == 1:
        return ns[0]
    return ', '.join(ns[:-1]) + ' e ' + ns[-1]


def linha(ns, cs):
    return (' ' + MS + ' ').join([ns[i] + ' ' + num(cs[i]) for i in range(len(ns))])

# ------------------------------------------------------------ votacao


def vot():
    return ('Sistemas de vota\u00e7\u00e3o',
            [N.fld('Votantes de cada coluna', '', '10 8 7 4', 'l'),
             N.fld('Prefer\u00eancias de cada coluna (1.\u00ba ao \u00faltimo)', '',
                   'ABC BCA CBA CAB', 't'),
             N.fld('M\u00e9todo', '', '', 'c',
                   ['todos (compara\u00e7\u00e3o)', 'maioria simples e absoluta',
                    'Borda', 'segunda volta', 'elimina\u00e7\u00e3o sucessiva',
                    'Condorcet (aprofundamento)'])], _vot)


def perfil(vs, tp):
    ps = tp.upper().replace(';', ' ').replace(',', ' ').split()
    N.need(ps, 'Escreve as prefer\u00eancias de cada coluna (ABC BCA)')
    N.need(len(ps) == len(vs), 'H\u00e1 ' + str(len(vs)) + ' n\u00fameros de votantes e ' +
           str(len(ps)) + ' colunas de prefer\u00eancias')
    cs = sorted(ps[0])
    N.need(len(cs) >= 2, 'S\u00e3o precisos pelo menos 2 candidatos')
    for p in ps:
        for ch in p:
            N.need('A' <= ch <= 'Z', 'Usa uma letra para cada candidato (A, B, '
                   'C...)')
        N.need(sorted(p) == cs and len(p) == len(cs), 'Cada coluna tem de ter '
               'todos os candidatos, uma vez cada: ' + ''.join(cs))
    return ps, cs


def conta1(vs, ps, at):
    # Votos em 1.o lugar de cada candidato ainda em jogo (lista at).
    c = [0] * len(at)
    for i in range(len(vs)):
        for ch in ps[i]:
            if ch in at:
                c[at.index(ch)] += vs[i]
                break
    return c


def topo(at, c):
    m = max(c)
    return [at[i] for i in range(len(at)) if c[i] == m], m


def duelo(vs, ps, a, b):
    # Votantes que preferem a a b.
    n = 0
    for i in range(len(vs)):
        if ps[i].index(a) < ps[i].index(b):
            n += vs[i]
    return n


def maiorias(vs, ps, cs, T, o):
    c = conta1(vs, ps, cs)
    w, m = topo(cs, c)
    o.append('Votos em 1.\u00ba lugar: ' + linha(cs, c))
    if len(w) == 1:
        o.append('> Maioria simples (relativa): ' + w[0] + ' (' + num(m) + ' votos)')
    else:
        o.append('> Maioria simples: empate entre ' + e_lista(w))
    if m * 2 > T:
        o.append('> Maioria absoluta: ' + w[0] + ' (' + num(m) + ' > ' +
                 num(T / 2) + ')')
        return w[0] if len(w) == 1 else '', w[0]
    o.append('Maioria absoluta: ningu\u00e9m tem mais de metade dos votos (' +
             num(T / 2) + ').')
    return (w[0] if len(w) == 1 else ''), ''


def borda(vs, ps, cs, o):
    n = len(cs)
    pt = [0] * n
    for i in range(len(vs)):
        for j in range(n):
            pt[cs.index(ps[i][j])] += vs[i] * (n - j)
    w, m = topo(cs, pt)
    o.append('Borda (' + str(n) + ' pontos ao 1.\u00ba, ..., 1 ao \u00faltimo): ' +
             linha(cs, pt))
    o.append('> Borda: ' + (w[0] if len(w) == 1 else 'empate entre ' +
                            e_lista(w)) + ' (' + num(m) + ' pontos)')
    return w[0] if len(w) == 1 else ''


def segunda(vs, ps, cs, T, o):
    c = conta1(vs, ps, cs)
    w, m = topo(cs, c)
    if m * 2 > T and len(w) == 1:
        o.append('> Segunda volta: n\u00e3o \u00e9 precisa; ' + w[0] +
                 ' tem maioria absoluta na 1.\u00aa volta.')
        return w[0]
    ix = list(range(len(cs)))
    ix.sort(key=lambda i: (-c[i], i))
    if len(cs) > 2 and c[ix[1]] == c[ix[2]]:
        o.append('Segunda volta: empate no 2.\u00ba lugar da 1.\u00aa volta (' +
                 e_lista([cs[i] for i in ix[1:] if c[i] == c[ix[1]]]) +
                 '); a lei teria de desempatar.')
        return ''
    a, b = cs[ix[0]], cs[ix[1]]
    na = duelo(vs, ps, a, b)
    o.append('Segunda volta entre ' + a + ' e ' + b + ': ' + a + ' ' + num(na) +
             ' ' + MS + ' ' + b + ' ' + num(T - na))
    if na * 2 == T:
        o.append('> Segunda volta: empate')
        return ''
    g = a if na * 2 > T else b
    o.append('> Segunda volta: ' + g)
    return g


def elimina(vs, ps, cs, T, o):
    at = list(cs)
    r = 1
    while True:
        c = conta1(vs, ps, at)
        w, m = topo(at, c)
        s = str(r) + '.\u00aa contagem: ' + linha(at, c)
        if m * 2 > T and len(w) == 1:
            o += [s, '> Elimina\u00e7\u00e3o sucessiva: ' + w[0] + ' (maioria absoluta)']
            return w[0]
        mn = min(c)
        sai = [at[i] for i in range(len(at)) if c[i] == mn]
        if len(sai) == len(at):
            o += [s, '> Elimina\u00e7\u00e3o sucessiva: empate entre ' + e_lista(at)]
            return ''
        o.append(s + ' \u2192 sai ' + e_lista(sai) + (
            ' (empate no \u00faltimo lugar: saem todos)' if len(sai) > 1 else ''))
        at = [x for x in at if x not in sai]
        r += 1


def condorcet(vs, ps, cs, T, o):
    o.append('Condorcet (aprofundamento), cada par:')
    ganha = [0] * len(cs)
    for i in range(len(cs)):
        for j in range(i + 1, len(cs)):
            a, b = cs[i], cs[j]
            na = duelo(vs, ps, a, b)
            nb = T - na
            if na > nb:
                ganha[i] += 1
                r = a
            elif nb > na:
                ganha[j] += 1
                r = b
            else:
                r = 'empate'
            o.append(' ' + a + ' vs ' + b + ': ' + num(na) + ' - ' + num(nb) +
                     ' \u2192 ' + r)
    for i in range(len(cs)):
        if ganha[i] == len(cs) - 1:
            o.append('> Vencedor de Condorcet: ' + cs[i] + ' (ganha a todos)')
            return cs[i]
    o.append('> N\u00e3o h\u00e1 vencedor de Condorcet: nenhum candidato ganha a '
             'todos os outros.')
    return ''


def _vot(v):
    tv, tp, mt = v
    vs = inteiros(tv, 'Os votantes')
    ps, cs = perfil(vs, tp)
    T = sum(vs)
    N.need(T > 0, 'N\u00e3o h\u00e1 votantes')
    o = [str(len(cs)) + ' candidatos, ' + num(T) + ' votantes.']
    res = []
    if mt in (0, 1):
        s, a = maiorias(vs, ps, cs, T, o)
        res.append(('maioria simples', s))
        if mt == 0:
            res.append(('maioria absoluta', a))
    if mt in (0, 2):
        res.append(('Borda', borda(vs, ps, cs, o)))
    if mt in (0, 3):
        res.append(('segunda volta', segunda(vs, ps, cs, T, o)))
    if mt in (0, 4):
        res.append(('elimina\u00e7\u00e3o', elimina(vs, ps, cs, T, o)))
    if mt in (0, 5):
        res.append(('Condorcet', condorcet(vs, ps, cs, T, o)))
    if mt == 0:
        o.append('Resumo: ' + '; '.join([a + ' ' + (b if b else '-')
                                         for a, b in res]) + '.')
        if len(set([b for a, b in res[2:] + res[:1] if b])) > 1:
            o.append('M\u00e9todos diferentes, vencedores diferentes: o sistema '
                     'eleitoral importa.')
    st = 'Maioria simples: mais votos em 1.\u00ba lugar. Maioria absoluta: ' \
        'mais de metade dos votos.\nBorda: com n candidatos, n pontos ao 1.\u00ba ' \
        'lugar, n - 1 ao 2.\u00ba, ..., 1 ao \u00faltimo.\nSegunda volta: os dois ' \
        'mais votados v\u00e3o a nova vota\u00e7\u00e3o.\nElimina\u00e7\u00e3o ' \
        'sucessiva: sai o menos votado at\u00e9 algu\u00e9m ter maioria absoluta.\n' \
        'Condorcet: ganha quem vence todos os outros, um a um.'
    return ('\n'.join(o), st, None, '')

# ------------------------------------------------------------ mandatos


def mand():
    return ('Mandatos: Hondt e Sainte-Lagu\u00eb',
            [N.fld('Votos de cada lista', '', '12000 8000 5000 2500', 'l'),
             N.fld('N\u00famero de mandatos', '', '7'),
             N.fld('Nomes das listas (opcional)', '', '', 't'),
             N.fld('M\u00e9todo', '', '', 'c', ['Hondt', 'Sainte-Lagu\u00eb',
                                               'os dois (compara\u00e7\u00e3o)'])],
            _mand)


def reparte(vs, m, sl):
    # Mandatos de cada lista; ordem de atribuicao; nota de empate.
    # Comparacoes exatas: a/b > c/d <=> a d > c b (inteiros).
    n = len(vs)
    s = [0] * n
    seq = []
    nota = ''

    def dv(k):
        return 2 * k + 1 if sl else k + 1
    while len(seq) < m:
        bv, bd = 0, 1
        for i in range(n):
            if vs[i] * bd > bv * dv(s[i]):
                bv, bd = vs[i], dv(s[i])
        if bv == 0:
            break
        ti = [i for i in range(n) if vs[i] * bd == bv * dv(s[i])]
        falta = m - len(seq)
        if len(ti) > falta:
            ti.sort(key=lambda i: (vs[i], i))
            if vs[ti[falta - 1]] == vs[ti[falta]]:
                nota = 'Empate no \u00faltimo mandato entre listas com os mesmos ' \
                    'votos: a regra da lei n\u00e3o decide.'
                break
            nota = 'Empate no \u00faltimo mandato: fica a lista com menos votos ' \
                '(Lei n.\u00ba 14/79, art. 16.\u00ba' + (', aplicada por analogia)'
                                                        if sl else ')') + '.'
            ti = ti[:falta]
        for i in ti:
            seq.append((i, vs[i] / dv(s[i])))
            s[i] += 1
    prox = 0
    for i in range(n):
        prox = max(prox, vs[i] / dv(s[i]))
    return s, seq, nota, prox


def _mand(v):
    tv, m, tn, mt = v
    vs = inteiros(tv, 'Os votos')
    N.need(sum(vs) > 0, 'Nenhuma lista tem votos')
    m = m[0]
    N.need(m == int(m) and 1 <= m <= 999, 'O n\u00famero de mandatos tem de ser '
           'um inteiro de 1 a 999')
    m = int(m)
    if tn:
        ns = tn.replace(';', ' ').split()
        N.need(len(ns) == len(vs), 'Escreve um nome para cada lista (' +
               str(len(vs)) + ')')
    else:
        N.need(len(vs) <= 26, 'No m\u00e1ximo 26 listas sem nome')
        ns = [chr(65 + i) for i in range(len(vs))]
    T = sum(vs)
    o = []
    rs = []
    for sl in ((0,), (1,), (0, 1))[mt]:
        s, seq, nota, prox = reparte(vs, m, sl)
        nm = 'Sainte-Lagu\u00eb' if sl else 'Hondt'
        o.append(nm + ' (divisores ' + ('1, 3, 5, 7...' if sl else
                                        '1, 2, 3, 4...') + '):')
        for i in range(len(vs)):
            qs = [vs[i] / (2 * k + 1 if sl else k + 1) for k in range(s[i] + 1)]
            o.append(' ' + ns[i] + ': ' + '; '.join([num(q) for q in qs[:-1]] +
                                                     ['(' + num(qs[-1]) + ')']))
        if seq:
            o.append('Ordem: ' + ', '.join([ns[i] for i, q in seq]))
            o.append('\u00daltimo mandato: ' + ns[seq[-1][0]] + ' (' +
                     num(seq[-1][1]) + '); quociente seguinte: ' + num(prox))
        if nota:
            o.append(nota)
        o.append('> ' + nm + ': ' + (' ' + MS + ' ').join(
            [ns[i] + ' ' + str(s[i]) for i in range(len(vs))]))
        for i in range(len(vs)):
            o.append(' ' + ns[i] + ': ' + num(100 * vs[i] / T, 1) + '% dos votos, ' +
                     num(100 * s[i] / m, 1) + '% dos mandatos')
        rs.append(s)
    if len(rs) == 2 and rs[0] != rs[1]:
        o.append('Os dois m\u00e9todos d\u00e3o resultados diferentes: o Hondt '
                 'favorece as listas mais votadas.')
    st = 'Divide-se o n\u00famero de votos de cada lista pelos divisores; os ' \
        'mandatos v\u00e3o, um a um, para os maiores quocientes.\nHondt: ' \
        '1, 2, 3, ...; Sainte-Lagu\u00eb: 1, 3, 5, ...\nEntre par\u00eanteses: o ' \
        'quociente seguinte de cada lista (n\u00e3o chegou).\nEmpate no \u00faltimo ' \
        'mandato: fica a lista com menos votos (Lei n.\u00ba 14/79, art. 16.\u00ba).'
    return ('\n'.join(o), st, None, '')
