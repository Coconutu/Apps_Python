# Se citeşte un număr natural. Se cere să se decidă dacă este prim sau nu.
# Exemplu. Citim 7, iar acesta este un număr prim. Citim 9. Acesta nu este număr prim!
n=int(input("nr="))
divizor=False
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        divizor=True
if divizor:
    print("Nu e prim!")
else:
    print("E prim!")
    #comment adaugat

