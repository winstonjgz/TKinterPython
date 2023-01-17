from tkinter import *

root =Tk()
root.title('Prueba input')
root.geometry('400x400')

e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa texto: ")


def click():
    texto = e.get()
    l=Label(root, text=texto)
    l.pack()
    e.delete(0, END)



btn = Button(root, text="Captura", command=click)
btn.pack()





root.mainloop()