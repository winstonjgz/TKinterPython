from tkinter import *

root =Tk()
root.title("Radio Button")
root.geometry('400x400')

r = IntVar()
r.set('2')

Lista = [
    ('Sabiduria', 'Sabiduria'),
    ('Prosperidad', 'Prosperidad'),
    ('Inteligencia', 'Inteligencia'),
    ('Liderazgo', 'Liderazgo'),
    ('Comunicacion', 'Comunicacion'),
    
]

l1 = StringVar()
l1.set('Comunicacion')

for text, lista in Lista:
    Radiobutton(root, text=text, variable=l1, value=lista).pack()

l = Label(root, textvariable=l1)
l.pack()


root.mainloop()