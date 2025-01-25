'''7. Se citeşte un numǎr natural n (citirea se va face într-o variabilǎ de tip int). Sǎ se scrie acest numǎr într-un vector.
Exemplu. Dacǎ citim 1231, vom avea V[1]=1, V[2]=2, V[3]=3, V[4]=1.'''

n=int(input("Introduceti numarul n :"))
lungime=len(str(n))
vector=[]
for i in range(0,lungime):
    c=int(n%10) #ultima cifra
    n=n/10
    vector.append(c)
vector.reverse()
print(vector)













