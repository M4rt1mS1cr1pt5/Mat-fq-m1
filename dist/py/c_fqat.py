# c_fqat.py - M1TR4M: calculadoras de quimica (atomos e quantidade de
# materia): massa molar, quantidade de materia, massa atomica relativa
# media e fracao molar/massica.
#@ c_fqat.mm|Massa molar|massa molar f\u00f3rmula qu\u00edmica composi\u00e7\u00e3o percentagem em massa hidratos|F|q1
#@ c_fqat.qm|Quantidade de mat\u00e9ria|quantidade de mat\u00e9ria mol massa n\u00famero de part\u00edculas avogadro volume molar|F|q1
#@ c_fqat.ar|Massa at\u00f3mica relativa m\u00e9dia|is\u00f3topos abund\u00e2ncia massa at\u00f3mica relativa m\u00e9dia|F|q1
#@ c_fqat.fr|Fra\u00e7\u00e3o molar e fra\u00e7\u00e3o m\u00e1ssica|fra\u00e7\u00e3o molar fra\u00e7\u00e3o m\u00e1ssica mistura composi\u00e7\u00e3o|F|q1
# Casos-limite: maiusculas erradas (Co e cobalto, CO e monoxido de
# carbono), parenteses por fechar, hidratos (CuSO4.5H2O), ioes (SO4^2-),
# elemento desconhecido; nenhum ou varios dados na quantidade de
# materia; abundancias que nao somam 100 %; listas de tamanhos diferentes.

import m1_nucleo as N

X = N.X
NA = 6.02e23          # tabela de constantes do exame (3 alg. sig.)
VM = 22.4             # dm3/mol, gases em PTN (3 alg. sig.)
SUB = '\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089'
# --- dados (gerado) ---
AR = "H 1.01 He 4.00 Li 6.94 Be 9.01 B 10.81 C 12.01 N 14.01 O 16.00 F 19.00 Ne 20.18 Na 22.99 Mg 24.31 Al 26.98 Si\
 28.09 P 30.97 S 32.06 Cl 35.45 Ar 39.95 K 39.10 Ca 40.08 Sc 44.96 Ti 47.87 V 50.94 Cr 52.00 Mn 54.94 Fe\
 55.85 Co 58.93 Ni 58.69 Cu 63.55 Zn 65.38 Ga 69.72 Ge 72.63 As 74.92 Se 78.97 Br 79.90 Kr 83.80 Rb 85.47 Sr\
 87.62 Y 88.91 Zr 91.22 Nb 92.91 Mo 95.95 Tc 98 Ru 101.07 Rh 102.91 Pd 106.42 Ag 107.87 Cd 112.41 In 114.82\
 Sn 118.71 Sb 121.76 Te 127.60 I 126.90 Xe 131.29 Cs 132.91 Ba 137.33 La 138.91 Ce 140.12 Pr 140.91 Nd 144.24\
 Pm 145 Sm 150.36 Eu 151.96 Gd 157.25 Tb 158.93 Dy 162.50 Ho 164.93 Er 167.26 Tm 168.93 Yb 173.05 Lu 174.97\
 Hf 178.49 Ta 180.95 W 183.84 Re 186.21 Os 190.23 Ir 192.22 Pt 195.08 Au 196.97 Hg 200.59 Tl 204.38 Pb 207.20\
 Bi 208.98 Po 209 At 210 Rn 222 Fr 223 Ra 226 Ac 227 Th 232.04 Pa 231.04 U 238.03 Np 237 Pu 244 Am 243 Cm 247\
 Bk 247 Cf 251 Es 252 Fm 257 Md 258 No 259 Lr 262 Rf 267 Db 268 Sg 269 Bh 270 Hs 269 Mt 278 Ds 281 Rg 282 Cn\
 285 Nh 286 Fl 289 Mc 290 Lv 293 Ts 294 Og 294"
# --- fim dos dados ---
_T = {}


