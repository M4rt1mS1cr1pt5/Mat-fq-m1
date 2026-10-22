# c_comd.py - M1TR4M: calculadoras comuns de dados (constantes, dados
# experimentais com incerteza, regressao linear e grafico).
#@ c_comd.cte|Constantes e dados|constantes avogadro planck velocidade da luz volume molar g exame|C|
#@ c_comd.exp|Dados experimentais|m\u00e9dia incerteza absoluta relativa erro percentual exatid\u00e3o precis\u00e3o|C|
#@ c_comd.reg|Regress\u00e3o linear e gr\u00e1fico|regress\u00e3o reta declive ordenada coeficiente de correla\u00e7\u00e3o gr\u00e1fico interpolar|C|
# Casos-limite: um so valor (sem incerteza estatistica), todos os x
# iguais (sem reta), todos os y iguais (r nao definido), dois pontos
# (r = 1 ou -1), valor de referencia zero (erro percentual impossivel),
# listas de tamanhos diferentes, extrapolacao fora dos dados.

import math
import m1_nucleo as N
import m1_ui as U

X = N.X
# --- dados (gerado) ---
CTE = "Velocidade de propaga\xe7\xe3o da luz no v\xe1cuo|c|3,00 \xd7 10\u2078|m s\u207b\xb9|IAVE, Tabela de\
 Constantes do exame de FQ A (715)|2024 (confirmar)\n\
M\xf3dulo da acelera\xe7\xe3o grav\xedtica junto \xe0 superf\xedcie da Terra|g|10|m s\u207b\xb2|IAVE, Tabela\
 de Constantes do exame de FQ A (715)|2024 (confirmar)\n\
Constante de gravita\xe7\xe3o universal|G|6,67 \xd7 10\u207b\xb9\xb9|N m\xb2 kg\u207b\xb2|IAVE, Tabela de\
 Constantes do exame de FQ A (715)|2024 (confirmar)\n\
Constante de Avogadro|NA|6,02 \xd7 10\xb2\xb3|mol\u207b\xb9|IAVE, Tabela de Constantes do exame de FQ A\
 (715)|2024 (confirmar)\n\
Constante de Stefan-Boltzmann|\u03c3|5,67 \xd7 10\u207b\u2078|W m\u207b\xb2 K\u207b\u2074|IAVE, Tabela de\
 Constantes do exame de FQ A (715); extens\xe3o no 10.\xba ano|2024 (confirmar)\n\
Produto i\xf3nico da \xe1gua (25 \xb0C)|Kw|1,00 \xd7 10\u207b\xb9\u2074||IAVE, Tabela de Constantes do exame\
 de FQ A (715); mat\xe9ria do 11.\xba ano|2024 (confirmar)\n\
Volume molar de um g\xe1s (PTN)|Vm|22,4|dm\xb3 mol\u207b\xb9|IAVE, Tabela de Constantes do exame de FQ A\
 (715)|2024 (confirmar)\n\
Constante de Planck|h|6,63 \xd7 10\u207b\xb3\u2074|J s|valor arredondado; CODATA: 6,626 070 15 \xd7\
 10\u207b\xb3\u2074 J s (exato)|2018\n\
Carga elementar|e|1,60 \xd7 10\u207b\xb9\u2079|C|valor arredondado; CODATA: 1,602 176 634 \xd7\
 10\u207b\xb9\u2079 C (exato)|2018\n\
Eletr\xe3o-volt|eV|1,60 \xd7 10\u207b\xb9\u2079|J|1 eV = e \xd7 1 V; CODATA|2018\n\
Unidade de massa at\xf3mica|u|1,66 \xd7 10\u207b\xb2\u2077|kg|valor arredondado; CODATA: 1,660 539 066 60\
 \xd7 10\u207b\xb2\u2077 kg|2018\n\
Acelera\xe7\xe3o grav\xedtica padr\xe3o|gn|9,80665|m s\u207b\xb2|valor convencional (3.\xaa CGPM)|1901\n\
Energia do eletr\xe3o no n\xedvel n do \xe1tomo de hidrog\xe9nio|En|-2,18 \xd7\
 10\u207b\xb9\u2078/n\xb2|J|modelo de Bohr (valor usado nos manuais)|\u2014\n\
Capacidade t\xe9rmica m\xe1ssica da \xe1gua l\xedquida|c|4,18 \xd7 10\xb3|J kg\u207b\xb9 K\u207b\xb9|valor\
 usado nos manuais (varia com a temperatura)|\u2014\n\
Varia\xe7\xe3o de entalpia (m\xe1ssica) de fus\xe3o do gelo|\u0394Hf|3,34 \xd7 10\u2075|J kg\u207b\xb9|valor\
 tabelado a 0 \xb0C|\u2014\n\
Varia\xe7\xe3o de entalpia (m\xe1ssica) de vaporiza\xe7\xe3o da \xe1gua|\u0394Hv|2,26 \xd7 10\u2076|J\
 kg\u207b\xb9|valor tabelado a 100 \xb0C|\u2014\n\
Massa vol\xfamica da \xe1gua (4 \xb0C)|\u03c1|1,00 \xd7 10\xb3|kg m\u207b\xb3|valor arredondado|\u2014\n\
Press\xe3o normal (1 atm)|p|1,01325 \xd7 10\u2075|Pa|valor convencional|\u2014\n\
Zero da escala Celsius em kelvin|T0|273,15|K|defini\xe7\xe3o da escala Celsius|\u2014"
# --- fim dos dados ---


