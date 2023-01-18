from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root =Tk()
root.title("Archivos")
root.geometry('400x400')

def open():
    global ImageTk
    root.filename = filedialog.askopenfilename(title='Elige una foto', filetypes=(("Archivos PNG", "*.png"), ('Todos', '*')))
    l= Label(text=root.filename)
    l.pack

    img = Image.open(root.filename)
    ImageTk = ImageTk.PhotoImage(img)

    l2 = Label(root, image=ImageTk)
    l2.pack()


btn= Button(root, text='Cargar imagen', command=open).pack()

root.mainloop()