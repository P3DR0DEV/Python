from def_exercicios import moeda


num = int(input('Digite um número para os calculos: '))

dobro = moeda.dobro(num)
metade = moeda.metade(num)
num2 = int(input('Quer adicionar quantos % nesse numero? '))
aumentar = moeda.aumentar(num ,num2)
num3 = int(input('Quer diminuir quantos % desse numero? '))
diminui = moeda.diminuir(num, num3)

print(f'O número {num} foi analizado')
print(f'{num} * 2 = {dobro}')
print(f'{num} / 2 = {metade}')
print(f'{num} + {num2}% = {aumentar}')
print(f'{num} - {num3}% = {diminui}')
