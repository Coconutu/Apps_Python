'''6. Se citeşte un vector cu n componente numere naturale. Sǎ se aranjeze
numerele în vector astfel încât cele pare sǎ ocupe primele poziţii.
Exemplu. Dacǎ n=4 şi se citeşte 1 2 7 8, o soluţie este 2 8 1 7.'''
import utile_vectori as uv
n=uv.citeste_n()
v=[]
w=[]
uv.citire(n,v,"int")
for i in v:
    if i%2==0:
        w.append(i)
for i in v:
    if i%2!=0:
        w.append(i)
print("Vectorul sortat este:")
uv.afisare(w)

