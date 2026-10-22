# c_fqci.py - M1TR4M: calculadoras de circuitos eletricos: lei de Ohm,
# resistividade, associacao de resistencias, gerador (fem e resistencia
# interna) e potencia, energia e custo.
#@ c_fqci.ohm|Resist\u00eancia el\u00e9trica (U = R I)|resist\u00eancia diferen\u00e7a de potencial tens\u00e3o corrente el\u00e9trica lei de ohm condutor \u00f3hmico|F|f2
#@ c_fqci.rho|Resistividade (R = \u03c1 \u2113 / A)|resistividade comprimento \u00e1rea de sec\u00e7\u00e3o fio condutor material cobre|F|f2
#@ c_fqci.assoc|Resist\u00eancias em s\u00e9rie e em paralelo|associa\u00e7\u00e3o s\u00e9rie paralelo resist\u00eancia equivalente divisor de corrente|F|f2
#@ c_fqci.ger|Gerador: for\u00e7a eletromotriz e resist\u00eancia interna|gerador pilha for\u00e7a eletromotriz resist\u00eancia interna curto-circuito rendimento|F|f2
#@ c_fqci.pot|Pot\u00eancia, energia e custo el\u00e9tricos|pot\u00eancia el\u00e9trica efeito joule energia quilowatt-hora custo fatura|F|f2
# Casos-limite: resistencias nulas ou negativas, campos a mais ou a
# menos, lista vazia ou com zeros, corrente maior do que a de
# curto-circuito (U < 0), tensao nos terminais maior do que a fem.

import m1_nucleo as N

X = N.X
US = 'V mV kV'
IS = 'A mA \u00b5A'
RS = '\u03a9 k\u03a9 M\u03a9 m\u03a9'
# Resistividades a 20 graus C (valores tabelados, arredondados):
# material|rho em ohm m
MAT = ('cobre|1.7e-8 alum\u00ednio|2.7e-8 tungst\u00e9nio|5.6e-8 ferro|9.7e-8 '
       'constantan|4.9e-7 n\u00edquel-cr\u00f3mio|1.1e-6')


def um(v, nome):
    # Exatamente um campo vazio; devolve o seu indice.
    f = [i for i in range(len(v)) if v[i] is None]
    N.need(len(f) == 1, 'Deixa vazio s\u00f3 o campo que queres calcular (' +
           nome + ')')
    return f[0]


def todos_pos(v, nomes):
    for x, nm in zip(v, nomes):
        if x is not None:
            N.pos(x[0], nm)

# ------------------------------------------------------------ Ohm


def ohm():
    return ('Resist\u00eancia el\u00e9trica',
            [N.fld('Diferen\u00e7a de potencial U', US, '', 'o'),
             N.fld('Resist\u00eancia R', RS, '', 'o'),
             N.fld('Corrente el\u00e9trica I', IS, '', 'o')], _ohm)


def _ohm(v):
    U, R, I = v
    k = um(v, 'U, R ou I')
    todos_pos(v, ('A diferen\u00e7a de potencial', 'A resist\u00eancia',
                  'A corrente'))
    s = N.sfv(*v)
    if k == 0:
        r = R[0] * I[0]
        o = ['= U = R I = ' + N.q(R[0], R[1], '\u03a9') + ' ' + X + ' ' +
             N.q(I[0], I[1], 'A'), N.res('U', r, 'V', s)]
        U = (r, s)
        u = 'V'
    elif k == 1:
        r = U[0] / I[0]
        o = ['= R = U / I = ' + N.q(U[0], U[1], 'V') + ' / ' +
             N.q(I[0], I[1], 'A'), N.res('R', r, '\u03a9', s)]
        u = '\u03a9'
    else:
        r = U[0] / R[0]
        o = ['= I = U / R = ' + N.q(U[0], U[1], 'V') + ' / ' +
             N.q(R[0], R[1], '\u03a9'), N.res('I', r, 'A', s)]
        I = (r, s)
        u = 'A'
    o.append('Pot\u00eancia: P = U I = ' + N.q(U[0] * I[0], s, 'W'))
    st = 'R = U / I define a resist\u00eancia (em \u03a9 = V/A).\nCondutor ' \
        '\u00f3hmico: R constante (a temperatura constante); o gr\u00e1fico ' \
        'U(I) \u00e9 uma reta que passa na origem.'
    return ('\n'.join(o), st, r, u)