def ar_of(s):
    # Ar com 2 casas (texto como na tabela do exame) de um simbolo.
    if not _T:
        p = AR.split(' ')
        for i in range(0, len(p) - 1, 2):
            _T[p[i]] = p[i + 1]
    return _T.get(s)


def _num(p, i):
    j = i
    while j < len(p) and N.dig(p[j]):
        j += 1
    return (int(p[i:j]) if j > i else 1), j


def norm(s):
    # Indices em baixo -> digitos; ponto dos hidratos; carga separada.
    o = []
    for c in s:
        k = SUB.find(c)
        o.append(str(k) if k >= 0 else c)
    s = ''.join(o).replace(' ', '').replace('\u00b7', '.').replace('*', '.')
    ch = ''
    k = s.find('^')
    if k >= 0:
        ch = s[k + 1:]
        s = s[:k]
    else:
        e = len(s)
        while e > 0 and s[e - 1] in '\u207a\u207b\u00b2\u00b3\u00b9\u2074':
            e -= 1
        if e < len(s):
            ch = N.P.vis(s[e:], 0).lstrip('^')
            s = s[:e]
        elif s.endswith('+') or s.endswith('-'):
            ch = s[-1]
            s = s[:-1]
    return s, ch


def parse(s):
    # Formula -> lista [(simbolo, quantos)] pela ordem em que aparecem.
    f, ch = norm(s)
    N.need(f != '', 'Escreve uma f\u00f3rmula qu\u00edmica, por exemplo H2SO4')
    tot = []
    for part in f.split('.'):
        if part == '':
            N.err('Falta a parte depois do ponto (ex.: CuSO4.5H2O)')
        co, i = _num(part, 0)
        st = [[]]
        p = part
        while i < len(p):
            c = p[i]
            if c in '([':
                st.append([])
                i += 1
            elif c in ')]':
                N.need(len(st) > 1, 'Par\u00eantese a mais')
                g = st.pop()
                k, i = _num(p, i + 1)
                for a, b in g:
                    st[-1].append((a, b * k))
            elif 'A' <= c <= 'Z':
                sy = c
                i += 1
                if i < len(p) and 'a' <= p[i] <= 'z':
                    sy += p[i]
                    i += 1
                N.need(ar_of(sy) is not None, 'Elemento desconhecido: ' + sy +
                       ' (Co \u00e9 cobalto; CO \u00e9 carbono + oxig\u00e9nio)')
                k, i = _num(p, i)
                st[-1].append((sy, k))
            elif 'a' <= c <= 'z':
                N.err('Os s\u00edmbolos come\u00e7am por mai\u00fascula: ' + c)
            else:
                N.err('S\u00edmbolo desconhecido na f\u00f3rmula: ' + c)
        N.need(len(st) == 1, 'Falta fechar um par\u00eantese')
        for a, b in st[0]:
            for x in tot:
                if x[0] == a:
                    x[1] += b * co
                    break
            else:
                tot.append([a, b * co])
    return tot, ch


def pretty(s):
    # "H2SO4" -> "H\u2082SO\u2084" (os coeficientes dos hidratos ficam normais).
    f, ch = norm(s)
    o = []
    idx = False
    for c in f:
        if N.dig(c):
            o.append(SUB[ord(c) - 48] if idx else c)
        else:
            idx = c.isalpha() or c in ')]'
            o.append('\u00b7' if c == '.' else c)
    if ch:
        if len(ch) > 1 and ch[:-1].isdigit():
            o.append(N.sup(int(ch[:-1])))
        o.append('\u207a' if ch.endswith('+') else '\u207b')
    return ''.join(o)


# ------------------------------------------------------------ massa molar


def mm():
    return ('Massa molar', [N.fld('F\u00f3rmula qu\u00edmica (ex.: H2SO4, '
                                  'CuSO4.5H2O)', '', 'H2O', 't')], _mm)


