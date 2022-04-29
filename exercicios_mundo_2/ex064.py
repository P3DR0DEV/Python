opção = soma = cont = 0
opção = int(input('Digite um valor [999 para parar]: '))

while opção != 999:
    opção = int(input('Digite um valor [999 para parar]: '))
    cont += 1
    soma += opção
print('O programa foi executado {} vezes. A soma de todos os valores digitados equivale à {}.' .format(cont , soma))

