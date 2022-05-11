from ex115 import menu , arquivo

arq = 'Teste.txt'
if not arquivo.existeArq(arq):
    arquivo.criarArq(arq)

while True:
    resp = menu.titulo('Ver Usuários Cadastrados', 'Cadastrar um Novo Usuário' , 'Sair do Sistema')
    if resp == 1:
        #lista o conteúdo do arquivo
        arquivo.lerArq(arq)
    elif resp == 2:
        #Cadastra um Novo Usuário
        print('--'*20)
        print('NOVO CADASTRO'.center(40))
        print('--'*20)
        nome = str(input('\033[33mNome: \033[m'))
        idade = menu.leiaint('\033[33mIdade: \033[m')
        arquivo.cadastro(arq, nome, idade)
    elif resp == 3:
        print('\033[31mO usuário escolheu sair.\033[m')
        break
    elif resp == 4:
        arquivo.apagaArq()
        