# m1_q.py - M1TR4M: aritmetica exata para os resolvedores de Matematica.
# Racionais como pares (n, d) com d > 0 e mdc(n, d) = 1; leitura de
# expressoes escritas pelo aluno para uma arvore (nunca eval); polinomios
# numa ou mais letras com coeficientes racionais, escritos como nos manuais
# (2x\u00b2 - x + 1/2). Carregado pelos resolvedores que precisam dele e
# libertado com eles (ranhura 'c').

import m1_nucleo as N

VER = 1
Z = (0, 1)
UM = (1, 1)
MAXLEN = 200
MAXPAR = 20

# ------------------------------------------------------------ racionais


def mdc(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def mmc(a, b):
    return abs(a * b) // mdc(a, b) if a and b else 0


def R(n, d=1):
    if d == 0:
        N.err('Divis\u00e3o por zero')
    if d < 0:
        n, d = -n, -d
    g = mdc(n, d) or 1
    n, d = n // g, d // g
    if abs(n) > 10 ** 40 or d > 10 ** 40:
        N.err('N\u00famero demasiado grande')
    return (n, d)


def add(a, b):
    return R(a[0] * b[1] + b[0] * a[1], a[1] * b[1])


def sub(a, b):
    return R(a[0] * b[1] - b[0] * a[1], a[1] * b[1])


def mul(a, b):
    return R(a[0] * b[0], a[1] * b[1])


def div(a, b):
    if b[0] == 0:
        N.err('Divis\u00e3o por zero')
    return R(a[0] * b[1], a[1] * b[0])


def neg(a):
    return (-a[0], a[1])


def cmp(a, b):
    x = a[0] * b[1] - b[0] * a[1]
    return (x > 0) - (x < 0)


def pw(a, k):
    # Potencia de expoente inteiro.
    if k < 0:
        if a[0] == 0:
            N.err('0 n\u00e3o tem pot\u00eancias de expoente negativo')
        a, k = R(a[1], a[0]), -k
    N.need(k <= 60, 'Expoente demasiado grande')
    return R(a[0] ** k, a[1] ** k)


def qf(a):
    return a[0] / a[1]


def qs(a):
    # "3", "-3/4"
    return str(a[0]) if a[1] == 1 else str(a[0]) + '/' + str(a[1])


def qp(a):
    # Como qs, mas entre parenteses se for negativo: 2 x (-3)
    s = qs(a)
    return '(' + s + ')' if a[0] < 0 else s


def isint(a):
    return a[1] == 1


def numq(t):
    # "2,5" -> (5, 2); aceita virgula ou ponto e expoente e-3.
    t = t.replace(',', '.')
    e = 0
    k = t.find('e')
    if k >= 0:
        e = int(t[k + 1:])
        t = t[:k]
    if t.count('.') > 1 or t in ('', '.'):
        N.err('N\u00famero mal escrito: ' + t)
    if '.' in t:
        a, b = t.split('.')
        r = R(int(a or '0') * 10 ** len(b) + int(b or '0'), 10 ** len(b))
    else:
        r = R(int(t), 1)
    N.need(abs(e) <= 30, 'Expoente demasiado grande')
    return mul(r, pw((10, 1), e)) if e else r


def fatores(n):
    # Decomposicao em fatores primos: [(p, e), ...].
    n = abs(n)
    out = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1 if p == 2 else 2
        N.need(p < 2000000, 'N\u00famero demasiado grande para decompor')
    if n > 1:
        out.append((n, 1))
    return out


def fstr(fs):
    # [(2, 3), (5, 1)] -> "2\u00b3 \u00d7 5"
    if not fs:
        return '1'
    return ' \u00d7 '.join([str(p) + (N.sup(e) if e > 1 else '') for p, e in fs])


def dizima(a, maxp=60):
    # Dizima de a: "2,25", "0,1(6)", "-3,(142857)".
    n, d = a
    s = '-' if n < 0 else ''
    n = abs(n)
    s += str(n // d)
    r = n % d
    if r == 0:
        return s
    ds = []
    vistos = {}
    while r and r not in vistos and len(ds) < maxp:
        vistos[r] = len(ds)
        r *= 10
        ds.append(str(r // d))
        r %= d
    if r == 0:
        return s + ',' + ''.join(ds)
    if r in vistos:
        i = vistos[r]
        return s + ',' + ''.join(ds[:i]) + '(' + ''.join(ds[i:]) + ')'
    return s + ',' + ''.join(ds) + '...'

# ------------------------------------------------------------ leitura


TROCA = {'\u2212': '-', '\u2013': '-', '\u00d7': '*', '\u00b7': '*',
         '\u00f7': ':', '[': '(', '{': '(', ']': ')', '}': ')',
         '\u221a': 'r'}
FUN = {'sqrt': 'r', 'raiz': 'r'}


def dig(c):
    return '0' <= c <= '9'


def toks(s):
    # Lista de (tipo, valor, posicao): 'n' numero (racional), 'v' letra,
    # 'o' operador (+ - * / ^), 'f' funcao (r: raiz quadrada), '(' e ')'.
    N.need(s.strip(), 'Escreve uma express\u00e3o')
    N.need(len(s) <= MAXLEN, 'Express\u00e3o demasiado longa (m\u00e1ximo ' +
           str(MAXLEN) + ' carateres)')
    out = []
    i = 0
    while i < len(s):
        c = TROCA.get(s[i], s[i])
        if c == ' ':
            i += 1
        elif dig(c) or (c in '.,' and i + 1 < len(s) and dig(s[i + 1])):
            j = i
            while j < len(s) and (dig(s[j]) or s[j] in '.,'):
                j += 1
            if j < len(s) and s[j] in 'eE' and j + 1 < len(s) and (
                    dig(s[j + 1]) or (s[j + 1] in '+-' and j + 2 < len(s)
                                      and dig(s[j + 2]))):
                j += 2
                while j < len(s) and dig(s[j]):
                    j += 1
            t = s[i:j].lower()
            if t[-1] in '.,':
                N.err('N\u00famero mal escrito: ' + s[i:j])
            out.append(('n', numq(t), i))
            i = j
        elif c in '\u00b2\u00b3':
            out.append(('o', '^', i))
            out.append(('n', (2 if c == '\u00b2' else 3, 1), i))
            i += 1
        elif c == 'r' and s[i] == '\u221a':
            out.append(('f', 'r', i))
            i += 1
        elif 'a' <= c.lower() <= 'z':
            j = i
            while j < len(s) and 'a' <= s[j].lower() <= 'z':
                j += 1
            w = s[i:j]
            if w.lower() in FUN:
                out.append(('f', FUN[w.lower()], i))
            else:
                for k in range(len(w)):
                    out.append(('v', w[k], i + k))
            i = j
        elif c in '+-*/:^':
            out.append(('o', c, i))
            i += 1
        elif c in '()':
            out.append((c, c, i))
            i += 1
        else:
            N.err('S\u00edmbolo desconhecido: ' + s[i])
    return out


class P:
    # Leitor recursivo: expr -> termo ((+|-) termo)*
    def __init__(self, s):
        self.s = s
        self.t = toks(s)
        self.i = 0
        self.prof = 0

    def ver(self):
        return self.t[self.i] if self.i < len(self.t) else (None, None, len(
            self.s))

    def tira(self):
        x = self.ver()
        self.i += 1
        return x

    def tudo(self):
        e = self.expr()
        if self.i < len(self.t):
            k = self.ver()
            N.err('N\u00e3o percebo "' + self.s[k[2]:k[2] + 8].strip() +
                  '" (falta um sinal?)')
        return e

    def termos(self):
        # Termos do 1.o nivel com o sinal e o texto: [(+1|-1, arvore, txt)].
        out = []
        sg = 1
        k = self.ver()
        if k[0] == 'o' and k[1] in '+-':
            self.tira()
            sg = -1 if k[1] == '-' else 1
        while True:
            a = self.ver()[2]
            t = self.termo()
            b = self.ver()[2]
            out.append((sg, t, self.s[a:b].strip()))
            k = self.ver()
            if k[0] == 'o' and k[1] in '+-':
                self.tira()
                sg = -1 if k[1] == '-' else 1
            else:
                break
        if self.i < len(self.t):
            self.tudo()
        return out

    def expr(self):
        self.prof += 1
        N.need(self.prof <= MAXPAR, 'Demasiados par\u00eanteses')
        e = self.termo()
        while True:
            k = self.ver()
            if k[0] == 'o' and k[1] in '+-':
                self.tira()
                e = (k[1], e, self.termo())
            else:
                break
        self.prof -= 1
        return e

    def termo(self):
        e = self.unario()
        while True:
            k = self.ver()
            if k[0] == 'o' and k[1] in '*/:':
                self.tira()
                d = self.unario()
                if k[1] == '/' and lit(e) and lit(d) and d[0] == 'n' and \
                        d[1][0]:
                    # 3/4 escrito pelo aluno e uma fracao, nao uma divisao
                    n = e[1][0] if e[0] == 'n' else -e[1][1][0]
                    e = ('n', R(n, d[1][0]))
                    continue
                k2 = self.ver()
                if k[1] != '/' and lit(d) and k2[0] == 'o' and k2[1] == '/' \
                        and self.i + 1 < len(self.t) and \
                        self.t[self.i + 1][0] == 'n' and \
                        self.t[self.i + 1][1][1] == 1 and \
                        self.t[self.i + 1][1][0]:
                    # 2 : 3/4 -> 2 : (3/4)
                    self.tira()
                    q = self.tira()[1][0]
                    n = d[1][0] if d[0] == 'n' else -d[1][1][0]
                    d = ('n', R(n, q))
                e = ('*' if k[1] == '*' else '/', e, d)
            elif k[0] in ('n', 'v', '(', 'f'):
                if k[0] == 'n' and e[0] == 'n':
                    N.err('Falta um sinal entre dois n\u00fameros')
                e = ('*', e, self.unario())
            else:
                break
        return e

    def unario(self):
        k = self.ver()
        if k[0] == 'o' and k[1] in '+-':
            self.tira()
            u = self.unario()
            return ('u', u) if k[1] == '-' else u
        return self.pot()

    def pot(self):
        b = self.atomo()
        k = self.ver()
        if k[0] == 'o' and k[1] == '^':
            self.tira()
            return ('^', b, self.unario())
        return b

    def atomo(self):
        k = self.tira()
        if k[0] == 'n':
            return ('n', k[1])
        if k[0] == 'v':
            return ('v', k[1])
        if k[0] == 'f':
            return (k[1], self.unario())
        if k[0] == '(':
            e = self.expr()
            f = self.tira()
            N.need(f[0] == ')', 'Falta fechar um par\u00eantese')
            return e
        if k[0] is None:
            N.err('A express\u00e3o acaba antes do tempo')
        N.err('N\u00e3o percebo "' + self.s[k[2]:k[2] + 6].strip() + '"')


def lit(e):
    # Inteiro escrito tal e qual (3 ou -3).
    if e[0] == 'u':
        e = e[1]
    return e[0] == 'n' and e[1][1] == 1


def arvore(s):
    return P(s).tudo()


def letras(t, out=None):
    out = [] if out is None else out
    if t[0] == 'v':
        if t[1] not in out:
            out.append(t[1])
    elif t[0] != 'n':
        for x in t[1:]:
            if isinstance(x, tuple):
                letras(x, out)
    return out

# ------------------------------------------------------------ polinomios
# Polinomio: dicionario {monomio: racional}; monomio: tuplo ordenado de
# (letra, expoente), () para o termo independente.


def mono(a, b):
    d = {}
    for v, e in a + b:
        d[v] = d.get(v, 0) + e
    return tuple(sorted([(v, d[v]) for v in d if d[v]]))


def padd(A, B, s=1):
    C = dict(A)
    for m in B:
        c = add(C.get(m, Z), B[m]) if s > 0 else sub(C.get(m, Z), B[m])
        if c[0]:
            C[m] = c
        elif m in C:
            del C[m]
    return C


def pmul(A, B):
    C = {}
    for a in A:
        for b in B:
            m = mono(a, b)
            c = add(C.get(m, Z), mul(A[a], B[b]))
            if c[0]:
                C[m] = c
            elif m in C:
                del C[m]
    return C


def pesc(A, k):
    return dict([(m, mul(A[m], k)) for m in A]) if k[0] else {}


def cte(A):
    for m in A:
        if m:
            return None
    return A.get((), Z)


def grau(A, v=None):
    g = -1
    for m in A:
        g = max(g, sum([e for x, e in m if v is None or x == v]))
    return g


def poli(t):
    k = t[0]
    if k == 'n':
        return {(): t[1]} if t[1][0] else {}
    if k == 'v':
        return {((t[1], 1),): UM}
    if k == 'u':
        return pesc(poli(t[1]), (-1, 1))
    if k == '+':
        return padd(poli(t[1]), poli(t[2]))
    if k == '-':
        return padd(poli(t[1]), poli(t[2]), -1)
    if k == '*':
        return pmul(poli(t[1]), poli(t[2]))
    if k == '/':
        d = cte(poli(t[2]))
        N.need(d is not None, 'Divis\u00e3o por uma express\u00e3o com letras: '
               'n\u00e3o \u00e9 um polin\u00f3mio')
        return pesc(poli(t[1]), div(UM, d))
    if k == '^':
        e = cte(poli(t[2]))
        N.need(e is not None and e[1] == 1, 'O expoente tem de ser um '
               'n\u00famero inteiro')
        e = e[0]
        b = poli(t[1])
        c = cte(b)
        if c is not None:
            return {(): pw(c, e)} if pw(c, e)[0] else {}
        N.need(0 <= e <= 12, 'Expoente demasiado grande ou negativo')
        r = {(): UM}
        for i in range(e):
            r = pmul(r, b)
        return r
    N.err('Ra\u00edzes n\u00e3o s\u00e3o permitidas aqui')


def ordem(A, vs=None):
    vs = vs or sorted(set([x for m in A for x, e in m]))

    def chave(m):
        d = dict(m)
        return [-sum([e for x, e in m])] + [-d.get(v, 0) for v in vs]
    ms = list(A.keys())
    ms.sort(key=chave)
    return ms


def mstr(m):
    return ''.join([v + (N.sup(e) if e > 1 else '') for v, e in m])


def pstr(A, vs=None):
    # Escrita habitual: 3x\u00b2 - (1/2)x + 4; "0" se for nulo.
    if not A:
        return '0'
    o = ''
    for m in ordem(A, vs):
        c = A[m]
        a = (abs(c[0]), c[1])
        if m:
            t = ('' if a == UM else ('(' + qs(a) + ')' if a[1] > 1 else
                                     qs(a))) + mstr(m)
        else:
            t = qs(a)
        if not o:
            o = ('-' if c[0] < 0 else '') + t
        else:
            o += (' - ' if c[0] < 0 else ' + ') + t
    return o


def coefs(A, v):
    # Polinomio numa letra -> lista de coeficientes do grau 0 ao grau n.
    g = grau(A)
    cs = [Z] * (g + 1)
    for m in A:
        N.need(not m or (len(m) == 1 and m[0][0] == v), 'O polin\u00f3mio s\u00f3 pode '
               'ter a letra ' + v)
        cs[m[0][1] if m else 0] = A[m]
    return cs


def decoefs(cs, v):
    A = {}
    for i in range(len(cs)):
        if cs[i][0]:
            A[((v, i),) if i else ()] = cs[i]
    return A


def valor(A, d):
    # Valor de um polinomio para letras com valores racionais (dict).
    r = Z
    for m in A:
        t = A[m]
        for v, e in m:
            N.need(v in d, 'Falta o valor de ' + v)
            t = mul(t, pw(d[v], e))
        r = add(r, t)
    return r


def denl(A):
    # m.m.c. dos denominadores dos coeficientes
    k = 1
    for m in A:
        k = mmc(k, A[m][1])
    return k


def raizes_rac(cs):
    # Raizes racionais de um polinomio de coeficientes inteiros (cs do grau
    # 0 ao n), pelo teste das raizes racionais.
    while cs and cs[0][0] == 0:
        cs = cs[1:]
    if len(cs) < 2:
        return []
    a0, an = abs(cs[0][0]), abs(cs[-1][0])
    N.need(a0 <= 10 ** 9 and an <= 10 ** 9, 'Coeficientes demasiado grandes')
    out = []
    ps = [p for p in range(1, int(a0 ** 0.5) + 2) if a0 % p == 0]
    ps = ps + [a0 // p for p in ps]
    qs_ = [q for q in range(1, int(an ** 0.5) + 2) if an % q == 0]
    qs_ = qs_ + [an // q for q in qs_]
    vistos = []
    for p in ps:
        for q in qs_:
            for s in (1, -1):
                r = R(s * p, q)
                if r in vistos:
                    continue
                vistos.append(r)
                if valor(decoefs(cs, 'x'), {'x': r})[0] == 0:
                    out.append(r)
    out.sort(key=lambda r: r[0] / r[1])
    return out

# ------------------------------------------------------------ intervalos
# Intervalo: (lo, lo_fechado, hi, hi_fechado); None no infinito.


def vstr(q):
    # Decimal quando e finito, senao fracao.
    d = q[1]
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    return dizima(q) if d == 1 else qs(q)


def istr(I):
    if I is None:
        return '\u2205'
    lo, lc, hi, hc = I
    if lo is not None and hi is not None and cmp(lo, hi) == 0:
        return '{' + vstr(lo) + '}'
    return ('[' if lc else ']') + ('-\u221e' if lo is None else vstr(lo)) + \
        sepr(lo, hi) + ('+\u221e' if hi is None else vstr(hi)) + (']' if hc
                                                                  else '[')


def sepr(lo, hi):
    for x in (lo, hi):
        if x is not None and ',' in vstr(x):
            return '; '
    return ', '


def cond(I):
    if I is None:
        return 'condi\u00e7\u00e3o imposs\u00edvel'
    lo, lc, hi, hc = I
    p = []
    if lo is not None:
        p.append(vstr(lo) + (' \u2264 ' if lc else ' < '))
    p.append('x')
    if hi is not None:
        p.append((' \u2264 ' if hc else ' < ') + vstr(hi))
    if lo is None and hi is None:
        return 'x \u2208 \u211d'
    if lo is not None and hi is not None and cmp(lo, hi) == 0:
        return 'x = ' + vstr(lo)
    return ''.join(p)


def inter(A, B):
    lo, lc = A[0], A[1]
    if B[0] is not None and (lo is None or cmp(B[0], lo) > 0):
        lo, lc = B[0], B[1]
    elif B[0] is not None and lo is not None and cmp(B[0], lo) == 0:
        lc = lc and B[1]
    hi, hc = A[2], A[3]
    if B[2] is not None and (hi is None or cmp(B[2], hi) < 0):
        hi, hc = B[2], B[3]
    elif B[2] is not None and hi is not None and cmp(B[2], hi) == 0:
        hc = hc and B[3]
    if lo is not None and hi is not None:
        c = cmp(lo, hi)
        if c > 0 or (c == 0 and not (lc and hc)):
            return None
    return (lo, lc, hi, hc)


def antes(A, B):
    # A comeca antes de B (ou ao mesmo tempo)
    if A[0] is None:
        return True
    if B[0] is None:
        return False
    c = cmp(A[0], B[0])
    return c < 0 or (c == 0 and A[1])


def uniao(A, B):
    if not antes(A, B):
        A, B = B, A
    # B comeca depois do fim de A?
    if A[2] is not None and B[0] is not None:
        c = cmp(B[0], A[2])
        if c > 0 or (c == 0 and not (A[3] or B[1])):
            return [A, B]
    if A[2] is None:
        return [A]
    if B[2] is None:
        return [(A[0], A[1], None, False)]
    c = cmp(B[2], A[2])
    if c > 0:
        return [(A[0], A[1], B[2], B[3])]
    if c == 0:
        return [(A[0], A[1], A[2], A[3] or B[3])]
    return [A]
