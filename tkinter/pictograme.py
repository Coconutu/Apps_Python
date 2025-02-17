import tkinter as tk
root=tk.Tk()
#Caracter Unicode pentru o săgeată la stânga (←)
sageata_stanga=u"\u2190"
# buton1=tk.Button(root,text=sageata_stanga+'\n Înapoi',font="Calibri 12 bold")
# buton1.pack()
sageata_stanga=tk.PhotoImage(file="Iconite/back.png")
sageata_dreapta=tk.PhotoImage(file="Iconite/forward.png")

buton_s=tk.Button(root,image=sageata_stanga,text="Inapoi",compound='top',font="Calibri 12 bold")
buton_s.grid(row=0,column=0,padx=20,pady=20)

buton_d=tk.Button(root,image=sageata_dreapta,text="Inapoi",compound='top',font="Calibri 12 bold")
buton_d.grid(row=0,column=1,padx=20,pady=20)

root.mainloop()