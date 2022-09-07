x = float(input("Digite um valor positivo: "))
while(x<=0):
    print("Valor invalido!")
    x = float(input("Digite um valor positivo: "))

a = int(input("Digite um valor(A): "))

b = int(input("Digite um valor(B) que seja maior que (A): "))
while(b<=a):
    print("Valor invalido!")
    b = float(input("Digite um valor(B) que seja maior que (A): "))

for i in range(b,a-1,-1):
    r = x * i
    print(f'{x} X {i} = {r}')