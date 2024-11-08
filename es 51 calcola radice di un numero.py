def square_root(n):
    approx = n / 2.0
    while True:
        better = (approx + n / approx) / 2
        if abs(approx - better) < 0.0001:
            return better
        approx = better

num = float(input("Inserisci un numero: "))
result = square_root(num)
print("Radice quadrata:", result)
