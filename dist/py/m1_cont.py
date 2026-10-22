# m1_cont.py - M1TR4M: leitor de pacotes.
# Importa um pacote quando o aluno abre um tema e liberta-o quando sai.
# Ha tres ranhuras: 'p' (conteudos: licoes, exercicios, indice, tabela
# periodica), 'c' (calculadoras) e 'f' (ferramentas grandes que so se
# usam as vezes: treino, definicoes, pesquisa). Nunca ha mais de um
# modulo em cada ranhura.
# Formato dos pacotes (seccao 4.3 do prompt): uma unica constante D com
# marcadores de linha "@V versao", "@N numero", "@L licao", "@A".."@J",
# "@R resposta", "@F formula", "@E exemplo", "@X exercicio".

import m1_plat as P

VER = 1
PVER = 1            # versao do formato dos pacotes que este leitor aceita
SL = {'p': [None, ''], 'c': [None, ''], 'f': [None, '']}
SEEN = []           # pacotes carregados quando nao ha sys.modules
WARN = []


class Falta(Exception):
    pass


def drop(slot):
    # Liberta o pacote da ranhura: apaga referencias, tira-o de
    # sys.modules e recolhe o lixo.
    n = SL[slot][1]
    SL[slot] = [None, '']
    if n:
        P.unload(n)
    P.collect()


def get(slot, name):
    # Devolve o modulo "name", carregando-o se for preciso.
    if SL[slot][1] == name and SL[slot][0] is not None:
        return SL[slot][0]
    drop(slot)
    if not P.has_mods() and name not in SEEN:
        if len(SEEN) >= 2 and 0 <= P.free() < 250000:
            raise Falta('Mem\u00f3ria: sai e volta a abrir a app para '
                        'abrir outro tema (sem sys.modules).')
        SEEN.append(name)
        if len(SEEN) > 2 and not WARN:
            WARN.append('sem sys.modules: os pacotes ficam em mem\u00f3ria')
    try:
        m = __import__(name)
    except ImportError:
        raise Falta('Falta o m\u00f3dulo ' + name + ' (instala ' + name + '.tns)')
    except MemoryError:
        P.collect()
        raise
    D = getattr(m, 'D', None)
    if D is not None:
        v = head(D, 'V')
        if v != str(PVER):
            P.unload(name)
            raise Falta('M\u00f3dulo ' + name + ' desatualizado (vers\u00e3o ' +
                        v + '; esta app l\u00ea a ' + str(PVER) + ')')
        nl = head(D, 'N')
        if nl != '' and not nl.isdigit():
            raise Falta('M\u00f3dulo ' + name + ' estragado')
    SL[slot] = [m, name]
    return m


def head(D, k):
    # Valor de um marcador de cabecalho ("@V 1" -> "1").
    i = D.find('@' + k + ' ')
    if i < 0 or i > 200:
        return ''
    j = D.find('\n', i)
    return D[i + 3:j].strip()


def recs(D, tag):
    # Lista dos cabecalhos "@tag ..." pela ordem do pacote:
    # (campos, posicao).
    out = []
    k = '\n@' + tag + ' '
    i = D.find(k)
    while i >= 0:
        j = D.find('\n', i + 1)
        out.append((D[i + len(k):j].split('|'), i))
        i = D.find(k, j)
    return out


def body(D, i):
    # Texto de um registo que comeca na posicao i (ate ao proximo
    # "@L", "@E" ou "@X" no inicio de uma linha).
    j = D.find('\n', i + 1)
    e = len(D)
    for t in ('\n@L ', '\n@E ', '\n@X '):
        k = D.find(t, j)
        if 0 <= k < e:
            e = k
    return D[j + 1:e].rstrip('\n')


def parts(txt):
    # Divide o texto de um registo nas suas secoes "@A".."@J", "@R",
    # "@F", "@O", "@S", "@P", "@D". Devolve dicionario letra -> texto
    # ('T' e o texto antes da primeira secao; as formulas @F ficam numa
    # lista em 'F*').
    d = {}
    fs = []
    cur = 'T'           # texto antes da primeira secao (enunciado)
    buf = []
    for ln in txt.split('\n'):
        if len(ln) >= 2 and ln[0] == '@' and ln[1] in 'ABCDEFGHIJROSPD' and \
                (len(ln) == 2 or ln[2] == ' '):
            if cur is not None:
                d[cur] = '\n'.join(buf)
            cur = ln[1]
            buf = []
            if cur == 'F' and len(ln) > 3:
                # "@F nome|formula|..." e uma formula; "@F" sozinho e a
                # pagina F (exemplo resolvido).
                fs.append(ln[3:].split('|'))
                cur = None
            elif len(ln) > 3:
                buf.append(ln[3:])
            continue
        if cur is not None:
            buf.append(ln)
    if cur is not None:
        d[cur] = '\n'.join(buf)
    d['F*'] = fs
    return d


def ftext(f):
    # Pagina de uma formula: nome, formula, simbolos, condicoes, exemplo.
    o = ['# ' + f[0], '= ' + f[1]]
    if len(f) > 2 and f[2]:
        for s in f[2].split(';'):
            o.append('- ' + s.strip())
    if len(f) > 3 and f[3]:
        o.append('Condi\u00e7\u00f5es: ' + f[3])
    if len(f) > 4 and f[4]:
        o.append('Exemplo: ' + f[4])
    return '\n'.join(o)


def lesson(D, lid):
    # Devolve (cabecalho, paginas A..J, resposta, formulas) de uma licao.
    for h, i in recs(D, 'L'):
        if h[0] == lid:
            d = parts(body(D, i))
            pg = []
            for c in 'ABCDEFGHIJ':
                pg.append(d.get(c, ''))
            fs = d['F*']
            if fs:
                pg[4] = '\n\n'.join([ftext(f) for f in fs])
            return h, pg, d.get('R', ''), fs
    raise Falta('Li\u00e7\u00e3o ' + lid + ' n\u00e3o encontrada')
