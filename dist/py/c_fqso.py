# c_fqso.py - M1TR4M: calculadoras de solucoes e gases: concentracao,
# massa a pesar, percentagens e ppm, diluicao e gases em PTN.
#@ c_fqso.con|Concentra\u00e7\u00e3o de uma solu\u00e7\u00e3o|concentra\u00e7\u00e3o molar concentra\u00e7\u00e3o m\u00e1ssica soluto solu\u00e7\u00e3o volume mol dm3 g dm3|F|q5
#@ c_fqso.pes|Massa de soluto a pesar|preparar solu\u00e7\u00e3o massa a pesar bal\u00e3o volum\u00e9trico concentra\u00e7\u00e3o pretendida|F|q5
#@ c_fqso.per|Percentagem e partes por milh\u00e3o|percentagem em massa percentagem em volume ppm partes por milh\u00e3o composi\u00e7\u00e3o|F|q5
#@ c_fqso.dil|Dilui\u00e7\u00e3o de solu\u00e7\u00f5es|dilui\u00e7\u00e3o fator de dilui\u00e7\u00e3o ci vi cf vf solu\u00e7\u00e3o m\u00e3e|F|q5
#@ c_fqso.gas|Gases (PTN)|gases volume molar massa vol\u00famica densidade ptn lei de avogadro|F|q5
# Casos-limite: volume zero ou negativo, massa do soluto maior do que a
# da solucao, diluicao com cf > ci (seria concentrar), campos a mais ou
# a menos na diluicao e nos gases, percentagens acima de 100 %.

import m1_nucleo as N

X = N.X
VM = 22.4                 # dm3/mol (PTN, tabela de constantes do exame)
VS = 'dm\u00b3 L mL cm\u00b3'
MS = 'g mg kg'


def con():
    return ('Concentra\u00e7\u00e3o de uma solu\u00e7\u00e3o',
            [N.fld('Massa de soluto m (opcional)', MS, '', 'o'),
             N.fld('Massa molar M em g/mol (opcional)', '', '', 'o'),
             N.fld('Quantidade de soluto n (opcional)', 'mol mmol', '', 'o'),
             N.fld('Volume da solu\u00e7\u00e3o V', VS, '0,250')], _con)


def _con(v):
    m, M, n, V = v
    N.pos(V[0], 'O volume')
    N.need(m is not None or n is not None, 'Escreve a massa ou a quantidade '
           'de soluto')
    o = []
    s = V[1]
    q = None
    if n is None and m is not None and M is not None:
        N.pos(M[0], 'A massa molar')
        q = m[0] / M[0]
        sn = N.sfm(m[1], M[1])
        o += ['= n = m / M = ' + N.q(m[0], m[1], 'g') + ' / ' +
              N.q(M[0], M[1], 'g mol\u207b\u00b9'), N.res('n', q, 'mol', sn)]
        s = N.sfm(sn, V[1])
    elif n is not None:
        N.pos(n[0], 'A quantidade')
        q = n[0]
        s = N.sfm(n[1], V[1])
    if q is not None:
        c = q / V[0]
        o += ['= c = n / V', N.res('c', c, 'mol dm\u207b\u00b3', s)]
    if m is not None:
        N.pos(m[0], 'A massa')
        cm = m[0] / V[0]
        o += ['= c\u2098 = m / V = ' + N.q(m[0], m[1], 'g') + ' / ' +
              N.q(V[0], V[1], 'dm\u00b3'),
              N.res('c\u2098', cm, 'g dm\u207b\u00b3', N.sfm(m[1], V[1]))]
    elif q is not None and M is not None:
        o += ['= c\u2098 = c ' + X + ' M',
              N.res('c\u2098', q / V[0] * M[0], 'g dm\u207b\u00b3',
                    N.sfm(s, M[1]))]
    st = 'c em mol dm\u207b\u00b3 e c\u2098 em g dm\u207b\u00b3, com V em dm\u00b3 ' \
        '(1 dm\u00b3 = 1 L = 1000 mL).\nc\u2098 = c ' + X + ' M.'
    return ('\n'.join(o), st, q / V[0] if q is not None else None,
            'mol/dm\u00b3')


