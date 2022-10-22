matriz=[]
 
linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))
for i in range(0, linhas, 1):
    matriz.append([])
for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        nome = input('Digite um nome: ')
        matriz[l].append(nome)

for i in range(0, linhas, 1):
    print(matriz[i])