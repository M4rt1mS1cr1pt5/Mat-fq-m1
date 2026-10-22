# m1_cfg.py - M1TR4M: definicoes, ajuda, sobre e diagnostico.
# Carregado a pedido. As definicoes ficam guardadas com store_list
# ("m1def"); o Diagnostico mostra o que a app detetou no aparelho para o
# aluno fotografar e reportar problemas.

import m1_plat as P
import m1_nucleo as N
import m1_ui as U
import m1_cont as C
import m1_app as A

VER = 1


def run():
    while True:
        A.S['where'] = 'defini\u00e7\u00f5es'
        r = U.menu('Defini\u00e7\u00f5es, ajuda e Diagn\u00f3stico',
                   ['Defini\u00e7\u00f5es', 'Ajuda', 'Sobre a M1TR4M',
                    'Diagn\u00f3stico'])
        if r < 0:
            return
        (settings, help_, about, diag)[r]()

# ------------------------------------------------------------ definicoes


def settings():
    sel = 0
    while True:
        c = A.S['cfg']
        it = ['Casas decimais em Matem\u00e1tica: ' + str(c[1]),
              'Alg. significativos autom\u00e1ticos em FQ: ' +
              ('sim' if c[2] else 'n\u00e3o'),
              'Nota\u00e7\u00e3o cient\u00edfica a partir de 10' + N.sup(c[3]),
              'Unidade angular: ' + ('graus' if c[4] == 0 else 'radianos'),
              'Valor de g: ' + A.GT[c[5]],
              'Toler\u00e2ncia dos exerc\u00edcios: ' + A.TT[c[6]],
              'Acentos e s\u00edmbolos: ' + ('completos', 's\u00f3 Latin-1',
                                            'letras simples')[2 - c[7]],
              'Calibra\u00e7\u00e3o do texto no ecr\u00e3',
              'Apagar o progresso',
              'Repor as predefini\u00e7\u00f5es']
        r = U.menu('Defini\u00e7\u00f5es', it, sel)
        if r < 0:
            A.save('m1def')
            return
        sel = r
        if r == 0:
            k = U.menu('Casas decimais', [str(i) for i in range(11)], c[1])
            if k >= 0:
                c[1] = k
        elif r == 1:
            c[2] = 1 - c[2]
        elif r == 2:
            ops = (3, 4, 5, 6, 9)
            k = U.menu('Nota\u00e7\u00e3o cient\u00edfica', ['|x| \u2265 10' + N.sup(v)
                                                       for v in ops])
            if k >= 0:
                c[3] = ops[k]
        elif r == 3:
            c[4] = 1 - c[4]
        elif r == 4:
            k = U.menu('Valor de g', list(A.GT), c[5])
            if k >= 0:
                c[5] = k
        elif r == 5:
            k = U.menu('Toler\u00e2ncia', list(A.TT), c[6])
            if k >= 0:
                c[6] = k
        elif r == 6:
            k = U.menu('Acentos e s\u00edmbolos', ['Completos (\u221a \u03c0 \u2248 \u00b2)',
                                              'S\u00f3 Latin-1 (\u00e1 \u00e7 \u00b2)',
                                              'Letras simples (a c ^2)'],
                       2 - c[7])
            if k >= 0:
                c[7] = 2 - k
        elif r == 7:
            calib()
        elif r == 8:
            A.wipe()
            continue
        else:
            if U.ask('Predefini\u00e7\u00f5es', 'Repor todas as defini\u00e7\u00f5es?'):
                A.S['cfg'] = list(A.DEF)
        A.apply_cfg()
        A.save('m1def')


