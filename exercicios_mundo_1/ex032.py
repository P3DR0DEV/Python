ano = int(input('Insira o ano que você quer analisar: ')) 
if ano % 4 == 0 and ano % 100 != 0 and ano % 400 !=0:
    print('O ano de {} é bissexto!' .format(ano))
else:
    print('O ano de {} não é bissexto!' .format(ano)) 
