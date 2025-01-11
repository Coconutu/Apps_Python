# Un grup de prieteni dorește să organizeze întâlniri periodice în diverse locații.
# Fiecare întâlnire este reprezentată printr-un tuplu ce conține data, locația și numele participanților.
# Creați o structură de date pentru a gestiona aceste întâlniri și rezolvați următoarele cerințe:

# a) Adăugați 3 întâlniri în structura de date, fiecare cu data, locația și lista de participanți.
# b) Găsiți toate locațiile unice unde s-au organizat întâlniri.
# c) Determinați câți prieteni au participat în total la întâlniri și afișați numărul acestora.
# d) Găsiți toate întâlnirile la care a participat un prieten specific și afișați-le.

# Indicații. Acest mic proiect vă oferă ocazia să vă familiarizați cu modul în care
# puteți utiliza tupluri pentru a reprezenta informațiile despre întâlniri, seturi pentru a găsi
# locațiile unice și dicționare pentru a organiza și accesa participanții la fiecare întâlnire.

int1=('12.01.2025','Oradea','Vasile Ionas','Grigorescu Pavel','Rebeca Antonia','Selejan Aurel')
int2=('11.06.2025','Arad','Saul Petrescu','Grigorescu Pavel','Rebeca Antonia','Stoian Vasile')
int3=('13.10.2025','Bucuresti','Vasile Ionas','Grigorescu George','Rebeca Vaszelena','Selejan Petre')
int4=('21.11.2025','Iasi','Vasile Ionas','Patrascu George','Rebeca Teodora','Selejan Vasile')
int5=('24.12.2025','Galati','Vasile Ionas','Calinescu George','Selejan Vasile')

locatii={int1[1],int2[1],int3[1],int4[1],int5[1]}
print("Locatii unice unde s-au realizat intalnirile:")
print('------------------------------')

for x in locatii:
    print(x)
print('------------------------------')
int1p=int1[2:]
int2p=int2[2:]
int3p=int3[2:]
int4p=int4[2:]
int5p=int5[2:]
total_prieteni=set(int1p+int2p+int3p+int4p+int5p)
print("Numarul de prieteni la intalniri:",len(total_prieteni))
print("Numele prietenilor:")
for x in total_prieteni:
    print(x)
print('------------------------------')
prieten=input("Introduceti numele prietenului pentru a afla intalnirile unde a participat:")
if prieten in int1:
    print(int1[1])
if prieten in int2:
    print(int2[1])
if prieten in int3:
    print(int3[1])
if prieten in int4:
    print(int4[1])
if prieten in int5:
    print(int5[1])


