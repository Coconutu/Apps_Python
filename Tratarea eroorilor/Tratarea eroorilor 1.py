n=int(input("Introduceti varsta = "))
anul_nasterii=2025-n
if n<3:
    print("Geniu! Te-ai nascut in ",anul_nasterii,"!")
elif n >120:
    print("Tu si piramidele ! Cum era prin", anul_nasterii,"?")
elif n > 99:
    print("Felicitari!Anul nasterii :",anul_nasterii, "!")
else:
    print("Anul nasterii:",anul_nasterii,".",sep="")