from ex115 import menu

while True:
    resp = menu.titulo('Ver Usuários Cadastrados', 'Cadastrar um Novo Usuário' , 'Sair do Sistema')
    if resp == 1:
        print('Opção 1')
    elif resp == 2:
        print('Opção 2')
    elif resp == 3:
        print('\033[31mO usuário escolheu sair.\033[m')
        break
        