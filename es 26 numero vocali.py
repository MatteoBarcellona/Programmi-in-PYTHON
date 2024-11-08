stringa = input("Inserisci una stringa: ")
vocali = "aeiouAEIOU"
numVocali = len([carattere for carattere in stringa if carattere in vocali])
print("Il numero di vocali nella stringa è:", numVocali)
