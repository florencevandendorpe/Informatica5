#input
som = 0
kaarten = 1

#berekening
while kaarten > 0 and som < 21:
    kaarten = int(input('geef kaart met waarde van 1 tot 11: '))
    som = kaarten + som
if som >= 22:
    print('Verbrand ({})'.format(som))
elif som <= 20:
    print('Voorzichtig gespeeld ({})'.format(som))
else:
    print('Gewonnen!')





