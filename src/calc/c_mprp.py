# c_mprp.py - M1TR4M: resolvedores de sequencias e proporcionalidade (7.o
# ao 9.o ano): termo geral de uma sequencia (aritmetica, quadratica ou
# geometrica), proporcionalidade direta e inversa (constante, tabela com
# valores em falta, grafico) e percentagens.
#@ c_mprp.seq|Sequ\u00eancias: termo geral|sequ\u00eancia regularidade termo geral lei de forma\u00e7\u00e3o termo de ordem n diferen\u00e7as constantes raz\u00e3o \u00e9 termo|M|a7
#@ c_mprp.prop|Proporcionalidade direta|proporcionalidade direta constante de proporcionalidade y = kx regra de tr\u00eas tabela valores em falta reta pela origem|M|a7
#@ c_mprp.inv|Proporcionalidade inversa|proporcionalidade inversa constante k = xy y = k/x hip\u00e9rbole tabela valores em falta|M|a9
#@ c_mprp.perc|Percentagens|percentagem aumento desconto valor inicial varia\u00e7\u00e3o percentual iva por cento|M|a7
# Casos-limite: menos de 3 termos, termos que nao seguem regra simples,
# x = 0 na proporcionalidade, valores so com "?", desconto de 100% ou mais,
# valor inicial nulo.

import m1_nucleo as N
import m1_q as Q


def numeros(t, nm, falta=False):
    out = []
    for p in t.replace(';', ' ').split():
        if falta and p == '?':
            out.append(None)
        else:
            c = Q.cte(Q.poli(Q.arvore(p)))
            N.need(c is not None, nm + ': s\u00f3 n\u00fameros' + (' ou ?' if falta
                                                        else ''))
            out.append(c)
    return out


def sub(i):
    return ''.join([chr(0x2080 + int(c)) for c in str(i)])

# ------------------------------------------------------------ sequencias


def seq():
    return ('Sequ\u00eancias: termo geral',
            [N.fld('Primeiros termos', '', '3 7 11 15', 't'),
             N.fld('Termo de ordem n (opcional)', '', '', 'o'),
             N.fld('Este n\u00famero \u00e9 termo? (opcional)', '', '', 't')], _seq)


def _seq(v):
    us = numeros(v[0], 'Os termos')
    N.need(len(us) >= 3, 'Escreve pelo menos 3 termos')
    ds = [Q.sub(us[i + 1], us[i]) for i in range(len(us) - 1)]
    o = ['Diferen\u00e7as entre termos seguidos: ' + ', '.join([Q.qs(d) for d in ds])]
    tipo = None
    if all_eq(ds):
        d = ds[0]
        G = Q.decoefs([Q.sub(us[0], d), d], 'n')
        o.append('Diferen\u00e7a constante ' + Q.qs(d) + ': sequ\u00eancia aritm\u00e9tica.')
        o.append('Lei de recorr\u00eancia: u(n+1) = u(n) ' + ('+ ' + Q.qs(d) if
                                                       d[0] >= 0 else '- ' +
                                                       Q.qs(Q.neg(d))))
        tipo = 'a'
    else:
        d2 = [Q.sub(ds[i + 1], ds[i]) for i in range(len(ds) - 1)]
        if len(us) >= 4 and all_eq(d2):
            a = Q.div(d2[0], (2, 1))
            b = Q.sub(Q.sub(us[1], us[0]), Q.mul((3, 1), a))
            c = Q.sub(Q.sub(us[0], a), b)
            G = Q.decoefs([c, b, a], 'n')
            o.append('Segundas diferen\u00e7as constantes (' + Q.qs(d2[0]) +
                     '): o termo geral \u00e9 do 2.\u00ba grau em n.')
            tipo = 'q'
        elif not [u for u in us if u[0] == 0]:
            rs = [Q.div(us[i + 1], us[i]) for i in range(len(us) - 1)]
            N.need(all_eq(rs), 'N\u00e3o encontrei uma regra simples (nem '
                   'diferen\u00e7as constantes, nem raz\u00e3o constante)')
            r = rs[0]
            o.append('Raz\u00e3o constante ' + Q.qs(r) + ': sequ\u00eancia geom\u00e9trica '
                     '(aprofundamento).')
            tipo = 'g'
        else:
            N.err('N\u00e3o encontrei uma regra simples (nem diferen\u00e7as '
                  'constantes, nem raz\u00e3o constante)')
    if tipo == 'g':
        o.append('> Termo geral: u(n) = ' + Q.qp(us[0]) + ' \u00d7 ' +
                 Q.qp(r) + '^(n - 1)')

        def termo(n):
            return Q.mul(us[0], Q.pw(r, n - 1))
    else:
        o.append('> Termo geral: u(n) = ' + Q.pstr(G))

        def termo(n):
            return Q.valor(G, {'n': (n, 1)})
    ok = [termo(i + 1) == us[i] for i in range(len(us))]
    o.append('Confirma\u00e7\u00e3o com os termos dados: ' + ('\u2713' if all(ok) else
                                                   '\u2717'))
    if v[1] is not None:
        n = v[1][0]
        N.need(n == int(n) and 1 <= n <= 10 ** 6, 'A ordem n tem de ser um '
               'inteiro positivo')
        n = int(n)
        o.append('u' + sub(n) + ' = ' + Q.qs(termo(n)))
    if v[2]:
        t = numeros(v[2], 'O n\u00famero')
        N.need(len(t) == 1, 'Escreve um s\u00f3 n\u00famero para verificar')
        t = t[0]
        n = ordem(tipo, G if tipo != 'g' else None, us, termo, t)
        if n:
            o.append(Q.qs(t) + ' \u00e9 termo: \u00e9 o termo de ordem ' + str(n) + '.')
        else:
            o.append(Q.qs(t) + ' n\u00e3o \u00e9 termo da sequ\u00eancia (n\u00e3o h\u00e1 n inteiro '
                     'positivo).')
    st = 'Termo geral: a express\u00e3o de u(n) em fun\u00e7\u00e3o da ordem n.\n' \
        'Aritm\u00e9tica (diferen\u00e7a d constante): u(n) = d n + (u(1) - d).\n' \
        'Para ver se um n\u00famero \u00e9 termo: resolve-se u(n) = n\u00famero e v\u00ea-se se ' \
        'n \u00e9 inteiro positivo.'
    return ('\n'.join(o), st, None, '')


