stringa = input("Inserisci una stringa: ")
numlettere = len([carattere for carattere in stringa if carattere.isalpha()])
print("Il numero di lettere nella stringa è:", numlettere)