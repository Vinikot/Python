v1 = float(input("Digite o Lado(A): "))

v2 = float(input("Digite o Lado(B): "))

v3 = float(input("Digite o Lado(C): "))

if ((v1 * v1 == v2 * v2 + v3 * v3) or (v2 * v2 == v1 * v1 + v3 * v3) or (v3 * v3 == v2 * v2 + v1 * v1)):
    print("Os lados formam um Triângulo Retângulo.")
else:
    print("Os lados não formam um Triângulo Retângulo.")

