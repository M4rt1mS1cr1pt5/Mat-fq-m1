# m1_plat.py - M1TR4M: camada de plataforma.
# Unico modulo que importa ti_draw e ti_system. Trata do ecra, das teclas,
# do tempo, da memoria, da gravacao de dados e da detecao de capacidades.
# Tres variantes com a mesma interface:
#  - calculadora: ti_draw e ti_system da TI-Nspire CX II;
#  - simulador: ti_draw e ti_system falsos (ferramentas/simulador);
#  - modo texto: sem ti_draw, desenha numa grelha e usa print/input.
# Codigo so em ASCII; os acentos aparecem como codigos \u.

VER = 1

try:
    import ti_draw as D
except Exception:
    D = None
try:
    import ti_system as S
except Exception:
    S = None
try:
    import time as T
except Exception:
    T = None
try:
    import gc
except Exception:
    gc = None
try:
    import sys
except Exception:
    sys = None

# Estado do ecra. W,H: tamanho; cw: largura de um caracter; lh: altura de
# uma linha; dy: deslocamento vertical do texto (draw_text usa a linha de
# base); mx: margem; g: 1 se ha graficos; sym: 2 simbolos todos,
# 1 so Latin-1, 0 so ASCII; log: avisos para o Diagnostico.
E = {'W': 318, 'H': 212, 'cw': 7, 'lh': 17, 'dy': 13, 'mx': 4,
     'cols': 44, 'rows': 12, 'g': 0, 'buf': 0, 'sym': 2, 'log': [],
     'scr': [], 'col': -1, 'grid': None, 'q': [], 'tm': None}

# Paleta: 0 texto, 1 fundo, 2 titulo, 3 formula, 4 resultado, 5 erro,
# 6 certo, 7 discreto, 8 destaque, 9 cinza claro, 10 branco do titulo
PAL = ((0, 0, 0), (255, 255, 255), (0, 51, 153), (128, 0, 128),
       (0, 96, 160), (200, 0, 0), (0, 128, 0), (100, 100, 100),
       (204, 224, 255), (232, 232, 232), (255, 255, 255))


def init():
    # Deteta o ecra e liga o buffer de desenho.
    if D is not None:
        E['g'] = 1
        try:
            w, h = D.get_screen_dim()
            if w > 100 and h > 100:
                E['W'] = int(w)
                E['H'] = int(h)
        except Exception:
            E['log'].append('get_screen_dim falhou: usa 318x212')
        try:
            D.use_buffer()
            E['buf'] = 1
        except Exception:
            E['log'].append('use_buffer falhou: pode piscar')
    metrics(E['cw'], E['lh'], E['dy'])


def metrics(cw, lh, dy):
    # Muda as metricas do texto e recalcula colunas e linhas.
    E['cw'] = max(4, int(cw))
    E['lh'] = max(8, int(lh))
    E['dy'] = int(dy)
    E['cols'] = (E['W'] - 2 * E['mx']) // E['cw']
    E['rows'] = E['H'] // E['lh']


def log(m):
    if len(E['log']) < 12:
        E['log'].append(m)

# ---------------------------------------------------------------- texto
# Tabela de substituicao para quando a fonte nao tem um simbolo.
# Pares "simbolo substituto" separados por "|".
_AM = ("\u00e1 a#\u00e0 a#\u00e2 a#\u00e3 a#\u00e9 e#\u00ea e#\u00e8 e#"
       "\u00ed i#\u00f3 o#\u00f4 o#\u00f5 o#\u00fa u#\u00fc u#\u00e7 c#"
       "\u00c1 A#\u00c0 A#\u00c2 A#\u00c3 A#\u00c9 E#\u00ca E#\u00cd I#"
       "\u00d3 O#\u00d4 O#\u00d5 O#\u00da U#\u00c7 C#\u00eb e#\u00ef i#"
       "\u00d7 x#\u00f7 /#\u00b7 .#\u221a sqrt#\u03c0 pi#\u2248 ~#\u2264 <=#"
       "\u2265 >=#\u2260 !=#\u2192 ->#\u2190 <-#\u2194 <->#\u21d4 <=>#"
       "\u2208 em#\u2209 nao em#\u0394 D#\u03b4 d#\u00b1 +-#\u00b0 o#"
       "\u00ba o#\u00aa a#\u2212 -#\u2013 -#\u2014 -#\u2026 ...#"
       "\u201c \"#\u201d \"#\u2018 '#\u2019 '#\u2227 e#\u2228 ou#"
       "\u2016 |#\u211d R#\u221e inf#\u03bb lambda#\u03bd v#\u03c1 ro#"
       "\u03b7 eta#\u03b1 alfa#\u03b2 beta#\u03b8 teta#\u03c3 sigma#"
       "\u03b5 eps#\u03bc u#\u00b5 u#\u03a3 Soma#\u2220 ang#\u22a5 perp#"
       "\u2225 //#\u25b8 >#\u25c2 <#\u2713 v#\u2717 x#\u2605 *#\u2022 -#"
       "\u2032 '#\u2033 \"#\u00bd 1/2#\u21cc <=>#\u2261 ==#\u00a0  #"
       "\u2080 0#\u2081 1#\u2082 2#\u2083 3#\u2084 4#\u2085 5#\u2086 6#"
       "\u2087 7#\u2088 8#\u2089 9#\u2223 |#\u2099 n#\u2090 a#\u2098 m#\u1d62 i#\u20d7 #\u0305 #\u2032 '#\u00ab \"#"
       "\u00bb \"#\u2191 ^#\u2193 v#\u25cf o#\u25cb o#\u2502 |#\u2500 -")
