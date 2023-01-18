from tkinter import *

root =Tk()
root.title("Radio Button")
root.geometry('400x400')

r = IntVar()
r.set('2')

Radiobutton(root, text='Opcion 1', variable=r, value=1).pack()

Radiobutton(root, text='Opcion 2', variable=r, value=2).pack()

l = Label(root, textvariable=r)
l.pack()


root.mainloop()