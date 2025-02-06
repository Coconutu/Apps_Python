import tkinter as tk
aplicatie=tk.Tk()#o instanta a ferestrei principale
aplicatie.title("Prima mea aplicatie")#setez titlul ferestrei
aplicatie.geometry("400x300")#setez dimensiunea ferestrei
eticheta=tk.Label(aplicatie,text="Bine ati venit!")
eticheta.pack()
buton=tk.Button(aplicatie,text="ok",command=lambda:print("Buton apasat"))
buton.pack()

aplicatie.mainloop()#pornesc bucla evenimentului principal