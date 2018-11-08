#input
r = int(input('geef getal kleiner dan 100: '))
som_veelvouden = 0

#berekening
for i in range(r, 101, r):
    som_veelvouden += i


#output
print(som_veelvouden)