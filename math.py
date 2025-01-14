import math

def f(x):
    return math.sin(x)+math.cos(x)+math.cos(2*x)
x=float(input())
print(f(x))