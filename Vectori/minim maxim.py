import utile_vectori as uv
#preiau datele din fisierul text date.in
n,v=uv.citeste_f("int")
#implementez algoritmul
maxim=v[0]
for i in v:
    if i>maxim:maxim=i
uv.afisare(v)
print("Maximul vectorului este",maxim)
#putem face si in alt mod
minim=v[0]
indice=0
for i in range(n):
    if v[i]<minim:
        minim=v[i]
        indice=i
print("Minimul este ",v[indice]," cu indicele", indice)
#sau putem utiliza functiile pythom
print("Maximul vectorului este ",max(v))
print("Minimul vectorului este ",min(v))

n,v=uv.citeste_f("int")
print(min(el for el in v if el<0))
print(min(el for el in v if el>0))