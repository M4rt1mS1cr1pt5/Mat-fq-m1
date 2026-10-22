# c_matd.py - M1TR4M: modelos matematicos para a cidadania - financas:
# salario (bruto, liquido, anual, por hora, horas extra), IRS (escaloes de
# um ano concreto, com a fonte, ou taxa manual), juros simples e compostos
# e, como aprofundamento, prestacoes constantes e valor atual.
#@ c_matd.sal|Sal\u00e1rio: bruto e l\u00edquido|sal\u00e1rio bruto l\u00edquido mensal anual valor por hora horas extra trabalho suplementar seguran\u00e7a social reten\u00e7\u00e3o na fonte 14 meses|M|m1
#@ c_matd.irs|IRS por escal\u00f5es|irs imposto escal\u00f5es taxa marginal taxa m\u00e9dia progressividade rendimento colet\u00e1vel coleta parcela a abater reembolso|M|m1
#@ c_matd.jur|Juros simples e compostos|juro simples composto capital taxa anual capitaliza\u00e7\u00e3o dep\u00f3sito a prazo tae poupan\u00e7a imposto sobre juros|M|m1
#@ c_matd.prest|Presta\u00e7\u00f5es e valor atual|presta\u00e7\u00e3o constante empr\u00e9stimo cr\u00e9dito valor atual amortiza\u00e7\u00e3o juros aprofundamento|M|m1
# Casos-limite: rendimento num limite de escalao, taxa de juro 0, tempo
# que nao e um numero inteiro de periodos, taxas fora de 0-100%,
# descontos que excedem o salario.

import m1_nucleo as N

X = N.X
MS = '\u00b7'
# IRS de 2026: CIRS, art. 68.o, na redacao da Lei n.o 73-A/2025, de 30 de
# dezembro (Orcamento do Estado para 2026). Limites superiores dos
# escaloes (euros) e taxas marginais (%). A confirmar no Portal das
# Financas. Verificacao: a taxa media do 8.o escalao da 34,856%.
IRS_ANO = '2026'
IRS_FONTE = 'CIRS, art. 68.\u00ba, Lei n.\u00ba 73-A/2025 (OE 2026)'
IRS_LIM = (8342, 12587, 17838, 23089, 29397, 43090, 46566, 86634)
IRS_TX = (12.5, 15.7, 21.2, 24.1, 31.1, 34.9, 43.1, 44.6, 48.0)
SS_T = 11.0     # Seguranca Social: trabalhador (%)
SS_E = 23.75    # Seguranca Social: entidade empregadora (%)


def grp(s):
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


def eur(x):
    # Euros com 2 casas e os milhares separados: 1 234,50 EUR.
    x = float(x)
    if abs(x) < 0.005:
        return '0,00 \u20ac'
    return grp(N.fix(x, 2)) + ' \u20ac'


def pc(x):
    # Percentagem: 12,5%, 23,75%, 11%.
    return N.fmt(x, 0, 3) + '%'


def taxa(t, nm):
    N.need(0 <= t <= 100, nm + ' tem de estar entre 0 e 100%')
    return t / 100


def inteiro(x, nm, a, b):
    N.need(x == int(x) and a <= x <= b, nm + ' tem de ser um inteiro de ' +
           str(a) + ' a ' + str(b))
    return int(x)


def coleta(R):
    # Imposto pela tabela: soma, escalao a escalao, da parte de R em cada
    # escalao vezes a taxa desse escalao.
    t = 0.0
    lo = 0
    for k in range(len(IRS_TX)):
        hi = IRS_LIM[k] if k < len(IRS_LIM) else None
        if R <= lo:
            break
        p = (R if hi is None else min(R, hi)) - lo
        t += p * IRS_TX[k] / 100
        if hi is None:
            break
        lo = hi
    return t


def escalao(R):
    for k in range(len(IRS_LIM)):
        if R <= IRS_LIM[k]:
            return k
    return len(IRS_LIM)

