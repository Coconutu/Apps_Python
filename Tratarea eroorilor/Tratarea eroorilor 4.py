try:
    n=int(input("Introduceti varsta intre 3 si 120 ani: "))
    if n<3 or n>120:
        raise ValueError
    else:
        print("Te-ai nascut in ", 2025-n)
except ValueError:
    print("Eroare. Date de intrare suspecte")
finally:
    print("Program terminat ok")