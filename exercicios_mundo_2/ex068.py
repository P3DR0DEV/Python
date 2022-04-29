from random import randint
cont = 0
print('=-' * 20)
print('Vamos jogar PAR ou ÍMPAR')
print('=-' * 20)
while True:
    n = int(input('Digite um valor: '))
    r = randint(0, 10)
    escolha = ' '
    while escolha not in 'pPiI':
        escolha = str(input('Par ou Ímpar? (P/I) ')).upper().strip()[0]
    print('-' * 20)
    soma = (n + r)
    if soma % 2 == 0 and escolha in 'Pp':
       print(f' A soma dos 2 valores vale: {soma} então PAR ganhou') 
    elif soma % 2 != 0 and escolha in 'Ii':
        print(f'A soma dos 2 valores vale: {soma} então Ímpar ganhou')
    else:
        print(f'A soma dos 2 valores vale: {soma} então você Perdeu')
        break
    cont += 1
print(f'Você ganhou {cont} vezes antes.')

