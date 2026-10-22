# m1_app.py - M1TR4M: navegacao, definicoes, catalogo e motor das
# calculadoras. Ecra inicial, menu principal (13 opcoes), menus de cada
# tema, licoes, formulario, exemplos, calculadoras do tema e resumo.
# As partes grandes que so se usam as vezes vivem em modulos carregados
# a pedido: m1_ex (exercicios, testes, revisao, progresso), m1_cfg
# (definicoes, ajuda, diagnostico), m1_pesq (pesquisa) e m1_tp (tabela
# periodica).

import m1_plat as P
import m1_nucleo as N
import m1_ui as U
import m1_cont as C
import m1_cat as K

VER = 1
APPV = '1.0'
# Estado da sessao: definicoes, progresso, historico de resultados,
# ultimos valores de cada calculadora e ecra atual (para os erros).
S = {'cfg': None, 'ex': None, 'lic': None, 'tst': None, 'rev': None,
     'pos': None, 'h': [], 'vals': {}, 'f0': -1, 'where': 'arranque',
     'gv': True, 'aviso': 0, 'imp': '', 'mods': ''}
# Definicoes (lista "m1def"): versao, casas decimais, alg. sig. auto,
# expoente da notacao cientifica, angulo (0 graus), g (indice em GV),
# tolerancia (indice em TOL), simbolos (2/1/0), cw, lh, dy.
DEF = [1, 4, 1, 6, 0, 0, 0, 2, 7, 17, 13]
GV = (9.8, 10.0, 9.80665)
GT = ('9,8 m s\u207b\u00b2 (manual)', '10 m s\u207b\u00b2 (exame)',
      '9,80665 m s\u207b\u00b2 (padr\u00e3o)')
TOL = (0.001, 0.01, 0.0001)
TT = ('0,1 %', '1 %', '0,01 %')
NIV = ('', 'B\u00e1sico', 'Interm\u00e9dio', 'Avan\u00e7ado')
GR = (('F', 'q', 'Qu\u00edmica'), ('F', 'f', 'F\u00edsica'),
      ('F', 'a', 'Atividades laboratoriais'),
      ('F', 'r', 'Revis\u00f5es do 7.\u00ba ao 9.\u00ba ano'),
      ('M', 't', 'Temas do 10.\u00ba ano'),
      ('M', 'r', 'Revis\u00f5es do 3.\u00ba ciclo'))
DN = {'F': 'F\u00edsica e Qu\u00edmica A', 'M': 'Matem\u00e1tica A',
      'C': 'Comuns'}

# ------------------------------------------------------------ estado


def _ld(nm, n, fill=0):
    # Le uma lista guardada; se nao existir ou for de outra versao,
    # comeca vazia. Ajusta o tamanho ao catalogo atual.
    v = P.load(nm)
    ok = v is not None and len(v) >= 1
    if ok:
        try:
            v = [int(x) for x in v]
            ok = v[0] == 1
        except Exception:
            ok = False
    if not ok:
        if v is None and nm == 'm1def':
            S['gv'] = P.save('m1t', [1])
        v = [1]
    v = v[:n + 1]
    while len(v) < n + 1:
        v.append(fill)
    return v


def load_state():
    c = _ld('m1def', len(DEF) - 1)
    if len(c) != len(DEF) or c[1] == 0 and c[8] == 0:
        c = list(DEF)
    S['cfg'] = c
    S['ex'] = _ld('m1prog', K.NEX)
    S['lic'] = _ld('m1lic', K.NLIC)
    S['tst'] = _ld('m1tst', 2 * len(K.TEMAS))
    S['rev'] = _ld('m1rev', K.NCART)
    S['pos'] = _ld('m1pos', 4)
    apply_cfg()


def apply_cfg():
    c = S['cfg']
    N.CF['dec'] = c[1]
    N.CF['sci'] = c[3]
    N.CF['ang'] = c[4]
    N.CF['sfa'] = c[2]
    N.CF['g'] = GV[c[5]]
    P.E['sym'] = c[7]
    P.metrics(c[8], c[9], c[10])


def save(nm):
    # Guarda uma das listas; avisa uma vez se a gravacao nao funcionar.
    key = {'m1def': 'cfg', 'm1prog': 'ex', 'm1lic': 'lic', 'm1tst': 'tst',
           'm1rev': 'rev', 'm1pos': 'pos'}[nm]
    if not P.save(nm, S[key]) and not S['aviso']:
        S['aviso'] = 1
        U.msg('Gravar', 'N\u00e3o foi poss\u00edvel guardar dados neste '
              'aparelho. A app funciona, mas o progresso n\u00e3o fica '
              'guardado.', 5)


