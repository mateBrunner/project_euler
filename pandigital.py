#!/usr/bin/python3.5

szum = 0
for i in range(1000000):
    if str(i) == str(i)[::-1]:
        a = bin(i)[2:]
        if a[::-1] == a:
            szum += i

print(szum)