# c_alq1.py - M1TR4M: assistentes das AL de Quimica 1.1 (gota de agua),
# 1.2 (teste de chama) e 1.3 (densidade relativa de metais).
#@ c_alq1.gota|AL 1.1 Volume e mol\u00e9culas de uma gota de \u00e1gua|al 1.1 gota de \u00e1gua volume n\u00famero de mol\u00e9culas massa m\u00e9dia incerteza ensaios|F|aq
#@ c_alq1.chama|AL 1.2 Teste de chama|al 1.2 teste de chama cor da chama identificar elemento s\u00f3dio pot\u00e1ssio l\u00edtio cobre comprimento de onda|F|aq
#@ c_alq1.dens|AL 1.3 Densidade relativa (picn\u00f3metro)|al 1.3 densidade relativa picn\u00f3metro metal erro percentual exatid\u00e3o|F|aq
# Casos-limite: listas vazias, massas nulas ou negativas, numero de gotas
# nao inteiro, massas do picnometro incoerentes (massa de agua deslocada
# nula ou negativa), cor sem elemento na tabela.

import m1_nucleo as N

X = N.X
NA = 6.02e23
MH2O = 18.02        # g/mol
# Teste de chama: cor|elementos|riscas ou bandas mais intensas (aprox.)
CH = ('vermelho carmim|l\u00edtio (Li)|671 nm#'
      'amarelo-alaranjado|s\u00f3dio (Na)|589 nm (dupleto)#'
      'violeta (lil\u00e1s)|pot\u00e1ssio (K)|404 nm e 766 nm; v\u00ea-se melhor com '
      'vidro de cobalto#'
      'vermelho-alaranjado (tijolo)|c\u00e1lcio (Ca)|bandas perto de 620 nm#'
      'vermelho intenso|estr\u00f4ncio (Sr)|bandas entre cerca de 600 nm e 690 nm#'
      'verde-amarelado|b\u00e1rio (Ba)|554 nm#'
      'verde-azulado|cobre (Cu)|510 nm a 522 nm')
# Densidades relativas a 20 graus C (valores tabelados)
DM = ('alum\u00ednio|2.70 ferro|7.87 zinco|7.14 cobre|8.96 chumbo|11.34')


def dec(x):
    # Casas decimais com que um dado (valor, alg. sig.) foi escrito.
    if x[0] == 0:
        return x[1] - 1
    return x[1] - 1 - N._e10(abs(x[0]))


def ensaios(xs):
    # Media, maior desvio e texto "m +- u" (convencao dos manuais).
    m = sum(xs) / len(xs)
    u = max([abs(x - m) for x in xs])
    return m, u

# ------------------------------------------------------------ AL 1.1


def gota():
    return ('AL 1.1 Gota de \u00e1gua',
            [N.fld('Massa de n gotas em cada ensaio (g)', '',
                   '0,99 1,02 1,01', 'l'),
             N.fld('N\u00famero de gotas n em cada ensaio', '', '20'),
             N.fld('Incerteza de leitura da balan\u00e7a (g)', '', '0,01')],
            _gota)


def _gota(v):
    ms, n, ub = v
    N.need(n[0] >= 1 and n[0] == int(n[0]), 'O n\u00famero de gotas \u00e9 um '
           'inteiro positivo')
    for x in ms:
        N.pos(x[0], 'Cada massa')
    N.nneg(ub[0], 'A incerteza')
    xs = [x[0] / n[0] for x in ms]
    m, u = ensaios(xs)
    u = max(u, ub[0] / n[0])
    rel = u / m
    vol = m / 1.00
    q = m / MH2O
    nn = q * NA
    o = ['Massa de uma gota em cada ensaio: ' +
         '; '.join([N.fmt(x, 3) for x in xs]) + ' g',
         '= m(gota) = m\u00e9dia', '> m(gota) = ' + N.pm(m, u) + ' g',
         'Incerteza relativa: ' + N.fmt(rel * 100, 2) + ' %',
         '= V = m / \u03c1 (\u03c1 = 1,00 g cm\u207b\u00b3)',
         '> V = ' + N.pm(vol, u) + ' cm\u00b3',
         '= n = m / M = ' + N.fmt(m, 3) + ' / 18,02',
         N.res('n', q, 'mol', 3),
         '= N = n NA', N.res('N', nn, 'mol\u00e9culas', 3),
         'Com a mesma incerteza relativa: N = ' + N.pm(nn, nn * rel)]
    st = 'Mede-se a massa de muitas gotas (por exemplo 20) para reduzir a ' \
        'incerteza de cada gota.\nIncerteza absoluta: maior desvio em ' \
        'rela\u00e7\u00e3o \u00e0 m\u00e9dia (ou a incerteza de leitura a dividir por n, se ' \
        'for maior).'
    return ('\n'.join(o), st, nn, 'mol\u00e9culas')

