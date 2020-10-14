from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import datetime
import re
import time
import pyautogui
import subprocess
# Initialize main windows
root = Tk()
menu = Menu(root)
root.geometry("300x200")
root.config(menu=menu)

tree = ttk.Treeview(root)

# Open Input windows
def open_input_link_window():

    # Initialize windows
    input_window = Toplevel()
    input_window.title("enter link")
    input_window.geometry("200x200")


    # Label
    day_label = Label(input_window, text="Day")
    name_label = Label(input_window, text="Name")
    link_label = Label(input_window, text="Zoom link")
    time_label = Label(input_window, text="Time")

    # Put label into screen
    day_label.grid(row=0, column=0)
    name_label.grid(row=1, column=0)
    link_label.grid(row=2, column=0)
    time_label.grid(row=3, column=0)

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    checkbox_var = StringVar()
    dropdown_var = StringVar()
    dropdown_var.set("Monday")

    # Entry field
    day_input = OptionMenu(input_window, dropdown_var, *days)
    name_input = Entry(input_window)
    link_input = Entry(input_window)
    time_input = Entry(input_window)
    checkbox = Checkbutton(input_window, text="auto launch",
                           variable=checkbox_var, onvalue="Yes", offvalue="No")

    # Deselect checkbox
    checkbox.deselect()

    # Put entry field to screen
    day_input.grid(row=0, column=1)
    name_input.grid(row=1, column=1)
    link_input.grid(row=2, column=1)
    time_input.grid(row=3, column=1)
    checkbox.grid(row=4, column=1)

    # Add user input to treeview
    def get_input():
        global count
        global data

        get_day = dropdown_var.get()
        get_name = name_input.get()
        get_link = link_input.get()
        get_time = time_input.get()
        get_check = checkbox_var.get()
        get_method = "Link"

        # Input validation
        # If entry field is empty, show warning box
        if (get_name == "" or get_link == "" or get_time == ""):
            messagebox.showwarning("Warning", "Fields must not be empty!")
        # Check if time field value is 24 hour format
        elif (get_time != "" and get_day != ""):
            try:
                convert_get_time = datetime.datetime.strptime(get_time, '%H:%M').time()

                tree.insert(parent='', index='end', iid=count, text='',
                            values=(get_day, get_name, get_time, get_check, get_method))

                with open('save.txt', 'a') as file:
                    file.write(get_day+","+get_name+","+get_time+","+get_check+","+get_method+","+get_link+"\n")
                    count += 1

                input_window.destroy()
            except ValueError:
                messagebox.showwarning("Warning", "Time field not valid!")
 

    # Buttons to start the function
    button = Button(input_window, text="Add", command=get_input)
    button.grid(row=5, column=1)

def open_input_id_window():

    # Initialize windows
    input_window = Toplevel()
    input_window.title("enter link")
    input_window.geometry("200x200")


    # Label
    day_label = Label(input_window, text="Day")
    name_label = Label(input_window, text="Name")
    id_label = Label(input_window, text="Meeting ID")
    pass_label = Label(input_window, text="Password")
    time_label = Label(input_window, text="Time")

    # Put label into screen
    day_label.grid(row=0, column=0)
    name_label.grid(row=1, column=0)
    id_label.grid(row=2, column=0)
    pass_label.grid(row=3, column=0)
    time_label.grid(row=4, column=0)

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    checkbox_var = StringVar()
    dropdown_var = StringVar()
    dropdown_var.set("Monday")

    # Entry field
    day_input = OptionMenu(input_window, dropdown_var, *days)
    name_input = Entry(input_window)
    id_input = Entry(input_window)
    pass_input = Entry(input_window)
    time_input = Entry(input_window)
    checkbox = Checkbutton(input_window, text="auto launch",
                           variable=checkbox_var, onvalue="Yes", offvalue="No")

    # Deselect checkbox
    checkbox.deselect()

    # Put entry field to screen
    day_input.grid(row=0, column=1)
    name_input.grid(row=1, column=1)
    id_input.grid(row=2, column=1)
    pass_input.grid(row=3, column=1)
    time_input.grid(row=4, column=1)
    checkbox.grid(row=5, column=1)

    # Add user input to treeview
    def get_input():
        global count
        global data

        get_day = dropdown_var.get()
        get_name = name_input.get()
        get_id = id_input.get()
        get_pass = pass_input.get()
        get_time = time_input.get()
        get_check = checkbox_var.get()
        get_method = "Meeting ID"

        # Input validation
        # If entry field is empty, show warning box
        if (get_name == "" or get_id == "" or get_pass == "" or get_time == ""):
            messagebox.showwarning("Warning", "Fields must not be empty!")
        # Check if time field value is 24 hour format
        elif (get_time != "" and get_day != ""):
            try:
                convert_get_time = datetime.datetime.strptime(get_time, '%H:%M').time()

                tree.insert(parent='', index='end', iid=count, text='',
                            values=(get_day, get_name, get_time, get_check, get_method))

                with open('save.txt', 'a') as file:
                    file.write(get_day+","+get_name+","+get_time+","+get_check+","+get_method+","+get_id+","+get_pass+"\n")
                    count += 1

                input_window.destroy()
            except ValueError:
                messagebox.showwarning("Warning", "Time field not valid!")
 

    # Buttons to start the function
    button = Button(input_window, text="Add", command=get_input)
    button.grid(row=6, column=1)


