a = float(input('Digite o primeiro valor(A): '))

b = float(input('Digite o segundo valor(B): '))

c = float(input('Digite o terceiro valor(C): '))

if(a > (b and c)):
    print("A é o maior valor.")
elif(b > (a and c)):
    print("B é o maior valor.")
else:
    print("C é o maior valor.")