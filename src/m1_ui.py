# m1_ui.py - M1TR4M: componentes de ecra.
# Menu numerado, texto paginado, licao (paginas A a J), editor de linha,
# formulario com varios campos, resultado, grafico simples e confirmacao.
# Todos os ecras tem titulo fixo em cima e um rodape que diz o que fazem
# enter e esc. Cada ecra e desenhado no buffer e mostrado de uma vez.

import m1_plat as P
import m1_nucleo as N

VER = 1
E = P.E
# Marcadores no inicio de uma linha de texto -> cor.
MK = {'= ': 3, '> ': 4, '! ': 5, '+ ': 6, '# ': 2}
OPS = ('=', '+', '-', '\u2212', '\u00d7', '/', '\u00f7', '\u00b7', '\u2248',
       '<', '>', '\u2264', '\u2265', '\u21d4', '\u2192')
OKS = '\u2713 '      # simbolo de certo
ERS = '\u2717 '      # simbolo de errado
_WC = [None, None]   # cache da ultima pagina partida em linhas
_H = ['']            # dica pendente para o proximo rodape


def cols():
    return E['cols']


def body():
    # Numero de linhas de conteudo (sem titulo nem rodape).
    return E['rows'] - 2


def clip(s, n):
    if len(s) <= n:
        return s
    return s[:max(0, n - 1)] + '\u2026'


def title(t, right=''):
    P.rect(0, 0, E['W'], E['lh'], 2)
    w = cols() - len(right) - 1
    P.put(0, 0, clip(t, w), 10)
    if right:
        P.put(cols() - len(right), 0, right, 10)


def foot(t):
    if _H[0]:
        t = _H[0]
        _H[0] = ''
    y = (E['rows'] - 1) * E['lh']
    P.rect(0, y, E['W'], E['H'] - y, 9)
    P.put(0, E['rows'] - 1, clip(t, cols()), 7)

# ------------------------------------------------------------ partir texto


def wrap(s, w=0, key=None):
    # Parte o texto em linhas (estilo, texto) entre palavras. Linhas com
    # "- " ficam com recuo; formulas ("= ") partem-se antes de um operador.
    if w <= 0:
        w = cols()
    if key is not None and _WC[0] == (key, w):
        return _WC[1]
    out = []
    for para in s.split('\n'):
        st = MK.get(para[:2], 0)
        if st:
            para = para[2:]
        ind = '  ' if para[:2] in ('- ', '  ') else ''
        cur = []
        pre = ''
        for wd in para.split(' '):
            while cur and len(pre) + len(' '.join(cur)) + 1 + len(wd) > w:
                k = len(cur)
                if st == 3:
                    j = k - 1
                    while j > 0 and cur[j] not in OPS:
                        j -= 1
                    if j > 0:
                        k = j
                out.append((st, pre + ' '.join(cur[:k])))
                cur = cur[k:]
                pre = ind
            cur.append(wd)
            t = pre + ' '.join(cur)
            if len(t) > w:
                while len(t) > w:
                    out.append((st, t[:w]))
                    t = ind + t[w:]
                pre = ind
                cur = [t[len(ind):]]
        out.append((st, pre + ' '.join(cur)))
    if key is not None:
        _WC[0] = (key, w)
        _WC[1] = out
    return out


def lines(lst, top=0, row=1, n=0):
    # Desenha linhas (estilo, texto) a partir da linha "row" do ecra.
    if n <= 0:
        n = body()
    for i in range(n):
        k = top + i
        if k >= len(lst):
            break
        st, t = lst[k]
        P.put(0, row + i, t, st)


