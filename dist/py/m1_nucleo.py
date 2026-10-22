# m1_nucleo.py - M1TR4M: nucleo de calculo.
# Formatacao de numeros (virgula decimal, x 10^n, casas decimais,
# algarismos significativos), leitor de numeros e de expressoes sem eval,
# fracoes e radicais exatos, unidades e conversoes, validacao.
# A formatacao e feita a mao (sem %g nem str(float)) para dar o mesmo
# resultado no Python do computador e no MicroPython.

import math
import m1_plat as P

VER = 1
LN10 = math.log(10.0)
# Definicoes usadas no calculo (a app copia-as das Definicoes do aluno):
# ang 0 graus / 1 radianos; dec casas decimais em Matematica;
# sci expoente a partir do qual se usa notacao cientifica.
CF = {'ang': 0, 'dec': 4, 'sci': 6, 'ans': None}

SUPD = "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079"
X = '\u00d7'      # sinal de multiplicar
AP = '\u2248'     # aproximadamente igual


def err(m):
    raise ValueError(m)


def ok(v):
    # Falso para infinito e NaN (teste que funciona no MicroPython).
    return v - v == 0


def chk(v):
    if not ok(v):
        err('Valor demasiado grande')
    return v

# ------------------------------------------------------------ formatar


def sup(n):
    # Inteiro -> expoente em carateres sobrescritos.
    o = []
    for ch in str(n):
        if ch == '-':
            o.append('\u207b')
        else:
            o.append(SUPD[ord(ch) - 48])
    return ''.join(o)


def _sc(a, k):
    # a * 10^k com o minimo de erro: 10^k ate 10^22 e exato em float,
    # por isso o resultado e o mesmo nos dois Pythons.
    while k > 22:
        a = a * _p10(22)
        k -= 22
    while k < -22:
        a = a / _p10(22)
        k += 22
    if k >= 0:
        return a * _p10(k)
    return a / _p10(-k)


def _p10(k):
    # 10^k exato em float para 0 <= k <= 22 (a conversao de inteiros
    # grandes para float do MicroPython pode errar no ultimo bit).
    if k <= 15:
        return float(10 ** k)
    return float(10 ** 15) * float(10 ** (k - 15))


def dig(c):
    # Digito ASCII (isdigit aceita tambem expoentes como o "2" elevado).
    return '0' <= c <= '9'


def _fl(t):
    # Texto "1.496e11", "-0,5" ou "1/3.6" -> float, igual nos dois Pythons.
    k = t.find('/')
    if k > 0:
        return _fl(t[:k]) / _fl(t[k + 1:])
    neg = t.startswith('-')
    if neg or t.startswith('+'):
        t = t[1:]
    ex = 0
    k = t.find('e')
    if k < 0:
        k = t.find('E')
    if k >= 0:
        ex = int(t[k + 1:])
        t = t[:k]
    v = _dn(t, ex)
    return -v if neg else v


def _dn(t, ex=0):
    # "12,345" -> 12.345 (x 10^ex) a partir dos digitos inteiros.
    t = t.replace('.', ',')
    k = t.find(',')
    d = 0
    if k >= 0:
        d = len(t) - k - 1
        t = t[:k] + t[k + 1:]
    if t == '':
        t = '0'
    return _sc(float(int(t)), ex - d)


def _e10(a):
    # Expoente decimal de a > 0: 10^e <= a < 10^(e+1).
    e = int(math.floor(math.log(a) / LN10))
    v = _sc(a, -e)
    if v >= 10:
        e += 1
    elif v < 1:
        e -= 1
    return e


def _rnd(v):
    # Arredonda v >= 0 a inteiro (meio para cima, com folga para o
    # erro binario: 2,675 -> 268 quando se pede 2 casas).
    return int(math.floor(v + 0.5 + v * 1e-15))


def _ds(m, d):
    # Inteiro m e d casas -> texto com virgula.
    s = str(m)
    if d <= 0:
        return s
    if len(s) <= d:
        s = '0' * (d - len(s) + 1) + s
    return s[:-d] + ',' + s[-d:]