def wipe():
    if U.ask('Apagar o progresso', 'Apagar li\u00e7\u00f5es vistas, exerc\u00edcios, '
             'testes e cart\u00f5es? N\u00e3o d\u00e1 para desfazer.'):
        for k in ('ex', 'lic', 'tst', 'rev', 'pos'):
            v = S[k]
            for j in range(1, len(v)):
                v[j] = 0
        for nm in ('m1prog', 'm1lic', 'm1tst', 'm1rev', 'm1pos'):
            save(nm)
        U.msg('Progresso', 'Progresso apagado. Grava o documento (ctrl+S).')


def g():
    # Valor de g escolhido nas Definicoes.
    return GV[S['cfg'][5]]


def sfa():
    return S['cfg'][2]

# ------------------------------------------------------------ catalogo


def th(i):
    # Campos de um tema: id, disc, grupo, titulo, pacote p, pacote x,
    # n licoes, 1.a licao, n exercicios, 1.o exercicio, n cartoes,
    # 1.o cartao, calculadoras.
    return K.TEMAS[i].split('|')


def tfind(tid):
    for i in range(len(K.TEMAS)):
        if K.TEMAS[i].startswith(tid + '|'):
            return i
    return -1


def calcs():
    # Catalogo das calculadoras: [id, nome, palavras, disciplina, tema].
    return [ln.split('|') for ln in K.CALC.split('\n') if ln]


def cname(cid):
    for c in calcs():
        if c[0] == cid:
            return c[1]
    return cid

# ------------------------------------------------------------ menus


def main_menu():
    it = ('F\u00edsica e Qu\u00edmica A', 'Matem\u00e1tica A', 'Pesquisa global',
          'Calculadoras', 'Tabela peri\u00f3dica', 'Formul\u00e1rio',
          'Constantes e unidades', 'Exemplos resolvidos',
          'Exerc\u00edcios e testes', 'O meu progresso', 'Revis\u00e3o r\u00e1pida',
          'Defini\u00e7\u00f5es, ajuda e Diagn\u00f3stico', 'Sair')
    sel = 0
    while True:
        S['where'] = 'menu principal'
        r = U.menu('M1TR4M \u00b7 FQ e Mat 10.\u00ba', it, sel)
        if r < 0 or r == 12:
            if U.ask('Sair', 'Sair da M1TR4M?', 1):
                return
            continue
        sel = r
        if r == 0:
            disc('F')
        elif r == 1:
            disc('M')
        elif r == 2:
            search()
        elif r == 3:
            calc_menu('')
        elif r == 4:
            C.get('p', 'm1_tp').run()
        elif r in (5, 7, 8, 10):
            d = pick_disc()
            if d:
                i = pick_theme(d)
                if i >= 0:
                    if r == 5:
                        formulas(i)
                    elif r == 7:
                        examples(i)
                    elif r == 8:
                        ex_menu(i)
                    else:
                        tool('m1_ex', 'review', i)
        elif r == 6:
            consts()
        elif r == 9:
            tool('m1_ex', 'progress')
        elif r == 11:
            tool('m1_cfg')


def tool(nm, fn='run', a=None):
    m = C.get('f', nm)
    f = getattr(m, fn)
    if a is None:
        f()
    else:
        f(a)


def search():
    # A pesquisa devolve o alvo; abre-se aqui, depois de libertar o
    # indice, e volta-se a pesquisa com o texto que o aluno escreveu.
    while True:
        t = C.get('f', 'm1_pesq').run()
        C.drop('f')
        C.drop('p')
        if not t:
            return
        go(t)


def go(t):
    k = t[0]
    v = t[2:]
    if k == 'L':
        goto_lesson(v)
    elif k == 'C':
        calc(v)
    elif k == 'T':
        C.get('p', 'm1_tp').sheet(int(v))
    elif k == 'K':
        calc('c_comd.cte')
    else:
        tid, n = v.split(':')
        i = tfind(tid)
        if k == 'F':
            fshow(i, int(n))
        elif k == 'E':
            eshow(i, int(n))
        else:
            tool('m1_ex', 'one', (i, int(n)))


def pick_disc():
    r = U.menu('Disciplina', [DN['F'], DN['M']])
    return ('F', 'M')[r] if r >= 0 else ''


