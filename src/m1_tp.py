# m1_tp.py - M1TR4M: tabela periodica (dados e ecra). Carregado a pedido.
# Grelha de 18 colunas com cursor; pesquisa por nome, simbolo ou Z;
# filtros por grupo, periodo e bloco; ficha de cada elemento com fonte.
# Os dados (TD) sao gerados de dados/elementos.csv por
# ferramentas/dados.py: Z|simbolo|nome|Ar|grupo|periodo|bloco|tipo|
# estado|raio (pm)|energia de 1.a ionizacao (kJ/mol).

import m1_plat as P
import m1_nucleo as N
import m1_ui as U
import m1_app as A

VER = 1
# --- dados (gerado) ---
TD = "1|H|Hidrog\u00e9nio|1.008|1|1|s|n\u00e3o metal|g\u00e1s|53|1312\n\
2|He|H\u00e9lio|4.0026|18|1|s|g\u00e1s nobre|g\u00e1s|31|2372\n\
3|Li|L\u00edtio|6.94|1|2|s|metal alcalino|s\u00f3lido|167|520\n\
4|Be|Ber\u00edlio|9.0122|2|2|s|metal alcalinoterroso|s\u00f3lido|112|900\n\
5|B|Boro|10.81|13|2|p|semimetal|s\u00f3lido|87|801\n\
6|C|Carbono|12.011|14|2|p|n\u00e3o metal|s\u00f3lido|67|1086\n\
7|N|Azoto|14.007|15|2|p|n\u00e3o metal|g\u00e1s|56|1402\n\
8|O|Oxig\u00e9nio|15.999|16|2|p|n\u00e3o metal|g\u00e1s|48|1314\n\
9|F|Fl\u00faor|18.998|17|2|p|halog\u00e9neo|g\u00e1s|42|1681\n\
10|Ne|N\u00e9on|20.180|18|2|p|g\u00e1s nobre|g\u00e1s|38|2081\n\
11|Na|S\u00f3dio|22.990|1|3|s|metal alcalino|s\u00f3lido|190|496\n\
12|Mg|Magn\u00e9sio|24.305|2|3|s|metal alcalinoterroso|s\u00f3lido|145|738\n\
13|Al|Alum\u00ednio|26.982|13|3|p|metal|s\u00f3lido|118|578\n\
14|Si|Sil\u00edcio|28.085|14|3|p|semimetal|s\u00f3lido|111|787\n\
15|P|F\u00f3sforo|30.974|15|3|p|n\u00e3o metal|s\u00f3lido|98|1012\n\
16|S|Enxofre|32.06|16|3|p|n\u00e3o metal|s\u00f3lido|88|1000\n\
17|Cl|Cloro|35.45|17|3|p|halog\u00e9neo|g\u00e1s|79|1251\n\
18|Ar|\u00c1rgon|39.95|18|3|p|g\u00e1s nobre|g\u00e1s|71|1521\n\
19|K|Pot\u00e1ssio|39.098|1|4|s|metal alcalino|s\u00f3lido|243|419\n\
20|Ca|C\u00e1lcio|40.078|2|4|s|metal alcalinoterroso|s\u00f3lido|194|590\n\
21|Sc|Esc\u00e2ndio|44.956|3|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|184|633\n\
22|Ti|Tit\u00e2nio|47.867|4|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|176|659\n\
23|V|Van\u00e1dio|50.942|5|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|171|651\n\
24|Cr|Cr\u00f3mio|51.996|6|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|166|653\n\
25|Mn|Mangan\u00eas|54.938|7|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|161|717\n\
26|Fe|Ferro|55.845|8|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|156|762\n\
27|Co|Cobalto|58.933|9|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|152|760\n\
28|Ni|N\u00edquel|58.693|10|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|149|737\n\
29|Cu|Cobre|63.546|11|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|145|745\n\
30|Zn|Zinco|65.38|12|4|d|metal de transi\u00e7\u00e3o|s\u00f3lido|142|906\n\
31|Ga|G\u00e1lio|69.723|13|4|p|metal|s\u00f3lido|136|579\n\
32|Ge|Germ\u00e2nio|72.630|14|4|p|semimetal|s\u00f3lido|125|762\n\
33|As|Ars\u00e9nio|74.922|15|4|p|semimetal|s\u00f3lido|114|947\n\
34|Se|Sel\u00e9nio|78.971|16|4|p|n\u00e3o metal|s\u00f3lido|103|941\n\
35|Br|Bromo|79.904|17|4|p|halog\u00e9neo|l\u00edquido|94|1140\n\
36|Kr|Cr\u00edpton|83.798|18|4|p|g\u00e1s nobre|g\u00e1s|88|1351\n\
37|Rb|Rub\u00eddio|85.468|1|5|s|metal alcalino|s\u00f3lido|265|403\n\
38|Sr|Estr\u00f4ncio|87.62|2|5|s|metal alcalinoterroso|s\u00f3lido|219|550\n\
39|Y|\u00cdtrio|88.906|3|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|212|600\n\
40|Zr|Zirc\u00f3nio|91.224|4|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|206|640\n\
41|Nb|Ni\u00f3bio|92.906|5|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|198|652\n\
42|Mo|Molibd\u00e9nio|95.95|6|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|190|684\n\
43|Tc|Tecn\u00e9cio|[98]|7|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|183|702\n\
44|Ru|Rut\u00e9nio|101.07|8|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|178|710\n\
45|Rh|R\u00f3dio|102.91|9|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|173|720\n\
46|Pd|Pal\u00e1dio|106.42|10|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|169|804\n\
47|Ag|Prata|107.87|11|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|165|731\n\
48|Cd|C\u00e1dmio|112.41|12|5|d|metal de transi\u00e7\u00e3o|s\u00f3lido|161|868\n\
49|In|\u00cdndio|114.82|13|5|p|metal|s\u00f3lido|156|558\n\
50|Sn|Estanho|118.71|14|5|p|metal|s\u00f3lido|145|709\n\
51|Sb|Antim\u00f3nio|121.76|15|5|p|semimetal|s\u00f3lido|133|834\n\
52|Te|Tel\u00fario|127.60|16|5|p|semimetal|s\u00f3lido|123|869\n\
53|I|Iodo|126.90|17|5|p|halog\u00e9neo|s\u00f3lido|115|1008\n\
54|Xe|X\u00e9non|131.29|18|5|p|g\u00e1s nobre|g\u00e1s|108|1170\n\
55|Cs|C\u00e9sio|132.91|1|6|s|metal alcalino|s\u00f3lido||\n\
56|Ba|B\u00e1rio|137.33|2|6|s|metal alcalinoterroso|s\u00f3lido||\n\
57|La|Lant\u00e2nio|138.91|3|6|d|lantan\u00eddeo|s\u00f3lido||\n\
58|Ce|C\u00e9rio|140.12||6|f|lantan\u00eddeo|s\u00f3lido||\n\
59|Pr|Praseod\u00edmio|140.91||6|f|lantan\u00eddeo|s\u00f3lido||\n\
60|Nd|Neod\u00edmio|144.24||6|f|lantan\u00eddeo|s\u00f3lido||\n\
61|Pm|Prom\u00e9cio|[145]||6|f|lantan\u00eddeo|s\u00f3lido||\n\
62|Sm|Sam\u00e1rio|150.36||6|f|lantan\u00eddeo|s\u00f3lido||\n\
63|Eu|Eur\u00f3pio|151.96||6|f|lantan\u00eddeo|s\u00f3lido||\n\
64|Gd|Gadol\u00ednio|157.25||6|f|lantan\u00eddeo|s\u00f3lido||\n\
65|Tb|T\u00e9rbio|158.93||6|f|lantan\u00eddeo|s\u00f3lido||\n\
66|Dy|Dispr\u00f3sio|162.50||6|f|lantan\u00eddeo|s\u00f3lido||\n\
67|Ho|H\u00f3lmio|164.93||6|f|lantan\u00eddeo|s\u00f3lido||\n\
68|Er|\u00c9rbio|167.26||6|f|lantan\u00eddeo|s\u00f3lido||\n\
69|Tm|T\u00falio|168.93||6|f|lantan\u00eddeo|s\u00f3lido||\n\
70|Yb|It\u00e9rbio|173.05||6|f|lantan\u00eddeo|s\u00f3lido||\n\
71|Lu|Lut\u00e9cio|174.97||6|f|lantan\u00eddeo|s\u00f3lido||\n\
72|Hf|H\u00e1fnio|178.49|4|6|d|metal de transi\u00e7\u00e3o|s\u00f3lido||\n\
73|Ta|T\u00e2ntalo|180.95|5|6|d|metal de transi\u00e7\u00e3o|s\u00f3lido||\n\
74|W|Tungst\u00e9nio|183.84|6|6|d|metal de transi\u00e7\u00e3o|s\u00f3lido||\n\
75|Re|R\u00e9nio|186.21|7|6|d|metal de transi\u00e7\u00e3o|s\u00f3lido||\n\
76|Os|\u00d3smio|190.23|8|6|d|metal de transi\u00e7\u00e3o|s\u00f3lido||\n\
77|Ir|Ir\u00eddio|192.22|9|6|d|metal de transi\u00e7\u00e3o|s\u00f3lido||\n\
78|Pt|Platina|195.08|10|6|d|metal de transi\u00e7\u00e3o|s\u00f3lido||\n\
79|Au|Ouro|196.97|11|6|d|metal de transi\u00e7\u00e3o|s\u00f3lido||\n\
80|Hg|Merc\u00fario|200.59|12|6|d|metal de transi\u00e7\u00e3o|l\u00edquido||\n\
81|Tl|T\u00e1lio|204.38|13|6|p|metal|s\u00f3lido||\n\
82|Pb|Chumbo|207.2|14|6|p|metal|s\u00f3lido||\n\
83|Bi|Bismuto|208.98|15|6|p|metal|s\u00f3lido||\n\
84|Po|Pol\u00f3nio|[209]|16|6|p|metal|s\u00f3lido||\n\
85|At|\u00c1stato|[210]|17|6|p|halog\u00e9neo|s\u00f3lido||\n\
86|Rn|R\u00e1don|[222]|18|6|p|g\u00e1s nobre|g\u00e1s||\n\
87|Fr|Fr\u00e2ncio|[223]|1|7|s|metal alcalino|s\u00f3lido||\n\
88|Ra|R\u00e1dio|[226]|2|7|s|metal alcalinoterroso|s\u00f3lido||\n\
89|Ac|Act\u00ednio|[227]|3|7|d|act\u00ednideo|s\u00f3lido||\n\
90|Th|T\u00f3rio|232.04||7|f|act\u00ednideo|s\u00f3lido||\n\
91|Pa|Protact\u00ednio|231.04||7|f|act\u00ednideo|s\u00f3lido||\n\
92|U|Ur\u00e2nio|238.03||7|f|act\u00ednideo|s\u00f3lido||\n\
93|Np|Nept\u00fanio|[237]||7|f|act\u00ednideo|s\u00f3lido||\n\
94|Pu|Plut\u00f3nio|[244]||7|f|act\u00ednideo|s\u00f3lido||\n\
95|Am|Amer\u00edcio|[243]||7|f|act\u00ednideo|s\u00f3lido||\n\
96|Cm|C\u00fario|[247]||7|f|act\u00ednideo|s\u00f3lido||\n\
97|Bk|Berqu\u00e9lio|[247]||7|f|act\u00ednideo|s\u00f3lido||\n\
98|Cf|Calif\u00f3rnio|[251]||7|f|act\u00ednideo|s\u00f3lido||\n\
99|Es|Einst\u00e9nio|[252]||7|f|act\u00ednideo|s\u00f3lido||\n\
100|Fm|F\u00e9rmio|[257]||7|f|act\u00ednideo|desconhecido||\n\
101|Md|Mendel\u00e9vio|[258]||7|f|act\u00ednideo|desconhecido||\n\
102|No|Nob\u00e9lio|[259]||7|f|act\u00ednideo|desconhecido||\n\
103|Lr|Laur\u00eancio|[262]||7|f|act\u00ednideo|desconhecido||\n\
104|Rf|Rutherf\u00f3rdio|[267]|4|7|d|metal de transi\u00e7\u00e3o (previsto)|desconhecido||\n\
105|Db|D\u00fabnio|[268]|5|7|d|metal de transi\u00e7\u00e3o (previsto)|desconhecido||\n\
106|Sg|Seab\u00f3rgio|[269]|6|7|d|metal de transi\u00e7\u00e3o (previsto)|desconhecido||\n\
107|Bh|B\u00f3hrio|[270]|7|7|d|metal de transi\u00e7\u00e3o (previsto)|desconhecido||\n\
108|Hs|H\u00e1ssio|[269]|8|7|d|metal de transi\u00e7\u00e3o (previsto)|desconhecido||\n\
109|Mt|Meitn\u00e9rio|[278]|9|7|d|metal de transi\u00e7\u00e3o (previsto)|desconhecido||\n\
110|Ds|Darmst\u00e1cio|[281]|10|7|d|metal de transi\u00e7\u00e3o (previsto)|desconhecido||\n\
111|Rg|Roentg\u00e9nio|[282]|11|7|d|metal de transi\u00e7\u00e3o (previsto)|desconhecido||\n\
112|Cn|Copern\u00edcio|[285]|12|7|d|metal de transi\u00e7\u00e3o (previsto)|desconhecido||\n\
113|Nh|Nip\u00f3nio|[286]|13|7|p|metal (previsto)|desconhecido||\n\
114|Fl|Fler\u00f3vio|[289]|14|7|p|metal (previsto)|desconhecido||\n\
115|Mc|Mosc\u00f3vio|[290]|15|7|p|metal (previsto)|desconhecido||\n\
116|Lv|Liverm\u00f3rio|[293]|16|7|p|metal (previsto)|desconhecido||\n\
117|Ts|Tenesso|[294]|17|7|p|halog\u00e9neo (previsto)|desconhecido||\n\
118|Og|Ogan\u00e9sson|[294]|18|7|p|g\u00e1s nobre (previsto)|desconhecido||"
# --- fim dos dados ---
FONTES = ('Ar: IUPAC (valores abreviados); [n] = n.\u00ba de massa do is\u00f3topo '
          'mais est\u00e1vel. Raio: calculado (Clementi e outros, 1967). '
          'Energia de ioniza\u00e7\u00e3o: NIST, convertida para kJ/mol.')
