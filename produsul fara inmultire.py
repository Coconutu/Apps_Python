# Se citesc numerele naturale n1 şi n2. Să se calculeze produsul lor, fără a utiliza operatorul de înmulţire.
# n1=int(input("n1="))
# n2=int(input("n2="))
# x=1
# s=0
# while x<=n2:
#     s=s+n1
#     x=x+1
# print("produsul numerelor",n1," si ",n2, " este ",s)

# 1. Rezolvați problema de mai sus folosind instrucțiunea for.

# n1=int(input("n1="))
# n2=int(input("n2="))
# s=0
# for x in range(1,n2+1):
#     s=s+n1
#     x=x+1
# print("produsul numerelor",n1," si ",n2, " este ",s)


# 2. Se citesc două numere naturale n1 şi n2. Se cere să se calculeze câtul şi restul împărţirii întregi
# ale celor două numere, fără a utiliza operatori de împărţire. Indicație. Aşa cum înmulţirea se poate face
# prin adunare repetată, tot aşa împărţirea se poate face prin scădere repetată...
deimpartit=int(input("Deimpartit="))
d=deimpartit
impartitor=int(input("Impartitor="))
cat=0
while(deimpartit>=impartitor):
    deimpartit=deimpartit-impartitor
    cat=cat+1

print("catul numerelor",d," si ",impartitor, " este ",cat," rest ",deimpartit)