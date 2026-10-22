#!/usr/bin/env python3
"""Converte carateres nao ASCII de ficheiros .py em codigos \\uXXXX.

Uso: python3 ferramentas/asciifica.py ficheiro.py [...]
So deve haver carateres nao ASCII dentro de strings; nos comentarios o
build recusa-os (seccao 5, passo 5 do prompt).
"""
import sys


def asciifica(txt):
    out = []
    for ch in txt:
        o = ord(ch)
        if o < 128:
            out.append(ch)
        elif o <= 0xFFFF:
            out.append('\\u%04x' % o)
        else:
            out.append('\\U%08x' % o)
    return ''.join(out)


def main(paths):
    mudou = 0
    for p in paths:
        with open(p, encoding='utf-8') as f:
            t = f.read()
        n = asciifica(t)
        if n != t:
            with open(p, 'w', encoding='ascii', newline='\n') as f:
                f.write(n)
            mudou += 1
            print('convertido:', p)
    return mudou


if __name__ == '__main__':
    main(sys.argv[1:])
