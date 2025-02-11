import random
import tkinter as tk
from tkinter import messagebox as ms

def genereaza_numere():
    f1 = random.randint(1, 5)
    f2 = random.randint(1, 3)
    pr=f1*f2
    return f1,f2,pr

def verifica_raspuns(x,y,z):
    if x==y/z:
        ms.showinfo("Info","Raspuns corect!")

    else:
        ms.showinfo("Info","Raspuns incorect!")


a,b,c=genereaza_numere()
aplicatie = tk.Tk()
aplicatie.geometry('300x200')
aplicatie.title("Calcule Maria")
eticheta1 = tk.Label(aplicatie, text="Efectueaza împărțirile :")
eticheta1.pack(padx=10,pady=10)
eticheta2 = tk.Label(aplicatie, text=str(c) + " : " + str(a) + " = ")
eticheta2.pack(padx=10,pady=10)
casuta_text = tk.Entry(aplicatie)
casuta_text.pack(padx=10,pady=10)
buton1=tk.Button(aplicatie,text="Trimite rezultat",command=lambda:verifica_raspuns(int(casuta_text.get()),c,a))

buton1.pack()
aplicatie.mainloop()
