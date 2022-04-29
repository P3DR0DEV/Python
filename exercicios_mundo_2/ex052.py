s = 0
n = int(input('Digite um número: '))
for c in range(1 , n +1):
    if n % c == 0:
        s += 1
print('O número {} foi divisível {} vezes.' .format(n , s))
if s > 2:
    print('Este número não é primo.')
else:
    print('Este número é primo.')
    