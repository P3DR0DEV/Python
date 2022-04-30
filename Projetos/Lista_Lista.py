'''dados = list() #variavel criando uma lista
dados.append('Pedro') #adicionar elemento
dados.append(25)
pessoas = list()
pessoas.append(dados[:]) #copiando a lista "dados" para a lista pessoas 
pessoas = [['Pedro', 25], ['Maria', 19], ['João',32]] #lista composta
print(pessoas[0][0]) #print o item 0 da primeira lista'''

galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    print('=-'*5)
maior = menor = 0
for p in galera:
    if p[1] >=18:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1 
print(f'Neste grupo de amigos {maior} pessoas são maiores de idade, e {menor} são menores de idade.')
