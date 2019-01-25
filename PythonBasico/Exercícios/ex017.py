import math
x = float(input('Digite o comprimento do cateto oposto: '))
y = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é {:.2f}'.format(math.hypot(x, y)))
