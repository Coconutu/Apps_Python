try:
    n=int(input("n (numar intreg)="))
    print(100/n)
except ValueError:
    print("Eroare. Introduceti un numar intreg!")
except ZeroDivisionError:
    print("Eroare: nu putem imparti la zero")
finally:
    print("Program terminat ok.")