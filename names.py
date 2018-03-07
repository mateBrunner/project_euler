#!/usr/bin/python3.5

with open('names.txt', 'r') as f:
    names = f.read()     #egy nagy string-be olvassa be

text = [x.strip() for x in names.split(',')]   #egy listát csinál a names-ből, a vesszőknél vágja szét

text = [text[i][1:-1] for i in range(len(text))] #a lista minden elemének levágja az első és utolsó betűjét

print(text[0])

abc = ["abc",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

szumma = 0
seged = 0
for szo in text:
    seged += 1
    szopont = 0
    for c in szo:
        for x in range(len(abc)):
            if abc[x].upper() == c: szopont += x
    szumma += szopont *seged

print(szumma)
    