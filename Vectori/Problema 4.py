'''4. Se citesc un numǎr natural n şi doi vectori a şi b cu n componente
numere întregi. Se cere sǎ se calculeze suma:
S=a1/b1+a2/b2+...an/bn'''
import utile_vectori as uv
a=[];b=[]
n=int(input("Numarul de elemente"))
uv.citire(n,a,"int")
uv.citire(n,b,"int")
s=0
vector=[]
for i in range(0,n):
    s=s+a[i]/b[i]
    vector.append(str(a[i])+"/"+str(b[i]))
print("Suma ",end=" ")
uv.afisare(vector)
print("este ",s)