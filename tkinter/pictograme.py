import tkinter as tk
root=tk.Tk()
#Caracter Unicode pentru o săgeată la stânga (←)
sageata_stanga=u"\u2190"
buton=tk.Button(root,text=sageata_stanga+'\n Înapoi',font="Calibri 12 bold")
buton.pack()
root.mainloop()