# ------------------------------------------------------------ salario


def sal():
    return ('Sal\u00e1rio: bruto e l\u00edquido',
            [N.fld('Sal\u00e1rio bruto mensal (\u20ac)', '', '1000'),
             N.fld('Meses pagos por ano', '', '14'),
             N.fld('Horas de trabalho por semana', '', '40'),
             N.fld('Taxa de reten\u00e7\u00e3o na fonte (%)', '', '', 'o'),
             N.fld('Outros descontos (%) (ex.: ADSE 3,5)', '', '', 'o'),
             N.fld('Horas extra num dia \u00fatil (opcional)', '', '', 'o')],
            _sal)


def _sal(v):
    B, me, h, tr, to, he = v
    B = B[0]
    N.pos(B, 'O sal\u00e1rio bruto')
    me = inteiro(me[0], 'O n\u00famero de meses', 12, 14)
    h = h[0]
    N.need(0 < h <= 60, 'As horas por semana t\u00eam de estar entre 0 e 60')
    ss = B * SS_T / 100
    o = ['= Seguran\u00e7a Social (' + pc(SS_T) + '): ' + eur(B) + ' ' + X + ' ' +
         N.fmt(SS_T / 100, 0, 4) + ' = ' + eur(ss)]
    d = ss
    if tr is not None:
        r = B * taxa(tr[0], 'A taxa de reten\u00e7\u00e3o')
        o.append('= Reten\u00e7\u00e3o na fonte de IRS (' + pc(tr[0]) + '): ' + eur(r))
        d += r
    if to is not None:
        r = B * taxa(to[0], 'A taxa dos outros descontos')
        o.append('= Outros descontos (' + pc(to[0]) + '): ' + eur(r))
        d += r
    N.need(d <= B, 'Os descontos n\u00e3o podem ser maiores do que o sal\u00e1rio')
    L = B - d
    o += ['> Sal\u00e1rio l\u00edquido mensal: ' + eur(B) + ' - ' + eur(d) + ' = ' +
          eur(L),
          'Bruto anual: ' + str(me) + ' ' + X + ' ' + eur(B) + ' = ' + eur(me * B),
          'L\u00edquido anual (descontos iguais todos os meses): ' + eur(me * L),
          'Entidade empregadora: Seg. Social ' + pc(SS_E) + ' = ' +
          eur(B * SS_E / 100) + '; custo mensal ' + eur(B * (1 + SS_E / 100))]
    rh = B * 12 / (52 * h)
    o.append('Valor da hora: (' + eur(B) + ' ' + X + ' 12) / (52 ' + X + ' ' +
             N.fmt(h) + ') = ' + eur(rh))
    if he is not None:
        e = he[0]
        N.need(0 < e <= 12, 'As horas extra num dia t\u00eam de estar entre 0 e 12')
        p1 = min(e, 1) * rh * 1.25
        p2 = max(e - 1, 0) * rh * 1.375
        o.append('Horas extra (dia \u00fatil): 1.\u00aa hora + 25%, seguintes + 37,5%: ' +
                 eur(p1) + (' + ' + eur(p2) if p2 else '') + ' = ' + eur(p1 + p2))
    st = 'L\u00edquido = bruto - descontos (Seguran\u00e7a Social ' + pc(SS_T) + \
        ', reten\u00e7\u00e3o de IRS, outros).\nValor da hora (C\u00f3digo do ' \
        'Trabalho, art. 271.\u00ba): (sal\u00e1rio mensal ' + X + ' 12) / (52 ' + X + \
        ' horas por semana).\nTrabalho suplementar em dia \u00fatil (art. 268.\u00ba, ' \
        'at\u00e9 100 h por ano): + 25% na 1.\u00aa hora e + 37,5% nas seguintes.\n' \
        'A entidade empregadora paga mais ' + pc(SS_E) + ' \u00e0 Seguran\u00e7a Social.'
    return ('\n'.join(o), st, L, '\u20ac')

