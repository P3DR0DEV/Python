from def_exercicios import moeda

coin = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(coin)} vale {moeda.moeda(moeda.metade(coin))}')
print(f'O dobro de {moeda.moeda(coin)} vale {moeda.moeda(moeda.dobro(coin))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(coin))}')