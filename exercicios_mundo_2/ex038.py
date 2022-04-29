print('Digite 2 números para serem comparados.')
numero = int(input('Primeiro número: '))
segNumero = int(input('Segundo número: '))

if numero > segNumero:
    print('O número {} é maior que {}. ' .format(numero ,segNumero))
elif numero < segNumero:
    print('O número {} é maior que {}. ' .format(segNumero , numero))
elif numero == segNumero:
    print('Os números digitados tem o mesmo valor. ')
    
    