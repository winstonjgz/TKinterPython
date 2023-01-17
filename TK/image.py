from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title('Prueba Imagen')
root.geometry('400x400')

#imagen = Image.open('/TK/walk.jpg')
#imagen.show()

img = ImageTk.PhotoImage(Image.open('..\Tk inter\TK\walk.jpg'))
l = Label(image=img)
l.pack()



root.mainloop()
