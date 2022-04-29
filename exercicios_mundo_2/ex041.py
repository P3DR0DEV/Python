from datetime import date 
anoAtual = date.today().year
nasci = int(input('Digite o ano de nascimento do participante: '))
idade = anoAtual - nasci

if idade <= 9:
    print('Competidor MIRIN.')
elif idade <= 14:
    print('Competidor INFANTIL.')
elif idade <= 19:
    print('Competidor JUNIOR.')
elif idade <= 25:
    print('Competidor SÊNIOR.')
else:
    print('Competidor MASTER.')


