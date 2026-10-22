# Testes ao acaso (com semente fixa, iguais nos dois Pythons):
# 400 equacoes do 2.o grau e conversoes de unidades de ida e volta.
import math
import m1_nucleo as N
import c_matq
from base import calc

SEM = [12345]


def rnd(a, b):
    SEM[0] = (SEM[0] * 1103515245 + 12345) % 2147483648
    return a + SEM[0] % (b - a + 1)


def t_400_equacoes():
    SEM[0] = 12345
    for i in range(400):
        a = rnd(-9, 9) or 1
        b = rnd(-20, 20)
        c = rnd(-20, 20)
        zs, d, dt = c_matq.roots(a, b, c, (a, 1), (b, 1), (c, 1))
        assert d == b * b - 4 * a * c, (a, b, c)
        if d < 0:
            assert zs == []
            continue
        assert len(zs) == (1 if d == 0 else 2)
        for x, t in zs:
            assert abs(a * x * x + b * x + c) < 1e-9 * max(1, abs(b), abs(c)), \
                (a, b, c, x)
            assert t is not None
        r = calc(c_matq, 'q2', [str(a), str(b), str(c)])
        assert 'C.S.' in r[0]


def t_conversoes_ida_volta():
    for cat in 'LMtAVTEWpncmdvFIURfQ':
        us = N.ulist(cat)
        assert len(us) >= 2, cat
        for u1 in us:
            for u2 in us:
                v = N.conv(N.conv(3.7, u1, u2, cat), u2, u1, cat)
                assert abs(v - 3.7) < 1e-9, (cat, u1, u2, v)


def t_formatar_ler():
    # Ida e volta: o texto formatado le-se de novo com o mesmo valor.
    SEM[0] = 999
    for i in range(300):
        m = rnd(1, 999999)
        e = rnd(-12, 12)
        x = m * math.pow(10, e - 5)
        for sf in (2, 3, 4):
            s = N.fsf(x, sf)
            v = N.num(s.replace(' ', ''))[0]
            assert abs(v - x) <= 0.51 * math.pow(10, N._e10(x) - sf + 1), \
                (x, sf, s, v)
