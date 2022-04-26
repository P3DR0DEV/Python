from time import sleep
def contador(i, f, p):
    print(f'Contador de {i} até {f} de {p} em {p}')
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p 
    print('Fim!')

contador(1, 10, 1)
