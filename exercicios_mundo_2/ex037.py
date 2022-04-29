numero = int(input('Digite um número inteiro: '))
n = int(input('Digite \'1\' para converter o número para binário, digite \'2\' para octal e \'3\' para hexadecimal: '))
#binário
if n == 1:
    print('{} convertido para binário equivale a {}' .format(numero ,bin(numero) [2:]))
#octal
elif n == 2:
    print('{} convertido para octal equivale a {}' .format(numero, oct(numero) [2:]))
#hexadecimal
elif n == 3:
    print('{} convertido para hexadecimal equivale a {}' .format(numero, hex(numero) [2:]))
else:
    print('Comando inválido.')

