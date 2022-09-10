n=int(input("Digite um valor positivo menor que 50: "))
while(n<=0 or n>50):
    print("Valor invalido!")
    n=int(input("Digite um valor positivo menor que 50: "))

i=1
a=((i+1)*(i+1))+1
b=(i+1)**3
x=(a/b)+2
for i in range(2,n+2,1):
    print(x)
    x=x+(a/b)
