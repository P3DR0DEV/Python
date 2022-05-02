def fatorial(n, show= False):
    """
    -> Calcula o Fatorial de um número.
    :param n: Numero para calcular o fatorial.
    :param show: (Opcional) mostra ou não a conta.
    :return: Retorna o valor do fatorial.
    """
    f = 1
    for c in range(n , 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ' ,end ='')
        f *= c
    return(f)


print(fatorial(10, True))