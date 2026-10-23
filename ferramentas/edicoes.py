#!/usr/bin/env python3
"""Edicoes de reserva (seccao 4.8 do prompt): "M1TR4M FQ" e "M1TR4M Mat",
cada uma num so ficheiro .py com no maximo 300 KB, para os aparelhos onde
importar modulos entre programas nao funcione.

Como se junta tudo num so ficheiro sem exec nem eval:
- cada modulo passa a ser uma funcao _m_<nome>() com o corpo do modulo; as
  variaveis do modulo sao variaveis dessa funcao (os "global" passam a
  "nonlocal") e a funcao devolve um objeto com os nomes do modulo;
- "import x as y" passa a "y = _imp('x')" e __import__(n) passa a _imp(n);
  _imp cria cada modulo uma vez e guarda-o; P.unload(n) esquece-o, como
  se fosse tirado de sys.modules;
- os textos grandes (licoes, exercicios, indice da pesquisa) vao
  comprimidos com um dicionario de palavras frequentes (tokens de 2
  caracteres ASCII) e descomprimem-se com str.replace quando o pacote abre;
- o codigo vai compactado: sem comentarios e com indentacao de 1 espaco.
Cada edicao tem o seu catalogo e o seu indice, so com o que leva.
"""
import ast
import collections
import copy
import io
import os
import re
import tokenize

import conteudo as CT

KB = 1024
LIMITE = 300 * KB
# Tokens de compressao, com caracteres que nao aparecem nos textos (PRE):
# primeiro len(PRE) x len(SEG) tokens de 2 caracteres (prefixo + um de
# SEG), depois tokens de 3 (prefixo + prefixo + um de SEG). Os prefixos
# so aparecem a abrir tokens e SEG nao tem prefixos, por isso nenhum
# token aparece por acaso dentro de outro (os de 3 tiram-se primeiro).
PRE = '`~$&#*Y'
SEG = ''.join(chr(c) for c in range(33, 127) if chr(c) not in '"\\' + PRE)
MAXDIC = 2000
# Pedacos candidatos: ate 3 palavras, com ou sem um inicio de linha. Nunca
# comecam logo a seguir a um prefixo (seria o meio de um token).
PAL = re.compile(r"(?<![%s])(?:\n- |\n|)[^\s%s]+(?: [^\s%s]+){0,2}" % (
    re.escape(PRE), re.escape(PRE), re.escape(PRE)))


def fora(w):
    # Ocorrencias de w que nao comecam dentro de um token.
    return re.compile('(?<![%s])%s' % (re.escape(PRE), re.escape(w)))

NUCLEO = ['m1', 'm1_plat', 'm1_nucleo', 'm1_ui', 'm1_app', 'm1_cont',
          'm1_cat', 'm1_calc', 'm1_nav', 'm1_ex', 'm1_cfg', 'm1_ini']
FQ10 = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'f1', 'f2', 'f3']
MAT79 = ['n7', 'a7', 'g7', 'd7', 'n8', 'a8', 'g8', 'd8', 'n9', 'a9', 'g9',
         'd9']
# O que cada edicao leva. As calculadoras de cada tema vem com ele (campo
# calcs do tema); 'calcs' acrescenta outras; 'extra' sao modulos a mais.
EDICOES = (
    {'id': 'FQ', 'ficheiro': 'M1TR4M_FQ', 'disc': 'F', 'temas': FQ10,
     'calcs': ['c_comu.sci', 'c_comu.sf', 'c_comu.uni', 'c_comu.pre',
               'c_comd.cte'],
     'extra': ['m1_tp'], 'pesquisa': False, 'teclas': 'e01_fq'},
    {'id': 'Mat', 'ficheiro': 'M1TR4M_Mat', 'disc': 'M', 'temas': MAT79,
     'calcs': [], 'extra': [], 'pesquisa': False, 'exercicios': True,
     'teclas': 'e02_mat',
     'sem': ['c_matg.dist', 'c_matg.medz', 'c_matv.vet', 'c_comu.sci',
             'c_matr.res', 'c_mpol.ruf']},
)


class Falha(Exception):
    pass


def proprio(nome):
    return nome == 'm1' or nome.startswith(('m1_', 'c_', 'p_', 'x_'))

# ------------------------------------------------------------ compactar


