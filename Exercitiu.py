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
def afisare_lista(l):
    x=0
    for i in l:
        print("Elementul ",x,":",i)
        x=x+1

a=int(input("Cate elemente sa aibe listele int si float?"))
print("creare lista int")
lista_de_int=creare_lista_int(a)
afisare_lista(lista_de_int)
print("creare lista float")
lista_de_float=creare_lista_float(a)
afisare_lista(lista_de_float)

def ad3(a,b,c,tip):
    if tip=='str':
        return str(a)+str(b)+str(c)
    elif tip=='int':
        return int(a)+int(b)+int(c)
    elif tip=='float':
        return float(a)+float(b)+float(c)
    return a+b+c
print("Introduceti numerele a,b,c pentru a efectua operatia ad3")
x,y,z=input(),input(),input()
print(ad3(x,y,z,'str'))
print(ad3(x,y,z,'int'))
print(ad3(x,y,z,'float'))
