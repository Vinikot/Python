v1 = int(input('Digite o primeiro valor: '))

v2 = int(input('Digite o segundo valor: '))

v3 = int(input('Digite o terceiro valor: '))

if (v1 > v2) and (v1 > v3):
    print('O primeior valor é o maior')
elif (v2 > v1) and (v2 > v3):
    print('O segundo valor é o maior.')
else:
    print('O terceiro valor é o maior.')