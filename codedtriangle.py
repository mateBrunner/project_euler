#!/usr/bin/python3.5
# Coded triangle numbers #42

with open('triangle42.txt', 'r') as f:
    words = f.read()     #egy nagy string-be olvassa be

text = [x.strip() for x in words.split(',')]   #egy listát csinál a names-ből, a vesszőknél vágja szét
text = [text[i][1:-1] for i in range(len(text))] #a lista minden elemének levágja az első és utolsó betűjét

abc = ["abc",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

triangle = []
for i in range(100):
    triangle.append(0.5*i*(i+1))


hanyszo = 0

for szo in text:
    szopont = 0
    for c in szo:
        for x in range(len(abc)):
            if abc[x].upper() == c: szopont += x
    if szopont in triangle: hanyszo += 1
    if szopont > triangle[-1]: print(szopont, triangle[-1])
print(hanyszo)
