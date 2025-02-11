import random
import tkinter as tk
from tkinter import messagebox as ms

from docutils.nodes import entry


def genereaza_numere():
    a = random.randint(1, 5)
    b = random.randint(1, 3)
    c=a*b
    return c,a,b

def verifica_raspuns(c,a,b):
    if c==a/b:
        ms.showinfo("Info","Raspuns corect!")

    else:
        ms.showinfo("Info","Raspuns incorect!")

    ms.showinfo("Info", "a : b=: " + str(c) + "a= " + str(a) + "b= " + str(b))
    c, a, b = genereaza_numere()

c,a,b=genereaza_numere()
aplicatie = tk.Tk()
aplicatie.geometry('300x200')
aplicatie.title("Calcule Maria")
eticheta1 = tk.Label(aplicatie, text="Efectueaza împărțirile :")
eticheta1.pack(padx=10,pady=10)
eticheta2 = tk.Label(aplicatie, text=str(a*b) + " : " + str(b) + " = ")
eticheta2.pack(padx=10,pady=10)
casuta_text = tk.Entry(aplicatie)
casuta_text.pack(padx=10,pady=10)
buton1=tk.Button(aplicatie,text="Trimite rezultat",command=lambda:verifica_raspuns(int(casuta_text.get()),a,b))

buton1.pack()
aplicatie.mainloop()
