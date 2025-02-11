import tkinter as tk
from tkinter import ttk
aplicatie=tk.Tk()
aplicatie.title("Exemple de parametri")
cadru=tk.Frame(aplicatie,borderwidth=5,relief='ridge')
cadru.pack()
eticheta=ttk.Label(cadru,text="Eticheta din cadru")
eticheta.pack(pady=5)
aplicatie.mainloop()
