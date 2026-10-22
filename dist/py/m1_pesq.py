# m1_pesq.py - M1TR4M: pesquisa global. Carregado a pedido; o indice
# (m1_idx, gerado pelo build) so esta em memoria durante a pesquisa.
# Os resultados aparecem a cada tecla e ignoram acentos e maiusculas.
# Ordem: titulo igual, titulo que comeca pela pesquisa, palavra do
# titulo, palavras-chave. Maximo de 60 resultados.

import m1_plat as P
import m1_ui as U
import m1_cont as C
import m1_app as A

VER = 1
# Pares de um so caracter (o texto dobrado tem o mesmo comprimento).
FOLD = ('\u00e1a\u00e0a\u00e2a\u00e3a\u00e9e\u00eae\u00e8e\u00edi\u00f3o\u00f4o\u00f5o'
        '\u00fau\u00fcu\u00e7c\u00c1a\u00c0a\u00c2a\u00c3a\u00c9e\u00cae\u00cdi\u00d3o'
        '\u00d4o\u00d5o\u00dau\u00c7c\u03c0p\u221av\u00b2 \u00b3 \u00b7 \u00ba \u00aa ')
TAG = {'L': 'L', 'C': 'C', 'F': 'F', 'E': 'E', 'X': 'X', 'T': 'T', 'K': 'K'}
FILT = ('tudo', 'FQ', 'Mat')
MAXR = 60
ST = A.S


def fold(s):
    s = s.lower()
    for i in range(0, len(FOLD), 2):
        a = FOLD[i]
        if a in s:
            s = s.replace(a, FOLD[i + 1])
    return s


def find(L, q, flt):
    # Procura q no texto dobrado L. Devolve [(ordem, titulo, posicao)].
    res = []
    i = L.find(q)
    while i >= 0 and len(res) < 200:
        a = L.rfind('\n', 0, i) + 1
        b = L.find('\n', i)
        if b < 0:
            b = len(L)
        ps = L[a:b].split('|')
        if len(ps) < 5 or ps[0].startswith('@'):
            i = L.find(q, b)
            continue
        t0 = a + len(ps[0]) + len(ps[1]) + 2
        t1 = t0 + len(ps[2]) + 1 + len(ps[3])
        if not (t0 <= i < t1):
            i = L.find(q, i + 1)
            continue
        d = ps[1]
        if flt == 1 and d == 'm' or flt == 2 and d == 'f':
            i = L.find(q, b)
            continue
        tl = ps[2]
        if tl == q:
            r = 0
        elif tl.startswith(q):
            r = 1
        elif (' ' + q) in (' ' + tl):
            r = 2
        elif q in tl:
            r = 3
        elif (' ' + q) in (' ' + ps[3]):
            r = 4
        else:
            r = 5
        res.append((r, tl, a))
        i = L.find(q, b)
    res.sort(key=lambda x: (x[0], x[1], x[2]))
    return res[:MAXR]


def run():
    # Devolve o alvo escolhido ("L:q1a", "C:c_fqat.mm"...) ou None.
    q = ST.get('q', '')
    flt = ST.get('qf', 0)
    mn = ST.get('qmin', 1)
    sel = 0
    top = 0
    D = C.get('p', 'm1_idx').D
    L = fold(D)
    h = U.body() - 1
    while True:
        A.S['where'] = 'pesquisa'
        t0 = P.ms()
        fq = fold(q.strip())
        res = find(L, fq, flt) if len(fq) >= mn else []
        if P.ms() - t0 > 300 and mn < 2:
            mn = 2
            ST['qmin'] = 2
        sel = max(0, min(sel, len(res) - 1))
        if sel < top:
            top = sel
        if sel >= top + h:
            top = sel - h + 1
        P.begin()
        U.title('Pesquisa \u00b7 ' + FILT[flt], str(len(res)) +
                (' (m\u00e1x.)' if len(res) >= MAXR else ''))
        U._box(1, q, len(q), U.cols() - 4, 1)
        if len(fq) < mn:
            P.put(0, 2, 'Escreve ' + ('pelo menos 2 letras' if mn > 1 else
                                     'uma palavra') + ' (sem acentos serve).', 7)
        elif not res:
            P.put(0, 2, 'Sem resultados. Experimenta outra palavra.', 7)
        for r in range(min(h, len(res) - top)):
            k = top + r
            a = res[k][2]
            b = D.find('\n', a)
            ps = D[a:b].split('|')
            y = (2 + r) * P.E['lh']
            if k == sel:
                P.rect(0, y, P.E['W'] - 5, P.E['lh'], 8)
            P.put(0, 2 + r, ps[0], 2)
            P.put(2, 2 + r, U.clip(ps[2], U.cols() - 3), 0)
        U.bar(top, h, len(res), 2)
        U.foot('enter: abrir \u00b7 tab: filtro \u00b7 esc: voltar')
        P.show()
        k = P.key()
        if k == 'esc':
            ST['q'] = q
            return None
        if k == 'enter':
            if res:
                ST['q'] = q
                a = res[sel][2]
                ps = D[a:D.find('\n', a)].split('|')
                return ps[0] + ':' + ps[4]
        elif k == 'up':
            sel = max(0, sel - 1)
        elif k == 'down':
            sel = min(len(res) - 1, sel + 1)
        elif k == 'tab':
            flt = (flt + 1) % 3
            ST['qf'] = flt
        elif k == 'del':
            q = q[:-1]
            sel = 0
        elif k == 'clear':
            q = ''
            sel = 0
        elif len(k) == 1 and k >= ' ' and len(q) < 30:
            q = q + k
            sel = 0
            top = 0
