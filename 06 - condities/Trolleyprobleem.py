
hendel_trekken = input('Trek aan de hendel van de wissel? (ja/nee)')
man_van_de_brug_duwen = input('Man van de brug duwen? (ja/nee)')

#aantal berekenen
if hendel_trekken == 'ja' and man_van_de_brug_duwen == 'ja':
    print('2')

elif hendel_trekken == 'nee' and man_van_de_brug_duwen == 'nee':
    print('5')

else:
    print('1')