def _strip(s):
    # Tira zeros a direita das casas decimais.
    if ',' in s:
        s = s.rstrip('0')
        if s.endswith(','):
            s = s[:-1]
    return s


def sci(m, e, n):
    # Mantissa inteira m com n algarismos e expoente e -> "m,mm x 10^e".
    s = _ds(m, n - 1)
    if e == 0:
        return s
    return s + ' ' + X + ' 10' + sup(e)


def fmt2(x, sf=0, dec=-1, strip=1):
    # Formata x. sf>0: sf algarismos significativos; senao dec casas
    # decimais (CF['dec'] se dec<0). Devolve (texto, exato).
    if isinstance(x, int) and sf <= 0:
        if abs(x) < 10 ** 12:
            return str(x), True
        x = float(x)
    x = float(x)
    if not ok(x):
        err('Valor demasiado grande')
    neg = x < 0
    a = -x if neg else x
    if a == 0:
        if sf > 0:
            return ('0,' + '0' * (sf - 1)) if sf > 1 else '0', True
        return '0', True
    e = _e10(a)
    hi = CF['sci']
    if sf > 0:
        sf = min(sf, 13)
        m, e = _sig(a, sf)
        exact = abs(_sc(float(m), e - sf + 1) - a) <= a * 1e-12
        if e >= hi or e < -3 or e >= sf:
            s = sci(m, e, sf)
        elif e == sf - 1:
            s = str(m)
        else:
            s = _ds(m, sf - 1 - e)
    else:
        if dec < 0:
            dec = CF['dec']
        if e >= 12 or e < -dec and e < -3:
            n = max(dec, 4)
            m, e = _sig(a, n)
            exact = abs(_sc(float(m), e - n + 1) - a) <= a * 1e-12
            s = _strip(_ds(m, n - 1)) if strip else _ds(m, n - 1)
            s = s + ' ' + X + ' 10' + sup(e)
        else:
            if e + dec > 12:
                dec = max(0, 12 - e)
            v = _sc(a, dec)
            m = _rnd(v)
            exact = abs(float(m) - v) <= v * 1e-12 + 1e-9
            s = _ds(m, dec)
            if strip:
                s = _strip(s)
    if neg and s.strip('0,') != '':
        s = '-' + s
    return s, exact


def _sig(a, n):
    # Arredonda a > 0 a n algarismos: devolve (m, e) com a ~ m x 10^(e-n+1).
    e = _e10(a)
    m = _rnd(_sc(a, n - 1 - e))
    if m >= 10 ** n:
        m = m // 10
        e += 1
    return m, e


def fmt(x, sf=0, dec=-1):
    return fmt2(x, sf, dec)[0]


def eq(x, sf=0, dec=-1):
    # "= 2,5" se for exato, "~ 2,47" se foi arredondado. Com dec dado
    # mantem os zeros a direita (74,10); com dec das Definicoes tira-os.
    s, e = fmt2(x, sf, dec, 0 if dec >= 0 else 1)
    return ('= ' if e else AP + ' ') + s


def fix(x, d):
    # Exatamente d casas decimais (mantem os zeros: 2,50).
    return fmt2(x, 0, d, 0)[0]


def fsf(x, n):
    # Formata com n algarismos significativos (n>=1).
    return fmt2(x, max(1, n))[0]

# ------------------------------------------------------------ ler numeros


def _clean(s):
    s = s.strip()
    for a, b in (('\u2212', '-'), (X, '*'), ('\u00b7', '*'), ('\u00f7', '/'),
                 (' ', '')):
        s = s.replace(a, b)
    return s


def num(s, allow_x=0):
    # Le um numero escrito pelo aluno. Devolve (valor, alg_sig);
    # alg_sig = 0 quando o valor e exato (fracao, pi, raiz...).
    t = _clean(s)
    if t == '':
        err('Escreve um n\u00famero, por exemplo 2,5')
    r = _simple(t)
    if r is not None:
        return r
    v = ev(comp(t, 0))
    return chk(v), 0


