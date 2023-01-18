from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


root =Tk()
root.title("Libreta de Clientes")


conn = sqlite3.connect('libreta_clientes.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL,
        empresa TEXT NOT NULL
        
    );
""")

def render_clientes():
    rows= c.execute("SELECT * FROM clientes").fetchall()

    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert('', END, row[0], values=(row[1], row[2], row[3]))



def insertar(cliente):
    c.execute("""
        INSERT INTO clientes (nombre, telefono, empresa) VALUES (?,?,?)
        """, (cliente['nombre'], cliente['telefono'],cliente['empresa']))
    conn.commit()
    render_clientes()




def nuevo_cliente():
    def guardar():
        if not Nombre.get():
            messagebox.showerror("Error", 'El nombre es obligatorio')
            return 
        if not Telefono.get():
            messagebox.showerror("Error", 'El telefono es obligatorio')
            return 
        if not Empresa.get():
            messagebox.showerror("Error", 'La Empresa es obligatoria')
            return 

        cliente = {
            'nombre': Nombre.get(),
            'telefono': Telefono.get(),
            'empresa': Empresa.get()
            
        }
        insertar(cliente)
        top.destroy()
    
    top = Toplevel()
    top.title('Nuevo Cliente')

    lnombre = Label(top, text='Nombre')
    Nombre = Entry(top, width=40)
    lnombre.grid(row=0, column=0)
    Nombre.grid(row=0, column=1)

    lTelefono = Label(top, text='Telefono')
    Telefono = Entry(top, width=40)
    lTelefono.grid(row=1, column=0)
    Telefono.grid(row=1, column=1)

    lEmpresa = Label(top, text='Empresa')
    Empresa = Entry(top, width=40)
    lEmpresa.grid(row=2, column=0)
    Empresa.grid(row=2, column=1)

    guardar = Button(top, text='Guardar', command=guardar)
    guardar.grid(row=3, column=1)

    top.mainloop()




def eliminar_cliente():
    id = tree.selection()[0]
    
    cliente = c.execute("SELECT * FROM clientes WHERE id = ? ", (id,)).fetchone()
    respuesta = messagebox.askokcancel('Seguro?', 'Seguro quiere eliminar el cliente?' + cliente[1]+'?')
    if respuesta:
        c.execute('DELETE FROM clientes WHERE id = ?', (id,))
        conn.commit()
        render_clientes()
    else:
        pass



btn_new = Button(root, text='Nuevo Cliente', command=nuevo_cliente)
btn_new.grid(column=0, row=0, padx=5, pady=5)

btn_del = Button(root, text='Eliminar Cliente', command=eliminar_cliente)
btn_del.grid(column=1, row=0)

tree = ttk.Treeview(root)
tree['columns']=('Nombre', 'Telefono', 'Empresa')
tree.column('#0', width=0, stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')


tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')

tree.grid(column=0, row=1, columnspan=2)




render_clientes()
root.mainloop()