def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade>=18:
        return f'Esta pessoa tem {idade} anos e seu voto é obrigatório.'
    elif idade <=16:
        return f'Esta pessoa tem {idade} anos e não pode votar.'
    else:
        return f'Esta pessoa tem {idade} anos e voto é Opcional.'

        
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))