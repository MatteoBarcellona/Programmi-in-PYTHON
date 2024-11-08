word = input("Inserisci una parola: ")
vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Numero di vocali nella parola:", count)
