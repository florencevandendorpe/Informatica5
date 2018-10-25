#uitvoer
d1 = float(input('verkeersdrukte vrachtwagens: '))
v1 = float(input('snelheid vrachtverkeer: '))
d2 = float(input('verkeersdrukte auto\s: '))
v2 = float(input('snelheid autoverkeer: '))

#berekening
pv = min(((v1 * d1) / 40), 1)
pa = min(((v2 * d2) / 40), 1)

if min(pv, pa) > 0.7:
    print('zwart')
elif max(pv, pa) > 0.7 and abs(pv - pa) < 0.2:
    print('rood')
elif abs(pv - pa) > 0.7:
    print('geel')
else:
    print('groen')