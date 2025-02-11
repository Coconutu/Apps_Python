import tkinter as tk
aplicatie=tk.Tk()
#un camp de text pe linia 0, coloana 0
entry=tk.Entry(aplicatie)
entry.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
#un buton pe linia 1, coloana 0
button1=tk.Button(aplicatie,text="Buton 1")
button1.grid(row=1,column=0,padx=10,pady=10)
#alt buton pe linia 1, coloana 1
button2=tk.Button(aplicatie,text="Buton 2")
button2.grid(row=1,column=1,padx=10,pady=10)
aplicatie.mainloop()