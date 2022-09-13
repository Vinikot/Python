a=int(input("Digite um valor qualquer(A): "))
b=int(input("Digite um valor qualquer(B): "))
while(a==b):
    print("Invalido! Os valores não podem ser iguais.")
    b=int(input("Digite um valor qualquer(B): "))

if(a>b):
    x1=a
    n1=b
else:
    n1=a
    x1=b
for n1 in range(n1,x1+1,1):
    if((n1%2)==0 and (n1>10)):
        print(n1)