def cte():
    cs = [c.split('|') for c in CTE.split('\n') if c]
    sel = 0
    while True:
        r = U.menu('Constantes e dados', [c[1] + ': ' + c[0] for c in cs], sel)
        if r < 0:
            return None
        sel = r
        c = cs[r]
        s = '# ' + c[0] + '\n= ' + c[1] + ' = ' + c[2] + \
            (' ' + c[3] if c[3] else '') + '\nFonte: ' + c[4] + \
            ('\nAno: ' + c[5] if c[5] and c[5] != '\u2014' else '')
        try:
            val = N.num(c[2].replace(' ', ''))[0]
        except ValueError:
            val = None
        k = U.text('Constante', s + ('\n\n1: usar como ans' if val is not None
                                     else ''), '', '', ('1',))
        if k == '1' and val is not None:
            N.CF['ans'] = val
            U.msg('Constante', 'ans = ' + c[2] + '. Escreve ans num campo '
                  'de uma calculadora.')

# ------------------------------------------------------------ dados


def exp():
    return ('Dados experimentais',
            [N.fld('Valores medidos (separa com ;)', '', '', 't'),
             N.fld('Unidade (opcional)', '', '', 't'),
             N.fld('Incerteza de leitura (opcional)', '', '', 'o'),
             N.fld('Valor de refer\u00eancia (opcional)', '', '', 'o')], _exp)


def ndec(s):
    # Casas decimais de um valor escrito (para a media).
    t = N._clean(s)
    for c in 'eE*x':
        if c in t:
            return -1
    return N.dps(t.lstrip('+-'))


def _exp(v):
    txt, un, il, ref = v
    ps = N.lst(txt)
    N.need(len(ps) >= 1, 'Escreve os valores medidos separados por ;')
    xs = [N.num(p)[0] for p in ps]
    n = len(xs)
    m = sum(xs) / n
    ds = [abs(x - m) for x in xs]
    dm = max(ds)
    u = (' ' + un) if un else ''
    o = ['= m\u00e9dia = (' + ' + '.join(ps) + ') / ' + str(n),
         '> m\u00e9dia ' + N.eq(m, 0, -1) + u]
    st = ['Desvios |x(i) - m\u00e9dia|:']
    for p, d in zip(ps, ds):
        st.append('- ' + p + ': ' + N.fmt(d, 0, 6))
    inc = dm
    src = 'maior desvio'
    if il is not None and il[0] > inc:
        inc = il[0]
        src = 'incerteza de leitura (maior do que os desvios)'
    if n == 1 and il is None:
        o.append('Com um s\u00f3 valor, indica a incerteza de leitura do '
                 'instrumento.')
        return ('\n'.join(o), '', m, un)
    o.append('Incerteza absoluta = ' + src + ' = ' + N.fmt(inc, 0, 6) + u)
    if inc > 0:
        e = N._e10(inc)
        i1 = N._sc(float(N._rnd(N._sc(inc, -e) + 0.0)), e)
        if i1 < inc:
            i1 = N._sc(float(int(math.ceil(N._sc(inc, -e) - 1e-9))), e)
        d = max(0, -e)
        o.append('> x = (' + N.fmt2(m, 0, d, 0)[0] + ' \u00b1 ' +
                 N.fmt2(i1, 0, d, 0)[0] + ')' + u)
        o.append('(incerteza com 1 algarismo significativo, arredondada '
                 'por excesso; m\u00e9dia com as mesmas casas)')
        if m != 0:
            o.append('Incerteza relativa = ' + N.fmt(inc / abs(m) * 100, 0, 2) +
                     ' % (quanto menor, maior a precis\u00e3o)')
    if ref is not None:
        r = ref[0]
        ea = abs(m - r)
        o.append('Erro absoluto = |m\u00e9dia - x_ref| = ' + N.fmt(ea, 0, 6) + u)
        if r != 0:
            o.append('> Erro percentual = ' + N.fmt(ea / abs(r) * 100, 0, 2) +
                     ' % (quanto menor, maior a exatid\u00e3o)')
        else:
            o.append('Com valor de refer\u00eancia 0 n\u00e3o h\u00e1 erro percentual.')
    return ('\n'.join(o), '\n'.join(st), m, un)

