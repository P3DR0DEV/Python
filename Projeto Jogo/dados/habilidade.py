def ponto_habilidade(vida, arq= 0, mago= 0, warrior= 0):
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
    classe = arq + mago + warrior 
    pontos['Força'] = int(força)  + classe 
    pontos['Armadura'] = int(armadura)
    pontos['Dex'] = int(dex)
    pontos['Vida'] = int(vida)
    print(pontos)




