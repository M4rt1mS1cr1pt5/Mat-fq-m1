# m1_ex.py - M1TR4M: exercicios (treino), teste do capitulo, revisao
# rapida (resumos e cartoes) e "O meu progresso". Carregado a pedido.
# Progresso: um numero por exercicio (0 por fazer, 1 errado, 2 certo).
# O teste diz quantas respostas estao certas, nunca que o aluno "domina".

import m1_plat as P
import m1_nucleo as N
import m1_ui as U
import m1_cont as C
import m1_app as A

VER = 1
TIPO = {'m': 'Escolha m\u00faltipla', 'n': 'Num\u00e9rico',
        'u': 'Num\u00e9rico com unidade', 'v': 'Verdadeiro ou falso'}
MARCA = ('\u00b7', '\u2717', '\u2713')
SEM = [1]


def rnd(n):
    # Gerador simples (congruencial); a semente vem de get_time_ms.
    SEM[0] = (SEM[0] * 1103515245 + 12345) % 2147483648
    return SEM[0] % n


def baralha(lst):
    SEM[0] = P.ms() % 2147483648 or 7
    for i in range(len(lst) - 1, 0, -1):
        j = rnd(i + 1)
        lst[i], lst[j] = lst[j], lst[i]
    return lst


def load(ti):
    # Exercicios do tema: lista de dicionarios.
    t = A.th(ti)
    D = C.get('p', t[5]).D
    out = []
    for h, pos in C.recs(D, 'X'):
        d = C.parts(C.body(D, pos))
        d['h'] = h
        out.append(d)
    return out


def first(x):
    # Primeira linha do enunciado (para as listas de exercicios).
    t = x.get('T', '').split('\n')[0]
    return t if t else TIPO[x['h'][0]]


def state(gi):
    return A.S['ex'][gi] if gi < len(A.S['ex']) else 0


def setst(gi, ok):
    if gi < len(A.S['ex']):
        if ok:
            A.S['ex'][gi] = 2
        elif A.S['ex'][gi] != 2:
            A.S['ex'][gi] = 1

# ------------------------------------------------------------ uma pergunta


def ask(x, t, n, k, test=0):
    # Mostra a pergunta e le a resposta. Devolve True/False (certo ou
    # errado) ou None (esc: nao respondida).
    h = x['h']
    tp = h[0]
    head = t + ' \u00b7 ' + str(k + 1) + '/' + str(n)
    txt = x.get('T', '')
    if tp in 'mv':
        ops = x.get('O', '').split('|') if tp == 'm' else \
            ['Verdadeiro', 'Falso']
        s = txt + '\n'
        for i in range(len(ops)):
            s = s + '\n' + str(i + 1) + ') ' + ops[i]
        while True:
            r = U.text(head, s, 'n\u00famero: responder', '',
                       tuple([str(i + 1) for i in range(len(ops))]))
            if r == 'esc':
                return None
            if r in '1234' and r:
                sol = x.get('S', '').strip()
                if tp == 'v':
                    sol = '1' if sol == 'V' else '2'
                return r == sol
    if tp == 'n':
        while True:
            a = U.edit(head, txt, '', 'Escreve o n\u00famero (aceita 2,5, 1/2, '
                       '5e-1). esc: ' + ('passar' if test else 'voltar'))
            if a is None:
                return None
            try:
                return N.check(a, N.num(x['S'])[0], h[3], A.TOL[A.S['cfg'][6]])
            except ValueError as e:
                U.msg(head, U.ERS + str(e), 5)
    us = h[4].split(' ')
    fs = [N.fld('Valor', '', ''), N.fld('Unidade', '', '', 'c', us)]
    while True:
        if U.text(head, txt + '\n\nenter: responder (valor e unidade)', '',
                  '', ('enter',)) == 'esc':
            return None
        if not U.form(head, fs):
            return None
        try:
            v = N.num(fs[0][2])[0]
            v = N.conv(v, us[fs[1][3]], us[0])
            return N.check(v, N.num(x['S'])[0], h[3], A.TOL[A.S['cfg'][6]])
        except ValueError as e:
            fs[0][5] = str(e)


def show_sol(x, t):
    s = x.get('D', '')
    h = x['h']
    if h[0] == 'm':
        ops = x.get('O', '').split('|')
        k = int(x['S']) - 1
        s = 'Resposta: ' + str(k + 1) + ') ' + ops[k] + '\n\n' + s
    elif h[0] == 'v':
        s = 'Resposta: ' + ('Verdadeiro' if x['S'].strip() == 'V' else
                            'Falso') + '\n\n' + s
    else:
        s = 'Resposta: ' + x['S'].strip() + (' ' + h[4].split(' ')[0]
                                              if h[0] == 'u' else '') + \
            '\n\n' + s
    U.text('Resolu\u00e7\u00e3o \u00b7 ' + t, s)

