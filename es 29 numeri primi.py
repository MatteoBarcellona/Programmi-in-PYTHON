num = int(input("Inserisci un numero: "))
Isprime = True

for i in range(2, num):
    if num % i == 0:
        Isprime = False
        break

if Isprime:
    print(num, "è un numero primo.")
else:
    print(num, "non è un numero primo.")

