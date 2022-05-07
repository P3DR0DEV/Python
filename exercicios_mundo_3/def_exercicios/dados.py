def leiadinheiro(msg):
    valido = False
    while not valido:
        dado = str(input(msg)).replace(',','.').strip()
        if dado.isalpha() or dado == '':
            print(f'\033[31mERRO! \"{dado}\" não é um número válido.\033[m')
        else:
            valido = True
            return float(dado)