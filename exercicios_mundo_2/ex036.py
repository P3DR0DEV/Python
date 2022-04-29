casa = float(input('Insira aqui o valor da casa desejada: R$'))
salario = float(input('Insira o salário do comprador: R$ '))
anos = float(input('Insira o tempo limite para o pagamento da casa (em anos): '))
tempo = anos * 12 #calculo de meses para a prestação
custo_parcela = casa / tempo # quantidade a se pagar por mes
emprestimo = custo_parcela / salario #porcentagem feita em cima do salário informado  (poderia ter usado apenas salario * 30/100)
print('Para pagar uma casa de {:.2f} em {} parcelas, o custo de cada parcela será de {:.2f}.' .format(casa , tempo , custo_parcela ))
if emprestimo <= 0.30: #se o valor da porcentagem for maior que 30% o emprestimo será negado
    print('O emprestimo pode ser feito.')
else:
    print('Emprestimo negado')

