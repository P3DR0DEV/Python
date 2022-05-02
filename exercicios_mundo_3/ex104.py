def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro! Digite um Número Válido.\033[m')
        if ok:
            return valor



n = leiaint('Digite um número: ')
print(f'\033[32mO número digitado foi {n}.\033[m')