def _simple(t):
    # Numero simples: [sinal] digitos [,digitos] [e+-n | *10^n | x10^n].
    i = 0
    n = len(t)
    if i < n and t[i] in '+-':
        i += 1
    j = i
    seps = 0
    while j < n and (dig(t[j]) or t[j] in ',.'):
        if t[j] in ',.':
            seps += 1
        j += 1
    mant = t[i:j]
    if mant == '' or mant in ',.':
        return None
    rest = t[j:]
    ex = 0
    if rest:
        k = -1
        for p in ('*10^', 'x10^', 'X10^', '*10**'):
            if rest.startswith(p):
                k = len(p)
        if rest[0] in 'eE':
            k = 1
        if rest.startswith('*10') and len(rest) > 3 and SUPD.find(rest[3]) >= 0 \
                or rest.startswith('*10\u207b'):
            rest = '*10^' + P.vis(rest[3:], 0).lstrip('^')
            k = 4
        if k < 0:
            return None
        es = rest[k:]
        if es.startswith('(') and es.endswith(')'):
            es = es[1:-1]
        if not _isint(es):
            if es == '' or _isint(es.lstrip('+-')) or es in '+-':
                err('Falta o expoente depois de ' + rest[:k])
            return None
        ex = int(es)
    if seps > 1 or mant[-1] in ',.' or mant[0] in ',.' and len(mant) == 1:
        err('N\u00famero mal escrito: ' + t)
    if ex > 300 or ex < -300:
        err('Valor demasiado grande')
    v = _dn(mant, ex)
    if t[0] == '-':
        v = -v
    chk(v)
    return v, sfs(mant)


def _isint(s):
    if s.startswith('+') or s.startswith('-'):
        s = s[1:]
    if s == '':
        return False
    for c in s:
        if not dig(c):
            return False
    return True


def sfs(m):
    # Algarismos significativos de uma mantissa escrita ("0,0250" -> 3).
    d = m.replace('.', ',')
    has = ',' in d
    g = d.replace(',', '').lstrip('0')
    if g == '':
        k = d.find(',')
        return max(1, len(d) - k - 1) if has else 1
    return len(g)


def dps(m):
    # Casas decimais escritas ("2,50" -> 2).
    m = m.replace('.', ',')
    k = m.find(',')
    return 0 if k < 0 else len(m) - k - 1

# ------------------------------------------------------------ expressoes
# Codigos: numero (float); 1 = x; 2 = ans; operadores:
# 10 +, 11 -, 12 *, 13 /, 14 ^, 15 menos unario, 20 sin, 21 cos,
# 22 tan, 23 raiz, 24 modulo. Marcadores na pilha: 30 '(', 31 '(' de
# funcao, 32 '|'.
FN = (('sqrt', 23), ('raiz', 23), ('sin', 20), ('sen', 20), ('cos', 21),
      ('tan', 22), ('tg', 22), ('abs', 24))
PRI = {10: 1, 11: 1, 12: 2, 13: 2, 15: 3, 20: 3, 21: 3, 22: 3, 23: 3,
       24: 3, 14: 4}
OPC = {'+': 10, '-': 11, '*': 12, '/': 13, '^': 14}
MAXLEN = 200
MAXDEP = 20