def bar(top, n, total, row=1):
    # Barra de deslocamento a direita.
    if total <= n or not E['g']:
        return
    x = E['W'] - 4
    y0 = row * E['lh']
    h = n * E['lh']
    P.rect(x, y0, 3, h, 9)
    th = max(6, h * n // total)
    ty = y0 + (h - th) * top // max(1, total - n)
    P.rect(x, ty, 3, th, 7)


def hint(t):
    # Dica no proximo rodape (teclas sem funcao sao ignoradas).
    _H[0] = t

# ------------------------------------------------------------ menu


def menu(t, items, sel=0, ft='', right=''):
    # Menu numerado. Devolve o indice escolhido ou -1 (esc ou 0).
    n = len(items)
    h = body()
    top = 0
    pend = -1
    if not ft:
        ft = 'n\u00famero ou enter: abrir \u00b7 esc: voltar'
    while True:
        if sel < top:
            top = sel
        if sel >= top + h:
            top = sel - h + 1
        P.begin()
        title(t, right)
        w = cols() - 4
        for i in range(min(h, n - top)):
            k = top + i
            y = (1 + i) * E['lh']
            lab = str(k + 1)
            if len(lab) < 2:
                lab = ' ' + lab
            if k == sel:
                P.rect(0, y, E['W'] - 5, E['lh'], 8)
                if not E['g']:
                    lab = '>' + lab[1:]
            P.put(0, 1 + i, lab, 2)
            P.put(3, 1 + i, clip(items[k], w), 0)
        bar(top, h, n)
        foot(ft if pend < 0 else str(pend) + '_ \u00b7 enter: op\u00e7\u00e3o ' +
             str(pend))
        P.show()
        k = P.key()
        if k == 'up':
            sel = (sel - 1) % n
            pend = -1
        elif k == 'down':
            sel = (sel + 1) % n
            pend = -1
        elif k == 'enter':
            return sel
        elif k == 'esc':
            return -1
        elif k == 'left':
            sel = max(0, sel - h)
        elif k == 'right':
            sel = min(n - 1, sel + h)
        elif len(k) == 1 and '0' <= k <= '9':
            d = ord(k) - 48
            if pend >= 0:
                v = pend * 10 + d
                pend = -1
                if 1 <= v <= n:
                    return v - 1
                continue
            if d == 0:
                return -1
            if d * 10 <= n:
                pend = d
                sel = d - 1
                continue
            if d <= n:
                return d - 1
        elif k:
            hint('Tecla sem fun\u00e7\u00e3o: usa os n\u00fameros e as setas')

# ------------------------------------------------------------ texto


def pager(t, ls, top=0, ft='', right='', keys=()):
    # Texto paginado. ls: lista (estilo, texto). Devolve (tecla, topo).
    # "keys": teclas que terminam logo o ecra (por exemplo setas na licao).
    h = body()
    n = len(ls)
    while True:
        top = max(0, min(top, max(0, n - h)))
        P.begin()
        title(t, right)
        lines(ls, top)
        bar(top, h, n)
        a = top + 1
        b = min(n, top + h)
        f = str(a) + '-' + str(b) + ' de ' + str(n)
        if b < n:
            f = f + ' \u00b7 enter: mais'
        if ft:
            f = ft + ' \u00b7 ' + f + ' \u00b7 esc'
        else:
            f = f + ' \u00b7 esc: voltar'
        foot(f)
        P.show()
        k = P.key()
        if k in keys:
            return k, top
        if k == 'down':
            top += 1
        elif k == 'up':
            top -= 1
        elif k == 'right':
            top += h
        elif k == 'left':
            top -= h
        elif k == 'enter':
            if top + h < n:
                top += h
            else:
                return k, top
        elif k == 'esc':
            return k, top
        elif k:
            hint('Tecla sem fun\u00e7\u00e3o: setas para ler, esc para voltar')


def text(t, s, ft='', right='', keys=()):
    return pager(t, wrap(s), 0, ft, right, keys)[0]


def msg(t, s, st=0):
    # Mensagem curta; qualquer tecla continua.
    ls = wrap(s)
    if st:
        ls = [(st, x[1]) for x in ls]
    P.begin()
    title(t)
    lines(ls)
    foot('qualquer tecla: continuar')
    P.show()
    return P.key()


def busy(s='A calcular\u2026'):
    # Aviso para operacoes que demoram mais de 2 s.
    y = (E['rows'] // 2) * E['lh']
    P.rect(20, y - 4, E['W'] - 40, E['lh'] + 8, 8)
    P.put(4, E['rows'] // 2, s, 2)
    P.show()


def ask(t, q, yes=0):
    # Confirmacao sim/nao. yes=1 deixa "Sim" selecionado.
    r = menu(t, ['Sim', 'N\u00e3o'], 0 if yes else 1,
             '1: sim \u00b7 2: n\u00e3o \u00b7 esc: n\u00e3o', '')
    return r == 0

# ------------------------------------------------------------ licao
PAGS = 'ABCDEFGHIJ'
PNOME = ('O que vais aprender', 'Intui\u00e7\u00e3o', 'Defini\u00e7\u00e3o formal',
         'Explica\u00e7\u00e3o detalhada', 'F\u00f3rmulas', 'Exemplo resolvido',
         'Interpreta\u00e7\u00e3o', 'Erros frequentes', 'Resumo',
         'Exerc\u00edcio de verifica\u00e7\u00e3o')


def lesson(t, pages, pg=0, top=0, ans='', lid='', extra=()):
    # pages: lista de textos (um por pagina, '' se a pagina nao existe).
    # Devolve (tecla, pagina, topo): tecla 'esc', 'fim' ou uma das extra.
    avail = [i for i in range(len(pages)) if pages[i]]
    if not avail:
        return 'esc', pg, 0
    if pg not in avail:
        pg = avail[0]
    while True:
        ls = wrap('# ' + PAGS[pg] + '. ' + PNOME[pg]) + \
            wrap(pages[pg], 0, (lid, pg))
        fx = '\u25c2\u25b8 p\u00e1gina'
        if pg == 9 and ans:
            fx = 'r: resposta \u00b7 ' + fx
        i = avail.index(pg)
        k, top = pager(t, ls, top, fx, PAGS[pg] + ' ' + str(i + 1) + '/' +
                       str(len(avail)), ('left', 'right', 'r') + extra)
        if k == 'esc' or k in extra:
            return k, pg, top
        if k == 'r':
            if pg == 9 and ans:
                text('Resposta', ans)
            continue
        if k == 'right' or k == 'enter':
            if i + 1 < len(avail):
                pg = avail[i + 1]
                top = 0
            elif k == 'enter':
                if pg == 9 and ans:
                    text('Resposta', ans)
                return 'fim', pg, 0
        elif k == 'left' and i > 0:
            pg = avail[i - 1]
            top = 0


# ------------------------------------------------------------ editor


def _ins(k, sh, caps):
    # Texto a inserir para a tecla k (None se nao e uma tecla de escrita).
    if k in ('^2', '\u00b2'):
        return '^2'
    if k in ('\u221a', '\u03c0'):
        return k
    if k in ('sin', 'cos', 'tan', 'sin(', 'cos(', 'tan('):
        return k.rstrip('(') + '('
    if k == 'ans':
        return 'ans'
    if len(k) == 1 and (k >= ' ' or k == '\t'):
        if 'a' <= k <= 'z' and (sh or caps):
            return k.upper()
        return k
    return None


def _box(row, s, cur, w, foc):
    # Caixa de texto numa linha com cursor e deslocamento horizontal.
    off = 0
    if cur > w - 1:
        off = cur - w + 1
    vis = s[off:off + w]
    y = row * E['lh']
    x0 = E['mx'] + 2 * E['cw']
    if foc:
        P.rect(x0 - 2, y, w * E['cw'] + 4, E['lh'], 8)
    P.put(2, row, vis, 0)
    if foc:
        cx = x0 + (cur - off) * E['cw']
        if E['g']:
            P.rect(cx, y + 2, 1, E['lh'] - 4, 0)
        else:
            P.put(2 + cur - off, row, '_' if cur >= len(s) else s[cur], 0)


def edit(t, lab, s='', hint_='', err=''):
    # Editor de uma linha. Devolve o texto ou None (esc).
    cur = len(s)
    sh = 0
    caps = 0
    while True:
        P.begin()
        title(t)
        r = 1
        for st, x in wrap(lab):
            P.put(0, r, x, st)
            r += 1
        _box(r, s, cur, cols() - 4, 1)
        r += 1
        if err:
            for st, x in wrap('! ' + ERS + err):
                P.put(0, r, x, 5)
                r += 1
        for st, x in wrap(hint_):
            if r < body():
                P.put(0, r, x, 7)
                r += 1
        m = ' \u00b7 MAI' if caps else (' \u00b7 mai' if sh else '')
        foot('enter: ok \u00b7 esc: cancelar \u00b7 del: apaga' + m)
        P.show()
        k = P.key()
        if k == 'enter':
            return s
        if k == 'esc':
            return None
        if k == 'left':
            cur = max(0, cur - 1)
        elif k == 'right':
            cur = min(len(s), cur + 1)
        elif k == 'del':
            if cur > 0:
                s = s[:cur - 1] + s[cur:]
                cur -= 1
        elif k == 'clear':
            s = ''
            cur = 0
        elif k == 'shift':
            sh = 1 - sh
            continue
        elif k == 'tab':
            caps = 1 - caps
            continue
        elif k in ('up', 'down'):
            continue
        else:
            a = _ins(k, sh, caps)
            if a is None:
                continue
            if len(s) + len(a) > 200:
                err = 'Texto demasiado longo (m\u00e1x. 200)'
                continue
            s = s[:cur] + a + s[cur:]
            cur += len(a)
            err = ''
        sh = 0

# ------------------------------------------------------------ formulario
# Campo: [rotulo, unidades (lista ou None), texto, unidade escolhida,
#         tipo ('n' numero, 't' texto, 'l' lista, 'c' escolha), erro,
#         opcoes (tipo 'c')]


def form(t, fs, foc=0, ft=''):
    # Formulario com varios campos. Devolve True (enter no ultimo campo)
    # ou False (esc). Os valores ficam em fs[i][2] e fs[i][3].
    stops = []
    for i in range(len(fs)):
        stops.append((i, 0))
        if fs[i][1] and len(fs[i][1]) > 1 and fs[i][4] != 'c':
            stops.append((i, 1))
    si = 0
    for j in range(len(stops)):
        if stops[j] == (foc, 0):
            si = j
    cur = len(fs[stops[si][0]][2])
    sh = 0
    caps = 0
    top = 0
    w = cols() - 4
    while True:
        fi, part = stops[si]
        f = fs[fi]
        # linhas de cada campo
        rows_ = []
        for i in range(len(fs)):
            g = fs[i]
            u = g[1][g[3]] if g[1] and g[4] != 'c' else ''
            lab = g[0]
            if u:
                us = (' \u25c2' + u + '\u25b8') if len(g[1]) > 1 else ' ' + u
                lab = clip(lab, cols() - len(us) - 1) + us
            rows_.append((i, 'L', lab))
            rows_.append((i, 'V', g[2]))
            if g[5]:
                for st, x in wrap(ERS + g[5], cols() - 2):
                    rows_.append((i, 'E', x))
        # janela visivel
        h = body()
        fr = 0
        for j in range(len(rows_)):
            if rows_[j][0] == fi and rows_[j][1] == 'V':
                fr = j
        if fr < top + 1:
            top = max(0, fr - 1)
        if fr >= top + h:
            top = fr - h + 1
        P.begin()
        title(t, str(fi + 1) + '/' + str(len(fs)))
        for r in range(h):
            j = top + r
            if j >= len(rows_):
                break
            i, kind, s = rows_[j]
            g = fs[i]
            row = 1 + r
            if kind == 'L':
                if i == fi and part == 1:
                    P.rect(0, row * E['lh'], E['W'], E['lh'], 8)
                P.put(0, row, s, 2 if i == fi else 0)
            elif kind == 'V':
                if g[4] == 'c':
                    s = '\u25c2 ' + g[6][g[3]] + ' \u25b8'
                    if i == fi:
                        P.rect(E['mx'] + 2 * E['cw'] - 2, row * E['lh'],
                               len(s) * E['cw'] + 4, E['lh'], 8)
                    P.put(2, row, s, 0)
                else:
                    _box(row, s, cur if i == fi else len(s), w,
                         i == fi and part == 0)
            else:
                P.put(1, row, s, 5)
        bar(top, h, len(rows_))
        if part == 1:
            fx = '\u25c2\u25b8 unidade'
        elif f[4] == 'c':
            fx = '\u25c2\u25b8 op\u00e7\u00e3o'
        else:
            fx = '\u25c2\u25b8 cursor'
        fx = fx + (' \u00b7 enter: calcular' if fi == len(fs) - 1 else
                   ' \u00b7 enter: seguinte')
        if caps:
            fx = fx + ' \u00b7 MAI'
        foot((ft + ' \u00b7 ' if ft else '') + fx + ' \u00b7 esc')
        P.show()
        k = P.key()
        if k == 'esc':
            return False
        if k == 'enter':
            if fi == len(fs) - 1:
                return True
            si = stops.index((fi + 1, 0))
            cur = len(fs[fi + 1][2])
            continue
        if k == 'up' or k == 'down':
            si = (si + (1 if k == 'down' else -1)) % len(stops)
            cur = len(fs[stops[si][0]][2])
            continue
        if f[4] == 'c' or part == 1:
            if k in ('left', 'right'):
                opts = f[6] if f[4] == 'c' else f[1]
                f[3] = (f[3] + (1 if k == 'right' else -1)) % len(opts)
                continue
            if f[4] == 'c':
                continue
            si = stops.index((fi, 0))
            part = 0
            cur = len(f[2])
        s = f[2]
        if k == 'left':
            cur = max(0, cur - 1)
        elif k == 'right':
            cur = min(len(s), cur + 1)
        elif k == 'del':
            if cur > 0:
                f[2] = s[:cur - 1] + s[cur:]
                cur -= 1
        elif k == 'clear':
            f[2] = ''
            cur = 0
        elif k == 'shift':
            sh = 1 - sh
            continue
        elif k == 'tab':
            caps = 1 - caps
            continue
        else:
            a = _ins(k, sh, caps)
            if a is not None and len(s) + len(a) <= 200:
                f[2] = s[:cur] + a + s[cur:]
                cur += len(a)
                f[5] = ''
        sh = 0

# ------------------------------------------------------------ grafico


def nice(a, b, n=5):
    # Passo "redondo" para as marcas dos eixos.
    d = (b - a) / max(1, n)
    if d <= 0:
        return 1.0
    e = N._e10(d)
    m = d / N._sc(1.0, e)
    for c in (1, 2, 5, 10):
        if m <= c:
            return c * N._sc(1.0, e)
    return 10 * N._sc(1.0, e)


def graph(t, items, x0, x1, y0, y1, leg=''):
    # items: lista de ('f', funcao(x), cor) ou ('p', [(x, y)...], cor)
    # ou ('s', [(x1, y1, x2, y2)...], cor). Setas deslocam, + e - mudam
    # a escala, esc volta.
    if not E['g']:
        out = []
        for it in items:
            if it[0] == 'f':
                for i in range(5):
                    x = x0 + (x1 - x0) * i / 4
                    try:
                        out.append('x = ' + N.fmt(x) + ' \u2192 y = ' +
                                   N.fmt(it[1](x)))
                    except Exception:
                        out.append('x = ' + N.fmt(x) + ' \u2192 sem valor')
            elif it[0] == 'p':
                for p in it[1][:10]:
                    out.append('(' + N.fmt(p[0]) + '; ' + N.fmt(p[1]) + ')')
        text(t, '(Gr\u00e1fico s\u00f3 no ecr\u00e3 gr\u00e1fico.)\n' + '\n'.join(out) +
             ('\n' + leg if leg else ''))
        return
    while True:
        busy()
        P.begin()
        title(t)
        L = 30
        R = E['W'] - 6
        T = E['lh'] + 4
        B = (E['rows'] - 2) * E['lh'] - 2
        if leg:
            B -= E['lh']
        sx = (R - L) / (x1 - x0)
        sy = (B - T) / (y1 - y0)

        def px(x):
            return L + (x - x0) * sx

        def py(y):
            return B - (y - y0) * sy
        P.frame(L, T, R - L, B - T, 9)
        st = nice(x0, x1)
        v = st * int(x0 / st)
        while v <= x1:
            if v >= x0:
                X = px(v)
                P.line(X, B, X, B + 3, 7)
            v += st
        st2 = nice(y0, y1)
        v = st2 * int(y0 / st2)
        while v <= y1:
            if v >= y0:
                Y = py(v)
                P.line(L - 3, Y, L, Y, 7)
            v += st2
        if x0 <= 0 <= x1:
            P.line(px(0), T, px(0), B, 7)
        if y0 <= 0 <= y1:
            P.line(L, py(0), R, py(0), 7)
        P.put(0, 1, N.fmt(y1, 2), 7)
        P.put(0, E['rows'] - 3 - (1 if leg else 0), N.fmt(y0, 2), 7)
        P.txt(L, B + 2, N.fmt(x0, 2), 7)
        s = N.fmt(x1, 2)
        P.txt(R - len(s) * E['cw'], B + 2, s, 7)
        for it in items:
            c = it[2]
            if it[0] == 'f':
                f = it[1]
                last = None
                for X in range(int(L), int(R) + 1, 2):
                    x = x0 + (X - L) / sx
                    try:
                        y = f(x)
                        Y = py(y)
                        if Y < T - 2 or Y > B + 2:
                            Y = None
                    except Exception:
                        Y = None
                    if Y is not None and last is not None:
                        P.line(X - 2, last, X, Y, c)
                    last = Y
            elif it[0] == 'p':
                for p in it[1]:
                    X = px(p[0])
                    Y = py(p[1])
                    if L <= X <= R and T <= Y <= B:
                        P.rect(X - 2, Y - 2, 5, 5, c)
            elif it[0] == 's':
                for q in it[1]:
                    P.line(px(q[0]), py(q[1]), px(q[2]), py(q[3]), c)
        if leg:
            P.put(0, E['rows'] - 2, clip(leg, cols()), 0)
        foot('setas: mover \u00b7 + -: escala \u00b7 esc: voltar')
        P.show()
        k = P.key()
        dx = (x1 - x0) / 4
        dy = (y1 - y0) / 4
        if k == 'esc' or k == 'enter':
            return
        if k == 'left':
            x0 -= dx
            x1 -= dx
        elif k == 'right':
            x0 += dx
            x1 += dx
        elif k == 'up':
            y0 += dy
            y1 += dy
        elif k == 'down':
            y0 -= dy
            y1 -= dy
        elif k == '+':
            x0 += dx
            x1 -= dx
            y0 += dy
            y1 -= dy
        elif k == '-':
            x0 -= 2 * dx
            x1 += 2 * dx
            y0 -= 2 * dy
            y1 += 2 * dy
