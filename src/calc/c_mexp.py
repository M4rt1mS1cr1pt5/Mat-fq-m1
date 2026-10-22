# c_mexp.py - M1TR4M: resolvedores de equacoes (7.o ao 9.o ano): equacao
# do 1.o grau passo a passo (parenteses, denominadores, equacoes literais),
# inequacao do 1.o grau (com conjuncao ou disjuncao) e sistema de duas
# equacoes do 1.o grau pelo metodo de substituicao, com grafico.
#@ c_mexp.eq1|Equa\u00e7\u00e3o do 1.\u00ba grau (passo a passo)|equa\u00e7\u00e3o do primeiro grau resolver inc\u00f3gnita par\u00eanteses denominadores mmc equa\u00e7\u00e3o literal poss\u00edvel imposs\u00edvel indeterminada|M|a7
#@ c_mexp.ineq|Inequa\u00e7\u00e3o do 1.\u00ba grau|inequa\u00e7\u00e3o do primeiro grau conjunto-solu\u00e7\u00e3o intervalo inverter o sinal conjun\u00e7\u00e3o disjun\u00e7\u00e3o dupla|M|a9
#@ c_mexp.sis|Sistema de duas equa\u00e7\u00f5es (substitui\u00e7\u00e3o)|sistema de duas equa\u00e7\u00f5es do primeiro grau m\u00e9todo de substitui\u00e7\u00e3o retas interse\u00e7\u00e3o poss\u00edvel determinado imposs\u00edvel indeterminado|M|a8
# Casos-limite: sem incognita, varias letras sem dizer a incognita, grau
# 2 ou mais, 0x = 0 e 0x = b, divisao por negativo, sistemas impossiveis e
# indeterminados, relacoes a mais ou a menos.

import m1_nucleo as N
import m1_q as Q

RELS = (('<=', '\u2264'), ('>=', '\u2265'), ('\u2264', '\u2264'),
        ('\u2265', '\u2265'), ('<', '<'), ('>', '>'), ('=', '='))
INV = {'<': '>', '>': '<', '\u2264': '\u2265', '\u2265': '\u2264'}
MENOS = (-1, 1)


def partes(s):
    # "a < b <= c" -> (['a', 'b', 'c'], ['<', '\u2264'])
    s = s.replace('=<', '<=').replace('=>', '>=')
    ps, rs = [], []
    i = 0
    ini = 0
    while i < len(s):
        for t, r in RELS:
            if s.startswith(t, i):
                ps.append(s[ini:i])
                rs.append(r)
                i += len(t)
                ini = i
                break
        else:
            i += 1
    ps.append(s[ini:])
    for p in ps:
        N.need(p.strip(), 'Falta um membro da ' + ('equa\u00e7\u00e3o' if '=' in rs
                                                    else 'inequa\u00e7\u00e3o'))
    return ps, rs


def lado(s):
    t = Q.arvore(s)
    return Q.poli(t), Q.letras(t)


def soma(ps):
    # Escreve uma soma de pedacos (polinomios) sem os juntar.
    o = ''
    for p in ps:
        t = Q.pstr(p)
        if t == '0':
            continue
        if not o:
            o = t
        elif t.startswith('-'):
            o += ' - ' + t[1:]
        else:
            o += ' + ' + t
    return o or '0'


def separa(A, x):
    a = dict([(m, A[m]) for m in A if dict(m).get(x)])
    b = dict([(m, A[m]) for m in A if not dict(m).get(x)])
    return a, b


def termos(A):
    return [{m: A[m]} for m in Q.ordem(A)]


def coef(A, x):
    # A = C x + D, com C e D sem x: devolve C.
    C = {}
    for m in A:
        if dict(m).get(x):
            C[tuple([(v, e) for v, e in m if v != x])] = A[m]
    return C


def mx(A, x):
    # "3x", "-x", "(a + b)x"
    c = Q.cte(A)
    if c is not None:
        return Q.pstr(Q.pmul(A, {((x, 1),): Q.UM})) if c[0] else '0' + x
    if len(A) == 1:
        return Q.pstr(Q.pmul(A, {((x, 1),): Q.UM}))
    return '(' + Q.pstr(A) + ')' + x


