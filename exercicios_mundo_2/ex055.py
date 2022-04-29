lista = []
for c in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: Kg ' .format(c)))
    lista += [peso]
print('O maior peso foi: {} Kg.' .format(max(lista)))
print('O menor peso foi: {} Kg.'  .format(min(lista)))