def pick_theme(d):
    ts = [i for i in range(len(K.TEMAS)) if th(i)[1] == d]
    r = U.menu(DN[d], [th(i)[3] for i in ts])
    return ts[r] if r >= 0 else -1


def disc(d):
    gs = [x for x in GR if x[0] == d]
    sel = 0
    while True:
        S['where'] = DN[d]
        r = U.menu(DN[d], [x[2] for x in gs], sel)
        if r < 0:
            return
        sel = r
        ts = [i for i in range(len(K.TEMAS))
              if th(i)[1] == d and th(i)[2] == gs[r][1]]
        s2 = 0
        while True:
            q = U.menu(gs[r][2], [th(i)[3] for i in ts], s2)
            if q < 0:
                break
            s2 = q
            theme(ts[q])


def theme(i):
    t = th(i)
    S['where'] = t[3]
    D = C.get('p', t[4]).D
    acts = [('Li\u00e7\u00f5es', 0)]
    if '\n@F ' in D:
        acts.append(('Formul\u00e1rio do tema', 1))
    if '\n@E ' in D:
        acts.append(('Exemplos', 2))
    if t[5]:
        acts.append(('Exerc\u00edcios', 3))
        acts.append(('Teste do cap\u00edtulo', 4))
    if t[12]:
        acts.append(('Calculadoras do tema', 5))
    if '\n@I' in D:
        acts.append(('Resumo', 6))
    D = None
    sel = 0
    while True:
        r = U.menu(t[3], [a[0] for a in acts], sel)
        if r < 0:
            return
        sel = r
        a = acts[r][1]
        if a == 0:
            lessons(i)
        elif a == 1:
            formulas(i)
        elif a == 2:
            examples(i)
        elif a == 3:
            tool('m1_ex', 'train', i)
        elif a == 4:
            tool('m1_ex', 'test', i)
        elif a == 5:
            calc_list(t[12].split(' '), t[3])
        else:
            summary(i)


def ex_menu(i):
    r = U.menu(th(i)[3], ['Treino (um exerc\u00edcio de cada vez)',
                          'Teste do cap\u00edtulo'])
    if r == 0:
        tool('m1_ex', 'train', i)
    elif r == 1:
        tool('m1_ex', 'test', i)

# ------------------------------------------------------------ licoes


def lessons(i):
    t = th(i)
    sel = 0
    while True:
        D = C.get('p', t[4]).D
        hs = [h[0] for h in C.recs(D, 'L')]
        D = None
        o = int(t[7])
        it = []
        for k in range(len(hs)):
            v = S['lic'][o + k + 1] if o + k + 1 < len(S['lic']) else 0
            it.append(('\u2713 ' if v else '\u00b7 ') + hs[k][1])
        r = U.menu(t[3], it, sel, 'enter: abrir \u00b7 \u2713 j\u00e1 vista \u00b7 esc')
        if r < 0:
            return
        sel = r
        open_lesson(i, r)


def open_lesson(i, k, pg=-1):
    # Abre a licao k do tema i na pagina onde o aluno ficou.
    t = th(i)
    gi = int(t[7]) + k + 1
    D = C.get('p', t[4]).D
    hs = C.recs(D, 'L')
    if k >= len(hs):
        return
    h, pages, ans, fs = C.lesson(D, hs[k][0][0])
    D = None
    S['where'] = 'li\u00e7\u00e3o ' + h[0]
    pages[0] = pages[0] + linfo(h)
    if pg < 0:
        pg = max(0, S['lic'][gi] - 1) if gi < len(S['lic']) else 0
    top = 0
    while True:
        k2, pg, top = U.lesson(h[1], pages, pg, top, ans, h[0],
                               ('c', 'l') if (len(h) > 3 and h[3]) or
                               (len(h) > 7 and (h[6] or h[7])) else ())
        if gi < len(S['lic']):
            S['lic'][gi] = pg + 1
        S['pos'] = [1, 1, i, k, pg]
        if k2 == 'c' and len(h) > 3 and h[3]:
            calc(h[3].split(' ')[0])
        elif k2 == 'l':
            links(h)
        else:
            break
    save('m1lic')
    save('m1pos')


