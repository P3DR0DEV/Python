from math import sqrt
catop = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimentod o cateto adjacente: '))
raiz = sqrt (catop ** 2 + catadj ** 2)
print ('A hipotenusa desse triangulo equivale à {:.2f}' .format(raiz))

#math.hypot(catop, catadj) <  hipotenusa
