str1 = input("Inserisci la prima stringa: ")
str2 = input("Inserisci la seconda stringa: ")

if sorted(str1) == sorted(str2):
    print("Le stringhe sono anagrammi.")
else:
    print("Le stringhe non sono anagrammi.")
