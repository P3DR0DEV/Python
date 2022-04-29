from time import sleep 


def maior(* num):
    maior= cont= 0 
    print('\n Analizando Valores...')
    for valor in num:
        print(f'{valor}', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            valor = maior
        else:
            if valor > maior:
                valor = maior
    cont += 1
    print(f'Foram analizador {cont} valores. ')
    print(f'O maior calor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
