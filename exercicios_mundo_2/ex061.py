print('Analise de P.A')
print('-='*7)

num = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))
cont = 1
termo = num 
while cont <= 10:
    print('{}' .format(termo) ,end='')
    print(' -> ' if cont < 10 else ' ' ,end='')
    cont += 1
    termo += razão 
print('FIM.')

