jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    partidas.clear()
    print('=-'*20)
    jogador['Nome'] = str(input('Nome: '))
    jogador['tot'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    if jogador['tot'] == 0:
        break
    for c in range(0,jogador['tot']):
        partidas.append(int(input(f'Quantos gols ele marcou no jogo {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('=-'*20)
print(f'{"Nº":<5}|{"Nome":^10}|{"Jogos":^10}|{"tot. Gols"}|')
for k, v in enumerate(time):
    print(f'{k:<5}|{v["Nome"]:^10}|{v["tot"]:^10}|{v["total"]:>8} |')
while True:
    continua = int(input('Digite o número do jogador para obter melhores info [999 para o programa]: '))
    if continua == 999:
        break
    if continua >= len(time):
        print(f'Não existe jogador com este número.')
    else:
        print(f'{time[continua]["Nome"]}: ')
        for k, v in enumerate(time[continua]['gols']):
            print(f'{k+1}º Jogo {time[continua]["Nome"]} marcou {v} gol(s)')