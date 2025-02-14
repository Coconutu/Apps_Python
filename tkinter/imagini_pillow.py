import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()
imagine_originala=Image.open('poster_interstelar.jpg')
imagine=ImageTk.PhotoImage(imagine_originala)
cadru_cu_imagine=tk.Frame(root,padx=20,pady=20)
cadru_cu_imagine.pack()

eticheta1 = tk.Label(cadru_cu_imagine, text="Filmul meu preferat",image=imagine,compound='top',font='Calibri 12 bold')

eticheta1.pack()

root.mainloop()
