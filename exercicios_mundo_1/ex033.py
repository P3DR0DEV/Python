primeiro = float(input('Primeiro valor: '))
segundo = float(input('Segundo valor: '))
terceiro = float(input('Terceiro valor: '))

if primeiro <= segundo and primeiro <= terceiro:
    print('O menor valor é: {}' .format(primeiro))
elif primeiro >= segundo and segundo<= terceiro:
    print('O menor valor é {}' .format(segundo))
elif primeiro >= terceiro and segundo >= terceiro:
    print('O menor valor é {}' .format(terceiro))

if primeiro >= segundo and primeiro >= terceiro:
    print('O maior valor é {}' .format(primeiro))
elif primeiro <= segundo and segundo >= terceiro:
    print('O maior  valor é {}' .format(segundo))
elif primeiro <= terceiro and segundo <= terceiro:
    print('O maior valor é {}' .format(terceiro))

