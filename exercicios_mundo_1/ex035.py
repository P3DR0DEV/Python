primeiro = float(input('Digite o valor primeiro lado: '))
segundo = float(input('Digite o valor do segundo lado: '))
terceiro = float(input('Digite o valor do terceiro lado: '))

if terceiro < (primeiro + segundo) and primeiro < (segundo + terceiro) and segundo < (primeiro + terceiro):
    print('Os valores inseridos podem formar um triângulo')
else:
    print('Os valores inseridos não podem formar um triângulo')

