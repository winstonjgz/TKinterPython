from tkinter import *

root =Tk()
root.title('Hola mundo')
root.geometry('400x400') #Indica el diamtro de la ventana ancho x alto

#Esto con variables
#label = Label(root, text='Hola mi primer TKinter') 
#label.pack()

#esto con OOP
label = Label(root, text='Hola mi primer TKinter').pack

root.mainloop() #Importante siempre mantener el main loop para que se actulicen los cambios
