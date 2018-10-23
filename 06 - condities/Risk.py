#invoer
a = int(input('het aantal ogen van aanvaller 1: '))
b = int(input('het aantal ogen van aanvaller 2: '))
c = int(input('het aantal ogen van aanvaller 3: '))
d = int(input('het aantal ogen van verdediger 1: '))
e = int(input('het aantal ogen van verdediger 2: '))

#berekening van het aantal verloren legers
f = max (a, b, c)
g = max (d, e)
h = a + b + c - f - min(a, b ,c)
i = d + e - g

if f > g and h > i:
    x = 0
    y = 2
    print('aanvaller verliest ' + str(x) + ' legers, verdediger verliest ' + str(y) + ' legers')
elif f <= g and h <= i:
    x = 2
    y = 0
    print('aanvaller verliest ' + str(x) + ' legers, verdediger verliest ' + str(y) + ' legers')
elif f <= g and h > i or f > g and h <= i:
    x = 1
    y = 1
    print('aanvaller verliest ' + str(x) + ' legers, verdediger verliest ' + str(y) + ' legers')
