P1= float(input("Nota da P1: "))

P2= float(input("Nota da P2: "))

MEDIA = (P1 + 2*P2) / 3

if(MEDIA >= 5):
    print(f"Sua Media é: {MEDIA:.2f}\nAprovado!")
else:
    print(f"Sua Media é: {MEDIA:.2f}\nReprovado!")