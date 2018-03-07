#!/usr/bin/python3.5
#pandigital prime #41
from collections import Counter
import math

#megnézi egy stringben, hogy van-e benne több különböző karakter, és 0
def kulonb(szoveg): 
    kulonb = True
    szotar = dict(Counter(szoveg))
    ertek = list(szotar.values())
    if (max(ertek) > 1) or ("0" in szoveg): kulonb = False
    return kulonb

def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def kovetkezo(n):
    szoveg = str(n)
    hossz = len(szoveg)
    lista = [int(c) for c in szoveg]
    atiras = False
    for i in range(hossz-1,-1,-1):
        while lista[i] > 1:
            lista[i] -= 1
            if lista[i] not in lista[:i]:
                for ii in range(i+1,hossz):
                    for j in range(hossz,0,-1):
                        if j not in lista[:ii]:
                            lista[ii] = j
                            atiras = True
                            break
                break
        if atiras: break
    
    szoveg = "".join([str(c) for c in lista])
    return int(szoveg)


szam = 7654321
while True:
    szam = kovetkezo(szam)
    print(szam)
    if is_prime(szam): break

print(is_prime(7652413))
