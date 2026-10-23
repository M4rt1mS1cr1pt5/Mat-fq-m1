#!/usr/bin/env python3
"""Previa (seccao 5, passo 10): uma imagem com os ecras principais,
tirados das capturas dos percursos de teclas (dist/capturas/*.frames).

Uso: python3 previa.py PASTA_DAS_CAPTURAS SAIDA.png
Precisa do Pillow (so no computador). Cada ecra escolhe-se pelo titulo
que mostra: se um percurso mudar e o ecra deixar de aparecer, a previa
falha com o nome do que falta, em vez de sair com um ecra errado.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, 'simulador'))

# (percurso, titulo do ecra, ocorrencia: 0 = primeira, -1 = ultima,
#  legenda)
ESCOLHA = (
    ('p01_fq_licao', 'M1TR4M · FQ 10.º · Mat 7.º-10.º', 0,
     'Menu principal'),
    ('p11_mat_anos', 'Matemática', 0, 'Matemática por anos'),
    ('p11_mat_anos', '7.º ano', 0, 'Temas do 7.º ano'),
    ('p01_fq_licao', 'Constituição do átomo e isótoposD 4/10', 0,
     'Lição de FQ (página D)'),
    ('p11_mat_anos', 'Ângulos e retas paralelasF 4/5', 0,
     'Ficha do 7.º ano (exemplo resolvido)'),
    ('p02_mat_calc', 'Equação do 2.º grau', 0,
     'Calculadora: resultado com passos'),
    ('p02_mat_calc', 'f(x) = 2x² - 3x + 1', 0, 'Gráfico'),
    ('p11_mat_anos', 'Paralelas cortadas por uma secante', -1,
     'Desenho: paralelas e secante'),
    ('p11_mat_anos', 'Tabela de dupla entrada: soma', -1,
     'Probabilidades: tabela de dupla entrada'),
    ('p10_mat_pontos', 'Triângulo [PQR] e pontos notáveis', 0,
     'Pontos notáveis do triângulo'),
    ('p05_tabela', 'Tabela periódica', 0, 'Tabela periódica'),
    ('p03_exercicios', 'Massa e tamanho dos átomos · 2/10', 0,
     'Exercício'),
)
COLS = 3
ESCALA = 2


def titulo(ops):
    # Texto desenhado na barra do titulo (y < 17), pela ordem.
    return ''.join('\t'.join(o[4:]) for o in ops
                   if o[0] == 'T' and int(o[2]) < 17)


def escolher(pasta, C):
    out = []
    faltam = []
    cache = {}
    for perc, tit, oc, leg in ESCOLHA:
        if perc not in cache:
            p = os.path.join(pasta, perc + '.frames')
            cache[perc] = C.ler(p) if os.path.exists(p) else {}
        fr = cache[perc]
        ns = [n for n in sorted(fr) if titulo(fr[n]) == tit]
        if not ns:
            faltam.append('%s: "%s"' % (perc, tit))
            continue
        out.append((fr[ns[oc]], leg))
    return out, faltam


def gerar(pasta, saida):
    """Escreve a previa e devolve o numero de ecras (ou levanta
    RuntimeError com os ecras que faltam)."""
    import capturas as C
    from PIL import Image, ImageDraw, ImageFont
    ecras, faltam = escolher(pasta, C)
    if faltam:
        raise RuntimeError('previa: faltam ecras: ' + '; '.join(faltam))
    w, h = C.W * ESCALA, C.H * ESCALA
    leg_h = 34
    marg = 12
    linhas = (len(ecras) + COLS - 1) // COLS
    W = COLS * (w + marg) + marg
    H = 70 + linhas * (h + leg_h + marg) + marg
    im = Image.new('RGB', (W, H), (245, 245, 245))
    d = ImageDraw.Draw(im)
    fonte = None
    for f in ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
              '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'):
        if os.path.exists(f):
            fonte = (ImageFont.truetype(f, 26), ImageFont.truetype(f, 20))
            break
    if fonte is None:
        fonte = (ImageFont.load_default(), ImageFont.load_default())
    d.text((marg, 18), 'M1TR4M · Física e Química A 10.º · '
           'Matemática 7.º-10.º — ecrãs principais (simulador, '
           '318 × 212 ampliado 2×)', fill=(0, 51, 153), font=fonte[0])
    for i, (ops, leg) in enumerate(ecras):
        x = marg + (i % COLS) * (w + marg)
        y = 70 + (i // COLS) * (h + leg_h + marg)
        im.paste(C.desenhar(ops, ESCALA), (x, y))
        d.rectangle([x - 1, y - 1, x + w, y + h], outline=(160, 160, 160))
        d.text((x + 4, y + h + 6), leg, fill=(0, 0, 0), font=fonte[1])
    im.save(saida)
    return len(ecras)


if __name__ == '__main__':
    print(gerar(sys.argv[1], sys.argv[2]), 'ecras em', sys.argv[2])
