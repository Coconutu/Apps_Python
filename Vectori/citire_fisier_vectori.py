from os import write

import utile_vectori as uv
n,vector=uv.citeste_f()
print("Valoarea lui n",n)
print("Vectorul este")
uv.afisare(vector)

def scrie_f(v):
    with open("date.out","w") as f:
        for el in v:
            f.write(str(el)+" ")
        f,write("\n")
# add comment