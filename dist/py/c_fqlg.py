# c_fqlg.py - M1TR4M: calculadoras de ligacao quimica e reacoes:
# Lewis, geometria e polaridade (tabela verificada), entalpia de reacao
# a partir das energias de ligacao e acerto de equacoes quimicas.
#@ c_fqlg.lew|Lewis, geometria e polaridade|lewis geometria polaridade mol\u00e9cula pares ligantes n\u00e3o ligantes linear angular piramidal tetra\u00e9drica triangular|F|q4
#@ c_fqlg.dh|Entalpia de rea\u00e7\u00e3o (energias de liga\u00e7\u00e3o)|entalpia energia de liga\u00e7\u00e3o endotermica exotermica quebra forma\u00e7\u00e3o de liga\u00e7\u00f5es|F|q6
#@ c_fqlg.ace|Acerto de equa\u00e7\u00f5es qu\u00edmicas|acerto equa\u00e7\u00e3o qu\u00edmica coeficientes estequiom\u00e9tricos lei de lavoisier conserva\u00e7\u00e3o|F|r8
# Casos-limite: molecula fora da tabela (nao se inventa); ligacao sem
# energia na tabela (pede-se o valor); lista vazia; equacao sem seta,
# com especies repetidas, impossivel de acertar ou com mais de 8 especies.

import m1_nucleo as N
import m1_ui as U

X = N.X
# Tabela fechada: formula|nome|ve|ligacoes|pares nao ligantes|geometria|
# angulo|polar|estrutura
MOL = ("H\u2082|hidrog\u00e9nio|2|1 simples|0|linear||apolar|H-H\n"
       "F\u2082|fl\u00faor|14|1 simples|6 (3 em cada F)|linear||apolar|F-F\n"
       "Cl\u2082|cloro|14|1 simples|6 (3 em cada Cl)|linear||apolar|Cl-Cl\n"
       "O\u2082|oxig\u00e9nio|12|1 dupla|4 (2 em cada O)|linear||apolar|O=O\n"
       "N\u2082|azoto|10|1 tripla|2 (1 em cada N)|linear||apolar|N\u2261N\n"
       "HF|fluoreto de hidrog\u00e9nio|8|1 simples|3 (no F)|linear||polar|H-F\n"
       "HCl|cloreto de hidrog\u00e9nio|8|1 simples|3 (no Cl)|linear||polar|"
       "H-Cl\n"
       "H\u2082O|\u00e1gua|8|2 simples|2 (no O)|angular|104,5\u00b0|polar|H-O-H\n"
       "H\u2082S|sulfureto de hidrog\u00e9nio|8|2 simples|2 (no S)|angular|92\u00b0|"
       "polar|H-S-H\n"
       "NH\u2083|amon\u00edaco|8|3 simples|1 (no N)|piramidal trigonal|107\u00b0|"
       "polar|H-N(-H)-H\n"
       "CH\u2084|metano|8|4 simples|0|tetra\u00e9drica|109,5\u00b0|apolar|"
       "C ligado a 4 H\n"
       "CCl\u2084|tetracloreto de carbono|32|4 simples|12 (3 em cada Cl)|"
       "tetra\u00e9drica|109,5\u00b0|apolar|C ligado a 4 Cl\n"
       "CO\u2082|di\u00f3xido de carbono|16|2 duplas|4 (2 em cada O)|linear|180\u00b0|"
       "apolar|O=C=O\n"
       "HCN|cianeto de hidrog\u00e9nio|10|1 simples e 1 tripla|1 (no N)|"
       "linear|180\u00b0|polar|H-C\u2261N\n"
       "CH\u2082O|metanal|12|2 simples e 1 dupla|2 (no O)|triangular plana|"
       "120\u00b0|polar|H\u2082C=O\n"
       "C\u2082H\u2086|etano|14|7 simples|0|tetra\u00e9drica em cada C|109,5\u00b0|"
       "apolar|H\u2083C-CH\u2083\n"
       "C\u2082H\u2084|eteno|12|5 simples e 1 dupla|0|triangular plana em cada C|"
       "120\u00b0|apolar|H\u2082C=CH\u2082\n"
       "C\u2082H\u2082|etino|10|2 simples e 1 tripla|0|linear|180\u00b0|apolar|"
       "HC\u2261CH")


