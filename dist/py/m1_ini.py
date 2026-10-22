# m1_ini.py - M1TR4M: arranque (carregado so no inicio e libertado a
# seguir). Le as definicoes e o progresso guardados e mostra o ecra
# inicial: animacao curta (max. 2 s) com o atomo, o nome em letras
# grandes e a legenda; qualquer tecla salta a animacao.

import m1_plat as P
import m1_nucleo as N
import m1_ui as U
import m1_app as A
import m1_cat as K

S = A.S


def start():
    load_state()
    splash()


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
    c = _ld('m1def', len(A.DEF) - 1)
    if len(c) != len(A.DEF) or c[1] == 0 and c[8] == 0:
        c = list(A.DEF)
    S['cfg'] = c
    S['ex'] = _ld('m1prog', K.NEX)
    S['lic'] = _ld('m1lic', K.NLIC)
    S['tst'] = _ld('m1tst', 2 * len(K.TEMAS))
    S['rev'] = _ld('m1rev', K.NCART)
    S['pos'] = _ld('m1pos', 4)
    A.apply_cfg()


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
