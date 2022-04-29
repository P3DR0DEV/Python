cont = homens = mulheres = age18 =  0
while True:
    print('-' * 20)
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Quantos anos você tem? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? (M/F) ')).upper().strip()[0]

    conti = ' '
    while conti not in 'SN': 
        conti = str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
    cont += 1

    if sexo in 'mM': #verificação homens
        homens += 1

    if sexo in 'fF' and idade <20: #verificação mulheres menores de 20
        mulheres += 1

    if idade >= 18: #verificação de pessoas com mais de 18 anos
        age18 += 1

    if conti in 'Nn':
        break
print('-' * 20)
print(f'''{cont} pessoas foram entrevistadas. 
{age18} são maiores de idade.
{homens} são homens.
{mulheres} são mulheres com menos de 20 anos de idade''') 
