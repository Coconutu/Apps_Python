import tkinter as tk
root=tk.Tk()
imagine=tk.PhotoImage(file='poster_interstelar.gif')
eticheta1 = tk.Label(root, text="Filmul meu preferat",
font="Calibri 12 bold")
eticheta1.pack()
cadru_cu_imagine=tk.Frame(root,padx=20,pady=20)
cadru_cu_imagine.pack()
etichete2=tk.Label(cadru_cu_imagine,image=imagine)
etichete2.pack()
root.mainloop()
