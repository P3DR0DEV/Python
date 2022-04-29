num = (int(input('Número um: ')), int(input('Outro número: ')), int(input('Outro número: ')), int(input('Ultimo: '))) 
if num == 9:
    print(f'O número 9 aparece {num.count(9)} vezes.')
if num == 3:
    print(f'O número 3 aparece na {num.index(3)} posição.')
print('Os valores pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
