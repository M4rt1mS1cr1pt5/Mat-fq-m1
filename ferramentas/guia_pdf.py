#!/usr/bin/env python3
"""Guia de instalacao em PDF (docs/INSTALAR_NA_CALCULADORA.pdf).

Uso: python3 ferramentas/guia_pdf.py
Precisa do reportlab e do Pillow, e das capturas do build (dist/capturas):
os ecras do guia sao os do simulador.
"""
import os
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.fonts import addMapping
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Image, KeepTogether, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
sys.path.insert(0, os.path.join(RAIZ, 'ferramentas', 'simulador'))
import capturas as C  # noqa: E402
import previa as PV  # noqa: E402

SAIDA = os.path.join(RAIZ, 'docs', 'INSTALAR_NA_CALCULADORA.pdf')
FONTES = '/usr/share/fonts/truetype/dejavu/'
AZUL = colors.HexColor('#003399')
CINZA = colors.HexColor('#f0f0f0')

pdfmetrics.registerFont(TTFont('DV', FONTES + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', FONTES + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVM', FONTES + 'DejaVuSansMono.ttf'))
# <b> nos paragrafos usa a versao negrito da DejaVu.
addMapping('DV', 0, 0, 'DV')
addMapping('DV', 1, 0, 'DVB')
addMapping('DV', 0, 1, 'DV')
addMapping('DV', 1, 1, 'DVB')

S = {
    'tit': ParagraphStyle('tit', fontName='DVB', fontSize=20, leading=25,
                          textColor=AZUL),
    'sub': ParagraphStyle('sub', fontName='DV', fontSize=11, leading=15,
                          textColor=colors.HexColor('#444444')),
    'h': ParagraphStyle('h', fontName='DVB', fontSize=13, leading=17,
                        textColor=AZUL, spaceBefore=10, spaceAfter=4),
    'p': ParagraphStyle('p', fontName='DV', fontSize=10, leading=14,
                        spaceAfter=4),
    'n': ParagraphStyle('n', fontName='DV', fontSize=10, leading=14,
                        leftIndent=16, firstLineIndent=-12, spaceAfter=3),
    'aviso': ParagraphStyle('aviso', fontName='DV', fontSize=9.5,
                            leading=13, backColor=colors.HexColor('#fff4d6'),
                            borderPadding=6, borderColor=colors.HexColor(
                                '#e0b040'), borderWidth=0.6, spaceBefore=6,
                            spaceAfter=10),
    'leg': ParagraphStyle('leg', fontName='DV', fontSize=8.5, leading=11,
                          alignment=TA_CENTER,
                          textColor=colors.HexColor('#555555')),
    'cel': ParagraphStyle('cel', fontName='DV', fontSize=9, leading=12),
}


def k(t):
    # Tecla ou nome de ficheiro em letra de maquina.
    return '<font name="DVM">%s</font>' % t


def passos(lista):
    return [Paragraph('%d.&nbsp;&nbsp;%s' % (i + 1, t), S['n'])
            for i, t in enumerate(lista)]


def ecra(perc, titulo, oc, legenda, largura=80 * mm):
    fr = C.ler(os.path.join(RAIZ, 'dist', 'capturas', perc + '.frames'))
    ns = [n for n in sorted(fr) if PV.titulo(fr[n]) == titulo]
    if not ns:
        raise RuntimeError('guia: falta o ecra "%s" em %s' % (titulo, perc))
    p = os.path.join(RAIZ, 'dist', 'capturas', '_guia_%s_%d.png' % (
        perc, ns[oc]))
    C.desenhar(fr[ns[oc]], 2).save(p)
    img = Image(p, width=largura, height=largura * C.H / C.W)
    return p, [img, Spacer(1, 2), Paragraph(legenda, S['leg'])]


def tabela(linhas, larguras):
    t = Table([[Paragraph(c, S['cel']) for c in ln] for ln in linhas],
              colWidths=larguras)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), AZUL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, CINZA]),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#bbbbbb')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    return t


def cabecalho(t):
    return '<font color="white">%s</font>' % t


def rodape(cv, doc):
    cv.saveState()
    cv.setFont('DV', 8)
    cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(18 * mm, 10 * mm, 'M1TR4M · guia de instalação')
    cv.drawRightString(A4[0] - 18 * mm, 10 * mm, 'página %d' % doc.page)
    cv.restoreState()


