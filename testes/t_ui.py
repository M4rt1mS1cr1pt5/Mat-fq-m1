# Testes do texto partido em linhas (o que decide se o texto cabe).
import m1_ui as U


def t_wrap_palavras():
    ls = U.wrap('um dois tres quatro cinco seis sete oito', 10)
    for st, t in ls:
        assert len(t) <= 10
    assert [t for s, t in ls] == ['um dois', 'tres', 'quatro', 'cinco seis',
                                  'sete oito']


def t_wrap_recuo():
    ls = U.wrap('- um texto com recuo nas linhas seguintes', 12)
    assert ls[0][1].startswith('- ')
    for s, t in ls[1:]:
        assert t.startswith('  ')


def t_wrap_formula():
    ls = U.wrap('= Ec = 1/2 × m × v² = 1/2 × 2,0 kg × (3,0 m/s)² '
                '= 9,0 J', 24)
    for st, t in ls:
        assert st == 3
        assert len(t) <= 24
    assert ls[1][1][0] in '=×+-'


def t_wrap_palavra_grande():
    ls = U.wrap('x' * 25, 10)
    assert [len(t) for s, t in ls] == [10, 10, 5]


def t_wrap_estilos():
    ls = U.wrap('> resultado\n! erro\n+ certo\n# titulo\nnormal', 40)
    assert [s for s, t in ls] == [4, 5, 6, 2, 0]
    assert ls[0][1] == 'resultado'
