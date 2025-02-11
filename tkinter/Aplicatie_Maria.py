import random
import tkinter as tk
rezultat=[1,1,1]

def genereaza_impartire():
    a = random.randint(10, 30)
    b = random.randint(1, 9)
    c = a * b
    rezultat = [a, b, c]
    return rezultat

def trimite_raspuns():
    raspuns=int(casuta_text.get())
    if raspuns:
        if



rezultat = genereaza_impartire()
aplicatie = tk.Tk()
aplicatie.geometry('300x200')
aplicatie.title("Calcule Maria")
eticheta1 = tk.Label(aplicatie, text="Efectueaza împărțirile :")
eticheta1.pack(padx=10,pady=10)
eticheta2 = tk.Label(aplicatie, text=str(rezultat[2]) + " : " + str(rezultat[1]) + " = ")
eticheta2.pack(padx=10,pady=10)
casuta_text = tk.Entry(aplicatie)
casuta_text.pack(padx=10,pady=10)
buton1=tk.Button(aplicatie,text="Trimite rezultat",command=trimite_rezultat)

aplicatie.mainloop()
