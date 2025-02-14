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
stop=10
a = random.randint(MIN_A, MAX_A)
b = random.randint(MIN_B, MAX_B)
c = a * b
aplicatie = tk.Tk()
aplicatie.resizable(False, False)
# aplicatie.geometry('350x200')
aplicatie.title("Calcule Maria")
def inchide_aplicatie():
	aplicatie.destroy()
buton_inchide=tk.Button(aplicatie,text="X",font=("Arial",15,"bold"),command=inchide_aplicatie,relief="raised",borderwidth=10)
buton_inchide.pack(side="top",anchor="ne")
eticheta1 = tk.Label(aplicatie, text="Efectueaza împărțirile :", font=font_etichete)
eticheta1.pack(pady=50)
eticheta2 = tk.Label(aplicatie, text=str(a * b) + " : " + str(b) + " = ", font=font_etichete)
eticheta2.pack()
casuta_text = tk.Entry(aplicatie, font=font_etichete)
casuta_text.pack(pady=50)
eticheta_corecte = tk.Label(aplicatie, text="Corecte : 0", font=font_etichete)
eticheta_corecte.pack()
eticheta_incorecte = tk.Label(aplicatie, text="Greșite : 0", font=font_etichete)
eticheta_incorecte.pack(pady=50)


def genereaza_numere():
    global a, b, c
    a = random.randint(MIN_A, MAX_A)
    b = random.randint(MIN_B, MAX_B)
    c = a * b
    eticheta2.config(text=str(a * b) + " : " + str(b) + " = ", font=font_etichete)
    casuta_text.delete(0, tk.END)


def verifica_raspuns():
    global count, corecte, gresite,stop
    try:

        if int(casuta_text.get()) == a:
            corecte += 1
            if corecte==stop:
            	ms.showinfo("Felicitari","Ai raspuns corect la "+str(stop)+" \n calcule! Ai gresit "+str(gresite)+" calcule!")
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


buton1 = tk.Button(aplicatie, text="Trimite rezultat", font=font_butoane, command=verifica_raspuns,width=50,height=3,bg="lightblue",relief="raised",borderwidth=20)
buton1.pack(pady=50)
aplicatie.mainloop()