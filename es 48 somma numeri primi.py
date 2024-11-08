def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

total = sum(num for num in range(1, 41) if isprime(num))
print("Somma dei numeri primi da 1 a 40:", total)