def asc(s):
    o = []
    for ch in s:
        c = ord(ch)
        if c < 128:
            o.append(ch)
        elif c < 256:
            o.append('\\x%02x' % c)
        else:
            o.append('\\u%04x' % c)
    return ''.join(o)


PALAVRA = (tokenize.NAME, tokenize.NUMBER)
CORTE = 200     # strings mais longas partem-se em pedacos (linhas curtas)


def pedacos(lit):
    # Parte uma string literal ASCII ('...') em pedacos de CORTE
    # caracteres no maximo, sem partir sequencias de escape.
    q = lit[0]
    corpo = lit[1:-1]
    out = []
    i = 0
    atual = ''
    while i < len(corpo):
        j = i + 1
        if corpo[i] == '\\':
            j = i + 2
            if corpo[i + 1] == 'x':
                j = i + 4
            elif corpo[i + 1] == 'u':
                j = i + 6
        if len(atual) + j - i > CORTE:
            out.append(q + atual + q)
            atual = ''
        atual += corpo[i:j]
        i = j
    out.append(q + atual + q)
    return '(' + '\n'.join(out) + ')' if len(out) > 1 else out[0]


def apertar(src):
    # Volta a escrever o codigo com o minimo de espacos: indentacao de 1
    # espaco por nivel e espacos so entre palavras e numeros.
    out = []
    lin = []
    nivel = 0
    ant = None
    par = 0         # parenteses abertos: ai pode-se mudar de linha
    col = 0         # tamanho da linha fisica atual
    for tk in tokenize.generate_tokens(io.StringIO(src).readline):
        tp, ts = tk.type, tk.string
        if tp in (tokenize.COMMENT, tokenize.NL, tokenize.ENCODING,
                  tokenize.ENDMARKER):
            continue
        if tp == tokenize.INDENT:
            nivel += 1
            continue
        if tp == tokenize.DEDENT:
            nivel -= 1
            continue
        if tp == tokenize.NEWLINE:
            out.append(' ' * nivel + ''.join(lin))
            lin = []
            ant = None
            col = nivel
            continue
        if tp == tokenize.STRING and len(ts) > CORTE + 20:
            ts = pedacos(ts)
        if ant is not None and (ant in PALAVRA and (tp in PALAVRA or
                                                   tp == tokenize.STRING)):
            lin.append(' ')
            col += 1
        lin.append(ts)
        col = len(ts) - ts.rfind('\n') - 1 if '\n' in ts else col + len(ts)
        ant = tp
        if tp == tokenize.OP:
            if ts in '([{':
                par += 1
            elif ts in ')]}':
                par -= 1
            elif ts == ',' and par > 0 and col > CORTE:
                lin.append('\n')
                col = 0
    return '\n'.join(out)


def unparse(no):
    # Codigo compacto: ast.unparse, so ASCII (os caracteres nao ASCII so
    # aparecem dentro de strings) e com o minimo de espacos.
    return apertar(asc(ast.unparse(no)))


def nomes_topo(corpo):
    # Nomes que o modulo define ao nivel de topo (nao entra em funcoes nem
    # classes; os nomes de "except ... as e" nao contam).
    out = []

    def alvo(t):
        if isinstance(t, ast.Name):
            out.append(t.id)
        elif isinstance(t, (ast.Tuple, ast.List)):
            for x in t.elts:
                alvo(x)

    def ver(st):
        for s in st:
            if isinstance(s, (ast.FunctionDef, ast.ClassDef)):
                out.append(s.name)
            elif isinstance(s, ast.Assign):
                for t in s.targets:
                    alvo(t)
            elif isinstance(s, (ast.AugAssign, ast.AnnAssign)):
                alvo(s.target)
            elif isinstance(s, (ast.Import, ast.ImportFrom)):
                for a in s.names:
                    out.append(a.asname or a.name.split('.')[0])
            elif isinstance(s, (ast.For, ast.While, ast.If)):
                if isinstance(s, ast.For):
                    alvo(s.target)
                ver(s.body)
                ver(s.orelse)
            elif isinstance(s, ast.Try):
                ver(s.body)
                ver(s.orelse)
                ver(s.finalbody)
                for h in s.handlers:
                    ver(h.body)
            elif isinstance(s, ast.With):
                for it in s.items:
                    if it.optional_vars is not None:
                        alvo(it.optional_vars)
                ver(s.body)
    ver(corpo)
    vistos = []
    for n in out:
        if n not in vistos:
            vistos.append(n)
    return vistos


