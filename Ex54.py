num=[]
num2=[]
for i in range(0,20,1):
    num.append(float(input("Digite um valor qualquer: ")))
    num2.append(num[i]*10)
for i in range(0,20,1):
    print(num[i],num2[i])