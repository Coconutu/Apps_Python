'''7. Se citeşte un numǎr natural n (citirea se va face într-o variabilǎ de tip int). Sǎ se scrie acest numǎr într-un vector.
Exemplu. Dacǎ citim 1231, vom avea V[1]=1, V[2]=2, V[3]=3, V[4]=1.'''
import utile_vectori as uv
n=int(input("Introduceti numarul n :"))
lungime=len(str(n))
print(lungime)
for i in range(lungime):
    c=n%10 #ultima cifra







