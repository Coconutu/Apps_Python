import random
import tkinter as tk
from tkinter import messagebox as ms

def genereaza_numere():
    f1 = random.randint(1, 5)
    f2 = random.randint(1, 3)
    return f1,f2

a,b=genereaza_numere()
aplicatie = tk.Tk()
aplicatie.geometry('300x200')
aplicatie.title("Calcule Maria")
eticheta1 = tk.Label(aplicatie, text="Efectueaza împărțirile :")
eticheta1.pack(padx=10,pady=10)
eticheta2 = tk.Label(aplicatie, text="Verificare rezultat")
eticheta2.pack(padx=10,pady=10)
eticheta3 = tk.Label(aplicatie, text=str(a*b) + " : " + str(a) + " = ")
eticheta3.pack(padx=10,pady=10)
casuta_text = tk.Entry(aplicatie)
casuta_text.pack(padx=10,pady=10)

def verifica_raspuns(pr,f1,f2):
    if pr==f1*f2:
        eticheta2.config(text="Raspuns corect")


    else:
        eticheta2.config(text="Raspuns incorect")





buton1=tk.Button(aplicatie,text="Trimite rezultat",command=lambda:verifica_raspuns(int(casuta_text.get()),a,b))

buton1.pack()
aplicatie.mainloop()
