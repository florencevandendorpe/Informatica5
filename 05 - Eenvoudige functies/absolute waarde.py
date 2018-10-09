
x = float(input('x: '))
y = float(input('y: '))

#berekening
linker_lid = abs(x) - abs(y)
rechter_lid =abs(x - y)

#uitvoer
uitvoer = str(linker_lid) + '' + str(rechter_lid)

print('{:.4f} ≤ {:.4f}'.format(linker_lid, rechter_lid))


