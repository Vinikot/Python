num=[]
c=int(input("Digite um valor para a constante: "))
for i in range(0,20,1):
    num.append(float(input("Digite um valor qualquer: ")))
    num[i]=num[i]*c
    print(num[i])