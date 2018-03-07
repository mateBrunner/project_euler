#!/usr/bin/python3.5
#pandigital multiples #38
from collections import Counter

#megnézi egy stringben, hogy van-e benne több különböző karakter, és 0
def kulonb(szoveg): 
    kulonb = True
    szotar = dict(Counter(szoveg))
    ertek = list(szotar.values())
    if (max(ertek) > 1) or ("0" in szoveg): kulonb = False
    return kulonb

maxi = "1"
maxiszam = 0


for szam in range(9500,0,-1):
    print(szam)
    if str(szam)[0] == "9":
        string = ""
        for ii in range(1,10):
            string += str(szam*ii)
            if len(string) == 9:
                if kulonb(string):
                    if string > maxi: 
                        maxi = string
                        maxiszam = szam
            if len(string) > 9:
                break

print(maxiszam, maxi)

