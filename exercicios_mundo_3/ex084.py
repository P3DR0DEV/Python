maior = menor = 0
temp = []
lista = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temp [1]
    else:
        if temp [1] > maior:
            maior =temp[1]
        if temp[1] < menor:
            menor = temp[1]

    lista.append(temp[:])
    temp.clear()
    conti = ' '

    while conti not in 'NS':
        conti = str(input('Deseja continuar? ')).upper()[0]

    if conti in 'N':
        break

print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.2f} Kg de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' e ')
    if p[1] == menor:
        print(f'{p[0]}', end=', ')
print(f'com {menor:.2f} Kg foi o menor.')

