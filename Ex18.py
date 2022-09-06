ac= float(input("Aceleração (m/s2): "))

v0= float(input("Velocidade inicial (v0 em m/s): "))

t= float(input("Tempo de percurso(t em s): "))

V = v0 + ac * t

print(f"Velocidade final (km/h): {V:.2f}")

if(V<=40):
    print("Veiculo muito lento.")
elif(40<V<=60):
    print("Velocidade permitida.")
elif(60<V<=80):
    print("Velocidade de cruzeiro.")
elif(80<V<=120):
    print("Veiculo rapido.")
else:
    print("Veiculo muito rapido.")
