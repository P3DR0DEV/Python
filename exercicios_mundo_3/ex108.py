from def_exercicios import moeda

coin = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(coin)} vale {moeda.metade(coin, True)}')
print(f'O dobro de {moeda.moeda(coin)} vale {moeda.dobro(coin, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(coin, 10, True)}')