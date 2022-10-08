num=[]
p=0
im=0
for i in range(0,20,1):
    num.append(int(input("Digite um numero: ")))
    if(num[i]!=0):
        if(num[i]%2==0):
            p=p+1
        else:
            im=im+1
x1=(p*100)/20
x2=(im*100)/20
print(f"Quantidade de valores pares: {p}({x1}%)\nQuantidade de valores impares: {im}({x2}%)")