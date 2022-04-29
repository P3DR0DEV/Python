from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno:'))
lista = [a1, a2 ,a3] 
a = shuffle(lista)
print('A ordem de apresentação será ')
print (lista)
