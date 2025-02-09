import tkinter as tk
from tkinter import messagebox as ms
from tkinter.simpledialog import askinteger
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
        ms.showerror("Eroare falsa","Eroare doar in scop didactic.")
        fereastra_noua.destroy()

    buton_inchidere_fereastra_noua = tk.Button(fereastra_noua, text="Buton inchidere fereastra noua",
                                                   command=inchide_fereastra_noua)
    buton_inchidere_fereastra_noua.pack()

def afisare_mesaj():
    raspuns=ms.askyesno("Alegere","Vrei sau nu?")
    if raspuns:
        ms.showinfo("Informatie","Ati ales Da")
    else:
        ms.showinfo("Informatie","Ati ales Nu")

def citeste_numar():
    rezultat=askinteger("Citeste date","Introduceti un numar intreg intre 1 si 100",minvalue=1,maxvalue=100)
    if rezultat!=None:
        ms.showinfo("Valoare citita","A fost introdusa valoarea "+str(rezultat))
    else:
        ms.showerror("Eroare","Nu a fost introdusa nicio valoare!")
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
buton_afisare_mesaj=tk.Button(aplicatie,text="Afisare mesaj",command=afisare_mesaj)
buton_afisare_mesaj.pack()
etichete_nr_intregi=tk.Label(aplicatie,text="Input numar intreg")
etichete_nr_intregi.pack()
buton_citests_numar=tk.Button(aplicatie,text="Citeste numar",command=citeste_numar)
buton_citests_numar.pack()
aplicatie.mainloop()