num=[]
for i in range(0,10,1):
    num.append(float(input("Digite um valor qualquer: ")))
    if(i==0):
        maior=num[i]
    if(maior<num[i]):
        maior=num[i]
print("O maior numero é:",maior)