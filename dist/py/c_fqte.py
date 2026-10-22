# c_fqte.py - M1TR4M: calculadoras de fenomenos termicos e radiacao:
# capacidade termica massica, mudanca de estado, temperatura de
# equilibrio, conducao, Primeira Lei e paineis fotovoltaicos.
#@ c_fqte.cal|Capacidade t\u00e9rmica m\u00e1ssica (Q = m c \u0394T)|capacidade t\u00e9rmica m\u00e1ssica calor energia aquecimento varia\u00e7\u00e3o de temperatura \u00e1gua|F|f3
#@ c_fqte.est|Mudan\u00e7a de estado (Q = m \u0394H)|mudan\u00e7a de estado fus\u00e3o vaporiza\u00e7\u00e3o entalpia gelo \u00e1gua ebuli\u00e7\u00e3o|F|f3
#@ c_fqte.eq|Temperatura de equil\u00edbrio de uma mistura|temperatura de equil\u00edbrio mistura balan\u00e7o energ\u00e9tico sistema isolado gelo|F|f3
#@ c_fqte.cond|Condu\u00e7\u00e3o t\u00e9rmica (P = k A \u0394T / \u2113)|condu\u00e7\u00e3o condutividade t\u00e9rmica isolamento parede janela fluxo|F|f3
#@ c_fqte.pl|Primeira Lei da Termodin\u00e2mica|primeira lei energia interna trabalho calor radia\u00e7\u00e3o sistema|F|f3
#@ c_fqte.pv|Painel fotovoltaico e irradi\u00e2ncia|irradi\u00e2ncia radia\u00e7\u00e3o painel fotovoltaico pot\u00eancia el\u00e9trica rendimento sol|F|f3
# Casos-limite: massas, areas e espessuras nulas ou negativas, mesma
# temperatura inicial e final (calor nulo), campos a mais ou a menos,
# gelo que nao funde todo, rendimento acima de 100 %.

import math
import m1_nucleo as N

X = N.X
MS = 'kg g'
TS = '\u00b0C K'
QS = 'J kJ MJ'
CU = 'J kg\u207b\u00b9 K\u207b\u00b9'
# Capacidades termicas massicas (J/(kg K), valores tabelados a ~25 C):
CMAT = ('\u00e1gua|4.18e3 gelo|2.1e3 alum\u00ednio|9.0e2 ferro|4.5e2 '
        'cobre|3.9e2 chumbo|1.3e2')
HF = 3.34e5     # J/kg, fusao do gelo (0 C)
HV = 2.26e6     # J/kg, vaporizacao da agua (100 C)
CA = 4.18e3     # J/(kg K), agua liquida


def um(v, nome):
    f = [i for i in range(len(v)) if v[i] is None]
    N.need(len(f) == 1, 'Deixa vazio s\u00f3 o campo que queres calcular (' +
           nome + ')')
    return f[0]


def dec(x):
    # Casas decimais com que um dado (valor, alg. sig.) foi escrito.
    if x[0] == 0:
        return x[1] - 1
    return x[1] - 1 - int(math.floor(math.log10(abs(x[0])) + 1e-12))


def sfdif(a, b, d):
    # Alg. sig. de d = b - a pela regra da soma (casas decimais).
    if not (a[1] and b[1]):
        return 0
    if d == 0:
        return 1
    e = int(math.floor(math.log10(abs(d)) + 1e-12))
    return max(1, e + 1 + min(dec(a), dec(b)))


def mat(t, k):
    # (nome, valor) da tabela "nome|valor nome|valor"; k comeca em 1.
    p = t.split(' ')[k - 1].split('|')
    return p[0], float(p[1])

# ------------------------------------------------------------ Q = m c dT


