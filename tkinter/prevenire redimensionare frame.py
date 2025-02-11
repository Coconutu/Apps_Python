import tkinter as tk
app=tk.Tk()
app.title('Prevenirea redimensionarii frame')
#un frame cu dimensiuni specificate
cadru=tk.Frame(app,width=200, height=100,bg='lightgray')
#prevenim redimensionarea frameului
#de care widgeturile interne
cadru.pack_propagate(False)
cadru.pack(padx=20,pady=20)
#adaugarea unei etichete in frame
eticheta=tk.Label(cadru,text="Eticheta in cadru")
eticheta.pack()
app.mainloop()