nome=[]
sex=[]
idade=[]
for i in range(0,3,1):
    nome.append(input("Digite seu nome: "))
    sex.append(input("DIgite seu sexo (apenas 'm' ou 'f'): "))
    idade.append(int(input("Digite sua idade: ")))
    print(i)
for i in range(0,3,1):
    a=0
    b=()
    c=()
    for j in range(i+1,3,1):
        if(idade[i]<idade[j]):
            a=idade[i]
            b=nome[i]
            c=sex[i]
            idade[i]=idade[j]
            nome[i]=nome[j]
            sex[i]=sex[j]
            idade[j]=a
            nome[j]=b
            sex[j]=c
for i in range(0,3,1):
    print(f"Nome({i}°): ",nome[i])
    print(f"Sexo({i}°): ",sex[i])
    print(f"Idade({i}°): ",idade[i])