def resolve1(L, R, x, o, rel, txt):
    # Parenteses, denominadores, separar os termos e reduzir: A x (rel) B.
    if '(' in txt or '/' in txt:
        o.append('Sem par\u00eanteses: ' + Q.pstr(L) + ' ' + rel + ' ' + Q.pstr(R))
    k = Q.mmc(Q.denl(L), Q.denl(R))
    if k > 1:
        L = Q.pesc(L, (k, 1))
        R = Q.pesc(R, (k, 1))
        o.append('\u00d7 ' + str(k) + ' (m.m.c. dos denominadores): ' +
                 Q.pstr(L) + ' ' + rel + ' ' + Q.pstr(R))
    Lx, L0 = separa(L, x)
    Rx, R0 = separa(R, x)
    if Rx or L0:
        o.append('Termos com ' + x + ' no 1.\u00ba membro: ' + soma(
            termos(Lx) + [Q.pesc(t, MENOS) for t in termos(Rx)]) + ' ' + rel +
            ' ' + soma(termos(R0) + [Q.pesc(t, MENOS) for t in termos(L0)]))
    A = coef(Q.padd(Lx, Rx, -1), x)
    B = Q.padd(R0, L0, -1)
    o.append('Reduzindo: ' + mx(A, x) + ' ' + rel + ' ' + Q.pstr(B))
    return A, B


def incognita(vs, tx, nm):
    if tx:
        x = tx.strip()
        if x not in vs:
            c = [v for v in vs if v.lower() == x.lower()]
            N.need(len(c) == 1, 'A inc\u00f3gnita ' + x + ' n\u00e3o est\u00e1 na ' + nm)
            x = c[0]
        return x
    N.need(vs, 'A ' + nm + ' n\u00e3o tem inc\u00f3gnita (nenhuma letra)')
    N.need(len(vs) == 1, 'A ' + nm + ' tem as letras ' + ', '.join(vs) +
           ': escreve qual \u00e9 a inc\u00f3gnita')
    return vs[0]


def grau_aviso(D, x):
    g = Q.grau(D, x)
    if g == 2 and len(set([v for m in D for v, e in m])) == 1:
        cs = Q.coefs(D, x)
        N.err('\u00c9 uma equa\u00e7\u00e3o do 2.\u00ba grau: ' + Q.pstr(D) + ' = 0 (a = ' +
              Q.qs(cs[2]) + ', b = ' + Q.qs(cs[1]) + ', c = ' + Q.qs(cs[0]) +
              '); usa a calculadora do 2.\u00ba grau')
    N.need(g <= 1, 'N\u00e3o \u00e9 do 1.\u00ba grau em ' + x + ' (grau ' + str(g) + '); usa '
           'a fatoriza\u00e7\u00e3o')


def negativo(A):
    return A[Q.ordem(A)[0]][0] < 0 if A else False

# ------------------------------------------------------------ equacao


def eq1():
    return ('Equa\u00e7\u00e3o do 1.\u00ba grau',
            [N.fld('Equa\u00e7\u00e3o', '', '3(x - 2) + 4 = 2x - 1', 't'),
             N.fld('Inc\u00f3gnita (se houver outras letras)', '', '', 't')], _eq1)


def _eq1(v):
    s, tx = v
    N.need(s, 'Escreve a equa\u00e7\u00e3o, por exemplo 2x + 3 = 7')
    ps, rs = partes(s)
    N.need(rs == ['='], 'Escreve uma equa\u00e7\u00e3o com um s\u00f3 sinal =')
    L, l1 = lado(ps[0])
    R, l2 = lado(ps[1])
    vs = sorted(set(l1 + l2))
    x = incognita(vs, tx, 'equa\u00e7\u00e3o')
    grau_aviso(Q.padd(L, R, -1), x)
    o = []
    A, B = resolve1(L, R, x, o, '=', s)
    c = Q.cte(A)
    r = None
    if c is None:
        if negativo(A):
            A, B = Q.pesc(A, MENOS), Q.pesc(B, MENOS)
            o.append('Multiplicando por -1: ' + mx(A, x) + ' = ' + Q.pstr(B))
        o.append('> ' + x + ' = ' + frac_txt(B, A) + ' (se ' + Q.pstr(A) +
                 ' \u2260 0)')
    elif c[0] == 0:
        if not B:
            o.append('> 0' + x + ' = 0: equa\u00e7\u00e3o poss\u00edvel e indeterminada; '
                     'C.S. = \u211d')
        else:
            o.append('> 0' + x + ' = ' + Q.pstr(B) + ': equa\u00e7\u00e3o imposs\u00edvel; '
                     'C.S. = \u2205')
    else:
        b = Q.cte(B)
        if b is not None:
            r = Q.div(b, c)
            if c != Q.UM:
                o.append('Dividindo por ' + Q.qp(c) + ': ' + x + ' = ' +
                         Q.qs(b) + ' : ' + Q.qp(c))
            o.append('> ' + x + ' = ' + Q.qs(r) + ' ; C.S. = {' + Q.vstr(r) +
                     '}')
            v1 = Q.valor(L, {x: r})
            v2 = Q.valor(R, {x: r})
            o.append('Verifica\u00e7\u00e3o: 1.\u00ba membro = ' + Q.qs(v1) + ' e 2.\u00ba membro '
                     '= ' + Q.qs(v2) + (' \u2713' if v1 == v2 else ' \u2717'))
        else:
            o.append('> ' + x + ' = ' + frac_txt(B, A))
    st = 'Resolver: tirar os par\u00eanteses; tirar os denominadores (multiplicar ' \
        'tudo pelo m.m.c.); passar os termos com a inc\u00f3gnita para um membro ' \
        '(trocando o sinal); reduzir; dividir pelo coeficiente.\n0x = 0: ' \
        'poss\u00edvel e indeterminada; 0x = b (b \u2260 0): imposs\u00edvel.'
    return ('\n'.join(o), st, Q.qf(r) if r else None, '')