def comp(s, allow_x=1):
    # Compila uma expressao para notacao polaca inversa (lista).
    s = _clean(s).replace('**', '^').replace('[', '(').replace(']', ')')
    if s == '':
        err('Express\u00e3o vazia')
    if len(s) > MAXLEN:
        err('Express\u00e3o demasiado longa (m\u00e1x. 200)')
    out = []
    st = []
    want = 1          # 1 = espera um operando
    dep = 0
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        # --- operandos
        tok = None
        if dig(ch) or ch in ',.':
            j = i
            while j < n and (dig(s[j]) or s[j] in ',.'):
                j += 1
            ex = 0
            if j < n and s[j] in 'eE' and j + 1 < n and (
                    dig(s[j + 1]) or s[j + 1] in '+-' and j + 2 < n and
                    dig(s[j + 2])):
                k = j + 1
                j += 2
                while j < n and dig(s[j]):
                    j += 1
                ex = int(s[k:j])
            t = s[i:j]
            if 'e' in t or 'E' in t:
                t = t[:max(t.find('e'), t.find('E'))]
            if t.count(',') + t.count('.') > 1 or t in ',.':
                err('N\u00famero mal escrito: ' + t)
            if ex > 300 or ex < -300:
                err('Valor demasiado grande')
            tok = _dn(t, ex)
            i = j
        elif ch == '\u03c0':
            tok = math.pi
            i += 1
        elif ch.isalpha() and ord(ch) < 128:
            low = s[i:].lower()
            hit = 0
            for nm, c in FN:
                if low.startswith(nm):
                    hit = c
                    i += len(nm)
                    break
            if hit:
                if not want:
                    _push(12, out, st)
                st.append(hit)
                if i < n and s[i] == '(':
                    st.append(31)
                    dep += 1
                    if dep > MAXDEP:
                        err('Demasiados par\u00eanteses (m\u00e1x. 20 n\u00edveis)')
                    i += 1
                want = 1
                continue
            if low.startswith('pi'):
                tok = math.pi
                i += 2
            elif low.startswith('ans'):
                tok = 2
                i += 3
            elif ch in 'xX' and allow_x:
                tok = 1
                i += 1
            else:
                err('S\u00edmbolo desconhecido: ' + ch)
        elif ch == '\u221a':
            if not want:
                _push(12, out, st)
            st.append(23)
            i += 1
            if i < n and s[i] == '(':
                st.append(31)
                dep += 1
                i += 1
            want = 1
            continue
        if tok is not None:
            if not want:
                _push(12, out, st)
            if isinstance(tok, int) and tok == 2 and CF['ans'] is None:
                err('Ainda n\u00e3o h\u00e1 resultado anterior (ans)')
            out.append(tok)
            want = 0
            continue
        # --- parenteses e modulo
        if ch == '(':
            if not want:
                _push(12, out, st)
            st.append(30)
            dep += 1
            if dep > MAXDEP:
                err('Demasiados par\u00eanteses (m\u00e1x. 20 n\u00edveis)')
            want = 1
            i += 1
            continue
        if ch == ')':
            if want:
                err('Falta um valor antes de )')
            while st and st[-1] not in (30, 31, 32):
                out.append(st.pop())
            if not st or st[-1] == 32:
                err('Par\u00eantese a mais')
            m = st.pop()
            dep -= 1
            if m == 31:
                out.append(st.pop())
            i += 1
            continue
        if ch == '|':
            if not want and 32 in st:
                while st[-1] != 32:
                    if st[-1] in (30, 31):
                        err('Falta fechar um par\u00eantese')
                    out.append(st.pop())
                st.pop()
                dep -= 1
                out.append(24)
                i += 1
                continue
            if not want:
                _push(12, out, st)
            st.append(32)
            dep += 1
            if dep > MAXDEP:
                err('Demasiados par\u00eanteses (m\u00e1x. 20 n\u00edveis)')
            want = 1
            i += 1
            continue
        # --- expoentes sobrescritos (x\u00b2)
        k = SUPD.find(ch)
        if k >= 0 or ch == '\u207b':
            if want:
                err('Falta a base antes do expoente')
            j = i
            while j < n and (SUPD.find(s[j]) >= 0 or s[j] == '\u207b'):
                j += 1
            e = P.vis(s[i:j], 0).lstrip('^')
            _push(14, out, st)
            if e.startswith('-'):
                out.append(-float(int(e[1:])))
            else:
                out.append(float(int(e)))
            want = 0
            i = j
            continue
        # --- operadores
        if ch in OPC:
            o = OPC[ch]
            if want:
                if ch == '-':
                    st.append(15)
                    i += 1
                    continue
                if ch == '+':
                    i += 1
                    continue
                err('Falta um n\u00famero antes de ' + ch)
            _push(o, out, st)
            want = 1
            i += 1
            continue
        err('S\u00edmbolo desconhecido: ' + ch)
    if want:
        if out or st:
            err('Falta um n\u00famero no fim')
        err('Express\u00e3o vazia')
    while st:
        o = st.pop()
        if o in (30, 31):
            err('Falta fechar um par\u00eantese')
        if o == 32:
            err('Falta fechar o m\u00f3dulo |')
        out.append(o)
    return out


