'''Miniproiect - biblioteca **
Într-o bibliotecă, sunt stocate informații despre cărțile preferate ale diferiților cititori.
Fiecare cititor este reprezentat prin numele său și o listă de cărți preferate.
Creati o structură de date care să stocheze aceste informații și rezolvați următoarele cerințe:

a) Adăugați 5 cititori diferiți în cadrul bibliotecii, împreună cu cărțile lor preferate.
b) Găsiți toate cărțile care sunt citite de cel puțin doi cititori și afișați-le.
c) Determinați câte cărți diferite sunt citite în total de toți cititorii.
d) Găsiți numele cititorului care citește cele mai multe cărți și afișați numărul lor.

Indicații. Realizează pentru fiecare cerință o secvență de cod.
Rezolvarea acestei probleme necesită utilizarea unei combinații de tupluri, seturi și dicționare pentru a
stoca și organiza informațiile despre cititori și cărțile lor preferate. Prin rezolvarea acestui proiect,
vei utilza mai multe concepte diferite și vei putea interconecta diverse structuri de date într-un proiect puțin mai complex.'''
from itertools import count

cititor1=["Vasile Bucataru","Dimineata care nu se va sfarsi","Am fost medic la Auschwitz"]
cititor2=["Morar Emanuel","Dimineata care nu se va sfarsi","Am fost medic la Auschwitz","Veterinarul","Vendetta"]
cititor3=["Morar Petru","Farsa","Renul"]
cititor4=["Morar Rebeca","Farsa","Chiaburii","Vendetta"]
cititor5=["Morar Mirela","Turnul"]
# print(cititor1)
# print(cititor2)
# print(cititor3)
# print(cititor4)
# print(cititor5)
print("Cărțile care sunt citite de cel puțin doi cititori")
total=cititor1+cititor2+cititor3+cititor4+cititor5
ccdc=[]
for e in total:
    if total.count(e)>=2:
        ccdc.append(e)
print(set(ccdc))
numecititor1=cititor1[0]
numecititor2=cititor2[0]
numecititor3=cititor3[0]
numecititor4=cititor4[0]
numecititor5=cititor5[0]
cititor1.remove(numecititor1)
cititor2.remove(numecititor2)
cititor3.remove(numecititor3)
cititor4.remove(numecititor4)
cititor5.remove(numecititor5)
carti=cititor1+cititor2+cititor3+cititor4+cititor5
print('Câte cărți diferite sunt citite în total de toți cititorii')
print(set(carti))
print("Numele cititorului care citește cel mai multe cărți și numărul lor")
dict={numecititor1:len(cititor1),numecititor2:len(cititor2),numecititor3:len(cititor3),numecititor4:len(cititor4),numecititor5:len(cititor5)}
print(max(dict,key=dict.get))
print(max(dict.values()))












