import random
import tkinter as tk
from tkinter import messagebox as ms

from PIL.ImageOps import expand

font_etichete = ("Arial", 16, 'bold')
font_butoane = ("Arial", 13, 'bold')
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
buton_inchide.pack(anchor='ne')
eticheta1 = tk.Label(aplicatie, text="Efectueaza împărțirile :", font=font_etichete)
eticheta1.pack()
eticheta2 = tk.Label(aplicatie, text=str(a * b) + " : " + str(b) + " = ", font=font_etichete)
eticheta2.pack()
casuta_text = tk.Entry(aplicatie, font=font_etichete,bg='yellow',fg='blue')
casuta_text.pack()


def scrie_in_casuta(x):
    text_nou=casuta_text.get()+str(x)
    #ms.showinfo("info",str(text_nou))
    casuta_text.delete(0,tk.END)
    casuta_text.insert(0,text_nou)


eticheta_corecte = tk.Label(aplicatie, text="Corecte : 0", font=font_etichete)
eticheta_corecte.pack()
eticheta_incorecte = tk.Label(aplicatie, text="Greșite : 0", font=font_etichete)
eticheta_incorecte.pack()
cadru1 = tk.Frame(aplicatie)
cadru1.pack(fill='both', expand=True)
buton_1 = tk.Button(cadru1, text='1', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:scrie_in_casuta(1),bg='lightgreen')
buton_1.pack(side='left')
buton_2 = tk.Button(cadru1, text='2', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:scrie_in_casuta(2),bg='lightgreen')
buton_2.pack(side='left')
buton_3 = tk.Button(cadru1, text='3', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:scrie_in_casuta(3),bg='lightgreen')
buton_3.pack(side='left')
buton_4 = tk.Button(cadru1, text='4', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:scrie_in_casuta(4),bg='lightgreen')
buton_4.pack(side='left')
buton_5 = tk.Button(cadru1, text='5', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:scrie_in_casuta(5),bg='lightgreen')
buton_5.pack(side='left')
cadru2 = tk.Frame(aplicatie)
cadru2.pack(fill='both', expand=True)
buton_6 = tk.Button(cadru2, text='6', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:scrie_in_casuta(6),bg='lightgreen')
buton_6.pack(side='left')
buton_7 = tk.Button(cadru2, text='7', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:scrie_in_casuta(7),bg='lightgreen')
buton_7.pack(side='left')
buton_8 = tk.Button(cadru2, text='8', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:scrie_in_casuta(8),bg='lightgreen')
buton_8.pack(side='left')
buton_9 = tk.Button(cadru2, text='9', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:scrie_in_casuta(9),bg='lightgreen')
buton_9.pack(side='left')
buton_del = tk.Button(cadru2, text='<-', borderwidth=5, width=5, height=2, font=font_butoane,command=lambda:casuta_text.delete(0,tk.END),bg='red')
buton_del.pack(side='left')

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


buton1 = tk.Button(aplicatie, text="Trimite rezultat", font=font_butoane, command=verifica_raspuns, height=2,
                   bg="lightblue", relief="raised", borderwidth=20)
buton1.pack()
aplicatie.mainloop()
