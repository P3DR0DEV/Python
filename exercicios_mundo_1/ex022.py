name = str(input('Digite seu nome completo: '))
print(name.upper())
print(name.lower())
num_name = len(name)
espaco = name.count(' ')  #lembrar de por o espaço entre aspas quando quiser contar a quantidade de espaços.
print('seu nome tem {} letras' .format(num_name - espaco))
s = name.split()
print('Seu primeiro nome tem {} letras' .format(len(s[0])))

