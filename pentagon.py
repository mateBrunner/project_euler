#!/usr/bin/python3.5
# pentagon numbers #44
import math


def ispentagon(szam):
    tort = (math.sqrt(1+24*szam)+1)/6
    return tort == int(tort)


result = 0
notfound = True
i = 1

while notfound:
    print(i)
    i += 1
    n = i * (3*i-1) / 2
    for j in range(i-1,0,-1):
        m = j * (3*j-1) / 2
        if ispentagon(n-m) and ispentagon(n+m):
            result = n-m
            notfound = False
            break

print(result)
