import random
print('-=-'*19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*19) 
r = random.randint(0, 5)
n = int(input('Em que número eu pensei? '))
if n == r:
    print('Parabéns você conseguiu acertar!')
else:
    print('Você não conseguiu acertar. :( ')

