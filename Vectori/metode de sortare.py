# Se citesc n numere întregi. Se cere ca acestea sǎ fie scrise în ordine crescǎtoare (descrescǎtoare).
#Sortarea prin selectarea minimului
import utile_vectori as uv
#citesc datele
n,A=uv.citeste_f("int")
print("Initial");uv.afisare(A)
for i in range(n-1):
    minim=A[i]
    k=i
    for j in range(i+1,n):
        if A[j]<minim:
            minim=A[j]
            k=j
    man=A[k]
    A[k]=A[i]
    A[i]=man
    #sau A[i],A[k]=A[k],A[i], fara a mai fi nevoie de variabila de manevra man
#afisez vectorul sortat
print("Sortat")
uv.afisare(A)

#Sortare descrescatoare
print("Sortare descrescatoare")
n,B=uv.citeste_f("int")
print("Initial");uv.afisare(B)
for i in range(n-1):
    max=B[i]
    k=i
    for j in range(i+1,n):
        if B[j]>max:
            max=B[j]
            k=j
    man=B[k]
    B[k]=B[i]
    B[i]=man
print("Dupa sortare descrescatoare")
uv.afisare(B)



