def area(l, h):
   print(f'A área deste retângulo equivale à: {l * h:.2f} m²')
def mensagem(txt):
    tam = len(txt) +4
    print('='*tam)
    print(f'  {txt}')
    print('='*tam)


mensagem('Trigonometria')
area(l =float(input('Lado A (m): ')), h = float(input('Lado B (m): ')))
#teste de commit