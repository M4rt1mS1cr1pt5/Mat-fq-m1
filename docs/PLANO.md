# M1TR4M — plano de trabalho e estado

Documento de trabalho (para retomar o desenvolvimento). O relatório final
fica em `RELATORIO.md`.

## Fases (secção 14 do prompt)

- Fase 0 — sonda da calculadora: `src/sonda/m1sonda.py` + `m1sonda2.py` (feito, 3,2 KB).
- Fase 1 — plataforma, núcleo, interface, simulador e testes (em curso).
- Fase 2 — pacotes piloto (FQ: Massa e tamanho dos átomos; Mat: Função
  quadrática), três calculadoras, medir e rever orçamentos.
- Fase 3 — restantes pacotes, calculadoras, exercícios e pesquisa.
- Fase 4 — acabamentos, prévia, relatório e lista de testes no aparelho.

## Módulos

| Módulo | Função | Carregado |
| --- | --- | --- |
| m1 | arranque e erros fatais | sempre |
| m1_plat | ecrã, teclas, tempo, memória, gravação | sempre |
| m1_nucleo | números, expressões, unidades, validação | sempre |
| m1_ui | componentes de ecrã | sempre |
| m1_app, m1_cont, m1_cat | navegação, leitor de pacotes, catálogo | sempre |
| m1_ex | treino, teste, revisão rápida, progresso | a pedido (ranhura f) |
| m1_cfg | definições, ajuda, diagnóstico | a pedido (ranhura f) |
| m1_pesq + m1_idx | pesquisa (código + índice) | a pedido (f + p) |
| m1_tp | tabela periódica (dados + ecrã) | a pedido (p) |
| p_* / x_* | lições / exercícios de um tema | a pedido (p) |
| c_* | calculadoras de um grupo | a pedido (c) |

## Ferramentas

- MicroPython 1.12, porta unix de 32 bits: compilar com
  `make -C ports/unix MICROPY_FORCE_32BIT=1 MICROPY_PY_FFI=0 MICROPY_PY_BTREE=0 MICROPY_PY_USSL=0 MICROPY_PY_AXTLS=0`
  (precisa de `gcc-multilib`).
- Luna 2.1 (github.com/ndless-nspire/Luna) para criar os `.tns`.
- `ferramentas/simulador/correr.py` corre a app com uma sequência de teclas
  (CPython ou MicroPython); `capturas.py` desenha os ecrãs em PNG.
