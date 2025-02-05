import math
l=float(input("latura mica (m): "))
L=float(input("latura mare (m): "))
p=float(input("Inaltime plinta (cm): "))
c=float(input("Cati mp are o cutie (mp)?"))
pc=float(input("Pretul unei cutii de gresie (ron)"))
pm=float(input("Pret montaj/mp (ron)"))
arie=math.ceil(l*L)
perimetru=math.ceil(2*(L+l))
necesar_nerotunjit=arie+(p/10)*perimetru+1
necesar=math.ceil(necesar_nerotunjit)
print("Necesar brut ",necesar_nerotunjit,"mp",sep="")
print("Necesar : ",necesar,"mp",sep="")
print("Trebuie sa cuperi ",math.ceil(necesar/c)," cutii",sep="")
print("cost gresie ",math.ceil(necesar/c)*pc," ron",sep="")
print("cost manopera ",math.ceil(necesar*pm)," ron",sep="")
total=math.ceil(necesar/c)*pc+pm*necesar
print("Cost total: ",math.floor(total)," ron",sep="")