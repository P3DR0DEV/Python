from math import sin, cos, tan, radians
an = float(input('Digite o angulo que você deseja: '))
cos = cos (radians(an))
sin = sin (radians(an))
tan = tan (radians(an))
print('O seno de {} equivale a {:.2f}' .format(an, sin))
print('O cosseno de {} equivale a {:.2f}' .format(an ,cos))
print('A tangente de {} equivale a {:.2f}' .format(an ,tan))