def calib():
    # Regua para acertar as metricas do texto (setas e + -).
    c = A.S['cfg']
    cw, lh, dy = c[8], c[9], c[10]
    while True:
        P.metrics(cw, lh, dy)
        P.begin()
        U.title('Calibra\u00e7\u00e3o do texto')
        y = 2 * lh
        for i in range(0, P.E['W'], 10):
            P.line(i, y, i, y + (6 if i % 50 == 0 else 3), 5)
        P.line(0, y, P.E['W'], y, 5)
        n = P.E['cols']
        P.put(0, 3, 'M' * n, 0)
        P.put(0, 4, ('0123456789' * (n // 10 + 1))[:n], 0)
        for r in range(3, 6):
            P.line(0, r * lh, P.E['W'], r * lh, 9)
        P.put(0, 6, 'cw=' + str(cw) + ' lh=' + str(lh) + ' dy=' + str(dy) +
              ' colunas=' + str(n), 2)
        P.put(0, 7, '\u25c2\u25b8 largura \u00b7 \u25b4\u25be altura \u00b7 + - base', 7)
        P.put(0, 8, 'Os M devem acabar antes da margem.', 7)
        U.foot('enter: guardar \u00b7 esc: cancelar')
        P.show()
        k = P.key()
        if k == 'left':
            cw = max(5, cw - 1)
        elif k == 'right':
            cw = min(12, cw + 1)
        elif k == 'up':
            lh = max(12, lh - 1)
        elif k == 'down':
            lh = min(24, lh + 1)
        elif k == '+':
            dy += 1
        elif k == '-':
            dy -= 1
        elif k == 'enter':
            c[8], c[9], c[10] = cw, lh, dy
            A.save('m1def')
            return
        elif k == 'esc':
            P.metrics(c[8], c[9], c[10])
            return

# ------------------------------------------------------------ ajuda


AJ = (('Teclas e navega\u00e7\u00e3o',
       '- n\u00famero: escolhe a op\u00e7\u00e3o (1 e depois 2 escolhe a 12)\n'
       '- setas \u25b4\u25be: mudam a op\u00e7\u00e3o ou deslizam o texto\n'
       '- setas \u25c2\u25b8: p\u00e1gina anterior ou seguinte\n'
       '- enter: confirma; num texto longo, avan\u00e7a\n'
       '- esc ou 0: volta ao ecr\u00e3 anterior\n'
       '- del: apaga um car\u00e1cter; clear: limpa o campo\n'
       '- shift: uma mai\u00fascula; tab: fixa as mai\u00fasculas\n'
       'O rodap\u00e9 diz sempre o que fazem enter e esc.'),
      ('N\u00fameros e express\u00f5es',
       'N\u00fameros: 2,5 ou 2.5; fra\u00e7\u00f5es 3/4; nota\u00e7\u00e3o cient\u00edfica 6,02e23 '
       'ou 6,02*10^23.\n'
       'Express\u00f5es: + - * / ^, par\u00eanteses, |x| (m\u00f3dulo), pi, sqrt( ) '
       'ou \u221a, sin cos tan (tamb\u00e9m sen e tg).\n'
       'Multiplica\u00e7\u00e3o impl\u00edcita: 2x e 3(x+1).\n'
       'ans \u00e9 o \u00faltimo resultado de uma calculadora.\n'
       'Listas de dados: separa os valores com ; (2,5; 3,1; 4).'),
      ('Unidades e f\u00f3rmulas qu\u00edmicas',
       'Nas calculadoras, escolhe a unidade de cada campo com \u25c2\u25b8 '
       '(quando h\u00e1 mais do que uma).\n'
       'F\u00f3rmulas qu\u00edmicas: mai\u00fasculas e min\u00fasculas como na tabela: '
       'H2SO4, Ca(OH)2, CuSO4.5H2O (o ponto separa a \u00e1gua de '
       'hidrata\u00e7\u00e3o). Co \u00e9 cobalto; CO \u00e9 mon\u00f3xido de carbono.'),
      ('Gravar o progresso',
       'A app guarda as defini\u00e7\u00f5es e o progresso em vari\u00e1veis do '
       'documento (m1def, m1prog...).\n'
       'Para ficarem guardados de vez, grava o documento: ctrl+S '
       '(ou menu Ficheiro > Guardar) antes de o fechar.'),
      ('Modo de exame',
       'Em modo de exame (Press-to-Test) a calculadora torna os '
       'documentos inacess\u00edveis. A M1TR4M n\u00e3o tenta contornar isso: '
       '\u00e9 uma ferramenta de estudo para usar fora dos testes.'))


def help_():
    sel = 0
    while True:
        r = U.menu('Ajuda', [a[0] for a in AJ], sel)
        if r < 0:
            return
        sel = r
        U.text(AJ[r][0], AJ[r][1])


def about():
    U.text('Sobre a M1TR4M',
           '# M1TR4M ' + A.APPV + ' \u00b7 by M1TR4M\n'
           'F\u00edsica e Qu\u00edmica A e Matem\u00e1tica A, 10.\u00ba ano.\n'
           'Build: ' + A.K.BUILD + '\n\n'
           '# Fontes\n'
           '- Aprendizagens Essenciais (DGE): FQ A, FQ 7.\u00ba-9.\u00ba, Mat A\n'
           '- Programa de F\u00edsica e Qu\u00edmica A (DGE)\n'
           '- Tabelas de constantes e formul\u00e1rio do exame de FQ A (IAVE)\n'
           '- Dados da tabela peri\u00f3dica: ver a ficha de cada elemento\n\n'
           '# Limita\u00e7\u00f5es conhecidas\n' + A.K.LIMITES)

# ------------------------------------------------------------ diagnostico


def diag():
    while True:
        A.S['where'] = 'diagn\u00f3stico'
        r = U.menu('Diagn\u00f3stico', ['Resumo do aparelho', 'Teste de teclas',
                                       'Teste de grava\u00e7\u00e3o',
                                       'R\u00e9gua de calibra\u00e7\u00e3o'])
        if r < 0:
            return
        if r == 0:
            summary()
        elif r == 1:
            keytest()
        elif r == 2:
            savetest()
        else:
            calib()


def summary():
    f = P.free()
    d = P.today()
    m = C.SL['p'][0]
    o = ['Vers\u00e3o: ' + A.APPV + ' (build ' + A.K.BUILD + ')',
         'Plataforma: ' + P.platform(),
         'Ecr\u00e3: ' + str(P.E['W']) + ' x ' + str(P.E['H']) + ' px, ' +
         str(P.E['cols']) + ' colunas, ' + str(P.E['rows']) + ' linhas',
         'Mem\u00f3ria livre: arranque ' + str(A.S['f0']) + ', agora ' + str(f),
         'Importa\u00e7\u00e3o: ' + A.S['imp'] + (' (' + P.mod_file(P) + ')'
                                        if P.mod_file(P) else ''),
         'sys.modules: ' + ('sim' if P.has_mods() else
                            'n\u00e3o (m\u00e1x. 2 pacotes)'),
         'Grava\u00e7\u00e3o: ' + ('funciona' if A.S['gv'] else 'falhou'),
         'Data: ' + (str(d[2]) + '/' + str(d[1]) + '/' + str(d[0]) if d
                     else 'sem data (o progresso funciona sem datas)'),
         'S\u00edmbolos: ' + ('completos', 'Latin-1', 'letras simples')[
             2 - P.E['sym']] + ' \u00b7 teste: \u221a \u0394 \u03c0 \u2248 \u2192 \u2208 \u2264 \u00b2 \u00b3']
    for w in P.E['log'] + C.WARN:
        o.append('! ' + w)
    U.text('Diagn\u00f3stico', '\n'.join(o))


def keytest():
    ks = []
    while True:
        P.begin()
        U.title('Teste de teclas')
        P.put(0, 1, 'Carrega em teclas; esc duas vezes: sair.', 7)
        for i in range(len(ks)):
            P.put(0, 2 + i, str(i + 1) + ': [' + ks[i] + '] \u2192 ' +
                  P.norm(ks[i]), 0)
        U.foot('esc esc: sair')
        P.show()
        k = P.raw_key()
        ks.append(str(k))
        ks = ks[-8:]
        if len(ks) >= 2 and P.norm(ks[-1]) == 'esc' and \
                P.norm(ks[-2]) == 'esc':
            return


def savetest():
    ok = P.save('m1t', [1, 2.5, 3])
    v = P.load('m1t')
    good = ok and v is not None and len(v) == 3 and abs(v[1] - 2.5) < 1e-9
    A.S['gv'] = good
    U.msg('Teste de grava\u00e7\u00e3o', ('+ ' + U.OKS + 'store_list e recall_list '
                                  'funcionam.') if good else
          ('! ' + U.ERS + 'A grava\u00e7\u00e3o falhou: a app funciona, mas sem '
           'guardar o progresso.'))
