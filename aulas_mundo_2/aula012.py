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
    elif:
        carro.siga()
    else:
        carro.siga()
        carro.esqueda()
        carro.siga()
        carro.esquerda()
        carro.siga()
   carro.pare()'''
nome = str(input('Qual o seu nome? '))
if nome == 'Pedro':
    print('que belo nome!')
elif nome == 'Maria' or nome == 'Paulo':
    print('Nome de viado, dog!')
print('Tenha um bom dia, {}' .format(nome)) 
