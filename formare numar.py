# 4. Se citesc, în ordine, cele n cifre ale unui număr natural.
# Se cere să se construiască şi să se afişeze numărul format.
# Exemplu: se citesc 6, 7, 3. Se va afişa 673.
n=int(input("Cate cifre are numarul ?")) #n=5
numar=0
for i in range(1,n+1):
    k=int(input("Cifra "+str(i)+" = "))
    numar=numar+k*10**(n-i)
print(numar)


