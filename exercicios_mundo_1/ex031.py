viagem = float(input('Quer saber quanto sua viagem de natal vai custar? Digite a distância em km: '))
longa = (viagem * 0.45) 
curta = (viagem * 0.50)
if viagem >= 200:
    print('O custo da viagem será de R$ {:.2f}!' .format(longa)) 
else:
    print('O custo da viagem será de R$ {:.2f}!' .format(curta))