ORB = ('1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p')
CAP = (2, 2, 6, 2, 6, 2, 10, 6)
# cor de fundo de cada tipo (indice da paleta): s, p, d, f
BC = {'s': 8, 'p': 9, 'd': 1, 'f': 9}


def rows():
    return [ln.split('|') for ln in TD.split('\n') if ln]


def el(z):
    # Campos do elemento de numero atomico z (a 1.a linha nao tem '\n'
    # antes, por isso find devolve -1 e o corte comeca em 0).
    i = TD.find('\n' + str(z) + '|') if z > 1 else -1
    j = TD.find('\n', i + 1)
    return TD[i + 1:j if j > 0 else len(TD)].split('|')


def cell(e):
    # Posicao na grelha (linha, coluna) de um elemento.
    z = int(e[0])
    if e[4] == '':
        return (7 if z < 89 else 8), z - (55 if z < 89 else 87)
    return int(e[5]) - 1, int(e[4]) - 1


def conf(z):
    # Configuracao eletronica (Z <= 36) pela ordem de energia.
    if z > 36:
        return ''
    o = []
    r = z
    for i in range(len(ORB)):
        if r <= 0:
            break
        n = min(r, CAP[i])
        o.append([ORB[i], n])
        r -= n
    if z in (24, 29):
        for x in o:
            if x[0] == '4s':
                x[1] = 1
            if x[0] == '3d':
                x[1] += 1
    return ' '.join([x[0] + N.sup(x[1]) for x in o])


