# m1_nav.py - M1TR4M: ecras de consulta carregados a pedido: escolha de
# disciplina e de tema, formulario, exemplos resolvidos, resumo,
# catalogo de calculadoras, historico de resultados e constantes.

import m1_nucleo as N
import m1_ui as U
import m1_cont as C
import m1_app as A

S = A.S
th = A.th
DN = A.DN
NIV = A.NIV
calc = A.calc
cname = A.cname
calcs = A.calcs
tool = A.tool
K = A.K


def pick():
    # Escolhe disciplina e tema; devolve o indice do tema ou -1.
    d = pick_disc()
    return pick_theme(d) if d else -1


def pick_disc():
    r = U.menu('Disciplina', [DN['F'], DN['M']])
    return ('F', 'M')[r] if r >= 0 else ''


def pick_theme(d):
    # Com mais de um grupo (Quimica, Fisica...; 7.o, 8.o... ano), escolhe
    # primeiro o grupo.
    gs = A.grupos(d)
    if not gs:
        U.msg(DN[d], 'Esta edi\u00e7\u00e3o n\u00e3o tem temas de ' + DN[d] + '.')
        return -1
    while True:
        g = 0
        if len(gs) > 1:
            g = U.menu(DN[d], [x[1] for x in gs])
            if g < 0:
                return -1
        ts = gs[g][2]
        r = U.menu(gs[g][1], [th(i)[3] for i in ts])
        if r >= 0:
            return ts[r]
        if len(gs) == 1:
            return -1


def ex_menu(i):
    r = U.menu(th(i)[3], ['Treino (um exerc\u00edcio de cada vez)',
                          'Teste do cap\u00edtulo'])
    if r == 0:
        tool('m1_ex', 'train', i)
    elif r == 1:
        tool('m1_ex', 'test', i)


def flist(i):
    # Formulas do tema: lista de (campos, titulo da licao).
    D = C.get('p', th(i)[4]).D
    ls = C.recs(D, 'L')
    out = []
    for f, pos in C.recs(D, 'F'):
        lt = ''
        for h, p in ls:
            if p < pos:
                lt = h[1]
        out.append((f, lt))
    return out


def formulas(i):
    fs = flist(i)
    if not fs:
        U.msg('Formul\u00e1rio', 'Este tema n\u00e3o tem f\u00f3rmulas.')
        return
    sel = 0
    while True:
        S['where'] = 'formul\u00e1rio'
        r = U.menu('Formul\u00e1rio \u00b7 ' + th(i)[3], [f[0][0] for f in fs], sel)
        if r < 0:
            return
        sel = r
        fshow(i, r, fs)


def fshow(i, k, fs=None):
    # Mostra a formula k do tema i (com a licao e a calculadora ligadas).
    if fs is None:
        fs = flist(i)
    f, lt = fs[k]
    s = C.ftext(f) + '\nLi\u00e7\u00e3o: ' + lt
    cid = f[5] if len(f) > 5 else ''
    if cid:
        s = s + '\nCalculadora: ' + cname(cid) + ' (tecla c)'
    if U.text('F\u00f3rmula', s, '', '', ('c',) if cid else ()) == 'c':
        calc(cid)


def examples(i):
    D = C.get('p', th(i)[4]).D
    es = C.recs(D, 'E')
    D = None
    if not es:
        U.msg('Exemplos', 'Este tema n\u00e3o tem exemplos.')
        return
    sel = 0
    while True:
        S['where'] = 'exemplos'
        r = U.menu('Exemplos \u00b7 ' + th(i)[3],
                   [NIV[int(e[0][0])] + ': ' + e[0][2] for e in es], sel)
        if r < 0:
            return
        sel = r
        eshow(i, r)


def eshow(i, k):
    # Mostra o exemplo resolvido k do tema i.
    D = C.get('p', th(i)[4]).D
    h, pos = C.recs(D, 'E')[k]
    b = C.body(D, pos)
    D = None
    cid = h[3] if len(h) > 3 else ''
    if U.text(NIV[int(h[0])] + ': ' + h[2], b, 'c: calculadora' if cid
              else '', '', ('c',) if cid else ()) == 'c':
        calc(cid)


def summary(i):
    D = C.get('p', th(i)[4]).D
    o = []
    for h, pos in C.recs(D, 'L'):
        d = C.parts(C.body(D, pos))
        if d.get('I'):
            o.append('# ' + h[1])
            o.append(d['I'])
            o.append('')
    D = None
    U.text('Resumo \u00b7 ' + th(i)[3], '\n'.join(o))


def calc_menu(d):
    ds = (('F', DN['F']), ('M', DN['M']), ('C', 'Comuns'))
    while True:
        S['where'] = 'calculadoras'
        r = U.menu('Calculadoras', [x[1] for x in ds] +
                   ['Hist\u00f3rico (\u00faltimos 5)'])
        if r < 0:
            return
        if r == 3:
            hist()
            continue
        cs = [c for c in calcs() if c[2] == ds[r][0]]
        gs = []
        for g in A.grupos(ds[r][0]):
            # pela ordem dos temas do grupo (Numeros, Algebra...)
            ids = [c[0] for i in g[2] for c in cs if c[3] == th(i)[0]]
            if ids:
                gs.append((g[1], ids))
        if not cs:
            U.msg(ds[r][1], 'Esta edi\u00e7\u00e3o n\u00e3o tem calculadoras de ' +
                  ds[r][1] + '.')
            continue
        if not gs:
            calc_list([c[0] for c in cs], ds[r][1])
            continue
        s = 0
        while True:
            q = U.menu(ds[r][1], [g[0] for g in gs], s)
            if q < 0:
                break
            s = q
            calc_list(gs[q][1], gs[q][0])


def calc_list(ids, t):
    names = [cname(c) for c in ids]
    sel = 0
    while True:
        r = U.menu(t, names, sel)
        if r < 0:
            return
        sel = r
        calc(ids[r])


def hist():
    h = S['h']
    if not h:
        U.msg('Hist\u00f3rico', 'Ainda n\u00e3o h\u00e1 resultados.')
        return
    r = U.menu('Hist\u00f3rico', [x[0] + ' = ' + N.fmt(x[1]) + ' ' + x[2]
                                for x in h], 0,
               'enter: usar como ans \u00b7 esc')
    if r >= 0:
        N.CF['ans'] = h[r][1]
        U.msg('Hist\u00f3rico', 'Escreve ans num campo para usar ' +
              N.fmt(h[r][1]) + '.')


def consts():
    r = U.menu('Constantes e unidades', ['Constantes e dados',
                                         'Conversor de unidades',
                                         'Prefixos do SI'])
    if r >= 0:
        calc(('c_comd.cte', 'c_comu.uni', 'c_comu.pre')[r])