# ------------------------------------------------------------ resistividade


def rho():
    return ('Resistividade',
            [N.fld('Material', '', '', 'c', ['escrevo \u03c1'] +
                   [x.split('|')[0] for x in MAT.split(' ')]),
             N.fld('Resistividade \u03c1 (\u03a9 m)', '', '', 'o'),
             N.fld('Comprimento \u2113', 'm cm km mm', '', 'o'),
             N.fld('\u00c1rea da sec\u00e7\u00e3o A', 'mm\u00b2 cm\u00b2 m\u00b2', '',
                   'o'),
             N.fld('Resist\u00eancia R', RS, '', 'o')], _rho)


def _rho(v):
    # A area chega em mm\u00b2 (1.a unidade da lista); as contas usam m\u00b2.
    m, p, l, a, R = v
    if a is not None:
        a = (a[0] * 1e-6, a[1])
    if m:
        N.need(p is None, 'Escolheste um material: deixa \u03c1 vazio')
        p = (float(MAT.split(' ')[m - 1].split('|')[1]), 2)
    w = [p, l, a, R]
    k = um(w, '\u03c1, \u2113, A ou R')
    todos_pos(w, ('A resistividade', 'O comprimento', 'A \u00e1rea',
                  'A resist\u00eancia'))
    s = N.sfv(*w)
    o = ['= R = \u03c1 \u2113 / A']
    if m:
        o.append('\u03c1(' + MAT.split(' ')[m - 1].split('|')[0] + ') = ' +
                 N.q(p[0], 2, '\u03a9 m') + ' (a 20 \u00b0C)')
    if k == 3:
        r = p[0] * l[0] / a[0]
        o += ['R = ' + N.q(p[0], p[1], '\u03a9 m') + ' ' + X + ' ' +
              N.q(l[0], l[1], 'm') + ' / (' + N.q(a[0], a[1], 'm\u00b2') + ')',
              N.res('R', r, '\u03a9', s)]
        u = '\u03a9'
    elif k == 0:
        r = R[0] * a[0] / l[0]
        o += ['\u03c1 = R A / \u2113', N.res('\u03c1', r, '\u03a9 m', s)]
        u = '\u03a9 m'
    elif k == 1:
        r = R[0] * a[0] / p[0]
        o += ['\u2113 = R A / \u03c1', N.res('\u2113', r, 'm', s)]
        u = 'm'
    else:
        r = p[0] * l[0] / R[0]
        o += ['A = \u03c1 \u2113 / R', N.res('A', r, 'm\u00b2', s),
              '= ' + N.fmt(r * 1e6, s) + ' mm\u00b2']
        u = 'm\u00b2'
    st = 'A resist\u00eancia aumenta com o comprimento e diminui com a ' \
        '\u00e1rea da sec\u00e7\u00e3o.\n\u03c1 depende do material e da ' \
        'temperatura (nos metais, aumenta com a temperatura).\n1 mm\u00b2 = ' \
        '10\u207b\u2076 m\u00b2.'
    return ('\n'.join(o), st, r, u)

# ------------------------------------------------------------ associacao


def assoc():
    return ('Resist\u00eancias em s\u00e9rie e em paralelo',
            [N.fld('Associa\u00e7\u00e3o', '', '', 'c', ['em s\u00e9rie',
                                                     'em paralelo']),
             N.fld('Resist\u00eancias em \u03a9 (separa com espa\u00e7os)', '',
                   '10 20 30', 'l'),
             N.fld('Diferen\u00e7a de potencial total U (opcional)', US, '',
                   'o')], _assoc)


