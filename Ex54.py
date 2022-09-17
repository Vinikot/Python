num=[]
num2=[]
c=int(input("Digite um valor para a constante: "))
for i in range(0,20,1):
    num.append(float(input("Digite um valor qualquer: ")))
    num2.append(num[i]*c)
for i in range(0,20,1):
    print(num[i],num2[i])