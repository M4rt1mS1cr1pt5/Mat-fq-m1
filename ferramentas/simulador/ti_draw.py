# ti_draw falso para o simulador no computador (CPython e MicroPython).
# Regista as operacoes de desenho de cada ecra (paint_buffer) e verifica
# se algum texto sai do ecra, com as metricas assumidas pela app
# (7 px por caracter, linha de base 13 px abaixo do topo da linha).

W = 318
H = 212
CW = 7          # largura assumida de um caracter
ASC = 12        # altura acima da linha de base
DESC = 4        # altura abaixo da linha de base
ST = {'col': (0, 0, 0), 'buf': 0, 'n': 0, 'log': None, 'viol': [],
      'texts': 0, 'mem': None, 'peak': 0}
OPS = []


def get_screen_dim():
    return (W, H)


def use_buffer():
    ST['buf'] = 1


def set_color(r, g, b):
    ST['col'] = (int(r), int(g), int(b))


def set_pen(a=None, b=None):
    pass


def clear():
    del OPS[:]
    OPS.append('R\t0\t0\t%d\t%d\t255,255,255' % (W, H))


def _c():
    c = ST['col']
    return str(c[0]) + ',' + str(c[1]) + ',' + str(c[2])


def fill_rect(x, y, w, h):
    OPS.append('R\t%d\t%d\t%d\t%d\t%s' % (x, y, w, h, _c()))


def draw_rect(x, y, w, h):
    OPS.append('r\t%d\t%d\t%d\t%d\t%s' % (x, y, w, h, _c()))


def draw_line(x1, y1, x2, y2):
    OPS.append('L\t%d\t%d\t%d\t%d\t%s' % (x1, y1, x2, y2, _c()))


def fill_circle(x, y, r):
    OPS.append('C\t%d\t%d\t%d\t%s' % (x, y, r, _c()))


def draw_circle(x, y, r):
    OPS.append('c\t%d\t%d\t%d\t%s' % (x, y, r, _c()))


def _poly(t, xs, ys):
    p = []
    for i in range(len(xs)):
        p.append(str(int(xs[i])) + ',' + str(int(ys[i])))
    OPS.append(t + '\t' + ' '.join(p) + '\t' + _c())


def fill_poly(xs, ys):
    _poly('P', xs, ys)


def draw_poly(xs, ys):
    _poly('p', xs, ys)


def plot_xy(x, y, s=1):
    OPS.append('R\t%d\t%d\t1\t1\t%s' % (x, y, _c()))


def draw_text(x, y, s):
    s = str(s)
    ST['texts'] += 1
    if x < 0 or x + len(s) * CW > W + 1 or y - ASC < 0 or y + DESC > H:
        if len(ST['viol']) < 50:
            ST['viol'].append('ecra %d: texto fora (%d,%d) "%s"' %
                              (ST['n'] + 1, x, y, s))
    OPS.append('T\t%d\t%d\t%s\t%s' % (x, y, _c(), s))


def paint_buffer():
    # Fecha um ecra: escreve-o no registo e mede a memoria viva da app.
    ST['n'] += 1
    f = ST['log']
    if f is not None:
        f.write('F\t%d\n' % ST['n'])
        for o in OPS:
            f.write(o)
            f.write('\n')
    del OPS[:]
    m = ST.get('mem')
    if m is not None:
        try:
            m.collect()
            a = m.mem_alloc()
            if a > ST['peak']:
                ST['peak'] = a
        except Exception:
            pass
