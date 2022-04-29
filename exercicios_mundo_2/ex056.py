s = 0
maiorIdadeH = 0
nomevelho =''
for c in range(1, 5):
    print('---- {} Pessoa ----' .format(c))
    nome= str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')) .strip()

    if c == 1 and sexo in 'mM':
        maiorIdadeH = idade
        nomevelho = nome
    
    if sexo in 'mM' and idade >maiorIdadeH:
        maiorIdadeH = idade
        nomevelho = nome
    
    if sexo in 'Ff' and idade < 20:
         s += 1
         médiaIdade = (s + idade) / c

print('A média da idade entre os participantes: {}' .format(médiaIdade)) 
print('O Homem mais velho tem {} anos e se chama {}.' .format(maiorIdadeH , nomevelho))
print('Tem {} mulheres menores de 20 anos.' .format(s))

