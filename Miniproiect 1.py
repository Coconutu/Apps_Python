# Miniproiect. Citiți o listă de la tastatură care reține numere reale,
# până este întâlnită cifra 0.
# Afișați "un raport" care să conțină: numărul de elemente, câte sunt pozitive, câte sunt negative și suma elementelor!
lista=[]
n=1
while n!=0:
    n=float(input("Introduceti n"))
    lista.append(n)
lista.pop()
# print(lista)
print("Numarul de elemente in lista ",len(lista))
p=0
n=0
for i in lista:
    if i>0:
        p=p+1
    else:
        n=n+1
print("Numere pozitive:",p)
print("Numere negative:",n)
print("Suma elementelor din lista",sum(lista))