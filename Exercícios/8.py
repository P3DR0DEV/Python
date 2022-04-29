from time import sleep
print('-' * 25)
print('         Boletim         ')
print('-' * 25)
lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], média])
    cont = str(input('Quer continuar? [S/N] '))[0]
    if cont in 'Nn':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    resp = int(input('Digite o número do aluno para informações mais detalhadas [999 Para sair]: '))
    if resp == 999:
        print('Finalizando programa.')
        sleep(1)
        break
    elif resp == i:
        print(f'As notas de {lista[resp][0]} foram: {lista[resp][1]}.')
print('Programa finalizado.')

