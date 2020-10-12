from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import datetime

# Initialize main windows
root = Tk()
menu = Menu(root)
root.geometry("300x200")
root.config(menu=menu)

tree = ttk.Treeview(root)

# Open Input windows


def open_input_window():

    # Initialize windows
    input_window = Toplevel()
    input_window.title("enter link")
    input_window.geometry("200x200")


    # Label
    name_label = Label(input_window, text="Name")
    link_label = Label(input_window, text="Zoom link")
    time_label = Label(input_window, text="Time")

    # Put label into screen
    name_label.grid(row=0, column=0)
    link_label.grid(row=1, column=0)
    time_label.grid(row=2, column=0)


    # Entry field
    name_input = Entry(input_window)
    link_input = Entry(input_window)
    time_input = Entry(input_window)

    # Put entry field to screen
    name_input.grid(row=0, column=1)
    link_input.grid(row=1, column=1)
    time_input.grid(row=2, column=1)


    var1 = StringVar()
    checkbox = Checkbutton(input_window, text="auto launch",
                           variable=var1, onvalue="Yes", offvalue="No")
    checkbox.deselect()
    checkbox.grid(row=3, column=1)

    # Add user input to treeview
    def get_input():
        global count
        get_name = name_input.get()
        get_link = link_input.get()
        get_time = time_input.get()

        # Input validation
        if (get_name == "" or get_link == "" or get_time == ""):
            messagebox.showwarning("Warning", "Fields must not be empty!")
        elif (get_time != ""):
            try:
                convert_get_time = datetime.datetime.strptime(get_time, '%H:%M')
                tree.insert(parent='', index='end', iid=count, text='',
                            values=(get_name, convert_get_time, var1.get()))
                input_window.destroy()
            except ValueError:
                messagebox.showwarning("Warning", "Time field not valid!")
                 

    # Buttons to start the function
    button = Button(input_window, text="Add", command=get_input)
    button.grid(row=4, column=1)


# Initialize menu
filemenu = Menu(menu)
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
    ["Chemistry", "12:45", "Yes"],
    ["Math", "1:45", "Yes"],
    ["History", "10:00", "Yes"]
]
count = 0

# Looping over the data and
# add rows based on the data
for data in data:
    tree.insert(parent='', index='end', iid=count, text='',
                values=(data[0], data[1], data[2]))
    count += 1

# Putting tree column to windows
tree.pack(side=TOP, fill=X)
root.mainloop()
