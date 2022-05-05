def moeda(preço=0, moeda = 'R$ '):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def dobro(n, formato = False):
    num = n *2
    if formato:
        return moeda(num)
    else:
        return num


def metade(n, formato = False):
    num = n / 2
    if formato:
        return moeda(num)
    else:
        return num


def aumentar(n, s= 10, formato = False):
    num = n + (n * s/100)
    if formato:
        return moeda(num)
    else:
        return num

def diminuir(n, s= 10, formato = False):
    num = n - (n * s/100)
    if formato:
        return moeda(num) 
    else:
        return num