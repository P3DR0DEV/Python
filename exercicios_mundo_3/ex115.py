from ex115 import menu , arquivo


if not arquivo.existeArq('Teste.txt'):
    arquivo.criarArq('Teste.txt')

while True:
    resp = menu.titulo('Ver Usuários Cadastrados', 'Cadastrar um Novo Usuário' , 'Sair do Sistema')
    if resp == 1:
        #lista o conteúdo do arquivo
        arquivo.lerArq('Teste.txt')
    elif resp == 2:
        arquivo.editArq('Teste.txt')
    elif resp == 3:
        arquivo.addList('Teste.txt')
        print('\033[31mO usuário escolheu sair.\033[m')
        break
        