def all_eq(xs):
    for x in xs:
        if x != xs[0]:
            return False
    return True


def ordem(tipo, G, us, termo, t):
    if tipo == 'a':
        d = G.get((('n', 1),), Q.Z)
        c = G.get((), Q.Z)
        if d[0] == 0:
            return 1 if c == t else 0
        n = Q.div(Q.sub(t, c), d)
        return n[0] if n[1] == 1 and n[0] >= 1 else 0
    for n in range(1, 2001):
        u = termo(n)
        if u == t:
            return n
        if tipo == 'g' and abs(u[0]) > abs(t[0]) * u[1] * 10 ** 6 + 10 ** 6:
            break
    return 0

# ------------------------------------------------------------ proporcoes


def tabela(tx, ty):
    xs = numeros(tx, 'Os valores de x', True)
    ys = numeros(ty, 'Os valores de y', True)
    N.need(len(xs) == len(ys), 'H\u00e1 ' + str(len(xs)) + ' valores de x e ' +
           str(len(ys)) + ' de y')
    N.need(len(xs) >= 1, 'Escreve os valores')
    for i in range(len(xs)):
        N.need(xs[i] is not None or ys[i] is not None, 'Na coluna ' +
               str(i + 1) + ' faltam os dois valores')
    return xs, ys


def prop():
    return ('Proporcionalidade direta',
            [N.fld('Valores de x (? = em falta)', '', '2 3 5 ?', 't'),
             N.fld('Valores de y (? = em falta)', '', '6 9 ? 21', 't')], _prop)


