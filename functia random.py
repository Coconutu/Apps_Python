import random
for i in range(4):
    print(random.random())
for i in range(4):
    print(round(20+random.random()*10)) #numere aleatorii intre 20 si 30
for i in range(4):
    print(random.randint(-100,100))
lista=['a','b','c','d','e']
for i in range(4):
    print(random.choice(lista))
random.seed(17) #pornim generatorul de la aceeași valoare, numerele vor fi aceleasi
for i in range(4):
    print(random.randint(-10,10)) #numerele vor fi tot timpul 6,3,-1,1