def _assoc(v):
    k, rs, U = v
    N.need(len(rs) >= 2, 'Escreve pelo menos duas resist\u00eancias')
    N.need(len(rs) <= 10, 'No m\u00e1ximo 10 resist\u00eancias')
    for x in rs:
        N.pos(x[0], 'Cada resist\u00eancia')
    s = N.sfm(*[x[1] for x in rs])
    if k == 0:
        r = sum([x[0] for x in rs])
        o = ['= Req = R1 + R2 + ...', N.res('Req', r, '\u03a9', s),
             'Req \u00e9 maior do que a maior resist\u00eancia.']
    else:
        r = 1 / sum([1 / x[0] for x in rs])
        o = ['= 1/Req = 1/R1 + 1/R2 + ...', N.res('Req', r, '\u03a9', s),
             'Req \u00e9 menor do que a menor resist\u00eancia.']
    if U is not None:
        N.pos(U[0], 'A diferen\u00e7a de potencial')
        s2 = N.sfm(s, U[1])
        i = U[0] / r
        o.append(N.res('I total', i, 'A', s2))
        for j in range(len(rs)):
            if k == 0:
                o.append('R' + str(j + 1) + ': I = ' + N.fmt(i, s2) + ' A; U = ' +
                         N.fmt(rs[j][0] * i, s2) + ' V')
            else:
                o.append('R' + str(j + 1) + ': U = ' + N.fmt(U[0], s2) +
                         ' V; I = ' + N.fmt(U[0] / rs[j][0], s2) + ' A')
    st = 'S\u00e9rie: a mesma corrente em todas; as tens\u00f5es somam-se.\n' \
        'Paralelo: a mesma tens\u00e3o em todas; as correntes somam-se.'
    return ('\n'.join(o), st, r, '\u03a9')

# ------------------------------------------------------------ gerador


def ger():
    return ('Gerador',
            [N.fld('For\u00e7a eletromotriz \u03b5', US, '', 'o'),
             N.fld('Resist\u00eancia interna r', RS, '', 'o'),
             N.fld('Corrente I', IS, '', 'o'),
             N.fld('Tens\u00e3o nos terminais U', US, '', 'o')], _ger)


def _ger(v):
    e, ri, I, U = v
    k = um(v, '\u03b5, r, I ou U')
    for x, nm in ((e, 'A for\u00e7a eletromotriz'), (I, 'A corrente')):
        if x is not None:
            N.pos(x[0], nm)
    for x, nm in ((ri, 'A resist\u00eancia interna'), (U, 'A tens\u00e3o')):
        if x is not None:
            N.nneg(x[0], nm)
    s = N.sfv(*v)
    o = ['= U = \u03b5 - r I']
    if k == 3:
        r = e[0] - ri[0] * I[0]
        N.need(r >= 0, 'Com esta corrente U < 0: maior do que a de '
               'curto-circuito (\u03b5 / r)')
        o.append(N.res('U', r, 'V', s))
        U = (r, s)
        u = 'V'
    elif k == 0:
        r = U[0] + ri[0] * I[0]
        o += ['\u03b5 = U + r I', N.res('\u03b5', r, 'V', s)]
        e = (r, s)
        u = 'V'
    elif k == 1:
        N.need(U[0] <= e[0], 'U n\u00e3o pode ser maior do que \u03b5 num '
               'gerador')
        r = (e[0] - U[0]) / I[0]
        o += ['r = (\u03b5 - U) / I', N.res('r', r, '\u03a9', s)]
        ri = (r, s)
        u = '\u03a9'
    else:
        N.need(U[0] <= e[0], 'U n\u00e3o pode ser maior do que \u03b5 num '
               'gerador')
        N.need(ri[0] > 0, 'Com r = 0 a corrente n\u00e3o fica determinada')
        r = (e[0] - U[0]) / ri[0]
        o += ['I = (\u03b5 - U) / r', N.res('I', r, 'A', s)]
        I = (r, s)
        u = 'A'
    pe = e[0] * I[0]
    pu = U[0] * I[0]
    o += ['Pot\u00eancias: gerada \u03b5 I = ' + N.q(pe, s, 'W') + ';',
          '\u00fatil U I = ' + N.q(pu, s, 'W') + '; dissipada r I\u00b2 = ' +
          N.q(ri[0] * I[0] ** 2, s, 'W')]
    if pe > 0:
        o.append('Rendimento: \u03b7 = U / \u03b5 = ' + N.fmt(pu / pe * 100, s) +
                 ' %')
    if ri[0] > 0:
        o.append('Curto-circuito: I = \u03b5 / r = ' +
                 N.q(e[0] / ri[0], s, 'A'))
    st = 'O gerador fornece \u03b5 I; parte dissipa-se dentro dele (r I\u00b2) ' \
        'e o resto vai para o circuito (U I).\nGr\u00e1fico U(I): reta de ' \
        'declive -r e ordenada na origem \u03b5.'
    return ('\n'.join(o), st, r, u)

