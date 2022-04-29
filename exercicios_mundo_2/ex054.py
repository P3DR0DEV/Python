from datetime import date
ano = date.today().year
s = 0
for c in range(1,8):
    a = int(input('em que ano a {} pessoa nasceu: '.format(c)))
    idade = ano - a
    if idade >= 21:
        s += 1
print('desta lista {} pessoas são maiores de idade'.format(s))
c = c - s
print('{} não são maiores de idade.'.format(c))
