a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

if (a > b > c):
    print("\n(A):",a,"\n(B):", b,"\n(C):", c)

elif(a > c > b):
    print("\n(A):",a,"\n(C):", c,"\n(B):", b)

elif(b > a > c):
    print("\n(B):",b,"\n(A):", a,"\n(C):", c)

elif(b > c > a):
    print("\n(B):",b,"\n(C):", c,"\n(A):", a)

elif(c > a > b):
    print("\n(C):",c,"\n(A):", a,"\n(B):", b)
else:
    print("\n(C):",c,"\n(B):", b,"\n(A):", a)