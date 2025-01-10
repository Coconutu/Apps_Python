print("Instructiunea break")
lista=["a","b","c","d","e","f"]
for x in lista:
    if x=="d":
        break
    print(x)
print("Instructiunea continue")
for x in lista:
    if x=="d":
        continue
    print(x)
n = 5
for i in range(1,n+1):
    for j in range(1,i):
        print(i,j)