def pes():
    return ('Massa de soluto a pesar',
            [N.fld('Concentra\u00e7\u00e3o pretendida c (mol/dm\u00b3)', '', '0,100'),
             N.fld('Volume do bal\u00e3o V', 'mL ' + VS.replace(' mL', ''),
                   '250'),
             N.fld('Massa molar M (g/mol)', '', '58,44')], _pes)


def _pes(v):
    c, V, M = v
    N.pos(c[0], 'A concentra\u00e7\u00e3o')
    N.pos(V[0], 'O volume')
    N.pos(M[0], 'A massa molar')
    Vd = V[0] / 1000.0
    n = c[0] * Vd
    m = n * M[0]
    s = N.sfm(c[1], V[1], M[1])
    o = ['= n = c ' + X + ' V = ' + N.q(c[0], c[1], 'mol dm\u207b\u00b3') + ' ' +
         X + ' ' + N.q(Vd, V[1], 'dm\u00b3'), N.res('n', n, 'mol', s),
         '= m = n ' + X + ' M', N.res('m', m, 'g', s),
         'Pesa ' + N.fsf(m, max(1, s or 3)) + ' g de soluto, dissolve num '
         'pouco de \u00e1gua e completa o bal\u00e3o at\u00e9 ao tra\u00e7o.']
    return ('\n'.join(o), 'Primeiro a quantidade de mat\u00e9ria, depois a massa.',
            m, 'g')


def per():
    return ('Percentagem e ppm',
            [N.fld('Calcular', '', '', 'c', ['% em massa (m/m)',
                                            '% em volume (V/V)',
                                            'ppm em massa (mg/kg)']),
             N.fld('Soluto (massa ou volume)', '', ''),
             N.fld('Solu\u00e7\u00e3o (mesma unidade)', '', '')], _per)


def _per(v):
    k, a, b = v
    N.pos(a[0], 'O soluto')
    N.pos(b[0], 'A solu\u00e7\u00e3o')
    N.need(a[0] <= b[0], 'O soluto n\u00e3o pode ser mais do que a solu\u00e7\u00e3o')
    s = N.sfm(a[1], b[1])
    if k == 2:
        p = a[0] / b[0] * 1e6
        o = ['= ppm = m(soluto) / m(solu\u00e7\u00e3o) ' + X + ' 10\u2076',
             N.res('ppm', p, '', s),
             '1 ppm = 1 mg de soluto por kg de solu\u00e7\u00e3o.']
    else:
        nm = '% (m/m)' if k == 0 else '% (V/V)'
        p = a[0] / b[0] * 100
        o = ['= ' + nm + ' = soluto / solu\u00e7\u00e3o ' + X + ' 100',
             N.res(nm, p, '%', s)]
    return ('\n'.join(o), 'As duas grandezas t\u00eam de estar na mesma '
            'unidade.', p, '%' if k < 2 else 'ppm')


def dil():
    return ('Dilui\u00e7\u00e3o',
            [N.fld('c inicial (mol/dm\u00b3), vazio = calcular', '', '', 'o'),
             N.fld('V inicial', 'mL dm\u00b3 L', '', 'o'),
             N.fld('c final (mol/dm\u00b3)', '', '', 'o'),
             N.fld('V final', 'mL dm\u00b3 L', '', 'o')], _dil)


