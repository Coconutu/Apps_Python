'''2. Scrieţi un program care citeşte o valoare care trebuie să fie un întreg
între 1 şi 5. Dacă valoarea introdusă nu este de tip întreg (de exemplu,
începe cu un caracter alfabetic) sau dacă valoarea este numerică, dar nu
este între 1 şi 5, citirea se reia până când condiţiile cerute sunt îndeplinite.
Indicaţie: pentru citire, se poate utiliza o variabilă de tip şir de caractere.'''
def citeste():
    x=input("Introduceti o valoare intreaga >=1 si <=5")
    try:
        n=int(x)
        if n<1 or n>5:
            raise ValueError
        else:

            return n

    except ValueError:
        print("Valoare incorecta! Reintroduceti valoarea.")
        citeste()

print(citeste())
#rezolvat