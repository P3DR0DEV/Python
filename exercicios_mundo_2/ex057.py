sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in  'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registradocom sucesso!' .format(sexo)) 
