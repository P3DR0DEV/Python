from datetime import date
from datetime import date 
atual = date.today().year
sexo = int(input('Para sexo MASCULINO digite \'1\', e FEMININO digite \'2\': '))
#para o sexo masculino
if sexo == 1:    
    ano  = int(input('Ano de nascimento: '))
    idade = atual - ano

    if  idade < 18:
        marcação = 18 - idade
        print('Ainda não é o seu ano de alistamento, o seu será em {} anos.' .format(marcação))
    elif  idade == 18:
        print('Você deverá comparecer para o alistamento ao exercito este ano')
    elif  idade > 18:
        atraso = idade - 18
        print('Caso não tenha se alistado ate o momento, o senhor deveria ter se alistado {} anos atrás.' .format(atraso))
#para o feminino 
elif sexo == 2: 
    print('No Brasil, mulheres não são obrigadas a se alistarem no exercito.')

