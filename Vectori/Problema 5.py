# ...5. Se dau n numere raţionale distincte, reţinute în doi vectori a şi b şi m
# numere raţionale distincte reţinute în vectorii c şi d. Atât cele n numere
# reţinute în vectorii a şi b, cât şi cele m numere reţinute în vectorii
# c şi d sunt sortate crescǎtor. Se cere sǎ se interclaseze cele douǎ şiruri
# de numere.
import utile_vectori as uv
n=int(input("Introduceti numarul de elemente al primului vector"))
a=[]
uv.citire(n,a,"float")
m=int(input("Introduceti numarul de elemente al celui de'al doilea vector"))
b=[]
uv.citire(m,b,"float")
print("Vectorii sunt ")
uv.afisare(a)
uv.afisare(b)
print("Sortare vectori")
a_sortat=sorted(a)
b_sortat=sorted(b)
uv.afisare(a_sortat)
uv.afisare(b_sortat)
interclasat=[]
k=0
lungime_a_sortat=len(a_sortat)
lungime_b_sortat=len(b_sortat)


for i in range(min(lungime_a_sortat,lungime_b_sortat)):
    interclasat.append(a_sortat[i])
    interclasat.append(b_sortat[i])
    k+=1
for l in range(k,max(lungime_a_sortat,lungime_b_sortat)):
    if lungime_a_sortat>lungime_b_sortat:
        interclasat.append(a_sortat[l])
    else:
        interclasat.append(b_sortat[l])

print("Vector interclasat")
uv.afisare(interclasat)