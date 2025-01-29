def recursiv1(n):
    if (n!=0):
        print(n)
        recursiv1(n-1)
recursiv1(7)

def suma1(n):
    if n>0:
        return n+suma1(n-1)
    else:
        return n
print("Suma este",suma1(7))


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

def fib(n):
    if n==0:return 0
    elif n==1:return 1
    else:return fib(n-1)+fib(n-2)

for i in range (21):
    print("fib("+str(i)+")=",fib(i))

'''1. Calculaţi recursiv suma a n numere naturale citite.'''
def sumap(n):
    if n>0:
        return n+sumap(n-1)
    else:
        return n
print(sumap(4))

'''Calculaţi recursiv expresiile:
a) 1*2+2*3+...+n*(n+1);'''
def expr(n):
    if n>0:
        return n*(n+1)+expr(n-1)
    else:return n
print(expr(3))