# ------------------------------------------------------------ IRS


def irs():
    return ('IRS por escal\u00f5es',
            [N.fld('Rendimento colet\u00e1vel anual (\u20ac)', '', '20000'),
             N.fld('Tabela', '', '', 'c', ['IRS ' + IRS_ANO + ' (escal\u00f5es)',
                                           'taxa \u00fanica manual']),
             N.fld('Taxa manual (%)', '', '', 'o'),
             N.fld('Reten\u00e7\u00f5es feitas no ano (\u20ac) (opcional)', '', '', 'o')],
            _irs)


def _irs(v):
    R, md, tm, rt = v
    R = R[0]
    N.nneg(R, 'O rendimento colet\u00e1vel')
    o = []
    gr = None
    if md == 1:
        N.need(tm is not None, 'Escreve a taxa manual (%)')
        t = taxa(tm[0], 'A taxa')
        c = R * t
        o.append('> Coleta: ' + eur(R) + ' ' + X + ' ' + pc(tm[0]) + ' = ' + eur(c))
    else:
        lo = 0
        k = escalao(R)
        for j in range(k + 1):
            hi = IRS_LIM[j] if j < len(IRS_LIM) else R
            p = min(R, hi) - lo
            if p > 0:
                o.append(str(j + 1) + '.\u00ba escal\u00e3o: ' + eur(p) + ' ' + X + ' ' +
                         pc(IRS_TX[j]) + ' = ' + eur(p * IRS_TX[j] / 100))
            lo = hi
        c = coleta(R)
        o.append('> Coleta: ' + eur(c))
        lo = IRS_LIM[k - 1] if k else 0
        hi = IRS_LIM[k] if k < len(IRS_LIM) else None
        o.append('Escal\u00e3o: ' + str(k + 1) + '.\u00ba (' + ('mais de ' + grp(str(lo)) +
                 ' \u20ac' if hi is None else ('at\u00e9 ' if k == 0 else grp(str(lo)) +
                                              ' a ') + grp(str(hi)) + ' \u20ac') +
                 '); taxa marginal ' + pc(IRS_TX[k]))
        if R > 0:
            o.append('Taxa m\u00e9dia: ' + eur(c)[:-2] + ' / ' + eur(R)[:-2] + ' = ' +
                     pc(100 * c / R))
        pa = lo * IRS_TX[k] / 100 - coleta(lo)
        o.append('Com a parcela a abater: ' + eur(R)[:-2] + ' ' + X + ' ' +
                 pc(IRS_TX[k]) + ' - ' + eur(pa)[:-2] + ' = ' +
                 eur(R * IRS_TX[k] / 100 - pa))
        if R > 80000:
            o.append('! Acima de 80 000 \u20ac h\u00e1 ainda a taxa adicional de '
                     'solidariedade (art. 68.\u00ba-A), que aqui n\u00e3o entra.')
        o.append('Tabela: IRS ' + IRS_ANO + ', ' + IRS_FONTE + '. Confirma no '
                 'Portal das Finan\u00e7as.')
        xm = max(2 * R, 50000)
        gr = ('Taxas de IRS ' + IRS_ANO + ' (%)',
              [('f', lambda x: IRS_TX[escalao(x)], 4),
               ('f', lambda x: 100 * coleta(x) / x if x > 0 else IRS_TX[0], 5),
               ('p', [(R, 100 * c / R if R > 0 else IRS_TX[0])], 6)],
              0, xm, 0, 50, 'degraus: taxa marginal; curva: taxa m\u00e9dia; '
              'ponto: o teu rendimento')
    if rt is not None:
        N.nneg(rt[0], 'As reten\u00e7\u00f5es')
        d = c - rt[0]
        o.append('Coleta - reten\u00e7\u00f5es = ' + eur(d) + (
            ': a pagar' if d > 0.005 else (': reembolso' if d < -0.005 else
                                           ': nada a acertar')))
    o.append('Sem dedu\u00e7\u00f5es \u00e0 coleta nem m\u00ednimo de exist\u00eancia.')
    st = 'O IRS \u00e9 progressivo: cada parte do rendimento paga a taxa do seu ' \
        'escal\u00e3o (taxa marginal); a taxa m\u00e9dia \u00e9 coleta / rendimento.\n' \
        'Rendimento colet\u00e1vel: o que fica depois das dedu\u00e7\u00f5es ' \
        'espec\u00edficas.\nParcela a abater: coleta = R ' + X + ' taxa - parcela.'
    if gr:
        return ('\n'.join(o), st, c, '\u20ac', gr)
    return ('\n'.join(o), st, c, '\u20ac')

