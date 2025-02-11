import tkinter as tk
from tkinter import ttk
aplicatie=tk.Tk()
aplicatie.geometry('300x200')
aplicatie.title("Exemple de parametri.Cursor diferit")
cadru=tk.Frame(aplicatie,width=20,height=100,bg='lightblue',cursor="hand2",relief='ridge')
cadru.pack()
eticheta=ttk.Label(cadru,text="Eticheta din cadru")
eticheta.pack(pady=50,padx=50)
aplicatie.mainloop()
