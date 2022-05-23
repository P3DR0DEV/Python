def menu(*lista):
    print('--'*20)
    print('Esquilo\'s RPG'.center(40))
    print('--'*20)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('--'*20)
    opc = inteiro('Sua Opção: ')
    return opc


def inteiro(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError,TypeError):
            print('Digite um Número inteiro Válido')
            continue
        else:
            return num
