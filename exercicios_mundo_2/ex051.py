i = int(input('Digite o primeiro dermo da P.A: '))
r = int(input('Digite a razão desta P.A: '))
décimo = i + (10 - 1) * r  #enézimo termo de uma P.A
for c in range(i, décimo + r, r):
    print(c , end=' ->')
print('acabou')