def _push(o, out, st):
    # Tira da pilha os operadores com prioridade maior ou igual.
    p = PRI[o]
    while st:
        t = st[-1]
        if t >= 30:
            break
        q = PRI[t]
        if q > p or (q == p and o != 14 and t < 15):
            out.append(st.pop())
        else:
            break
    st.append(o)


def ev(code, x=0.0):
    # Calcula o valor da expressao compilada para um valor de x.
    st = []
    for c in code:
        if isinstance(c, float):
            st.append(c)
        elif c == 1:
            st.append(x)
        elif c == 2:
            st.append(CF['ans'])
        elif c < 15:
            b = st.pop()
            a = st.pop()
            if c == 10:
                a = a + b
            elif c == 11:
                a = a - b
            elif c == 12:
                a = a * b
            elif c == 13:
                if b == 0:
                    raise ZeroDivisionError('Divis\u00e3o por zero')
                a = a / b
            else:
                a = _pow(a, b)
            st.append(a)
        else:
            a = st.pop()
            if c == 15:
                a = -a
            elif c == 23:
                if a < 0:
                    err('Raiz de um n\u00famero negativo')
                a = math.sqrt(a)
            elif c == 24:
                a = abs(a)
            else:
                r = a * math.pi / 180 if CF['ang'] == 0 else a
                if c == 20:
                    a = math.sin(r)
                elif c == 21:
                    a = math.cos(r)
                else:
                    if abs(math.cos(r)) < 1e-12:
                        err('Tangente n\u00e3o definida')
                    a = math.tan(r)
            st.append(a)
    v = st[0]
    if not ok(v):
        err('Valor demasiado grande')
    return v


def _pow(a, b):
    if a == 0 and b < 0:
        raise ZeroDivisionError('Divis\u00e3o por zero')
    if a < 0 and b != int(b):
        f = frac(b, 99)
        if f is not None and f[1] % 2 == 1:
            r = (-a) ** (1.0 * f[0] / f[1])
            return -r if f[0] % 2 else r
        err('Pot\u00eancia de base negativa sem valor real')
    try:
        r = a ** b
    except OverflowError:
        err('Valor demasiado grande')
    if isinstance(r, complex) or not ok(r):
        err('Valor demasiado grande')
    return r


def val(s, x=0.0):
    return ev(comp(s), x)


def has_x(code):
    return 1 in code

# ------------------------------------------------------------ exatos


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def frac(x, maxd=1000):
    # x -> (n, d) se x for (quase) exatamente n/d com d <= maxd.
    if not ok(x):
        return None
    neg = x < 0
    a = -x if neg else x
    if a > 1e9:
        return None
    h0, h1 = 0, 1
    k0, k1 = 1, 0
    v = a
    for i in range(20):
        q = int(math.floor(v))
        h0, h1 = h1, q * h1 + h0
        k0, k1 = k1, q * k1 + k0
        if k1 > maxd:
            return None
        if abs(a - 1.0 * h1 / k1) <= 1e-12 * max(1.0, a):
            return (-h1 if neg else h1, k1)
        r = v - q
        if r < 1e-12:
            return None
        v = 1.0 / r
    return None


def rad(n):
    # sqrt(n) = k*sqrt(m), m sem fatores quadrados. n inteiro >= 0.
    k = 1
    m = n
    f = 2
    while f * f <= m:
        while m % (f * f) == 0:
            m //= f * f
            k *= f
        f += 1
    return k, m


