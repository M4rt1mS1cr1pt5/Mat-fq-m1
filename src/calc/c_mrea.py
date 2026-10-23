# c_mrea.py - M1TR4M: resolvedores de Numeros (8.o e 9.o anos): notacao
# cientifica (escrever e operar), raizes e radicais (simplificar, operar,
# racionalizar, enquadrar entre inteiros e valores aproximados) e
# intervalos de numeros reais (intersecao, reuniao, condicoes, inteiros).
#@ c_mrea.ncie|Nota\u00e7\u00e3o cient\u00edfica|nota\u00e7\u00e3o cient\u00edfica pot\u00eancias de 10 expoente mantissa multiplicar dividir somar n\u00fameros muito grandes pequenos|M|n8
#@ c_mrea.rad|Ra\u00edzes e radicais|raiz quadrada c\u00fabica radicais simplificar racionalizar denominador quadrado perfeito irracional enquadrar valores aproximados|M|n9
#@ c_mrea.intv|Intervalos de n\u00fameros reais|intervalos interse\u00e7\u00e3o reuni\u00e3o uni\u00e3o condi\u00e7\u00e3o n\u00fameros inteiros reta real aberto fechado infinito|M|n9
# Casos-limite: zero (sem notacao cientifica), radicandos negativos,
# denominadores com mais de dois termos, intervalos vazios ou degenerados,
# intervalos ilimitados, extremos trocados.

import math
import m1_nucleo as N
import m1_q as Q

MS = '\u00b7'


def valor(s, nm):
    s = s.replace(' ', '')
    N.need(s, 'Escreve ' + nm)
    t = Q.arvore(s)
    N.need(not Q.letras(t), nm[0].upper() + nm[1:] + ' n\u00e3o pode ter letras')
    c = Q.cte(Q.poli(t))
    return c if c is not None else Q.Z


# ------------------------------------------------------------ notacao


def expo(v):
    # n tal que 1 <= |v| / 10^n < 10 (exato).
    a = (abs(v[0]), v[1])
    n = int(math.floor(math.log10(Q.qf(a)))) if Q.qf(a) > 0 else 0
    while Q.cmp(a, Q.pw((10, 1), n)) < 0:
        n -= 1
    while Q.cmp(a, Q.pw((10, 1), n + 1)) >= 0:
        n += 1
    return n


def cien(v):
    N.need(v[0] != 0, '0 n\u00e3o se escreve em nota\u00e7\u00e3o cient\u00edfica')
    n = expo(v)
    m = Q.div(v, Q.pw((10, 1), n))
    return m, n


def mtxt(m):
    s = Q.vstr(m)
    if '/' in s or '(' in s or len(s) > 12:
        return N.AP + ' ' + N.fsf(Q.qf(m), 4)
    return s


def ctxt(m, n):
    s = mtxt(m)
    return s + ' \u00d7 10' + N.sup(n)


def ncie():
    return ('Nota\u00e7\u00e3o cient\u00edfica',
            [N.fld('N\u00famero A', '', '0,00052', 't'),
             N.fld('N\u00famero B (opcional)', '', '', 't'),
             N.fld('Opera\u00e7\u00e3o', '', '', 'c', ['s\u00f3 escrever A em nota\u00e7\u00e3o '
                                              'cient\u00edfica', 'A \u00d7 B', 'A : B',
                                              'A + B', 'A - B'])], _ncie)


