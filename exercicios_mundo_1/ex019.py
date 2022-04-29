from random import choice 
a = str(input('Digite um nome: '))
b = str(input('Digite outro nome: '))
c = str(input('Digite outro nome: '))
d = str(input('Digite outro nome: '))
e = str(input('Digite o ultimo nome: '))
lista = [a, b, c, d, e]
sorteado = choice (lista)
print('O aluno sorteado foi {} ' .format(sorteado))
