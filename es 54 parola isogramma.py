parola = input("Inserisci una parola: ")
isogramma = len(parola) == len(set(parola))
if isogramma:
    print("La parola è un isogramma.")
else:
    print("La parola non è un isogramma.")

