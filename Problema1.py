# Se citește un număr natural n. Să se calculeze suma:
# S = 1 + 1·2 + 1·2·3 + ... 1·2·...·n
n=int(input("n="))
s=0
p=1
for x in range(1,n+1):
    p=p*x
    s=s+p
print("Rezultatul este",s)