def fstr(n, d):
    # Fracao (n, d) -> "n/d" simplificada.
    g = gcd(n, d) or 1
    n //= g
    d //= g
    if d < 0:
        n, d = -n, -d
    if d == 1:
        return str(n)
    return str(n) + '/' + str(d)


def rstr(k, m, d=1):
    # k*sqrt(m)/d simplificado -> texto ("2\u221a3", "\u221a5/2").
    if m == 0 or k == 0:
        return '0'
    if m == 1:
        return fstr(k, d)
    g = gcd(k, d) or 1
    k //= g
    d //= g
    if d < 0:
        k, d = -k, -d
    s = '' if k == 1 else ('-' if k == -1 else str(k))
    s = s + '\u221a' + str(m)
    if d != 1:
        s = s + '/' + str(d)
    return s


def exact(x):
    # Forma exata de x quando e reconhecivel: inteiro, fracao, k*raiz(m)/d
    # ou k*pi/d. Senao None.
    if not ok(x):
        return None
    f = frac(x)
    if f is not None:
        return fstr(f[0], f[1])
    f = frac(x * x, 1000)
    if f is not None and f[0] > 0:
        k, m = rad(f[0] * f[1])
        if m > 1 and m < 10000:
            return rstr(-k if x < 0 else k, m, f[1])
    f = frac(x / math.pi, 100)
    if f is not None:
        s = fstr(f[0], f[1])
        if '/' in s:
            a, b = s.split('/')
            return ('' if a == '1' else ('-' if a == '-1' else a)) + \
                '\u03c0/' + b
        return ('' if s == '1' else ('-' if s == '-1' else s)) + '\u03c0'
    return None


def rhs(x, dec=-1):
    # Lado direito para Matematica: "= 2,5", "= 1/3 ~ 0,3333",
    # "= raiz(2) ~ 1,4142" ou "~ 1,2346" (forma exata quando existe).
    s, ex = fmt2(x, 0, dec)
    if ex:
        return '= ' + s
    e = exact(x)
    if e is not None and e != s:
        return '= ' + e + ' ' + AP + ' ' + s
    return AP + ' ' + s