def linfo(h):
    # Informacao da licao no fim da pagina A: nivel, calculadora,
    # pre-requisitos, ligacao a outra disciplina e fonte.
    o = ['']
    if len(h) > 5 and h[5]:
        o.append('N\u00edvel: ' + h[5] + (' \u00b7 ' + h[4] + '.\u00ba ano'
                                          if len(h) > 4 and h[4] else ''))
    if len(h) > 3 and h[3]:
        o.append('Calculadora: ' + cname(h[3].split(' ')[0]) + ' (tecla c)')
    for j, nm in ((6, 'Pr\u00e9-requisitos'), (7, 'Liga\u00e7\u00e3o')):
        if len(h) > j and h[j]:
            o.append(nm + ': ' + ', '.join([x.split(':')[1] for x in
                                            h[j].split(';') if ':' in x]) +
                     ' (tecla l)')
    if len(h) > 8 and h[8]:
        o.append('Fonte: ' + h[8])
    return '\n'.join(o)


def links(h):
    ls = []
    for j in (6, 7):
        if len(h) > j and h[j]:
            ls = ls + [x.split(':') for x in h[j].split(';') if ':' in x]
    if not ls:
        return
    r = U.menu('Li\u00e7\u00f5es ligadas', [x[1] for x in ls])
    if r >= 0:
        goto_lesson(ls[r][0])


def goto_lesson(lid):
    # Abre uma licao pelo identificador (pode ser de outro tema).
    for i in range(len(K.TEMAS)):
        t = th(i)
        if lid in t[13].split(' '):
            open_lesson(i, t[13].split(' ').index(lid))
            return
    U.msg('Li\u00e7\u00e3o', 'Li\u00e7\u00e3o ' + lid + ' n\u00e3o encontrada.', 5)

# ------------------------------------------------------------ formulario


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

# ------------------------------------------------------------ calculadoras


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
        cs = [c for c in calcs() if c[3] == ds[r][0]]
        calc_list([c[0] for c in cs], ds[r][1])


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


def calc(cid):
    # Motor comum: formulario -> validacao -> formula, substituicao e
    # resultado -> opcoes (passos, alterar, novo, usar noutra, grafico).
    # A calculadora devolve (titulo, campos, funcao) ou None (cancelada);
    # sem campos, mostra logo o resultado. A funcao devolve (texto,
    # passos, valor, unidade, grafico) ou None (tratou tudo sozinha).
    mn, fn = cid.split('.')
    sp = getattr(C.get('c', mn), fn)()
    if sp is None:
        return
    t, fs, f = sp
    dflt = [x[2] for x in fs]
    old = S['vals'].get(cid)
    if old and len(old) == len(fs):
        for j in range(len(fs)):
            fs[j][2] = old[j][0]
            fs[j][3] = old[j][1]
    foc = 0
    while True:
        S['where'] = 'calculadora ' + t
        if fs and not U.form(t, fs, foc):
            return
        foc = len(fs) - 1
        v = N.rdf(fs)
        if fs:
            S['vals'][cid] = [(x[2], x[3]) for x in fs]
        if v is None:
            for j in range(len(fs)):
                if fs[j][5]:
                    foc = j
                    break
            continue
        try:
            r = f(v)
        except ValueError as e:
            r = (ERR_ + str(e), '', None)
        except ZeroDivisionError:
            r = (ERR_ + 'Divis\u00e3o por zero: verifica os dados.', '', None)
        except OverflowError:
            r = (ERR_ + 'Valor demasiado grande.', '', None)
        except IndexError:
            r = (ERR_ + 'Faltam dados: verifica as listas.', '', None)
        if r is None:
            return
        if r[0].startswith(ERR_):
            U.msg(t, '! ' + r[0])
            if not fs:
                return
            continue
        if len(r) > 2 and r[2] is not None:
            S['h'].insert(0, (t, r[2], r[3] if len(r) > 3 else ''))
            del S['h'][5:]
            N.CF['ans'] = r[2]
        k = res_menu(t, r)
        if k == '3':
            for j in range(len(fs)):
                fs[j][2] = dflt[j]
            foc = 0
        elif k == '4':
            calc_menu('')
            return
        elif k == 'esc' or not fs:
            return


def res_menu(t, r):
    # Ecra de resultado com as opcoes. Devolve a tecla que o fechou.
    gr = len(r) > 4 and r[4]
    o = '1 passos \u00b7 2 alterar \u00b7 3 novo \u00b7 4 usar'
    if gr:
        o = o + ' \u00b7 5 gr\u00e1fico'
    while True:
        k = U.text(t, r[0], o, '', ('1', '2', '3', '4', '5'))
        if k == '1':
            U.text(t + ' \u00b7 passos', r[1] if len(r) > 1 and r[1] else
                   'Esta calculadora n\u00e3o tem mais passos.')
        elif k == '5' and gr:
            U.graph(*r[4])
        elif k in ('2', '3', '4', 'esc', 'enter'):
            return k


