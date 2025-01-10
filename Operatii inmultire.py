import random
from random import randint
rez=0
nota=1
for x in range(10):
    a=int(random.randint(4,9))
    b=int(random.randint(4,9))
    rez=a*b
    rasp=int(input(str(a)+"*"+str(b)+"="))
    if rez==rasp:
        print("Corect")
        nota=nota+0.9
    else:
        print("Incorect")
print("Nota este ",round(nota),"/10")