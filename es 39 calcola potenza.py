base = int(input("Inserisci la base: "))
esponente = int(input("Inserisci l'esponente: "))
resulto = 1

for _ in range(esponente):
    resulto *= base

print("Risultato:", resulto)


