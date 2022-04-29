name = str(input('Digite o seu nome aqui: ')).strip()
split = name.split()
name1 = split[0]
name2 = split[-1]
print('''{}
Primeiro nome: {}
Ultimo nome: {}''' .format(name ,name1 ,name2))

