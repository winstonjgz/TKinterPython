from tkinter import *
from tkinter import messagebox

root =Tk()
root.title("Message Box")
root.geometry('400x400')

def click():
    messagebox.showwarning('Alerta', "Esta es una prueba de MsgBox")



exit = Button(root, text='Presioname', command=click)
exit.pack()

root.mainloop()