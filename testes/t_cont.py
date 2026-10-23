# Testes do leitor de pacotes com um pacote pequeno.
import m1_cont as C

D = ('@V 1\n@N 2\n@T Teste\n'
     '@L a1|Primeira|x y|c_comu.sci|10|núcleo|||AE\n@A\n- objetivo\n'
     '@B\nintuição\n@F Nome|E = m c²|E: energia;m: massa|sempre|ex|\n'
     '@F\nexemplo resolvido\n@J\npergunta\n@R\nresposta\n@I\n- resumo\n'
     '@L a2|Segunda|z||10|núcleo|||AE\n@A\n- outro\n@J\np2\n@R\nr2\n'
     '@E 1|e1|Exemplo um|c_comu.sci|a1\ntexto do exemplo\n'
     '@X m|x1|a1|r|\nenunciado\n@O a|b|c|d\n@S 2\n@P pista\n@D\nresolução\n')


def t_head():
    assert C.head(D, 'V') == '1'
    assert C.head(D, 'N') == '2'


def t_recs():
    ls = C.recs(D, 'L')
    assert [h[0] for h, p in ls] == ['a1', 'a2']
    assert C.recs(D, 'E')[0][0][2] == 'Exemplo um'
    assert C.recs(D, 'F')[0][0][0] == 'Nome'


def t_lesson():
    h, pg, ans, fs = C.lesson(D, 'a1')
    assert h[1] == 'Primeira'
    assert pg[0] == '- objetivo'
    assert 'E = m c²' in pg[4]
    assert pg[9] == 'pergunta'
    assert pg[5] == 'exemplo resolvido'
    assert ans == 'resposta'
    assert len(fs) == 1
    h, pg, ans, fs = C.lesson(D, 'a2')
    assert pg[9] == 'p2' and ans == 'r2' and pg[4] == ''


def t_exercicio():
    h, pos = C.recs(D, 'X')[0]
    d = C.parts(C.body(D, pos))
    assert h[0] == 'm' and h[1] == 'x1'
    assert d['T'] == 'enunciado'
    assert d['O'] == 'a|b|c|d'
    assert d['S'] == '2'
    assert d['D'] == 'resolução'


def t_exemplo():
    h, pos = C.recs(D, 'E')[0]
    assert C.body(D, pos) == 'texto do exemplo'


def t_falta():
    try:
        C.lesson(D, 'zz')
    except C.Falta:
        return
    raise AssertionError('esperava Falta')


def t_check():
    # Versao e numero de licoes (@N 2 e duas licoes @L): aceita.
    C.check(D, 't')
    for d, err in ((D.replace('@V 1', '@V 2'), 'desatualizado'),
                   (D.replace('@N 2', '@N 3'), 'estragado'),
                   (D.replace('@N 2', '@N x'), 'estragado')):
        try:
            C.check(d, 't')
        except C.Falta as e:
            assert err in str(e), str(e)
            continue
        raise AssertionError('esperava Falta: ' + err)
    # Indice da pesquisa: @N conta as entradas (sem @L nem @X).
    C.check(IDX, 'i')


# ------------------------------------------------------------ pesquisa
IDX = ('@V 1\n@N 4\nL|Função quadrática|vertice parabola|m5a\n'
       'F|Fórmula resolvente||m5:2\n'
       'C|Equação do 2.º grau|quadratica zeros|c_matq.q2\n'
       'X|Quadrática com zeros 2 e 3||m5:0')


def t_pesq_ordem():
    import m1_pesq as Q
    L = Q.fold(IDX)
    assert len(L) == len(IDX)
    r = Q.find(L, 'quadratica', 0, [])
    r.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
    # titulo que comeca pela pesquisa, palavra do titulo, palavra-chave
    assert [x[0] for x in r] == [1, 2, 4]
    assert r[0][1] == 'quadratica com zeros 2 e 3'
    assert IDX[r[2][3]:].startswith('C|')


def t_pesq_campos():
    import m1_pesq as Q
    L = Q.fold(IDX)
    # 'm5' so aparece nos alvos: nao conta
    assert Q.find(L, 'm5', 0, []) == []
    assert Q.find(L, 'formula resolvente', 1, [])[0][:3] == (
        0, 'formula resolvente', 1)
    # palavra do titulo antes de palavra-chave
    assert sorted([x[0] for x in Q.find(L, 'zeros', 0, [])]) == [2, 4]
