'''11. Se citeşte un tablou cu n linii şi n coloane, numere întregi. Un astfel de
tablou, în care numǎrul liniilor coincide cu numǎrul coloanelor, se numeşte
tablou pǎtratic.
a) Pentru un tablou pǎtratic A, numim diagonalǎ principalǎ,
elementele aflate pe "linia" care uneşte A[1,1], A[n,n].
Exemplu: pentru tabloul alǎturat, elementele sunt: 1, 5 şi 9.
Se cere:
a1) suma elementelor aflate pe diagonala principalǎ;
a2) suma elementelor aflate deasupra diagonalei principale;
a3) suma elementelor aflate sub diagonala principalǎ.
b) Pentru un tablou pǎtratic A, numim diagonalǎ secundarǎ,
elementele aflate pe "linia" care uneşte A[n][1], A[1][n].
Exemplu: pentru tabloul alǎturat, elementele sunt: 7, 5 şi 3.
Se cere:
b1) suma elementelor aflate pe diagonala secundarǎ;
b2) suma elementelor aflate deasupra diagonalei secundare;
b3) suma elementelor aflate sub diagonala secundarǎ.
Cerinţe suplimentare
1. Pentru fiecare cerinţǎ se va face un program separat.
2. În nici un program nu se va folosi instrucţiunea if.'''
import numpy as np
n=int(input("Cate linii/coloane are matricea ?"))
matrice=[]
linie=[]
for i in range (n):
    print("Linia ",i+1)
    for i in range(n):
        linie.append(int(input("E["+str(i)+"]=")))
    matrice.append(linie)
    linie=[]

m=np.asmatrix(matrice)
print(m)
print("Suma elementelor aflate pe diagonala principala")
suma=0
for i in range(n):
    suma=suma+m[i,i]
print(suma)

print("Suma elementelor aflate deasupra diagonalei principale")
suma=0
for i in range(0,n-1):
    suma=suma+m[i,i+1]
print(suma)