def frac_txt(B, A):
    c = Q.cte(A)
    if c is not None:
        return Q.pstr(Q.pesc(B, Q.div(Q.UM, c)))
    b = Q.pstr(B)
    return ('(' + b + ')' if len(B) > 1 else b) + ' / ' + (
        '(' + Q.pstr(A) + ')' if len(A) > 1 else Q.pstr(A))

# ------------------------------------------------------------ inequacao


def ineq():
    return ('Inequa\u00e7\u00e3o do 1.\u00ba grau',
            [N.fld('Inequa\u00e7\u00e3o (ex.: 3 - 2x >= 7)', '', '3 - 2x >= 7', 't'),
             N.fld('2.\u00aa inequa\u00e7\u00e3o (opcional)', '', '', 't'),
             N.fld('Liga\u00e7\u00e3o das duas', '', '', 'c',
                   ['e (\u2227, interse\u00e7\u00e3o)', 'ou (\u2228, reuni\u00e3o)'])], _ineq)


def uma(s, o, x=None):
    ps, rs = partes(s)
    N.need(rs and '=' not in rs and len(rs) <= 2, 'Escreve uma inequa\u00e7\u00e3o com '
           '<, >, <= ou >= (por exemplo 2x + 1 < 7)')
    if len(rs) == 2:
        o.append('Inequa\u00e7\u00e3o dupla: ' + ps[0].strip() + ' ' + rs[0] + ' ' +
                 ps[1].strip() + ' e ' + ps[1].strip() + ' ' + rs[1] + ' ' +
                 ps[2].strip())
        I1, x = uma(ps[0] + rs[0] + ps[1], o, x)
        I2, x = uma(ps[1] + rs[1] + ps[2], o, x)
        return Q.inter(I1, I2) if I1 and I2 else None, x
    L, l1 = lado(ps[0])
    R, l2 = lado(ps[1])
    vs = sorted(set(l1 + l2))
    x = x or incognita(vs, '', 'inequa\u00e7\u00e3o')
    N.need(vs == [x] or not vs, 'Usa s\u00f3 a inc\u00f3gnita ' + x)
    grau_aviso(Q.padd(L, R, -1), x)
    rel = rs[0]
    A, B = resolve1(L, R, x, o, rel, s)
    a = Q.cte(A)
    b = Q.cte(B) or Q.Z
    if a[0] == 0:
        ok = {'<': 0 < b[0], '>': 0 > b[0], '\u2264': 0 <= b[0],
              '\u2265': 0 >= b[0]}[rel]
        o.append('0 ' + rel + ' ' + Q.qs(b) + ' \u00e9 ' + ('sempre verdade: '
                                                      'C.S. = \u211d' if ok else
                                                      'falso: C.S. = \u2205'))
        return ((None, False, None, False) if ok else None), x
    r = Q.div(b, a)
    if a[0] < 0:
        rel = INV[rel]
        o.append('Dividindo por ' + Q.qp(a) + ' (negativo), o sinal inverte-'
                 'se: ' + x + ' ' + rel + ' ' + Q.qs(r))
    elif a != Q.UM:
        o.append('Dividindo por ' + Q.qp(a) + ': ' + x + ' ' + rel + ' ' +
                 Q.qs(r))
    if rel in ('<', '\u2264'):
        I = (None, False, r, rel == '\u2264')
    else:
        I = (r, rel == '\u2265', None, False)
    o.append('C.S. = ' + Q.istr(I))
    return I, x


