# Se citesc două numere întregi m şi n. Se cere să se tipărească cel mai mare divizor comun (cmmdc)
# şi cel mai mic multiplu comun (cmmmc) al celor două numere.

m = int(input("m="))
n = int(input("n="))
#rețin valorile initiale
init_m = m
init_n = n
#calculez cmmdc
while m!=n:
    if m>n: m = m - n
    else: n = n - m
#m va reține cmmdc
print("cmmdc =",m)
#calculez cmmmc
cmmmc = init_m*init_n // m
print("cmmmc =",cmmmc)
