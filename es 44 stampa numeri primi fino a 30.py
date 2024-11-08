prime = []
for num in range(2, 31):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)

print("Numeri primi da 2 a 30:", prime)