def _prop(v):
    xs, ys = tabela(v[0], v[1])
    ks = []
    o = []
    for i in range(len(xs)):
        if xs[i] is not None and ys[i] is not None:
            N.need(xs[i][0] != 0, 'Com x = 0, o quociente y/x n\u00e3o existe')
            k = Q.div(ys[i], xs[i])
            ks.append(k)
            o.append(Q.qs(ys[i]) + ' : ' + Q.qp(xs[i]) + ' = ' + Q.qs(k))
    N.need(ks, '\u00c9 preciso pelo menos um par (x, y) completo')
    if not all_eq(ks):
        o.append('> Os quocientes y/x n\u00e3o s\u00e3o todos iguais: x e y n\u00e3o s\u00e3o '
                 'diretamente proporcionais.')
        return ('\n'.join(o), ST_PROP, None, '')
    k = ks[0]
    o.append('> Constante de proporcionalidade: k = y/x = ' + Q.qs(k) +
             '; y = ' + (Q.pstr({(('x', 1),): k}) if k[0] else '0'))
    for i in range(len(xs)):
        if xs[i] is None:
            N.need(k[0], 'Com k = 0 n\u00e3o se pode calcular x')
            xs[i] = Q.div(ys[i], k)
            o.append('x = y : k = ' + Q.qs(ys[i]) + ' : ' + Q.qp(k) + ' = ' +
                     Q.qs(xs[i]))
        elif ys[i] is None:
            ys[i] = Q.mul(k, xs[i])
            o.append('y = k \u00d7 x = ' + Q.qs(k) + ' \u00d7 ' + Q.qp(xs[i]) +
                     ' = ' + Q.qs(ys[i]))
    o.append('Tabela: ' + '; '.join(['(' + Q.vstr(xs[i]) + Q.sepr(xs[i], ys[i]) +
                                      Q.vstr(ys[i]) + ')' for i in
                                      range(len(xs))]))
    fx = [Q.qf(x) for x in xs]
    fy = [Q.qf(y) for y in ys]
    x1 = max([abs(x) for x in fx] + [1.0]) * 1.2
    y1 = max([abs(y) for y in fy] + [1.0]) * 1.2
    gr = ('y = ' + Q.qs(k) + 'x', [('f', lambda t: Q.qf(k) * t, 4),
                                   ('p', list(zip(fx, fy)), 5)],
          -x1 * 0.2, x1, -y1 * 0.2, y1, 'reta que passa na origem; pontos: '
          'a tabela')
    return ('\n'.join(o), ST_PROP, Q.qf(k), '', gr)


ST_PROP = 'Proporcionalidade direta: y/x \u00e9 sempre o mesmo n\u00famero k ' \
    '(constante de proporcionalidade); y = kx.\nO gr\u00e1fico \u00e9 uma reta que ' \
    'passa na origem.\nRegra de tr\u00eas simples: valor em falta = k \u00d7 x ou ' \
    'y : k.'


def inv():
    return ('Proporcionalidade inversa',
            [N.fld('Valores de x (? = em falta)', '', '2 4 5 ?', 't'),
             N.fld('Valores de y (? = em falta)', '', '10 5 ? 2', 't')], _inv)


def _inv(v):
    xs, ys = tabela(v[0], v[1])
    ks = []
    o = []
    for i in range(len(xs)):
        if xs[i] is not None and ys[i] is not None:
            k = Q.mul(xs[i], ys[i])
            ks.append(k)
            o.append(Q.qs(xs[i]) + ' \u00d7 ' + Q.qp(ys[i]) + ' = ' + Q.qs(k))
    N.need(ks, '\u00c9 preciso pelo menos um par (x, y) completo')
    if not all_eq(ks) or ks[0][0] == 0:
        o.append('> Os produtos x \u00d7 y n\u00e3o s\u00e3o todos iguais (ou s\u00e3o 0): x '
                 'e y n\u00e3o s\u00e3o inversamente proporcionais.')
        return ('\n'.join(o), ST_INV, None, '')
    k = ks[0]
    o.append('> Constante: k = x \u00d7 y = ' + Q.qs(k) + '; y = ' + Q.qs(k) +
             '/x')
    for i in range(len(xs)):
        if xs[i] is None:
            N.need(ys[i][0], 'y = 0 n\u00e3o \u00e9 poss\u00edvel na proporcionalidade '
                   'inversa')
            xs[i] = Q.div(k, ys[i])
            o.append('x = k : y = ' + Q.qs(k) + ' : ' + Q.qp(ys[i]) + ' = ' +
                     Q.qs(xs[i]))
        elif ys[i] is None:
            N.need(xs[i][0], 'x = 0 n\u00e3o \u00e9 poss\u00edvel na proporcionalidade '
                   'inversa')
            ys[i] = Q.div(k, xs[i])
            o.append('y = k : x = ' + Q.qs(k) + ' : ' + Q.qp(xs[i]) + ' = ' +
                     Q.qs(ys[i]))
    o.append('Tabela: ' + '; '.join(['(' + Q.vstr(xs[i]) + Q.sepr(xs[i], ys[i]) +
                                      Q.vstr(ys[i]) + ')' for i in
                                      range(len(xs))]))
    fx = [Q.qf(x) for x in xs]
    fy = [Q.qf(y) for y in ys]
    kf = Q.qf(k)
    x1 = max([abs(x) for x in fx] + [1.0]) * 1.3
    y1 = max([abs(y) for y in fy] + [1.0]) * 1.3

    def f(t):
        N.need(abs(t) > 1e-9, '')
        return kf / t
    gr = ('y = ' + Q.qs(k) + '/x', [('f', f, 4), ('p', list(zip(fx, fy)), 5)],
          0, x1, 0 if kf > 0 else -y1, y1 if kf > 0 else 0,
          'ramo de hip\u00e9rbole; pontos: a tabela')
    return ('\n'.join(o), ST_INV, kf, '', gr)


