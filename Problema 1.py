'''
Tupluri


c) Găsiți cel mai mare și cel mai mic element dintr-un tuplu de numere întregi.
d) Declarati un tuplu de numere întregi și afișați-l în ordine inversă.'''

# a) Creați un tuplu cu 5 culori preferate și apoi afișați-l.
culori=("rosu","verde","galben","albastru","crem")
print(culori)

# b) Combinați două tupluri conținând numere întregi și afișați rezultatul.
a=(1,2,3,4)
b=(5,6,7,8)
c=a+b
print(c)
print("Maxim",max(c))
print("Minim",min(c))
print(c[::-1])