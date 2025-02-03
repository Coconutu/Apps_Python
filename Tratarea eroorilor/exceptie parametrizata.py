def test(x):
    if x>=1 and x<=5:return x
    else:
        raise Exception(x)

x=int(input("x="))
try:
    print(test(x))
except Exception as exceptie:
    valoare=exceptie.args[0]
    print(valoare)
    if valoare<1:print("x<1")
    if valoare>5:print("x>1")