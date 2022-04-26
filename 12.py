pessoa = {}
grupo = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Favor selecionar M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break 
    if resp in 'N':
        break
print('=-'*20)
print(f'Ao todo temos {len(grupo)} pessoas cadastradas.')
media = soma / len(grupo)
print(f'A média de idades é de {media:5.2f}.')
print(f'As mulheres cadastradas foram: ' ,end='')
for p in grupo:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print(f'Lista de pessoas que são mais velhas que a média do grupo: ' ,end='')
for p in grupo:
    if p['Idade'] > media:
        print(f'{p["Nome"]}', end=' ')
print()
print('=-'*20)