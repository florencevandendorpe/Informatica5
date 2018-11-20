#invoer
woord = str(input('geef verborgen woord: '))
bedrag = int(input('geef bedrag: '))
letters = str(input('geef letters: '))
gewonnen_bedrag = 0
x = ''
#berekening
while letters in woord and letters not in x:
    gewonnen_bedrag += bedrag
    x += letters
    letters = str(input('geef letters: '))

if letters not in woord or letters in x:
    print(gewonnen_bedrag)


