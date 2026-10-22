# c_fqel.py - M1TR4M: calculadoras de quimica (eletroes nos atomos):
# espetros e fotoes, atomo de hidrogenio e configuracao eletronica.
#@ c_fqel.fot|Espetros e fot\u00f5es|fot\u00e3o energia frequ\u00eancia comprimento de onda espetro eletromagn\u00e9tico e = h f c = lambda f regi\u00e3o cor|F|q2
#@ c_fqel.hid|\u00c1tomo de hidrog\u00e9nio|n\u00edveis de energia transi\u00e7\u00e3o emiss\u00e3o absor\u00e7\u00e3o lyman balmer paschen risca ioniza\u00e7\u00e3o|F|q2
#@ c_fqel.conf|Configura\u00e7\u00e3o eletr\u00f3nica|configura\u00e7\u00e3o eletr\u00f3nica orbitais caixas hund pauli constru\u00e7\u00e3o valencia per\u00edodo grupo|F|q2
# Casos-limite: comprimento de onda nulo ou negativo, n inicial igual ao
# n final (sem transicao), n < 1, ionizacao (n final infinito), Z fora de
# 1 a 36 (o 10.o ano vai ate 4s, Z = 20), cr\u00f3mio e cobre (excecoes).

import m1_nucleo as N

X = N.X
H = 6.63e-34          # J s (valor usado nos manuais)
C = 3.00e8            # m/s (tabela de constantes do exame)
NA = 6.02e23
E1 = 2.18e-18         # J: E(n) = -2,18 x 10^-18 / n^2 (modelo de Bohr)
EV = 1.60e-19         # J por eletrao-volt
REG = ((1e-11, 'raios gama'), (1e-8, 'raios X'), (4e-7, 'ultravioleta'),
       (7e-7, 'vis\u00edvel'), (1e-3, 'infravermelho'), (1.0, 'micro-ondas'),
       (1e99, 'ondas de r\u00e1dio'))
COR = ((450e-9, 'violeta'), (495e-9, 'azul'), (570e-9, 'verde'),
       (590e-9, 'amarelo'), (620e-9, 'laranja'), (700e-9, 'vermelho'))


def regiao(lam):
    # Regiao do espetro (limites aproximados) e cor, se for visivel.
    for lim, nm in REG:
        if lam < lim:
            if nm == 'vis\u00edvel':
                for l2, c in COR:
                    if lam < l2:
                        return 'vis\u00edvel (' + c + ')'
            return nm
    return REG[-1][1]

# ------------------------------------------------------------ fotoes


def fot():
    return ('Espetros e fot\u00f5es',
            [N.fld('Valor conhecido (\u03bb, f ou E)', 'nm m \u00b5m pm Hz THz '
                   'PHz J eV', '500', 'u')], _fot)


def _fot(v):
    x, sf, iu = v[0]
    N.pos(x, 'O valor')
    s = N.sfm(sf, 3)
    o = []
    if iu <= 3:
        lam = x * (1e-9, 1.0, 1e-6, 1e-12)[iu]
        f = C / lam
        e = H * f
        o += ['= f = c / \u03bb = ' + N.q(C, 3, 'm s\u207b\u00b9') + ' / ' +
              N.q(lam, sf, 'm'), N.res('f', f, 'Hz', s)]
        o += ['= E = h f', N.res('E', e, 'J', s)]
    elif iu <= 6:
        f = x * (1.0, 1e12, 1e15)[iu - 4]
        lam = C / f
        e = H * f
        o += ['= \u03bb = c / f', N.res('\u03bb', lam, 'm', s),
              '= E = h f = ' + N.q(H, 3) + ' J s ' + X + ' ' + N.q(f, sf, 'Hz'),
              N.res('E', e, 'J', s)]
    else:
        e = x * (1.0, EV)[iu - 7]
        f = e / H
        lam = C / f
        o += ['= f = E / h', N.res('f', f, 'Hz', s), '= \u03bb = c / f',
              N.res('\u03bb', lam, 'm', s)]
    o.append('\u03bb = ' + N.fmt(lam * 1e9, s) + ' nm')
    o.append('E = ' + N.fmt(e / EV, s) + ' eV por fot\u00e3o')
    o.append('Por mole de fot\u00f5es: ' + N.fmt(e * NA / 1000, s) + ' kJ mol\u207b\u00b9')
    o.append('Regi\u00e3o do espetro: ' + regiao(lam) + ' (limites aproximados)')
    st = 'h = 6,63 ' + X + ' 10\u207b\u00b3\u2074 J s e c = 3,00 ' + X + \
        ' 10\u2078 m s\u207b\u00b9.\nQuanto maior a frequ\u00eancia, maior a ' \
        'energia e menor o comprimento de onda.'
    return ('\n'.join(o), st, e, 'J')

