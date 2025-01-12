# masini = ["Audi","BMW","Ford","Opel","Ferrari"]
# #tiparesc lista
# print(masini)
# #unele elemente apoi
# print(masini[0])
# print(masini[2])
# #ultimul element
# print(masini[len(masini)-1])
# #tipul de date
# print(type(masini))
# lista1 = ["a","b","c",1,2,3.14]
# #afisez toata lista
# print(lista1)
# #afisez primele 3 elemente
# print(lista1[0:3])
# #de la 3 spre dreapta
# print(lista1[3:])
# print(lista1[4:])
# #ultimul element
# print(lista1[-1])
# #lista inversa...
# print(lista1[::-1])
# lista1=["a","b","g"]
# lista2=["c","d"]
# lista3=["e","f"]
# lista4=lista1+lista2+lista3
# print(lista4)
# print(lista1*3)
# lista5=lista1*2+lista2
# print(lista5)
# print("a" in lista1)
# print("a" in lista2)
# print("a" in lista3)
# lista1[1]="g"
# print(lista1)
# lista1.remove("g") #sterge primul element cu valoarea gdin lista
# print(lista1)
# del lista1[1]
# print(lista1)
# # del lista1
# print(lista1)
# # Metoda pop(indice_optional) șterge și întoarce ultimul element din listă ca rezultat,
# # ori pe cel trimis ca argument prin indice_optional:
# lista6=["a","b","g","h","i"]
# print(lista6)
#
# lista6.pop()
# print(lista6)
# lista6.pop()
# lista6.append("i")
# print(lista6)
# lista6.insert(0,"k")
# print(lista6)
# lista7=[0,1]
# lista6.append(lista7)
# print(lista6)
# lista1 = [1, 2, 3, 4, 5, 2, 3]
# print(lista1)
# #funcția sum calculează suma elementelor
# print(sum(lista1))
# #funcția sum cu valoare inițială
# print(sum(lista1,7))
# #funcțiile min() și max()
# print(min(lista1),max(lista1))
# #metoda count()
# print(lista1.count(2))
# lista1.sort()
# print(lista1)
# lista1.sort(reverse=True)
# print(lista1)

prenume = ['Mihai','George','Ana','Dan','Ion','Geta','Vio']
varsta = [14, 23, 15, 14, 12, 41, 39]
# a) Cosiderând că fiecare persoană are asociată vârsta pe același indice, afișați precum mai jos:
# #
# # Mihai are varsta de 14 ani.
# # George are varsta de 23 de ani.
print(prenume[0]," are varsta de ",varsta[0]," ani.")
print(prenume[1]," are varsta de ",varsta[1]," ani.")
# b) Adăugați în liste la final, corespunzător, datele: Andreea, 34 și Ioan, 23.
# Tipăriți ambele liste apoi.
prenume.append("Andreea")
varsta.append(34)
prenume.append("Ioan")
varsta.append(23)
print(prenume)
print(varsta)
# c) Ștergeți datele din ambele liste despre Ana (atenție la indici).
del prenume[2]
del varsta[2]
print(prenume)
print(varsta)
# d) Afișați primele trei elemente din lista prenume.
print(prenume[0:3])
# e) Afișați lista prenume de la dreapta la stânga.
print(prenume[::-1])
# f) Tipăriți elementele cu indicii 2 și 4, apoi de la 0 la 5 din ambele liste.
print(prenume[2])
print(prenume[4])
print(prenume[0:5])
print(varsta[2])
print(varsta[4])
print(varsta[0:5])
lista5 = [8,7,9,10,6,5,4]
print(sum(lista5))
print(59//2)