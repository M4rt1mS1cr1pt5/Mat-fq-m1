# c_mpol.py - M1TR4M: resolvedores de polinomios (8.o ano em diante):
# desenvolver e simplificar (casos notaveis), fatorizar (fator comum, casos
# notaveis, zeros racionais; equacoes pela lei do anulamento do produto) e
# dividir polinomios (regra de Ruffini e teorema do resto; divisao inteira).
#@ c_mpol.pol|Polin\u00f3mios: desenvolver e simplificar|polin\u00f3mio mon\u00f3mio express\u00e3o alg\u00e9brica casos not\u00e1veis quadrado do bin\u00f3mio diferen\u00e7a de quadrados termos semelhantes grau valor num\u00e9rico|M|a8
#@ c_mpol.fat|Fatorizar e resolver por fatoriza\u00e7\u00e3o|fatorizar fator comum casos not\u00e1veis diferen\u00e7a de quadrados lei do anulamento do produto zeros equa\u00e7\u00e3o do 2.\u00ba grau incompleta|M|a8
#@ c_mpol.ruf|Divis\u00e3o de polin\u00f3mios e regra de Ruffini|regra de ruffini divis\u00e3o inteira de polin\u00f3mios quociente resto teorema do resto divisor fator|M|a8
# Casos-limite: polinomio nulo, letras diferentes no dividendo e no
# divisor, divisor de grau maior, divisor nulo, polinomios sem zeros
# racionais, discriminante negativo, expoentes grandes.

import m1_nucleo as N
import m1_q as Q

MENOS = (-1, 1)

# ------------------------------------------------------------ desenvolver


def binomio(P):
    return len(P) == 2


def caso(t, ex):
    # Nome do caso notavel de um termo (arvore), se for um.
    if t[0] == '^':
        e = Q.cte(Q.poli(t[2]))
        b = Q.poli(t[1])
        if e == (2, 1) and binomio(b):
            return 'quadrado do bin\u00f3mio: (a \u00b1 b)\u00b2 = a\u00b2 \u00b1 2ab + b\u00b2'
        if e == (3, 1) and binomio(b):
            return 'cubo do bin\u00f3mio'
    if t[0] == '*':
        a, b = Q.poli(t[1]), Q.poli(t[2])
        if binomio(a) and binomio(b) and len(ex) == 2 and len(
                Q.padd(a, b)) == 1 and len(Q.padd(a, b, -1)) == 1:
            return 'diferen\u00e7a de quadrados: (a + b)(a - b) = a\u00b2 - b\u00b2'
        if len(a) > 1 or len(b) > 1:
            return 'propriedade distributiva'
    return ''


def pol():
    return ('Polin\u00f3mios: desenvolver e simplificar',
            [N.fld('Express\u00e3o', '', '(2x - 3)^2 - (x + 1)(x - 1)', 't'),
             N.fld('Valor da letra (opcional)', '', '', 'o')], _pol)


