import calendar
anul=2025
calendarul=calendar.calendar(anul)
print(calendarul)
luna=6
calendarul_lunii=calendar.month(2025,luna)
print(calendarul_lunii)
ziua=24
z=calendar.weekday(anul,luna,ziua) #ziua din saptamana pentru o anumita data din calendar
if z==0:
    z="Luni"
elif z==1:
    z="Marti"
elif z==2:
    z="Miercuri"
elif z==3:
    z="Joi"
elif z==4:
    z="Vineri"
elif z==5:
    z="Sambata"
elif z==6:
    z="Duminica"
print(z)
#verificare daca anul e bisect
print(calendar.isleap(2025))
#numarul zilelor dintr-oo luna
print(calendar.monthrange(anul,luna))