# ------------------------------------------------------------ hidrogenio


def hid():
    return ('\u00c1tomo de hidrog\u00e9nio',
            [N.fld('n inicial', '', '3'),
             N.fld('n final (0 = ioniza\u00e7\u00e3o)', '', '2')], _hid)


def en(n):
    return -E1 / (n * n)


def _hid(v):
    ni, nf = v[0][0], v[1][0]
    N.need(ni == int(ni) and nf == int(nf), 'Os n\u00edveis s\u00e3o n\u00fameros '
           'inteiros (1, 2, 3...)')
    ni, nf = int(ni), int(nf)
    N.need(ni >= 1, 'O n\u00edvel inicial \u00e9 1 ou mais')
    N.need(nf >= 0, 'O n\u00edvel final \u00e9 1 ou mais (0 = ioniza\u00e7\u00e3o)')
    N.need(ni <= 50 and nf <= 50, 'Usa n\u00edveis at\u00e9 50')
    N.need(ni != nf, 'O n\u00edvel inicial e o final s\u00e3o iguais: n\u00e3o h\u00e1 '
           'transi\u00e7\u00e3o')
    ei = en(ni)
    ef = 0.0 if nf == 0 else en(nf)
    d = ef - ei
    o = ['= E\u2099 = -2,18 ' + X + ' 10\u207b\u00b9\u2078 / n\u00b2 J',
         'E(' + str(ni) + ') = ' + N.fmt(ei, 3) + ' J',
         'E(' + ('\u221e' if nf == 0 else str(nf)) + ') = ' +
         N.fmt(ef, 3) + ' J',
         '= \u0394E = E final - E inicial', N.res('\u0394E', d, 'J', 3)]
    if d > 0:
        o.append('Absor\u00e7\u00e3o: o eletr\u00e3o recebe energia (sobe de n\u00edvel).')
        if nf == 0:
            o.append('n final = \u221e: \u00e9 a energia de ioniza\u00e7\u00e3o a partir de '
                     'n = ' + str(ni) + '.')
    else:
        o.append('Emiss\u00e3o: o \u00e1tomo emite um fot\u00e3o (o eletr\u00e3o desce).')
    e = abs(d)
    lam = H * C / e
    o.append('Fot\u00e3o: E = ' + N.fmt(e, 3) + ' J; \u03bb = ' +
             N.fmt(lam * 1e9, 3) + ' nm')
    o.append('Regi\u00e3o: ' + regiao(lam))
    lo = min(ni, nf) if nf else ni
    if nf != 0:
        ser = {1: 'Lyman (UV)', 2: 'Balmer (vis\u00edvel e UV)',
               3: 'Paschen (IV)'}.get(lo, '')
        if ser:
            o.append('S\u00e9rie de ' + ser + ': n\u00edvel mais baixo n = ' + str(lo))
    st = 'O \u00e1tomo s\u00f3 absorve ou emite fot\u00f5es com energia igual \u00e0 ' \
        'diferen\u00e7a entre dois n\u00edveis: a energia est\u00e1 quantizada.\n' \
        '\u03bb = h c / E.'
    return ('\n'.join(o), st, d, 'J')

# ------------------------------------------------------------ configuracao
ORB = ('1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p')
CAP = (2, 2, 6, 2, 6, 2, 10, 6)
SIMB = ('H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg',
        'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr',
        'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr')


def config(z):
    o = []
    r = z
    for i in range(len(ORB)):
        if r <= 0:
            break
        n = min(r, CAP[i])
        o.append([ORB[i], n])
        r -= n
    if z in (24, 29):
        for x in o:
            if x[0] == '4s':
                x[1] = 1
            if x[0] == '3d':
                x[1] += 1
    return o