def _pol(v):
    s, x0 = v
    N.need(s, 'Escreve uma express\u00e3o, por exemplo (x + 2)^2')
    p = Q.P(s)
    ts = p.termos()
    o = []
    for sg, t, txt in ts:
        e = Q.poli(t)
        nm = caso(t, e)
        if nm or (t[0] in '*^/' and Q.pstr(e) != txt.replace(' ', '')):
            o.append(txt + ' = ' + Q.pstr(e) + ('  (' + nm + ')' if nm else ''))
    P = {}
    for sg, t, txt in ts:
        P = Q.padd(P, Q.poli(t), sg)
    if len(ts) > 1:
        o.append('Juntando os termos semelhantes:')
    o.append('> ' + Q.pstr(P))
    ls = sorted(set([x for m in P for x, e in m]))
    g = Q.grau(P)
    o.append('Grau: ' + (str(g) if P else 'n\u00e3o tem (polin\u00f3mio nulo)') +
             '; termo independente: ' + Q.qs(P.get((), Q.Z)))
    r = None
    if x0 is not None:
        N.need(len(ls) <= 1, 'Para o valor num\u00e9rico, o polin\u00f3mio s\u00f3 pode ter '
               'uma letra')
        f = N.frac(x0[0], 10 ** 6)
        q = Q.R(f[0], f[1]) if f else None
        N.need(q is not None, 'Escreve o valor como inteiro, decimal ou '
               'fra\u00e7\u00e3o')
        r = Q.valor(P, {ls[0]: q}) if ls else P.get((), Q.Z)
        o.append('Valor para ' + (ls[0] if ls else 'x') + ' = ' + Q.qs(q) +
                 ': ' + Q.qs(r))
    st = 'Casos not\u00e1veis: (a + b)\u00b2 = a\u00b2 + 2ab + b\u00b2; (a - b)\u00b2 = ' \
        'a\u00b2 - 2ab + b\u00b2; (a + b)(a - b) = a\u00b2 - b\u00b2.\nMultiplicar ' \
        'polin\u00f3mios: cada termo de um por cada termo do outro.\nTermos ' \
        'semelhantes: a mesma parte literal; somam-se os coeficientes.'
    return ('\n'.join(o), st, Q.qf(r) if r else None, '')

# ------------------------------------------------------------ fatorizar


def isq(n):
    if n < 0:
        return None
    k = int(n ** 0.5)
    while k * k > n:
        k -= 1
    while (k + 1) * (k + 1) <= n:
        k += 1
    return k if k * k == n else None


def lin(q, p, x):
    # (q x - p) com q > 0
    if p == 0:
        return x
    s = ('' if q == 1 else str(q)) + x + (' - ' + str(p) if p > 0 else ' + ' +
                                          str(-p))
    return '(' + s + ')'


def pobj(cs, x):
    return Q.pstr(Q.decoefs(cs, x))


def divide(cs, r):
    # cs (grau 0..n) dividido por (x - r): (quociente, resto)
    n = len(cs) - 1
    q = [Q.Z] * n
    acc = Q.Z
    for i in range(n, 0, -1):
        acc = Q.add(cs[i], Q.mul(r, acc))
        q[i - 1] = acc
    return q, Q.add(cs[0], Q.mul(r, acc))