def _ncie(v):
    ta, tb, op = v
    A = valor(ta, 'o n\u00famero A')
    ma, na = cien(A)
    o = ['A = ' + ctxt(ma, na)]
    r = A
    if op:
        B = valor(tb, 'o n\u00famero B')
        mb, nb = cien(B)
        o.append('B = ' + ctxt(mb, nb))
        if op == 1:
            m = Q.mul(ma, mb)
            o.append('= (' + mtxt(ma) + ' \u00d7 ' + mtxt(mb) + ') \u00d7 10^(' +
                     str(na) + ' + ' + qn(nb) + ')')
            o.append('= ' + mtxt(m) + ' \u00d7 10' + N.sup(na + nb))
            r = Q.mul(A, B)
        elif op == 2:
            m = Q.div(ma, mb)
            o.append('= (' + mtxt(ma) + ' : ' + mtxt(mb) + ') \u00d7 10^(' +
                     str(na) + ' - ' + qn(nb) + ')')
            o.append('= ' + mtxt(m) + ' \u00d7 10' + N.sup(na - nb))
            r = Q.div(A, B)
        else:
            k = max(na, nb)
            a2 = Q.div(A, Q.pw((10, 1), k))
            b2 = Q.div(B, Q.pw((10, 1), k))
            sg = ' + ' if op == 3 else ' - '
            o.append('Mesma pot\u00eancia de 10: ' + mtxt(a2) + ' \u00d7 10' +
                     N.sup(k) + sg + mtxt(b2) + ' \u00d7 10' + N.sup(k))
            m = Q.add(a2, b2) if op == 3 else Q.sub(a2, b2)
            o.append('= ' + mtxt(m) + ' \u00d7 10' + N.sup(k))
            r = Q.add(A, B) if op == 3 else Q.sub(A, B)
        N.need(r[0] != 0, 'O resultado \u00e9 0')
        mr, nr = cien(r)
        o.append('> ' + ctxt(mr, nr))
    else:
        o[0] = '> ' + o[0]
    st = 'Nota\u00e7\u00e3o cient\u00edfica: a \u00d7 10\u207f com 1 \u2264 a < 10 e n inteiro.\n' \
        'Multiplicar: multiplicam-se os n\u00fameros e somam-se os expoentes.\n' \
        'Dividir: dividem-se os n\u00fameros e subtraem-se os expoentes.\n' \
        'Somar: primeiro, a mesma pot\u00eancia de 10.'
    return ('\n'.join(o), st, Q.qf(r), '')


def qn(x):
    return str(x) if x >= 0 else '(' + str(x) + ')'

# ------------------------------------------------------------ radicais
# Radical: dicionario {m: q} = soma de q raiz(m), m inteiro sem fatores
# quadrados (m = 1 para a parte racional).


