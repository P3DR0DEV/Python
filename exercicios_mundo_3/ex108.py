from def_exercicios import moeda

coin = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.converter(coin)} vale {moeda.converter(moeda.metade(coin))}')
print(f'O dobro de {moeda.converter(coin)} vale {moeda.converter(moeda.dobro(coin))}')
print(f'Aumentando 10% temos {moeda.converter(moeda.aumentar(coin))}')