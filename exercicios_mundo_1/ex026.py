frase = str(input('Digite uma frase: ').strip())
a = frase.upper().count('A')
a1 = frase.upper().find('A'+1)
al = frase.upper().rfind('A'+1)
print('''Nesta frase existem {} A\'s 
O primeiro A está localizado na {} posição
O ultimo A está localizado na {} posição
''' .format(a ,a1 ,al))

