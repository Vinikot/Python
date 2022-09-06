import string


alt = float(input('Digite a sua altura em (m): '))
 
peso = float(input('Digite o seu peso (em Kg): '))

sexo = string(input("Sexo - F ou M ?: "))
vsexo = string("M" or "F")
while sexo != vsexo:
    sexo = string(input("Sexo- F ou M ?: "))
 
imc = peso / (alt * alt)
 
if imc < 20:
    print("Abaixo do peso!")
elif imc < 25:
    print("Peso ideal!")
else:
    print("Acima do peso!")