class Troca(ast.NodeTransformer):
    # import de modulos da app -> _imp; __import__ -> _imp; global ->
    # nonlocal.
    def __init__(self):
        self.deps = []

    def visit_Import(self, no):
        novos = []
        resto = []
        for a in no.names:
            if proprio(a.name):
                self.deps.append(a.name)
                novos.append(ast.Assign(
                    targets=[ast.Name(id=a.asname or a.name, ctx=ast.Store())],
                    value=ast.Call(func=ast.Name(id='_imp', ctx=ast.Load()),
                                   args=[ast.Constant(a.name)], keywords=[]),
                    lineno=no.lineno))
            else:
                resto.append(a)
        if resto:
            novos.insert(0, ast.Import(names=resto))
        return novos

    def visit_ImportFrom(self, no):
        if no.module and proprio(no.module):
            raise Falha('from %s import ... nao e suportado' % no.module)
        return no

    def visit_Call(self, no):
        self.generic_visit(no)
        if isinstance(no.func, ast.Name) and no.func.id == '__import__':
            no.func = ast.Name(id='_imp', ctx=ast.Load())
            if no.args and isinstance(no.args[0], ast.Constant):
                self.deps.append(no.args[0].value)
        return no

    def visit_Global(self, no):
        return ast.Nonlocal(names=no.names)


def corpo_funcao(nome, src):
    # Funcao vazia "def nome(): ..." com o corpo dado em codigo Python.
    return ast.parse('def %s():\n%s' % (nome, '\n'.join(
        ' ' + ln for ln in src.split('\n')))).body[0].body


# Mudancas so para as edicoes (o resto do codigo fica igual).
REMENDOS = {
    'm1_plat': {'has_mods': 'return True',
                'unload': '_L.pop(n, None)\nreturn True',
                'mod_file': "return ''"},
}


def dados(arv):
    # Modulo so com D = "texto" (pacotes e indice): devolve o texto.
    corpo = [s for s in arv.body if not (isinstance(s, ast.Expr) and
                                         isinstance(s.value, ast.Constant))]
    if len(corpo) == 1 and isinstance(corpo[0], ast.Assign) and \
            len(corpo[0].targets) == 1 and \
            isinstance(corpo[0].targets[0], ast.Name) and \
            corpo[0].targets[0].id == 'D' and \
            isinstance(corpo[0].value, ast.Constant) and \
            isinstance(corpo[0].value.value, str):
        return corpo[0].value.value
    return None


def usados(textos):
    # Nomes que podem ser lidos de fora de um modulo: atributos (X.nome) e
    # strings que parecem nomes (getattr com o nome de uma calculadora ou
    # de um ecra). Os outros nomes do modulo nao precisam de ser devolvidos.
    out = set(['D'])
    for t in textos:
        for no in ast.walk(ast.parse(t)):
            if isinstance(no, ast.Attribute):
                out.add(no.attr)
            elif isinstance(no, ast.Constant) and isinstance(no.value, str):
                for w in re.findall(r'[A-Za-z_][A-Za-z_0-9]*', no.value):
                    out.add(w)
    return out


def _carga(no):
    # Nomes lidos dentro de um no (inclui funcoes e lambdas aninhadas).
    return set(x.id for x in ast.walk(no) if isinstance(x, ast.Name) and
               isinstance(x.ctx, ast.Load))


def _pura(no):
    # Atribuicao sem efeitos ao correr: nenhuma chamada fora de lambdas.
    if not isinstance(no, ast.Assign) or not all(
            isinstance(t, ast.Name) for t in no.targets):
        return False
    pilha = [no.value]
    while pilha:
        x = pilha.pop()
        if isinstance(x, ast.Lambda):
            continue
        if isinstance(x, ast.Call):
            return False
        pilha.extend(ast.iter_child_nodes(x))
    return True


def podar(corpo, exp):
    # Tira do topo do modulo as funcoes, classes e constantes que nada
    # usa: as raizes sao o codigo que corre ao importar e os nomes que
    # podem ser lidos de fora (exp).
    defs = {}
    raizes = set()
    for s in corpo:
        if isinstance(s, (ast.FunctionDef, ast.ClassDef)):
            defs.setdefault(s.name, []).append(s)
        elif _pura(s):
            for t in s.targets:
                defs.setdefault(t.id, []).append(s)
        else:
            raizes |= _carga(s)
    vivos = set()
    fila = [n for n in defs if n in exp or n in raizes]
    while fila:
        n = fila.pop()
        if n in vivos:
            continue
        vivos.add(n)
        for s in defs.get(n, []):
            fila.extend(x for x in _carga(s) if x in defs and x not in vivos)
    out = []
    for s in corpo:
        if isinstance(s, (ast.FunctionDef, ast.ClassDef)):
            if s.name in vivos:
                out.append(s)
        elif _pura(s):
            if [t for t in s.targets if t.id in vivos]:
                out.append(s)
        else:
            out.append(s)
    return out