# ------------------------------------------------------------ potencia


def pot():
    return ('Pot\u00eancia, energia e custo',
            [N.fld('Pot\u00eancia P (preenche 2 de P, U, I, R)', 'W kW mW', '',
                   'o'),
             N.fld('Tens\u00e3o U', US, '', 'o'),
             N.fld('Corrente I', IS, '', 'o'),
             N.fld('Resist\u00eancia R', RS, '', 'o'),
             N.fld('Tempo de funcionamento \u0394t (opcional)', 'h min s', '',
                   'o'),
             N.fld('Pre\u00e7o do kWh em euros (opcional)', '', '', 'o')], _pot)


def _pot(v):
    P, U, I, R, t, c = v
    d = [P, U, I, R]
    N.need(len([x for x in d if x is not None]) == 2, 'Preenche exatamente '
           'dois de P, U, I e R')
    todos_pos(d, ('A pot\u00eancia', 'A tens\u00e3o', 'A corrente',
                  'A resist\u00eancia'))
    s = N.sfv(*d)
    o = []
    if U is not None and I is not None:
        p = U[0] * I[0]
        o.append('= P = U I')
    elif I is not None and R is not None:
        p = R[0] * I[0] ** 2
        o.append('= P = R I\u00b2 (efeito Joule)')
    elif U is not None and R is not None:
        p = U[0] ** 2 / R[0]
        o.append('= P = U\u00b2 / R')
    elif U is not None:
        p = P[0]
        o += ['= I = P / U', N.res('I', p / U[0], 'A', s)]
    elif I is not None:
        p = P[0]
        o += ['= U = P / I', N.res('U', p / I[0], 'V', s)]
    else:
        p = P[0]
        o += ['= I = \u221a(P / R)', N.res('I', (p / R[0]) ** 0.5, 'A', s)]
    if P is None:
        o.append(N.res('P', p, 'W', s))
    r = p
    u = 'W'
    if t is not None:
        # o tempo chega em horas (1.a unidade da lista)
        N.pos(t[0], 'O tempo')
        s2 = N.sfm(s, t[1])
        e = p * t[0] * 3600
        o += ['= E = P \u0394t', N.res('E', e, 'J', s2),
              '= ' + N.fmt(e / 3.6e6, s2) + ' kWh (1 kWh = 3,6 ' + X +
              ' 10\u2076 J)']
        r = e
        u = 'J'
        if c is not None:
            N.nneg(c[0], 'O pre\u00e7o')
            o.append('Custo: ' + N.fmt(e / 3.6e6, s2) + ' kWh ' + X + ' ' +
                     N.fmt(c[0]) + ' \u20ac/kWh = ' +
                     N.fix(e / 3.6e6 * c[0], 2) + ' \u20ac')
    st = 'P = U I = R I\u00b2 = U\u00b2 / R.\nEfeito Joule: num condutor ' \
        'a energia el\u00e9trica passa a energia interna (aquecimento).\n' \
        'Energia em kWh: P em kW vezes \u0394t em horas.'
    return ('\n'.join(o), st, r, u)
