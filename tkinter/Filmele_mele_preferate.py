import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()
# root.geometry("400x600")
#primul cadru cu eticheta cu imagine atasata
imagine_originala=Image.open("Imagini/1.jpg")
imagine=ImageTk.PhotoImage(imagine_originala)
cadru_cu_imagine=tk.Frame(root,padx=20,pady=20)
cadru_cu_imagine.pack()
eticheta=tk.Label(cadru_cu_imagine,image=imagine)
eticheta.pack()
contor=1
numar_imagini=3
def buton_inainte():
    global contor,imagine
    if contor<numar_imagini:
        contor=contor+1
    else:
        contor=1
    imagine_originala=Image.open('Imagini/'+str(contor)+".jpg")
    imagine=ImageTk.PhotoImage(imagine_originala)
    eticheta.config(image=imagine)
def buton_inapoi():
    global contor,imagine
    if contor>1:
        contor=contor-1
    else:
        contor=numar_imagini
    imagine_originala = Image.open('Imagini/'+str(contor) + ".jpg")
    imagine = ImageTk.PhotoImage(imagine_originala)
    eticheta.config(image=imagine)
sageata_stanga=tk.PhotoImage(file="Iconite/back.png")
sageata_dreapta=tk.PhotoImage(file="Iconite/forward.png")
cadru_cu_butoane=tk.Frame(root,padx=20,pady=20)
cadru_cu_butoane.pack()
buton_s=tk.Button(cadru_cu_butoane,image=sageata_stanga,text="Inapoi",compound='top',font="Calibri 12 bold",command=buton_inapoi)
buton_s.grid(row=0,column=0,padx=20,pady=20)
buton_d=tk.Button(cadru_cu_butoane,image=sageata_dreapta,text="Inainte",compound='top',font="Calibri 12 bold",command=buton_inainte)
buton_d.grid(row=0,column=1,padx=20,pady=20)
root.mainloop()


