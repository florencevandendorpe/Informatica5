#invoer
a = int(input('geef getallen : '))
max = 0
som = 0

#uitvoer
for i in range(a):
    getal = int(input('getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

gemiddelde = round((som / a), 2)

#uitvoer
print('Het grootste getal is ' + str(max) + ' en het gemiddelde is ' + str('{.2f}'.format(gemiddelde)))







#uivoer
print('het grootste getal is ' + 'en het gemiddelde is ' + )