# Expoentes: cada sequencia passa a "^..." no modo sem simbolos.
_SUP = "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079\u207b\u207a"
_SUPP = "0123456789-+"
_AMD = None


def _amap():
    global _AMD
    if _AMD is None:
        _AMD = {}
        for p in _AM.split('#'):
            if len(p) > 1:
                _AMD[p[0]] = p[2:]
    return _AMD


def vis(s, lvl=-1):
    # Adapta o texto ao nivel de simbolos que a fonte aguenta.
    if lvl < 0:
        lvl = E['sym']
    if lvl >= 2:
        return s
    try:
        if len(s.encode()) == len(s):
            return s
    except Exception:
        pass
    m = _amap()
    o = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        k = _SUP.find(ch)
        if k >= 0:
            j = i
            while j < n and _SUP.find(s[j]) >= 0:
                j += 1
            run = s[i:j]
            keep = lvl == 1
            if keep:
                for c in run:
                    if ord(c) > 255:
                        keep = False
            if keep:
                o.append(run)
            else:
                o.append('^')
                for c in run:
                    o.append(_SUPP[_SUP.find(c)])
            i = j
            continue
        if ord(ch) > 127 and (lvl == 0 or ord(ch) > 255):
            o.append(m.get(ch, '?'))
        else:
            o.append(ch)
        i += 1
    return ''.join(o)

# ---------------------------------------------------------------- desenho


def _col(c):
    if c != E['col']:
        E['col'] = c
        r, g, b = PAL[c]
        D.set_color(r, g, b)


def begin():
    # Comeca um ecra novo (fora do ecra, no buffer).
    if E['g']:
        E['col'] = -1
        _col(1)
        D.fill_rect(0, 0, E['W'], E['H'])
    else:
        E['grid'] = [[' '] * E['cols'] for i in range(E['rows'])]


def show():
    # Mostra o ecra de uma so vez.
    if E['g']:
        if E['buf']:
            D.paint_buffer()
    else:
        g = E['grid']
        if g is None:
            return
        out = []
        for r in g:
            out.append(''.join(r).rstrip())
        print('-' * E['cols'])
        print('\n'.join(out))


def rect(x, y, w, h, c):
    if E['g'] and w > 0 and h > 0:
        _col(c)
        D.fill_rect(int(x), int(y), int(w), int(h))


def frame(x, y, w, h, c):
    if E['g']:
        _col(c)
        D.draw_rect(int(x), int(y), int(w), int(h))


def line(x1, y1, x2, y2, c):
    if E['g']:
        _col(c)
        D.draw_line(int(x1), int(y1), int(x2), int(y2))


def circ(x, y, r, c, fill=0):
    if E['g']:
        _col(c)
        if fill:
            D.fill_circle(int(x), int(y), int(r))
        else:
            D.draw_circle(int(x), int(y), int(r))


def poly(xs, ys, c, fill=0):
    if E['g']:
        _col(c)
        xs = [int(v) for v in xs]
        ys = [int(v) for v in ys]
        if fill:
            D.fill_poly(xs, ys)
        else:
            D.draw_poly(xs, ys)