def _ineq(v):
    s1, s2, lig = v
    N.need(s1, 'Escreve a inequa\u00e7\u00e3o')
    o = []
    I1, x = uma(s1, o)
    res = [I1] if I1 else []
    if s2:
        o.append('2.\u00aa inequa\u00e7\u00e3o:')
        I2, x = uma(s2, o, x)
        if lig == 0:
            C = Q.inter(I1, I2) if I1 and I2 else None
            res = [C] if C else []
            o.append('Interse\u00e7\u00e3o (e):')
        else:
            res = Q.uniao(I1, I2) if I1 and I2 else [I for I in (I1, I2) if I]
            o.append('Reuni\u00e3o (ou):')
    o.append('> C.S. = ' + (' \u222a '.join([Q.istr(I) for I in res]) if res
                            else '\u2205'))
    st = 'Resolve-se como uma equa\u00e7\u00e3o, mas ao multiplicar ou dividir por um ' \
        'n\u00famero negativo o sinal da desigualdade inverte-se.\nO conjunto-' \
        'solu\u00e7\u00e3o escreve-se com intervalos; e (\u2227): interse\u00e7\u00e3o; ou (\u2228): ' \
        'reuni\u00e3o.'
    return ('\n'.join(o), st, None, '')

# ------------------------------------------------------------ sistema


def forma(D, vs, k):
    # D = a x + b y + d (= 0) -> (a, b, c) com a x + b y = c (inteiros)
    N.need(Q.grau(D) <= 1, 'A ' + str(k) + '.\u00aa equa\u00e7\u00e3o n\u00e3o \u00e9 do 1.\u00ba grau')
    D = Q.pesc(D, (Q.denl(D), 1))
    a = D.get(((vs[0], 1),), Q.Z)
    b = D.get(((vs[1], 1),), Q.Z)
    return a, b, Q.neg(D.get((), Q.Z))


def lin(ts):
    # [(coeficiente, texto)] -> "2(-y + 5) - y"; texto '' para constantes.
    o = ''
    for c, t in ts:
        if c[0] == 0:
            continue
        a = (abs(c[0]), c[1])
        if t:
            p = ('' if a == Q.UM else ('(' + Q.qs(a) + ')' if a[1] > 1 else
                                       Q.qs(a))) + t
        else:
            p = Q.qs(a)
        if not o:
            o = ('-' if c[0] < 0 else '') + p
        else:
            o += (' - ' if c[0] < 0 else ' + ') + p
    return o or '0'


def sis():
    return ('Sistema de duas equa\u00e7\u00f5es',
            [N.fld('1.\u00aa equa\u00e7\u00e3o', '', 'x + y = 5', 't'),
             N.fld('2.\u00aa equa\u00e7\u00e3o', '', '2x - y = 1', 't')], _sis)