def cal():
    return ('Capacidade t\u00e9rmica m\u00e1ssica',
            [N.fld('Material', '', '', 'c', ['escrevo c'] +
                   [x.split('|')[0] for x in CMAT.split(' ')]),
             N.fld('Energia Q', QS, '', 'o'),
             N.fld('Massa m', MS, '', 'o'),
             N.fld('c (J kg\u207b\u00b9 K\u207b\u00b9)', '', '', 'o'),
             N.fld('Temperatura inicial \u03b8i', TS, '', 'o'),
             N.fld('Temperatura final \u03b8f', TS, '', 'o')], _cal)


def _cal(v):
    k0, Q, m, c, ti, tf = v
    if k0:
        N.need(c is None, 'Escolheste um material: deixa c vazio')
        nm, x = mat(CMAT, k0)
        c = (x, 2 if x < 4e3 else 3)
    w = [Q, m, c, ti, tf]
    k = um(w, 'Q, m, c, \u03b8i ou \u03b8f')
    for x, t in ((m, 'A massa'), (c, 'A capacidade t\u00e9rmica m\u00e1ssica')):
        if x is not None:
            N.pos(x[0], t)
    if ti is not None and tf is not None:
        dt = tf[0] - ti[0]
        s = N.sfm(N.sfv(Q, m, c), sfdif(ti, tf, dt))
    else:
        s = N.sfv(Q, m, c, ti, tf)
    o = ['= Q = m c \u0394T']
    if k0:
        o.append('c(' + nm + ') = ' + N.q(c[0], c[1], CU))
    if k == 0:
        N.need(dt != 0, 'Temperatura igual no in\u00edcio e no fim: Q = 0')
        r = m[0] * c[0] * dt
        o += ['\u0394T = ' + N.fmt(dt) + ' K (igual a \u0394\u03b8 em \u00b0C)',
              N.res('Q', r, 'J', s)]
        o.append('Q > 0: o corpo recebe energia.' if r > 0 else
                 'Q < 0: o corpo cede energia.')
        u = 'J'
    elif k == 1:
        N.need(dt != 0, 'Com \u0394T = 0 n\u00e3o d\u00e1 para calcular a massa')
        r = Q[0] / (c[0] * dt)
        N.need(r > 0, 'Sinais incoerentes: se o corpo aquece, Q > 0')
        o += ['m = Q / (c \u0394T)', N.res('m', r, 'kg', s)]
        u = 'kg'
    elif k == 2:
        N.need(dt != 0, 'Com \u0394T = 0 n\u00e3o d\u00e1 para calcular c')
        r = Q[0] / (m[0] * dt)
        N.need(r > 0, 'Sinais incoerentes: se o corpo aquece, Q > 0')
        o += ['c = Q / (m \u0394T)', N.res('c', r, CU, s)]
        u = 'J/(kg K)'
    else:
        d = Q[0] / (m[0] * c[0])
        if k == 3:
            r = tf[0] - d
            o += ['\u03b8i = \u03b8f - Q / (m c)', N.res('\u03b8i', r, '\u00b0C', s)]
        else:
            r = ti[0] + d
            o += ['\u03b8f = \u03b8i + Q / (m c)', N.res('\u03b8f', r, '\u00b0C', s)]
        u = '\u00b0C'
    st = 'c: energia para aquecer 1 kg do material 1 K (ou 1 \u00b0C).\n' \
        '\u0394T em K \u00e9 igual a \u0394\u03b8 em \u00b0C.\n\u00c1gua: c = 4,18 ' + \
        X + ' 10\u00b3 J kg\u207b\u00b9 K\u207b\u00b9 (muito elevada).'
    return ('\n'.join(o), st, r, u)

# ------------------------------------------------------------ Q = m dH


def est():
    return ('Mudan\u00e7a de estado',
            [N.fld('Mudan\u00e7a', '', '', 'c', ['fus\u00e3o do gelo',
                                                'vaporiza\u00e7\u00e3o da \u00e1gua',
                                                'escrevo \u0394H']),
             N.fld('\u0394H (J/kg, s\u00f3 se escreves)', '', '', 'o'),
             N.fld('Massa m', MS, '', 'o'),
             N.fld('Energia Q', QS, '', 'o')], _est)


