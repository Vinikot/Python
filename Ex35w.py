x = float(input("Digite um valor positivo: "))
while(x<=0):
    print("Valor invalido!")
    x = float(input("Digite um valor positivo: "))
i=1
while(i<=10):
    r = x * i
    print(f'{x} X {i} = {r}')
    i=i+1