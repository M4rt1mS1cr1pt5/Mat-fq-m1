#!/usr/bin/env python3
"""Ajuda para editar fontes de conteudo: substitui a secao #X de um
bloco (licao, exemplo ou exercicio) por texto novo."""
import re


def bloco(s, ident):
    m = re.search(r'^@(licao|exemplo|exercicio) ' + re.escape(ident) + r'\n',
                  s, re.M)
    if not m:
        raise KeyError(ident)
    i = m.start()
    n = re.search(r'^@(tema|licao|exemplo|exercicio)\b', s[m.end():], re.M)
    j = m.end() + n.start() if n else len(s)
    return i, j


def setsec(path, ident, sec, texto):
    s = open(path, encoding='utf-8').read()
    i, j = bloco(s, ident)
    blk = s[i:j]
    k = blk.index('\n#' + sec + '\n')
    m = re.search(r'^#[A-Z]\s*$', blk[k + 3:], re.M)
    fim = k + 3 + m.start() if m else len(blk.rstrip('\n'))
    novo = blk[:k] + '\n#' + sec + '\n' + texto.strip('\n') + '\n' + blk[fim:]
    if not m:
        novo = novo.rstrip('\n') + '\n\n'
    s = s[:i] + novo + s[j:]
    open(path, 'w', encoding='utf-8').write(s)


def setmeta(path, ident, chave, valor):
    s = open(path, encoding='utf-8').read()
    i, j = bloco(s, ident)
    blk = s[i:j]
    if re.search(r'^' + chave + r':.*$', blk, re.M):
        blk = re.sub(r'^' + chave + r':.*$', chave + ': ' + valor, blk, count=1,
                     flags=re.M)
    else:
        k = blk.index('\n') + 1
        blk = blk[:k] + chave + ': ' + valor + '\n' + blk[k:]
    open(path, 'w', encoding='utf-8').write(s[:i] + blk + s[j:])
