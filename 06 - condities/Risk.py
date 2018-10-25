#invoer
a = float(input('het aantal ogen van aanvaller 1: '))
b = float(input('het aantal ogen van aanvaller 2: '))
c = float(input('het aantal ogen van aanvaller 3: '))
d = float(input('het aantal ogen van verdediger 1: '))
e = float(input('het aantal ogen van verdediger 2: '))

#sorteren
f = max(a, b, c)
g = max(d, e)
h = a + b + c - f - min(a, b, c)
i = d + e - g

#berekening van het aantal verloren legers
if f > g and h > i:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
elif f <= g and h <= i:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
else:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
