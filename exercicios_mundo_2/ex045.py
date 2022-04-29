import random
lista = ['pedra' , 'papel' , 'tesoura']
print('Vamos jogar JOKENPO. Suas opções: ')
computador = random.randint(0, 2)
jogador = int(input('''
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual a sua jogada? '''))

print('O computador jogou {}.'.format(lista[computador]))
print('O jogador escolheu {}.' .format(lista[jogador]))

if computador == 0: #pedra
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('O jogador ganhou.')
    elif jogador == 2:
        print('O computador ganhou.')
    else: 
        print('Comando invalido.')

elif computador == 1: #papel
    if jogador == 0:
        print('O computador ganhou.')
    elif jogador == 1:
        print('Empate.')
    elif jogador == 2:
        print('O jogador ganhou.')
    else:
        print('Comando invalido.')
        
elif computador == 2: #tesoura
    if jogador == 0:
        print('O jogador ganhou.')
    elif jogador == 1:
        print('O jogador perdeu.')
    elif jogador == 2:
        print('Empate.')
    else:
        print('Comando invalido.')
        