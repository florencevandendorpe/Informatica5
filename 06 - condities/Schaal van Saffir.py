windsnelheid = int(input('geef de windsnelheid van de orkaan in km/h: '))

if windsnelheid >= 119:
    if windsnelheid < 154:
        print('categorie 1')
    elif windsnelheid < 178:
        print('categorie 2')
    elif windsnelheid < 210:
        print('categorie 3')
    elif windsnelheid < 250:
        print('categorie 4')
    elif windsnelheid >= 250:
        print('categorie 5')
else:
    print('geen orkaan')