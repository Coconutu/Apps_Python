# 1. Ionel a depus la bancă suma de S lei. Dobânda este p% pe lună.
# Ce sumă are Ionel după k luni? Programul va citi S, p, k şi va afişa suma cerută.
S=float(input("Suma depusa : "))
p=float(input("Dobanda : "))
k=int(input("Luni : "))
for j in range(1,k+1):
    S=S+S*(p/100)
print("Suma dupa ",k," luni :",int(S))