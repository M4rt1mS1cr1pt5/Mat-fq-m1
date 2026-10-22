#!/usr/bin/env python3
"""Leitura, validacao e geracao dos conteudos da M1TR4M.

Formato das fontes (conteudo/**/*.txt), um ficheiro por tema:

    @tema q1
    disc: F            (F = FQ, M = Matematica)
    grupo: q           (q quimica, f fisica, a AL, r revisoes; t temas Mat)
    titulo: Massa e tamanho dos atomos
    calcs: c_fqat.mm c_fqat.qm

    @licao q1a
    titulo: ...
    chave: palavras-chave
    calc: c_fqat.mm
    ano: 10
    nivel: nucleo | aprofundamento | extensao | revisao
    pre: r9a r9b       (licoes pre-requisito)
    liga: m4b          (licao da outra disciplina que apoia esta)
    fonte: item das Aprendizagens Essenciais ou pagina do manual
    #A ... #J          paginas da licao (secao 9 do prompt)
    #E                 so linhas "@F nome|formula|simbolos;...|condicoes|exemplo|calc"
    #R                 resposta do exercicio J
    #V                 codigo Python (so corre no computador) que define V,
                       a lista dos valores marcados com [[..]] nas paginas
                       A a J e R, pela ordem em que aparecem

    @exemplo q1e1
    nivel: 1 | 2 | 3   (basico, intermedio, avancado)
    titulo: ...
    licao: q1a
    calc: c_fqat.mm
    #T  texto (enunciado, dados, objetivo, metodo, resolucao, resultado...)
    #V  V = [...]

    @exercicio q1x1
    tipo: m (escolha multipla) | n (numerico) | u (numerico com unidade)
          | v (verdadeiro ou falso)
    licao: q1a
    modo: r (tolerancia) | d2 (2 casas) | s3 (3 alg. sig.)   (n e u)
    unidades: g kg mg  (u: a solucao vem na primeira)
    #T enunciado   #O opcoes (uma por linha)   #S solucao   #P pista
    #D resolucao   #V codigo que define S (e V se houver marcas)

Linhas que comecam por "%%" sao comentarios.
Marcas: "[[2,45]]" e um numero que o build recalcula; "[[=1/3]]" compara
o valor exato. No pacote gerado os parenteses retos duplos desaparecem.
"""
import math
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'src'))
import m1_nucleo as N  # noqa: E402
import m1_ui as U  # noqa: E402

LARG = 41          # colunas usadas para medir as paginas (seccao 9)
PAGS = 'ABCDEFGHIJ'
NIVEIS = ('núcleo', 'aprofundamento', 'extensão', 'revisão')
TIPOS = 'mnuv'
SINONIMOS = [
    ('sen', 'seno'), ('cos', 'cosseno'), ('tg', 'tangente'),
    ('epg', 'energia potencial gravitica'), ('ec', 'energia cinetica'),
    ('em', 'energia mecanica'), ('mol', 'quantidade de materia'),
    ('m', 'massa'), ('na', 'avogadro'), ('vm', 'volume molar'),
    ('ddp', 'diferenca de potencial'), ('fem', 'forca eletromotriz'),
    ('aiq', 'amplitude interquartil'), ('dp', 'desvio padrao'),
    ('pmq', 'minimos quadrados'), ('reta de regressao', 'minimos quadrados'),
    ('tp', 'tabela periodica'), ('ei', 'energia de ionizacao'),
    ('ra', 'raio atomico'), ('rendimento', 'eficiencia'),
    ('juro', 'juros'), ('hondt', 'mandatos'), ('vetor', 'vetores'),
]


class Erro(Exception):
    pass


class Bloco:
    def __init__(self, tipo, ident, fich, linha):
        self.tipo = tipo
        self.id = ident
        self.fich = fich
        self.linha = linha
        self.meta = {}
        self.sec = {}
        self.formulas = []

    def onde(self):
        return '%s:%d (%s %s)' % (os.path.relpath(self.fich, RAIZ),
                                  self.linha, self.tipo, self.id)


