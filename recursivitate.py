def recursiv1(n):
    if (n!=0):
        print(n)
        recursiv1(n-1)
recursiv1(7)

def suma(n):
    if n>0:
        return n+suma(n-1)
    else:
        return n
print("Suma este",suma(7))


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))