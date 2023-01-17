from tkinter import *

root =Tk()
root.title('Prueba input')
root.geometry('400x400')

e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa texto: ")


def click():
    texto = e.get()
    l.configure(text=texto)



btn = Button(root, text="Captura", command=click)
btn.pack()

l = Label(root, text='Capturado el texto')
l.pack()





root.mainloop()