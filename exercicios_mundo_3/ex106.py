def ajuda(txt):
    print(help(txt))
def titulo(msg):
    tam = len(msg) +4
    print('=' * tam)
    print(f'\033[1;34m  {msg}\033[m')
    print('=' * tam)
from time import sleep

titulo('Sistema de Ajuda Python')
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        sleep(0.5)
        ajuda(comando)
    print('=-' * 30)
titulo('Até Logo!')
