'''Metoda place permite folosirea coordonatelor relative (prin relx, rely, relwidth
și relheight) în loc de valori absolute, ceea ce este util pentru un layout flexibil
care se adaptează la dimensiunea ferestrei.'''
import tkinter as tk
aplicatie=tk.Tk()
aplicatie.geometry('400x400')
buton1=tk.Button(aplicatie,text="Buton")
buton1.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)
#coordonate relative
aplicatie.mainloop()
