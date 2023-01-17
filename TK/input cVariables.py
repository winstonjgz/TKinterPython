from tkinter import *

root =Tk()
root.title('Prueba input')
root.geometry('400x400')

e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa texto: ")


def click():
    texto = e.get()
    textVariable.set(texto)

    e.delete(0, END)



btn = Button(root, text='click', command=click  )
btn.pack()

textVariable = StringVar()
l=Label(root, textvariable=textVariable)
l.pack()


root.mainloop()