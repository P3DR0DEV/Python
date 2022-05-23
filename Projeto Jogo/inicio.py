from dados import dado, habilidade


vida_guerreiro = 100
vida_mago = vida_arqueiro = 90 

resp = dado.menu('Guerreiro', 'Mago', 'Arqueiro', 'Sair')
if resp == 1:
    print('Você escolheu a Classe dos Guerreiros.')
    habilidade.ponto_habilidade(vida_guerreiro, warrior=0)

elif resp == 2:
    print('Você escolhe a Classe dos Magos.')
    habilidade.ponto_habilidade(vida_mago, mago= 1)

elif resp == 3:
    print('Você escolheu a Classe dos Arqueiros.')    
    habilidade.ponto_habilidade(vida_arqueiro, arq= 1)
    
elif resp == 4:
    print('Você escolheu sair.')
