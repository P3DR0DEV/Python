print('-='*19)
print(f'{"Lista de Compras":^40}')
print('-='*19)
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor' , 4.20,
            'Commpasso', 9.99,
            'Mochila', 120,
            'Canetas', 22,
            'Livro', 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print('R$', end='')
        print(f'{listagem[pos]:>6.2f}')
print('-='*19)