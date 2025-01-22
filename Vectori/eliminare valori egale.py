#metoda naiva
import utile_vectori as uv
#citesc datele din fisierul date.in
n,v=uv.citeste_f("int")
vd=[]
#algoritmul
for i in v:
    if i not in vd:
        vd.append(i)
#afisez datele
uv.afisare(v)
uv.afisare(vd)

# Varianta 2. Metoda „list comprehension”
import utile_vectori as uv
#citesc datele din fisierul date.in
n,v=uv.citeste_f("int")
vd=[]
#pur si simplu
[vd.append(i) for i in v if i not in vd]
#afisez datele
uv.afisare(v)
uv.afisare(vd)

#Varianta 3. Folosim seturile de date
import utile_vectori as uv
#citesc datele din fisierul date.in
n,v=uv.citeste_f("int")
vd=list(set(v))
uv.afisare(v)
uv.afisare(vd)