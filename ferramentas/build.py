#!/usr/bin/env python3
"""Build da M1TR4M (secao 5 do prompt). Para no primeiro erro.

  1. Validar conteudos       6. Testar (CPython e MicroPython 32 bits)
  2. Verificar a matematica  7. Medir a memoria (heap de 512 KB)
  3. Gerar os pacotes        8. Simular o ecra (percursos de teclas)
  4. Gerar indice e catalogo 9. Empacotar (Luna) e conferir byte a byte
  5. Verificar o codigo     10. Relatorio

Uso: python3 ferramentas/build.py [--rapido] [--sem-tns]
  --rapido   salta a medicao de memoria por bissecao (passo 7a)
Ferramentas: MicroPython 1.12 (porta unix, 32 bits), mpy-cross e Luna,
procurados em ferramentas/bin, no PATH ou nas variaveis M1_MP, M1_MPY,
M1_LUNA (ver ferramentas/prepara.sh).
"""
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
import conteudo as CT  # noqa: E402
import dados  # noqa: E402
import verifica  # noqa: E402
import memoria  # noqa: E402
import tns  # noqa: E402

SRC = os.path.join(RAIZ, 'src')
DIST = os.path.join(RAIZ, 'dist')
PY = os.path.join(DIST, 'py')
KB = 1024
RESIDENTES = ['m1', 'm1_plat', 'm1_nucleo', 'm1_ui', 'm1_app', 'm1_cont',
              'm1_cat']
FERRAMENTAS = ['m1_ex', 'm1_cfg', 'm1_pesq', 'm1_ini', 'm1_nav']
ORC = {'m1': 4 * KB, 'm1_plat': 12 * KB, 'm1_nucleo': 35 * KB,
       'm1_ui': 30 * KB, 'p_': 40 * KB, 'c_': 25 * KB, 'x_': 30 * KB,
       'm1_idx': 30 * KB, 'm1_tp': 25 * KB, 'm1_ex': 25 * KB,
       'm1_cfg': 25 * KB, 'm1_pesq': 25 * KB, 'm1_ini': 25 * KB,
       'm1_nav': 25 * KB}
ORC_APP = 30 * KB          # m1_app + m1_cont + m1_cat
ORC_RES = 115 * KB         # todos os residentes
HEAP = 512 * KB


class Falha(Exception):
    pass


def ferramenta(nome, var):
    v = os.environ.get(var)
    if v and os.path.exists(v):
        return v
    p = os.path.join(RAIZ, 'ferramentas', 'bin', nome)
    if os.path.exists(p):
        return p
    return shutil.which(nome)


def passo(n, t):
    print('\n[%d] %s' % (n, t))
    sys.stdout.flush()


def catalogo_calcs():
    out = []
    pasta = os.path.join(SRC, 'calc')
    for f in sorted(os.listdir(pasta)):
        if not f.endswith('.py'):
            continue
        for ln in open(os.path.join(pasta, f), encoding='ascii'):
            if ln.startswith('#@ '):
                t = re.sub(r'\\u([0-9a-fA-F]{4})',
                           lambda m: chr(int(m.group(1), 16)), ln[3:].strip())
                p = t.split('|')
                if len(p) != 5:
                    raise Falha('%s: linha de catalogo invalida: %s' % (f, t))
                if not p[0].startswith(f[:-3] + '.'):
                    raise Falha('%s: id %s nao e deste modulo' % (f, p[0]))
                p[2] = CT.norm(p[2])
                out.append(p)
    ids = [c[0] for c in out]
    if len(set(ids)) != len(ids):
        raise Falha('calculadoras com id repetido')
    return out


def escrever(nome, texto):
    p = os.path.join(PY, nome)
    with open(p, 'w', encoding='ascii', newline='\n') as f:
        f.write(texto)
    return p


def limites():
    p = os.path.join(RAIZ, 'docs', 'limitacoes.txt')
    if os.path.exists(p):
        return open(p, encoding='utf-8').read().strip()
    return ''


