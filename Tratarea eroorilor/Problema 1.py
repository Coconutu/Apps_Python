'''1. Scrieţi un program care citeşte o valoare întreagă până când ea este mai
mare sau egală cu 1 şi mai mică sau egală cu 5. La citirea unei valori
incorecte, să se afişeze un mesaj de eroare şi să se reia citirea.'''
from csv import excel


def citeste():
    n=int(input("Introduceti o valoare intreaga >=1 si <=5"))
    try:
        if n<1 or n>5:
            raise ValueError
    except ValueError:
        print("Valoare incorecta! Reintroduceti valoarea.")
        citeste()
    if n>=1 or n<=5:
        return n
print(citeste())