#!/usr/bin/env python3
"""Mostra como uma pagina de uma licao fica partida no ecra (41 colunas).

Uso: python3 ferramentas/medir.py conteudo/fq/q1.txt [id] [paginas]
Sem id: mostra o numero de linhas de todas as paginas de todas as licoes.
"""
import sys

import conteudo as CT


def main(a):
    bs = CT.ler_ficheiro(a[0])
    for b in bs:
        if b.tipo != 'licao':
            continue
        if len(a) > 1 and b.id != a[1]:
            continue
        pags = a[2] if len(a) > 2 else 'ABCDFGHIJR'
        lim = {'A': 5, 'B': 8, 'C': 12, 'D': 30, 'F': 30, 'G': 8, 'H': 5,
               'I': 6, 'J': 10, 'R': 99}
        linha = []
        for p in pags:
            s = b.sec.get(p, '')
            n = CT.nlinhas(s)
            linha.append('%s%d%s' % (p, n, '!' if n > lim[p] and p not in
                                     'AHI' else ''))
            if len(a) > 1:
                print('--- %s pag. %s: %d linhas' % (b.id, p, n))
                for st, t in CT.U.wrap(CT.tirar_marcas(s), CT.LARG):
                    print('|' + t.ljust(CT.LARG) + '|')
        if len(a) <= 1:
            print(b.id, ' '.join(linha))


if __name__ == '__main__':
    main(sys.argv[1:])
