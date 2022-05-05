def dobro(n):
    f = n *2
    return f


def metade(n):
    f = n / 2
    return f


def aumentar(n, s= 10):
    f =n + (n *s/100)
    return f

def diminuir(n, s= 10):
    f = n - (n * s/100)
    return f

def moeda(preço=0, moeda = 'R$'):
    return f'{moeda:.2f}{preço:.2f}' .replace('.', ',')