def ler_ficheiro(fn):
    blocos = []
    cur = None
    sec = None
    with open(fn, encoding='utf-8') as f:
        for n, ln in enumerate(f, 1):
            ln = ln.rstrip('\n').rstrip()
            if ln.startswith('%%'):
                continue
            m = re.match(r'^@(tema|licao|exemplo|exercicio)\b\s*(\S*)\s*$', ln)
            if m:
                cur = Bloco(m.group(1), m.group(2), fn, n)
                blocos.append(cur)
                sec = None
                continue
            if cur is None:
                if ln.strip():
                    raise Erro('%s:%d texto fora de um bloco' % (fn, n))
                continue
            m = re.match(r'^#([A-JROSPDTVMU])\s*$', ln)
            if m:
                sec = m.group(1)
                if sec in cur.sec:
                    raise Erro('%s secao #%s repetida' % (cur.onde(), sec))
                cur.sec[sec] = []
                continue
            if sec is None:
                if not ln.strip():
                    continue
                m = re.match(r'^([a-z]+):\s*(.*)$', ln)
                if not m:
                    raise Erro('%s:%d linha de metadados invalida: %r' %
                               (fn, n, ln))
                cur.meta[m.group(1)] = m.group(2).strip()
                continue
            if sec == 'E' and cur.tipo == 'licao':
                if ln.startswith('@F '):
                    cur.formulas.append(ln[3:].split('|'))
                elif ln.strip():
                    raise Erro('%s:%d na pagina E so ha linhas @F' % (fn, n))
                continue
            cur.sec[sec].append(ln)
    for b in blocos:
        for k in list(b.sec):
            t = b.sec[k]
            while t and not t[-1].strip():
                t.pop()
            while t and not t[0].strip():
                t.pop(0)
            b.sec[k] = '\n'.join(t)
    return blocos

# ------------------------------------------------------------ marcas


MARCA = re.compile(r'\[\[(.+?)\]\]')


def tirar_marcas(t):
    return MARCA.sub(lambda m: m.group(1).lstrip('='), t)


def marcas(t):
    return MARCA.findall(t)


OPER = re.compile(r'[\d)²³#]\s*[×/+−-]\s*[\d(√#]')
ANTES = re.compile(r'[\d\s,.()×/+−\-²³√π·#]*$')
DEPOIS = re.compile(r'\s*[−-]?(\d+(?:,\d+)?)(?:\s*×\s*10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)?'
                    r'(\s*[×/+−-]\s*[\d(√])?')


def contas_sem_marca(t):
    """Linhas com uma conta acabada em '= numero' sem marca [[..]].

    So conta o ultimo '=' de uma cadeia (2 + 3 = 5, nao 2 = 1 + 1 = ...)
    e ignora '= 0' (equacoes) e numeros dados (sem conta antes do '=')."""
    r = []
    for ln in t.split('\n'):
        s = MARCA.sub('#', ln)
        for i, ch in enumerate(s):
            if ch != '=':
                continue
            m = DEPOIS.match(s, i + 1)
            if not m or m.group(2) or m.group(1) == '0':
                continue
            if OPER.search(ANTES.search(s[:i]).group(0)):
                r.append(ln)
                break
    return r


SUPR = '⁰¹²³⁴⁵⁶⁷⁸⁹'


def ulp(s):
    """Unidade da ultima casa de um numero escrito (2,45 -> 0,01)."""
    s = s.strip().replace('−', '-')
    m = re.match(r'^[+-]?([\d ]+)(?:,(\d+))?(?:\s*×\s*10([⁻' + SUPR +
                 r']+))?(?:\s*%)?$', s)
    if not m:
        return None
    dec = len(m.group(2)) if m.group(2) else 0
    e = 0
    if m.group(3):
        t = ''.join('-' if c == '⁻' else str(SUPR.index(c))
                    for c in m.group(3))
        e = int(t)
    return 10.0 ** (e - dec)


def valor(s):
    s = s.strip().replace(' ', '').rstrip('%')
    return N.num(s)[0]


def confere(txt, V, onde):
    """Compara as marcas do texto com os valores calculados em V."""
    ms = marcas(txt)
    if not ms:
        return
    if V is None:
        raise Erro('%s tem %d marcas mas o bloco #V nao define V' %
                   (onde, len(ms)))
    if len(V) != len(ms):
        raise Erro('%s: %d marcas no texto e %d valores em V (%s)' %
                   (onde, len(ms), len(V), ms))
    for s, v in zip(ms, V):
        if s.startswith('='):
            e = valor(s[1:])
            if abs(e - v) > 1e-9 * max(1.0, abs(v)):
                raise Erro('%s: marca [[%s]] = %r mas o calculo da %r' %
                           (onde, s, e, v))
            continue
        u = ulp(s)
        if u is None:
            raise Erro('%s: marca [[%s]] nao e um numero' % (onde, s))
        e = valor(s)
        if abs(e - v) > 0.5 * u * (1 + 1e-9) + 1e-12 * abs(v):
            raise Erro('%s: marca [[%s]] mas o calculo da %r (arredondado: %s)' %
                       (onde, s, v, N.fmt(v, 0, 10)))


