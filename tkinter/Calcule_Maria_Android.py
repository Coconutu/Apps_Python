import random
import tkinter as tk
from tkinter import messagebox as ms

font_etichete = ("Arial", 16)
font_butoane = ("Arial", 13)
corecte = 0
gresite = 0
MIN_A = 8
MAX_A = 20
MIN_B = 2
MAX_B = 9
stop = 10
a = random.randint(MIN_A, MAX_A)
b = random.randint(MIN_B, MAX_B)
c = a * b
aplicatie = tk.Tk()
aplicatie.resizable(False, False)
# aplicatie.geometry('350x200')
aplicatie.title("Calcule Maria")


def inchide_aplicatie():
    aplicatie.destroy()


buton_inchide = tk.Button(aplicatie, text="X", font=("Arial", 15, "bold"), command=inchide_aplicatie, relief="raised",
                          borderwidth=10)
buton_inchide.grid(row=0,column=4)
eticheta1 = tk.Label(aplicatie, text="Efectueaza împărțirile :", font=font_etichete)
eticheta1.grid(row=0,column=0)
eticheta2 = tk.Label(aplicatie, text=str(a * b) + " : " + str(b) + " = ", font=font_etichete)
eticheta2.grid(row=1,column=0)
casuta_text = tk.Entry(aplicatie, font=font_etichete)
casuta_text.grid(row=2,column=0)
eticheta_corecte = tk.Label(aplicatie, text="Corecte : 0", font=font_etichete)
eticheta_corecte.grid(row=3,column=0)
eticheta_incorecte = tk.Label(aplicatie, text="Greșite : 0", font=font_etichete)
eticheta_incorecte.grid(row=4, column=0)
for x in range(0,5):
    buton_nr=tk.Button(aplicatie,text=str(x))
    buton_nr.grid(row=5, column=x)
for x in range(5,9):
    buton_nr=tk.Button(aplicatie,text=str(x))
    buton_nr.grid(row=6,column=x-5)

def genereaza_numere():
    global a, b, c
    a = random.randint(MIN_A, MAX_A)
    b = random.randint(MIN_B, MAX_B)
    c = a * b
    eticheta2.config(text=str(a * b) + " : " + str(b) + " = ", font=font_etichete)
    casuta_text.delete(0, tk.END)


def verifica_raspuns():
    global count, corecte, gresite, stop
    try:

        if int(casuta_text.get()) == a:
            corecte += 1
            if corecte == stop:
                ms.showinfo("Felicitari", "Ai raspuns corect la " + str(stop) + " \n calcule! Ai gresit " + str(
                    gresite) + " calcule!")
                inchide_aplicatie()

            eticheta_corecte.config(text="Corecte : " + str(corecte))
            genereaza_numere()
            casuta_text.delete(0, tk.END)


        else:
            gresite += 1
            eticheta_incorecte.config(text="Greșite : " + str(gresite))
            casuta_text.delete(0, tk.END)
    except ValueError:
        eticheta_corecte.config(text=" Introduceti rezultatul", font=font_etichete)


buton1 = tk.Button(aplicatie, text="Trimite rezultat", font=font_butoane, command=verifica_raspuns, width=30, height=2,
                   bg="lightblue", relief="raised", borderwidth=20)
buton1.grid(row=7,column=0)
aplicatie.mainloop()
