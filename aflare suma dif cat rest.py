try:
    n1=int(input("introduceti doua numere naturale nenule "))
    n2=int(input())
    if n2==0:raise ZeroDivisionError
    print("suma este ",n1+n2)
    print("diferenta este ",n1-n2)
    print("produsul este ",n1*n2)
    print("catul este ",n1//n2)
    print("restul este ",n1%n2)
except ValueError:
    print("Numerele trebuie sa fie naturale")
except ZeroDivisionError:
    print("al doilea numar trebuie sa fie diferit de zero")
finally:
    print("Program terminat ok")



