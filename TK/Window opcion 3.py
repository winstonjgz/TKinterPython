from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title("Ventanas")
root.geometry('400x400')

def open(img):
   
    top = Toplevel()
    top.title('Nueva Ventana')
    l = Label(top, text='Segunda Ventana')
    l2 = Label(top, image=img)
    l2.pack()
    l.pack()

img = ImageTk.PhotoImage(Image.open('../TK Inter/TK/Imagenes/nature.jpg'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()
root.mainloop()