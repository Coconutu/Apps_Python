import tkinter as tk
aplicatie=tk.Tk()
aplicatie.title("Metoda place")
aplicatie.geometry('300x200')
#plasarea unui buton la coordonatele 50,50
buton1=tk.Button(aplicatie,text="Apasa-ma")
buton1.place(x=50,y=50)
aplicatie.mainloop()