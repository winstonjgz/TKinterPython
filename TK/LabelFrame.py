from tkinter import *

root =Tk()
root.title('Prueba Frame')
root.geometry('400x400')

frame= LabelFrame(root, text='Login', padx=15, pady=10, borderwidth=10)
frame.pack(padx=25, pady=50)

l= Label(frame, text='Dentro del frame')
btn = Button(frame, text='Salir', command=root.quit)
l.pack()
btn.pack()


root.mainloop()


