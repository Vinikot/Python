r=''
while(r!='n'):
    matriz=[]
    r=''
    a=True
    linhas=0
    while((linhas<1)or(linhas>10)):
        linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
    colunas=0
    while((colunas<1)or(colunas>10)):
        colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))
    for i in range(0, linhas, 1):
        matriz.append([])
    for l in range(0, linhas, 1):
        for c in range(0, colunas, 1):    
            num = int(input('Digite um numero: '))
            matriz[l].append(num)
    x=int(input("Digite um valor: "))
    for l in range(0, linhas, 1):
        for c in range(0, colunas, 1):
            if(matriz[l][c]==x):
                print("O valor digitado se encontra na:\nLinha: ",l,"\nColuna: ",c)
                a=False
    if(a):
        print("Numero não encontardo!")
    while((r!='n')and(r!='s')):
        r=input("Dejesa uma nova consulta? (APENAS 's' ou 'n'): ")