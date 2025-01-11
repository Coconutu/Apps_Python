antonime = {'inalt':'scund', 'frumos':'urat', 'rapid':'lent'}
print(antonime)
#dimensiunea unui dicționar - în acest caz, 3
print(len(antonime))
#accesam valoarea cheii 'inalt'
print(antonime['inalt'])
print(antonime['frumos'])

# Putem folosi o listă de tupluri, ca în exemplul următor:
dict1 = dict( [('inalt','scund'), ('rece','cald')] )
print(dict1)

# Pentru a șterge un dicționar, folosim cuvântul cheie del, adică "del dict1", așa cum suntem obișnuiți.
# Dacă dorim să îl golim, apelăm iar la metoda clear(), mai exact scriem în exemplul nostru: "dict1.clear()".
# dict1.clear()
# print(dict1)
#
# del dict1
# print("Dictionarul a fost sters")
#Am precizat anterior faptul că putem accesa un element cu ajutorul unui cuvânt cheie folosind parantezele pătrate,
# însă dacă nu este găsit în dicționar, obținem o eroare ce ne blochează programul.
#Folosim elegant metoda get() ce primește ca parametru un cuvânt cheie.
# Dacă există în dicționar este afișată valoarea asociată, iar dacă nu, cuvântul cheie None:
el1 = dict1.get('inalt')
el2 = dict1.get('rece')
el3 = dict1.get('mic') #afiseaza None
#le afișăm
print(el1,el2,el3)
dict1['mare']="micut" #adaugare element
print(dict1)
dict2=frozenset(dict1) #conversie explicita
print(dict2) #o sa contina doar cheile, nu si valorile asociate