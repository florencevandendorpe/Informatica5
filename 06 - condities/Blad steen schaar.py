#invoer
speler_1 = input('Blad steen schaar? ')
speler_2 = input('Blad steen schaar? ')

#winnaar berekenen
if speler_1 == 'steen' and speler_2 == 'schaar':
    print('Speler 1 wint')
elif speler_1 == speler_2:
    print('onbeslist')
elif speler_1 == 'schaar' and speler_2 == 'blad':
    print('Speler 1 wint')
elif speler_2 == 'blad ' and speler_2 == 'steen':
    print('Speler 1 wint')
else:
    print('speler 2 wint')