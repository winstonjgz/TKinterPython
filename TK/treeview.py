from tkinter import *
from tkinter import ttk


root =Tk()
root.title("TreeView")
#root.geometry('600x400')

tree = ttk.Treeview(root)
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')

#tree.column('#0')
tree.column('#0', width=0, stretch=NO) # con esto desaparecemos el id del formulario 

tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

#tree.heading('#0', text='id')
tree.heading('#0')
tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')

tree.grid(column=0, row=0)

tree.insert('', END, 'Test1', values=('Uno', 'Dos', 'Tres'), text="Test01")
tree.insert('', END, 'Test2', values=('Uno1', 'Dos2', 'Tres3'), text="Test02")
tree.insert('Test2', END, 'Test3', values=('Uno11', 'Dos22', 'Tres33'), text="Test03")


root.mainloop()