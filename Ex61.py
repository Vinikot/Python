num=[]
for i in range(0,10,1):
    num.append(int(input("Digite um valor qualquer: ")))
for i in range(0,10,1):
    for j in range(i+1,10,1):
        if(num[i]>num[j]):
            x=num[i]
            num[i]=num[j]
            num[j]=x
for item in num:
    print(item)