# ------------------------------------------------------------ unidades
# "simbolo:categoria:fator para a unidade base[:somar]".
# Categorias: L comprimento (m), M massa (kg), t tempo (s), V volume (m3),
# A area (m2), T temperatura (K), E energia (J), W potencia (W),
# p pressao (Pa), n quantidade (mol), c concentracao (mol/m3),
# m concentracao massica (kg/m3), v velocidade (m/s), d massa volumica
# (kg/m3), F forca (N), I corrente (A), U tensao (V), R resistencia,
# f frequencia (Hz), Q carga (C).
UT = ("m:L:1 km:L:1e3 hm:L:100 dam:L:10 dm:L:0.1 cm:L:0.01 mm:L:1e-3 "
      "\u00b5m:L:1e-6 nm:L:1e-9 pm:L:1e-12 UA:L:1.496e11 a.l.:L:9.461e15 "
      "kg:M:1 t:M:1e3 g:M:1e-3 mg:M:1e-6 \u00b5g:M:1e-9 u:M:1.66054e-27 "
      "s:t:1 ms:t:1e-3 \u00b5s:t:1e-6 ns:t:1e-9 min:t:60 h:t:3600 d:t:86400 "
      "ano:t:3.15576e7 "
      "m\u00b3:V:1 dm\u00b3:V:1e-3 L:V:1e-3 cm\u00b3:V:1e-6 mL:V:1e-6 "
      "dL:V:1e-4 cL:V:1e-5 mm\u00b3:V:1e-9 hL:V:0.1 "
      "m\u00b2:A:1 cm\u00b2:A:1e-4 mm\u00b2:A:1e-6 dm\u00b2:A:0.01 km\u00b2:A:1e6 ha:A:1e4 "
      "K:T:1:0 \u00b0C:T:1:273.15 "
      "J:E:1 kJ:E:1e3 MJ:E:1e6 Wh:E:3600 kWh:E:3.6e6 eV:E:1.602176634e-19 "
      "cal:E:4.184 kcal:E:4184 "
      "W:W:1 mW:W:1e-3 kW:W:1e3 MW:W:1e6 GW:W:1e9 "
      "Pa:p:1 hPa:p:100 kPa:p:1e3 MPa:p:1e6 bar:p:1e5 atm:p:101325 mmHg:p:133.322 "
      "mol:n:1 mmol:n:1e-3 \u00b5mol:n:1e-6 kmol:n:1e3 "
      "mol/dm\u00b3:c:1e3 mol/L:c:1e3 mmol/L:c:1 mol/m\u00b3:c:1 "
      "g/dm\u00b3:m:1 g/L:m:1 mg/L:m:1e-3 kg/m\u00b3:m:1 g/cm\u00b3:d:1e3 "
      "g/mL:d:1e3 kg/m\u00b3:d:1 kg/L:d:1e3 g/L:d:1 "
      "m/s:v:1 km/h:v:1/3.6 cm/s:v:0.01 "
      "N:F:1 kN:F:1e3 mN:F:1e-3 "
      "A:I:1 mA:I:1e-3 \u00b5A:I:1e-6 kA:I:1e3 "
      "V:U:1 mV:U:1e-3 kV:U:1e3 "
      "\u03a9:R:1 k\u03a9:R:1e3 M\u03a9:R:1e6 m\u03a9:R:1e-3 "
      "Hz:f:1 kHz:f:1e3 MHz:f:1e6 GHz:f:1e9 THz:f:1e12 PHz:f:1e15 "
      "C:Q:1 mC:Q:1e-3 \u00b5C:Q:1e-6 mAh:Q:3.6 Ah:Q:3600")
_UD = None


def _units():
    global _UD
    if _UD is None:
        _UD = {}
        for it in UT.split(' '):
            p = it.split(':')
            if len(p) >= 3:
                k = p[0] + ':' + p[1]
                _UD[k] = (_fl(p[2]), _fl(p[3]) if len(p) > 3 else 0.0)
                if p[0] not in _UD:
                    _UD[p[0]] = p[1]
    return _UD


def ucat(u):
    # Categoria de uma unidade ('' se nao existe).
    r = _units().get(u)
    return r if isinstance(r, str) else ''


def ulist(cat):
    # Unidades de uma categoria, pela ordem da tabela.
    o = []
    for it in UT.split(' '):
        p = it.split(':')
        if len(p) >= 3 and p[1] == cat:
            o.append(p[0])
    return o


def tobase(v, u, cat=''):
    # Valor na unidade u -> valor na unidade base da categoria.
    d = _units()
    if not cat:
        cat = ucat(u)
    f = d.get(u + ':' + cat)
    if f is None:
        err('Unidade desconhecida: ' + u)
    return v * f[0] + f[1]


def frombase(v, u, cat=''):
    d = _units()
    if not cat:
        cat = ucat(u)
    f = d.get(u + ':' + cat)
    if f is None:
        err('Unidade desconhecida: ' + u)
    return (v - f[1]) / f[0]


def conv(v, u1, u2, cat=''):
    if not cat:
        cat = ucat(u1)
    if cat != ucat(u2) and not (u2 + ':' + cat) in _units():
        err('Unidades de grandezas diferentes: ' + u1 + ' e ' + u2)
    return frombase(tobase(v, u1, cat), u2, cat)

# ------------------------------------------------------------ exercicios


