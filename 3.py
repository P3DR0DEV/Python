lanche = ['Hamburguer', 'suco', 'pudim' , 'pizza' ]

#adicionar um item à uma lista:
lanche.append('Cookie') #adiciona um novo elemento à lista
lanche.insert(0,'cachorro quente') #insere na lista em um determinado local previamente assinalado

#remover um item de uma lista:
del lanche[3]
lanche.pop(3) #mais utilizado para remover o ultimo item da lista : lanche.pop()
lanche.remove('suco') #remove sem utilizar a sequencia numérica, utilizando o conteúdo

if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(4,11)) #para criar uma lista = list()
valores.sort() #ordenar de forma crescente
valores.sort(reverse=True) #ordenar de forma decrescente 

a = ['0','1','2','3']
b = a #ligação entre listas, o que fizer em uma se aplica a outra também 
b = a [:] #copia os valores da lista a, portanto se fizer uma mudança em uma lista, a outra continua intacta.


print(lanche)
