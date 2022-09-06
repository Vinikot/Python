sts = int(input("Escolha uma opção a seguir:\n1 – Multiplicação\n2 – Adição\n3 – Divisão\n4 – Subtração\n5 – Fim de processo (sair do programa)\n"))

if(sts == 1):
    o1a = float(input("Digite um valor(A):"))
    o1b = float(input("Digite um valor(B):"))
    o1r = o1a * o1b
    print("O resultado é:",o1r)
elif(sts == 2):
    o2a = float(input("Digite um valor(A):"))
    o2b = float(input("Digite um valor(B):"))
    o2r = o2a + o2b
    print("O resultado é:",o2r)
elif(sts == 3):
    o3a = float(input("Digite um valor(A):"))
    o3b = float(input("Digite um valor(B):"))
    o3r = o3a / o3b
    print("O resultado é:",o3r)
elif(sts == 4):
    o4a = float(input("Digite um valor(A):"))
    o4b = float(input("Digite um valor(B):"))
    o4r = o4a - o4b
    print("O resultado é:",o4r)
elif(sts == 5):
    print("O programa foi encerrado.")
else:
    print("Opção invalida, por favor selecione uma opção valida.")