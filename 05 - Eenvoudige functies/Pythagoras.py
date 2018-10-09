#invoer
a = float(input('a: '))
b = float(input('b: '))

#berekening
from math import sqrt
c = sqrt( a ** 2 + b ** 2)



#schuine zijde berekenen
print('In een rechthoekige driehoek met rechthoekszijden a = ' + ('{:.2f}'.format(a)) +  ' en b = ' + ('{:.2f}'.format(b)) + ' is de schuine zijde ' + ('{:.2f}'.format(c)))