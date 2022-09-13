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
for n1 in range(n1,x1+1,1):
    print(n1)