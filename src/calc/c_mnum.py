# c_mnum.py - M1TR4M: resolvedores de Numeros (7.o e 8.o anos): expressoes
# numericas com fracoes e numeros negativos (passo a passo, com o m.m.c.),
# ordenar racionais, potencias e as suas regras, decomposicao em fatores
# primos, m.d.c. e m.m.c., dizimas finitas e periodicas <-> fracoes.
#@ c_mnum.frac|Fra\u00e7\u00f5es e n\u00fameros racionais (passo a passo)|fra\u00e7\u00f5es opera\u00e7\u00f5es n\u00fameros racionais negativos express\u00e3o num\u00e9rica prioridades simplificar ordenar comparar d\u00edzima|M|n7
#@ c_mnum.pot|Pot\u00eancias e regras das pot\u00eancias|pot\u00eancia expoente base produto quociente mesma base mesmo expoente pot\u00eancia de pot\u00eancia expoente negativo|M|n7
#@ c_mnum.mdc|Fatores primos, m.d.c. e m.m.c.|decomposi\u00e7\u00e3o em fatores primos m\u00e1ximo divisor comum m\u00ednimo m\u00faltiplo comum mdc mmc divisores n\u00famero primo simplificar fra\u00e7\u00e3o|M|n7
#@ c_mnum.dec|D\u00edzimas e fra\u00e7\u00f5es|d\u00edzima finita infinita peri\u00f3dica per\u00edodo fra\u00e7\u00e3o geratriz converter decimal|M|n8
# Casos-limite: divisao por zero, letras numa expressao numerica, 0 com
# expoente negativo, expoentes nao inteiros, numeros muito grandes,
# periodos longos, numeros negativos e zero no m.d.c.

import m1_nucleo as N
import m1_q as Q

SIM = {'+': '+', '-': '-', '*': '\u00d7', '/': ':'}


def ler(s):
    t = Q.arvore(s)
    ls = Q.letras(t)
    N.need(not ls, 'Esta calculadora \u00e9 s\u00f3 para n\u00fameros (encontrei a letra ' +
           (ls[0] if ls else '') + ')')
    return t


def base_txt(a):
    return '(' + Q.qs(a) + ')' if a[0] < 0 or a[1] > 1 else Q.qs(a)


