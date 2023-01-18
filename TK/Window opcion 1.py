from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title("Ventanas")
root.geometry('400x400')

def open():
    img = ImageTk.PhotoImage(Image.open('../TK Inter/TK/Imagenes/nature.jpg'))
    top = Toplevel()
    top.title('Nueva Ventana')
    l = Label(top, text='Segunda Ventana')
    l2 = Label(top, image=img)
    l2.pack()
    l.pack()
    top.mainloop()




btn = Button(root, text='Click', command=open).pack()




root.mainloop()