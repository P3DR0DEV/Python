preço = float(input('Digite o preço do produto: R$ '))
cond = int(input('''Selecione o método de pagamento:
[1] Dinheiro/Cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão 
Método escolhido:  '''))

if cond == 1:
    print('O preço a se pagar será  de : {:.2f} , após a aplicação do desconto.' .format(preço - (preço * 10 / 100)))
elif cond == 2:
    print('O preço a se pagar será de: {:.2f}, após a aplicação de desconto no cartão.' .format(preço - (preço * 5 /100)))
elif cond == 3:
    print('O preço a se pagar será de {:.2f}, com 2 parcelas de {:.2f}.' .format (preço , preço/2))
elif cond == 4:
    quantParcela = int(input('Deseja pagar em quantas parcelas? '))
    total = preço + ( preço * 20/100)
    print('Com a aplicação de juros, o preço total será de {:.2f}, em {} parcelas de R$ {:.2f}. ' .format(total , quantParcela , total / quantParcela))
else:
    print('Comando inválido.')

