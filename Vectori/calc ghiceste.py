'''Scrieţi un subprogram recursiv prin care calculatorul ghiceşte un număr
natural ascuns de dumneavoastră (numărul este cuprins între 1
şi 30000). Atunci când calculatorul propune un număr i, se va
răspunde prin:
1, dacă numărul este prea mare;
2, dacă numărul este prea mic;
0, dacă numărul a fost ghicit.'''
#recursiv
import random
a=0
b=100
def genereaza_int(a,b):
    n=random.randint(a,b)
    return n

def ghiceste(a,b):
    print("Apasati 1 daca numarul este prea mare, 2 daca este prea mic si 0 daca este cel la care v-ati gandit!")

    i=genereaza_int(a,b)
    print("Numarul este ",i," ?")
    n=int(input())
    if n==0:
        ghicit=True
        print("Felicitari !")
    elif n==2:
        a=i+1
        ghiceste(a,b)
    elif n==1:
        b=i-1
        ghiceste(a,b)
    else:
        print("Apasati 1 daca numarul este prea mare, 2 daca este prea mic si 0 daca este cel la care v-ati gandit!")
print("Gandeste-te la un numar intre 1 si 100. Eu voi incerca sa il nimeresc")
ghiceste(1,100)

