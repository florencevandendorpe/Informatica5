#invoer
woord = input('geef verborgen woord: ')
bedrag = int(input('geef bedrag: '))
letters = input('geef letters: ')
gewonnen_bedrag = 0

#berekening
while letters in woord:
    letters = input('geef letters: ')
    gewonnen_bedrag = gewonnen_bedrag + bedrag
if letters not in woord:
    print(gewonnen_bedrag)
