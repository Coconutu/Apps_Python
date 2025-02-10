import tkinter as tk
from tkinter import ttk

# Modulul ttk este o prescurtare de la "themed tkinter"
# care face parte din biblioteca standard Tkinter și oferă acces
# la setul de widget-uri stilizate (themed widgets). Aceste widget-uri sunt concepute
# să ofere o formă mai modernă și mai atractivă interfețelor grafice, în comparație
# cu widget-urile standard Tkinter.

from PIL.ImageOps import expand

aplicatie = tk.Tk()
aplicatie.title("exemplu cu doua cadre")
# primul cadru pentru introducerea datelor
cadrul_1 = ttk.Frame(aplicatie, padding="10")
cadrul_1.pack(fill='both', expand=True)
# adaugarea componetelor in cadru
eticheta1 = ttk.Label(cadrul_1, text='Preluare date')
eticheta1.pack()

text1 = ttk.Entry(cadrul_1)
text1.pack(pady=5)
text2 = ttk.Entry(cadrul_1)
text2.pack(pady=5)

# al doilea cadru pentru butoane
cadrul_2 = ttk.Frame(aplicatie, padding='10')
cadrul_2.pack(fill='both', expand=True)
# adaugarea butoanelor in cadrul al doilea
buton_trimite = ttk.Button(cadrul_2, text="Trimite")
buton_trimite.pack(side='left', padx=10)
buton_anuleaza = ttk.Button(cadrul_2, text="Anuleaza")
buton_anuleaza.pack(side='left', padx=10)

aplicatie.mainloop()
'''Parametrul pady creează un spațiu vertical peste și sub un widget, 
ajutând la evitarea aglomerării și îmbunătățind aspectul interfeței, 
de exemplu: .pack(pady=10) adaugă 10 pixeli de spațiu sus și jos (pe verticală). 
Similar, există și padx care adaugă spațiu suplimentar pe orizontală, la stânga și la dreapta.'''
