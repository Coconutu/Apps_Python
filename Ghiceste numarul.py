import random
numar=random.randint(1,50)
ghicit=False
while ghicit==False:
    introdus=int(input('Scrie numarul:'))
    if introdus<numar:
        print("Prea mic. Mai incearca!")
    elif introdus>numar:
        print("Prea mare. Mai incearca!")
    else:
        print("Felicitari, ai chicit! Era numarul",numar)
        break