def txt(x, y, s, c=0):
    # Texto em pixeis; y e o topo da linha.
    if not s:
        return
    if E['g']:
        if E['sym'] < 2:
            s = vis(s)
        _col(c)
        try:
            D.draw_text(int(x), int(y) + E['dy'], s)
        except Exception:
            if E['sym'] > 0:
                E['sym'] = 0
                log('draw_text falhou com simbolo: passa a letras simples')
                try:
                    D.draw_text(int(x), int(y) + E['dy'], vis(s, 0))
                except Exception:
                    pass
    else:
        g = E['grid']
        r = int(y) // E['lh']
        cc = (int(x) - E['mx']) // E['cw']
        if g is None or r < 0 or r >= len(g):
            return
        row = g[r]
        if E['sym'] < 2:
            s = vis(s)
        for ch in s:
            if 0 <= cc < len(row):
                row[cc] = ch
            cc += 1


def put(col, row, s, c=0):
    # Texto na grelha de caracteres (coluna, linha).
    txt(E['mx'] + col * E['cw'], row * E['lh'], s, c)

# ---------------------------------------------------------------- teclas
# Nomes alternativos -> nome unico usado pela app.
KN = {'center': 'enter', '\n': 'enter', '\r': 'enter', 'return': 'enter',
      'ok': 'enter', 'escape': 'esc', 'backspace': 'del', 'delete': 'del',
      'space': ' ', '\u2212': '-', 'pi': '\u03c0', '\u00d7': '*',
      '\u00f7': '/', 'clr': 'clear', 'sqrt': '\u221a', 'sqrt(': '\u221a',
      'ctrl': 'ctrl', 'shift': 'shift', 'tab': 'tab', 'exp': 'e',
      'ee': 'e', 'square': '^2', 'x^2': '^2', '\u00b2': '^2'}
TXT_KEYS = ('enter', 'esc', 'up', 'down', 'left', 'right', 'del', 'clear',
            'tab', 'shift', 'home', 'menu', 'ctrl', 'ans', 'var')


def raw_key(wait=1):
    # Tecla tal como a plataforma a devolve (para o "Teste de teclas").
    if E['g'] and S is not None:
        if wait:
            return S.get_key(1)
        return S.get_key()
    q = E['q']
    while not q:
        try:
            ln = input('tecla> ')
        except EOFError:
            raise KeyboardInterrupt
        for t in ln.split(' '):
            if t == '':
                continue
            if t in TXT_KEYS or t.lower() in KN:
                q.append(t)
            else:
                for ch in t:
                    q.append(ch)
        if ln == '':
            q.append('enter')
    return q.pop(0)


def norm(k):
    if not k:
        return ''
    if len(k) > 1:
        k2 = k.lower()
        return KN.get(k2, k2)
    return KN.get(k, k)


def key(wait=1):
    # Espera por uma tecla (get_key(1) nao gasta bateria) e normaliza-a.
    return norm(raw_key(wait))

# ---------------------------------------------------------------- tempo


def ms():
    # Milissegundos (para medir duracoes e semear a ordem dos testes).
    if not E['tm']:
        try:
            v = int(S.get_time_ms())
            E['tm'] = 0
            return v
        except Exception:
            E['tm'] = 1
    if E['tm'] == 1:
        try:
            return int(T.ticks_ms())
        except Exception:
            E['tm'] = 2
    try:
        return int(T.time() * 1000)
    except Exception:
        return 0


def today():
    # (ano, mes, dia) se o modulo time der uma data credivel; senao None.
    try:
        t = T.localtime()
        if t[0] >= 2020 and 1 <= t[1] <= 12:
            return (t[0], t[1], t[2])
    except Exception:
        pass
    return None


def sleep_ms(n):
    try:
        T.sleep(n / 1000)
    except Exception:
        pass

# ---------------------------------------------------------------- memoria


def free():
    # Memoria livre depois de recolher o lixo (-1 se nao se sabe).
    try:
        gc.collect()
        return gc.mem_free()
    except Exception:
        return -1


def collect():
    try:
        gc.collect()
    except Exception:
        pass


def has_mods():
    try:
        return sys.modules is not None
    except Exception:
        return False


def unload(n):
    # Remove um modulo de sys.modules para a memoria poder ser libertada.
    try:
        if n in sys.modules:
            del sys.modules[n]
        return True
    except Exception:
        return False


def mod_file(m):
    try:
        return m.__file__
    except Exception:
        return ''

# ---------------------------------------------------------------- gravar


def save(n, lst):
    # Guarda uma lista de numeros numa variavel do documento.
    try:
        S.store_list(n, lst)
        return True
    except Exception:
        return False


def load(n):
    try:
        r = S.recall_list(n)
        if r is None:
            return None
        return [v for v in r]
    except Exception:
        return None


def platform():
    try:
        return str(S.get_platform())
    except Exception:
        if D is None:
            return 'texto'
        return '?'
