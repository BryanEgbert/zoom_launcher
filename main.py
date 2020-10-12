from tkinter import *

root = Tk()
menu = Menu(root)
root.config(menu=menu)

def open_input_window():

    input_window = Toplevel()
    input_window.title("enter link")

    name_label = Label(input_window, text="Name")
    name_label.grid(row=0, column=0)
    link_label = Label(input_window, text="Zoom link")
    link_label.grid(row=1, column=0)

    name_input = Entry(input_window)
    name_input.grid(row=0, column=1)
    link_input = Entry(input_window)
    link_input.grid(row=1, column=1)
    
    def print_input():
        get_name = name_input.get()
        get_link = link_input.get()
        print(get_name, get_link)
    button = Button(input_window, text="Add", command=print_input)
    button.grid(row=2, column=1)


filemenu=Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=open_input_window)
add=Button(root, text="Add")

root.mainloop()