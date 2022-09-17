r=()
while(r!="N"):
    n=int(input("Digite o numero(até 20) de valores a serem armazenados: "))
    while(n>20):
        print("Valor invalido!")
        n=int(input("Digite o numero(até 20) de valores a serem armazenados: "))
    num=[]
    for i in range(0,n,1):
        num.append(float(input("Digite um valor qualquer: ")))
    x=int(input("\nDigite um numero a ser buscado no vetor: "))
    i=0
    a=0
    for item in num:        
        if(x==item):
            print(f"O valor({x}) foi armazenado na posição({i}).")
            a=a+1
        elif(i==n-1 and a!=1):
            print("Valor não encontrada.")
        i=i+1
    r=input("Deseja uma nova execução? (S) ou (N): ")
    while((r!="S" and r!="N")):
        print("Apenas (S) ou (N).")
        r=input("Deseja uma nova execução? (S) ou (N): ")