nome=[]
idade=[]
sexo=[]
j=0
for i in range(0,5,1):
    nome.append(input(f"{i+1}°,Digite seu nome: "))
    idade.append(int(input(f"{i+1}°,Digite sua idade (APENAS VALORES POSITIVOS!): ")))
    while(idade[i]<=0):
        idade[i]=(int(input(f"{i+1}°,Digite sua idade (APENAS VALORES POSITIVOS!): ")))
    sexo.append(input(f"{i+1}°,Digite seu sexo(APENAS 'F' OU 'M' !): "))
    while((sexo[i]!='F') and (sexo[i]!='M')):
        sexo[i]=(input(f"{i+1}°,Digite seu sexo(APENAS 'F' OU 'M' !): "))
for i in range(0,5,1):
    if(idade[i]>18):
        print(f"{i+1}°Nome:{nome[i]}\n{i+1}°Idade:{idade[i]}\n{i+1}°Sexo:{sexo[i]}\n")
        j=j+1
print("Numero de pessoas maiores que 18 anos: ",j)