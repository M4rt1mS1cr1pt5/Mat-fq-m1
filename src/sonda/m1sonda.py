# m1sonda.py - M1TR4M, Fase 0: sonda da calculadora.
# Corre no aparelho antes de tudo. Mostra tamanho do ecra, memoria livre,
# se gc e sys existem, se importar outro programa do mesmo problema
# funciona, se store_list/recall_list funcionam, se time da a data e como
# a fonte desenha alguns simbolos. Depois mostra o nome de cada tecla.
# Fotografa os ecras e envia as fotos.
R = []


def t(nome, f):
    try:
        R.append(nome + ' ' + str(f()))
    except Exception as e:
        R.append(nome + ' ERRO ' + type(e).__name__ + ' ' + str(e))


def mem():
    import gc
    gc.collect()
    return str(gc.mem_free()) + ' livre ' + str(gc.mem_alloc()) + ' usada'


def sysi():
    import sys
    v = sys.implementation
    m = 'sim' if hasattr(sys, 'modules') else 'nao'
    return str(v[1]) + ' ' + sys.platform + ' modules:' + m


def imp():
    import m1sonda2
    return m1sonda2.OLA


def grava():
    import ti_system as s
    s.store_list('m1t', [1, 2.5, 3])
    return str(s.recall_list('m1t'))


def data():
    import time
    return str(time.localtime()[:6])


def ms():
    import ti_system as s
    a = s.get_time_ms()
    return a


def uni():
    return 'len(e acento)=' + str(len('\u00e9')) + ' 1/3=' + repr(1 / 3)


def plat():
    import ti_system as s
    return s.get_platform()


t('mem', mem)
t('sys', sysi)
t('import', imp)
t('grava', grava)
t('data', data)
t('ms', ms)
t('texto', uni)
t('plat', plat)
SYM = '\u221a \u0394 \u03c0 \u2248 \u2192 \u2208 \u2264 \u00b2 \u00b3 \u207b \u2074 \u00d7 \u00b7 \u00e9\u00e7\u00e3 \u2713\u2717 \u25c2\u25b8 \u2026'
try:
    import ti_draw as d
except Exception:
    d = None
if d is None:
    for x in R:
        print(x)
    print(SYM)
else:
    try:
        W, H = d.get_screen_dim()
    except Exception:
        W, H = 318, 212
    R.insert(0, 'ecra ' + str(W) + 'x' + str(H))
    try:
        d.use_buffer()
        buf = 1
    except Exception:
        buf = 0
    d.clear()
    d.set_color(0, 0, 0)
    y = 13
    for x in R:
        d.draw_text(2, y, x[:44])
        y += 14
    # Simbolos (cada um isolado, para ver quais aparecem).
    x = 2
    for s in SYM.split(' '):
        try:
            d.draw_text(x, y, s)
        except Exception:
            d.draw_text(x, y, '?')
        x += 8 * len(s) + 6
    y += 18
    # Regua: marcas de 10 em 10 px e texto para medir a largura e a base.
    d.set_color(200, 0, 0)
    d.draw_line(0, y, W, y)
    for i in range(0, W, 10):
        d.draw_line(i, y, i, y + (6 if i % 50 == 0 else 3))
    d.set_color(0, 0, 255)
    d.draw_text(0, y + 22, 'MMMMMMMMMMiiiiiiiiii0123456789')
    d.draw_line(0, y + 22, W, y + 22)
    if buf:
        d.paint_buffer()
    import ti_system as s
    s.get_key(1)
    ks = []
    while True:
        d.clear()
        d.set_color(0, 0, 0)
        d.draw_text(2, 16, 'Teste de teclas: carrega em teclas.')
        d.draw_text(2, 32, 'esc duas vezes seguidas: sair')
        for i in range(len(ks)):
            d.draw_text(2, 52 + 15 * i, str(i + 1) + ': [' + ks[i] + ']')
        if buf:
            d.paint_buffer()
        k = s.get_key(1)
        ks.append(str(k))
        ks = ks[-9:]
        if len(ks) >= 2 and ks[-1] == 'esc' and ks[-2] == 'esc':
            break