ST_INV = 'Proporcionalidade inversa: x \u00d7 y \u00e9 sempre o mesmo n\u00famero k; ' \
    'y = k/x.\nQuando x duplica, y passa a metade.\nO gr\u00e1fico (x > 0) \u00e9 um ' \
    'ramo de hip\u00e9rbole.'

# ------------------------------------------------------------ percentagens

TIPOS = ['p% de a', 'a em % de b', 'a com aumento de p%',
         'a com desconto de p%', 'valor inicial (a j\u00e1 com aumento de p%)',
         'valor inicial (a j\u00e1 com desconto de p%)',
         'varia\u00e7\u00e3o percentual de a para b']


def perc():
    return ('Percentagens',
            [N.fld('Calcular', '', '', 'c', TIPOS),
             N.fld('Valor a', '', '80', 'o'),
             N.fld('Valor b', '', '', 'o'),
             N.fld('Percentagem p (%)', '', '15', 'o')], _perc)


def qv(x, nm):
    N.need(x is not None, 'Escreve ' + nm)
    f = N.frac(x[0], 10 ** 6)
    return Q.R(f[0], f[1]) if f else None


def _perc(v):
    t, a, b, p = v
    o = []
    cem = (100, 1)
    if t in (0, 2, 3, 4, 5):
        a = qv(a, 'o valor a')
        p = qv(p, 'a percentagem p')
        N.need(a is not None and p is not None, 'Valores com demasiadas casas '
               'decimais')
        f = Q.div(p, cem)
    if t == 0:
        r = Q.mul(f, a)
        o += ['= p% de a = (p/100) \u00d7 a',
              '> ' + Q.vstr(p) + '% de ' + Q.vstr(a) + ' = ' + Q.vstr(f) +
              ' \u00d7 ' + Q.vstr(a) + ' = ' + Q.vstr(r)]
    elif t == 1 or t == 6:
        a = qv(a, 'o valor a')
        b = qv(b, 'o valor b')
        N.need(a is not None and b is not None, 'Valores com demasiadas casas '
               'decimais')
        if t == 1:
            N.need(b[0], 'b n\u00e3o pode ser 0')
            r = Q.mul(Q.div(a, b), cem)
            o += ['= a/b \u00d7 100', '> ' + Q.vstr(a) + ' \u00e9 ' + pt(r) + ' de ' +
                  Q.vstr(b)]
        else:
            N.need(a[0], 'O valor inicial a n\u00e3o pode ser 0')
            r = Q.mul(Q.div(Q.sub(b, a), a), cem)
            o += ['= (b - a)/a \u00d7 100', '> Varia\u00e7\u00e3o: ' + ('+' if r[0] > 0
                                                             else '') + pt(r) +
                  (' (aumento)' if r[0] > 0 else (' (diminui\u00e7\u00e3o)' if r[0] < 0
                                                  else ''))]
    else:
        up = t in (2, 4)
        N.need(up or Q.cmp(p, cem) < 0, 'Um desconto tem de ser menor do que '
               '100%')
        fat = Q.add((1, 1), f) if up else Q.sub((1, 1), f)
        if t in (2, 3):
            r = Q.mul(a, fat)
            o += ['= a \u00d7 (1 ' + ('+' if up else '-') + ' p/100)',
                  '> ' + Q.vstr(a) + ' \u00d7 ' + Q.vstr(fat) + ' = ' + Q.vstr(r)]
        else:
            r = Q.div(a, fat)
            o += ['= a : (1 ' + ('+' if up else '-') + ' p/100)',
                  '> ' + Q.vstr(a) + ' : ' + Q.vstr(fat) + ' = ' + Q.vstr(r)]
    if '/' in Q.vstr(r):
        o.append('Valor aproximado: ' + N.fmt(Q.qf(r), 0, 2))
    st = 'p% = p/100. Aumento de p%: \u00d7 (1 + p/100); desconto de p%: ' \
        '\u00d7 (1 - p/100).\nValor inicial: divide-se pelo fator.\nVaria\u00e7\u00e3o ' \
        'percentual: (novo - antigo)/antigo \u00d7 100.'
    return ('\n'.join(o), st, Q.qf(r), '')


def pt(r):
    s = Q.vstr(r)
    return (s if '/' not in s else N.AP + ' ' + N.fmt(Q.qf(r), 0, 2)) + '%'
