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