x = 6
print(x)

def inc():
    global x
# Așadar, o variabilă definită în exteriorul funcției este globală implicit – trebuie doar să specificăm acest fapt în interior.
    x = x + 1
# Variabilele declarate în interiorul funcțiilor sunt numite variabile locale - mai precis, pot fi declarate în orice bloc (instrucțiune compusă) din cadrul acestora.
# Trebuie să folosim cuvântul cheie global pentru a scrie și a citi o variabilă din afară în interiorul unei funcții.
# Folosirea lui global în afara funcțiilor nu are niciun efect.
inc()
print(x)
