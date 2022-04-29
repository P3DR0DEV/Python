lista = list()
dict = dict()
print(f'Lanchonete do Esquilo')
print(f'1 - Pastel R$ 4,50')
print(f'2 - Coxinha R$ 4,00')
print(f'3 - Hamburguer R$ 12,00')
while True:
    cont = int(input('Digite o código do produto desejado [0 para fechar a compra]: '))
    if cont == 1:
        print('Você selecionou um Pastel.')
        lista.append(4.50)
    elif cont == 2:
        print('Você selecionou uma Coxinha.')
        lista.append(4.00)
    elif cont == 3:
        print('Você selecionou um Hamburguer.')
        lista.append(12.00)
    elif cont == 0:
        break
dict['total'] = sum(lista)
print(f'A sua compra deu R$ {dict["total"]}.')
while True:
    dinheiro = float((input('Quantidade do pagamento: ')))
    if dinheiro < dict['total']:
        print(f'Forma de pagamento negada, selecione outra quantia.')
    elif dinheiro >= dict['total']:
        print(f'Troco: R$ {dinheiro - dict["total"]}')
        break
print('Obrigado pela compra.')

