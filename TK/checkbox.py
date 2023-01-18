from tkinter import *

root =Tk()
root.title("CheckBox")
root.geometry('500x500')

var = StringVar()
var.set('si')


def mostrar():
    l = Label(root, text=var.get())
    l.pack()


c = Checkbutton(root, text='Soy un CheckButton', variable = var, onvalue='si', offvalue='Otro valor' )
c.pack()



btn = Button(root, text='Click', command=mostrar).pack()



root.mainloop()
