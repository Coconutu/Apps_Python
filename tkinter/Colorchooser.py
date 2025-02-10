import tkinter as tk
from tkinter.colorchooser import askcolor
def schimba_culoarea():
    culoare_aleasa,hex_culoare_aleasa=askcolor()
    if hex_culoare_aleasa:
        #setez culoarea de fundal a butonului
        buton.config(bg=hex_culoare_aleasa)
        #afisez in colsona cele doua valori
    print(culoare_aleasa,hex_culoare_aleasa)
aplicatie=tk.Tk()
buton=tk.Button(aplicatie,text="Alege o culoare",command=schimba_culoarea)
buton.pack()
aplicatie.mainloop()