# ------------------------------------------------------------ treino


def train(ti):
    t = A.th(ti)
    if not t[5]:
        U.msg('Exerc\u00edcios', 'Este tema n\u00e3o tem exerc\u00edcios.')
        return
    off = int(t[9]) + 1
    sel = 0
    while True:
        xs = load(ti)
        it = []
        for i in range(len(xs)):
            st = state(off + i)
            it.append(MARCA[st] + ' ' + first(xs[i]))
        A.S['where'] = 'treino ' + t[0]
        r = U.menu('Treino \u00b7 ' + t[3], it, sel,
                   '\u2713 certo \u00b7 \u2717 errado \u00b7 \u00b7 por fazer \u00b7 esc')
        if r < 0:
            A.save('m1prog')
            return
        x = xs[r]
        xs = None
        while True:
            ok = ask(x, t[3], len(it), r)
            if ok is None:
                break
            setst(off + r, ok)
            if ok:
                k = U.text(t[3], '+ ' + U.OKS + 'Certo!\n\n1: ver a resolu\u00e7\u00e3o '
                           '\u00b7 enter: seguinte', '', '', ('1',))
                if k == '1':
                    show_sol(x, t[3])
                break
            k = U.text(t[3], '! ' + U.ERS + 'Ainda n\u00e3o est\u00e1 certo.\n\n'
                       '1: tentar outra vez\n2: ver a pista\n'
                       '3: ver a resolu\u00e7\u00e3o\n4: ir \u00e0 li\u00e7\u00e3o',
                       '', '', ('1', '2', '3', '4'))
            if k == '2':
                U.text('Pista', x.get('P', ''))
                continue
            if k == '3':
                show_sol(x, t[3])
                break
            if k == '4':
                A.save('m1prog')
                A.goto_lesson(x['h'][2])
                break
            if k != '1':
                break
        A.save('m1prog')
        sel = min(r + 1, len(it) - 1)

def one(a):
    # Um exercicio aberto a partir da pesquisa: (tema, indice).
    ti, k = a
    t = A.th(ti)
    x = load(ti)[k]
    while True:
        ok = ask(x, t[3], int(t[8]), k)
        if ok is None:
            break
        setst(int(t[9]) + 1 + k, ok)
        A.save('m1prog')
        if U.text(t[3], ('+ ' + U.OKS + 'Certo!' if ok else '! ' + U.ERS +
                         'Ainda n\u00e3o est\u00e1 certo.') + '\n\n1: ver a '
                  'resolu\u00e7\u00e3o \u00b7 2: tentar outra vez', '', '',
                  ('1', '2')) == '1':
            show_sol(x, t[3])
            break
        if ok:
            break

# ------------------------------------------------------------ teste


def test(ti):
    t = A.th(ti)
    if not t[5]:
        U.msg('Teste', 'Este tema n\u00e3o tem exerc\u00edcios.')
        return
    off = int(t[9]) + 1
    xs = load(ti)
    n = len(xs)
    order = baralha(list(range(n)))
    res = [None] * n
    A.S['where'] = 'teste ' + t[0]
    if not U.ask('Teste do cap\u00edtulo', str(n) + ' perguntas por ordem '
                 'baralhada. esc numa pergunta deixa-a sem resposta. '
                 'Come\u00e7ar?', 1):
        return
    for k in range(n):
        i = order[k]
        r = ask(xs[i], t[3], n, k, 1)
        res[i] = r
        if r is not None:
            setst(off + i, r)
    A.save('m1prog')
    c = len([r for r in res if r])
    A.S['tst'][1 + 2 * ti] = c
    A.S['tst'][2 + 2 * ti] = n
    A.save('m1tst')
    sel = 0
    while True:
        it = []
        for k in range(n):
            i = order[k]
            r = res[i]
            m = '\u2014' if r is None else (U.OKS if r else U.ERS)
            it.append(m + first(xs[i]))
        r = U.menu(str(c) + ' de ' + str(n) + ' certas', it, sel,
                   'enter: ver a resolu\u00e7\u00e3o \u00b7 esc: sair')
        if r < 0:
            break
        sel = r
        show_sol(xs[order[r]], t[3])
    U.msg('Teste do cap\u00edtulo', str(c) + ' de ' + str(n) + ' certas.\n\n'
          'O resultado diz respeito s\u00f3 a estas perguntas.')

# ------------------------------------------------------------ revisao


