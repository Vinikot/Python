matriz=[]
matriz2=[]
linhas = int(input('Digite a quantidade de linhas que a matriz terá: '))
colunas = int(input('Digite a quantidade de colunas que a matriz terá: '))
for i in range(0, linhas, 1):
    matriz.append([])
    matriz2.append([])
for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):    
        num = int(input('Digite um numero: '))
        matriz[l].append(num)
        matriz2[l].append(0)
const=int(input("Digite um valor para a constante: "))
for l in range(0, linhas, 1):
    for c in range(0, colunas, 1):
        matriz2[l][c]=matriz[l][c]*const
print("\nMATRIX 1:")
for i in range(0, linhas, 1):
    print(matriz[i])
print("\nMATRIX 2:")
for i in range(0, linhas, 1):
    print(matriz2[i])