# c_alq2.py - M1TR4M: assistentes das AL de Quimica 2.1 (miscibilidade
# de liquidos) e 2.2 (solucoes a partir de solutos solidos, com
# incerteza). A AL 2.3 usa c_fqso.dil e a AL 2.4 e qualitativa.
#@ c_alq2.misc|AL 2.1 Miscibilidade de l\u00edquidos|al 2.1 miscibilidade l\u00edquidos misc\u00edveis imisc\u00edveis polar apolar intera\u00e7\u00f5es intermoleculares \u00e1gua hexano etanol|F|aq
#@ c_alq2.sol|AL 2.2 Solu\u00e7\u00e3o a partir de soluto s\u00f3lido|al 2.2 preparar solu\u00e7\u00e3o soluto s\u00f3lido bal\u00e3o volum\u00e9trico massa a pesar incerteza concentra\u00e7\u00e3o|F|aq
# Casos-limite: o mesmo liquido duas vezes, pares em que a previsao
# simples nao chega (alcool ou cetona com liquido apolar), volume ou
# massa molar nulos, nenhuma de c e m preenchida.

import m1_nucleo as N

X = N.X
# Liquidos: nome|tipo (p polar com ligacoes de H, d polar, a apolar)|
# interacoes|massa volumica (g/cm3, 20 C, aprox.)
LQ = ('\u00e1gua|p|liga\u00e7\u00f5es de hidrog\u00e9nio e dipolo-dipolo|1,00#'
      'etanol|p|liga\u00e7\u00f5es de hidrog\u00e9nio; cadeia apolar curta|0,79#'
      'propanona (acetona)|d|dipolo-dipolo; aceita liga\u00e7\u00f5es de H|0,79#'
      'hexano|a|s\u00f3 for\u00e7as de London|0,66#'
      'ciclo-hexano|a|s\u00f3 for\u00e7as de London|0,78#'
      '\u00f3leo alimentar|a|quase s\u00f3 for\u00e7as de London|0,92')


def misc():
    nomes = [x.split('|')[0] for x in LQ.split('#')]
    return ('AL 2.1 Miscibilidade',
            [N.fld('L\u00edquido A', '', '', 'c', nomes),
             N.fld('L\u00edquido B', '', '', 'c', nomes)], _misc)


def _misc(v):
    N.need(v[0] != v[1], 'Escolhe dois l\u00edquidos diferentes')
    a = LQ.split('#')[v[0]].split('|')
    b = LQ.split('#')[v[1]].split('|')
    o = [a[0] + ': ' + a[2] + '.', b[0] + ': ' + b[2] + '.']
    ta, tb = a[1], b[1]
    agua = v[0] == 0 or v[1] == 0
    if (ta == 'a') == (tb == 'a'):
        o.append('> Previs\u00e3o: misc\u00edveis (intera\u00e7\u00f5es semelhantes).')
        r = 1
    elif agua:
        o.append('> Previs\u00e3o: imisc\u00edveis (uma polar e outra apolar).')
        r = 0
    else:
        o.append('> Previs\u00e3o incerta: o ' + (a[0] if ta != 'a' else b[0]) +
                 ' tem uma parte polar e outra apolar; confirma no '
                 'laborat\u00f3rio.')
        r = None
    if r == 0:
        da = float(a[3].replace(',', '.'))
        db = float(b[3].replace(',', '.'))
        cima = a[0] if da < db else b[0]
        o.append('Fica por cima o menos denso: ' + cima + ' (\u03c1 \u2248 ' +
                 (a[3] if da < db else b[3]) + ' g cm\u207b\u00b3).')
    st = 'Regra: "semelhante dissolve semelhante". L\u00edquidos com ' \
        'intera\u00e7\u00f5es do mesmo tipo e intensidade parecida misturam-se.\n' \
        'Massas vol\u00famicas aproximadas, a 20 \u00b0C.'
    return ('\n'.join(o), st, r, '')

# ------------------------------------------------------------ AL 2.2


def sol():
    return ('AL 2.2 Solu\u00e7\u00e3o a partir de um s\u00f3lido',
            [N.fld('Massa molar M (g/mol)', '', ''),
             N.fld('Volume do bal\u00e3o V (mL)', '', '100,00'),
             N.fld('Incerteza do bal\u00e3o (mL)', '', '0,10'),
             N.fld('Concentra\u00e7\u00e3o pretendida (mol/dm\u00b3)', '', '', 'o'),
             N.fld('Massa pesada (g)', '', '', 'o'),
             N.fld('Incerteza da balan\u00e7a (g)', '', '0,01')], _sol)


def _sol(v):
    M, V, uV, c, m, um = v
    N.pos(M[0], 'A massa molar')
    N.pos(V[0], 'O volume')
    N.nneg(uV[0], 'A incerteza do bal\u00e3o')
    N.nneg(um[0], 'A incerteza da balan\u00e7a')
    N.need(c is not None or m is not None, 'Escreve a concentra\u00e7\u00e3o '
           'pretendida ou a massa pesada')
    Vd = V[0] / 1000
    o = []
    if c is not None:
        N.pos(c[0], 'A concentra\u00e7\u00e3o')
        mp = c[0] * Vd * M[0]
        o += ['= m = c V M = ' + N.q(c[0], c[1]) + ' ' + X + ' ' +
              N.q(Vd, V[1], 'dm\u00b3') + ' ' + X + ' ' + N.q(M[0], M[1]),
              N.res('m a pesar', mp, 'g', N.sfm(c[1], M[1], 3))]
    if m is not None:
        N.pos(m[0], 'A massa pesada')
        cr = m[0] / (M[0] * Vd)
        rel = um[0] / m[0] + uV[0] / V[0]
        o += ['= c = m / (M V)', 'c = ' + N.pm(cr, cr * rel) + ' mol dm\u207b\u00b3',
              'Incerteza relativa \u2248 u(m)/m + u(V)/V = ' +
              N.fmt(rel * 100, 2) + ' %']
        if c is not None:
            e = abs(cr - c[0]) / c[0] * 100
            o.append('Diferen\u00e7a para a pretendida: ' + N.fmt(e, 2) + ' %')
        r = cr
        u = 'mol/dm\u00b3'
    else:
        r = mp
        u = 'g'
    st = 'Procedimento: pesar o s\u00f3lido num gobel\u00e9, dissolver com pouca ' \
        '\u00e1gua, transferir para o bal\u00e3o, lavar o gobel\u00e9 para o ' \
        'bal\u00e3o e completar at\u00e9 ao tra\u00e7o.\nA incerteza relativa \u00e9 ' \
        'aproximada pela soma das incertezas relativas da massa e do volume.'
    return ('\n'.join(o), st, r, u)
