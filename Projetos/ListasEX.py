valores = []
print('-='*10)
for c in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
    maior = max(valores)
    menor = min(valores)
print(f'O maior número digitado foi {maior} e o menor foi {menor}')