def passo_op(k, a, b, r, ps):
    # Escreve uma operacao; somas de fracoes passam pelo m.m.c.
    if k in '+-' and (a[1] > 1 or b[1] > 1):
        L = Q.mmc(a[1], b[1])
        fa = str(a[0] * (L // a[1])) + '/' + str(L)
        fb = str(b[0] * (L // b[1])) + '/' + str(L)
        s = Q.qs(a) + ' ' + k + ' ' + Q.qp(b)
        if a[1] != L or b[1] != L:
            s += ' = ' + fa + ' ' + k + ' ' + ('(' + fb + ')' if b[0] < 0
                                                else fb)
        n = a[0] * (L // a[1]) + (1 if k == '+' else -1) * b[0] * (L // b[1])
        s += ' = ' + str(n) + '/' + str(L)
        if (n, L) != r:
            s += ' = ' + Q.qs(r)
        ps.append(s)
    elif k == '*' and (a[1] > 1 or b[1] > 1):
        s = Q.qs(a) + ' \u00d7 ' + Q.qp(b) + ' = ' + str(a[0] * b[0]) + '/' + \
            str(a[1] * b[1])
        if (a[0] * b[0], a[1] * b[1]) != r:
            s += ' = ' + Q.qs(r)
        ps.append(s)
    elif k == '/' and (a[1] > 1 or b[1] > 1 or Q.qs(r).find('/') >= 0):
        inv = Q.R(b[1], b[0])
        ps.append(Q.qs(a) + ' : ' + Q.qp(b) + ' = ' + Q.qs(a) + ' \u00d7 ' +
                  Q.qp(inv) + ' = ' + Q.qs(r))
    else:
        ps.append(Q.qp(a) + ' ' + SIM[k] + ' ' + Q.qp(b) + ' = ' + Q.qs(r))


def calc(t, ps):
    k = t[0]
    if k == 'n':
        return t[1]
    if k == 'u':
        return Q.neg(calc(t[1], ps))
    if k in '+-*/':
        a = calc(t[1], ps)
        b = calc(t[2], ps)
        r = {'+': Q.add, '-': Q.sub, '*': Q.mul, '/': Q.div}[k](a, b)
        passo_op(k, a, b, r, ps)
        return r
    if k == '^':
        a = calc(t[1], ps)
        e = calc(t[2], ps)
        N.need(e[1] == 1, 'O expoente tem de ser um n\u00famero inteiro')
        r = Q.pw(a, e[0])
        s = base_txt(a) + N.sup(e[0]) + ' = '
        if e[0] < 0:
            s += '(' + Q.qs(Q.R(a[1], a[0])) + ')' + N.sup(-e[0]) + ' = '
        ps.append(s + Q.qs(r))
        return r
    if k == 'r':
        a = calc(t[1], ps)
        N.need(a[0] >= 0, 'N\u00e3o h\u00e1 raiz quadrada de um n\u00famero negativo')
        n, d = isqrt(a[0]), isqrt(a[1])
        N.need(n * n == a[0] and d * d == a[1], '\u221a' + Q.qs(a) + ' n\u00e3o \u00e9 '
               'um n\u00famero racional: usa a calculadora de radicais')
        r = Q.R(n, d)
        ps.append('\u221a' + base_txt(a) + ' = ' + Q.qs(r))
        return r
    N.err('Express\u00e3o inv\u00e1lida')


def isqrt(n):
    if n < 2:
        return n
    x = int(n ** 0.5)
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


def mostra(r):
    o = ['> = ' + Q.qs(r)]
    if r[1] > 1:
        o.append('Em d\u00edzima: ' + Q.dizima(r) + (
            '' if fin(r[1]) else ' \u2248 ' + N.fmt(Q.qf(r))))
        if abs(r[0]) > r[1]:
            ip = abs(r[0]) // r[1]
            o.append('Numeral misto: ' + ('-' if r[0] < 0 else '') + str(ip) +
                     ' e ' + str(abs(r[0]) - ip * r[1]) + '/' + str(r[1]))
    return o


def fin(d):
    for p, e in Q.fatores(d):
        if p not in (2, 5):
            return False
    return True

# ------------------------------------------------------------ fracoes


def frac():
    return ('Fra\u00e7\u00f5es e n\u00fameros racionais',
            [N.fld('Express\u00e3o num\u00e9rica', '', '1/2 + 3/4 \u00d7 (2/3 - 1)', 't'),
             N.fld('Ordenar (opcional): n\u00fameros com espa\u00e7os', '', '', 't')],
            _frac)


def _frac(v):
    te, to = v
    o = []
    r = None
    if te:
        ps = []
        r = calc(ler(te), ps)
        if ps:
            o.append('Pela ordem das opera\u00e7\u00f5es (par\u00eanteses, '
                     'pot\u00eancias, \u00d7 e :, + e -):')
            o += [str(i + 1) + '. ' + ps[i] for i in range(len(ps))]
        o += mostra(r)
    if to:
        xs = []
        for p in to.replace(';', ' ').split():
            r2 = calc(ler(p), [])
            k = len(xs)
            while k > 0 and Q.cmp(xs[k - 1][0], r2) > 0:
                k -= 1
            xs.insert(k, (r2, p))
        N.need(len(xs) >= 2, 'Escreve pelo menos dois n\u00fameros para ordenar')
        txt = xs[0][1]
        for i in range(1, len(xs)):
            txt += (' = ' if Q.cmp(xs[i][0], xs[i - 1][0]) == 0 else ' < ') + \
                xs[i][1]
        o.append('Por ordem crescente: ' + txt)
        o.append('(Valores: ' + '; '.join([N.fmt(Q.qf(x)) for x, p in xs]) +
                 ')')
    N.need(te or to, 'Escreve uma express\u00e3o ou n\u00fameros para ordenar')
    st = 'Ordem das opera\u00e7\u00f5es: par\u00eanteses, pot\u00eancias, multiplica\u00e7\u00f5es e ' \
        'divis\u00f5es, adi\u00e7\u00f5es e subtra\u00e7\u00f5es (da esquerda para a direita).\n' \
        'Somar fra\u00e7\u00f5es: reduz-se ao mesmo denominador (m.m.c.).\n' \
        'Dividir por uma fra\u00e7\u00e3o: multiplica-se pelo inverso.\n' \
        'Sinais: (-) \u00d7 (-) = (+); (-) \u00d7 (+) = (-).'
    return ('\n'.join(o), st, Q.qf(r) if r else None, '')

# ------------------------------------------------------------ potencias


def fatores_pot(t, sg, out):
    # Cadeia de produtos e quocientes -> [(+1 ou -1, base, expoente)].
    k = t[0]
    if k == '*':
        return fatores_pot(t[1], sg, out) and fatores_pot(t[2], sg, out)
    if k == '/':
        return fatores_pot(t[1], sg, out) and fatores_pot(t[2], -sg, out)
    if k == '^':
        b, e = t[1], t[2]
        if b[0] == '^':
            pp = []
            if not fatores_pot(b, 1, pp) or len(pp) != 1:
                return False
            ee = calc(e, [])
            if ee[1] != 1:
                return False
            out.append((sg, pp[0][1], pp[0][2] * ee[0], (pp[0][2], ee[0])))
            return True
        ee = calc(e, [])
        if ee[1] != 1 or b[0] not in ('n', 'v', 'u'):
            return False
        if b[0] == 'u' and b[1][0] != 'n':
            return False
        out.append((sg, b, ee[0], None))
        return True
    if k in ('n', 'v'):
        out.append((sg, t, 1, None))
        return True
    return False


def btxt(b):
    if b[0] == 'v':
        return b[1]
    if b[0] == 'u':
        return '(-' + Q.qs(b[1][1]) + ')'
    return base_txt(b[1])


def pot():
    return ('Pot\u00eancias e as suas regras',
            [N.fld('Express\u00e3o com pot\u00eancias', '', '2^3 \u00d7 2^4 : 2^5', 't')],
            _pot)


def _pot(v):
    s = v[0]
    N.need(s, 'Escreve uma express\u00e3o, por exemplo 2^3 \u00d7 2^4')
    t = Q.arvore(s)
    o = []
    fs = []
    if fatores_pot(t, 1, fs) and len(fs) >= 1:
        for sg, b, e, pp in fs:
            if pp:
                o.append('Pot\u00eancia de pot\u00eancia: (' + btxt(b) + N.sup(pp[0]) +
                         ')' + N.sup(pp[1]) + ' = ' + btxt(b) + '^(' +
                         str(pp[0]) + ' \u00d7 ' + qn(pp[1]) + ') = ' + btxt(b) +
                         N.sup(e))
        grupos = []
        for sg, b, e, pp in fs:
            nm = btxt(b)
            for g in grupos:
                if g[0] == nm:
                    g[2].append(sg * e)
                    break
            else:
                grupos.append([nm, b, [sg * e]])
        for g in grupos:
            if len(g[2]) > 1:
                soma = sum(g[2])
                o.append('Mesma base ' + g[0] + ': soma-se ou subtrai-se os '
                         'expoentes: ' + g[0] + '^(' + ' '.join(
                             [('+ ' + str(x) if x >= 0 else '- ' + str(-x))
                              for x in g[2]]).lstrip('+ ') + ') = ' + g[0] +
                         N.sup(soma))
        res = [(g[0], g[1], sum(g[2])) for g in grupos]
        es = set([e for nm, b, e in res])
        if len(res) > 1 and len(es) == 1 and not [1 for nm, b, e in res
                                                  if b[0] == 'v']:
            e = list(es)[0]
            prod = Q.UM
            for nm, b, x in res:
                prod = Q.mul(prod, calc(b, []))
            o.append('Mesmo expoente: multiplicam-se as bases: ' + ' \u00d7 '.join(
                [nm + N.sup(e) for nm, b, x in res]) + ' = (' + ' \u00d7 '.join(
                    [nm for nm, b, x in res]) + ')' + N.sup(e) + ' = ' +
                base_txt(prod) + N.sup(e))
        if [1 for nm, b, e in res if b[0] == 'v']:
            o.append('> ' + ' \u00d7 '.join([nm + (N.sup(e) if e != 1 else '')
                                             for nm, b, e in res if e != 0]
                                            ) or '> 1')
            for nm, b, e in res:
                if e < 0:
                    o.append(nm + N.sup(e) + ' = 1/' + nm + N.sup(-e) +
                             ' (expoente negativo)')
            return ('\n'.join(o), ST_POT, None, '')
        for nm, b, e in res:
            if e < 0:
                o.append(nm + N.sup(e) + ' = 1/' + nm + N.sup(-e) +
                         ' (expoente negativo)')
            if e == 0:
                o.append(nm + '\u2070 = 1 (expoente zero)')
    ps = []
    r = calc(t, ps)
    o.append('Valor: ' + (ps[-1] if ps else Q.qs(r)))
    o += mostra(r)
    if abs(r[0]) >= 10 ** 6 or (r[0] and abs(Q.qf(r)) < 10 ** -4):
        o.append('Em nota\u00e7\u00e3o cient\u00edfica: usa a calculadora de nota\u00e7\u00e3o '
                 'cient\u00edfica.')
    return ('\n'.join(o), ST_POT, Q.qf(r), '')


def qn(x):
    return str(x) if x >= 0 else '(' + str(x) + ')'


ST_POT = 'a^m \u00d7 a^n = a^(m + n); a^m : a^n = a^(m - n), com a \u2260 0.\n' \
    '(a^m)^n = a^(m \u00d7 n); a^n \u00d7 b^n = (a \u00d7 b)^n.\n' \
    'a\u2070 = 1; a^(-n) = 1/a^n.\n' \
    'Base negativa: expoente par d\u00e1 positivo; expoente \u00edmpar d\u00e1 negativo.'

# ------------------------------------------------------------ mdc e mmc


def mdc():
    return ('Fatores primos, m.d.c. e m.m.c.',
            [N.fld('N\u00fameros inteiros (2 ou mais)', '', '84 120', 'l')], _mdc)


def _mdc(v):
    ns = []
    for x, sf in v[0]:
        N.need(x == int(x) and 1 <= x <= 10 ** 12, 'Escreve n\u00fameros inteiros '
               'positivos (at\u00e9 10\u00b9\u00b2)')
        ns.append(int(x))
    N.need(len(ns) <= 6, 'No m\u00e1ximo 6 n\u00fameros')
    o = []
    fs = []
    for n in ns:
        f = Q.fatores(n)
        fs.append(f)
        o.append(str(n) + ' = ' + Q.fstr(f) + (' (primo)' if len(f) == 1 and
                                                f[0][1] == 1 else ''))
    if len(ns) == 1:
        n = ns[0]
        if n <= 10 ** 6:
            ds = [d for d in range(1, n + 1) if n % d == 0] if n <= 2000 else \
                divisores(fs[0])
            o.append('Divisores (' + str(len(ds)) + '): ' + ', '.join(
                [str(d) for d in ds[:40]]) + (' ...' if len(ds) > 40 else ''))
        st = 'Decomp\u00f5e-se dividindo pelos primos 2, 3, 5, 7, ... por ordem.'
        return ('\n'.join(o), st, None, '')
    ps = sorted(set([p for f in fs for p, e in f]))
    com = []
    tod = []
    g = ns[0]
    m = ns[0]
    for n in ns[1:]:
        g = Q.mdc(g, n)
        m = Q.mmc(m, n)
    for p in ps:
        es = [dict(f).get(p, 0) for f in fs]
        if min(es) > 0:
            com.append((p, min(es)))
        tod.append((p, max(es)))
    o.append('= m.d.c.: fatores comuns, com o menor expoente')
    o.append('> m.d.c. = ' + (Q.fstr(com) + ' = ' if com else '') + str(g))
    o.append('= m.m.c.: fatores comuns e n\u00e3o comuns, com o maior expoente')
    o.append('> m.m.c. = ' + Q.fstr(tod) + ' = ' + str(m))
    if g == 1:
        o.append('Os n\u00fameros s\u00e3o primos entre si (m.d.c. = 1).')
    if len(ns) == 2:
        a, b = ns
        o.append('Confirma\u00e7\u00e3o: m.d.c. \u00d7 m.m.c. = ' + str(g * m) + ' = ' +
                 str(a) + ' \u00d7 ' + str(b))
        o.append('Fra\u00e7\u00e3o ' + str(a) + '/' + str(b) + ' simplificada (: ' +
                 str(g) + '): ' + Q.qs(Q.R(a, b)))
    st = 'm.d.c.: o maior divisor comum (serve para simplificar fra\u00e7\u00f5es).\n' \
        'm.m.c.: o menor m\u00faltiplo comum (serve para somar fra\u00e7\u00f5es).'
    return ('\n'.join(o), st, g, '')


def divisores(f):
    ds = [1]
    for p, e in f:
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    ds.sort()
    return ds

# ------------------------------------------------------------ dizimas


def dec():
    return ('D\u00edzimas e fra\u00e7\u00f5es',
            [N.fld('Fra\u00e7\u00e3o ou d\u00edzima (ex.: 7/12 ou 1,2(45))', '', '7/12', 't')],
            _dec)


def dez(k):
    return '10' if k == 1 else '10' + N.sup(k)


def _dec(v):
    s = v[0].replace(' ', '').replace('.', ',')
    N.need(s, 'Escreve uma fra\u00e7\u00e3o (7/12) ou uma d\u00edzima (0,(3) ou 1,25)')
    o = []
    if '(' in s:
        N.need(s.endswith(')') and s.count('(') == 1 and ',' in s,
               'Escreve a d\u00edzima peri\u00f3dica assim: 1,2(45) (per\u00edodo entre '
               'par\u00eanteses)')
        neg = s.startswith('-')
        s2 = s.lstrip('-+')
        ip, rest = s2.split(',')
        np_, per = rest[:-1].split('(')
        N.need((ip + np_ + per).isdigit() and per, 'D\u00edzima mal escrita')
        k, p = len(np_), len(per)
        a = int(ip + np_ + per)
        b = int(ip + np_) if (ip + np_) else 0
        num, den = a - b, 10 ** (k + p) - 10 ** k
        r = Q.R(-num if neg else num, den)
        sg = '-' if neg else ''
        o.append('Seja d = ' + sg + (ip or '0') + ',' + np_ + '(' + per + ')')
        if k:
            o.append(dez(k) + ' d = ' + sg + str(int(ip + np_)) + ',(' + per +
                     ')')
        o.append(dez(k + p) + ' d = ' + sg + str(int(ip + np_ + per)) + ',(' +
                 per + ')')
        o.append('Subtraindo: ' + str(den) + ' d = ' + ('-' if neg else '') +
                 str(num))
        o.append('> d = ' + ('-' if neg else '') + str(num) + '/' + str(den) +
                 (' = ' + Q.qs(r) if (num, den) != (abs(r[0]), r[1]) else ''))
    else:
        r = calc(ler(s.replace(',', '.') if '/' not in s else s), [])
        o.append('> ' + s + ' = ' + Q.qs(r) + (' (fra\u00e7\u00e3o irredut\u00edvel)'
                                              if r[1] > 1 else ''))
        o.append('D\u00edzima: ' + Q.dizima(r))
    if r[1] > 1:
        f = Q.fatores(r[1])
        o.append('Denominador ' + str(r[1]) + ' = ' + Q.fstr(f))
        if fin(r[1]):
            o.append('S\u00f3 tem os fatores 2 e 5: d\u00edzima finita.')
        else:
            dz = Q.dizima(r)
            o.append('Tem fatores diferentes de 2 e 5: d\u00edzima infinita '
                     'peri\u00f3dica' + (', per\u00edodo ' + dz[dz.find('(') + 1:-1]
                                    if '(' in dz else ''))
    st = 'Fra\u00e7\u00e3o irredut\u00edvel com denominador s\u00f3 com fatores 2 e 5: d\u00edzima ' \
        'finita; sen\u00e3o, infinita peri\u00f3dica.\nD\u00edzima peri\u00f3dica para fra\u00e7\u00e3o: ' \
        'multiplica-se por pot\u00eancias de 10 e subtrai-se para o per\u00edodo ' \
        'desaparecer.'
    return ('\n'.join(o), st, Q.qf(r), '')
