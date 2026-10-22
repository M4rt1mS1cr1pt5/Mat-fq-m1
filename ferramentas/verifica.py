#!/usr/bin/env python3
"""Verificacao do codigo (secao 5, passo 5 do prompt).

Para cada modulo: so ASCII; sem f-strings, operador :=, anotacoes de
tipos, eval nem exec, nem metodos de str que o MicroPython 1.12 nao tem; so importa os modulos permitidos (math, time,
ti_system, ti_draw; gc e sys so dentro de try/except; e os da propria
app); compila com o mpy-cross do MicroPython 1.12 de 32 bits.
"""
import ast
import io
import os
import subprocess
import sys
import tokenize

PERMITIDOS = {'math', 'time', 'ti_system', 'ti_draw'}
# Metodos de str que o MicroPython 1.12 nao tem (falham so no aparelho).
SEM_MP = {'capitalize', 'title', 'ljust', 'rjust', 'zfill', 'center',
          'casefold', 'swapcase', 'expandtabs', 'format_map', 'isnumeric',
          'isdecimal', 'isidentifier', 'isprintable', 'istitle',
          'removeprefix', 'removesuffix'}
SO_EM_TRY = {'gc', 'sys'}
PROPRIOS = ('m1', 'c_', 'p_', 'x_')


def proprio(nome):
    return nome == 'm1' or nome.startswith(('m1_', 'c_', 'p_', 'x_'))


def verificar_fonte(caminho, texto, extra_ok=()):
    erros = []
    nome = os.path.basename(caminho)
    try:
        texto.encode('ascii')
    except UnicodeEncodeError as e:
        linha = texto[:e.start].count('\n') + 1
        erros.append('%s:%d: caracter nao ASCII' % (nome, linha))
        return erros
    try:
        for tok in tokenize.generate_tokens(io.StringIO(texto).readline):
            if tok.type == tokenize.STRING:
                p = tok.string[:3].lower()
                if p.startswith(('f', 'rf', 'fr')):
                    erros.append('%s:%d: f-string' % (nome, tok.start[0]))
    except tokenize.TokenError as e:
        erros.append('%s: erro de tokens: %s' % (nome, e))
    try:
        arv = ast.parse(texto)
    except SyntaxError as e:
        erros.append('%s:%s: erro de sintaxe: %s' % (nome, e.lineno, e.msg))
        return erros
    modulos = set()
    for no in ast.walk(arv):
        if isinstance(no, ast.Import):
            for a in no.names:
                modulos.add(a.asname or a.name)
    dentro_try = set()
    for no in ast.walk(arv):
        if isinstance(no, ast.Try):
            for sub in no.body:
                for x in ast.walk(sub):
                    dentro_try.add(id(x))
    for no in ast.walk(arv):
        if isinstance(no, ast.NamedExpr):
            erros.append('%s:%d: operador :=' % (nome, no.lineno))
        if isinstance(no, ast.AnnAssign):
            erros.append('%s:%d: anotacao de tipo' % (nome, no.lineno))
        if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if no.returns is not None or any(
                    a.annotation is not None for a in
                    no.args.args + no.args.kwonlyargs):
                erros.append('%s:%d: anotacao de tipo' % (nome, no.lineno))
        if isinstance(no, ast.Call) and isinstance(no.func, ast.Attribute) \
                and no.func.attr in SEM_MP and not (
                    isinstance(no.func.value, ast.Name) and
                    no.func.value.id in modulos):
            erros.append('%s:%d: .%s() nao existe no MicroPython 1.12' %
                         (nome, no.lineno, no.func.attr))
        if isinstance(no, ast.Call) and isinstance(no.func, ast.Name) and \
                no.func.id in ('eval', 'exec', 'compile'):
            erros.append('%s:%d: %s' % (nome, no.lineno, no.func.id))
        if isinstance(no, (ast.Import, ast.ImportFrom)):
            mods = [a.name for a in no.names] if isinstance(no, ast.Import) \
                else [no.module or '']
            if isinstance(no, ast.ImportFrom):
                if any(a.name == '*' for a in no.names):
                    erros.append('%s:%d: from ... import *' % (nome, no.lineno))
            for m in mods:
                if m in PERMITIDOS or proprio(m) or m in extra_ok:
                    continue
                if m in SO_EM_TRY:
                    if id(no) not in dentro_try:
                        erros.append('%s:%d: import %s fora de try/except' %
                                     (nome, no.lineno, m))
                    continue
                erros.append('%s:%d: modulo nao permitido: %s' %
                             (nome, no.lineno, m))
    return erros


def mpy_cross(caminho, mpyc):
    if not mpyc or not os.path.exists(mpyc):
        return ['mpy-cross nao encontrado (%s)' % mpyc]
    r = subprocess.run([mpyc, '-o', '/dev/null', caminho],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return ['%s: mpy-cross: %s' % (os.path.basename(caminho),
                                       (r.stderr or r.stdout).strip())]
    return []


def verificar(pasta, mpyc=None, extra_ok=()):
    erros = []
    n = 0
    for f in sorted(os.listdir(pasta)):
        if not f.endswith('.py'):
            continue
        p = os.path.join(pasta, f)
        with open(p, encoding='utf-8', errors='replace') as fh:
            t = fh.read()
        erros += verificar_fonte(p, t, extra_ok)
        erros += mpy_cross(p, mpyc)
        n += 1
    return n, erros


if __name__ == '__main__':
    n, e = verificar(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    for x in e:
        print('ERRO', x)
    print(n, 'modulos verificados,', len(e), 'erros')
    sys.exit(1 if e else 0)
