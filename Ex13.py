x = float(input('Digite o lado(A): '))

y = float(input('Digite o lado(B): '))

z = float(input('Digite o lado(C): '))

if(x > (y and z) and x != (y and z)):
    c = x; a = y; b = z 
elif(y > (x and z) and y !=(x and z)):
    c = y; a = x; b = z
else:
    c = z; a = x; b = y

if((a*a) + (b*b) == (c*c)):
    print("Os lado formam um Triângulo Retângulo.")
else:
    print("Os lados não formam um Triângulo Retângulo")
