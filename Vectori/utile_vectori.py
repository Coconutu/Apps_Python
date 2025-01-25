def citeste_n():
    n=int(input("Cate elemente are vectorul? "))
    return n
def citire(n,v,tip):
    for i in range(n):
        if tip=="int":
            v.append(int(input("v["+str(i)+"]=")))
        elif tip=="float":
            v.append(float(input("v["+str(i)+"]=")))
        else:
            v.append(input("v[" + str(i) + "]="))

def citeste_f(tip):
    with open("date.in","r") as f:
        n=int(f.readline())
        linie_sir=f.readline().replace("\n"," ")
        linie_lista=linie_sir.split()
        if tip=="int":
            return[n,[int(el) for el in linie_lista]]
        elif tip=="float":
            return[n,[float(el) for el in linie_lista]]
        else:
            return [n, linie_lista]

def afisare(v):
    for el in v:
        print(el,end=" ")
    print()

def scrie_f(v):
    with open("date.out","w") as f:
        for el in v:
            f.write(str(el)+" ")
        f,write("\n")

