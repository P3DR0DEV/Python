def fatorial(n):
    """
    -> Calcula o fatorial de um número
    :param n: Número a ser calculado
    :return: retorna O valor
    """
    f =1
    for c in range(1 , n+1):
        f *=c
    return f

def dobro(n):
    """
    -> Calcula o dobro de um número
    :param n: Número a ser calculado
    :return: retorna O valor
    """
    f = n * 2
    return f