#!/usr/bin/python3.5
# Digit cancelling fractions #33

def szamjegy(szam,n):
    szamjegy = int(str(szam)[n-1])
    return szamjegy


for szamlalo in range(10,100):
    for nevezo in range(10,100):
        if szamlalo % 10 != 0 and nevezo % 10 != 0:
            tort = szamlalo/nevezo
            if tort == szamjegy(szamlalo,1)/szamjegy(nevezo,1) and tort < 1:
                if szamjegy(szamlalo,2) == szamjegy(nevezo,2):
                    print(szamlalo, nevezo)
                    break
            if tort == szamjegy(szamlalo,1)/szamjegy(nevezo,2) and tort < 1:
                if szamjegy(szamlalo,2) == szamjegy(nevezo,1):
                    print(szamlalo, nevezo)
                    break
            if tort == szamjegy(szamlalo,2)/szamjegy(nevezo,1) and tort < 1:
                if szamjegy(szamlalo,1) == szamjegy(nevezo,2):
                    print(szamlalo, nevezo)
                    break
            if tort == szamjegy(szamlalo,2)/szamjegy(nevezo,2) and tort < 1:
                if szamjegy(szamlalo,1) == szamjegy(nevezo,1):
                    break
                    print(szamlalo, nevezo)



