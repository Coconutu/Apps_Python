import tkinter as tk
from tkinter import messagebox as mb
from tkinter.simpledialog import askstring
def citeste_email():
    rezultat=askstring("Email","Introduceti adresa de email")
    print("Emailul este ",rezultat)
aplicatie=tk.Tk()
aplicatie.title("Formular de date")
aplicatie.geometry("300x200")
buton_email=tk.Button(aplicatie,text="Adresa de email",command=citeste_email);buton_email.pack()

aplicatie.mainloop()


