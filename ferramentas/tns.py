#!/usr/bin/env python3
"""Empacotamento em .tns com o Luna e verificacao byte a byte.

Um .tns do Luna e um zip com cabecalho proprio: a 1.a entrada comeca por
"*TIMLP" + versao em vez de "PK\\x03\\x04"; os .py vao so comprimidos
(deflate), sem cifra. Este leitor percorre os cabecalhos locais e
extrai cada .py para comparar com o original.
"""
import os
import struct
import subprocess
import zlib


def luna(exe, entradas, saida):
    if os.path.exists(saida):
        os.remove(saida)
    r = subprocess.run([exe] + list(entradas) + [saida], capture_output=True,
                       text=True)
    if r.returncode != 0 or not os.path.exists(saida):
        raise RuntimeError('luna falhou: ' + (r.stdout + r.stderr)[-500:])


def ler_tns(caminho):
    """Devolve {nome: bytes} das entradas nao cifradas (.py, ...)."""
    d = open(caminho, 'rb').read()
    out = {}
    i = 0
    while i < len(d) - 30:
        sig = d[i:i + 4]
        if sig == b'*TIM':
            h = i + 6 + 4 - 4          # "*TIMLP" + "0500" ocupam 10 bytes
            base = i + 10 - 4          # alinha com um cabecalho PK normal
        elif sig == b'PK\x03\x04':
            base = i
        else:
            if sig == b'PK\x01\x02' or sig == b'PK\x05\x06':
                break
            i += 1
            continue
        # campos do cabecalho local a partir de base+4
        (ver, flag, met, t, dt, crc, csz, usz, nl, xl) = struct.unpack(
            '<HHHHHIIIHH', d[base + 4:base + 30])
        nome = d[base + 30:base + 30 + nl].decode('utf-8', 'replace')
        ini = base + 30 + nl + xl
        dados = d[ini:ini + csz]
        if flag & 8:
            raise RuntimeError('tamanho em descritor de dados nao suportado')
        if met == 8:
            try:
                out[nome] = zlib.decompress(dados, -15)
            except zlib.error:
                out[nome] = None
        elif met == 0:
            out[nome] = dados
        else:
            out[nome] = None      # entrada cifrada (XML do problema)
        i = ini + csz
    return out


def confere(caminho, originais):
    """Confirma que cada .py dentro do .tns e igual ao original."""
    lido = ler_tns(caminho)
    erros = []
    for p in originais:
        n = os.path.basename(p)
        if n not in lido:
            erros.append('%s: falta %s' % (os.path.basename(caminho), n))
            continue
        if lido[n] != open(p, 'rb').read():
            erros.append('%s: %s diferente do original' %
                         (os.path.basename(caminho), n))
    return erros