def fatq(cs, x, o, fs, zs):
    # Fatoriza um polinomio de grau 2 com coeficientes inteiros.
    c, b, a = cs[0][0], cs[1][0], cs[2][0]
    D = b * b - 4 * a * c
    ka, kc = isq(a), isq(abs(c))
    if b == 0 and c < 0 and ka and kc:
        o.append('Diferen\u00e7a de quadrados: ' + pobj(cs, x) + ' = ' + (
            '(' + str(ka) + x + ')' if ka > 1 else x) + '\u00b2 - ' + str(kc) +
            '\u00b2')
        fs += [lin(ka, kc, x), lin(ka, -kc, x)]
        zs += [Q.R(kc, ka), Q.R(-kc, ka)]
        return
    if D == 0 and ka and kc:
        sg = -1 if b * c < 0 or b < 0 else 1
        o.append('Quadrado do bin\u00f3mio: ' + pobj(cs, x) + ' = ' +
                 lin(ka, -sg * kc, x) + '\u00b2')
        fs += [lin(ka, -sg * kc, x)] * 2
        zs += [Q.R(-sg * kc, ka)]
        return
    o.append('\u0394 = b\u00b2 - 4ac = ' + str(D))
    if D < 0:
        o.append('\u0394 < 0: ' + pobj(cs, x) + ' n\u00e3o tem zeros reais; n\u00e3o se '
                 'decomp\u00f5e em fatores do 1.\u00ba grau.')
        fs.append('(' + pobj(cs, x) + ')')
        return
    k = isq(D)
    if k is not None:
        r1, r2 = Q.R(-b + k, 2 * a), Q.R(-b - k, 2 * a)
        o.append('Zeros (f\u00f3rmula resolvente): ' + Q.qs(r2) + ' e ' + Q.qs(r1))
        f = [lin(r1[1], r1[0], x), lin(r2[1], r2[0], x)]
        k2 = Q.R(a, r1[1] * r2[1])
        if k2 != Q.UM:
            fs.append(Q.qs(k2))
        fs += f
        zs += [r2, r1]
        return
    kk, m = 1, D
    for p, e in Q.fatores(D):
        kk *= p ** (e // 2)
        m //= p ** (2 * (e // 2))
    g = Q.mdc(Q.mdc(b, kk), 2 * a)
    rr = (str(kk // g) if kk // g > 1 else '') + '\u221a' + str(m)
    den = '/' + str(2 * a // g) if 2 * a // g > 1 else ''
    if b:
        z1 = ('(' if den else '') + str(-b // g) + ' + ' + rr + (')' if den
                                                                else '') + den
        z2 = ('(' if den else '') + str(-b // g) + ' - ' + rr + (')' if den
                                                                else '') + den
    else:
        z1, z2 = rr + den, '-' + rr + den
    o.append('Zeros irracionais: ' + z2 + ' \u2248 ' + N.fmt((-b - D ** 0.5) /
                                                         (2 * a)) + ' e ' +
             z1 + ' \u2248 ' + N.fmt((-b + D ** 0.5) / (2 * a)))
    fs.append((str(a) if a != 1 else '') + fz(z1, x) + fz(z2, x))
    zs += [z2, z1]


def fz(z, x):
    # Fator (x - z) para um zero escrito com radicais.
    if z.startswith('-') and ' ' not in z:
        return '(' + x + ' + ' + z[1:] + ')'
    if ' ' in z and not z.startswith('('):
        return '(' + x + ' - (' + z + '))'
    return '(' + x + ' - ' + z + ')'


def fat():
    return ('Fatorizar e resolver por fatoriza\u00e7\u00e3o',
            [N.fld('Polin\u00f3mio ou equa\u00e7\u00e3o (... = ...)', '', 'x^3 - 4x', 't')],
            _fat)


def _fat(v):
    s = v[0]
    N.need(s, 'Escreve um polin\u00f3mio, por exemplo x^2 - 9')
    eq = '=' in s
    if eq:
        N.need(s.count('=') == 1, 'S\u00f3 um sinal =')
        a, b = s.split('=')
        N.need(a.strip() and b.strip(), 'Falta um membro da equa\u00e7\u00e3o')
        P = Q.padd(Q.poli(Q.arvore(a)), Q.poli(Q.arvore(b)), -1)
    else:
        P = Q.poli(Q.arvore(s))
    N.need(P, 'O polin\u00f3mio \u00e9 nulo')
    ls = sorted(set([x for m in P for x, e in m]))
    o = []
    if eq:
        o.append('Tudo no 1.\u00ba membro: ' + Q.pstr(P) + ' = 0')
    # fator comum (coeficiente e letras)
    L = Q.denl(P)
    Pi = Q.pesc(P, (L, 1))
    g = 0
    for m in Pi:
        g = Q.mdc(g, Pi[m][0])
    lead = Pi[Q.ordem(Pi)[0]][0]
    c = Q.R(g if lead > 0 else -g, L)
    mins = {}
    for x in ls:
        mins[x] = min([dict(m).get(x, 0) for m in P])
    fm = tuple([(x, mins[x]) for x in ls if mins[x]])
    R = {}
    for m in P:
        d = dict(m)
        m2 = tuple([(x, d[x] - mins.get(x, 0)) for x in sorted(d)
                    if d[x] - mins.get(x, 0)])
        R[m2] = Q.div(P[m], c)
    ca = (abs(c[0]), c[1])
    fc = ('-' if c[0] < 0 else '') + ('' if ca == Q.UM else (
        '(' + Q.qs(ca) + ')' if ca[1] > 1 else Q.qs(ca))) + Q.mstr(fm)
    if fc == '-':
        o.append('Sinal - em evid\u00eancia: ' + Q.pstr(P) + ' = -(' +
                 Q.pstr(R) + ')')
    elif fc:
        o.append('Fator comum: ' + fc + ', logo ' + Q.pstr(P) + ' = ' + fc +
                 '(' + Q.pstr(R) + ')')
    fs = []
    zs = []
    if len(ls) > 1:
        N.need(not eq, 'Para resolver, a equa\u00e7\u00e3o s\u00f3 pode ter uma letra')
        res = fc + '(' + Q.pstr(R) + ')' if fc else Q.pstr(P)
        o.append('> ' + res)
        return ('\n'.join(o), ST_FAT, None, '')
    x = ls[0] if ls else 'x'
    if fm:
        zs.append(Q.Z)
    cs = Q.coefs(R, x) if R else [Q.UM]
    # zeros racionais (grau 3 ou mais)
    while len(cs) > 3:
        rs = Q.raizes_rac(cs)
        if not rs:
            o.append(pobj(cs, x) + ' n\u00e3o tem zeros racionais.')
            fs.append('(' + pobj(cs, x) + ')')
            cs = None
            break
        r = rs[0]
        qcs, resto = divide(cs, r)
        o.append(x + ' = ' + Q.qs(r) + ' \u00e9 zero (resto 0): divide-se por ' +
                 lin(r[1], r[0], x) + ' [Ruffini]')
        fs.append(lin(r[1], r[0], x))
        zs.append(r)
        cs = [Q.div(y, (r[1], 1)) for y in qcs]
    if cs is not None:
        if len(cs) == 3:
            fatq(cs, x, o, fs, zs)
        elif len(cs) == 2:
            fs.append(lin(cs[1][0], -cs[0][0], x) if cs[1][0] > 0 else
                      '(' + pobj(cs, x) + ')')
            zs.append(Q.div(Q.neg(cs[0]), cs[1]))
    txt = junta(fc, fs)
    o.append('> ' + Q.pstr(P) + ' = ' + txt)
    if eq:
        reais = [z for z in zs if not isinstance(z, str)]
        reais.sort(key=lambda z: Q.qf(z))
        irr = [z for z in zs if isinstance(z, str)]
        vs = [Q.vstr(z) for z in reais] + irr
        o.append('Lei do anulamento do produto: cada fator igual a zero.')
        o.append('> C.S. = ' + ('{' + '; '.join(vs) + '}' if vs else '\u2205'))
    return ('\n'.join(o), ST_FAT, None, '')


def junta(fc, fs):
    # Junta fatores iguais em potencias: (x - 1)(x - 1) -> (x - 1)\u00b2
    o = []
    for f in fs:
        for k in range(len(o)):
            if o[k][0] == f:
                o[k][1] += 1
                break
        else:
            o.append([f, 1])
    t = ''.join([f + (N.sup(n) if n > 1 else '') for f, n in o])
    return (fc + t) if fc and fc != '-' else ((fc or '') + t)


ST_FAT = 'Por ordem: fator comum; casos not\u00e1veis (a\u00b2 - b\u00b2 = (a - b)(a + b); ' \
    'a\u00b2 \u00b1 2ab + b\u00b2 = (a \u00b1 b)\u00b2); zeros (com a f\u00f3rmula resolvente ou a ' \
    'regra de Ruffini).\nLei do anulamento do produto: a \u00d7 b = 0 \u21d4 a = 0 ' \
    '\u2228 b = 0.'

# ------------------------------------------------------------ dividir


def ruf():
    return ('Divis\u00e3o de polin\u00f3mios (Ruffini)',
            [N.fld('Dividendo D(x)', '', '2x^3 - 3x^2 + 4', 't'),
             N.fld('Divisor d(x)', '', 'x - 2', 't')], _ruf)


def _ruf(v):
    sD, sd = v
    N.need(sD and sd, 'Escreve o dividendo e o divisor')
    D = Q.poli(Q.arvore(sD))
    d = Q.poli(Q.arvore(sd))
    N.need(d, 'O divisor n\u00e3o pode ser nulo')
    ls = sorted(set([x for m in list(D) + list(d) for x, e in m]))
    N.need(len(ls) <= 1, 'Os polin\u00f3mios s\u00f3 podem ter uma letra (e a mesma)')
    x = ls[0] if ls else 'x'
    cD = Q.coefs(D, x) if D else [Q.Z]
    cd = Q.coefs(d, x)
    N.need(len(cD) <= 11, 'Grau demasiado grande (m\u00e1ximo 10)')
    o = []
    if len(cd) == 2:
        a, b = cd[1], cd[0]
        r = Q.div(Q.neg(b), a)
        o.append('Coeficientes de D (os que faltam s\u00e3o 0): ' + ', '.join(
            [Q.qs(c) for c in reversed(cD)]))
        o.append('Regra de Ruffini com ' + Q.qs(r) + ' (zero do divisor):')
        acc = Q.Z
        qs = []
        for i in range(len(cD) - 1, -1, -1):
            if i == len(cD) - 1:
                acc = cD[i]
                o.append(' ' + Q.qs(acc))
            else:
                novo = Q.add(cD[i], Q.mul(r, acc))
                o.append(' ' + Q.qs(cD[i]) + ' + ' + Q.qp(r) + ' \u00d7 ' +
                         Q.qp(acc) + ' = ' + Q.qs(novo) + (' (resto)' if i == 0
                                                          else ''))
                acc = novo
            if i:
                qs.insert(0, acc)
        resto = acc if len(cD) > 1 else cD[0]
        if len(cD) == 1:
            qs = []
            resto = cD[0]
        if a != Q.UM:
            o.append('Como d(x) = ' + Q.qs(a) + '(' + x + ' - ' + Q.qp(r) +
                     '), divide-se o quociente por ' + Q.qs(a) + '.')
            qs = [Q.div(c, a) for c in qs]
        Qx = Q.decoefs(qs, x) if qs else {}
        R = {(): resto} if resto[0] else {}
        o.append('Teorema do resto: D(' + Q.qs(r) + ') = ' + Q.qs(
            Q.valor(D, {x: r}) if D else Q.Z))
    else:
        N.need(len(cd) > 1 or cd[0][0], 'Divis\u00e3o por zero')
        Qx, R = {}, dict(D)
        gd = len(cd) - 1
        lt = cd[-1]
        while R and Q.grau(R) >= gd:
            g = Q.grau(R)
            c = Q.div(Q.coefs(R, x)[g], lt)
            t = {((x, g - gd),) if g - gd else (): c}
            Qx = Q.padd(Qx, t)
            R = Q.padd(R, Q.pmul(t, d), -1)
            o.append('Termo ' + Q.pstr(t) + ': resto parcial ' + Q.pstr(R))
    o.append('> Quociente: ' + Q.pstr(Qx) + ' ; resto: ' + Q.pstr(R))
    o.append('D(x) = d(x) \u00d7 Q(x) + R(x): ' + Q.pstr(D) + ' = (' + Q.pstr(d) +
             ')(' + Q.pstr(Qx) + ')' + ('' if not R else ' + ' + Q.pstr(R)))
    chk = Q.padd(Q.padd(Q.pmul(d, Qx), R), D, -1)
    o.append('Confirma\u00e7\u00e3o: ' + ('\u2713' if not chk else '\u2717'))
    if not R:
        o.append('O resto \u00e9 0: ' + Q.pstr(d) + ' \u00e9 um fator de ' + Q.pstr(D) +
                 '.')
    st = 'Ruffini (divisor x - a): baixa-se o 1.\u00ba coeficiente; depois, ' \
        'multiplica-se por a e soma-se ao coeficiente seguinte.\nO \u00faltimo ' \
        'n\u00famero \u00e9 o resto. Teorema do resto: o resto da divis\u00e3o por x - a \u00e9 ' \
        'D(a).\nDivisor ax + b: usa-se o zero -b/a e divide-se o quociente ' \
        'por a.'
    return ('\n'.join(o), st, None, '')
