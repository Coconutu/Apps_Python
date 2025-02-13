import tkinter as tk
aplicatie=tk.Tk()
aplicatie.geometry("200x200")
#primul buton
buton1=tk.Button(aplicatie,text="buton 1",bg='red')
buton1.place(x=50,y=50,width=100,height=50)
#al doilea buton suprapus peste primul
buton2=tk.Button(aplicatie,text="buton 2",bg='blue')
buton2.place(x=70,y=70,width=100,height=50)
aplicatie.mainloop()