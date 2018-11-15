n = int(input('Hoeveeste getal van Fibonacci: '))

vorige, huidige = 1, 1

for i in range(n-2):
    vorige, huidige = huidige, huidige + vorige


print(huidige)