import utile_vectori as uv
with open("date.in","r") as f:
    n=int(f.readline())
    linie_sir=f.readline().replace("\n"," ")
    linie_lista=linie_sir.split()
    vector=[int(el) for el in linie_lista]
    print('Valoarea lui n=',n)
    print("Vectorul este")
    uv.afisare(vector)
lista="1 2 3 4 5 6"
print(lista)
lista_splituita=lista.split()
print(lista_splituita)
vector=[int(ek) for ek in lista_splituita]
uv.afisare(vector)