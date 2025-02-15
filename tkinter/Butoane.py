import tkinter as tk
root = tk.Tk()
imagine=tk.PhotoImage(file='imagine_iconita.png')
def functia_mea():
    print("Butonul a fost apăsat!")
buton = tk.Button(root, text="Apasă-mă",command=functia_mea,activebackground='red',activeforeground='blue',borderwidth=3,relief='raised',
                  padx=20,pady=10,image=imagine,compound='top')
buton.pack()
root.mainloop()