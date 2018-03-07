#!/usr/bin/python3.5
#champerpowne's constant #40

elemek = [1, 10, 100, 1000, 10000, 100000, 1000000]
result = ["a" for i in range(7)]


seged = 0
seged2 = 0
for i in range(1,200000):
    string = str(i)
    seged += len(string)
    if seged >= elemek[seged2]:
        kul = seged - elemek[seged2]
        print(i, seged, kul)
        result[seged2] = string[-1-kul]
        seged2 += 1
        if seged2 > 6: 
            break

print(result)





