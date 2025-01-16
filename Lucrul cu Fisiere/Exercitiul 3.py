#Se citesc n linii de la tastatura. Sa se creeze un program care sa le retina intr-un fisier text
n=int(input("Numarul de linii="))
print("------------------------")
open("date.out","w").close()
with open("date.out",'a') as f:
    for i in range(n):
        linie=input()
        f.write(linie+"\n")
print("________________________")
print("Super, fisierul a fost creat")
print("Continutul ascestuia este:")
print("________________________")
with open('date.out',"r") as f:
    print(f.read())