from asyncio.windows_events import NULL


rm=[]
nome=[]
curso=[]
for i in range(0,5,1):
    rm.append(input("Digite o RM do aluno: "))
    while(rm[i]==("")):
        rm[i]=input("Digite o RM do aluno: ")
    nome.append(input("Digite o NOME do aluno: "))
    while(nome[i]==("")):
        nome[i]=input("Digite o NOME do aluno: ")
    r=input("O aluno esta matriculado em um curso?(APENAS 's' ou 'n'): ")
    if(r=='s'):
        curso.append(input("Digite o nome do CURSO: "))
    elif(r=='n'):
        curso.append("O aluno não esta matriculado em um curso.")
for i in range(0,5,1):
    print("RM DO ALUNO: "+rm[i]+"  --  NOME DO ALUNO: "+nome[i]+"  --  CURSO DO ALUNO: "+curso[i])