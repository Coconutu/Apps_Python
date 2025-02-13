import tkinter as tk
root=tk.Tk()
root.geometry("500x200")
#eticheta cu text simplu
label1=tk.Label(root,text='Eticheta simplă')
label1.pack()
#eticheta cu text ingrosat si culoare de fundal
label2=tk.Label(root,text='Eticheta cu text ingrosat si culoare de fundal',font=('Arial',12,'bold'),bg='yellow',relief='sunken')
label2.pack()
#eticheta cu text italic si culoare a textului
label3=tk.Label(root,text='Eticheta cu text italic si culoare a textului',font=('Helvetica',12,'italic'),fg='red',relief='raised',wraplength=200)
label3.pack()
root.mainloop()