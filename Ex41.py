n=int(input("Digite um valor positivo menor que 100: "))
while(n<=0 or n>100):
    print("Valor invalido!")
    n=int(input("Digite um valor positivo menor que 100: "))

for i in range(1,n+1,1):
    a=((i+1)*(i+1))+1
    print(a)
