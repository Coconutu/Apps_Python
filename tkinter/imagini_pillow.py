import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()
imagine_originala=Image.open('poster_interstelar.jpg')
imagine=ImageTk.PhotoImage(imagine_originala)
eticheta1 = tk.Label(root, text="Filmul meu preferat",
font="Calibri 12 bold")
eticheta1.pack()
cadru_cu_imagine=tk.Frame(root,padx=20,pady=20)
cadru_cu_imagine.pack()
etichete2=tk.Label(cadru_cu_imagine,image=imagine)
etichete2.pack()
root.mainloop()
