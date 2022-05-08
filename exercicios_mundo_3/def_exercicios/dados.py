def leiadinheiro(msg):
    valido = False
    while not valido:
        dado = str(input(msg)).replace(',','.').strip()
        if dado.isalpha() or dado == '':
            print(f'\033[31mERRO! \"{dado}\" não é um número válido.\033[m')
        else:
            valido = True
            return float(dado)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro Válido.')
            continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar um número')
            return None
        else:
            return n
 

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! O número digitado não é Real.')
        except KeyboardInterrupt:
            print('\n O usuário preferiu não informar um dado')
            return None
        else:
            return n 