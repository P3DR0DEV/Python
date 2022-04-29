p = float(input('Qual o preço do produto? R$'))
a = p - (p * 10 / 100)
parcelado = p + (p * 8 / 100)
print('O produto custa {:.2f} reais, avista {:.2f} e parcelado {:.2f}' .format(p, a ,parcelado))