def _est(v):
    k0, h, m, Q = v
    if k0 < 2:
        N.need(h is None, 'Escolheste a mudan\u00e7a: deixa \u0394H vazio')
        h = ((HF, HV)[k0], 3)
    w = [h, m, Q]
    k = um(w, '\u0394H, m ou Q')
    for x, nm in ((h, '\u0394H'), (m, 'A massa'), (Q, 'A energia')):
        if x is not None:
            N.pos(x[0], nm)
    s = N.sfv(*w)
    o = ['= Q = m \u0394H']
    if k0 < 2:
        o.append('\u0394H = ' + N.q(h[0], 3, 'J kg\u207b\u00b9') +
                 (' (a 0 \u00b0C)' if k0 == 0 else ' (a 100 \u00b0C)'))
    if k == 2:
        r = m[0] * h[0]
        o.append(N.res('Q', r, 'J', s))
        u = 'J'
    elif k == 1:
        r = Q[0] / h[0]
        o += ['m = Q / \u0394H', N.res('m', r, 'kg', s)]
        u = 'kg'
    else:
        r = Q[0] / m[0]
        o += ['\u0394H = Q / m', N.res('\u0394H', r, 'J kg\u207b\u00b9', s)]
        u = 'J/kg'
    o.append('Durante a mudan\u00e7a de estado a temperatura n\u00e3o varia.')
    st = '\u0394H: energia para mudar o estado de 1 kg, \u00e0 temperatura ' \
        'de mudan\u00e7a.\nSolidifica\u00e7\u00e3o e condensa\u00e7\u00e3o libertam a ' \
        'mesma energia.'
    return ('\n'.join(o), st, r, u)

# ------------------------------------------------------------ equilibrio


def eq():
    return ('Temperatura de equil\u00edbrio',
            [N.fld('Massa do corpo 1', MS, ''),
             N.fld('c do corpo 1 (J kg\u207b\u00b9 K\u207b\u00b9)', '', '4,18e3'),
             N.fld('Temperatura do corpo 1', TS, ''),
             N.fld('Corpo 2', '', '', 'c', ['sem mudan\u00e7a de estado',
                                           'gelo a 0 \u00b0C (funde)']),
             N.fld('Massa do corpo 2', MS, ''),
             N.fld('c do corpo 2 (J kg\u207b\u00b9 K\u207b\u00b9)', '', '4,18e3'),
             N.fld('Temperatura do corpo 2', TS, '0')], _eq)


def _eq(v):
    m1, c1, t1, g, m2, c2, t2 = v
    for x, nm in ((m1, 'A massa do corpo 1'), (c1, 'c do corpo 1'),
                  (m2, 'A massa do corpo 2'), (c2, 'c do corpo 2')):
        N.pos(x[0], nm)
    s = N.sfv(m1, c1, t1, m2, c2, t2)
    a = m1[0] * c1[0]
    o = []
    if g == 0:
        b = m2[0] * c2[0]
        r = (a * t1[0] + b * t2[0]) / (a + b)
        o += ['= m1 c1 (\u03b8e - \u03b81) + m2 c2 (\u03b8e - \u03b82) = 0',
              '\u03b8e = (m1 c1 \u03b81 + m2 c2 \u03b82) / (m1 c1 + m2 c2)',
              N.res('\u03b8e', r, '\u00b0C', s),
              'Energia transferida: ' + N.q(abs(a * (r - t1[0])), s, 'J')]
    else:
        N.need(t1[0] > 0, 'A \u00e1gua tem de estar acima de 0 \u00b0C')
        o.append('= m1 c1 (\u03b81 - \u03b8e) = m2 \u0394Hf + m2 c(\u00e1gua) \u03b8e')
        if a * t1[0] < m2[0] * HF:
            f = a * t1[0] / HF
            r = 0.0
            o += ['Nem todo o gelo funde: \u03b8e = 0 \u00b0C.',
                  N.res('Funde', f, 'kg', s), 'Sobra ' + N.q(m2[0] - f, s, 'kg') +
                  ' de gelo.']
        else:
            r = (a * t1[0] - m2[0] * HF) / (a + m2[0] * CA)
            o += ['\u03b8e = (m1 c1 \u03b81 - m2 \u0394Hf) / (m1 c1 + m2 c(\u00e1gua))',
                  N.res('\u03b8e', r, '\u00b0C', s),
                  'Para fundir o gelo: ' + N.q(m2[0] * HF, s, 'J')]
    st = 'Sistema isolado: a energia cedida pelo corpo quente \u00e9 igual ' \
        '\u00e0 recebida pelo corpo frio.\n\u0394Hf(gelo) = 3,34 ' + X + \
        ' 10\u2075 J kg\u207b\u00b9; c(\u00e1gua) = 4,18 ' + X + ' 10\u00b3 J kg\u207b\u00b9 K\u207b\u00b9.'
    return ('\n'.join(o), st, r, '\u00b0C')

