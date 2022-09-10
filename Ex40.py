d=0
c=1
b=1
a=-1
print(f"{b}\n{c}")
for i in range(1,21,1):   
    d=c+b+a
    a=b
    b=c
    c=d
    print(d)