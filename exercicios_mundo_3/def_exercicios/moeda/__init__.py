def converter(preço=0, moeda = 'R$'):
    return f'{moeda:.2f}{preço:.2f}'.replace(',', '.')


def dobro(n):
    f = n *2
    converter(f)



def metade(n):
    f = n / 2
    converter(f)



def aumentar(n, s= 10):
    f =n + (n *s/100)
    converter(f)

def diminuir(n, s= 10):
    f = n - (n * s/100)
    converter(f) 
