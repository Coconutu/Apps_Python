import tkinter as tk
aplicatie=tk.Tk()#o instanta a ferestrei principale
aplicatie.title("Prima mea aplicatie")#setez titlul ferestrei
aplicatie.iconbitmap("python.ico")
aplicatie.config(bg="cyan") #culoarea de fundal a ferestrei
aplicatie.attributes('-alpha',0.6) #transparenta ferestrei
aplicatie.geometry("400x300+100+100")#setez dimensiunea ferestrei, o plasez la 100 px de marginea stanga si 100 de sus
aplicatie.resizable(width=True,height=False) #permitem redimensionarea ferestrei pe oizontala, nu si pe verticala
eticheta=tk.Label(aplicatie,text="Bine ati venit!") #eticheta este variabila ce retine referinta la obiectul Label
eticheta.pack()
buton=tk.Button(aplicatie,text="ok",command=lambda:print("Buton apasat"))
buton.pack()#pentru a afisa butonul, fara aceasta instructiune, butonu ramane creat doar in memorie, nu ar fi afisat
buton_inchidere=tk.Button(aplicatie,text="Inchidere",command=aplicatie.destroy)
buton_inchidere.pack()
aplicatie.mainloop()#pornesc bucla evenimentului principal
