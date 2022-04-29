from time import sleep
jogador = dict()
partidas = list()

jogador['Nome'] = str(input('Nome: '))
cont = int(input(f'Quantos jogos {jogador["Nome"]} jogou? '))
for c in range(0,cont):
    partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez no jogo {c + 1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-' * 15)
print(f'{jogador["Nome"]} disputou {cont} jogos no campeonato e marcou {jogador["total"]} Gols!')

sleep(1)

continuar = str(input('Deseja ver as estatísticas? [S/N] ')).upper()
if continuar in 'S':
    for k, v in enumerate(jogador['gols']):
        print(f'No {k + 1}° jogo ele marcou {v} gols.')
        
