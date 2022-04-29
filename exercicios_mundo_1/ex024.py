cidade = str(input('Digite o nome de uma cidade: ') .strip())
santo = cidade[:5].upper() == 'SANTO'
print('O nome dessa cidade começa com a palavra santo? {}' .format(santo))
