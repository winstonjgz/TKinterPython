from tkinter import *

root =Tk()
root.title("Quit")
root.geometry('400x400')

exit = Button(root, text='Salir', command=root.quit)
exit.pack()

root.mainloop()