# ------------------------------------------------------------ regressao


def reg():
    return ('Regress\u00e3o linear',
            [N.fld('Valores de x (separa com ;)', '', '', 'l'),
             N.fld('Valores de y (separa com ;)', '', '', 'l'),
             N.fld('Unidade de x (opcional)', '', '', 't'),
             N.fld('Unidade de y (opcional)', '', '', 't'),
             N.fld('Interpolar em x = (opcional)', '', '', 'o')], _reg)


def fit(xs, ys):
    # Reta dos minimos quadrados: (m, b, r); r e None se nao definido.
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum([(x - mx) ** 2 for x in xs])
    syy = sum([(y - my) ** 2 for y in ys])
    sxy = sum([(xs[i] - mx) * (ys[i] - my) for i in range(n)])
    N.need(sxx > 0, 'Todos os x s\u00e3o iguais: n\u00e3o h\u00e1 reta de regress\u00e3o')
    m = sxy / sxx
    b = my - m * mx
    r = sxy / math.sqrt(sxx * syy) if syy > 0 else None
    return m, b, r


def _reg(v):
    xs = [p[0] for p in v[0]]
    ys = [p[0] for p in v[1]]
    N.need(len(xs) == len(ys), 'H\u00e1 ' + str(len(xs)) + ' valores de x e ' +
           str(len(ys)) + ' de y: t\u00eam de ser tantos x como y')
    N.need(len(xs) >= 2, 'S\u00e3o precisos pelo menos 2 pontos')
    m, b, r = fit(xs, ys)
    ux, uy = v[2], v[3]
    um = (uy + '/' + ux) if ux and uy else (uy if uy else ('1/' + ux if ux
                                                           else ''))
    o = ['Reta dos m\u00ednimos quadrados:',
         '= y = m x + b',
         '> m ' + N.eq(m, 4) + (' ' + um if um else ''),
         '> b ' + N.eq(b, 4) + (' ' + uy if uy else ''),
         '> y = ' + N.fmt(m, 4) + ' x ' + ('+ ' + N.fmt(b, 4) if b >= 0 else
                                         '- ' + N.fmt(-b, 4))]
    if r is None:
        o.append('r n\u00e3o est\u00e1 definido (todos os y s\u00e3o iguais).')
    else:
        o.append('Coeficiente de correla\u00e7\u00e3o r ' + N.eq(r, 0, 4) +
                 (' (dois pontos: r = \u00b11 sempre)' if len(xs) == 2 else ''))
    o.append('(Em Matem\u00e1tica escreve-se y = a x + b.)')
    x0 = v[4]
    if x0 is not None:
        x = x0[0]
        y = m * x + b
        dentro = min(xs) <= x <= max(xs)
        o.append('> x = ' + N.fmt(x) + ': y ' + N.eq(y, 4) + (' ' + uy if uy
                                                            else ''))
        o.append('Interpola\u00e7\u00e3o (dentro dos dados).' if dentro else
                 '! Extrapola\u00e7\u00e3o: x est\u00e1 fora dos dados; a previs\u00e3o '
                 'pode n\u00e3o valer.')
    x0_, x1_ = min(xs), max(xs)
    y0_, y1_ = min(ys), max(ys)
    dx = (x1_ - x0_) * 0.15 or 1.0
    dy = (y1_ - y0_) * 0.15 or 1.0
    g = ('Regress\u00e3o', [('p', list(zip(xs, ys)), 5),
                          ('f', lambda x: m * x + b, 2)],
         x0_ - dx, x1_ + dx, y0_ - dy, y1_ + dy,
         'pontos: dados \u00b7 linha: reta de regress\u00e3o')
    st = 'M\u00e9dia dos x = ' + N.fmt(sum(xs) / len(xs)) + \
        '; m\u00e9dia dos y = ' + N.fmt(sum(ys) / len(ys)) + '.\n' \
        'm = Sxy / Sxx e b = (m\u00e9dia dos y) - m ' + X + \
        ' (m\u00e9dia dos x).\nA reta passa no ponto (m\u00e9dia dos x; ' \
        'm\u00e9dia dos y).'
    return ('\n'.join(o), st, m, um, g)
