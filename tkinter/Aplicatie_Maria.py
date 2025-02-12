import random
import tkinter as tk

font_etichete = ("Arial", 16)
font_butoane = ("Arial", 13)

corecte=0
gresite=0

def genereaza_numere():
    global a, b, c
    a = random.randint(10, 15)
    b = random.randint(2, 9)
    c = a * b


genereaza_numere()
aplicatie = tk.Tk()
aplicatie.resizable(False, False)
aplicatie.geometry('350x200')
aplicatie.title("Calcule Maria")
eticheta1 = tk.Label(aplicatie, text="Efectueaza împărțirile :", font=font_etichete)
eticheta1.place(x=10, y=10)
eticheta2 = tk.Label(aplicatie, text=str(a * b) + " : " + str(b) + " = ", font=font_etichete)
eticheta2.place(x=10, y=50)
casuta_text = tk.Entry(aplicatie, font=font_etichete)
casuta_text.place(x=100, y=50, width=50)
eticheta_corecte= tk.Label(aplicatie, text="Corecte :", font=font_etichete)
eticheta_corecte.place(x=10, y=100)
eticheta_incorecte=tk.Label(aplicatie, text="Greșite :", font=font_etichete)
eticheta_incorecte.place(x=10, y=150)

def verifica_raspuns():
    global count,corecte,gresite

    try:

        if int(casuta_text.get()) == a:
            corecte+=1
            eticheta_corecte.config(text="Corecte : "+str(corecte))
            genereaza_numere()
            eticheta2.config(text=str(a * b) + " : " + str(b) + " = ", font=font_etichete)
            casuta_text.delete(0, tk.END)
        else:
            gresite+=1
            eticheta_incorecte.config(text="Greșite :"+str(gresite))
    except ValueError:
        eticheta_corecte.config(text="Eroare! Introduceti rezultatul in casuta text!",font=font_butoane)

buton1 = tk.Button(aplicatie, text="Trimite rezultat", font=font_butoane,command=verifica_raspuns)
buton1.place(x=180, y=50)
aplicatie.mainloop()
