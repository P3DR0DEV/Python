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
    except:
        print('Erro ao ler o arquivo')
    else:
        print('--'*20)
        print('Pessoas Cadastradas'.center(40))
        print('--'*20)
        print(f'{arquivo.read()}')
    finally:
        arquivo.close()



def cadastro(arq, nome = 'Desconhecido', idade = 0):
    try: 
        arquivo = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            arquivo.write(f'{nome:<30}{idade:3} anos\n')
        except:
            print('Houve um erro ao escrever no arquivo.')
        else:
            print(f'Novo registro de {nome}.')
            arquivo.close

