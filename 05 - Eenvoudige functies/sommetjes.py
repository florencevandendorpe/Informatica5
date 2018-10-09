#invoer
a = float(input('a: '))
b = float(input('b: '))
from random import random, randint, seed

#berekening
getal_1 = (10 ** 0) * a
getal_2 = (10 ** 0) * b
som_1 = getal_1 + getal_2

getal_3 = (10 ** 1) * a
getal_4 = (10 ** 1) * b
som_2= getal_3 + getal_4

getal_5 = (10 ** 2) * a
getal_6= (10 ** 2) * b
som_3 = getal_5+ getal_6

getal_7 = (10 ** 3) * a
getal_8 = (10 ** 3) * b
som_4 = getal_7 + getal_8

getal_9 =(10 ** 4) * a
getal_10 = (10 ** 4) * b
som_5 = getal_9 + getal_10

#uitvoer
print('{:>6.0f} + {:<6.0f} = {:>6.0f}'.format(getal_1, getal_2, som_1))
print('{:>6.0f} + {:<6.0f} = {:>6.0f}'.format(getal_3, getal_4, som_2))
print('{:>6.0f} + {:<6.0f} = {:>6.0f}'.format(getal_5, getal_6, som_3))
print('{:>6.0f} + {:<6.0f} = {:>6.0f}'.format(getal_7, getal_8, som_4))
print('{:>6.0f} + {:<6.0f} = {:>6.0f}'.format(getal_9, getal_10, som_5))