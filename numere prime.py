# 3. Tipăriţi toate numerele prime aflate între două numere naturale citite.
a=int(input("a="))
b=int(input("b="))
def esteprim(numar):
    for i in range(2,int(numar**0.5)+1):
        if numar%i==0:
            return False
    return True
for x in range(a,b+1):
    if esteprim(x):
        print(x)
