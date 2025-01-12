def subp(n):
    s=0
    for i in range(n):
        s=s+1/(i+1)
    return s
# n=int(input("Introduceti n"))
# print(subp(n))

def creare_lista(dim):
    lista_locala=[]
    for i in range(dim):
        element=input("Element "+str(i)+":")
        lista_locala.append(element)
    return lista_locala
n=int(input("De cate elemente sa fie lista"))
print(creare_lista(n))