# ------------------------------------------------------------ conducao


def cond():
    return ('Condu\u00e7\u00e3o t\u00e9rmica',
            [N.fld('Condutividade k (W m\u207b\u00b9 K\u207b\u00b9)', '', '', 'o'),
             N.fld('\u00c1rea A', 'm\u00b2 cm\u00b2', '', 'o'),
             N.fld('Diferen\u00e7a de temperatura \u0394T (K ou \u00b0C)', '', '',
                   'o'),
             N.fld('Espessura \u2113', 'm cm mm', '', 'o'),
             N.fld('Pot\u00eancia P (energia por segundo)', 'W kW', '', 'o')],
            _cond)


def _cond(v):
    k, A, dT, l, P = v
    j = um(v, 'k, A, \u0394T, \u2113 ou P')
    for x, nm in ((k, 'A condutividade'), (A, 'A \u00e1rea'),
                  (dT, 'A diferen\u00e7a de temperatura'), (l, 'A espessura'),
                  (P, 'A pot\u00eancia')):
        if x is not None:
            N.pos(x[0], nm)
    s = N.sfv(*v)
    o = ['= P = k A \u0394T / \u2113']
    if j == 4:
        r = k[0] * A[0] * dT[0] / l[0]
        o += ['P = ' + N.q(k[0], k[1]) + ' ' + X + ' ' + N.q(A[0], A[1], 'm\u00b2') +
              ' ' + X + ' ' + N.q(dT[0], dT[1], 'K') + ' / ' +
              N.q(l[0], l[1], 'm'), N.res('P', r, 'W', s)]
        u = 'W'
    elif j == 0:
        r = P[0] * l[0] / (A[0] * dT[0])
        o += ['k = P \u2113 / (A \u0394T)', N.res('k', r, 'W m\u207b\u00b9 K\u207b\u00b9', s)]
        u = 'W/(m K)'
    elif j == 1:
        r = P[0] * l[0] / (k[0] * dT[0])
        o += ['A = P \u2113 / (k \u0394T)', N.res('A', r, 'm\u00b2', s)]
        u = 'm\u00b2'
    elif j == 2:
        r = P[0] * l[0] / (k[0] * A[0])
        o += ['\u0394T = P \u2113 / (k A)', N.res('\u0394T', r, 'K', s)]
        u = 'K'
    else:
        r = k[0] * A[0] * dT[0] / P[0]
        o += ['\u2113 = k A \u0394T / P', N.res('\u2113', r, 'm', s)]
        u = 'm'
    st = 'Bons condutores t\u00eam k grande (metais); isoladores t\u00eam k ' \
        'pequeno (ar, l\u00e3, esferovite).\nA energia passa do lado mais ' \
        'quente para o mais frio.'
    return ('\n'.join(o), st, r, u)

# ------------------------------------------------------------ 1.a lei


def pl():
    return ('Primeira Lei da Termodin\u00e2mica',
            [N.fld('Trabalho W (recebido > 0)', QS, '', 'o'),
             N.fld('Calor Q (recebido > 0)', QS, '', 'o'),
             N.fld('Radia\u00e7\u00e3o R (recebida > 0)', QS, '0', 'o'),
             N.fld('Varia\u00e7\u00e3o da energia interna \u0394U', QS, '', 'o')],
            _pl)


