dados={}
dados['Nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))
dados['situação'] = ''
if dados['media'] < 5:
    dados['situação'] = 'foi Reprovado'
elif dados['media'] >= 7:
    dados['situação'] = 'foi Aprovado'
else:
    dados['situação'] = 'está Recuperação'
print(f'O aluno {dados["Nome"]} teve {dados["media"]} de média e foi {dados["situação"]}.')
for k, v in dados.items():
    print(f'O {k} é {v}.')
    