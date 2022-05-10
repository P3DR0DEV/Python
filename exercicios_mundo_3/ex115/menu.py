def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro Válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar um número.\033[m')
            return None
        else:
            return n



def titulo(*lista):
    print('--'*20)
    print('MENU PRINCIPAL'.center(40))
    print('--'*20)
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print('--'*20)
    opc = leiaint('\033[34mSua Opção: \033[m')
    return opc
    

 

