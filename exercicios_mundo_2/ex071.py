print('=' * 30)
print('{:^30}'.format('Banco'))
print('=' * 30)

valor = int(input('Valor de Saque: R$ '))
total = valor 
céd = 50
cont = 0
while True:
    if total >= céd:
        total -= céd
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédulas de R$ {céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        cont = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre.')
