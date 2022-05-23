def ponto_habilidade():
    pontos = {}
    while True:
        s = 0
        print('Você Possui 5 pontos para serem distribuidos.')
        força = int(input('Força: '))
        armadura = int(input('Armor: '))
        dex = int(input('Destreza: '))
        s = dex + força + armadura
        if s > 5:
            s = 0
            print('Você só pode utilizar 5 pontos de habilidade.')
        elif s == 5:
            break
        elif s <5:
            print(f'Adicione mais {5 - s} pontos e selecione 0 nos que não deseja adicionar mais .')  
    pontos['Força'] = int(força) 
    pontos['Armadura'] = int(armadura)
    pontos['Dex'] = int(dex)
    print(pontos)