AMBIENTE = {
    'NA': 6.02e23, 'NA_exato': 6.02214076e23, 'h': 6.63e-34,
    'h_exato': 6.62607015e-34, 'c': 3.00e8, 'Vm': 22.4, 'e_carga': 1.60e-19,
    'G': 6.67e-11, 'sigma': 5.67e-8, 'Kw': 1.00e-14, 'u': 1.66e-27,
}


def correr_v(b, codigo, extra=None):
    env = dict(vars(math))
    env.update(AMBIENTE)
    env['N'] = N
    env['sf'] = lambda x, n: float(N.fsf(x, n).replace(',', '.').replace(
        ' × 10', 'e').translate(str.maketrans(
            '⁻' + SUPR, '-0123456789')))
    env['arr'] = lambda x, n: round(x + (1e-12 if x >= 0 else -1e-12), n)
    if extra:
        env.update(extra)
    try:
        exec(compile(codigo, b.onde(), 'exec'), env)
    except Exception as e:
        raise Erro('%s: erro no bloco #V: %s: %s' % (b.onde(),
                                                    type(e).__name__, e))
    return env

# ------------------------------------------------------------ medidas


def nlinhas(t, w=LARG):
    return len(U.wrap(tirar_marcas(t), w)) if t else 0


def balas(t):
    return len([x for x in t.split('\n') if x.startswith('- ')])


def frases_longas(t, lim=20):
    out = []
    for ln in tirar_marcas(t).split('\n'):
        if ln[:2] in ('= ', '> '):
            continue
        for fr in re.split(r'(?<=[.!?])\s+', ln):
            ws = [w for w in fr.split() if re.search(r'[A-Za-zÀ-ÿ]', w)]
            if len(ws) >= lim:
                out.append((len(ws), fr[:60]))
    return out


def ftexto(f):
    o = ['# ' + f[0], '= ' + f[1]]
    if len(f) > 2 and f[2]:
        for s in f[2].split(';'):
            o.append('- ' + s.strip())
    if len(f) > 3 and f[3]:
        o.append('Condições: ' + f[3])
    if len(f) > 4 and f[4]:
        o.append('Exemplo: ' + f[4])
    return '\n'.join(o)

# ------------------------------------------------------------ temas


class Tema:
    def __init__(self, b):
        self.b = b
        self.id = b.id
        self.meta = b.meta
        self.licoes = []
        self.exemplos = []
        self.exercicios = []
        for k in ('disc', 'grupo', 'titulo'):
            if not b.meta.get(k):
                raise Erro('%s sem "%s:"' % (b.onde(), k))
        self.disc = b.meta['disc']
        self.grupo = b.meta['grupo']
        self.titulo = b.meta['titulo']
        self.calcs = b.meta.get('calcs', '').split()
        self.revisao = self.grupo == 'r'

    @property
    def pacote(self):
        return 'p_' + self.id

    @property
    def pacote_x(self):
        return ('x_' + self.id) if self.exercicios else ''


def ler_temas(pasta=None):
    pasta = pasta or os.path.join(RAIZ, 'conteudo')
    fs = []
    for r, ds, ns in os.walk(pasta):
        for n in ns:
            if n.endswith('.txt'):
                fs.append(os.path.join(r, n))
    temas = []
    for fn in sorted(fs):
        bs = ler_ficheiro(fn)
        if not bs:
            continue
        if bs[0].tipo != 'tema':
            raise Erro('%s: o ficheiro tem de comecar por @tema' % fn)
        t = Tema(bs[0])
        for b in bs[1:]:
            if b.tipo == 'licao':
                t.licoes.append(b)
            elif b.tipo == 'exemplo':
                t.exemplos.append(b)
            elif b.tipo == 'exercicio':
                t.exercicios.append(b)
            else:
                raise Erro('%s: so um @tema por ficheiro' % b.onde())
        temas.append(t)
    temas.sort(key=lambda t: (ORDEM.index(t.id) if t.id in ORDEM else 999,
                              t.id))
    return temas