def cards(ti):
    # Cartoes do tema: (frente, verso). Formulas e exercicios J.
    t = A.th(ti)
    D = C.get('p', t[4]).D
    out = []
    for f, pos in C.recs(D, 'F'):
        out.append(('F\u00f3rmula: ' + f[0] + '\n\n(enter: ver)',
                    '= ' + f[1] + ('\n- ' + '\n- '.join(f[2].split(';'))
                                   if len(f) > 2 and f[2] else '')))
    for h, pos in C.recs(D, 'L'):
        d = C.parts(C.body(D, pos))
        if d.get('J'):
            out.append((h[1] + '\n\n' + d['J'] + '\n\n(enter: ver)',
                        d.get('R', '')))
    return out


def review(ti):
    r = U.menu('Revis\u00e3o r\u00e1pida \u00b7 ' + A.th(ti)[3],
               ['Resumos (p\u00e1ginas I)', 'Cart\u00f5es pergunta-resposta'])
    if r == 0:
        A.nav('summary', ti)
    elif r == 1:
        flash(ti)


def flash(ti):
    # Tres caixas de repeticao: os cartoes da caixa 1 aparecem mais vezes.
    t = A.th(ti)
    off = int(t[11]) + 1
    cs = cards(ti)
    if not cs:
        U.msg('Cart\u00f5es', 'Este tema n\u00e3o tem cart\u00f5es.')
        return
    rv = A.S['rev']
    SEM[0] = P.ms() % 2147483648 or 7
    pool = []
    for i in range(len(cs)):
        b = rv[off + i] if off + i < len(rv) else 0
        pool = pool + [i] * (3 - min(2, max(0, b - 1)))
    feitos = 0
    while feitos < 10 and pool:
        i = pool[rnd(len(pool))]
        f, v = cs[i]
        k = U.text('Cart\u00e3o ' + str(feitos + 1) + '/10', f)
        if k == 'esc':
            break
        k = U.text('Cart\u00e3o \u00b7 verso', v + '\n\n1: sabia \u00b7 2: n\u00e3o sabia',
                   '', '', ('1', '2'))
        if k == 'esc':
            break
        if off + i < len(rv):
            b = max(1, rv[off + i])
            rv[off + i] = min(3, b + 1) if k == '1' else 1
        pool = [j for j in pool if j != i] + ([i] if k != '1' else [])
        feitos += 1
    A.save('m1rev')

# ------------------------------------------------------------ progresso


def progress():
    while True:
        A.S['where'] = 'progresso'
        r = U.menu('O meu progresso', ['Continuar onde fiquei',
                                       'Por tema', 'Temas a rever',
                                       'Apagar o progresso'])
        if r < 0:
            return
        if r == 0:
            p = A.S['pos']
            if p[1] == 1:
                A.open_lesson(p[2], p[3], p[4])
            else:
                U.msg('Continuar', 'Ainda n\u00e3o abriste nenhuma li\u00e7\u00e3o.')
        elif r == 1:
            bytheme()
        elif r == 2:
            torev()
        else:
            A.wipe()


def stats(i):
    t = A.th(i)
    nl = int(t[6])
    ol = int(t[7]) + 1
    vl = len([k for k in range(nl) if A.S['lic'][ol + k]])
    ne = int(t[8])
    oe = int(t[9]) + 1
    sts = [state(oe + k) for k in range(ne)]
    return vl, nl, len([s for s in sts if s]), len([s for s in sts if s == 2]), \
        ne, A.S['tst'][1 + 2 * i], A.S['tst'][2 + 2 * i]


def bytheme():
    o = []
    for i in range(len(A.K.TEMAS)):
        vl, nl, f, c, ne, tc, tn = stats(i)
        o.append('# ' + A.th(i)[3])
        s = 'Li\u00e7\u00f5es vistas: ' + str(vl) + '/' + str(nl)
        if ne:
            s = s + '\nExerc\u00edcios: ' + str(f) + '/' + str(ne) + \
                ' feitos, ' + str(c) + ' certos'
        if tn:
            s = s + '\n\u00daltimo teste: ' + str(tc) + ' de ' + str(tn) + \
                ' certas'
        o.append(s)
    U.text('Progresso por tema', '\n'.join(o))


def torev():
    o = []
    for i in range(len(A.K.TEMAS)):
        vl, nl, f, c, ne, tc, tn = stats(i)
        if f and (f - c) * 2 >= f:
            o.append('- ' + A.th(i)[3] + ' (' + str(f - c) + ' de ' + str(f) +
                     ' errados)')
    U.text('Temas a rever', '\n'.join(o) if o else
           'Nenhum tema tem metade ou mais dos exerc\u00edcios errados.')