# ------------------------------------------------------------ juros


def jur():
    return ('Juros simples e compostos',
            [N.fld('Capital inicial (\u20ac)', '', '1000'),
             N.fld('Taxa de juro anual (%)', '', '3'),
             N.fld('Tempo (anos)', '', '5'),
             N.fld('Regime', '', '', 'c', ['composto', 'simples']),
             N.fld('Capitaliza\u00e7\u00f5es por ano (composto)', '', '1'),
             N.fld('Imposto sobre os juros (%) (opcional)', '', '', 'o')], _jur)


def _jur(v):
    C, r, t, rg, k, im = v
    C = C[0]
    N.pos(C, 'O capital')
    r = taxa(r[0], 'A taxa de juro')
    t = t[0]
    N.pos(t, 'O tempo')
    tx = taxa(im[0], 'O imposto') if im is not None else 0.0
    o = []
    if rg == 1:
        J = C * r * t
        Cn = C + J
        o += ['= J = C ' + X + ' r ' + X + ' t = ' + eur(C) + ' ' + X + ' ' +
              pc(100 * r) + ' ' + X + ' ' + N.fmt(t) + ' = ' + eur(J),
              '> Capital final: ' + eur(Cn)]
        f = None
        if tx:
            o.append('Juro l\u00edquido (imposto de ' + pc(100 * tx) + '): ' +
                     eur(J * (1 - tx)) + '; capital ' + eur(C + J * (1 - tx)))
    else:
        k = inteiro(k[0], 'O n\u00famero de capitaliza\u00e7\u00f5es', 1, 365)
        n = k * t
        N.need(abs(n - round(n)) < 1e-9, 'O tempo tem de dar um n\u00famero inteiro '
               'de per\u00edodos (' + str(k) + ' por ano)')
        n = int(round(n))
        i = r / k
        Cn = C * (1 + i) ** n
        J = Cn - C
        o += ['= i = ' + pc(100 * r) + ' / ' + str(k) + ' = ' + pc(100 * i) + '; n = ' +
              str(n) + ' per\u00edodos',
              '= Cn = C ' + X + ' (1 + i)^n',
              '> Capital final: ' + eur(Cn) + '; juro ' + eur(J)]
        for j in list(range(1, min(n, 3) + 1)) + ([n] if n > 3 else []):
            o.append(' ap\u00f3s ' + str(j) + ' per\u00edodo' + ('s' if j > 1 else '') +
                     ': ' + eur(C * (1 + i) ** j))
        if k > 1:
            o.append('Taxa anual efetiva: (1 + i)^' + str(k) + ' - 1 = ' +
                     pc(100 * ((1 + i) ** k - 1)))
        if tx:
            il = i * (1 - tx)
            o.append('Com imposto de ' + pc(100 * tx) + ' em cada capitaliza\u00e7\u00e3o: '
                     'capital ' + eur(C * (1 + il) ** n) + '; juro l\u00edquido ' +
                     eur(C * (1 + il) ** n - C))
        o.append('Em juro simples seria: ' + eur(C * (1 + r * t)))
        f = (lambda x: C * (1 + i) ** (k * x))
    its = [('f', lambda x: C * (1 + r * x), 4)]
    leg = 'reta: juro simples'
    if f:
        its.append(('f', f, 5))
        leg += '; curva: juro composto'
    gr = ('Capital (\u20ac) ao longo do tempo (anos)', its, 0, t, 0,
          max(Cn, C * (1 + r * t)) * 1.1, leg)
    st = 'Juro simples: o juro de cada ano \u00e9 sempre C ' + X + ' r.\nJuro ' \
        'composto: o juro junta-se ao capital e tamb\u00e9m rende; com k ' \
        'capitaliza\u00e7\u00f5es por ano, i = r / k.\nEm Portugal, os juros de ' \
        'dep\u00f3sitos pagam IRS \u00e0 taxa liberat\u00f3ria de 28% (confirmar).'
    return ('\n'.join(o), st, Cn, '\u20ac', gr)

