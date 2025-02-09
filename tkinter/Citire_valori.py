'''Cerință. Se cere să se realizeze un program care citește de la tastatură
două numere naturale între 1 și 10000 și afișează apoi produsul acestora.'''
import tkinter as tk
from tkinter import messagebox as mb
from tkinter.simpledialog import askinteger as ak
nr1=0;nr2=0;suma=0

def citeste_numar_1():
    global nr1
    nr1=ak("Numarul 1","Numar intreg intre 1 si 1000",minvalue=1,maxvalue=1000)

def citeste_numar_2():
    global nr2
    nr2=ak("Numarul 1","Numar intreg intre 1 si 1000",minvalue=1,maxvalue=1000)
def afisare_rezultat():
    global suma,nr1,nr2
    suma=nr1+nr2
    mb.showinfo("Rezultat","Suma este "+str(suma))
aplicatie=tk.Tk()
aplicatie.title("Citirea unui numar intreg")
aplicatie.geometry("300x200")
buton1=tk.Button(aplicatie,text="nr1",command=citeste_numar_1);buton1.pack()
buton2=tk.Button(aplicatie,text="nr2",command=citeste_numar_2);buton2.pack()
buton3=tk.Button(aplicatie,text="Afisare rezultat",command=afisare_rezultat);buton3.pack()
aplicatie.mainloop()







