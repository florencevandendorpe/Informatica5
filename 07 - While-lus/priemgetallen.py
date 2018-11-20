#invoer
getal = int(input('geef een getal :'))
a = 2
b = 1

#berekening
while a < getal:
    if (getal % a) == 0:
        resultaat = '{} is geen priemgetal'.format(getal)
        b = 0
    a += 1
if b and getal != 1:
    resultaat = '{} is een priemgetal'.format(getal)
elif getal == 1:
    resultaat  = '1 is geen priemgetal'

#uitvoer
print(resultaat)