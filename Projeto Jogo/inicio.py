from dados import dado, habilidade


resp = dado.menu('Guerreiro', 'Mago', 'Arqueiro', 'Sair')
if resp == 1:
    print('Você escolheu a Classe dos Guerreiros.')
    habilidade.ponto_habilidade()
elif resp == 2:
    print('Você escolhe a Classe dos Magos.')
    habilidade.ponto_habilidade()
elif resp == 3:
    print('Você escolheu a Classe dos Arqueiros.')    
    habilidade.ponto_habilidade()
elif resp == 4:
    print('Você escolheu sair.')
