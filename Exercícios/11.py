from datetime import date

dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Ano'] = int(input('Ano de Nascimento: '))
dados['Idade'] = (date.today().year - dados['Ano'])
dados['CTPS'] = int(input('Carteira de trabalho [0 se não possuir]: '))

if dados['CTPS'] == 0:
    print(f'{dados["Nome"]} ainda não começou o seu periodo de contribuição trabalhista. Não possui carteira de trabalho. ')

else:
    dados['cont'] = int(input('Ano de contratação: '))
    dados['Aposentar'] = (dados['cont'] - dados["Ano"] + 35)
    dados['Salário'] = float(input('Salario: '))
    dados['Eco'] = float(input('Quanto você pretende guardar por mês: '))
    dados['tot'] = dados['Eco'] * 420

print('='*40)
print(f'{dados["Nome"]} tem {dados["Idade"]} anos, começou a trabalhar no ano de {dados["cont"]} e terá {dados["Aposentar"]} anos quanto aposentar.')
print(f'Se {dados["Nome"]} economizar por mês R${dados["Eco"]:.2f} ao final de 35 anos de contribuição, ele terá juntado {dados["tot"]:.2f}')