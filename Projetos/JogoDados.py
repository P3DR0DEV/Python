from random import randint
from time import sleep
from operator import itemgetter

jogo = { 'Jogador1' : randint(1,6),
'Jogador2': randint(1,6),
'Jogador3': randint(1,6),
'Jogador4': randint(1,6)
}
ranking = list()

for k, v in jogo.items():
    print(f'O {k} tirou {v} ao jogar o dado.')
    sleep(1)

print('='*15)
print(f'{"Ranking":>11}')
print('='*15)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]}, tirou {v[1]}')
    sleep(1)

