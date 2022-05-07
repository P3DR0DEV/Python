def leiadinheiro(msg):
    valido = False
    while not valido:
        var = str(input(msg))
        if var.isnumeric():
            valido = True
            return float(var)
        else:
            print(f'\033[31mERRO! \"{var}\" não é um número válido.\033[m')