def caixas(o):
    # Diagrama de caixas com a Regra de Hund (um eletrao em cada orbital
    # antes de emparelhar).
    s = []
    for orb, n in o:
        k = {'s': 1, 'p': 3, 'd': 5}[orb[1]]
        cx = []
        for i in range(k):
            e = (1 if n > i else 0) + (1 if n > i + k else 0)
            cx.append('[' + ('\u2191\u2193' if e == 2 else ('\u2191 ' if e == 1
                                                           else '  ')) + ']')
        s.append(orb + ' ' + ''.join(cx))
    return s


def conf():
    return ('Configura\u00e7\u00e3o eletr\u00f3nica',
            [N.fld('N\u00famero at\u00f3mico Z (1 a 36)', '', '8'),
             N.fld('Carga do i\u00e3o (0 = \u00e1tomo)', '', '0')], _conf)


def _conf(v):
    z, q = v[0][0], v[1][0]
    N.need(z == int(z) and 1 <= z <= 36, 'Escreve um Z inteiro de 1 a 36')
    N.need(q == int(q), 'A carga \u00e9 um n\u00famero inteiro (ex.: 2 ou -1)')
    z, q = int(z), int(q)
    ne = z - q
    N.need(0 <= ne <= 36, 'Esse i\u00e3o teria ' + str(ne) + ' eletr\u00f5es')
    if ne == 0:
        return ('Sem eletr\u00f5es (\u00e9 s\u00f3 o n\u00facleo).', '', None, '')
    o = config(ne)
    if q > 0 and z > 20:
        # Nos ioes dos metais de transicao saem primeiro os eletroes 4s.
        o = config(z)
        r = q
        for x in o:
            if x[0] == '4s':
                t = min(r, x[1])
                x[1] -= t
                r -= t
        for x in o[::-1]:
            if r and x[0] == '3d':
                t = min(r, x[1])
                x[1] -= t
                r -= t
        o = [x for x in o if x[1]]
    nome = SIMB[z - 1] + (N.sup(abs(q)) if abs(q) > 1 else '') + \
        ('\u207a' if q > 0 else ('\u207b' if q < 0 else ''))
    t = [nome + ' (Z = ' + str(z) + ', ' + str(ne) + ' eletr\u00f5es)',
         '> ' + ' '.join([x[0] + N.sup(x[1]) for x in o])]
    t += caixas(o)
    des = 0
    for orb, n in o:
        k = {'s': 1, 'p': 3, 'd': 5}[orb[1]]
        des += n if n <= k else 2 * k - n
    t.append('Eletr\u00f5es desemparelhados: ' + str(des))
    if q == 0 and z <= 20:
        nmax = max([int(x[0][0]) for x in o])
        val = sum([x[1] for x in o if int(x[0][0]) == nmax])
        g = val if val <= 2 else val + 10
        if z == 2:
            g = 18
        t.append('Eletr\u00f5es de val\u00eancia: ' + str(val))
        t.append('Posi\u00e7\u00e3o: per\u00edodo ' + str(nmax) + ', grupo ' + str(g) +
                 ', bloco ' + o[-1][0][1])
    if ne > 20:
        t.append('(Al\u00e9m do programa do 10.\u00ba ano, que vai at\u00e9 4s.)')
    if z in (24, 29) and q == 0:
        t.append('Exce\u00e7\u00e3o: ' + SIMB[z - 1] + ' fica com 4s\u00b9 (mais est\u00e1vel).')
    st = 'Princ\u00edpio da Constru\u00e7\u00e3o: as orbitais enchem-se por ordem de ' \
        'energia: 1s 2s 2p 3s 3p 4s 3d 4p.\nPrinc\u00edpio de Exclus\u00e3o de ' \
        'Pauli: no m\u00e1ximo 2 eletr\u00f5es por orbital, com spins opostos.\n' \
        'Regra de Hund: nas orbitais com a mesma energia, primeiro um ' \
        'eletr\u00e3o em cada uma, com o mesmo spin.'
    return ('\n'.join(t), st, None, '')
