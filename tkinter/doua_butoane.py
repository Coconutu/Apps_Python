import tkinter as tk
root=tk.Tk()
def saluta(i):
    print('Butonul ',i," a fost apasat!")
buton1=tk.Button(root,text='Butonul1',command=lambda:saluta(1),relief='raised',bg='green',fg='white',activeforeground='magenta')
buton1.grid(row=0,column=0,padx=20,pady=20)
buton2=tk.Button(root,text='Buton2',command=lambda:saluta(2),relief='raised',bg='yellow',fg='red',activebackground='blue',activeforeground='white')
buton2.grid(row=0,column=1,padx=20,pady=20)
root.mainloop()