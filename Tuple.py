# pers1 = ("Mihai", "Stamate", 26, 1.82, "Oradea", "Bihor")
# pers2 = ("Dana", "Petrișor", 22, 1.64, "Viscri", "Brasov")
# print(pers1[0:2])
# print(pers1[3])
# print(pers1[3:])
# print(pers1[-1], pers1[-2])
# print(pers1[::-1])
# print(len(pers1))
# print("Dan" in pers2)
# print("Dana" in pers2)
# print("Petrișor" not in pers2)
# t1 = (1,2,3)
# t2 = (4,5)
# print(t1+t2)
# print((t1+t2)*2)

# tuplu = (1,2,3,4,5,2,3)
# print("3 apare de", tuplu.count(3), "ori.")
# print("Indexul lui 5 este", tuplu.index(5))
# print("Valoarea minimă este", min(tuplu))
# print("Valoarea maximă este", max(tuplu))
# print("Valorile sortate ca listă:", sorted(tuplu))
# print("Suma elementelor este:", sum(tuplu))

pers1 = ("Dan", "Grigorescu", 26, 1.79, "Oradea", "Bihor")
#am greșit vârsta, trebuie reținut 25
#P1. Creăm o listă ce conține elementele tuplului
lista=list(pers1)
#P2. Listele pot fi modificate, deci...
lista[2]=25
#P3. Rețin în pers1 elementele listei ca tuplu
pers1=tuple(lista)
print(pers1)