# Ordem dos temas nos menus.
ORDEM = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'f1', 'f2', 'f3', 'aq', 'af',
         'r7', 'r8', 'r9', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8',
         'm9', 'mr']

# ------------------------------------------------------------ validar


def validar(temas, calcs_ids, avisos):
    ids = {}
    for t in temas:
        for b in t.licoes + t.exemplos + t.exercicios:
            if b.id in ids:
                raise Erro('%s: identificador repetido (ja em %s)' %
                           (b.onde(), ids[b.id].onde()))
            ids[b.id] = b
        for c in t.calcs:
            if c not in calcs_ids:
                raise Erro('%s: calculadora %s nao existe' % (t.b.onde(), c))
    lic = {b.id: (t, b) for t in temas for b in t.licoes}
    erros = []
    for t in temas:
        if not t.licoes:
            erros.append('%s: tema sem licoes' % t.b.onde())
        for fn, bs in ((validar_licao, t.licoes), (validar_exemplo, t.exemplos),
                       (validar_exercicio, t.exercicios)):
            for b in bs:
                try:
                    if fn is validar_exercicio:
                        fn(t, b, lic, avisos)
                    else:
                        fn(t, b, lic, calcs_ids, avisos)
                except Erro as e:
                    erros.append(str(e))
    if erros:
        raise Erro('%d erros nos conteudos:\n  ' % len(erros) +
                   '\n  '.join(erros))
    return ids


def _calc_ok(b, c, calcs_ids):
    for x in c.split():
        if x not in calcs_ids:
            raise Erro('%s: calculadora %s nao existe' % (b.onde(), x))


def validar_licao(t, b, lic, calcs_ids, avisos):
    m = b.meta
    for k in ('titulo', 'chave', 'nivel', 'fonte', 'ano'):
        if not m.get(k):
            raise Erro('%s: falta "%s:"' % (b.onde(), k))
    if m['nivel'] not in NIVEIS:
        raise Erro('%s: nivel invalido %r' % (b.onde(), m['nivel']))
    if m.get('calc'):
        _calc_ok(b, m['calc'], calcs_ids)
    for k in ('pre', 'liga'):
        for x in m.get(k, '').split():
            if x not in lic:
                raise Erro('%s: %s %s nao e uma licao' % (b.onde(), k, x))
    precisas = 'ACEFJ' if t.revisao else 'ABCDEFGHIJ'
    for p in precisas:
        if p == 'E':
            if not b.formulas:
                raise Erro('%s: pagina E sem formulas (@F)' % b.onde())
            continue
        if not b.sec.get(p):
            raise Erro('%s: falta a pagina %s' % (b.onde(), p))
    if not b.sec.get('R'):
        raise Erro('%s: falta a resposta R' % b.onde())
    lim = {'A': ('b', 5), 'B': ('l', 8), 'C': ('l', 12), 'D': ('l', 30),
           'F': ('l', 30), 'G': ('l', 8), 'H': ('b', 5), 'I': ('b', 6),
           'J': ('l', 10)}
    errs = []
    for p in 'ABCDFGHIJ':
        k, n = lim[p]
        s = b.sec.get(p, '')
        if not s:
            continue
        v = balas(s) if k == 'b' else nlinhas(s)
        if v > n:
            errs.append('%s: pagina %s tem %d %s (max. %d)' % (
                b.onde(), p, v, 'pontos' if k == 'b' else 'linhas', n))
        if k == 'b' and balas(s) != len([x for x in s.split('\n') if x]):
            errs.append('%s: pagina %s so tem pontos "- "' % (b.onde(), p))
    if errs:
        raise Erro('\n  '.join(errs))
    for f in b.formulas:
        if len(f) != 6:
            raise Erro('%s: formula com %d campos (sao 6): %s' % (
                b.onde(), len(f), f[0]))
        if not f[0] or not f[1]:
            raise Erro('%s: formula sem nome ou sem expressao' % b.onde())
        if f[5]:
            _calc_ok(b, f[5], calcs_ids)
        n = nlinhas(ftexto(f))
        if n > 10:
            raise Erro('%s: formula "%s" ocupa %d linhas (max. 10)' %
                       (b.onde(), f[0], n))
    texto = '\n'.join(b.sec.get(p, '') for p in PAGS + 'R')
    env = correr_v(b, b.sec['V']) if b.sec.get('V') else {}
    confere(texto, env.get('V'), b.onde())
    for ln in contas_sem_marca(texto):
        avisos.append('%s: conta sem marca [[..]]: %s' % (b.onde(), ln))
    for p in 'ABCDFGHIJR':
        for n, fr in frases_longas(b.sec.get(p, '')):
            avisos.append('%s pág. %s: frase com %d palavras: %s' %
                          (b.onde(), p, n, fr))