def _mm(v):
    tot, ch = parse(v[0])
    pf = pretty(v[0])
    M = 0.0
    a = []
    b = []
    for s, n in tot:
        t = ar_of(s)
        M += n * N._fl(t)
        a.append((str(n) + ' ' + X + ' ' if n > 1 else '') + 'Ar(' + s + ')')
        b.append((str(n) + ' ' + X + ' ' if n > 1 else '') + t.replace('.', ','))
    o = ['= M(' + pf + ') = ' + ' + '.join(a),
         '= M = ' + ' + '.join(b),
         N.res('M', M, 'g mol\u207b\u00b9', 0, 2), 'Composi\u00e7\u00e3o (% em massa):']
    for s, n in tot:
        w = n * N._fl(ar_of(s)) / M * 100
        o.append('- ' + s + ': ' + N.fix(w, 2) + ' %')
    if ch:
        o.append('A carga (' + ch + ') n\u00e3o muda a massa molar: a massa '
                 'dos eletr\u00f5es \u00e9 desprez\u00e1vel.')
    st = 'Ar com 2 casas decimais, como na tabela peri\u00f3dica do exame.\n' \
        'A massa molar em g/mol tem o mesmo valor que a massa molecular ' \
        'relativa Mr.'
    return ('\n'.join(o), st, M, 'g/mol')

# ------------------------------------------------------------ quantidade


def qm():
    return ('Quantidade de mat\u00e9ria',
            [N.fld('Massa molar M (g/mol, se usas a massa)', '', '', 'o'),
             N.fld('Massa m', 'g kg mg', '', 'o'),
             N.fld('Quantidade n', 'mol mmol', '', 'o'),
             N.fld('N.\u00ba de part\u00edculas N', '', '', 'o'),
             N.fld('Volume de g\u00e1s em PTN V', 'dm\u00b3 L mL cm\u00b3 m\u00b3', '', 'o')],
            _qm)


def _qm(v):
    Mm, m, n, Np, V = v
    dados = [x for x in (m, n, Np, V) if x is not None]
    N.need(len(dados) == 1, 'Preenche s\u00f3 um dos campos m, n, N ou V '
           '(e M se usares a massa)')
    o = []
    if m is not None:
        N.need(Mm is not None, 'Para usar a massa, escreve a massa molar M')
        N.pos(m[0], 'A massa')
        N.pos(Mm[0], 'A massa molar')
        s = N.sfm(m[1], Mm[1])
        q = m[0] / Mm[0]
        o += ['= n = m / M', '= n = ' + N.q(m[0], m[1], 'g') + ' / ' +
              N.q(Mm[0], Mm[1], 'g mol\u207b\u00b9'), N.res('n', q, 'mol', s)]
    elif n is not None:
        N.pos(n[0], 'A quantidade')
        q = n[0]
        s = N.sfm(n[1])
        o.append('n = ' + N.q(q, s, 'mol'))
    elif Np is not None:
        N.pos(Np[0], 'O n\u00famero de part\u00edculas')
        s = N.sfm(Np[1], 3)
        q = Np[0] / NA
        o += ['= n = N / NA', '= n = ' + N.q(Np[0], Np[1]) + ' / ' +
              N.q(NA, 3, 'mol\u207b\u00b9'), N.res('n', q, 'mol', s)]
    else:
        N.pos(V[0], 'O volume')
        s = N.sfm(V[1], 3)
        q = V[0] / VM
        o += ['= n = V / Vm', '= n = ' + N.q(V[0], V[1], 'dm\u00b3') + ' / ' +
              N.q(VM, 3, 'dm\u00b3 mol\u207b\u00b9'), N.res('n', q, 'mol', s)]
    if m is None and Mm is not None:
        s2 = N.sfm(s, Mm[1])
        o += ['= m = n ' + X + ' M', N.res('m', q * Mm[0], 'g', s2)]
    if Np is None:
        o += ['= N = n ' + X + ' NA = ' + N.q(q, s) + ' ' + X + ' ' +
              N.q(NA, 3), N.res('N', q * NA, '', N.sfm(s, 3))]
    if V is None:
        o += ['= V = n ' + X + ' Vm (s\u00f3 para gases em PTN)',
              N.res('V', q * VM, 'dm\u00b3', N.sfm(s, 3))]
    st = 'NA = 6,02 ' + X + ' 10\u00b2\u00b3 mol\u207b\u00b9 e Vm = 22,4 dm\u00b3 ' \
        'mol\u207b\u00b9 (tabela de constantes do exame; 3 alg. sig.).\n' \
        'O resultado tem os algarismos significativos do dado com menos.'
    return ('\n'.join(o), st, q, 'mol')

