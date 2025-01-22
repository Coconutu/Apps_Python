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