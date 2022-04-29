print('Insira a seguir o resultado obtido nas provas.')
prova1 = float(input('Primeira prova: '))
prova2 = float(input('Segunda prova: '))
média = (prova1 + prova2) / 2

if média < 5:
    print('A sua média foi de {}, abaixo dos 5 pontos necessários para se qualificar para recuperação.' .format(média))
elif média >= 7:
    print('A sua média foi de {}, se mantendo acima do necessário, portanto está aprovado.' .format(média))
else:
    print('A sua média foi de {}, portanto, terá que fazer a recuperação.' .format(média))

