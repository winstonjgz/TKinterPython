from tkinter import *

root =Tk()
root.title("Option Menu")
root.geometry('500x500')


def  enviar():
    l = Label(root, text=value.get())
    l.pack()



lista=[
    ('Liderazgo'), 
    ('Sabiduria'),
    ('Inteligencia')
]


value=StringVar()
value.set(lista[0])

drop = OptionMenu(root, value, *lista)
drop.pack()

btn= Button(root, text='Enviar', command=enviar).pack()

root.mainloop()
