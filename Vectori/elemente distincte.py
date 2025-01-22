'''Se citeşte n şi un vector cu n componente numere întregi.
Sǎ se decidǎ dacǎ numerele citite sunt distincte (nu existǎ douǎ valori egale).'''
import utile_vectori as uv
n,v=uv.citeste_f("int")
gasit=0
for i in range(n-1):
    for j in range(i+1,n):
        if v[i]==v[j]:
            gasit=1
            break
    if gasit:break
if gasit:
    print('Numerele nu sunt distincte')
    print("Pozitiile primelor doua valori egale gasite sunt ", i, j)
else:
    print("Numerele sunt distincte")



'''EXERCIȚIU PROPUS. Modificați algoritmul a.î. să fie afișate pozițiile primelor două 
valori egale găsite, dacă acestea există.'''
