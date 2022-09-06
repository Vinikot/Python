sts = int(input("Escolha uma opção a seguir:\n1 – Triângulo\n2 – Quadrado\n3 – Retângulo\n4 – Círculo\n5 – Fim de processo (sair do programa)\n"))

if(sts > 5):
    print("Opção invalida, por favor selecione uma opção valida.")
    sts = sts - sts

if(sts == 1):
    o1a = float(input("Base do triangulo:"))
    o1b = float(input("Altura do triangulo:"))
    o1r = (o1a * o1b)/2
    print("Area do triangulo é:",o1r) 
elif(sts == 2):
    o2a = float(input("Aresta do quadrado:"))
    o2r = o2a * o2a
    print("Area do quadrado é:",o2r)  
elif(sts == 3):
    o3a = float(input('Base do retangulo: '))
    o3b = float(input('Altura do retangulo: '))
    o3r = o3a * o3b
    print('Area do retangulo: ',o3r) 
elif(sts == 4):
    o4a = float(input("Digite o raio do circulo:"))
    o4r = 3.14 * (o4a * o4a)
    print("Area do circulo é:",o4r)
elif(sts == 5):
    print("O programa foi encerrado.")
else:
    print("Opção invalida, por favor selecione uma opção valida.")