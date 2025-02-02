n=int(input("Introduceti varsta (intre 3 si 120)"))
anul_nasterii=2025-n
if n<3 or n>120:
    print("-------------------------------")
    print("Eroare. Va rugam sa respectati intervalul")
    print("Reporniti programul")
else:
    print("Anul nasterii:",anul_nasterii,".",sep="")