def valence(e):
    b = e[6]
    if b == 's' or b == 'p':
        g = int(e[4])
        return str(g if g <= 2 else g - 10) if int(e[0]) > 2 else e[0]
    return ''


def ar2(e):
    # Ar com 2 casas (como na tabela do exame) ou o n.o de massa.
    a = e[3]
    if a.startswith('['):
        return a
    return N.fmt(N._fl(a), 0, 2)


def sheet(z):
    e = el(z)
    s = ['# ' + e[2] + ' (' + e[1] + ')',
         'N\u00famero at\u00f3mico: Z = ' + e[0],
         'Massa at\u00f3mica relativa: Ar = ' + e[3].replace('.', ',') +
         ('' if e[3].startswith('[') else ' (tabela do exame: ' + ar2(e) + ')')]
    if e[4]:
        s.append('Grupo ' + e[4] + ', per\u00edodo ' + e[5] + ', bloco ' + e[6])
    else:
        s.append('Per\u00edodo ' + e[5] + ', bloco ' + e[6] + ' (s\u00e9rie dos ' +
                 ('lantan\u00eddeos)' if z < 89 else 'act\u00ednideos)'))
    s.append('Tipo: ' + e[7])
    s.append('Estado f\u00edsico a 25 \u00b0C: ' + e[8])
    c = conf(z)
    if c:
        s.append('Configura\u00e7\u00e3o eletr\u00f3nica: ' + c +
                 (' (al\u00e9m do programa: o 10.\u00ba ano vai at\u00e9 4s)' if z > 20
                  else ''))
        v = valence(e)
        if v and z <= 20:
            s.append('Eletr\u00f5es de val\u00eancia: ' + v)
    if e[9]:
        s.append('Raio at\u00f3mico: ' + e[9] + ' pm')
        s.append('Energia de 1.\u00aa ioniza\u00e7\u00e3o: ' + e[10] + ' kJ/mol')
    else:
        s.append('Raio e energia de ioniza\u00e7\u00e3o: sem dados nesta app.')
    s.append('')
    s.append('Fontes: ' + FONTES)
    U.text(e[2], '\n'.join(s))


