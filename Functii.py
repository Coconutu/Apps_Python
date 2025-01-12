def subp(n):
    s=0
    for i in range(n):
        s=s+1/(i+1)
    return s
n=int(input("Introduceti n"))
print(subp(n))