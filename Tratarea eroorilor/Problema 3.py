'''3. Scrieţi un program care citeşte, de pe prima linie a unui fişier text cu
numele “date.in”, o valoare naturală între 1 şi 5. Dacă fişierul nu există sau
dacă pe prima linie nu este o valoare naturală sau dacă valoarea se
găseşte, dar nu este între 1 şi 5, programul se opreşte şi se afişează un
mesaj corespunzător. Dacă valoarea se găseşte, atunci să se afişeze
valoarea ridicată la pătrat'''
try:
    with open("date.in","r") as f:
        citire_linie=f.readline()
        valoare=int(citire_linie)
        if valoare<1 or valoare>5:
            raise ValueError
        else:
            print(valoare*valoare)

except FileNotFoundError:
    print("Fisierul nu exista")
except ValueError:
    print("Valoare suspecta")

