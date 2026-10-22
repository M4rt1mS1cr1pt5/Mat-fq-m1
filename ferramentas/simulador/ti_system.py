# ti_system falso para o simulador. As teclas vem de uma sequencia
# (ficheiro em ferramentas/teclas). get_key() sem espera devolve '' (nenhuma
# tecla premida); get_key(1) devolve a proxima tecla da sequencia. Quando
# a sequencia acaba, levanta KeyboardInterrupt e marca 'esgotou'.

ST = {'keys': [], 'pos': 0, 't': 1000, 'esgotou': 0, 'store': {},
      'vals': {}, 'plat': 'sim'}


def get_key(wait=0):
    if not wait:
        return ''
    if ST['pos'] >= len(ST['keys']):
        ST['esgotou'] = 1
        raise KeyboardInterrupt
    k = ST['keys'][ST['pos']]
    ST['pos'] += 1
    ST['t'] += 250
    return k


def get_time_ms():
    ST['t'] += 37
    return ST['t']


def store_list(n, lst):
    ST['store'][n] = [float(v) for v in lst]


def recall_list(n):
    if n not in ST['store']:
        raise NameError('sem a lista ' + n)
    return ST['store'][n][:]


def store_value(n, v):
    ST['vals'][n] = v


def recall_value(n):
    return ST['vals'][n]


def get_platform():
    return ST['plat']


def get_mouse():
    return (-1, -1)


def clear_history():
    pass
