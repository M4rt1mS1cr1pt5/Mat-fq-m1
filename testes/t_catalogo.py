# Testes do catalogo das calculadoras: cada calculadora abre e os rotulos
# dos campos e as opcoes cabem numa linha do ecra (45 colunas de 7 px).
import sys

try:
    import gc
except ImportError:
    gc = None

COLS = 45


def t_rotulos_cabem():
    try:
        import m1_calc
    except ImportError:
        return
    mods = {}
    for ln in m1_calc.CALC.split('\n'):
        if ln:
            cid = ln.split('|')[0]
            m, f = cid.split('.')
            mods.setdefault(m, []).append(f)
    longos = []
    nomes = sorted(mods.keys())
    # as calculadoras que comecam com um menu (constantes, unidades, Lewis)
    # recebem "esc" e nao devolvem formulario
    import m1_ui as U
    menu, text = U.menu, U.text
    U.menu = lambda *a: -1
    U.text = lambda *a: 0
    try:
        for m in nomes:
            checa(m, mods[m], longos)
    finally:
        U.menu, U.text = menu, text
    assert not longos, 'rotulos longos: ' + '; '.join(longos)


def checa(m, fns, longos):
    novo = m not in sys.modules
    mod = __import__(m)
    for f in fns:
        r = getattr(mod, f)()
        if r is None:
            continue
        t, fs, fn = r
        for g in fs:
            if not g[1] and len(g[0]) > COLS - 1:
                longos.append(m + '.' + f + ': "' + g[0] + '"')
            if g[4] == 'c':
                for o in g[6]:
                    if len(o) > COLS - 6:
                        longos.append(m + '.' + f + ': opcao "' + o + '"')
    if novo:
        del sys.modules[m]
        mod = None
        if gc:
            gc.collect()
