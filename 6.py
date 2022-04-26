soma = maior = coluna = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'Digite um valor para {l},{c}: '))
        if matriz[l][c] % 2 ==0:
            soma += matriz[l][c]
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*20)
print(f'A soma dos números pares dessa matriz equivale à: {soma}')
for l in range(0,3):
    coluna += matriz[l][2]
print(f'A soma dos valoras na terceira coluna equivale à: {coluna}')
for c in range(0,3):
    if c == 0:
            maior = matriz[1][c]
    elif maior < matriz[1][c]:
        maior = matriz[1][c]
print(f'O maior item da segunda linha equivale à: {maior}')
