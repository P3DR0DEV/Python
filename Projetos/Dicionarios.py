dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input('Média: '))
dados['situação'] = ''
if dados['Média'] < 5:
    dados['situação'] = 'Reprovado'
elif dados['Média'] >= 7:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'em Recuperação'
print(f'O aluno {dados["Nome"]} teve uma média de {dados["Média"]} e está {dados["situação"]}.')