# Initialize menu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Add by link", command=open_input_link_window)
filemenu.add_command(label="Add by ID", command=open_input_id_window)

# Create tree column
tree["columns"] = ("day-column","name-column", "time-column", "auto-column", "method-column")

# Formatting the tree column
tree.column("#0", width=0, stretch=NO)
tree.column("day-column", width=70, minwidth=30)
tree.column("name-column", width=70, minwidth=30)
tree.column("time-column", width=50, minwidth=30)
tree.column("auto-column", width=50, minwidth=30)
tree.column("method-column", width=70, minwidth=30)

# Add heading to each column
tree.heading("#0", text="", anchor=W)
tree.heading("day-column", text="day", anchor=W)
tree.heading("name-column", text="name", anchor=W)
tree.heading("time-column", text="time", anchor=W)
tree.heading("auto-column", text="auto", anchor=W)
tree.heading("method-column", text="method", anchor=W)

data = []
count = len(data)
# Open text file
with open('save.txt', 'r') as file:
    # Check every line inside the file
    for line in file:
        stripped_line = line.strip() # Remove space in each line
        splitted_line = re.split('\n |,', stripped_line) # Split into list based on , and \n
        data.append(splitted_line) # Add splitted line to data list
    
    # Check the content of each list inside a data list
    # and insert it to treeview
    for record in data:
        # If there is a content inside the record list
        # then insert the list to treeview 
        if(len(record) > 1):
            tree.insert(parent='', index='end', iid=count, text='',
                        values=(record[0], record[1], record[2], record[3], record[4]))
            count += 1
            convert_time_record = datetime.datetime.strptime(record[2], '%H:%M').time()
            date_now = datetime.datetime.now()
            # Datetime and auto validation for web automation 
            if(record[0] == date_now.strftime('%A') and convert_time_record == date_now.strftime('%H:%M:%S') and record[3] == "Yes" and record[4] == "Link"):
                driver = webdriver.Chrome()
                driver.get(record[5])
                try:
                    element = WebDriverWait(driver, 15).until(
                        ec.presence_of_element_located((By.CLASS_NAME, "_3Gj8x8oc"))
                    )
                    element.click()
                    time.sleep(2)
                    pyautogui.click('open_zoom_web.png')
                finally:
                    driver.close()
            # Check if the method was by meeting ID
            elif(record[0] == date_now.strftime('%A') and convert_time_record == date_now.strftime('%H:%M:%S') and record[3] == "Yes" and record[4] == "Meeting ID"):
                # Open Zoom 
                subprocess.Popen([r'C:\Users\bryan\Desktop\Zoom.Ink'])
                time.sleep(3)
                # Locate the center of the join button then move the cursor
                join_button = pyautogui.locateCenterOnScreen('join_button.png')
                # Move the cursor to the location
                pyautogui.moveTo(join_button)
                # Click the button
                pyautogui.click()
                time.sleep(3)
                # Write the meeting id to the text field
                pyautogui.write(record[5])
                # Press the enter key
                pyautogui.press('enter')
                time.sleep(3)
                # Write the passcode to the text field
                pyautogui.write(record[6])
                # Press the enter key
                pyautogui.press('enter')
                
        # Else if the content of the record is empty or ['']
        # Delete the empty record
        elif(len(record) < 1):
            tree.delete(record)


# Putting tree column to windows
tree.pack(side=TOP, fill=X)
root.mainloop()
