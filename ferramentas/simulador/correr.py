# Corre a app no simulador (CPython ou MicroPython) com uma sequencia de
# teclas. Uso:
#   python3 correr.py TECLAS [--log FRAMES] [--estado FICH] [--texto]
#   micropython -X heapsize=512K correr.py TECLAS ...
# Sem --texto usa o ti_draw falso (ecra grafico simulado). Com --texto o
# ti_draw fica desligado e a app escreve cada ecra com print.
# No fim escreve um resumo: ecras, textos fora do ecra, teclas usadas,
# teclas a sobrar e pico de memoria viva (MicroPython).
import sys

AQUI = sys.argv[0].rsplit('/', 1)[0] if '/' in sys.argv[0] else '.'
RAIZ = AQUI + '/../..'


def ler_teclas(fn):
    ks = []
    f = open(fn)
    for ln in f.read().split('\n'):
        ln = ln.strip()
        if ln == '' or ln.startswith('#'):
            continue
        if ln == 'space':
            ks.append(' ')
        else:
            ks.append(ln)
    f.close()
    return ks


def main():
    a = sys.argv[1:]
    teclas = a[0]
    log = None
    estado = None
    texto = '--texto' in a
    src = RAIZ + '/src'
    if '--log' in a:
        log = a[a.index('--log') + 1]
    if '--estado' in a:
        estado = a[a.index('--estado') + 1]
    if '--src' in a:
        src = a[a.index('--src') + 1]
    sys.path.insert(0, src)
    sys.path.insert(0, AQUI)
    import ti_system
    import ti_draw
    ks = ler_teclas(teclas)
    ti_system.ST['keys'] = ks
    ti_system.ST['trace'] = '--rastreio' in a
    if estado:
        try:
            f = open(estado)
            for ln in f.read().split('\n'):
                p = ln.split(' ')
                if len(p) >= 1 and p[0]:
                    ti_system.ST['store'][p[0]] = [float(x) for x in p[1:]]
            f.close()
        except OSError:
            pass
    if log:
        ti_draw.ST['log'] = open(log, 'w')
    try:
        import gc
        ti_draw.ST['mem'] = gc
    except ImportError:
        pass
    import m1_plat
    # Data e memoria fixas: a saida e igual em todas as corridas.
    m1_plat.today = lambda: (2026, 10, 22)
    if texto:
        # Modo texto: sem ti_draw; as teclas vem da mesma sequencia (em vez
        # de input(), para a saida ser igual nos dois Pythons).
        m1_plat.D = None
        m1_plat.raw_key = lambda wait=1: ti_system.get_key(1) if wait else ''
    import m1
    fim = 'ok'
    if ti_system.ST['esgotou']:
        fim = 'FALHA: a sequencia acabou antes de a app sair'
    elif ti_system.ST['pos'] < len(ks):
        fim = 'FALHA: sobraram %d teclas' % (len(ks) - ti_system.ST['pos'])
    if log:
        ti_draw.ST['log'].close()
    if estado:
        f = open(estado, 'w')
        for k in sorted(ti_system.ST['store']):
            f.write(k + ' ' + ' '.join([str(v) for v in
                                        ti_system.ST['store'][k]]) + '\n')
        f.close()
    print('RESUMO ecras=%d textos=%d fora=%d teclas=%d/%d pico=%d %s' % (
        ti_draw.ST['n'], ti_draw.ST['texts'], len(ti_draw.ST['viol']),
        ti_system.ST['pos'], len(ks), ti_draw.ST['peak'], fim))
    for v in ti_draw.ST['viol']:
        print('FORA', v)


main()
