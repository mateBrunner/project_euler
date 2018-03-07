#!/usr/bin/python3.5
#substring divisibility #43
from collections import Counter
import math

#megnézi egy stringben, hogy van-e benne több különböző karakter, és 0
def kulonb(szoveg): 
    kulonb = True
    szotar = dict(Counter(szoveg))
    ertek = list(szotar.values())
    if (max(ertek) > 1): kulonb = False
    return kulonb


def kovetkezo(n):
    szoveg = str(n)
    hossz = len(szoveg)
    lista = [int(c) for c in szoveg]
    atiras = False
    for i in range(hossz-1,-1,-1):
        while lista[i] > 0:
            lista[i] -= 1
            if lista[i] not in lista[:i]:
                for ii in range(i+1,hossz):
                    for j in range(hossz-1,-1,-1):
                        if j not in lista[:ii]:
                            lista[ii] = j
                            atiras = True
                            break
                break
        if atiras: break
    
    szoveg = "".join([str(c) for c in lista])
    return int(szoveg)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def harmas(szam,a,b,c):
    text = str(szam)
    harmas = "".join([text[a-1], text[b-1], text[c-1]])
    harmas = int(harmas)
    return harmas

prim = [2,3,5,7,11,13,17]
jok = 0

szam = 9876543210
while szam > 1000000000:
    szam = kovetkezo(szam)
    oke = True
    for i in range(len(prim)):
        if harmas(szam,8-i,9-i,10-i)%prim[-(i+1)] != 0: 
            oke = False
            break
    if oke: 
        print("joooooo",    szam)
        jok += szam
        print(jok)


    