def validar_exemplo(t, b, lic, calcs_ids, avisos):
    m = b.meta
    for k in ('nivel', 'titulo', 'licao'):
        if not m.get(k):
            raise Erro('%s: falta "%s:"' % (b.onde(), k))
    if m['nivel'] not in ('1', '2', '3'):
        raise Erro('%s: nivel tem de ser 1, 2 ou 3' % b.onde())
    if m['licao'] not in lic:
        raise Erro('%s: licao %s nao existe' % (b.onde(), m['licao']))
    if m.get('calc'):
        _calc_ok(b, m['calc'], calcs_ids)
    if not b.sec.get('T'):
        raise Erro('%s: exemplo sem texto #T' % b.onde())
    if nlinhas(b.sec['T']) > 30:
        raise Erro('%s: exemplo com %d linhas (max. 30 = 3 ecras)' %
                   (b.onde(), nlinhas(b.sec['T'])))
    env = correr_v(b, b.sec['V']) if b.sec.get('V') else {}
    confere(b.sec['T'], env.get('V'), b.onde())
    for ln in contas_sem_marca(b.sec['T']):
        avisos.append('%s: conta sem marca [[..]]: %s' % (b.onde(), ln))
    if marcas(b.sec['T']) == [] and re.search(r'\d', b.sec['T']):
        avisos.append('%s: exemplo com numeros sem marcas [[..]]' % b.onde())
    for n, fr in frases_longas(b.sec['T']):
        avisos.append('%s: frase com %d palavras: %s' % (b.onde(), n, fr))


def validar_exercicio(t, b, lic, avisos):
    m = b.meta
    tp = m.get('tipo', '')
    if tp not in TIPOS or len(tp) != 1:
        raise Erro('%s: tipo tem de ser m, n, u ou v' % b.onde())
    if m.get('licao') not in lic:
        raise Erro('%s: licao %r nao existe' % (b.onde(), m.get('licao')))
    for k in 'TSPD':
        if not b.sec.get(k):
            raise Erro('%s: falta #%s' % (b.onde(), k))
    if not b.sec.get('V'):
        raise Erro('%s: falta o bloco #V com a verificacao independente' %
                   b.onde())
    env = correr_v(b, b.sec['V'])
    if 'S' not in env:
        raise Erro('%s: o bloco #V nao define S' % b.onde())
    S = env['S']
    sol = b.sec['S'].strip()
    if tp == 'm':
        ops = [x for x in b.sec.get('O', '').split('\n') if x.strip()]
        if len(ops) != 4:
            raise Erro('%s: escolha multipla precisa de 4 opcoes' % b.onde())
        if len(set(ops)) != 4:
            raise Erro('%s: opcoes repetidas' % b.onde())
        if sol not in '1234' or len(sol) != 1:
            raise Erro('%s: #S tem de ser 1, 2, 3 ou 4' % b.onde())
        if int(sol) != S:
            raise Erro('%s: #S diz %s mas a verificacao da %r' %
                       (b.onde(), sol, S))
        for i, o in enumerate(ops):
            if len(U.wrap(tirar_marcas(o), LARG - 3)) > 4:
                raise Erro('%s: opcao %d demasiado longa' % (b.onde(), i + 1))
    elif tp == 'v':
        if sol not in ('V', 'F'):
            raise Erro('%s: #S tem de ser V ou F' % b.onde())
        if sol != S:
            raise Erro('%s: #S diz %s mas a verificacao da %r' %
                       (b.onde(), sol, S))
    else:
        modo = m.get('modo', 'r')
        if not re.match(r'^(r|d\d+|s\d+)$', modo):
            raise Erro('%s: modo invalido %r' % (b.onde(), modo))
        try:
            v = N.num(sol)[0]
        except Exception as e:
            raise Erro('%s: #S nao e um numero: %s' % (b.onde(), e))
        tol = 0.001
        if not N.check(sol, v, modo, tol):
            raise Erro('%s: a resposta mostrada %s nao e aceite pela app' %
                       (b.onde(), sol))
        if not N.check(sol, float(S), modo, tol):
            raise Erro('%s: #S = %s mas a verificacao da %r' %
                       (b.onde(), sol, S))
        if tp == 'u':
            us = m.get('unidades', '').split()
            if len(us) < 2:
                raise Erro('%s: tipo u precisa de pelo menos 2 unidades' %
                           b.onde())
            cat = N.ucat(us[0])
            for u in us:
                if not N.ucat(u):
                    raise Erro('%s: unidade desconhecida %s' % (b.onde(), u))
                if N.ucat(u) != cat and (u + ':' + cat) not in N._units():
                    raise Erro('%s: unidades de grandezas diferentes' %
                               b.onde())
    texto = '\n'.join(b.sec.get(k, '') for k in 'TOD')
    confere(texto, env.get('V'), b.onde())
    for ln in contas_sem_marca(b.sec.get('D', '')):
        avisos.append('%s: conta sem marca [[..]]: %s' % (b.onde(), ln))
    if nlinhas(b.sec['T']) > 10:
        raise Erro('%s: enunciado com %d linhas (max. 10)' %
                   (b.onde(), nlinhas(b.sec['T'])))
    if nlinhas(b.sec['D']) > 30:
        raise Erro('%s: resolucao com %d linhas (max. 30)' %
                   (b.onde(), nlinhas(b.sec['D'])))

