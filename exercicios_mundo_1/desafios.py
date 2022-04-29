#Desafio 005
n = int(input('Digite um número:'))
print('O número {}, tem como seu antecessor {} e sucessor {}' .format(n ,n-1 , n+1))
#Desafio 006
n2 = int(input('Digite outro número:'))
print('O número {} multiplicado por 2, equivale a {}, por 3: {} e sua raiz: {:.2f}' .format(n2, n2*2 ,n2*3 , n2**(1/2)))
#Desafio 007
n3 = float(input('Nota da primeira prova:'))
n4 = float(input('Nota da segunda prova:'))
print('A média entre as duas notas equivale a {}' .format((n3 + n4) / 2))
#Desafio 008
m = float(input('Insira a medida em metros:'))
print('A medida equivale a {} metros, {} centimetros, e {} milimetros' .format(m , m*100 , m*1000))
#Desafio 009
i = int(input('Digite um número:'))
print('Tabuada do {} \n = x2 {} \n x3 = {} \n x4 = {} \n x5 = {} \n x6 = {} \n x7 = {} \n x8 = {} \n x9 = {}' .format(i ,i*2 ,i*3, i*4 ,i*5 ,i*6 ,i*7 ,i*8 ,i*9))
#Desafio 010
c = float(input('Quantos Reais você tem na sua carteira? R$ '))
print('Com seus {:.2f} reais, você consegue comprar {:.2f} dólares.' .format(c ,c/5.53))
#Desafio 011
h = float(input('Altura em metros da parede:'))
l = float(input('largura em metros da parede:'))
print('Sua área equivale à {} metros², e será necessário {} litros de tinta para pinta-la!' .format(h * l , (h * l) / 2))
#Desafio 012
p = float(input('Qual o preço do produto? R$ '))
print('O produto custará {}, com o desconto aplicado'. format(p - (p*5/100)))
#Desafio 013
s = int(input('Quanto você recebe? '))
print('Seu novo salário será de {} reais com o benefício aplicado' .format(s + (s*15/100)))

