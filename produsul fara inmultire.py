# Se citesc numerele naturale n1 şi n2. Să se calculeze produsul lor, fără a utiliza operatorul de înmulţire.
n1=int(input("n1="))
n2=int(input("n2="))
x=1
s=0
while x<=n2:
    s=s+n1
    x=x+1
print("produsul numerelor",n1," si ",n2, " este ",s)