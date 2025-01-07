# Se citeşte un număr natural n. Să se tipărească numărul obţinut prin inversarea poziţiilor cifrelor pe care le ocupă numărul citit.
# Exemplu. Dacă citim n=248, se va tipări 842.
n=int(input("n="))
inv=0
while n!=0:
    inv=inv*10+n%10
    n=n//10
print("Inversul este ",inv)