def _dil(v):
    ci, vi, cf, vf = v
    falta = [i for i in range(4) if v[i] is None]
    N.need(len(falta) == 1, 'Deixa vazio s\u00f3 o campo que queres calcular')
    for x, nm in ((ci, 'c inicial'), (vi, 'V inicial'), (cf, 'c final'),
                  (vf, 'V final')):
        if x is not None:
            N.pos(x[0], nm)
    s = N.sfm(*[x[1] for x in v if x is not None])
    k = falta[0]
    o = ['= ci ' + X + ' Vi = cf ' + X + ' Vf']
    if k == 0:
        r = cf[0] * vf[0] / vi[0]
        o.append(N.res('c inicial', r, 'mol dm\u207b\u00b3', s))
        ci = (r, s)
    elif k == 1:
        r = cf[0] * vf[0] / ci[0]
        o.append(N.res('V inicial', r, 'mL', s))
        vi = (r, s)
    elif k == 2:
        r = ci[0] * vi[0] / vf[0]
        o.append(N.res('c final', r, 'mol dm\u207b\u00b3', s))
        cf = (r, s)
    else:
        r = ci[0] * vi[0] / cf[0]
        o.append(N.res('V final', r, 'mL', s))
        vf = (r, s)
    N.need(cf[0] <= ci[0] * (1 + 1e-9), 'c final maior do que c inicial: '
           'isso n\u00e3o \u00e9 uma dilui\u00e7\u00e3o')
    f = vf[0] / vi[0]
    o.append('Fator de dilui\u00e7\u00e3o: f = Vf / Vi = ci / cf ' +
             N.eq(f, s))
    o.append('Volumes em mL (os dois na mesma unidade).')
    return ('\n'.join(o), 'Na dilui\u00e7\u00e3o a quantidade de soluto n\u00e3o '
            'muda: n = ci Vi = cf Vf.', r, '')


def gas():
    return ('Gases em PTN',
            [N.fld('Massa molar M (g/mol)', '', ''),
             N.fld('Massa m (opcional)', MS, '', 'o'),
             N.fld('Quantidade n (opcional)', 'mol mmol', '', 'o'),
             N.fld('Volume V (opcional)', VS, '', 'o')], _gas)


def _gas(v):
    M, m, n, V = v
    N.pos(M[0], 'A massa molar')
    rho = M[0] / VM
    s0 = N.sfm(M[1], 3)
    o = ['= \u03c1 = M / V\u2098 = ' + N.q(M[0], M[1], 'g mol\u207b\u00b9') + ' / 22,4 '
         'dm\u00b3 mol\u207b\u00b9', N.res('\u03c1', rho, 'g dm\u207b\u00b3', s0)]
    ds = [x for x in (m, n, V) if x is not None]
    N.need(len(ds) <= 1, 'Preenche no m\u00e1ximo um de m, n ou V')
    if ds:
        if m is not None:
            N.pos(m[0], 'A massa')
            q = m[0] / M[0]
            s = N.sfm(m[1], M[1])
        elif n is not None:
            N.pos(n[0], 'A quantidade')
            q = n[0]
            s = N.sfm(n[1])
        else:
            N.pos(V[0], 'O volume')
            q = V[0] / VM
            s = N.sfm(V[1], 3)
        o += ['n = ' + N.q(q, s, 'mol'), 'm = n ' + X + ' M = ' +
              N.q(q * M[0], N.sfm(s, M[1]), 'g'),
              'V = n ' + X + ' V\u2098 = ' + N.q(q * VM, N.sfm(s, 3), 'dm\u00b3')]
    o.append('Ar seco: \u03c1 \u2248 1,29 g dm\u207b\u00b3 em PTN (M \u2248 28,97 g mol\u207b\u00b9).')
    o.append('Gases com M maior do que a do ar s\u00e3o mais densos.')
    st = 'Lei de Avogadro: volumes iguais de gases, \u00e0 mesma press\u00e3o e ' \
        'temperatura, t\u00eam a mesma quantidade de mat\u00e9ria.\nEm PTN (0 \u00b0C e ' \
        '1 atm), V\u2098 = 22,4 dm\u00b3 mol\u207b\u00b9.'
    return ('\n'.join(o), st, rho, 'g/dm\u00b3')