# ------------------------------------------------------------ AL 1.2


def chama():
    return ('AL 1.2 Teste de chama',
            [N.fld('Cor observada na chama', '', '', 'c',
                   [x.split('|')[0] for x in CH.split('#')])], _chama)


def _chama(v):
    c, el, lam = CH.split('#')[v[0]].split('|')
    o = ['Cor: ' + c, '> Elemento prov\u00e1vel: ' + el,
         'Emiss\u00e3o mais intensa (aprox.): ' + lam,
         'A cor vem da desexcita\u00e7\u00e3o dos eletr\u00f5es: cada elemento '
         'emite radia\u00e7\u00f5es com energias pr\u00f3prias.',
         'O teste de chama identifica o elemento met\u00e1lico, n\u00e3o o '
         'composto.']
    st = 'O s\u00f3dio \u00e9 uma impureza frequente: a sua cor amarela pode ' \
        'esconder outras.\nLimpa o fio (ou usa uma vara nova) entre ' \
        'amostras.\nCor diferente da tabela: o teste n\u00e3o \u00e9 conclusivo; ' \
        'confirma com um espetrosc\u00f3pio.'
    return ('\n'.join(o), st, None, '')

# ------------------------------------------------------------ AL 1.3


def dens():
    return ('AL 1.3 Densidade relativa',
            [N.fld('Massa do metal m (g)', '', ''),
             N.fld('Picn\u00f3metro cheio de \u00e1gua m1 (g)', '', ''),
             N.fld('Picn\u00f3metro com metal e \u00e1gua m2 (g)', '', ''),
             N.fld('Valor tabelado', '', '', 'c', ['n\u00e3o comparar'] +
                   [x.split('|')[0] for x in DM.split(' ')])], _dens)


def _dens(v):
    m, m1, m2, k = v
    for x, nm in ((m, 'A massa do metal'), (m1, 'm1'), (m2, 'm2')):
        N.pos(x[0], nm)
    ma = m[0] + m1[0] - m2[0]
    N.need(ma > 0, 'Massas incoerentes: m + m1 - m2 tem de ser positivo')
    k2 = max(0, min(dec(m), dec(m1), dec(m2)))
    sa = N._e10(ma) + 1 + k2
    d = m[0] / ma
    o = ['Massa de \u00e1gua deslocada: m + m1 - m2 = ' + N.fix(ma, k2) + ' g',
         '= d = m / (m + m1 - m2)', N.res('d', d, '', N.sfm(m[1], sa))]
    if k:
        nm, t = DM.split(' ')[k - 1].split('|')
        r = float(t)
        e = abs(d - r) / r * 100
        if e < 1e-9:
            e = 0.0
        o += ['Valor tabelado (' + nm + ', 20 \u00b0C): ' + t.replace('.', ','),
              '> Erro percentual = ' + N.fmt(e, 2) + ' %']
        o.append('Boa exatid\u00e3o (erro < 5 %).' if e < 5 else
                 'Erro grande: verifica bolhas de ar e se o picn\u00f3metro '
                 'estava bem cheio e seco por fora.')
    st = 'A densidade relativa compara a massa do metal com a de igual ' \
        'volume de \u00e1gua (n\u00e3o tem unidades).\nO volume do metal \u00e9 o ' \
        'volume da \u00e1gua que ele desloca.'
    return ('\n'.join(o), st, d, '')
