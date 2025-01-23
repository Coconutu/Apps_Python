'''2. Se citeşte un vector cu n componente numere întregi. Care este cea mai
mare sumǎ care se poate forma cu ele?
Exemplu: dacǎ n=4, iar numerele citite sunt -1 3 2 -7, se afişeazǎ 5.'''
import utile_vectori as uv
n=int(input("Introduceti cate elemente are vectorul :"))
v=[]
uv.citire(n,v,"int")
uv.afisare(v)
max=0
for i in range(0,n-1):
    for j in range (i+1,n):
        if v[i]+v[j]>max:
            max=v[i]+v[j]
print(max)
