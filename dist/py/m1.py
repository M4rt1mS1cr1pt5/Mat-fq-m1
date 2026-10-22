# m1.py - M1TR4M: arranque. Mede a memoria, importa o nucleo, mostra o
# ecra inicial e apanha qualquer erro fatal com uma mensagem clara.
# Fisica e Quimica A e Matematica A, 10.o ano. by M1TR4M

MODO = 'documento'


def _nome(e):
    # Nome do modulo numa mensagem "no module named 'x'".
    s = str(e)
    i = s.find("'")
    j = s.find("'", i + 1)
    if 0 <= i < j:
        return s[i + 1:j]
    return s


def main():
    f0 = -1
    try:
        import gc
        gc.collect()
        f0 = gc.mem_free()
    except Exception:
        pass
    try:
        import m1_app
    except MemoryError:
        print('M1TR4M: mem\u00f3ria insuficiente para arrancar.')
        print('Fecha outros documentos e tenta de novo.')
        return
    except ImportError as e:
        n = _nome(e)
        print('M1TR4M: falta o m\u00f3dulo ' + n + ' (instala ' + n + '.tns).')
        return
    try:
        m1_app.S['imp'] = MODO
        m1_app.run(f0)
    except KeyboardInterrupt:
        pass
    except MemoryError:
        print('M1TR4M: mem\u00f3ria insuficiente. Volta a abrir a app.')
    except Exception as e:
        print('M1TR4M: erro fatal ' + type(e).__name__ + ': ' + str(e))


main()
