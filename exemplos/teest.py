from tkinter import * 
from tkinter import messagebox
root = Tk()
root.title('BST')
root.configure(bg='lightblue')
root.minsize(400,500)
root.maxsize(800,900)

def show_tree():
    pass

def insert_node():
    try:
        val = int(value_entry.get())
        if val < 0:
            raise ValueError
        messagebox.showinfo('Message',f'O número {val} foi inserido com sucesso')    
    except:
        messagebox.showwarning('ERRO','valor inválido')                       

def press_enter(event):
    insert_button.invoke()


main_window = Frame(root)


value_entry = Entry(root)
label_value = Label(root,text='Insira um valor: ',bg='lightblue',font=('Arial',12))

insert_button = Button(root, text="Insert", command= insert_node,bg='lightgreen')
value_entry.bind('<Return>',press_enter)
insert_button.place(relx=0.75,rely=0.001)
value_entry.place(relx=0.4,rely=0.01)
label_value.place(relx=0.1,rely=0.01)


root.mainloop()
