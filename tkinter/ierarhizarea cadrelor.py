import tkinter as tk
from tkinter import ttk


aplicatie = tk.Tk()
aplicatie.title('Cadre imbricate')
# Nivelul superior
cadru_exterior = ttk.Frame(aplicatie, padding='10', relief='sunken', borderwidth=5)
cadru_exterior.pack(fill='both', expand=True)
#adaugarea unui cadru in interiorul celui superior
cadru_interior=ttk.Frame(cadru_exterior,padding='10',relief='raised',borderwidth=3)
cadru_interior.pack(padx=20,pady=20)
#adaugarea unui cadru si mai interior
cadru_mai_interior=ttk.Frame(cadru_interior,padding='5',relief='groove',borderwidth=2)
cadru_mai_interior.pack(padx=10,pady=10)
#adaugarea unei eticete in cel mai interior cadru
etichette=ttk.Label(cadru_mai_interior,text="Eticheta in cel mai interior cadru!")
etichette.pack(pady=5)
aplicatie.mainloop()

