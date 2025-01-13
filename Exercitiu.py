# # Creați câte o funcție care citește o listă cu elemente de tip int, apoi float.
# # De asemenea, realizați o funcție care citește un dicționar!
# def creare_lista_int(n):
#     lista_int = []
#     for i in range(n):
#         x = int(input('Elementul ' + str(i) + ":"))
#         lista_int.append(x)
#     return lista_int
#
#
# def creare_lista_float(n):
#     lista_float = []
#     for i in range(n):
#         x = float(input('Elementul ' + str(i) + ":"))
#         lista_float.append(x)
#     return lista_float
#
#
# def afisare_lista(l):
#     x = 0
#     for i in l:
#         print("Elementul ", x, ":", i)
#         x = x + 1
#
#
# a = int(input("Cate elemente sa aibe listele int si float?"))
# print("creare lista int")
# lista_de_int = creare_lista_int(a)
# afisare_lista(lista_de_int)
# print("creare lista float")
# lista_de_float = creare_lista_float(a)
# afisare_lista(lista_de_float)
#
#
# def ad3(a=0, b=0, c=0, tip='str'):
#     if tip == 'str':
#         return str(a) + str(b) + str(c)
#     elif tip == 'int':
#         return int(a) + int(b) + int(c)
#     elif tip == 'float':
#         return float(a) + float(b) + float(c)
#     elif tip == 'list':
#         l = list[a, b, c]
#         return l
#     return a + b + c
#
#
# print("Introduceti numerele a,b,c pentru a efectua operatia ad3")
# x, y, z = input(), input(), input()
# print(ad3(x, y, z))
# print(ad3(x, y, z, 'int'))
# print(ad3(x, y, z, 'float'))
# print(ad3(x, y, z, 'list'))


# Argumente arbitrare
# În cazul în care nu cunoaștem numărul de argumente trimise unei funcții,
# adăugăm un asterix "*" înaintea numelui parametrului:
# def arbitrar(*masina):
#     print(masina)
# arbitrar('Honda', 'Audi', 'BMW', 'Dacia')
# arbitrar('Ford', 'Lancia', 'Lada')

# Argumente cuvinte cheie (keywords)
# Se poate întâmpla să nu cunoaștem ordinea în care trimitem argumentele către o anumită funcție.
# Putem folosi ca parametri asocieri de cuvinte cheie - valoare pentru a apela funcția respectivă, precum în exemplul
# de mai jos:
def functia_mea(c,b,a):
    print(c,b,a)
functia_mea(a=1,b=2,c=4)

#exemplu de argumente arbitrare keywords
def functia_mea(**x):
    print(x['unu'],x['doi'],x['trei'])
functia_mea(trei='a',doi='b',unu='c')

# În cadrul codului nostru, putem avea nevoie câteodată de anumite mici funcții fără nume, cu unul sau mai mulți parametri,
# iar corpul să conțină o unică expresie – ceva rapid și ușor! Forma generală este
medie=lambda x,y:(x+y)/2
print(medie(4,6))
print( (lambda x,y : (x+y)/2)(100,200) )
print( (lambda x,y : (x+y)/2)(100,200))
suma=lambda a,b: a+b
print(suma(10,20))