v = int(input('Insira a velocida do veículo no momento em que passou pelo radar: '))
if v <= 80:
    print('Você está limpo! Dirija com cuidado.')
else:
    print('MULTADO! O preço a se pagar é R$ {:.2f}!' .format((v - 80)*7))
#(v-80)*7

