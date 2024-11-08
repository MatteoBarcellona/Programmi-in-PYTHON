num = int(input("Inserisci un numero: "))
fattoriale = 1
for i in range(1, num + 1):
    fattoriale *= i
print("Il fattoriale di", num, "è:", fattoriale);