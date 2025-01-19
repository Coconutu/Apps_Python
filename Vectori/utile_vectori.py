def citire(n,v,tip):
    for i in range(n):
        if tip=="int":
            v.append(int(input("v["+str(i)+"]=")))
        elif tip=="float":
            v.append(float(input("v["+str(i)+"]=")))
        else:
            v.append(input("v[" + str(i) + "]="))
def afisare(v):
    for el in v:
        print(el,end=" ")
    print()