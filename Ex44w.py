i=1
while(i<=10):
    num=int(input(f"Digite um valor positivo(n{i}): "))
    while(num<=0):
        print("Valor invalido!")
        num=int(input("Digite um valor positivo: "))
    #Verifica o maior numero.
    if(i==1):
        a=num
    elif(num>a):
        a=num
    #Faz a soma
    if(i==1):
        b=num
    else:
        b=b+num
    i=i+1
print("O maior valor é:",a,"\nA soma dos valores é:",b,"\nA media aritimetica é:",b/10)