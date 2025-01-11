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
int4=('21.11.2025','Bucuresti','Vasile Ionas','Patrascu George','Rebeca Teodora','Selejan Vasile')
int5=('24.12.2025','Bucuresti','Vasile Ioana','Calinescu George','Selejan Vasile')

locatii={int1[1],int2[1],int3[1]}
print(locatii)