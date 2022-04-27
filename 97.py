from time import sleep
def lin(msg):
    print('=-'*20)
    print(f'{msg:^40}')
    print('=-'*20)
def contador(i, f, p):
    print(f'Contador de {i} até {f} de {p} em {p}')
    c = i
    if i < f:
        while c <= f:
            print(f'{c}', end=' ', flush=True)
            c += p 
            sleep(0.5)
        print('Fim!')
    else:
        while c>= f:
            print(f'{c}',end=' ', flush=True)
            c -= p
            sleep(0.5)
        print('Fim!')


lin('Exemplo de contadores: ')
contador(1, 10, 1)
contador(10, 0, 2)
lin('Faça o seu contador')
contador(i = int(input('Inicio:')), f = int(input('Fim: ')), p = int(input('Passo: ')))
        # commit
