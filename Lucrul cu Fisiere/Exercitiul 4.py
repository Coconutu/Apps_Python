lista=[]
with open("date.out","r") as f:
    lista=f.read()
LISTA=[]
print(lista)
for i in lista:
    j=i.upper()
    LISTA.append(j)

with open("date2.out",'w') as g:
    for i in LISTA:
        g.write(i)

with open("date2.out","r") as f:
    lista1=f.read()
print(lista1)