# ------------------------------------------------------------ gerar


def esc(s):
    """Texto -> conteudo de uma string Python ASCII (\\uXXXX, \\n)."""
    o = []
    for ch in s:
        c = ord(ch)
        if ch == '\\':
            o.append('\\\\')
        elif ch == '"':
            o.append('\\"')
        elif ch == '\n':
            o.append('\\n')
        elif c < 32:
            raise Erro('caracter de controlo %r' % ch)
        elif c < 128:
            o.append(ch)
        elif c <= 0xFFFF:
            o.append('\\u%04x' % c)
        else:
            raise Erro('caracter fora do plano basico: %r' % ch)
    return ''.join(o)


def literal(nome, texto, cab=''):
    """Gera 'NOME = "..."' com linhas fisicas curtas (barra no fim da
    linha continua a mesma string, sem custo a compilar)."""
    out = [cab] if cab else []
    linhas = texto.split('\n')
    corpo = []
    for i, ln in enumerate(linhas):
        e = esc(ln) + ('\\n' if i < len(linhas) - 1 else '')
        while len(e) > 120:
            k = e.rfind(' ', 40, 110)
            if k < 0:
                k = 100
                while e[k - 1] == '\\' or re.search(r'\\u[0-9a-f]{0,3}$',
                                                     e[:k]):
                    k -= 1
            corpo.append(e[:k] + '\\')
            e = e[k:]
        corpo.append(e + '\\')
    corpo[-1] = corpo[-1][:-1]
    out.append(nome + ' = "' + corpo[0])
    out.extend(corpo[1:])
    out[-1] = out[-1] + '"'
    return '\n'.join(out) + '\n'


def lic_ref(lic, ids):
    out = []
    for x in ids.split():
        out.append(x + ':' + lic[x][1].meta['titulo'])
    return ';'.join(out)


def gerar_pacote(t, lic):
    o = ['@V 1', '@N %d' % len(t.licoes), '@T ' + t.titulo]
    for b in t.licoes:
        m = b.meta
        h = [b.id, m['titulo'], N.low(m['chave']), m.get('calc', ''),
             m.get('ano', ''), m['nivel'], lic_ref(lic, m.get('pre', '')),
             lic_ref(lic, m.get('liga', '')), m['fonte']]
        for x in h:
            if '|' in x or '\n' in x:
                raise Erro('%s: "|" ou mudanca de linha num campo' % b.onde())
        o.append('@L ' + '|'.join(h))
        for p in PAGS + 'R':
            if p == 'E':
                for f in b.formulas:
                    o.append('@F ' + '|'.join(x.strip() for x in f))
                continue
            s = b.sec.get(p)
            if s:
                o.append('@' + p)
                o.append(tirar_marcas(s))
    for b in t.exemplos:
        m = b.meta
        o.append('@E ' + '|'.join([m['nivel'], b.id, m['titulo'],
                                   m.get('calc', ''), m['licao']]))
        o.append(tirar_marcas(b.sec['T']))
    return '\n'.join(o) + '\n'