def fabrica(nome, texto, modo=None, exp=None):
    # Codigo da funcao _m_<nome>() e lista dos modulos que importa. exp:
    # nomes que podem ser lidos de fora (None: todos).
    arv = ast.parse(texto)
    tr = Troca()
    arv = tr.visit(arv)
    ast.fix_missing_locations(arv)
    rem = REMENDOS.get(nome, {})
    for s in arv.body:
        if isinstance(s, ast.FunctionDef) and s.name in rem:
            s.body = corpo_funcao(s.name, rem[s.name])
        if nome == 'm1' and modo and isinstance(s, ast.Assign) and \
                isinstance(s.targets[0], ast.Name) and \
                s.targets[0].id == 'MODO':
            s.value = ast.Constant(modo)
    if exp is not None:
        arv.body = podar(arv.body, exp)
    ns = [n for n in nomes_topo(arv.body) if exp is None or n in exp]
    ret = ast.parse('return _ns(%r%s)' % (' '.join(ns), ''.join(
        ', ' + n for n in ns))).body[0]
    fn = ast.FunctionDef(name='_m_' + nome, args=ast.arguments(
        posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[],
        kwarg=None, defaults=[]), body=arv.body + [ret],
        decorator_list=[], returns=None, type_params=[])
    mod = ast.Module(body=[fn], type_ignores=[])
    ast.fix_missing_locations(mod)
    return unparse(mod), tr.deps

# ------------------------------------------------------------ comprimir


def custo(s):
    # Bytes que o texto ocupa dentro de uma string Python ASCII.
    n = 0
    for ch in s:
        c = ord(ch)
        n += 1 if c < 128 else (4 if c < 256 else 6)
        if ch in '\\"\n':
            n += 1
    return n


