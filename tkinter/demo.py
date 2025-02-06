import tkinter as tk
aplicatie=tk.Tk()#o instanta a ferestrei principale
aplicatie.title("Prima mea aplicatie")#setez titlul ferestrei
aplicatie.geometry("400x300")#setez dimensiunea ferestrei
eticheta=tk.Label(aplicatie,text="Bine ati venit!") #eticheta este variabila ce retine referinta la obiectul Label
eticheta.pack()
buton=tk.Button(aplicatie,text="ok",command=lambda:print("Buton apasat"))
buton.pack()#pentru a afisa butonul, fara aceasta instructiune, butonu ramane creat doar in memorie, nu ar fi afisat

aplicatie.mainloop()#pornesc bucla evenimentului principal