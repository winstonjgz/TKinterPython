from tkinter import *

root =Tk()
root.title("Prueba")
root.geometry('400x400')

l=Label(root, text='Esto es una prueba')
def click():
#l=Label(root, text='Esto es una prueba') asi se sique cargando cada vez que se clickee

    l.pack()


    

btn = Button(root, text="Prueba", command=click, fg="green", bg='yellow').pack()

root.mainloop()