# ------------------------------------------------------------ Ar media


def ar():
    return ('Massa at\u00f3mica relativa m\u00e9dia',
            [N.fld('Massas isot\u00f3picas relativas', '', '', 'l'),
             N.fld('Abund\u00e2ncias em %', '', '', 'l')], _ar)


def _ar(v):
    ms, ab = v
    N.need(len(ms) == len(ab), 'Escreve tantas abund\u00e2ncias como massas')
    N.need(len(ms) >= 1, 'Escreve pelo menos um is\u00f3topo')
    s = sum([a[0] for a in ab])
    for a in ab:
        N.need(a[0] >= 0, 'As abund\u00e2ncias n\u00e3o podem ser negativas')
    N.need(s > 0, 'As abund\u00e2ncias somam 0 %')
    r = sum([ms[i][0] * ab[i][0] for i in range(len(ms))]) / s
    sf = N.sfm(*([x[1] for x in ms] + [x[1] for x in ab]))
    t = ' + '.join([N.q(ms[i][0], ms[i][1]) + ' ' + X + ' ' +
                    N.q(ab[i][0], ab[i][1]) for i in range(len(ms))])
    o = ['= Ar m\u00e9dio = \u03a3 (Ar(i) ' + X + ' abund\u00e2ncia(i)) / 100',
         '= Ar m\u00e9dio = (' + t + ') / 100', N.res('Ar m\u00e9dio', r, '', sf)]
    if abs(s - 100) > 0.1:
        o.append('! As abund\u00e2ncias somam ' + N.fmt(s, 0, 3) + ' % (e n\u00e3o '
                 '100 %): dividi pela soma. Confirma os dados.')
    return ('\n'.join(o), 'A massa at\u00f3mica relativa m\u00e9dia \u00e9 a m\u00e9dia '
            'pesada das massas dos is\u00f3topos.', r, '')

# ------------------------------------------------------------ fracoes


def fr():
    return ('Fra\u00e7\u00e3o molar e m\u00e1ssica',
            [N.fld('Tipo', '', '', 'c', ['fra\u00e7\u00e3o molar (n em mol)',
                                         'fra\u00e7\u00e3o m\u00e1ssica (m em g)']),
             N.fld('Quantidades ou massas', '', '', 'l'),
             N.fld('Nomes dos componentes (opcional)', '', '', 't')], _fr)


def _fr(v):
    tp, xs, nm = v
    N.need(len(xs) >= 2, 'Uma mistura tem pelo menos 2 componentes')
    for x in xs:
        N.need(x[0] >= 0, 'Os valores n\u00e3o podem ser negativos')
    tot = sum([x[0] for x in xs])
    N.need(tot > 0, 'O total \u00e9 zero')
    ns = [x for x in nm.replace(';', ' ').split(' ') if x] if nm else []
    sy = 'x' if tp == 0 else 'w'
    o = ['= ' + sy + '(i) = ' + ('n(i) / n total' if tp == 0 else
                                    'm(i) / m total'),
         'Total = ' + N.fmt(tot, 0, 6) + (' mol' if tp == 0 else ' g')]
    sf = N.sfm(*[x[1] for x in xs])
    for i in range(len(xs)):
        lab = ns[i] if i < len(ns) and ns[i] else 'componente ' + str(i + 1)
        f = xs[i][0] / tot
        o.append('> ' + sy + '(' + lab + ') ' + N.eq(f, sf) + ' (' +
                 N.fix(f * 100, 2) + ' %)')
    o.append('A soma das fra\u00e7\u00f5es \u00e9 1 (100 %).')
    return ('\n'.join(o), '', xs[0][0] / tot, '')
