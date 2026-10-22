#!/usr/bin/env python3
"""Medicao de memoria no MicroPython 1.12 de 32 bits (secao 5, passo 7).

- Pico de compilacao de cada modulo: o menor heap (-X heapsize) com que
  o modulo se importa sem MemoryError, procurado por bissecao. Mede-se de
  duas formas: "import" (o lexer le o ficheiro aos bocados) e "fonte
  inteira" (le o texto todo para a memoria e compila-o; e o caso pior,
  se a calculadora guardar o programa inteiro no heap).
- Memoria residente: bytes ocupados depois de importar e recolher o lixo.
"""
import os
import subprocess

MAXH = 2048 * 1024


def _corre(mp, pasta, codigo, heap):
    r = subprocess.run([mp, '-X', 'heapsize=%d' % heap, '-c', codigo],
                       capture_output=True, text=True, cwd=pasta, timeout=60)
    return r.returncode == 0 and 'OK' in r.stdout, r.stdout + r.stderr


def _bissecao(mp, pasta, codigo, lo=8 * 1024, hi=MAXH):
    ok, out = _corre(mp, pasta, codigo, hi)
    if not ok:
        return None, out
    while hi - lo > 1024:
        mid = (lo + hi) // 2
        ok, _ = _corre(mp, pasta, codigo, mid)
        if ok:
            hi = mid
        else:
            lo = mid
    return hi, ''


def pico_import(mp, pasta, mod, pre=()):
    imps = ''.join('import %s\n' % p for p in pre)
    c = ('import sys\nsys.path.insert(0, ".")\n' + imps +
         'import gc\ngc.collect()\nimport %s\nprint("OK")\n' % mod)
    return _bissecao(mp, pasta, c)


def pico_fonte(mp, pasta, mod, pre=()):
    imps = ''.join('import %s\n' % p for p in pre)
    c = ('import sys\nsys.path.insert(0, ".")\n' + imps +
         'import gc\ngc.collect()\nf = open("%s.py")\ns = f.read()\nf.close()\n'
         'co = compile(s, "%s", "exec")\ns = None\nd = {"__name__": "%s"}\n'
         'exec(co, d)\nprint("OK")\n' % (mod, mod, mod))
    return _bissecao(mp, pasta, c)


def residente(mp, pasta, mods):
    """Bytes ocupados depois de importar cada modulo da lista (cumulativo)."""
    c = ['import sys', 'sys.path.insert(0, ".")', 'import gc', 'gc.collect()',
         'a0 = gc.mem_alloc()', 'prev = a0']
    for m in mods:
        c.append('import %s' % m)
        c.append('gc.collect()')
        c.append('a = gc.mem_alloc()')
        c.append('print("RES %s", a - prev)' % m)
        c.append('prev = a')
    c.append('print("RES total", prev - a0)')
    c.append('print("OK")')
    r = subprocess.run([mp, '-X', 'heapsize=%d' % MAXH, '-c', '\n'.join(c)],
                       capture_output=True, text=True, cwd=pasta, timeout=60)
    out = {}
    for ln in r.stdout.split('\n'):
        if ln.startswith('RES '):
            p = ln.split()
            out[p[1]] = int(p[2])
    if r.returncode != 0:
        out['ERRO'] = r.stderr.strip()[-300:]
    return out


def medir_todos(mp, pasta, mods, residentes):
    res = {}
    for m in mods:
        pre = [] if m in residentes else ['m1_app']
        pi, e1 = pico_import(mp, pasta, m, pre)
        pf, e2 = pico_fonte(mp, pasta, m, pre)
        res[m] = (pi, pf, (e1 or e2)[-300:])
    return res


if __name__ == '__main__':
    import sys
    mp, pasta = sys.argv[1], sys.argv[2]
    for m in sys.argv[3:]:
        print(m, pico_import(mp, pasta, m)[0], pico_fonte(mp, pasta, m)[0])
