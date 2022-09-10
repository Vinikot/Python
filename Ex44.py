for i in range(1,11,1):
    num=int(input("Digite um valor positivo: "))
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
print("O maior valor é:",a,"\nA soma dos valores é:",b,"\nA media aritimetica é:",b/10)
