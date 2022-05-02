def jogador(nome = '<desconhecido>', gols = 0):
    """
    -> Mostra uma Ficha do jogador
    :param nome: Nome do Jogador, se não informado, então jogador desconhecido.
    :param gols: Quantidade de gols feita, se não informado, então número de gols = 0
    """
    print('-'*30)
    print(f'O jogador {nome} marcou {gols} gols.')



n =str(input('Nome do Jogador: '))
g =str(input('Quantidade de gols: '))
if g.isnumeric():
    g= int(g)
else:
    g=0

if n.strip() == '':
    jogador(gols = g)
else:
    jogador(n, g)