def main():
    temp = []
    st = []
    st += [Paragraph('M1TR4M — instalar na calculadora', S['tit']),
           Paragraph('TI-Nspire CX II-T · Física e Química A (10.º ano) e '
                     'Matemática (7.º ao 10.º ano)', S['sub']),
           Paragraph('<b>Atenção:</b> a app foi toda testada no computador '
                     '(simulador e MicroPython), mas ainda não numa '
                     'calculadora. Por isso o primeiro passo é a sonda: ela '
                     'mostra o que a tua calculadora aguenta. Se algo falhar, '
                     'fotografa o ecrã e envia.', S['aviso'])]

    st.append(Paragraph('O que precisas', S['h']))
    st += [Paragraph('• Calculadora TI-Nspire CX II-T com o sistema operativo '
                     '<b>5.2 ou mais recente</b> (é o que traz o Python). '
                     'Vês a versão em Início ▸ Definições ▸ Estado.', S['n']),
           Paragraph('• Cabo USB e um computador com o <b>TI-Nspire CX II '
                     'Connect</b> (grátis, no site da Texas Instruments; '
                     'funciona no Chrome ou no Edge). Também serve o '
                     'TI-Nspire Computer Link ou o software do aluno.',
                     S['n']),
           Paragraph('• Os ficheiros da app (ver a seguir).', S['n'])]

    st.append(Paragraph('Onde estão os ficheiros', S['h']))
    st.append(Paragraph(
        'No GitHub, repositório ' + k('M4rt1mS1cr1pt5/Mat-fq-m1') +
        ', ramo ' + k('claude/new-session-8ceduw') + ', pasta ' +
        k('dist/tns') + '. Para os descarregar: escolhe esse ramo, carrega '
        'em <b>Code ▸ Download ZIP</b> e descompacta. Também podes usar o '
        'zip ' + k('M1TR4M_calculadora.zip') + ', que tem os mesmos '
        'ficheiros.', S['p']))
    st.append(tabela([
        [cabecalho('Ficheiro'), cabecalho('Para quê')],
        [k('M1TR4M_sonda.tns'), 'Sonda: corre-a primeiro.'],
        [k('M1TR4M.tns'), 'A app inteira num só documento (forma '
         'preferida).'],
        [k('PyLib/') + ' (113 ficheiros)', 'Um ficheiro por módulo, para a '
         'pasta PyLib (se a forma anterior falhar).'],
        [k('M1TR4M_arranque.tns'), 'Documento pequeno que arranca a app '
         'instalada na PyLib.'],
        [k('M1TR4M_FQ.tns') + '<br/>' + k('M1TR4M_Mat.tns'),
         'Edições de reserva, cada uma num só programa: FQ do 10.º ano, ou '
         'Matemática do 7.º ao 9.º ano.'],
    ], [62 * mm, 112 * mm]))

    st.append(Paragraph('Passo 1 — Ligar a calculadora ao computador', S['h']))
    st += passos([
        'Abre o TI-Nspire CX II Connect.',
        'Liga a calculadora com o cabo USB e liga-a. Ela aparece no '
        'programa.',
        'Para enviar um ficheiro, arrasta-o para a calculadora (ou usa a '
        'opção de enviar ficheiros do programa). Os ficheiros ficam em '
        '<b>Os meus documentos</b>.'])

    st.append(Paragraph('Passo 2 — Correr a sonda', S['h']))
    st += passos([
        'Envia ' + k('M1TR4M_sonda.tns') + '.',
        'Na calculadora: Início ▸ <b>Os meus documentos</b> ▸ abre '
        + k('M1TR4M_sonda') + '.',
        'Vai à página do ' + k('m1sonda.py') + ' (ctrl + ◂ ▸ mudam de '
        'página) e carrega em <b>ctrl + R</b> para correr.',
        '<b>Fotografa o ecrã</b>: tamanho do ecrã, memória livre e se a '
        'linha "import" diz "funciona".',
        'Carrega numa tecla: entra o teste de teclas. Para sair, carrega em '
        '<b>esc duas vezes</b>.'])

    st.append(Paragraph('Passo 3 — Instalar a app (forma preferida)', S['h']))
    st += passos([
        'Envia ' + k('M1TR4M.tns') + '.',
        'Abre-o, vai à página do ' + k('m1.py') + ' e carrega em '
        '<b>ctrl + R</b>.',
        'Aparece uma animação curta (qualquer tecla salta) e depois o menu '
        'principal com 13 opções.'])
    p, menu = ecra('p01_fq_licao', 'M1TR4M · FQ 10.º · Mat 7.º-10.º', 0,
                   'Menu principal (ecrã do simulador)')
    temp.append(p)
    st.append(KeepTogether(menu))

    st.append(Paragraph('Passo 4 — Se aparecer "falta o módulo…" (forma '
                        'PyLib)', S['h']))
    st += passos([
        'Em <b>Os meus documentos</b> tem de existir a pasta <b>PyLib</b>. '
        'Se não existir, cria-a com esse nome exato.',
        'Envia os <b>113 ficheiros</b> da pasta ' + k('PyLib') + ' '
        'diretamente para essa pasta (sem subpastas).',
        'Envia ' + k('M1TR4M_arranque.tns') + ' para outra pasta '
        'qualquer, abre-o e corre o ' + k('m1.py') + ' com ctrl + R.'])

    st.append(Paragraph('Passo 5 — Se aparecer "memória insuficiente" '
                        '(edições de reserva)', S['h']))
    st.append(Paragraph(
        'Envia ' + k('M1TR4M_FQ.tns') + ' ou ' + k('M1TR4M_Mat.tns') +
        ', abre e corre como no passo 3. Cada uma é um só programa e não '
        'precisa de mais nada, mas tem menos conteúdo e não tem pesquisa. '
        'No computador precisaram de cerca de 0,9 MB (FQ) e 1,2 MB (Mat) de '
        'memória livre.', S['p']))

    st.append(Paragraph('Confirmar que está tudo bem', S['h']))
    st.append(Paragraph(
        'Menu principal ▸ ' + k('1') + ' ' + k('2') + ' (Definições, ajuda e '
        'Diagnóstico) ▸ ' + k('4') + ' (Diagnóstico) ▸ ' + k('1') +
        ' (Resumo do aparelho). A linha <b>Importação</b> diz qual forma '
        'está a funcionar ("documento" ou "PyLib") e a linha <b>Memória '
        'livre</b> mostra a memória da calculadora. Fotografa este ecrã.',
        S['p']))
    p, diag = ecra('p06_definicoes', 'Diagnóstico', 1,
                   'Resumo do aparelho (ecrã do simulador; na calculadora '
                   'aparecem os valores reais)')
    temp.append(p)
    st.append(KeepTogether(diag))

    st.append(Paragraph('No dia a dia', S['h']))
    st.append(tabela([
        [cabecalho('Tecla'), cabecalho('O que faz')],
        ['número', 'Escolhe a opção. Com 10 ou mais opções, "1" fica à espera '
         'do 2.º algarismo: "1" e enter escolhe a 1, "1" e "2" a 12.'],
        ['▴ ▾', 'Mudam a opção ou deslizam o texto.'],
        ['◂ ▸', 'Página anterior ou seguinte (numa lição).'],
        ['enter', 'Confirma; num texto longo, avança.'],
        ['esc ou 0', 'Volta ao ecrã anterior.'],
        ['del / clear', 'Apaga um carácter / limpa o campo.'],
        ['▾ num campo', 'Nas calculadoras, leva à unidade do campo; ◂ ▸ '
         'mudam-na.'],
    ], [30 * mm, 144 * mm]))
    st.append(Spacer(1, 6))
    st += [Paragraph('• <b>Gravar:</b> antes de fechar o documento, carrega '
                     'em <b>ctrl + S</b>. Sem isso, as definições e o '
                     'progresso perdem-se.', S['n']),
           Paragraph('• <b>Sair da app:</b> opção 13 do menu principal (ou '
                     'esc no menu principal) e confirmar.', S['n']),
           Paragraph('• <b>Modo de exame:</b> no Press-to-Test os documentos '
                     'ficam bloqueados; a app é para estudar fora dos '
                     'testes.', S['n'])]

    st.append(Paragraph('Problemas frequentes', S['h']))
    st.append(tabela([
        [cabecalho('O que aparece'), cabecalho('O que fazer')],
        ['"falta o módulo …"', 'Usa a forma PyLib (passo 4) e confirma que '
         'os 113 ficheiros estão dentro da pasta PyLib.'],
        ['"memória insuficiente"', 'Fecha outros documentos e tenta de '
         'novo; se continuar, usa uma edição de reserva (passo 5).'],
        ['Símbolos como ? ou caixas', 'Definições ▸ Acentos e símbolos ▸ '
         'letras simples.'],
        ['Texto cortado ou desalinhado', 'Definições ▸ Calibração do texto '
         'no ecrã.'],
        ['O progresso desapareceu', 'Grava o documento com ctrl + S antes '
         'de o fechar.'],
    ], [55 * mm, 119 * mm]))
    st.append(Spacer(1, 8))
    st.append(Paragraph(
        'A lista completa do que testar na calculadora, com os resultados '
        'esperados, está em ' + k('docs/TESTES_NO_APARELHO.md') + '.',
        S['p']))

    doc = SimpleDocTemplate(SAIDA, pagesize=A4, leftMargin=18 * mm,
                            rightMargin=18 * mm, topMargin=16 * mm,
                            bottomMargin=18 * mm,
                            title='M1TR4M — instalar na calculadora',
                            author='M1TR4M')
    doc.build(st, onFirstPage=rodape, onLaterPages=rodape)
    for p in temp:
        os.remove(p)
    print(SAIDA)


if __name__ == '__main__':
    main()
