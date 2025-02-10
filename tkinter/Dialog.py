import tkinter as tk
from tkinter import messagebox as ms


def intrebare():
    result = ms.askquestion("Intrebare", "Mingea sare in poarta cand e gol")
    if result == 'yes':
        print("Mingea sare, intr-adevar in poarta cand e gol!")
    else:
        print("Gresit")


def ok_anulare():
    rezult = ms.askokcancel("Intrebare", "Doriti sa continuam")
    if rezult == "ok":
        print("Continuam")
    else:
        print("anulam")


aplicatie = tk.Tk()
aplicatie.title("Dialog tkinter")
aplicatie.geometry("400x300")

buton1 = tk.Button(aplicatie, text="Dialog 1", command=intrebare)
buton1.pack()
buton2 = tk.Button(aplicatie, text="Dialog 2", command=ok_anulare)
buton2.pack()

aplicatie.mainloop()
'''Funcțiile askopenfilename, asksaveasfilename, și askdirectory din modulul filedialog oferă 
utilizatorilor interfețe grafice intuitive pentru selecția fișierelor și directoarelor, fie pentru 
deschiderea, salvarea, sau alegerea locației fișierelor în cadrul aplicațiilor. Dacă vom avea de realizat 
o aplicație care trebuie să manipuleze fișiere, precum un editor de text primar, vom avea nevoie de toate acestea!'''
