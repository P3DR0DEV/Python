from time import sleep
num = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))
cont = 1
termo = num 
total = 0
mais = 10

while mais != 0:
    total += mais 

    while cont <= total:
        print('{} -> ' .format(termo), end='')
        termo += razão 
        cont += 1
    print('Pausa')
    mais = int(input('Você deseja ver mais quantos números? '))
    sleep(1)
print('Progressão finalizada com {} termos.' .format(total))

