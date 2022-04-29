salario = float(input('Insira a seguir o seu salário: R$ '))
if salario <= 1250:
    print('Com o reajuste salarial, o seu salário passará de R$ {:.2f} para R$ {:.2f}!' .format(salario , salario + (salario * 15/100)))
else:
    print('Com o reajuste salarial, o seu salário passará de R$ {:.2f} para R$ {:.2f}!' .format(salario , salario + (salario * 10/100)))
print('Agora vose será menos pobre que antes!!!!')

