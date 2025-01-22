'''1. Se citeşte un vector cu n componente, numere naturale. Sǎ se afişeze
cel mai mare numǎr raţional subunitar în care numǎrǎtorul şi numitorul fac
parte din mulţimea valorilor citite.

Exemplu: dacǎ am citit valorile 1 2 3 se afişeazǎ 2/3.'''
#citim n
n=int(input("Numarul de componente ale vectorului. n="))
#citim vectorul
v=[]
for i in range (n):
    c=int(input("v["+str(i)+"]="))
    v.append(c)
numitor=max(v)
index=0
i=0
for i in range(n):
    if numitor==v[i]:
        break

# print("Numitor",numitor)
v.pop(i)
numarator=max(v)
# print("Numarator=",numarator)
print("Numarul rational:",numarator,"/",numitor)













