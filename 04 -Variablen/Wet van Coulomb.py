Q1 = (2.0 * 10 ** -4)
Q2 = (1.0 * 10 ** -4)

k = (8.99 * 10 ** 9)

r =float(input('geef straal: '))

FC= k * (Q1*Q2) / (r ** 2)

resultaat = str(FC)
print(resultaat)
