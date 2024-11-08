n = int(input("Inserisci il numero di elementi di Fibonacci da visualizzare: "))
fibonacci = [0, 1]

while len(fibonacci) < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("Sequenza di Fibonacci con", n, "elementi:", fibonacci)

