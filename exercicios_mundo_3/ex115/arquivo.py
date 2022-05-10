lista = []
def existeArq(nome): #verifica se o arquivo.txt existe
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome): # cria um arquivo.txt caso não exista
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso!')


def lerArq(nome):
    #Le o arquivo nome.txt
    try:
        arquivo = open(nome, 'rt')
        lista.clear()
    except:
        print('Erro ao ler o arquivo')
    else:
        print('--'*20)
        print('Pessoas Cadastradas'.center(40))
        print('--'*20)
        print(arquivo.readlines())



def editArq(nome): #Edita o arquivo
    dict = {}
    arquivo = open(nome, 'w+')
    dict['Nome'] =  str(input('Nome: '))
    dict['Idade'] = int(input('Idade: '))
    lista.append(dict)
    arquivo.write(f'{lista}')


def addList(nome):
    arquivo = open(nome, 'w+')
    arquivo.write(f'{lista}')
