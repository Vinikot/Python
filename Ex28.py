a = int(input("Digite um valor inteiro(A):"))
b = int(input("Digite um valor inteiro(B):"))
if(b==a):
    b = int(input("(B) não pode ser igual a (A) ou (C)\nDigite um inteiro valor(B):"))
c = int(input("Digite um valor(C):"))
if(c==(a or b)):
    c = int(input("(C) não pode ser igual a (A) ou (B)\nDigite um inteiro valor(C):"))
if(a<(b) and (c)):
    print("(A)",a)
    if(b<c):
        print("(B)",b,"\n(C)",c)
    else:
        print("(C)",c,"\n(B)",b)
elif(b<(a) and (c)):
    print("(B)",b)
    if(a<c):
        print("(A)",a,"\n(C)",c)
    else:
        print("(C)",c,"\n(A)",a)
elif(c<(a) and (b)):
    print("(C)",c)
    if(b<a):
        print("(B)",b,"\n(A)",a)
    else:
        print("(A)",a,"\n(B)",b)