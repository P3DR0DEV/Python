'''carro.siga()
    if carro.esquerda():
        carro.siga()
         carro.direita()
        carro.siga()
        carro.direita()
        carro.esquerda()
        carro.siga()
        carro.direita()
        carro.siga()
    else:
        carro.siga()
        carro.esqueda()
        carro.siga()
        carro.esquerda()
        carro.siga()
   carro.pare()'''
tempo = int(input('Quantos anos tem o seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('carro velho') 
print('----FIM----')
    #print('carro novo' if tempo<= 3 else'carro velho') 
    
