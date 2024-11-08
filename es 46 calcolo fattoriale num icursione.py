def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Inserisci un numero: "))
print("Fattoriale di", num, ":", factorial(num))