def _pl(v):
    W, Q, R, dU = v
    k = um(v, 'W, Q, R ou \u0394U')
    s = N.sfv(*v)
    o = ['= \u0394U = W + Q + R']
    nm = ('W', 'Q', 'R', '\u0394U')[k]
    if k == 3:
        r = W[0] + Q[0] + R[0]
    else:
        r = dU[0] - sum([v[i][0] for i in range(3) if i != k])
        o.append(nm + ' = \u0394U - (as outras parcelas)')
    o.append(N.res(nm, r, 'J', s))
    if k == 3:
        o.append('\u0394U > 0: a energia interna aumenta.' if r > 0 else
                 '\u0394U < 0: a energia interna diminui.' if r < 0 else
                 '\u0394U = 0: a energia interna n\u00e3o varia.')
    elif r < 0:
        o.append(nm + ' < 0: o sistema cede energia desta forma.')
    else:
        o.append(nm + ' > 0: o sistema recebe energia desta forma.')
    st = 'Conven\u00e7\u00e3o: energia recebida pelo sistema \u00e9 positiva; ' \
        'cedida \u00e9 negativa.\nSistema isolado: W = Q = R = 0 e \u0394U = 0.'
    return ('\n'.join(o), st, r, 'J')

# ------------------------------------------------------------ painel


def pv():
    return ('Painel fotovoltaico',
            [N.fld('Irradi\u00e2ncia Er (W/m\u00b2)', '', '1,0e3'),
             N.fld('\u00c1rea do painel A', 'm\u00b2 cm\u00b2', ''),
             N.fld('Pot\u00eancia el\u00e9trica P (ou U e I)', 'W kW mW', '', 'o'),
             N.fld('Tens\u00e3o U (opcional)', 'V mV', '', 'o'),
             N.fld('Corrente I (opcional)', 'A mA', '', 'o')], _pv)


def _pv(v):
    er, A, P, U, I = v
    N.pos(er[0], 'A irradi\u00e2ncia')
    N.pos(A[0], 'A \u00e1rea')
    o = ['= P(radia\u00e7\u00e3o) = Er A', N.res('P(rad)', er[0] * A[0], 'W',
                                              N.sfv(er, A))]
    if P is None:
        N.need(U is not None and I is not None, 'Escreve a pot\u00eancia '
               'el\u00e9trica ou a tens\u00e3o e a corrente')
        N.pos(U[0], 'A tens\u00e3o')
        N.pos(I[0], 'A corrente')
        p = U[0] * I[0]
        s = N.sfv(U, I)
        o += ['= P(el\u00e9trica) = U I', N.res('P(el)', p, 'W', s)]
    else:
        N.need(U is None and I is None, 'Escreve a pot\u00eancia el\u00e9trica ou '
               'U e I, n\u00e3o os tr\u00eas')
        N.pos(P[0], 'A pot\u00eancia')
        p = P[0]
        s = P[1]
    r = p / (er[0] * A[0]) * 100
    N.need(r <= 100, '\u03b7 > 100 %: imposs\u00edvel (verifica a \u00e1rea e as '
           'unidades)')
    o += ['= \u03b7 = P(el) / P(rad) ' + X + ' 100 %',
          N.res('\u03b7', r, '%', N.sfm(s, er[1], A[1]))]
    st = 'Irradi\u00e2ncia: pot\u00eancia da radia\u00e7\u00e3o por unidade de ' \
        '\u00e1rea (W m\u207b\u00b2).\nCom sol direto, \u00e0 superf\u00edcie, ' \
        'Er \u2248 1,0 ' + X + ' 10\u00b3 W m\u207b\u00b2.\nOs pain\u00e9is comuns t\u00eam ' \
        '\u03b7 entre cerca de 15 % e 22 %.'
    return ('\n'.join(o), st, r, '%')
