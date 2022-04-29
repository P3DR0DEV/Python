'''tuplas
variaveis simples e compostas
TUPLAS SÃO IMUTÁVEIS'''

lanche = ('hambúrguer' , 'suco' , 'pizza' , 'pudim')
for cont in range(0, len(lanche)):
    print(lanche[cont])  

for comida in lanche:
    print(comida)

for pos, comida in enumerate(lanche):
    print(f'{pos} -> {comida}')

print(sorted(lanche))  # organização por tamanho de palavra 

'''tuplas com números
a = (2, 5 , 4)
b = (5, 8 , 1 ,2)
c = a + b -> (2, 5 , 4 ,5 ,8 ,1 ,2)
print(c .count(5)) ->> contar quantidade de numeros 5
print(c .index(5) ->> primeira aparição do número 5
'''


#print(lanche[0]) #HAMBURGUER
#print(lanche[1]) #SUCO
#print(lanche[2]) #PIZZA
#print(lanche[3]) #PUDIM
