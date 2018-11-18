#invoer
prijs = 1
som = 0
#bereking
while prijs > 0:
    prijs = float(input('geef prijs: '))
    som += prijs



print('De totale prijs is €', '{:.2f}'.format(som ))