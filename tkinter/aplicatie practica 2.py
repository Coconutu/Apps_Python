import tkinter as tk
aplicatie=tk.Tk()
aplicatie.title("Exemplu de layout")
aplicatie.geometry("600x400")
#cadru pentru header
cadru_header=tk.Frame(aplicatie,height=90,bg='lightblue')
cadru_header.pack(fill='x')
cadru_header.pack_propagate(False)
label_header=tk.Label(cadru_header,text="Header",bg='lightblue')
label_header.pack(pady=10)
#cadrul central ce contine 3 coloane
cadru_central=tk.Frame(aplicatie)
cadru_central.pack(fill='both',expand=True)
colors=['lightgreen','lightyellow','lightcoral']
for color in colors:
    subcadru=tk.Frame(cadru_central,borderwidth=5,relief='ridge')
    subcadru.pack(side='left',expand=True,padx=5,fill='both')
    label=tk.Label(subcadru,text="33%",bg=color)
    label.pack(Expand=True)
#cadru pentru footer
cadru_footer=tk.Frame(aplicatie,height=60,bg='lightgray')
cadru_footer.pack(fill="x",side='bottom')
cadru_footer.pack_propagate(False)
label_footer=tk.Label(cadru_footer,text="Footer",bg='lightgray')
label_footer.pack(pady=10)
aplicatie.mainloop()

aplicatie.mainloop()