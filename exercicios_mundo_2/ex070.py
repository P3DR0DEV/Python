soma = prod1000 = menor = cont = barato = 0
print('-' * 20)
print('Loja Super Baratão')
print('-' * 20)
while True:
    nomeP = str(input('Nome do Produto: '))
    preçoP = float(input('Preço: R$ '))
    cont += 1
    if cont == 1 or preçoP < menor: #MENOR COMPRA 
        menor = preçoP
        barato = nomeP

    conti = ' '
    while conti not in 'SN':
        conti = str(input('Deseja continuar comprando? (S/N) ')).upper().strip()[0]

    if preçoP >= 1000: #PRODUTO > 1000 REAIS 
        prod1000 += 1
    

    soma += preçoP #CUSTO TOTAL DA COMPRA
    if conti == 'N':
        break
print('=' * 20)
print(f'''O preço total do seu carrinho equivale à R$ {soma:.2f}.
No seu carrinho {prod1000} produtos custam mais de 1000.00 reais.
O produto mais barato é o {barato} e custa {menor:.2f}. ''')
