# Se citesc n numere întregi. Se cere ca acestea sǎ fie scrise în ordine crescǎtoare (descrescǎtoare).
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
#afisez vectorul sortat
print("Sortat")
uv.afisare(A)

