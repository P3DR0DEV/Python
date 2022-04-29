print('Analisando Triângulos!')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and b + c > a:
    print('Com esses segmentos podemos formar um triângulo.')
    if a == c and c == b:
        print('O triângulo será Equilátero. ')
    elif a == c or a == b and c != a:
        print('O triângulo será Isósceles.')
    else:
        print('O triângulo será Escaleno.')

else:
    print('Esses segmentos não podem formar um triângulo.')
    