def find(q):
    # Elemento por Z, simbolo ou nome (sem acentos); 0 se nao existe.
    q = q.strip()
    if q.isdigit():
        z = int(q)
        return z if 1 <= z <= 118 else 0
    lq = N.low(q)
    best = 0
    for e in rows():
        if e[1].lower() == lq:
            return int(e[0])
        if not best and N.low(e[2]).startswith(lq):
            best = int(e[0])
    return best


def run():
    if not P.E['g']:
        while True:
            q = U.edit('Tabela peri\u00f3dica', 'Nome, s\u00edmbolo ou n\u00famero '
                       'at\u00f3mico do elemento:', '')
            if q is None:
                return
            z = find(q)
            if z:
                sheet(z)
            else:
                U.msg('Tabela peri\u00f3dica', 'Elemento n\u00e3o encontrado: ' + q)
    es = rows()
    grid = {}
    for e in es:
        grid[cell(e)] = e
    r, c = 0, 0
    flt = 0
    q = ''
    cw = 17
    ch = 15
    x0 = (P.E['W'] - 18 * cw) // 2
    y0 = P.E['lh'] + 2
    while True:
        A.S['where'] = 'tabela peri\u00f3dica'
        cur = grid[(r, c)]
        P.begin()
        U.title('Tabela peri\u00f3dica', ('', 'grupo ' + cur[4], 'per\u00edodo ' + cur[5],
                                       'bloco ' + cur[6])[flt])
        for (rr, cc), e in grid.items():
            x = x0 + cc * cw
            y = y0 + rr * ch + (4 if rr >= 7 else 0)
            on = flt == 0 or flt == 1 and e[4] == cur[4] and e[4] or \
                flt == 2 and e[5] == cur[5] and rr < 7 or \
                flt == 3 and e[6] == cur[6]
            if (rr, cc) == (r, c):
                P.rect(x, y, cw - 1, ch - 1, 2)
                P.txt(x + 1, y - 2, e[1], 10)
            else:
                P.rect(x, y, cw - 1, ch - 1, BC[e[6]] if on else 1)
                P.txt(x + 1, y - 2, e[1], 0 if on else 9)
        info = cur[0] + ' ' + cur[1] + ' ' + cur[2] + '  Ar ' + ar2(cur)
        P.put(0, 10, U.clip(info, U.cols()), 2)
        U.foot(('procura: ' + q + '_' if q else 'setas \u00b7 enter: ficha') +
               ' \u00b7 tab: filtro \u00b7 esc')
        P.show()
        k = P.key()
        if k == 'esc':
            if q:
                q = ''
                continue
            return
        if k == 'enter':
            if q:
                z = find(q)
                q = ''
                if z:
                    r, c = cell(el(z))
                else:
                    U.hint('Elemento n\u00e3o encontrado')
                continue
            sheet(int(cur[0]))
        elif k == 'tab':
            flt = (flt + 1) % 4
        elif k == 'del':
            q = q[:-1]
        elif k in ('left', 'right'):
            d = -1 if k == 'left' else 1
            cc = c + d
            while 0 <= cc < 18 and (r, cc) not in grid:
                cc += d
            if 0 <= cc < 18:
                c = cc
        elif k in ('up', 'down'):
            d = -1 if k == 'up' else 1
            rr = r + d
            while 0 <= rr < 9:
                if (rr, c) in grid:
                    r = rr
                    break
                if rr >= 7 or r >= 7:
                    cs = [cc for (a, cc) in grid if a == rr]
                    if cs:
                        c = min(cs, key=lambda x: (abs(x - c), x))
                        r = rr
                        break
                rr += d
        elif len(k) == 1 and (k.isalpha() or '0' <= k <= '9') and len(q) < 12:
            q = q + k
