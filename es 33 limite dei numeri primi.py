limite = int(input("Inserisci un limite di nuemri primi: "))
prime = []

for num in range(2, limite + 1):
    isprime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isprime = False
            break
    if isprime:
        prime.append(num)

print("Numeri primi fino a", limite, ":", prime)
