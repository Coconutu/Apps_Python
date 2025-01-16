with open("date.out","r") as f:
    citire=f.read()
    citire.replace("\n"," ")
lista=list(citire)

numerele=[]
numar=""
for i in lista:
    numar=numar+i
    if i==" ":
        numerele.append(numar)
        numar=""
suma=0
for j in numerele:
    suma=suma+int(j)
print("Suma numerelor din fisierul date.out este",suma)