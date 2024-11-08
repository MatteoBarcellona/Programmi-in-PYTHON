numeri = [float(x) for x in input("Inserisci una lista di numeri separati da spazi: ").split()]
n = len(numeri)
mean = sum(numeri) / n
variance = sum((x - mean) ** 2 for x in numeri ) / n
Deviazione = variance ** 0.5

print("Media:", mean)
print("Varianza:", variance)
print("Deviazione Standard:", Deviazione)
