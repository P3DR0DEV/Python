peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (M) '))
imc = peso / (altura ** 2)
print('O imc equivale à: {:.1f}' .format(imc))
if imc < 18.5: 
    print('MAGREZA.')
elif imc < 24.9:
    print('NORMAL.')
elif imc < 30:
    print ('SOBREPESO.')
elif imc < 40:
    print('OBESIDADE.')
else:
    print('OBESIDADE MÓRBIDA. ')