def _sis(v):
    eqs = []
    vs = []
    for k in range(2):
        N.need(v[k], 'Escreve a ' + str(k + 1) + '.\u00aa equa\u00e7\u00e3o')
        ps, rs = partes(v[k])
        N.need(rs == ['='], 'A ' + str(k + 1) + '.\u00aa equa\u00e7\u00e3o tem de ter um s\u00f3 '
               'sinal =')
        L, l1 = lado(ps[0])
        R, l2 = lado(ps[1])
        eqs.append(Q.padd(L, R, -1))
        vs = sorted(set(vs + l1 + l2))
    N.need(len(vs) == 2, 'O sistema tem de ter duas inc\u00f3gnitas (encontrei ' +
           (', '.join(vs) or 'nenhuma') + ')')
    E = [forma(eqs[k], vs, k + 1) for k in range(2)]
    for k in range(2):
        N.need(E[k][0][0] or E[k][1][0], 'A ' + str(k + 1) + '.\u00aa equa\u00e7\u00e3o n\u00e3o '
               'tem inc\u00f3gnitas')
    o = ['Forma reduzida:']
    for k in range(2):
        o.append(' ' + str(k + 1) + '.\u00aa: ' + lin([(E[k][0], vs[0]),
                                                  (E[k][1], vs[1])]) + ' = ' +
                 Q.qs(E[k][2]))
    esc = None
    for i, j in ((0, 0), (0, 1), (1, 0), (1, 1)):
        if abs(E[i][j][0]) == 1 and E[i][j][1] == 1:
            esc = (i, j)
            break
    if esc is None:
        esc = (0, 0) if E[0][0][0] else (0, 1)
    i, j = esc
    u, w = vs[j], vs[1 - j]
    al, be, ga = E[i][j], E[i][1 - j], E[i][2]
    c0 = Q.div(ga, al)
    c1 = Q.neg(Q.div(be, al))
    ex = lin([(c1, w), (c0, '')])
    o.append('Da ' + str(i + 1) + '.\u00aa equa\u00e7\u00e3o: ' + u + ' = ' + ex)
    k = 1 - i
    al2, be2, ga2 = E[k][j], E[k][1 - j], E[k][2]
    sub = lin([(be2, w)]) if not al2[0] else (
        ('-' if al2 == (-1, 1) else ('' if al2 == Q.UM else Q.qs(al2))) +
        '(' + ex + ')' + (('' if not be2[0] else (' - ' if be2[0] < 0 else ' + ') +
                           lin([((abs(be2[0]), be2[1]), w)]))))
    o.append('Substituindo na ' + str(k + 1) + '.\u00aa: ' + sub + ' = ' + Q.qs(ga2))
    K = Q.add(be2, Q.mul(al2, c1))
    M = Q.sub(ga2, Q.mul(al2, c0))
    o.append('Reduzindo: ' + lin([(K, w)]) + ' = ' + Q.qs(M))
    r = None
    if K[0] == 0:
        if M[0] == 0:
            o.append('> 0' + w + ' = 0: sistema poss\u00edvel e indeterminado '
                     '(infinitas solu\u00e7\u00f5es; as retas s\u00e3o coincidentes)')
        else:
            o.append('> 0' + w + ' = ' + Q.qs(M) + ': sistema imposs\u00edvel (as '
                     'retas s\u00e3o paralelas)')
    else:
        yw = Q.div(M, K)
        xu = Q.add(c0, Q.mul(c1, yw))
        if K != Q.UM:
            o.append(w + ' = ' + Q.qs(M) + ' : ' + Q.qp(K) + ' = ' + Q.qs(yw))
        o.append(u + ' = ' + ex.replace(w, '(' + Q.qs(yw) + ')') + ' = ' +
                 Q.qs(xu))
        sol = {u: xu, w: yw}
        r = sol
        par = '(' + Q.vstr(sol[vs[0]]) + Q.sepr(sol[vs[0]], sol[vs[1]]) + \
            Q.vstr(sol[vs[1]]) + ')'
        o.append('> (' + vs[0] + ', ' + vs[1] + ') = ' + par +
                 '; poss\u00edvel e determinado')
        ok = [Q.valor(eqs[q], sol)[0] == 0 for q in range(2)]
        o.append('Verifica\u00e7\u00e3o nas duas equa\u00e7\u00f5es: ' + ' e '.join(
            ['\u2713' if b else '\u2717' for b in ok]))
        o.append('As duas retas intersetam-se no ponto ' + par + '.')
    its = []
    cx, cy = (Q.qf(r[vs[0]]), Q.qf(r[vs[1]])) if r else (0.0, 0.0)
    sg = []
    for q in range(2):
        a, b, c = [Q.qf(z) for z in E[q]]
        if b:
            def f(t, a=a, b=b, c=c):
                return (c - a * t) / b
            its.append(('f', f, 4 + q))
        elif a:
            sg.append((c / a, cy - 100, c / a, cy + 100))
    if sg:
        its.append(('s', sg, 6))
    if r:
        its.append(('p', [(cx, cy)], 2))
    gr = ('Sistema: as duas retas', its, cx - 8, cx + 8, cy - 4.5, cy + 4.5,
          vs[0] + ' na horizontal, ' + vs[1] + ' na vertical; ponto: a solu\u00e7\u00e3o')
    st = 'M\u00e9todo de substitui\u00e7\u00e3o: resolve-se uma equa\u00e7\u00e3o em ordem a uma ' \
        'inc\u00f3gnita e substitui-se na outra.\nCada equa\u00e7\u00e3o \u00e9 uma reta; a ' \
        'solu\u00e7\u00e3o \u00e9 o ponto de interse\u00e7\u00e3o (se as retas forem paralelas, n\u00e3o ' \
        'h\u00e1 solu\u00e7\u00e3o; se coincidirem, h\u00e1 infinitas).'
    return ('\n'.join(o), st, None, '', gr)
