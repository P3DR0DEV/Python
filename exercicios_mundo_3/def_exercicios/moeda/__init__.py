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

def diminuir(n, sub= 10, formato = False):
    num = n - (n * sub/100)
    if formato:
        return moeda(num) 
    else:
        return num


def resumo(n, s, sub):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço Analizado:{moeda(n):>13}')
    print(f'Dobro do Preço:{dobro(n , True):>14}')
    print(f'Metade do Preço:{metade(n , True):>13}')
    print(f'Aumentando {s}%:{aumentar(n , s , True):>14}')
    print(f'Diminuindo {sub}%:{diminuir(n, sub, True):>14}')
    print('-'*30)

