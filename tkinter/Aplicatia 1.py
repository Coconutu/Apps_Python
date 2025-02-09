'''Cerință. Se cere să se realizeze un program care solicită utilizatorului să
introducă numele, prenumele și o adresă de email, apoi să afișeze un mesaj
drăguț de bun venit, care să confirme înregistrarea datelor în program.'''
import tkinter as tk
from tkinter import messagebox as mb
from tkinter.simpledialog import askstring

date_utilizator={"Nume":"","Prenume":"","Email":""}
def solicita_informatie(info):
    rezultat=askstring("Input",f"Introduceti {info}")
    if rezultat:
        date_utilizator[info]=rezultat
        if all(date_utilizator.values()):
            mesaj=f"Bun venit,{date_utilizator['Nume']},{date_utilizator['Prenume']}!.Emailul tau,{date_utilizator['Email']},a fost inregistrat cu succes."
            mb.showinfo("Inregistrare completa",mesaj)
aplicatie=tk.Tk()
aplicatie.title("Inregistrare")
buton_n=tk.Button(aplicatie,text="Introduceti numele",command=lambda:solicita_informatie("Nume"));buton_n.pack()
buton_p=tk.Button(aplicatie,text="Introduceti prenumele",command=lambda:solicita_informatie("Prenume"));buton_p.pack()
buton_e=tk.Button(aplicatie,text="Introduceti emailul",command=lambda:solicita_informatie("Email"));buton_e.pack()
aplicatie.mainloop()