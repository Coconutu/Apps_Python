'''3. Se citeşte un vector cu n componente numere naturale. Se cere sǎ se
obţinǎ toate permutǎrile circulare la dreapta.
Exemplu: dacǎ n=4, şi vectorul este 1 2 3 4, permutǎrile circulare sunt:
1 2 3 4
4 1 2 3
3 4 1 2
2 3 4 1
Observaţi faptul cǎ, de fiecare datǎ, ultimul element trece pe prima
poziţie, iar restul elementelor sunt deplasate la dreapta cu o poziţie.'''
import utile_vectori as uv
n=int(input("Introduceti numarul de elemente"))
v=[]
uv.citire(n,v,"int")
print("Vectorul este:",end=" ");uv.afisare(v)
print("Permutari circulare :")
for i in range(1,n):
    for j in range(0,n-1):
        v[j],v[j+1]=v[j+1],v[j]
    uv.afisare(v)






uv.afisare(v)




