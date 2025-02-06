import tkinter as tk
aplicatie=tk.Tk()#o instanta a ferestrei principale
aplicatie.title("Prima mea aplicatie")#setez titlul ferestrei
aplicatie.iconbitmap("python.ico")
def functie_de_inchidere(): #definim o functie pe care o vom folosi dupa ce apasam butonul X al ferestrei
    print("La revedere!")
    aplicatie.destroy()

def deschide_fereastra_noua():
    fereastra_noua=tk.Toplevel()
    fereastra_noua.title("Fereastra noua")
    fereastra_noua.geometry("300x200")
    eticheta=tk.Label(fereastra_noua,text='Salut, fereastra noua')
    eticheta.pack()

aplicatie.protocol("WM_DELETE_WINDOW",functie_de_inchidere) #apelam functie de inchidere in momentul cand se apasa x
aplicatie.config(bg="cyan") #culoarea de fundal a ferestrei
aplicatie.attributes('-alpha',0.7) #transparenta ferestrei
aplicatie.attributes('-fullscreen',"True") #rulam aplicatia in fullscreen
aplicatie.geometry("400x300+100+100")#setez dimensiunea ferestrei, o plasez la 100 px de marginea stanga si 100 de sus
aplicatie.resizable(width=True,height=False) #permitem redimensionarea ferestrei pe oizontala, nu si pe verticala
eticheta=tk.Label(aplicatie,text="Bine ati venit!") #eticheta este variabila ce retine referinta la obiectul Label
eticheta.pack()
buton=tk.Button(aplicatie,text="ok",command=lambda:print("Buton apasat"))
buton.pack()#pentru a afisa butonul, fara aceasta instructiune, butonu ramane creat doar in memorie, nu ar fi afisat
buton_deschide_fereastra_noua=tk.Button(aplicatie,text="Deschide fereastra noua!",command=deschide_fereastra_noua)
buton_deschide_fereastra_noua.pack()
buton_inchidere=tk.Button(aplicatie,text="Inchidere",command=aplicatie.destroy)
buton_inchidere.pack()
aplicatie.mainloop()#pornesc bucla evenimentului principal
