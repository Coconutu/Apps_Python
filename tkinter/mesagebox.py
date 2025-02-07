import tkinter as tk
from tkinter import messagebox as ms
def inchide_fereastra():
    ms.showinfo("La revedere","Aplicatia se va inchide")
    aplicatie.destroy()

def deschide_fereastra_noua():
    fereastra_noua = tk.Toplevel()
    fereastra_noua.title("Fereastra noua - Toplevel")
    fereastra_noua.geometry("200x200")
    eticheta=tk.Label(fereastra_noua,text="Bine ati venit")
    eticheta.pack()

    def inchide_fereastra_noua():
        fereastra_noua.destroy()

    buton_inchidere_fereastra_noua = tk.Button(fereastra_noua, text="Buton inchidere fereastra noua",
                                                   command=inchide_fereastra_noua)
    buton_inchidere_fereastra_noua.pack()


aplicatie=tk.Tk()
aplicatie.iconbitmap("python.ico")
aplicatie.geometry("400x300+550+250")
aplicatie.attributes('-alpha',0.70,'-fullscreen',True)
aplicatie.protocol('WM_DELETE_WINDOW',inchide_fereastra)
etichete_inchidere=tk.Label(aplicatie,text="Buton de inchidere")
etichete_inchidere.pack()
buton_inchidere=tk.Button(aplicatie,text="Inchide aplicatia",command=inchide_fereastra)
buton_inchidere.pack()
buton_deschide_fereastra_noua=tk.Button(aplicatie,text="Deschide fereastra noua",command=deschide_fereastra_noua)
buton_deschide_fereastra_noua.pack()


aplicatie.mainloop()