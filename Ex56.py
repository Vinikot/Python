nome=[]
idade=[]
for i in range(0,100,1):
    nome.append(input(f"{i+1}°,Digite seu nome: "))
    idade.append(input(f"{i+1}°,Digite sua idade: "))
for i in range(0,100,1):
    print(f"{i+1}°Nome:{nome[i]}\n{i+1}°Idade:{idade[i]}\n")