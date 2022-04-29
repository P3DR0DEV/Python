resposta = 'sS'
cont = soma = 0
lista = []
while resposta in 'sS':
    num = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ')).strip() [0]
    cont += 1
    soma += num
    lista += [num]
print('''O programa mostrou {} valores. A soma dos valores equivale à {} e a média entre eles equivale à {}. 
O maior número digitado foi {} e o menor {}. ''' .format(cont , soma, soma/cont , max(lista) , min(lista)))

