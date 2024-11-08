parola = input("Inserisci una parola: ").replace(" ", "").lower()
if parola == parola[::-1]:
    print("La parola è un palindromo.")
else:
    print("La parola non è un palindromo.")
