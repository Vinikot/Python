c=1
b=1
a=0
for i in range(1,31,1):   
    c=b+a
    a=b
    b=c
    print(c)