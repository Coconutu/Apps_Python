# Creați câte o funcție care citește o listă cu elemente de tip int, apoi float.
# De asemenea, realizați o funcție care citește un dicționar!
def creare_lista_int(n):
    lista_int=[]
    for i in range(n):
        x=int(input('Elementul'+str(i)+":"))
        lista_int.append(x)
    return lista_int

def creare_lista_float(n):
    lista_float=[]
    for i in range(n):
        x=float(input('Elementul'+str(i)+":"))
        lista_float.append(x)
    return lista_float

a=int(input("Cate elemente sa aibe listele int si float?"))
print("creare lista int")
print(creare_lista_int(a))
print("creare lista float")
print(creare_lista_float(a))