def check(ans, sol, mode='r', tol=0.001):
    # Resposta numerica certa? ans: texto do aluno (ou numero); sol: valor
    # certo. mode: 'r' tolerancia relativa tol; 'dN' arredondado a N casas;
    # 'sN' com N algarismos significativos. Aceita 0,5, 1/2, 5e-1, 5x10^-1.
    v = num(ans)[0] if isinstance(ans, str) else ans
    if mode[0] == 'd':
        n = int(mode[1:])
        return fmt2(v, 0, n, 0)[0] == fmt2(sol, 0, n, 0)[0]
    if mode[0] == 's':
        n = int(mode[1:])
        return fsf(v, n) == fsf(sol, n)
    if sol == 0:
        return abs(v) <= tol
    return abs(v - sol) <= tol * abs(sol)

# ------------------------------------------------------------ calculadoras


def fld(lab, u, t, k='n', o=None):
    # Campo de formulario: rotulo, unidades ("g kg mg"), texto inicial,
    # tipo ('n' numero, 't' texto, 'l' lista, 'c' escolha), opcoes.
    return [lab, u.split(' ') if u else None, t, 0, k, '', o]


def sfm(*vs):
    # Algarismos significativos do resultado (regra do produto): o menor
    # dos dados; 0 se as definicoes os desligam ou se os dados sao exatos.
    if not CF.get('sfa', 1):
        return 0
    m = 0
    for v in vs:
        if v and (m == 0 or v < m):
            m = v
    return m


def sfv(*xs):
    # Como sfm, mas recebe dados (valor, alg. sig.): ignora os vazios e
    # os zeros ("parte do repouso" nao limita o resultado).
    return sfm(*[x[1] for x in xs if x is not None and x[0] != 0])


def res(sym, x, u='', sf=0, dec=-1):
    # Linha de resultado: "> m = 2,5 g" ou "> m ~ 2,47 g".
    s = eq(x, sf, dec)
    return '> ' + sym + ' ' + s + (' ' + u if u else '')


def q(x, sf=0, u=''):
    # Valor formatado com unidade (para a substituicao).
    return fmt(x, sf) + (' ' + u if u else '')

def lst(t):
    # Partes de uma lista escrita pelo aluno: separador ";" (ou espacos,
    # quando nenhum valor usa notacao cientifica com espacos).
    ps = []
    for p in t.replace('\n', ';').split(';'):
        p = p.strip()
        if not p:
            continue
        if ' ' in p and not (X in p or '*' in p or 'x' in p.lower()):
            ps = ps + [x for x in p.split(' ') if x]
        else:
            ps.append(p)
    return ps


def rdf(fs):
    # Le os campos do formulario. Numeros vem na 1.a unidade da lista
    # (a da formula), como (valor, alg. sig.); 'o' e um numero opcional
    # (None se vazio); 'u' da (valor, alg. sig., indice da unidade) sem
    # converter. Os erros ficam escritos no proprio campo.
    out = []
    bad = 0
    for f in fs:
        f[5] = ''
        try:
            k = f[4]
            if k == 'o' and f[2].strip() == '':
                out.append(None)
            elif k == 'n' or k == 'o':
                v, sf = num(f[2])
                if f[1] and f[3]:
                    v = conv(v, f[1][f[3]], f[1][0])
                out.append((v, sf))
            elif k == 'u':
                # numero com unidade livre (a calculadora interpreta-a)
                v, sf = num(f[2])
                out.append((v, sf, f[3]))
            elif k == 'l':
                vs = [num(x) for x in lst(f[2])]
                if not vs:
                    err('Escreve os valores separados por ; (2,5; 3,1)')
                out.append(vs)
            elif k == 'c':
                out.append(f[3])
            else:
                out.append(f[2].strip())
        except Exception as e:
            f[5] = str(e)
            bad = 1
    return None if bad else out


# ------------------------------------------------------------ validacao


def need(c, m):
    if not c:
        err(m)


def pos(v, nome):
    need(v > 0, nome + ' tem de ser positivo; escreve, por exemplo, 2,5')
    return v


def nneg(v, nome):
    need(v >= 0, nome + ' n\u00e3o pode ser negativo')
    return v


def low(s):
    # Texto sem acentos e em minusculas (para pesquisar).
    return P.vis(s, 0).lower()
