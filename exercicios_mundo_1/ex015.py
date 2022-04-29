km = float(input('Quantos km foram rodados? '))
d = int(input('Qauntos dias o carro ficou alugado?'))
preço = ((60 * d) + (0.15 * km))
print('Você deverá pagar: R$ {:.2f}' .format(preço))

