matriz=[]
x=1
for i in range(0, 10, 1):
        matriz.append([])
while(x<40):
    for l in range(0, 10, 1):
        for c in range(0, 4, 1):
            matriz[l].append(x)
            print(matriz[l],x)
            x=x+1
for i in range(0, 10, 1):
    print(matriz[i])