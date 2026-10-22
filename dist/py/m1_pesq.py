# m1_pesq.py - M1TR4M: pesquisa global. Carregado a pedido; o indice
# (gerado pelo build em partes de 30 KB no maximo, por disciplina: lista
# em m1_cat.IDX) so esta em memoria durante a pesquisa: o filtro "tudo"
# carrega todas as partes, "FQ" e "Mat" so as suas. Os resultados
# aparecem a cada tecla e ignoram acentos e maiusculas. Ordem: titulo igual, titulo que comeca pela pesquisa,
# palavra do titulo, palavras-chave. Maximo de 60 resultados.

import m1_plat as P
import m1_ui as U
import m1_cont as C
import m1_app as A
import m1_cat as K

VER = 2
# Pares de um so caracter (o texto dobrado tem o mesmo comprimento).
FOLD = ('\u00e1a\u00e0a\u00e2a\u00e3a\u00e9e\u00eae\u00e8e\u00edi\u00f3o\u00f4o\u00f5o'
        '\u00fau\u00fcu\u00e7c\u00c1a\u00c0a\u00c2a\u00c3a\u00c9e\u00cae\u00cdi\u00d3o'
        '\u00d4o\u00d5o\u00dau\u00c7c\u03c0p\u221av\u00b2 \u00b3 \u00b7 \u00ba \u00aa ')
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


def find(L, q, k, res):
    # Procura q no indice dobrado L (numero k) e junta a res os
    # resultados (ordem, titulo, k, posicao). Linha: TAG|titulo|palavras|alvo.
    i = L.find(q)
    while i >= 0 and len(res) < 200:
        a = L.rfind('\n', 0, i) + 1
        b = L.find('\n', i)
        if b < 0:
            b = len(L)
        ps = L[a:b].split('|')
        if len(ps) < 4 or ps[0].startswith('@'):
            i = L.find(q, b)
            continue
        t0 = a + len(ps[0]) + 1
        if not (t0 <= i < t0 + len(ps[1]) + 1 + len(ps[2])):
            i = L.find(q, i + 1)
            continue
        tl = ps[1]
        if tl == q:
            r = 0
        elif tl.startswith(q):
            r = 1
        elif (' ' + q) in (' ' + tl):
            r = 2
        elif q in tl:
            r = 3
        elif (' ' + q) in (' ' + ps[2]):
            r = 4
        else:
            r = 5
        res.append((r, tl, k, a))
        i = L.find(q, b)
    return res


def parts():
    return [x.split(':') for x in K.IDX.split()]


def load(flt):
    # Partes do indice do filtro: [(k, D, D dobrado)]; liberta as outras.
    ix = []
    for k, (nm, d) in enumerate(parts()):
        sl = 'i' + str(k)
        if flt == 0 or FILT[flt][0] == d:
            if C.SL.get(sl, [0, ''])[1] != nm:
                U.busy('A abrir o \u00edndice\u2026')
            D = C.get(sl, nm).D
            ix.append((k, D, fold(D)))
        else:
            C.drop(sl)
    return ix


def free():
    for k in range(len(parts())):
        C.drop('i' + str(k))


def run():
    # Devolve o alvo escolhido ("L:q1a", "C:c_fqat.mm"...) ou None.
    q = ST.get('q', '')
    flt = ST.get('qf', 0)
    mn = ST.get('qmin', 1)
    sel = 0
    top = 0
    C.drop('p')
    ix = load(flt)
    Ds = {}
    for k, D, L in ix:
        Ds[k] = D
    h = U.body() - 1
    while True:
        A.S['where'] = 'pesquisa'
        t0 = P.ms()
        fq = fold(q.strip())
        res = []
        if len(fq) >= mn:
            for k, D, L in ix:
                find(L, fq, k, res)
            res.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
            res = res[:MAXR]
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
            D = Ds[res[k][2]]
            a = res[k][3]
            ps = D[a:D.find('\n', a)].split('|')
            y = (2 + r) * P.E['lh']
            if k == sel:
                P.rect(0, y, P.E['W'] - 5, P.E['lh'], 8)
            P.put(0, 2 + r, ps[0], 2)
            P.put(2, 2 + r, U.clip(ps[1], U.cols() - 3), 0)
        U.bar(top, h, len(res), 2)
        U.foot('enter: abrir \u00b7 tab: filtro \u00b7 esc: voltar')
        P.show()
        k = P.key()
        if k == 'esc':
            ST['q'] = q
            free()
            return None
        if k == 'enter':
            if res:
                ST['q'] = q
                D = Ds[res[sel][2]]
                a = res[sel][3]
                ps = D[a:D.find('\n', a)].split('|')
                free()
                return ps[0] + ':' + ps[3]
        elif k == 'up':
            sel = max(0, sel - 1)
        elif k == 'down':
            sel = min(len(res) - 1, sel + 1)
        elif k == 'tab':
            flt = (flt + 1) % 3
            ST['qf'] = flt
            ix = None
            Ds = {}
            ix = load(flt)
            for k, D, L in ix:
                Ds[k] = D
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
