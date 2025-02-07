import tkinter as tk
from tkinter import messagebox as ms
def inchide_fereastra():
    ms.showinfo("La revedere","Aplicatia se va inchide")
    aplicatie.destroy()

aplicatie=tk.Tk()
aplicatie.iconbitmap("python.ico")
aplicatie.geometry("400x300+550+250")
aplicatie.attributes('-alpha',0.70,'-fullscreen',True)
aplicatie.protocol('WM_DELETE_WINDOW',inchide_fereastra)
etichete_inchidere=tk.Label(aplicatie,text="Buton de inchidere")
etichete_inchidere.pack()
buton_inchidere=tk.Button(aplicatie,text="Inchide aplicatia",command=inchide_fereastra)
buton_inchidere.pack()



aplicatie.mainloop()