def token(i):
    k = len(SEG)
    n = len(PRE) * k
    if i < n:
        return PRE[i // k] + SEG[i % k]
    i -= n
    return PRE[i // n] + PRE[i // k % len(PRE)] + SEG[i % k]


def comprimir(textos, maxe=MAXDIC):
    # Dicionario guloso: escolhe a cada passo o pedaco (caractere nao
    # ASCII, palavra ou grupo de ate 3 palavras) que mais poupa e troca-o
    # por um token. Devolve os textos comprimidos e a lista de pedacos.
    for t in textos.values():
        for p in PRE:
            if p in t:
                raise Falha('o texto tem o caractere %r reservado' % p)
    ts = dict(textos)
    tab = []
    maxe = min(maxe, (len(PRE) + 1) * len(PRE) * len(SEG))
    while len(tab) < maxe:
        tl = len(token(len(tab)))
        cont = collections.Counter()
        nasc = collections.Counter()
        for t in ts.values():
            nasc.update(ch for ch in t if ord(ch) > 127)
            for m in PAL.finditer(t):
                g = m.group(0)
                lead = ''
                for x in ('\n- ', '\n'):
                    if g.startswith(x):
                        lead, g = x, g[len(x):]
                        break
                ws = g.split(' ')
                for i in range(len(ws)):
                    for j in range(i + 1, min(len(ws), i + 3) + 1):
                        w = ' '.join(ws[i:j])
                        if len(w) >= 3:
                            cont[w] += 1
                        if i == 0 and lead:
                            cont[lead + w] += 1
        cands = [((custo(w) - tl) * n - custo(w) - 1, w)
                 for w, n in cont.most_common(4000)]
        cands += [((custo(ch) - tl) * n - custo(ch) - 1, ch)
                  for ch, n in nasc.items()]
        cands.sort(reverse=True)
        melhor, mg = None, 0
        for est, w in cands[:80]:
            # ocorrencias que nao comecam dentro de um token
            n = sum(t.count(w) - sum(t.count(p + w) for p in PRE)
                    for t in ts.values())
            g = (custo(w) - tl) * n - custo(w) - 1
            if g > mg:
                melhor, mg = w, g
        if melhor is None or mg <= 12:
            break
        tk = token(len(tab))
        rx = fora(melhor)
        for k in ts:
            ts[k] = rx.sub(lambda m: tk, ts[k])
        tab.append(melhor)
    for k in textos:
        if descomprimir(ts[k], tab) != textos[k]:
            raise Falha('a compressao de %s nao e reversivel' % k)
    return ts, tab


def descomprimir(t, tab):
    for i in range(len(tab) - 1, -1, -1):
        t = t.replace(token(i), tab[i])
    return t

# ------------------------------------------------------------ juntar


RUNTIME = '''_F = {}
_L = {}
_ED = %(ed)r


class _NS:
 pass


def _ns(n, *v):
 m = _NS()
 i = 0
 for k in n.split():
  setattr(m, k, v[i])
  i += 1
 return m


def _imp(n):
 m = _L.get(n)
 if m is None:
  f = _F.get(n)
  if f is None:
   raise ImportError("no module named '" + n + "'")
  m = f()
  _L[n] = m
 return m


_W = None


def _dz(s):
 global _W
 if _W is None:
  _W = _T.split(%(sep)r)
 a = %(pre)r
 b = %(seg)r
 k = len(b)
 n = len(a) * k
 for i in range(len(_W) - 1, -1, -1):
  if i < n:
   t = a[i // k] + b[i %% k]
  else:
   j = i - n
   t = a[j // n] + a[j // k %% len(a)] + b[j %% k]
  s = s.replace(t, _W[i])
 return s
'''


def literal(nome, texto, ind=''):
    # Atribuicao de uma string longa em linhas curtas (barra no fim da
    # linha); so a 1.a linha leva a indentacao.
    s = CT.literal(nome, texto)
    return ind + s.rstrip('\n')


def juntar(ed, mods, rel):
    """Gera o ficheiro unico da edicao. mods: {nome: texto ASCII}."""
    dad = {}
    cod = {}
    for n, t in mods.items():
        d = dados(ast.parse(t))
        if d is not None:
            # as calculadoras que a edicao nao leva saem dos cabecalhos
            for c in ed.get('sem', []):
                d = re.sub(r'(?<=[| ])%s ?' % re.escape(c), '', d)
            dad[n] = d
        else:
            cod[n] = t
    comp, tab = comprimir(dad) if dad else ({}, [])
    if [w for w in tab if PRE[0] in w]:
        raise Falha('uma entrada do dicionario tem o separador')
    partes = ['# %s.py - M1TR4M: edicao de reserva "M1TR4M %s" num so '
              'ficheiro\n# (gerada pelo build; nao editar). Usa-se so se '
              'importar modulos entre\n# programas nao funcionar no aparelho.'
              ' Leva: %s.\n' % (ed['ficheiro'], ed['id'], rel),
              RUNTIME % {'ed': ed['id'], 'pre': PRE, 'seg': SEG,
                         'sep': PRE[0]},
              literal('_T', PRE[0].join(tab))]
    deps = {}
    exp = usados(list(cod.values()))
    for d in dad.values():
        exp.update(re.findall(r'c_[a-z0-9]+\.([A-Za-z_][A-Za-z_0-9]*)', d))
    for n in sorted(cod):
        modo = 'edi\u00e7\u00e3o de reserva ' + ed['id'] if n == 'm1' else None
        src, ds = fabrica(n, cod[n], modo, exp)
        deps[n] = ds
        partes.append(src)
        partes.append("_F['%s'] = _m_%s" % (n, n))
    for n in sorted(comp):
        partes.append("def _m_%s():\n%s\n return _ns('D', _dz(D))" % (
            n, literal('D', comp[n], ' ')))
        partes.append("_F['%s'] = _m_%s" % (n, n))
    partes.append("_imp('m1')")
    return '\n\n\n'.join(partes) + '\n', deps, len(tab), dad


def dependencias(pasta, nomes):
    # Fecho dos imports de modulos da app (estaticos).
    fila = list(nomes)
    vistos = set()
    while fila:
        n = fila.pop()
        if n in vistos:
            continue
        vistos.add(n)
        p = os.path.join(pasta, n + '.py')
        if not os.path.exists(p):
            raise Falha('falta o modulo %s' % n)
        for no in ast.walk(ast.parse(open(p, encoding='ascii').read())):
            if isinstance(no, ast.Import):
                for a in no.names:
                    if proprio(a.name):
                        fila.append(a.name)
    return vistos


def gerar(pasta, temas, calcs, ed, extra_cat):
    """Escreve <ficheiro>.py da edicao em pasta/../edicoes e devolve
    (caminho, tamanho, resumo). pasta: dist/py (modulos ja gerados)."""
    # copias dos temas (a edicao muda as calculadoras e os exercicios)
    ts = [copy.copy(t) for t in temas if t.id in ed['temas']]
    if [x for x in ed['temas'] if x not in [t.id for t in ts]]:
        raise Falha('edicao %s: temas que nao existem' % ed['id'])
    if not ed.get('exercicios', True):
        for t in ts:
            t.exercicios = []
    sem = set(ed.get('sem', []))
    ids = set(ed['calcs'])
    dono = {}
    for t in ts:
        t.calcs = [c for c in t.calcs if c not in sem]
        us = list(t.calcs)
        for b in t.licoes:
            us += b.meta.get('calc', '').split()
            us += [f[5] for f in b.formulas if f[5]]
        for b in t.exemplos:
            us += b.meta.get('calc', '').split()
        for c in us:
            if c not in sem:
                ids.add(c)
                dono.setdefault(c, t.id)
    # uma calculadora de um tema que nao vai passa para o 1.o tema da
    # edicao que a usa (para aparecer no menu das calculadoras)
    cs = []
    for c in calcs:
        if c[0] in ids:
            c = list(c)
            if c[4] and c[4] not in ed['temas']:
                c[4] = dono.get(c[0], '')
            cs.append(c)
    # catalogo e indice so com o conteudo da edicao
    mods = {}
    cat = CT.gerar_catalogo(ts) + 'BUILD = "%s"\n' % extra_cat['data']
    idx = []
    if ed['pesquisa']:
        idx = [(n, d, x) for n, d, x in CT.gerar_indice(
            ts, cs, extra_cat['elementos'], extra_cat['constantes'])
            if d == ed['disc']]
    cat += 'IDX = "%s"\n' % ' '.join(n + ':' + d for n, d, x in idx)
    cat += CT.literal('LIMITES', extra_cat['limites'])
    mods['m1_cat'] = cat
    mods['m1_calc'] = CT.gerar_calc(cs)
    for n, d, x in idx:
        mods[n] = x
    base = set(NUCLEO + ed['extra'] + ([] if not idx else ['m1_pesq']))
    base.update(t.pacote for t in ts)
    base.update(t.pacote_x for t in ts if t.pacote_x)
    base.update(c[0].split('.')[0] for c in cs)
    todos = dependencias(pasta, sorted(base - set(mods)))
    for n in sorted(todos):
        if n not in mods:
            mods[n] = open(os.path.join(pasta, n + '.py'), encoding='ascii').read()
    rel = '%d temas (%s), %d calculadoras%s' % (
        len(ts), ' '.join(t.id for t in ts), len(cs),
        ', pesquisa' if idx else '')
    texto, deps, nt, dad = juntar(ed, mods, rel)
    # prova: carregar o ficheiro (sem arrancar a app) e descomprimir cada
    # pacote com o _dz da propria edicao
    env = {}
    exec(compile(texto[:texto.rindex("_imp('m1')")], ed['ficheiro'],
                 'exec'), env)
    for n, d in dad.items():
        if env['_imp'](n).D != d:
            raise Falha('edicao %s: %s descomprimido nao confere' % (
                ed['id'], n))
    for n, ds in deps.items():
        for d in ds:
            if d not in mods:
                raise Falha('edicao %s: %s importa %s, que nao vai' % (
                    ed['id'], n, d))
    try:
        texto.encode('ascii')
    except UnicodeEncodeError:
        raise Falha('edicao %s: o ficheiro nao e ASCII' % ed['id'])
    destino = os.path.join(os.path.dirname(pasta), 'edicoes')
    os.makedirs(destino, exist_ok=True)
    p = os.path.join(destino, ed['ficheiro'] + '.py')
    with open(p, 'w', encoding='ascii', newline='\n') as f:
        f.write(texto)
    tam = len(texto.encode('ascii'))
    if tam > LIMITE:
        raise Falha('edicao %s: %d bytes (max. %d)' % (ed['id'], tam, LIMITE))
    return p, tam, '%s; %d modulos; dicionario de %d palavras' % (
        rel, len(mods), nt)
