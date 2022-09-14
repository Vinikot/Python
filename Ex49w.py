n=int(input("Digite um valor qualquer(n): "))
x=int(input("Digite um valor qualquer(x): "))
while(n==x):
    print("Invalido! Os valores não podem ser iguais.")
    x=int(input("Digite um valor qualquer(x): "))
if(n>x):
    x1=n
    n1=x
else:
    n1=n
    x1=x
a=n1
while(n1<=x1):
    if(n1==a):
        s=n1
    else:
        s=s+n1
    n1=n1+1
print(s)