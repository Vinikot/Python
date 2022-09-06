alt = float(input('Digite a sua altura em (m): '))
 
peso = float(input('Digite o seu peso (em Kg): '))

sexo = input("Sexo: M ou F : ")

while ( (sexo != 'M') and (sexo != 'F') ):
    print("Opção Invalida. Escolha 'M'(masculino) ou 'F'(feminino).")
    sexo = input("Sexo: M ou F : ")
 
imc = peso / (alt * alt)
 
if (sexo == 'M'):
    if imc < 20:
        print("Abaixo do peso!")
    elif imc < 25:
        print("Peso ideal!")
    else:
        print("Acima do peso!")
else:
    if imc < 19:
        print("Abaixo do peso!")
    elif imc < 24:
        print("Peso ideal!")
    else:
        print("Acima do peso!")
