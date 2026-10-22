# c_comu.py - M1TR4M: calculadoras comuns (cientifica, algarismos
# significativos, conversor de unidades e prefixos do SI).
# Catalogo (lido pelo build): id|nome|palavras-chave|disciplina|tema
#@ c_comu.sci|Calculadora cient\u00edfica|express\u00e3o pot\u00eancia raiz seno cosseno tangente pi fra\u00e7\u00e3o|C|
#@ c_comu.sf|Algarismos significativos|algarismos significativos arredondar soma produto regra|C|
#@ c_comu.uni|Conversor de unidades|unidades convers\u00e3o comprimento massa volume temperatura energia press\u00e3o|C|
#@ c_comu.pre|Prefixos do SI|prefixos quilo mili micro nano mega giga pot\u00eancias de dez|C|
# Casos-limite: express\u00e3o vazia, simbolo desconhecido, divisao por zero,
# raiz de negativo, valores enormes (1e400); numeros com zeros a esquerda
# e a direita; regra da soma com casas decimais negativas (1,2 x 10^3);
# temperatura em graus Celsius (soma 273,15).

import math
import m1_nucleo as N
import m1_ui as U

X = N.X


def sci():
    return ('Calculadora cient\u00edfica',
            [N.fld('Express\u00e3o (ex.: 2^10+\u221a2, sen 30)', '', '', 't')], _sci)


def _sci(v):
    e = v[0]
    if not e:
        N.err('Escreve uma express\u00e3o, por exemplo 2^10 + sqrt(2)')
    r = N.ev(N.comp(e, 0))
    a = 'graus' if N.CF['ang'] == 0 else 'radianos'
    t = '= ' + e + '\n> ' + N.rhs(r, 10) + '\n\nUnidade angular: ' + a + \
        ' (muda nas Defini\u00e7\u00f5es).'
    return (t, 'O valor exato aparece quando \u00e9 uma fra\u00e7\u00e3o, uma raiz ou '
            'um m\u00faltiplo de \u03c0; o aproximado tem as casas das '
            'Defini\u00e7\u00f5es (aqui at\u00e9 10).', r, '')

# ------------------------------------------------------------ alg. sig.


def info(s):
    # (valor, alg. sig., casas decimais efetivas, mantissa, expoente).
    v, sf = N.num(s)
    if sf == 0:
        N.err('Escreve n\u00fameros decimais (n\u00e3o fra\u00e7\u00f5es): ' + s)
    t = N._clean(s).lstrip('+-')
    j = 0
    while j < len(t) and (N.dig(t[j]) or t[j] in ',.'):
        j += 1
    mant = t[:j]
    m = N._dn(mant)
    ex = 0
    if m != 0 and v != 0:
        ex = int(math.floor(math.log(abs(v) / m) / N.LN10 + 0.5))
    return v, sf, N.dps(mant) - ex, mant, ex


def sf():
    return ('Algarismos significativos',
            [N.fld('Opera\u00e7\u00e3o', '', '', 'c',
                   ['contar e arredondar', 'soma', 'subtra\u00e7\u00e3o (1.\u00ba - restantes)',
                    'multiplica\u00e7\u00e3o', 'divis\u00e3o (1.\u00ba / restantes)']),
             N.fld('N\u00fameros (separa com espa\u00e7os)', '', '0,0250 12,3', 't'),
             N.fld('Arredondar a (alg. sig., opcional)', '', '', 'o')], _sf)


def why(mant):
    # Explicacao das regras para uma mantissa escrita.
    d = mant.replace('.', ',')
    g = d.replace(',', '')
    lz = len(g) - len(g.lstrip('0'))
    o = []
    if lz and g.strip('0'):
        o.append(str(lz) + ' zero(s) \u00e0 esquerda n\u00e3o contam')
    tz = len(g) - len(g.rstrip('0'))
    if tz and g.strip('0'):
        if ',' in d:
            o.append(str(tz) + ' zero(s) \u00e0 direita, depois da v\u00edrgula, contam')
        else:
            o.append(str(tz) + ' zero(s) \u00e0 direita sem v\u00edrgula s\u00e3o '
                     'amb\u00edguos (contados); usa nota\u00e7\u00e3o cient\u00edfica')
    return '; '.join(o)