def lew():
    ms = [m.split('|') for m in MOL.split('\n')]
    sel = 0
    while True:
        r = U.menu('Lewis, geometria e polaridade', [m[0] + ' \u00b7 ' + m[1]
                                                     for m in ms], sel)
        if r < 0:
            return None
        sel = r
        m = ms[r]
        s = ['# ' + m[0] + ' (' + m[1] + ')',
             'Estrutura: ' + m[8],
             'Eletr\u00f5es de val\u00eancia: ' + m[2] + ' (' + str(int(m[2]) // 2) +
             ' pares)',
             'Liga\u00e7\u00f5es: ' + m[3],
             'Pares n\u00e3o ligantes: ' + m[4],
             'Geometria: ' + m[5] + (' (\u00e2ngulo ' + m[6] + ')' if m[6] else ''),
             '> Mol\u00e9cula ' + m[7]]
        if m[7] == 'apolar' and m[0] not in ('H\u2082', 'F\u2082', 'Cl\u2082', 'O\u2082',
                                             'N\u2082'):
            s.append('As liga\u00e7\u00f5es podem ser polares, mas a geometria '
                     'sim\u00e9trica anula os efeitos.')
        s.append('Fonte: tabela verificada da M1TR4M (s\u00f3 mol\u00e9culas do '
                 'programa).')
        U.text(m[0], '\n'.join(s))

# ------------------------------------------------------------ entalpia
# Energias medias de ligacao (kJ/mol), valores tipicos de manuais.
EL = ("H-H 436 C-H 413 C-C 348 C=C 614 C#C 839 C-O 358 C=O 799 O-H 463 "
      "O=O 498 O-O 146 N-H 391 N-N 163 N=N 418 N#N 945 C-N 293 C#N 891 "
      "H-F 567 H-Cl 431 H-Br 366 H-I 299 F-F 159 Cl-Cl 242 Br-Br 193 "
      "I-I 151 C-Cl 328 C-F 485 S-H 339")


def energia(lig):
    # Energia de uma ligacao da tabela ("C=O"); None se nao existir.
    t = EL.split(' ')
    a = lig.replace('\u2261', '#')
    b = '-'.join(a.split('-')[::-1]) if '-' in a else a
    for k in range(0, len(t) - 1, 2):
        x = t[k]
        if x == a or x == b or ('=' in x and x.split('=')[::-1] ==
                                a.split('=')) or ('#' in x and
                                                  x.split('#')[::-1] ==
                                                  a.split('#')):
            return int(t[k + 1])
    return None


def termos(txt):
    # "4 C-H; 2 O=O" ou "2 C=O:805" -> [(n, ligacao, energia)].
    out = []
    for p in txt.replace(',', ';').replace('\n', ';').split(';'):
        if not p.strip():
            continue
        p = p.strip()
        k = 0
        while k < len(p) and N.dig(p[k]):
            k += 1
        n = int(p[:k]) if k else 1
        rest = p[k:].strip()
        e = None
        if ':' in rest:
            rest, ev = rest.split(':')
            e = N.num(ev)[0]
        rest = rest.strip()
        N.need(rest != '', 'Falta a liga\u00e7\u00e3o em "' + p + '"')
        if e is None:
            e = energia(rest)
            N.need(e is not None, 'Liga\u00e7\u00e3o ' + rest + ' sem energia na '
                   'tabela: escreve-a assim: ' + rest + ':valor')
        out.append((n, rest, e))
    return out


def dh():
    return ('Entalpia de rea\u00e7\u00e3o',
            [N.fld('Liga\u00e7\u00f5es quebradas (ex.: 4 C-H; 2 O=O)', '',
                   '4 C-H; 2 O=O', 't'),
             N.fld('Liga\u00e7\u00f5es formadas (ex.: 2 C=O; 4 O-H)', '',
                   '2 C=O; 4 O-H', 't')], _dh)


def _dh(v):
    q = termos(v[0])
    f = termos(v[1])
    N.need(q and f, 'Escreve as liga\u00e7\u00f5es quebradas e as formadas')
    sq = sum([n * e for n, l, e in q])
    sf = sum([n * e for n, l, e in f])
    d = sq - sf
    o = ['= \u0394H = \u03a3 E(quebradas) - \u03a3 E(formadas)',
         'Quebradas: ' + ' + '.join([str(n) + ' ' + X + ' ' + N.fmt(e) for
                                     n, l, e in q]) + ' = ' + N.fmt(sq) +
         ' kJ',
         'Formadas: ' + ' + '.join([str(n) + ' ' + X + ' ' + N.fmt(e) for
                                    n, l, e in f]) + ' = ' + N.fmt(sf) +
         ' kJ',
         N.res('\u0394H', d, 'kJ mol\u207b\u00b9', 0, 0)]
    if d < 0:
        o.append('\u0394H < 0: rea\u00e7\u00e3o exot\u00e9rmica (liberta energia).')
    elif d > 0:
        o.append('\u0394H > 0: rea\u00e7\u00e3o endot\u00e9rmica (absorve energia).')
    else:
        o.append('\u0394H = 0 (com estes valores).')
    st = 'Quebrar liga\u00e7\u00f5es absorve energia; formar liga\u00e7\u00f5es liberta ' \
        'energia.\nAs energias da tabela s\u00e3o m\u00e9dias aproximadas: usa ' \
        'sempre as do enunciado (escreve C=O:805, por exemplo).'
    return ('\n'.join(o), st, d, 'kJ/mol')

# ------------------------------------------------------------ acerto
SUB = '\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089'


def contar(f):
    # Formula -> {elemento: quantidade} (sem carga; hidratos com ponto).
    o = []
    for c in f:
        k = SUB.find(c)
        o.append(str(k) if k >= 0 else c)
    f = ''.join(o).replace('\u00b7', '.')
    tot = {}
    for part in f.split('.'):
        i = 0
        co = 1
        k = 0
        while k < len(part) and N.dig(part[k]):
            k += 1
        if k:
            co = int(part[:k])
            i = k
        st = [{}]
        while i < len(part):
            c = part[i]
            if c in '([':
                st.append({})
                i += 1
            elif c in ')]':
                N.need(len(st) > 1, 'Par\u00eantese a mais em ' + f)
                g = st.pop()
                j = i + 1
                while j < len(part) and N.dig(part[j]):
                    j += 1
                m = int(part[i + 1:j]) if j > i + 1 else 1
                for a in g:
                    st[-1][a] = st[-1].get(a, 0) + g[a] * m
                i = j
            elif 'A' <= c <= 'Z':
                s = c
                i += 1
                if i < len(part) and 'a' <= part[i] <= 'z':
                    s += part[i]
                    i += 1
                j = i
                while j < len(part) and N.dig(part[j]):
                    j += 1
                m = int(part[i:j]) if j > i else 1
                st[-1][s] = st[-1].get(s, 0) + m
                i = j
            else:
                N.err('S\u00edmbolo inesperado "' + c + '" em ' + f)
        N.need(len(st) == 1, 'Falta fechar um par\u00eantese em ' + f)
        for a in st[0]:
            tot[a] = tot.get(a, 0) + st[0][a] * co
    return tot


def ace():
    return ('Acerto de equa\u00e7\u00f5es',
            [N.fld('Equa\u00e7\u00e3o (ex.: H2 + O2 -> H2O)', '',
                   'CH4 + O2 -> CO2 + H2O', 't')], _ace)


def _ace(v):
    t = v[0].replace('\u2192', '->').replace('=', '->')
    N.need('->' in t, 'Separa os reagentes dos produtos com ->')
    a, b = t.split('->', 1)
    rs = [x.strip() for x in a.split('+') if x.strip()]
    ps = [x.strip() for x in b.split('+') if x.strip()]
    N.need(rs and ps, 'Faltam reagentes ou produtos')
    sp = rs + ps
    N.need(len(sp) <= 8, 'No m\u00e1ximo 8 esp\u00e9cies')
    cs = [contar(x) for x in sp]
    els = []
    for c in cs:
        for e in c:
            if e not in els:
                els.append(e)
    els.sort()
    for e in els:
        N.need(any([e in c for c in cs[:len(rs)]]) and
               any([e in c for c in cs[len(rs):]]),
               'O elemento ' + e + ' s\u00f3 aparece de um dos lados')
    # matriz (elementos x especies), produtos com sinal menos
    M = [[(c.get(e, 0) if j < len(rs) else -c.get(e, 0))
          for j, c in enumerate(cs)] for e in els]
    k = nulo(M, len(sp))
    N.need(k is not None, 'N\u00e3o consegui acertar esta equa\u00e7\u00e3o '
           '(verifica as f\u00f3rmulas)')
    N.need(max(k) <= 1000, 'Coeficientes demasiado grandes')
    lado = lambda xs, ks: ' + '.join([(str(n) + ' ' if n > 1 else '') + x
                                      for x, n in zip(xs, ks)])
    o = ['> ' + lado(rs, k[:len(rs)]) + ' \u2192 ' + lado(ps, k[len(rs):])]
    o.append('Confer\u00eancia (\u00e1tomos de cada elemento):')
    for i, e in enumerate(els):
        r = sum([k[j] * cs[j].get(e, 0) for j in range(len(rs))])
        o.append('- ' + e + ': ' + str(r) + ' = ' + str(r))
    return ('\n'.join(o), 'Lei de Lavoisier: numa rea\u00e7\u00e3o qu\u00edmica a massa '
            'conserva-se, porque o n\u00famero de \u00e1tomos de cada elemento '
            '\u00e9 o mesmo antes e depois.', None, '')


def nulo(M, n):
    # Vetor inteiro positivo do nucleo de M (eliminacao com fracoes).
    A = [[(x, 1) for x in r] for r in M]
    piv = []
    r = 0
    for c in range(n):
        p = -1
        for i in range(r, len(A)):
            if A[i][c][0] != 0:
                p = i
                break
        if p < 0:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [_div(x, pv) for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c][0] != 0:
                f = A[i][c]
                A[i] = [_sub(A[i][j], _mul(f, A[r][j])) for j in range(n)]
        piv.append(c)
        r += 1
    livres = [c for c in range(n) if c not in piv]
    if len(livres) != 1:
        return None
    lv = livres[0]
    x = [(0, 1)] * n
    x[lv] = (1, 1)
    for i, c in enumerate(piv):
        x[c] = (-A[i][lv][0], A[i][lv][1])
    den = 1
    for a, b in x:
        den = den * b // N.gcd(den, b)
    ks = [a * den // b for a, b in x]
    g = 0
    for k in ks:
        g = N.gcd(g, k)
    ks = [k // g for k in ks]
    if ks[0] < 0:
        ks = [-k for k in ks]
    if min(ks) <= 0:
        return None
    return ks


def _nr(a, b):
    g = N.gcd(a, b) or 1
    if b < 0:
        a, b = -a, -b
    return (a // g, b // g)


def _mul(x, y):
    return _nr(x[0] * y[0], x[1] * y[1])


def _div(x, y):
    return _nr(x[0] * y[1], x[1] * y[0])


def _sub(x, y):
    return _nr(x[0] * y[1] - y[0] * x[1], x[1] * y[1])
