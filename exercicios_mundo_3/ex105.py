def notas(*n, sit= False):
    """
    -> Mostra as Notas, Quantidade, Maior, Menor e Média.
    :param n: Dicionário onde está contida as notas. (Aceita várias)
    :param sit: (Opicional) Mostra a situação do aluno baseado na média.
    :return: Dicionário com informações sobre a situação da Turma 
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n) /r['Total']
    if sit:
        if r['Media'] <= 5:
            r['Situação']= 'Ruim.'
        elif r['Media'] >= 7:
            r['Situação'] = 'Boa.'
        else:
            r['Situação'] = 'Mediana'
    return r

resp = notas(6, 5, 5, 6, sit = True)
print(resp)
help(notas)