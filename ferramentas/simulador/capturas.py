#!/usr/bin/env python3
"""Desenha em PNG os ecras registados pelo simulador (so CPython + Pillow).

Uso: python3 capturas.py FRAMES.txt PASTA [n1 n2 ...]  (sem numeros: todos)
     python3 capturas.py FRAMES.txt PASTA --ultimos  (ecra antes de cada tecla)
Cada caracter e desenhado numa grelha de 7 px (as metricas assumidas pela
app), com a linha de base no y que a app passou ao draw_text.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H, CW = 318, 212, 7
FONTES = ['/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
          '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf']


def fonte(tam=11):
    for f in FONTES:
        if os.path.exists(f):
            return ImageFont.truetype(f, tam)
    return ImageFont.load_default()


def ler(fn):
    frames = {}
    cur = None
    with open(fn, encoding='utf-8') as f:
        for ln in f:
            ln = ln.rstrip('\n')
            if ln.startswith('F\t'):
                cur = int(ln.split('\t')[1])
                frames[cur] = []
            elif cur is not None and ln:
                frames[cur].append(ln.split('\t'))
    return frames


def cor(s):
    return tuple(int(v) for v in s.split(','))


def desenhar(ops, escala=2):
    im = Image.new('RGB', (W, H), (255, 255, 255))
    d = ImageDraw.Draw(im)
    ft = fonte()
    for o in ops:
        t = o[0]
        if t == 'R':
            x, y, w, h = map(int, o[1:5])
            if w > 0 and h > 0:
                d.rectangle([x, y, x + w - 1, y + h - 1], fill=cor(o[5]))
        elif t == 'r':
            x, y, w, h = map(int, o[1:5])
            d.rectangle([x, y, x + w, y + h], outline=cor(o[5]))
        elif t == 'L':
            x1, y1, x2, y2 = map(int, o[1:5])
            d.line([x1, y1, x2, y2], fill=cor(o[5]))
        elif t in 'Cc':
            x, y, r = map(int, o[1:4])
            box = [x - r, y - r, x + r, y + r]
            if t == 'C':
                d.ellipse(box, fill=cor(o[4]))
            else:
                d.ellipse(box, outline=cor(o[4]))
        elif t in 'Pp':
            pts = [tuple(map(int, p.split(','))) for p in o[1].split(' ')]
            if t == 'P':
                d.polygon(pts, fill=cor(o[2]))
            else:
                d.polygon(pts, outline=cor(o[2]))
        elif t == 'T':
            x, y = int(o[1]), int(o[2])
            c = cor(o[3])
            s = '\t'.join(o[4:])
            for i, ch in enumerate(s):
                d.text((x + i * CW, y), ch, font=ft, fill=c, anchor='ls')
    if escala != 1:
        im = im.resize((W * escala, H * escala), Image.NEAREST)
    return im


def main(a):
    frames = ler(a[0])
    os.makedirs(a[1], exist_ok=True)
    nums = [int(x) for x in a[2:] if x.isdigit()]
    if not nums:
        nums = sorted(frames)
    for n in nums:
        if n in frames:
            desenhar(frames[n]).save(os.path.join(a[1], 'ecra_%03d.png' % n))
    print(len(nums), 'capturas em', a[1])


if __name__ == '__main__':
    main(sys.argv[1:])
