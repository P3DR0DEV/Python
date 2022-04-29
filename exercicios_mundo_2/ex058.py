from random import randint
print('-=-' *19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' *19)
s = 0
acertou = False
r = randint(0, 10) #randomizador do chute do computador

while not acertou:
    chute = int(input('Qual o seu palpite? '))
    s += 1 #contador de tentativas
    if r == chute:
        acertou = True
    else:
        if chute < r:
            print('Mais... Tente outra vez.')
        elif r > chute:
            print('Menos... Tente outra vez. ')

print('Você jogou o número {} e acertou depois de {} tentativas. Parabéns!' .format(chute , s))
