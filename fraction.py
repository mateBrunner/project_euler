#!/usr/bin/python3.5

long_cycle = 0

for szam in range(1000,0,-1):
    if long_cycle >= szam: break 
    
    maradek = list([0]*szam)
    value = 1
    position = 0

    while maradek[value] == 0 and value != 0:
        maradek[value] = position
        value *= 10
        value %= szam
        position += 1

    if position - maradek[value] > long_cycle: long_cycle = position - maradek[value]
    print(szam, position-maradek[value])



