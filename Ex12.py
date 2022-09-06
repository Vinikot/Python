a = float(input('Digite o lado(A): '))

b = float(input('Digite o lado(B): '))

c = float(input('Digite o lado(C): '))

if(a < b + c and b < a + c and c < b + c):
    if((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
        print("Os lados formam um Triângulo Isósceles.")
    else:
        if(a != (b and c) and b != c):
            print("Os lados formam um Triângulo Escaleno.")
        else:
            print("Os lados formam um Triângulo Equilátero.")
else:
    print("Os lados não formam um triângulo.")