def _sf(v):
    op, txt, rn = v
    ps = N.lst(txt)
    if not ps:
        N.err('Escreve pelo menos um n\u00famero')
    xs = [info(p) for p in ps]
    o = []
    if op == 0:
        for p, x in zip(ps, xs):
            s = p + ': ' + str(x[1]) + ' alg. sig.'
            w = why(x[3])
            if w:
                s = s + ' (' + w + ')'
            o.append('- ' + s)
            if rn is not None:
                n = int(rn[0])
                N.need(n >= 1 and n == rn[0], 'Arredonda a um n\u00famero inteiro '
                       'de algarismos (1, 2, 3...)')
                o.append('> arredondado a ' + str(n) + ': ' + N.fsf(x[0], n))
        return ('\n'.join(o), 'Regras: contam todos os algarismos diferentes '
                'de zero, os zeros entre eles e os zeros \u00e0 direita depois da '
                'v\u00edrgula. Os zeros \u00e0 esquerda s\u00f3 marcam a posi\u00e7\u00e3o.',
                None, '')
    N.need(len(xs) >= 2, 'Escreve pelo menos dois n\u00fameros')
    if op in (1, 2):
        # Conta exata em decimal: inteiros na escala 10^D.
        D = max([x[2] for x in xs] + [0])
        S = 0
        for i in range(len(xs)):
            k = int(N._rnd(abs(N._sc(xs[i][0], D))))
            k = -k if xs[i][0] < 0 else k
            S = S + k if (op == 1 or i == 0) else S - k
        r = S / N._p10(D) if D <= 22 else N._sc(float(S), -D)
        d = min([x[2] for x in xs])
        if d >= 0:
            q = 10 ** (D - d)
            m = (abs(S) + q // 2) // q
            s = ('-' if S < 0 and m else '') + N._ds(m, d)
        else:
            n = N._e10(abs(r)) + d + 1 if r != 0 else 1
            s = N.fsf(r, max(1, n))
        t = (' + ' if op == 1 else ' - ').join(ps)
        o.append('= ' + t + ' = ' + N.fmt(r, 0, 12))
        o.append('Regra da ' + ('soma' if op == 1 else 'subtra\u00e7\u00e3o') +
                 ': o resultado fica com as casas decimais do dado com menos '
                 'casas (' + str(d) + ').')
        o.append('> ' + s)
        return ('\n'.join(o), '', N.num(s)[0], '')
    r = xs[0][0]
    for x in xs[1:]:
        if op == 3:
            r = r * x[0]
        else:
            N.need(x[0] != 0, 'Divis\u00e3o por zero')
            r = r / x[0]
    n = min([x[1] for x in xs])
    t = (' ' + X + ' ' if op == 3 else ' / ').join(ps)
    o.append('= ' + t + ' = ' + N.fmt(r, 0, 12))
    o.append('Regra do produto e do quociente: o resultado fica com os '
             'algarismos significativos do dado com menos (' + str(n) + ').')
    s = N.fsf(r, n)
    o.append('> ' + s)
    return ('\n'.join(o), '', N.num(s)[0], '')

# ------------------------------------------------------------ unidades
CATS = (('L', 'Comprimento'), ('M', 'Massa'), ('t', 'Tempo'),
        ('A', '\u00c1rea'), ('V', 'Volume'), ('T', 'Temperatura'),
        ('E', 'Energia'), ('W', 'Pot\u00eancia'), ('p', 'Press\u00e3o'),
        ('n', 'Quantidade de mat\u00e9ria'), ('c', 'Concentra\u00e7\u00e3o'),
        ('m', 'Concentra\u00e7\u00e3o m\u00e1ssica'), ('d', 'Massa vol\u00famica'),
        ('v', 'Velocidade'), ('F', 'For\u00e7a'), ('I', 'Corrente el\u00e9trica'),
        ('U', 'Diferen\u00e7a de potencial'), ('R', 'Resist\u00eancia el\u00e9trica'),
        ('f', 'Frequ\u00eancia'), ('Q', 'Carga el\u00e9trica'))


def uni():
    r = U.menu('Conversor de unidades', [c[1] for c in CATS])
    if r < 0:
        return None
    cat = CATS[r][0]
    us = N.ulist(cat)
    f = N.fld('Valor', ' '.join(us), '1')
    return (CATS[r][1], [f, N.fld('Converter para', '', '', 'c', us)],
            lambda v: _uni(v, cat, us, f))


def _uni(v, cat, us, f):
    x = v[0][0]
    u0 = us[0]
    ui = us[f[3]]
    uo = us[v[1]]
    r = N.conv(x, u0, uo, cat)
    xi = N.conv(x, u0, ui, cat)
    s = N.fmt(xi, 0, 12) + ' ' + ui
    o = ['= ' + s + ' = ' + N.fmt(r, 0, 12) + ' ' + uo]
    if cat == 'T':
        o.append('T (K) = \u03b8 (\u00b0C) + 273,15')
    else:
        k = N.conv(1.0, ui, uo, cat)
        o.append('1 ' + ui + ' = ' + N.fmt(k, 0, 12) + ' ' + uo)
    sf = v[0][1]
    if sf:
        o.append('> ' + N.fsf(r, sf) + ' ' + uo + ' (' + str(sf) + ' alg. sig.)')
    return ('\n'.join(o), 'Para converter, multiplica-se pelo fator de '
            'convers\u00e3o (uma fra\u00e7\u00e3o igual a 1).', r, uo)


PREF = ('tera T 10\u00b9\u00b2', 'giga G 10\u2079', 'mega M 10\u2076', 'quilo k 10\u00b3',
        'hecto h 10\u00b2', 'deca da 10\u00b9', 'deci d 10\u207b\u00b9',
        'centi c 10\u207b\u00b2', 'mili m 10\u207b\u00b3', 'micro \u00b5 10\u207b\u2076',
        'nano n 10\u207b\u2079', 'pico p 10\u207b\u00b9\u00b2', 'femto f 10\u207b\u00b9\u2075')


def pre():
    return ('Prefixos do SI', [], _pre)


def _pre(v):
    o = ['Prefixo, s\u00edmbolo e fator:']
    for p in PREF:
        a = p.split(' ')
        o.append('- ' + a[0] + ' (' + a[1] + ') = ' + a[2])
    o.append('Exemplo: 2,5 km = 2,5 ' + X + ' 10\u00b3 m; 3 mL = 3 ' + X +
             ' 10\u207b\u00b3 L.')
    return ('\n'.join(o), '', None, '')
