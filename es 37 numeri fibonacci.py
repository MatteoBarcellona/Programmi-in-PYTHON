fib= [0, 1]
for _ in range(30):
    fib.append(fib[-1] + fib[-2])
print("Primi 30 numeri di Fibonacci:", fib)