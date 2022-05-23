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
    print('--'*20)
    return opc


def inteiro(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError,TypeError):
            print('Digite um Número inteiro Válido')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu sair.\033[m')
            return None
        else:
            return num