def main(args):
    t0 = time.time()
    rel = {'data': datetime.date.today().isoformat(), 'avisos': []}
    mp = ferramenta('micropython', 'M1_MP')
    mpyc = ferramenta('mpy-cross', 'M1_MPY')
    lun = ferramenta('luna', 'M1_LUNA')
    if os.path.isdir(PY):
        shutil.rmtree(PY)
    os.makedirs(PY)

    passo(1, 'Validar conteudos')
    e = dados.aplicar(verifica=True)
    if e:
        raise Falha('; '.join(e))
    calcs = catalogo_calcs()
    temas = CT.ler_temas()
    avisos = []
    ids = CT.validar(temas, set(c[0] for c in calcs), avisos)
    for c in calcs:
        if c[4] and c[4] not in [t.id for t in temas]:
            avisos.append('calculadora %s: tema %s ainda nao existe' %
                          (c[0], c[4]))
    # minimos da seccao 11: 3 exemplos e 8 exercicios por tema; nas AL,
    # 2 exercicios por atividade
    for t in temas:
        mx = 2 * len(t.licoes) if t.grupo == 'a' else 8
        if len(t.exemplos) < 3 or len(t.exercicios) < mx:
            avisos.append('tema %s: %d exemplos (min. 3) e %d exercicios '
                          '(min. %d)' % (t.id, len(t.exemplos),
                                         len(t.exercicios), mx))
    nl = sum(len(t.licoes) for t in temas)
    ne = sum(len(t.exemplos) for t in temas)
    nx = sum(len(t.exercicios) for t in temas)
    nf = sum(len(b.formulas) for t in temas for b in t.licoes)
    print('  %d temas, %d licoes, %d formulas, %d exemplos, %d exercicios, '
          '%d calculadoras' % (len(temas), nl, nf, ne, nx, len(calcs)))
    print('  %d avisos (frases longas e outros)' % len(avisos))
    rel['avisos'] = avisos

    passo(2, 'Verificar a matematica (blocos #V)')
    print('  feito durante a validacao: todas as marcas [[..]] conferem')

    passo(3, 'Gerar os pacotes')
    lic = {b.id: (t, b) for t in temas for b in t.licoes}
    for t in temas:
        escrever(t.pacote + '.py', CT.literal(
            'D', CT.gerar_pacote(t, lic),
            '# %s.py - M1TR4M: %s (gerado pelo build).' % (t.pacote, CT.esc(
                t.titulo))))
        if t.exercicios:
            escrever(t.pacote_x + '.py', CT.literal(
                'D', CT.gerar_exercicios(t),
                '# %s.py - M1TR4M: exercicios de %s (gerado pelo build).' % (
                    t.pacote_x, CT.esc(t.titulo))))
    for f in os.listdir(SRC):
        if f.endswith('.py'):
            shutil.copy(os.path.join(SRC, f), PY)
    for f in os.listdir(os.path.join(SRC, 'calc')):
        if f.endswith('.py'):
            shutil.copy(os.path.join(SRC, 'calc', f), PY)

    passo(4, 'Gerar o indice e o catalogo')
    els = dados.elementos()
    ctes = [(c['nome'], c['simbolo']) for c in dados.constantes()]
    idx = CT.gerar_indice(temas, calcs, els, ctes)
    for nome, d, txt in idx:
        escrever(nome + '.py', txt)
    cat = CT.gerar_catalogo(temas, calcs)
    cat += 'BUILD = "%s"\n' % rel['data']
    cat += '# Partes do indice da pesquisa: modulo:disciplina\n'
    cat += 'IDX = "%s"\n' % ' '.join(n + ':' + d for n, d, x in idx)
    cat += CT.literal('LIMITES', limites() or 'ver RELATORIO.md')
    escrever('m1_cat.py', cat)
    print('  indice da pesquisa em %d partes: %s' % (
        len(idx), ', '.join(n for n, d, x in idx)))

    tam = {}
    for f in sorted(os.listdir(PY)):
        if f.endswith('.py'):
            tam[f[:-3]] = os.path.getsize(os.path.join(PY, f))
    rel['tamanhos'] = tam
    erros = []
    for m, s in tam.items():
        lim = ORC.get(m)
        if lim is None:
            for k in ('p_', 'c_', 'x_', 'm1_idx'):
                if m.startswith(k):
                    lim = ORC[k]
        if lim and s > lim:
            erros.append('%s.py tem %d bytes (max. %d)' % (m, s, lim))
    app = tam['m1_app'] + tam['m1_cont'] + tam['m1_cat']
    res = sum(tam[m] for m in RESIDENTES)
    print('  residentes: %d bytes (max. %d); m1_app+m1_cont+m1_cat: %d '
          '(max. %d)' % (res, ORC_RES, app, ORC_APP))
    if app > ORC_APP:
        erros.append('m1_app+m1_cont+m1_cat tem %d bytes (max. %d)' %
                     (app, ORC_APP))
    if res > ORC_RES:
        erros.append('residentes: %d bytes (max. %d)' % (res, ORC_RES))
    if erros:
        raise Falha('orcamentos ultrapassados: ' + '; '.join(erros))
    rel['residentes'] = res

    passo(5, 'Verificar o codigo')
    n, e = verifica.verificar(PY, mpyc)
    if e:
        raise Falha('\n'.join(e))
    print('  %d modulos: ASCII, sem f-strings, :=, anotacoes, eval/exec; '
          'imports permitidos; compilam no mpy-cross 1.12' % n)

    passo(6, 'Testar')
    rel['testes'] = {}
    for nome, cmd in (('CPython', [sys.executable]),
                      ('MicroPython', [mp, '-X', 'heapsize=2M'])):
        if cmd[0] is None:
            raise Falha('MicroPython nao encontrado')
        r = subprocess.run(cmd + [os.path.join(RAIZ, 'testes', 'correr.py'),
                                  PY], capture_output=True, text=True,
                           timeout=600)
        out = r.stdout + r.stderr
        m = re.search(r'TESTES (\d+) falhas (\d+)', out)
        if not m or m.group(2) != '0':
            raise Falha('testes em %s:\n%s' % (nome, out[-3000:]))
        rel['testes'][nome] = int(m.group(1))
        print('  %s: %s testes, 0 falhas' % (nome, m.group(1)))

    passo(7, 'Medir a memoria')
    rel['residente'] = memoria.residente(mp, PY, ['m1_plat', 'm1_nucleo',
                                                  'm1_ui', 'm1_cont', 'm1_cat',
                                                  'm1_app'])
    print('  memoria residente depois de importar o nucleo: %s bytes' %
          rel['residente'].get('total'))
    if '--rapido' not in args:
        mods = sorted(m for m in tam if m != 'm1' and not
                      m.startswith('m1sonda'))
        picos = memoria.medir_todos(mp, PY, mods, RESIDENTES)
        rel['picos'] = picos
        for m in mods:
            pi, pf, err = picos[m]
            if pi is None:
                raise Falha('%s nao importa com 2 MB de heap: %s' % (m, err))
            print('  %-10s import %4d KB, fonte inteira %4d KB' % (
                m, pi // KB, (pf or 0) // KB))
    caminhos = percursos(mp, rel)

    passo(8, 'Simular o ecra')
    print('  %d percursos de teclas: 0 textos fora do ecra, 0 teclas a '
          'sobrar, modo texto igual nos dois Pythons' % caminhos)

    passo(9, 'Empacotar')
    if '--sem-tns' in args or not lun:
        print('  saltado' + ('' if lun else ' (Luna nao encontrado)'))
    else:
        empacotar(lun, rel)

    passo(10, 'Relatorio')
    rel['tempo'] = round(time.time() - t0, 1)
    with open(os.path.join(DIST, 'build.json'), 'w', encoding='utf-8') as f:
        json.dump(rel, f, ensure_ascii=False, indent=1, sort_keys=True)
    with open(os.path.join(DIST, 'avisos.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(avisos) + '\n')
    print('  dist/build.json e dist/avisos.txt (%.0f s)' % rel['tempo'])


def percursos(mp, rel):
    pasta = os.path.join(RAIZ, 'ferramentas', 'teclas')
    corr = os.path.join(RAIZ, 'ferramentas', 'simulador', 'correr.py')
    cap = os.path.join(DIST, 'capturas')
    os.makedirs(cap, exist_ok=True)
    fs = sorted(f for f in os.listdir(pasta) if f.endswith('.txt'))
    rel['percursos'] = {}
    for f in fs:
        k = os.path.join(pasta, f)
        nome = f[:-4]
        log = os.path.join(cap, nome + '.frames')
        res = {}
        for py, cmd in (('cpy', [sys.executable]),
                        ('mp', [mp, '-X', 'heapsize=%d' % HEAP])):
            r = subprocess.run(cmd + [corr, k, '--src', PY] +
                               (['--log', log] if py == 'cpy' else []),
                               capture_output=True, text=True, timeout=600)
            out = r.stdout + r.stderr
            m = re.search(r'RESUMO (.*)', out)
            if not m or not m.group(1).endswith(' ok') or 'fora=0' not in \
                    m.group(1):
                raise Falha('percurso %s (%s): %s' % (nome, py, out[-2000:]))
            if 'Faltou mem' in open(log, encoding='utf-8').read() if \
                    py == 'cpy' else False:
                raise Falha('percurso %s: mensagem de falta de memoria' % nome)
            res[py] = m.group(1)
        t = {}
        for py, cmd in (('cpy', [sys.executable]),
                        ('mp', [mp, '-X', 'heapsize=%d' % HEAP])):
            r = subprocess.run(cmd + [corr, k, '--src', PY, '--texto'],
                               capture_output=True, text=True, timeout=600)
            t[py] = r.stdout
        if t['cpy'] != t['mp']:
            raise Falha('percurso %s: modo texto diferente nos dois Pythons'
                        % nome)
        if 'RESUMO' not in t['cpy'] or not t['cpy'].rstrip().endswith('ok'):
            raise Falha('percurso %s (texto): %s' % (nome, t['cpy'][-1500:]))
        rel['percursos'][nome] = res
        print('  %-14s %s' % (nome, res['mp']))
    return len(fs)


def empacotar(lun, rel):
    tnsd = os.path.join(DIST, 'tns')
    if os.path.isdir(tnsd):
        shutil.rmtree(tnsd)
    os.makedirs(os.path.join(tnsd, 'PyLib'))
    mods = sorted(f for f in os.listdir(PY) if f.endswith('.py') and
                  f != 'm1.py' and not f.startswith('m1sonda'))
    todos = [os.path.join(PY, 'm1.py')] + [os.path.join(PY, f) for f in mods]
    doc = os.path.join(tnsd, 'M1TR4M.tns')
    tns.luna(lun, todos, doc)
    erros = tns.confere(doc, todos)
    # PyLib: um .tns por modulo e um documento pequeno que arranca a app
    for p in todos[1:]:
        n = os.path.basename(p)[:-3]
        out = os.path.join(tnsd, 'PyLib', n + '.tns')
        tns.luna(lun, [p], out)
        erros += tns.confere(out, [p])
    arr = os.path.join(tnsd, 'arranque')
    os.makedirs(arr, exist_ok=True)
    m1 = open(os.path.join(PY, 'm1.py'), encoding='ascii').read().replace(
        "MODO = 'documento'", "MODO = 'PyLib'")
    pm1 = os.path.join(arr, 'm1.py')
    open(pm1, 'w', encoding='ascii', newline='\n').write(m1)
    out = os.path.join(tnsd, 'M1TR4M_arranque.tns')
    tns.luna(lun, [pm1], out)
    erros += tns.confere(out, [pm1])
    # sonda (Fase 0)
    son = [os.path.join(SRC, 'sonda', 'm1sonda.py'),
           os.path.join(SRC, 'sonda', 'm1sonda2.py')]
    out = os.path.join(tnsd, 'M1TR4M_sonda.tns')
    tns.luna(lun, son, out)
    erros += tns.confere(out, son)
    if erros:
        raise Falha('\n'.join(erros))
    n = len(os.listdir(os.path.join(tnsd, 'PyLib')))
    rel['tns'] = {'documento': os.path.getsize(doc), 'pylib': n}
    print('  M1TR4M.tns (%d modulos, %d bytes), %d .tns para a PyLib, '
          'arranque e sonda; cada .py confere byte a byte' % (
              len(todos), os.path.getsize(doc), n))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except (Falha, CT.Erro) as e:
        print('\nBUILD FALHOU:', e)
        sys.exit(1)
    print('\nBUILD OK')
