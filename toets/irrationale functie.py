#invoer
a = float(input('geef waarde van x: '))

#formule
from math import sqrt
b = sqrt(abs(((a) - 2)))

#berekening
if a < 2:
    print('{:.2f}'.format(a) + ' ∉ dom(f)')
elif a == 2:
    print('{:.2f}'.format(a) + ' is nulpunt van f')
else:
    print('f({:.2f})'.format(a) + ' = {:.2f}'.format(b))