def sqf(n):
    k, m = 1, 1
    for p, e in Q.fatores(n):
        k *= p ** (e // 2)
        m *= p ** (e % 2)
    return k, m


def rlimpa(A):
    return dict([(m, A[m]) for m in A if A[m][0]])


def radd(A, B, s=1):
    C = dict(A)
    for m in B:
        C[m] = Q.add(C.get(m, Q.Z), B[m]) if s > 0 else Q.sub(C.get(m, Q.Z),
                                                              B[m])
    return rlimpa(C)


def rmul(A, B):
    C = {}
    for a in A:
        for b in B:
            k, m = sqf(a * b)
            C[m] = Q.add(C.get(m, Q.Z), Q.mul(Q.mul(A[a], B[b]), (k, 1)))
    return rlimpa(C)


def rsqrt(q, ps):
    N.need(q[0] >= 0, 'N\u00e3o h\u00e1 raiz quadrada de um n\u00famero negativo')
    if q[0] == 0:
        return {}
    k, m = sqf(q[0] * q[1])
    r = {m: Q.R(k, q[1])}
    if k > 1 or q[1] > 1:
        p = ['\u221a' + ('(' + Q.qs(q) + ')' if q[1] > 1 else str(q[0]))]
        if q[1] > 1:
            p.append('\u221a' + str(q[0] * q[1]) + '/' + str(q[1]))
        if k > 1:
            p.append('\u221a(' + str(k * k) + ' \u00d7 ' + str(m) + ')' + (
                '/' + str(q[1]) if q[1] > 1 else ''))
        if rstr(r) != p[-1]:
            p.append(rstr(r))
        ps.append(' = '.join(p))
    return r


def rconj(B):
    ks = list(B.keys())
    if len(ks) == 1:
        return {ks[0]: Q.UM}
    N.need(len(ks) == 2, 'Denominador com mais de dois termos: n\u00e3o sei '
           'racionalizar')
    return {ks[0]: B[ks[0]], ks[1]: Q.neg(B[ks[1]])}


def rdiv(A, B, ps):
    N.need(B, 'Divis\u00e3o por zero')
    if list(B.keys()) == [1]:
        return dict([(m, Q.div(A[m], B[1])) for m in A])
    c = rconj(B)
    den = rmul(B, c)
    N.need(list(den.keys()) in ([1], []), 'N\u00e3o sei racionalizar este '
           'denominador')
    N.need(den, 'Divis\u00e3o por zero')
    ps.append('Racionalizar: multiplica-se em cima e em baixo por ' + rstr(c) +
              ' (o denominador fica ' + Q.vstr(den[1]) + ')')
    num = rmul(A, c)
    return dict([(m, Q.div(num[m], den[1])) for m in num])


def reval(t, ps):
    k = t[0]
    if k == 'n':
        return {1: t[1]} if t[1][0] else {}
    if k == 'r':
        a = reval(t[1], ps)
        N.need(list(a.keys()) in ([1], []), 'Ra\u00edzes de ra\u00edzes: n\u00e3o sei '
               'simplificar')
        return rsqrt(a.get(1, Q.Z), ps)
    if k == 'u':
        return dict([(m, Q.neg(c)) for m, c in reval(t[1], ps).items()])
    if k in '+-':
        return radd(reval(t[1], ps), reval(t[2], ps), 1 if k == '+' else -1)
    if k == '*':
        return rmul(reval(t[1], ps), reval(t[2], ps))
    if k == '/':
        return rdiv(reval(t[1], ps), reval(t[2], ps), ps)
    if k == '^':
        e = reval(t[2], ps)
        N.need(list(e.keys()) in ([1], []) and e.get(1, Q.Z)[1] == 1,
               'O expoente tem de ser inteiro')
        e = e.get(1, Q.Z)[0]
        b = reval(t[1], ps)
        N.need(abs(e) <= 12, 'Expoente demasiado grande')
        r = {1: Q.UM}
        for i in range(abs(e)):
            r = rmul(r, b)
        return rdiv({1: Q.UM}, r, ps) if e < 0 else r
    if k == 'c':
        N.err('Raiz c\u00fabica s\u00f3 sozinha (por exemplo \u221b54)')
    N.err('Os radicais n\u00e3o podem ter letras')


def rstr(A):
    if not A:
        return '0'
    o = ''
    for m in sorted(A.keys()):
        c = A[m]
        a, d = abs(c[0]), c[1]
        if m == 1:
            t = Q.qs((a, d))
        else:
            t = ('' if a == 1 else str(a)) + '\u221a' + str(m) + (
                '/' + str(d) if d > 1 else '')
        if not o:
            o = ('-' if c[0] < 0 else '') + t
        else:
            o += (' - ' if c[0] < 0 else ' + ') + t
    return o


def rval(A):
    return sum([Q.qf(A[m]) * m ** 0.5 for m in A])


def rad():
    return ('Ra\u00edzes e radicais',
            [N.fld('Express\u00e3o com \u221a (ex.: \u221a50 + 2\u221a8)', '',
                   '\u221a50 + 2\u221a8 - \u221a18', 't')], _rad)


def _rad(v):
    s = v[0].replace('\u221b', ' cbrt ')
    N.need(s.strip(), 'Escreve uma express\u00e3o, por exemplo \u221a50')
    if 'cbrt' in s:
        N.need(s.strip().startswith('cbrt'), 'A raiz c\u00fabica tem de estar '
               'sozinha (por exemplo \u221b54)')
        return cubica(s.replace('cbrt', '').strip())
    t = Q.arvore(s)
    ps = []
    A = reval(t, ps)
    o = []
    if ps:
        o += ['Passos:'] + ['- ' + p for p in ps]
    o.append('> ' + rstr(A))
    x = rval(A)
    o.append('Valor aproximado: ' + N.fmt(x))
    if list(A.keys()) not in ([1], []):
        o.append('\u00c9 um n\u00famero irracional (tem uma raiz que n\u00e3o \u00e9 exata).')
    if t[0] == 'r' and len(A) == 1 and list(A.keys()) != [1]:
        q = Q.cte(Q.poli(t[1]))
        if q is not None and q[1] == 1:
            k = int(q[0] ** 0.5)
            while k * k > q[0]:
                k -= 1
            while (k + 1) * (k + 1) <= q[0]:
                k += 1
            o.append('Enquadramento: ' + str(k) + ' < \u221a' + str(q[0]) +
                     ' < ' + str(k + 1) + ' (' + str(k * k) + ' < ' + str(q[0]) +
                     ' < ' + str((k + 1) ** 2) + ')')
            lo = int(x * 10) / 10
            o.append('\u00c0s d\u00e9cimas: ' + N.fix(lo, 1) + ' < \u221a' + str(q[0]) +
                     ' < ' + N.fix(lo + 0.1, 1) + ' (por defeito e por excesso)')
    st = '\u221a(a \u00d7 b) = \u221aa \u00d7 \u221ab e \u221a(a/b) = \u221aa / \u221ab ' \
        '(a, b \u2265 0).\nSimplificar: tira-se para fora o maior quadrado ' \
        'perfeito: \u221a50 = \u221a(25 \u00d7 2) = 5\u221a2.\nS\u00f3 se somam radicais ' \
        'iguais: 5\u221a2 + 4\u221a2 = 9\u221a2.\nRacionalizar: multiplicar pelo ' \
        'conjugado, (a + \u221ab)(a - \u221ab) = a\u00b2 - b.'
    return ('\n'.join(o), st, x, '')


def cubica(s):
    q = Q.cte(Q.poli(Q.arvore(s)))
    N.need(q is not None, 'Escreve um n\u00famero dentro da raiz c\u00fabica')
    sg = -1 if q[0] < 0 else 1
    o = []
    res = []
    for x in (abs(q[0]), q[1]):
        k, m = 1, 1
        for p, e in Q.fatores(x):
            k *= p ** (e // 3)
            m *= p ** (e % 3)
        res.append((k, m))
    (kn, mn), (kd, md) = res
    v = sg * (abs(Q.qf(q))) ** (1 / 3)
    if mn == 1 and md == 1:
        o.append('> \u221b' + Q.vstr(q) + ' = ' + Q.qs(Q.R(sg * kn, kd)) +
                 ' (cubo perfeito)')
    else:
        o.append('> \u221b' + Q.vstr(q) + ' = ' + ('-' if sg < 0 else '') + (
            str(kn) if kn > 1 else '') + '\u221b' + str(mn * md * md) + (
                '/' + str(kd * md) if kd * md > 1 else ''))
        o.append('Valor aproximado: ' + N.fmt(v))
    st = '\u221b(a\u00b3) = a; a raiz c\u00fabica de um n\u00famero negativo \u00e9 negativa.'
    return ('\n'.join(o), st, v, '')

# ------------------------------------------------------------ intervalos


def extremo(s):
    s = s.strip().lower().replace('+', '')
    if s in ('inf', '\u221e', 'infinito'):
        return 'inf'
    if s in ('-inf', '-\u221e', '-infinito'):
        return '-inf'
    return valor(s, 'o extremo')


def intervalo(s):
    s = s.strip().replace(' ', '').replace('\u221e', 'inf')
    N.need(len(s) >= 5 and s[0] in '[]' and s[-1] in '[]', 'Escreve o '
           'intervalo assim: [-2, 5[ (ou com ; se usares v\u00edrgulas decimais)')
    meio = s[1:-1]
    sep = ';' if ';' in meio else ','
    N.need(meio.count(sep) == 1, 'Um intervalo tem dois extremos')
    a, b = meio.split(sep)
    lo, hi = extremo(a), extremo(b)
    N.need(lo != 'inf' and hi != '-inf', 'Extremos trocados')
    lc = s[0] == '[' and lo != '-inf'
    hc = s[-1] == ']' and hi != 'inf'
    lo = None if lo == '-inf' else lo
    hi = None if hi == 'inf' else hi
    if lo is not None and hi is not None:
        c = Q.cmp(lo, hi)
        N.need(c < 0 or (c == 0 and lc and hc), 'O 1.\u00ba extremo tem de ser '
               'menor do que o 2.\u00ba')
    return (lo, lc, hi, hc)


def inteiros(I):
    lo, lc, hi, hc = I
    if lo is None or hi is None:
        return None
    a = -((-lo[0]) // lo[1])
    if Q.cmp((a, 1), lo) == 0 and not lc:
        a += 1
    b = hi[0] // hi[1]
    if Q.cmp((b, 1), hi) == 0 and not hc:
        b -= 1
    return list(range(a, b + 1))


def intv():
    return ('Intervalos de n\u00fameros reais',
            [N.fld('Intervalo A', '', '[-2, 5[', 't'),
             N.fld('Intervalo B (opcional)', '', ']3, +inf[', 't')], _intv)


def _intv(v):
    A = intervalo(v[0])
    o = ['A = ' + Q.istr(A) + ': ' + Q.cond(A)]
    its = [A]
    B = None
    if v[1]:
        B = intervalo(v[1])
        its.append(B)
        o.append('B = ' + Q.istr(B) + ': ' + Q.cond(B))
        C = Q.inter(A, B)
        o.append('> A \u2229 B = ' + Q.istr(C) + (' (' + Q.cond(C) + ')' if C else ''))
        U = Q.uniao(A, B)
        o.append('> A \u222a B = ' + ' \u222a '.join([Q.istr(x) for x in U]))
        alvo = C
    else:
        alvo = A
    if alvo:
        zs = inteiros(alvo)
        if zs is not None:
            o.append('N\u00fameros inteiros em ' + ('A \u2229 B' if B else 'A') +
                     ': ' + (', '.join([str(z) for z in zs[:30]]) +
                             (' ...' if len(zs) > 30 else '') if zs else
                             'nenhum') + ' (' + str(len(zs)) + ')')
        if alvo[0] is not None and alvo[2] is not None:
            o.append('Amplitude: ' + Q.vstr(Q.sub(alvo[2], alvo[0])))
    fin = [x for I in its for x in (I[0], I[2]) if x is not None]
    lo = min([Q.qf(x) for x in fin]) if fin else 0.0
    hi = max([Q.qf(x) for x in fin]) if fin else 1.0
    d = (hi - lo) * 0.25 + 1
    sg = []
    tx = []
    for j in range(len(its)):
        I = its[j]
        y = 2 - j
        a = lo - d if I[0] is None else Q.qf(I[0])
        b = hi + d if I[2] is None else Q.qf(I[2])
        sg.append((a, y, b, y))
        if I[0] is not None:
            tx.append((a, y, '[' if I[1] else ']'))
        if I[2] is not None:
            tx.append((b, y, ']' if I[3] else '['))
    gr = ('Na reta real', [('s', sg, 4), ('t', tx, 5)], lo - d, hi + d, 0, 3,
          'em cima: A' + ('; em baixo: B' if B else ''))
    st = '[a, b]: a \u2264 x \u2264 b (fechado); ]a, b[: a < x < b (aberto).\n' \
        'A \u2229 B: os n\u00fameros que est\u00e3o nos dois (e, \u2227); A \u222a B: os que ' \
        'est\u00e3o em pelo menos um (ou, \u2228).\nNo infinito o intervalo \u00e9 ' \
        'sempre aberto.'
    return ('\n'.join(o), st, None, '', gr)
