#invoer
a = float(input('geef waarde van x: '))
a
from math import sqrt
b = sqrt(a) - sqrt(2)

#berekening
if a < 2:
    print('{:.2f}'.format(a) + ' NOT AN ELEMENT OF dom(f)')
elif a == 2:
    print('{:.2f}'.format(a) + ' is nulpunt van f')
else:
    print('f({:.2f})'.format(a) + ' = {:.2f}'.format(b))