from tkinter import *
import tkinter.ttk as ttk

# Initialize main windows
root = Tk()
menu = Menu(root)
root.config(menu=menu)

tree = ttk.Treeview(root)

# Open Input windows
def open_input_window():
    
    # Initialize windows
    input_window = Toplevel()
    input_window.title("enter link")

    # Label
    name_label = Label(input_window, text="Name")
    name_label.grid(row=0, column=0)
    link_label = Label(input_window, text="Zoom link")
    link_label.grid(row=1, column=0)

    # Text field
    name_input = Entry(input_window)
    name_input.grid(row=0, column=1)
    link_input = Entry(input_window)
    link_input.grid(row=1, column=1)
    
    # Temporary function
    def print_input():
        get_name = name_input.get()
        get_link = link_input.get()
        print(get_name, get_link)
    
    # Buttons to start the function
    button = Button(input_window, text="Add", command=print_input)
    button.grid(row=2, column=1)


# Initialize menu
filemenu=Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=open_input_window)

# Create tree column
tree["columns"] = ("name-column", "time-column", "auto-column")

# Formatting the tree column
tree.column("#0", width=0, stretch=NO)
tree.column("name-column", width=70, minwidth=30)
tree.column("time-column", width=50, minwidth=30)
tree.column("auto-column", width=50, minwidth=30)

# Add heading to each column
tree.heading("#0", text="", anchor=W)
tree.heading("name-column", text="name", anchor=W)
tree.heading("time-column", text="time", anchor=W)
tree.heading("auto-column", text="auto", anchor=W)

# Temporary data
data = [
    ["Chemistry", "12:45", "Yes" ],
    ["Math", "1:45", "Yes"],
    ["History", "10:00", "Yes"]
]
count=0

# Looping over the data and 
# add rows based on the data
for data in data:
    tree.insert(parent='', index='end', iid=count, text='', values=(data[0], data[1], data[2]))
    count += 1

# Putting tree column to windows
tree.pack(side=TOP, fill=X)
root.mainloop()