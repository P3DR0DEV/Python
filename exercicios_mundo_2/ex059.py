from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    print( '''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair''')
    opção = int(input('Qual a sua opção? '))    

    if opção == 1:
        print('A soma entre os 2 números equivale à : ' ,n1 + n2)

    elif opção == 2:
        print('A Multiplicação entre os 2 números equivale à:' , n1 * n2)

    elif opção == 3:
        if n1 > n2:
            print('O primeiro número {} é maior que o segundo {}.' . format(n1, n2))
        elif n1 < n2:
            print('O segundo número \'{}\' é maior que o primeiro \'{}\'.' .format(n2, n1))
        else:
            print('Os números tem o mesmo valor.')

    elif opção == 4:
        n1 = int(input('Digite o novo valor: '))
        n2 = int(input('Digite o novo valor: '))
    sleep(1)
print('Fim do programa. Volte sempre!')

