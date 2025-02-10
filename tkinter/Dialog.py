import tkinter as tk
from tkinter import messagebox as ms
def intrebare():
    result=ms.askquestion("Intrebare","Mingea sare in poarta cand e gol")
    if result=='yes':
        print("Mingea sare, intr-adevar in poarta cand e gol!")
    else:
        print("Gresit")


aplicatie=tk.Tk()
aplicatie.title("Dialog tkinter")
aplicatie.geometry("400x300")

buton1=tk.Button(aplicatie,text="Dialog 1",command=intrebare);buton1.pack()

aplicatie.mainloop()
