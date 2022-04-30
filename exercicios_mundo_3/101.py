from datetime import date
def voto(nasc):
    idade = date.today().year - nasc
    if idade>=18:
        print(f'Esta pessoa tem {idade} anos e seu voto é obrigatório.')
    elif idade <=16:
        print(f'Esta pessoa tem {idade} e não pode votar.')
    else:
        print(f'Esta pessoa tem {idade} anos e voto é Opcional.')

        
voto(int(input('Ano de nascimento: ')))