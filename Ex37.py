x = float(input("Digite um valor positivo: "))
while(x<=0 or x>20):
    print("Valor invalido!")
    x = float(input("Digite um valor positivo: "))

for i in range(1,11,1):
    r = x * i
    print(f'{x} X {i} = {r}')
    input("Pressione uma tecla:")