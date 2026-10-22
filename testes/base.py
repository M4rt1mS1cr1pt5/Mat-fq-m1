# Ajudas para os testes (funcionam em CPython e MicroPython).
import m1_nucleo as N


def calc(mod, fn, vals, units=None):
    # Preenche o formulario de uma calculadora e devolve o resultado
    # (texto, passos, valor, ...) ou levanta ValueError com a mensagem
    # do campo errado.
    sp = getattr(mod, fn)()
    t, fs, f = sp
    for i in range(len(vals)):
        if fs[i][4] == 'c':
            fs[i][3] = vals[i]
        else:
            fs[i][2] = vals[i]
    if units:
        for i in units:
            fs[i][3] = units[i]
    v = N.rdf(fs)
    if v is None:
        raise ValueError('campo: ' + '; '.join([x[5] for x in fs if x[5]]))
    return f(v)


def erro(fn, *a):
    # Devolve a mensagem do ValueError (falha se nao houver erro).
    try:
        fn(*a)
    except ValueError as e:
        return str(e)
    except ZeroDivisionError as e:
        return 'ZeroDivisionError ' + str(e)
    raise AssertionError('esperava um erro')


def tem(txt, *partes):
    for p in partes:
        if p not in txt:
            raise AssertionError('falta "' + p + '" em: ' + txt[:300])


def perto(a, b, tol=1e-9):
    if abs(a - b) > tol * max(1.0, abs(b)):
        raise AssertionError(str(a) + ' != ' + str(b))
