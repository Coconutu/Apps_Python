# 5. Se citeşte un număr natural n. Să se afişeze numărul de cifre din care acesta este format.
# Exemplu: se citeşte 1078, se afişează 4.
n=int(input("n="))
i=0
while n!=0:
    k=n%10
    n=n//10
    i=i+1
print("Numarul are",i, " cifre")
