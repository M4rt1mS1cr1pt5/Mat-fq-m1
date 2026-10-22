# Corre os testes unitarios no Python do computador e no MicroPython.
# Uso: python3 testes/correr.py PASTA_DOS_MODULOS [teste ...]
#      micropython -X heapsize=1M testes/correr.py PASTA_DOS_MODULOS
# Cada ficheiro testes/t_*.py tem funcoes t_... ; uma falha e uma
# excecao (AssertionError ou outra). No fim escreve "TESTES n falhas f".
import sys

AQUI = sys.argv[0].rsplit('/', 1)[0] if '/' in sys.argv[0] else '.'
MODS = ('t_nucleo', 't_ui', 't_calc_com', 't_calc_fq', 't_calc_fis',
        't_calc_al', 't_calc_mat', 't_calc_num', 't_calc_alg',
        't_cont', 't_aleatorios', 't_catalogo')


def main():
    pasta = sys.argv[1]
    sel = sys.argv[2:]
    sys.path.insert(0, AQUI)
    sys.path.insert(0, pasta)
    total = 0
    falhas = []
    for nm in MODS:
        if sel and nm not in sel:
            continue
        try:
            m = __import__(nm)
        except ImportError as e:
            if 'no module named' in str(e).lower() and nm in str(e):
                continue
            falhas.append(nm + ': import: ' + str(e))
            continue
        fs = [k for k in dir(m) if k.startswith('t_')]
        fs.sort()
        for k in fs:
            total += 1
            try:
                getattr(m, k)()
            except Exception as e:
                falhas.append(nm + '.' + k + ': ' + type(e).__name__ + ': ' +
                              str(e))
    for f in falhas:
        print('FALHA', f)
    print('TESTES %d falhas %d' % (total, len(falhas)))


main()
