from tkinter import *
import sqlite3


root =Tk()
root.title("Lista de tareas")
root.geometry('400x400')

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")

conn.commit()


def remove(id):
    def _remove():
        c.execute("DELETE FROM todo WHERE id = ?", (id, ))
        conn.commit()
        render_todos()
    return _remove
    

#Currying = retraso de ejecucion de una funcion
def complete(id):
    def _complete():
        todo = c.execute("SELECT * from todo WHERE id=?",(id, )).fetchone()
        c.execute("UPDATE todo SET completed = ? WHERE id = ?", (not todo[3], id))
        conn.commit()
        render_todos()
        #print(id)
    return _complete




def render_todos():
    rows = c.execute("SELECT * FROM todo").fetchall()
    #print(rows)
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(0, len(rows)):
        id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        color = 'grey' if completed else 'blue'
        ce = Checkbutton(frame, text=description, fg=color, width=42, anchor='w', command= complete(id))
        ce.grid(row=i, column=0, sticky='nswe')
        btn = Button(frame, text='Borrar', command=remove(id))
        btn.grid(row=i, column=1)
        ce.select() if completed else ce.deselect()



def addTodo():
    todo=e.get()
    if todo:
        c.execute("""
        INSERT INTO todo (description, completed) VALUES (?,?)
        """, (todo, False))
        conn.commit()
        e.delete(0, END)
        render_todos()
    else:
        pass

    

l = Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar', command=addTodo)
btn.grid(row=0, column=2)

frame = LabelFrame(root, text='Mis Tareas', padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)


e.focus()

root.bind('<Return>', lambda x: addTodo())
render_todos()

root.mainloop()