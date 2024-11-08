num1 = int(input("Inserisci il primo numero: "));
num2 = int(input("Inserisci il secondo numero: "));
calcolatrice = input("Inserisci operazione della calcolatrice fra +, -, *, /: ");

if calcolatrice == "+":
    print(num1 + num2);
elif calcolatrice == "-":
    print(num1 - num2);
elif calcolatrice == "*":
    print(num1 * num2);
elif calcolatrice == "/":
    print(num1 / num2);
else:
    print("non valido");
