#!/usr/bin/python3.5

hossz= 99

lista = hossz**2

szamok = list()

for i in range(2,hossz+2):
    print(i)
    for j in range(2,hossz+2):
        if i**j not in szamok: szamok.append(i**j)


print(len(szamok))


