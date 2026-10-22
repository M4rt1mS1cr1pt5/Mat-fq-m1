# Testes do leitor de pacotes com um pacote pequeno.
import m1_cont as C

D = ('@V 1\n@N 2\n@T Teste\n'
     '@L a1|Primeira|x y|c_comu.sci|10|núcleo|||AE\n@A\n- objetivo\n'
     '@B\nintuição\n@F Nome|E = m c²|E: energia;m: massa|sempre|ex|\n'
     '@J\npergunta\n@R\nresposta\n@I\n- resumo\n'
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