def gerar_exercicios(t):
    o = ['@V 1', '@N %d' % len(t.exercicios), '@T ' + t.titulo]
    for b in t.exercicios:
        m = b.meta
        o.append('@X ' + '|'.join([m['tipo'], b.id, m['licao'],
                                   m.get('modo', 'r'),
                                   m.get('unidades', '')]))
        o.append(tirar_marcas(b.sec['T']))
        if b.sec.get('O'):
            o.append('@O ' + '|'.join(tirar_marcas(x).strip() for x in
                                      b.sec['O'].split('\n') if x.strip()))
        o.append('@S ' + b.sec['S'].strip())
        o.append('@P ' + tirar_marcas(b.sec['P']).replace('\n', ' '))
        o.append('@D')
        o.append(tirar_marcas(b.sec['D']))
    return '\n'.join(o) + '\n'


def cartoes(t):
    n = sum(len(b.formulas) for b in t.licoes)
    n += sum(1 for b in t.licoes if b.sec.get('J'))
    return n


def gerar_catalogo(temas, calcs):
    o = []
    ol = oe = oc = 0
    for t in temas:
        nl = len(t.licoes)
        ne = len(t.exercicios)
        nc = cartoes(t)
        o.append('|'.join([t.id, t.disc, t.grupo, t.titulo, t.pacote,
                           t.pacote_x, str(nl), str(ol), str(ne), str(oe),
                           str(nc), str(oc), ' '.join(t.calcs),
                           ' '.join(b.id for b in t.licoes)]))
        ol += nl
        oe += ne
        oc += nc
    cab = ('# m1_cat.py - M1TR4M: catalogo gerado pelo build (nao editar).\n'
           '# TEMAS: id|disc|grupo|titulo|pacote|exercicios|n licoes|1.a licao|'
           'n exerc.|1.o exerc.|n cartoes|1.o cartao|calculadoras|licoes\n'
           '# CALC: id|nome|disciplina|tema (as palavras-chave estao no '
           'indice da pesquisa)\n')
    s = cab + 'NLIC = %d\nNEX = %d\nNCART = %d\n' % (ol, oe, oc)
    s += 'TEMAS = (\n'
    for x in o:
        s += '    "' + esc(x) + '",\n'
    s += ')\n'
    s += literal('CALC', '\n'.join('|'.join([c[0], c[1], c[3], c[4]])
                                    for c in calcs))
    return s


def norm(s):
    return N.low(s)


def sinonimos(txt):
    w = ' ' + txt + ' '
    extra = []
    for a, b in SINONIMOS:
        if ' ' + a + ' ' in w and b not in txt:
            extra.append(b)
        if ' ' + b + ' ' in w or b in txt:
            if ' ' + a + ' ' not in w:
                extra.append(a)
    return (txt + ' ' + ' '.join(extra)).strip()


def gerar_indice(temas, calcs, elementos, constantes):
    """Indice da pesquisa: TAG|disc|titulo|palavras|alvo."""
    o = []

    def add(tag, d, tit, pal, alvo):
        pal = sinonimos(' '.join(sorted(set(norm(pal).split()) -
                                        set(norm(tit).split()))))
        o.append('|'.join([tag, d, tit, pal, alvo]))
    for t in temas:
        for b in t.licoes:
            add('L', t.disc, b.meta['titulo'], b.meta['chave'], b.id)
        k = 0
        for b in t.licoes:
            for f in b.formulas:
                add('F', t.disc, f[0], '', t.id + ':' + str(k))
                k += 1
        for i, b in enumerate(t.exemplos):
            add('E', t.disc, b.meta['titulo'], '', t.id + ':' + str(i))
        for i, b in enumerate(t.exercicios):
            tit = b.meta.get('titulo') or tirar_marcas(
                b.sec['T']).split('\n')[0][:40]
            add('X', t.disc, tit, '', t.id + ':' + str(i))
    for c in calcs:
        add('C', c[3], c[1], c[2], c[0])
    for e in elementos:
        add('T', 'F', e['nome'], e['simbolo'].lower() + ' ' + e['z'],
            e['z'])
    for i, c in enumerate(constantes):
        add('K', 'F', c[0], c[1], str(i))
    cab = ('# m1_idx.py - M1TR4M: indice da pesquisa gerado pelo build.\n'
           '# Cada linha: etiqueta|disciplina|titulo|palavras|alvo\n')
    return cab + literal('D', '@V 1\n@N %d\n' % len(o) + '\n'.join(o))