# ------------------------------------------------------------ prestacoes


def prest():
    return ('Presta\u00e7\u00f5es e valor atual (aprofundamento)',
            [N.fld('Calcular', '', '', 'c', ['a presta\u00e7\u00e3o', 'o valor atual']),
             N.fld('Empr\u00e9stimo ou valor atual (\u20ac)', '', '10000', 'o'),
             N.fld('Presta\u00e7\u00e3o (\u20ac)', '', '', 'o'),
             N.fld('Taxa de juro anual (%)', '', '6'),
             N.fld('Prazo (anos)', '', '5'),
             N.fld('Presta\u00e7\u00f5es por ano', '', '12')], _prest)


def _prest(v):
    md, va, p, r, t, k = v
    r = taxa(r[0], 'A taxa de juro')
    t = t[0]
    N.pos(t, 'O prazo')
    k = inteiro(k[0], 'O n\u00famero de presta\u00e7\u00f5es por ano', 1, 52)
    n = k * t
    N.need(abs(n - round(n)) < 1e-9, 'O prazo tem de dar um n\u00famero inteiro '
           'de presta\u00e7\u00f5es')
    n = int(round(n))
    i = r / k
    a = n if i == 0 else (1 - (1 + i) ** -n) / i
    o = ['= i = ' + pc(100 * r) + ' / ' + str(k) + ' = ' + pc(100 * i) + '; n = ' +
         str(n) + ' presta\u00e7\u00f5es']
    if md == 0:
        N.need(va is not None, 'Escreve o valor do empr\u00e9stimo')
        V = va[0]
        N.pos(V, 'O empr\u00e9stimo')
        P = V / a
        o += ['= p = V ' + X + ' i / (1 - (1 + i)^(-n))',
              '> Presta\u00e7\u00e3o: ' + eur(P)]
        res = P
    else:
        N.need(p is not None, 'Escreve o valor da presta\u00e7\u00e3o')
        P = p[0]
        N.pos(P, 'A presta\u00e7\u00e3o')
        V = P * a
        o += ['= V = p ' + X + ' (1 - (1 + i)^(-n)) / i',
              '> Valor atual: ' + eur(V)]
        res = V
    o += ['Total pago: ' + str(n) + ' ' + X + ' ' + eur(P) + ' = ' + eur(n * P),
          'Juros pagos: ' + eur(n * P - V)]
    D = V
    for j in range(1, min(n, 3) + 1):
        ju = D * i
        D -= P - ju
        o.append(' ' + str(j) + '.\u00aa: juro ' + eur(ju) + ' ' + MS + ' amortiza ' +
                 eur(P - ju) + ' ' + MS + ' fica ' + eur(max(D, 0.0)))
    st = 'Presta\u00e7\u00f5es constantes: cada presta\u00e7\u00e3o paga o juro da ' \
        'd\u00edvida e amortiza o resto.\nValor atual: quanto vale hoje uma ' \
        's\u00e9rie de presta\u00e7\u00f5es futuras.\n(Aprofundamento.)'
    return ('\n'.join(o), st, res, '\u20ac')
