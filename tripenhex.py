#!/usr/bin/python3.5
# triangular, pentagonal and hexagonal #45
import math


def ispentagonal(szam):
    tort = (math.sqrt(1+24*szam)+1)/6
    return tort == int(tort)

def istriangular(szam):
    tort = (math.sqrt(1+8*szam)-1)/2
    return tort == int(tort)

def ishexagonal(szam):
    tort = (math.sqrt(1+8*szam)+1)/4
    return tort == int(tort)

talalat = 0
i = 0
while talalat < 4:
    i += 1
    szam = i*(2*i-1)
    if ispentagonal(szam) and istriangular(szam):
        talalat += 1
        print(szam)
