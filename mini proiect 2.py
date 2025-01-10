# Miniproiect. Realizați un program care oferă utilizatorului posibilitatea să aleagă operația
# – adunare, scădere ori înmulțire (mai exact, un mic meniu). În funcție de valoarea introdusă,
# afișați un test format din zece întrebări.
import random
nota=1
print("Introduceti cifra corespunzatoare operatiei dorite")
print("Adunare   - 1")
print("Scadere   - 2")
print("Inmultire - 3")

c=int(input())
for i in range(10):
    n=random.randint(2,10)
    m=random.randint(2,10)
    if c==1:
        rez=n+m
        operator="+"
    elif c==2:
        rez=n-m
        operator="-"
    elif c==3:
        rez=n*m
        operator="*"
    else:
        print("Operatie inexistenta. Alegeti 1,2 sau 3!")
    k=int(input(str(n)+operator+str(m)+"="))
    if k==rez:
        print("Corect")
        nota=nota+0.9
    else:
        print("Incorect")
print("Nota dvs. este",round(nota))

