num = int(input("Inserisci un numero: "));
num2 = int(input("Inserisci un numero2: "));
num3 = int(input("Inserisci un numero2: "));
#faccio 3 confronti.

if num>num2:
  print("il primo numero:",num," è maggiore di numero2:",num2);
else:
  print("il secondo numero2:",num2," è maggiore di numero:",num);


if num3>num2:
  print("il terzo numero:",num3," è maggiore di numero2:",num2);
else:
  print("il secondo numero2:",num2," è maggiore di numero3:",num3);


if num3>num:
  print("il terzo numero:",num3," è maggiore di numero:",num);
else:
  print("il secondo numero2:",num," è maggiore di numero3:",num3);
