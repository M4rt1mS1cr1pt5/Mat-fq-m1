#!/usr/bin/env python3
"""Gera os blocos de dados a partir de dados/*.csv e escreve-os nos
modulos (entre as marcas "# --- dados (gerado) ---" e "# --- fim dos
dados ---"): src/m1_tp.py (tabela periodica), src/calc/c_fqat.py (massas
atomicas relativas para a massa molar) e src/calc/c_comd.py (constantes).

Uso: python3 ferramentas/dados.py [--verifica]
Com --verifica nao escreve: falha se algum modulo estiver desatualizado.
"""
import csv
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
from conteudo import literal  # noqa: E402

INI = '# --- dados (gerado) ---\n'
FIM = '# --- fim dos dados ---\n'


def elementos():
    with open(os.path.join(RAIZ, 'dados', 'elementos.csv'),
              encoding='utf-8') as f:
        return list(csv.DictReader(f))


def constantes():
    with open(os.path.join(RAIZ, 'dados', 'constantes.csv'),
              encoding='utf-8') as f:
        return list(csv.DictReader(f))


def bloco_tp():
    ls = []
    for e in elementos():
        ls.append('|'.join([e['z'], e['simbolo'], e['nome'], e['ar'],
                            e['grupo'], e['periodo'], e['bloco'], e['tipo'],
                            e['estado'], e['raio_pm'], e['ei_kj_mol']]))
    return literal('TD', '\n'.join(ls))


def ar_iave(a):
    """Ar com 2 casas decimais (como na tabela periodica do exame)."""
    if a.startswith('['):
        return a.strip('[]')
    v = float(a)
    return ('%.2f' % (v + 1e-9))


def bloco_ar():
    ls = []
    for e in elementos():
        ls.append(e['simbolo'] + ' ' + ar_iave(e['ar']))
    return literal('AR', ' '.join(ls))


def bloco_cte():
    ls = []
    for c in constantes():
        ls.append('|'.join([c['nome'], c['simbolo'], c['valor'], c['unidade'],
                            c['fonte'], c['ano']]))
    return literal('CTE', '\n'.join(ls))


ALVOS = [('src/m1_tp.py', bloco_tp), ('src/calc/c_fqat.py', bloco_ar),
         ('src/calc/c_comd.py', bloco_cte)]


def aplicar(verifica=False):
    erros = []
    for rel, f in ALVOS:
        p = os.path.join(RAIZ, rel)
        if not os.path.exists(p):
            erros.append(rel + ': nao existe')
            continue
        s = open(p, encoding='ascii').read()
        i = s.find(INI)
        j = s.find(FIM)
        if i < 0 or j < 0:
            erros.append(rel + ': sem marcas de dados')
            continue
        novo = s[:i + len(INI)] + f() + s[j:]
        if novo != s:
            if verifica:
                erros.append(rel + ': dados desatualizados (corre '
                             'ferramentas/dados.py)')
            else:
                with open(p, 'w', encoding='ascii', newline='\n') as fo:
                    fo.write(novo)
                print('dados escritos em', rel)
    return erros


if __name__ == '__main__':
    e = aplicar('--verifica' in sys.argv)
    for x in e:
        print('ERRO', x)
    sys.exit(1 if e else 0)
