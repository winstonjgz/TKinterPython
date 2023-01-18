from tkinter import *

root =Tk()
root.title("Option Menu")
root.geometry('500x500')

value=StringVar()
value.set('Inteligencia')
drop = OptionMenu(root, value, 'Liderazgo', 'Sabiduria', 'Inteligencia')
drop.pack()


root.mainloop()
