try:
    n=int(input("Introduceti varsta (intre 3 si 120)"))
    anul_nasterii=2025-n
    if n>=3 and n<=120:
        print("Anul nasterii:", anul_nasterii, ".", sep="")
    else:
        print("Respecta intervalul!")
except ValueError:
    print("Ups. Nu ai introdus un numar natural")
    print("Reporneste programul")
finally:
    print("Program terminat ok")