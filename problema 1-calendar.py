# 1. Să se introducă de la tastatură un an și o lună, iar apoi să se afișeze calendarul pentru acea lună.
# import calendar
# anul=int(input("Introduceti anul "))
# luna=int(input("Introduceti luna "))
# calendarul_meu=calendar.month(anul,luna)
# print(calendarul_meu)
import calendar

# 2. Să se introducă de la tastatură un an, iar apoi să se afișeze dacă acel an este bisect sau nu.
# anul=int(input("Introduceti anul "))
# print(calendar.isleap(anul))

# 3. Să se ceară utilizatorului să introducă o dată de început și o dată de sfârșit, iar apoi să se afișeze numărul
# de zile lucrătoare (fără weekend) din acel interval.
# Sugestie: utilizați funcția calendar.weekday(anul, luna, ziua) și iterați prin zilele din interval
# pentru a număra zilele lucrătoare.
ziua_i=int(input("Introduceti ziua de inceput"))
luna_i=int(input("Introduceti luna de inceput"))
anul_i=int(input("Introduceti anul de inceput"))
ziua_s=int(input("Introduceti ziua de sfarsit"))
luna_s=int(input("Introduceti luna de sfarsti"))
anul_s=int(input("Introduceti anul de sfarsit"))