ERR_ = '\u2717 '

# ------------------------------------------------------------ arranque


def splash():
    # Animacao curta (max. 2 s): atomo com orbitas, poligonos e o nome.
    t0 = P.ms()
    W = P.E['W']
    H = P.E['H']
    if not P.E['g']:
        print('M1TR4M \u00b7 F\u00edsica e Qu\u00edmica A \u00b7 Matem\u00e1tica A '
              '\u2014 10.\u00ba ano \u00b7 by M1TR4M')
        return
    import math
    cx = W // 2
    cy = 62
    for fr in range(12):
        P.begin()
        a = fr * 0.5
        for o in range(3):
            pts = []
            for s in range(0, 360, 30):
                r = s * math.pi / 180
                x = 70 * math.cos(r)
                y = 22 * math.sin(r)
                ang = o * math.pi / 3
                pts.append((cx + x * math.cos(ang) - y * math.sin(ang),
                            cy + x * math.sin(ang) + y * math.cos(ang)))
            P.poly([p[0] for p in pts], [p[1] for p in pts], 4)
            r = a + o * 2.1
            x = 70 * math.cos(r)
            y = 22 * math.sin(r)
            ang = o * math.pi / 3
            P.circ(cx + x * math.cos(ang) - y * math.sin(ang),
                   cy + x * math.sin(ang) + y * math.cos(ang), 4, 5, 1)
        P.circ(cx, cy, 9, 2, 1)
        for k in range(3):
            P.poly([18 + k * 8, 40 + k * 8, 29 + k * 8],
                   [190 - k * 30, 190 - k * 30, 170 - k * 30], 6 if k % 2 else 3)
        big('M1TR4M', cx - 84, 104, 4)
        s = 'F\u00edsica e Qu\u00edmica A \u00b7 Matem\u00e1tica A \u2014 10.\u00ba ano'
        P.txt(cx - len(s) * P.E['cw'] // 2, 146, s, 0)
        P.txt(cx - 6 * P.E['cw'] // 2, 166, 'by M1TR4M', 7)
        P.show()
        if P.key(0) or P.ms() - t0 > 1800:
            break


# Letras grandes 5x7 (cada linha e um numero de 5 bits).
BIG = {'M': (17, 27, 21, 21, 17, 17, 17), '1': (4, 12, 4, 4, 4, 4, 14),
       'T': (31, 4, 4, 4, 4, 4, 4), 'R': (30, 17, 17, 30, 20, 18, 17),
       '4': (2, 6, 10, 18, 31, 2, 2)}


def big(s, x, y, k):
    for ch in s:
        rows = BIG.get(ch, ())
        for r in range(len(rows)):
            for c in range(5):
                if rows[r] & (16 >> c):
                    P.rect(x + c * k, y + r * k, k, k, 2)
        x += 6 * k


def run(f0=-1):
    # Ciclo principal com a protecao geral contra erros (seccao 4.7).
    S['f0'] = f0
    P.init()
    load_state()
    splash()
    while True:
        try:
            main_menu()
            break
        except KeyboardInterrupt:
            break
        except MemoryError:
            for sl in ('p', 'c', 'f'):
                C.drop(sl)
            P.collect()
            U.msg('Mem\u00f3ria', 'Faltou mem\u00f3ria em: ' + S['where'] +
                  '. Os pacotes foram libertados; voltas ao menu.', 5)
        except C.Falta as e:
            U.msg('Falta um m\u00f3dulo', str(e), 5)
        except Exception as e:
            U.msg('Erro inesperado', type(e).__name__ + ': ' + str(e) +
                  '\nEcr\u00e3: ' + S['where'] + '\nVoltas ao menu.', 5)
    for sl in ('p', 'c', 'f'):
        C.drop(sl)
    if P.E['g']:
        P.begin()
        U.title('M1TR4M')
        P.put(0, 2, 'At\u00e9 \u00e0 pr\u00f3xima!')
        P.put(0, 4, 'Grava o documento (ctrl+S) para')
        P.put(0, 5, 'guardar o progresso e as defini\u00e7\u00f5es.')
        P.show()
