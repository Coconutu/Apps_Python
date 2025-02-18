import tkinter as tk
import winsound

def reda_sunetul():

    #reda un beep simplu
    winsound.MessageBeep(winsound.MB_ICONASTERISK)


root=tk.Tk()
buton_s=tk.Button(root,text="Genereaza sunet",command=reda_sunetul)
buton_s.pack()
root.mainloop()