from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import datetime
import threading
import pyautogui
import subprocess
import webbrowser
import logging
import ctypes
import cv2
import time
import sys
import re
import os

# Initialize main windows
root = Tk()
root.title("zoom_launcher")
menu = Menu(root)
root.geometry("500x400")
root.config(menu=menu)

# Logging config
logging.basicConfig(level=logging.INFO, filename='image_location.log',
                    format='%(asctime)s:%(message)s')

# Treeview
tree = ttk.Treeview(root, height=36)
tree_style = ttk.Style(root)
tree_style.configure('Treeview', rowheight=25)

"""Functions"""
# Open Input windows if user add by link


def open_input_link_window():

    # Initialize windows
    input_window = Toplevel()
    input_window.title("enter link")
    input_window.geometry("400x400")

    # Label
    day_label = Label(input_window, text="Day")
    name_label = Label(input_window, text="Name")
    link_label = Label(input_window, text="Zoom link")
    time_label = Label(input_window, text="Time")

    # Put label into screen
    day_label.grid(row=0, column=0, pady=2)
    name_label.grid(row=1, column=0, pady=2)
    link_label.grid(row=2, column=0, pady=2)
    time_label.grid(row=3, column=0, pady=2)

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
    auto_input = Checkbutton(input_window, text="Auto Launch",
                             variable=checkbox_var, onvalue="Yes", offvalue="No").deselect()

    # Put entry field to screen
    day_input.grid(row=0, column=1)
    name_input.grid(row=1, column=1)
    link_input.grid(row=2, column=1)
    time_input.grid(row=3, column=1)
    auto_input.grid(row=4, column=1)

    # Add user input to treeview
    def get_input():
        global count
        global data

        get_day = dropdown_var.get()
        get_name = name_input.get()
        get_link = link_input.get()
        get_time = time_input.get()
        get_auto = checkbox_var.get()
        get_method = "Link"

        # Input validation
        # If entry field is empty, show warning box
        if (get_name == "" or get_link == "" or get_time == ""):
            messagebox.showwarning("Warning", "Fields must not be empty!")
        # Check if time field value is 24 hour format
        elif (get_time != "" and get_day != ""):
            try:
                convert_get_time = datetime.datetime.strptime(
                    get_time, '%H:%M').time()

                tree.insert(parent='', index='end', iid=count, text='',
                            values=(get_day, get_name, get_time, "Yes", get_method))

                with open('save.txt', 'a') as file:
                    file.write(get_day+","+get_name+","+get_time +
                               ","+get_auto+","+get_method+","+get_link+"\n")
                    count += 1

                input_window.destroy()
            except ValueError:
                messagebox.showwarning("Warning", "Time field not valid!")

    # Buttons to start the function
    button = Button(input_window, text="Add", command=get_input)
    button.grid(row=5, column=1)
# Input windows by meeting ID


def open_input_id_window():

    # Initialize windows
    input_window = Toplevel()
    input_window.title("enter link")
    input_window.geometry("400x400")

    # Label
    day_label = Label(input_window, text="Day")
    name_label = Label(input_window, text="Name")
    id_label = Label(input_window, text="Meeting ID")
    pass_label = Label(input_window, text="Password")
    time_label = Label(input_window, text="Time")

    # Put label into screen
    day_label.grid(row=0, column=0, pady=2)
    name_label.grid(row=1, column=0, pady=2)
    id_label.grid(row=2, column=0, pady=2)
    pass_label.grid(row=3, column=0, pady=2)
    time_label.grid(row=4, column=0, pady=2)

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
    auto_input = Checkbutton(input_window, text="Auto Launch",
                             variable=checkbox_var, onvalue="Yes", offvalue="No")
    auto_input.deselect()

    # Put entry field to screen
    day_input.grid(row=0, column=1)
    name_input.grid(row=1, column=1)
    id_input.grid(row=2, column=1)
    pass_input.grid(row=3, column=1)
    time_input.grid(row=4, column=1)
    auto_input.grid(row=5, column=1)

    # Add user input to treeview
    def get_input():
        global count
        global data

        get_day = dropdown_var.get()
        get_name = name_input.get()
        get_id = id_input.get()
        get_pass = pass_input.get()
        get_time = time_input.get()
        get_auto = checkbox_var.get()
        get_method = "Meeting ID"

        # Input validation
        # If entry field is empty, show warning box
        if (get_name == "" or get_id == "" or get_pass == "" or get_time == ""):
            messagebox.showwarning("Warning", "Fields must not be empty!")
        # Check if time field value is 24 hour format
        elif (get_time != ""):
            try:
                convert_get_time = datetime.datetime.strptime(
                    get_time, '%H:%M').time()

                tree.insert(parent='', index='end', iid=count, text='',
                            values=(get_day, get_name, get_time, "Yes", get_method))

                with open('save.txt', 'a') as file:
                    file.write(get_day+","+get_name+","+get_time+"," +
                               get_auto+","+get_method+","+get_id+","+get_pass+"\n")
                    count += 1

                input_window.destroy()
            except ValueError:
                messagebox.showwarning("Warning", "Time field not valid!")

    # Buttons to start the function
    button = Button(input_window, text="Add", command=get_input)
    button.grid(row=6, column=1)


def quit_window():
    root.quit()

# Click function


class Click:
    def __init__(self, location):
        self.location = pyautogui.locateCenterOnScreen(
            location, confidence=0.7)
        logging.info(f"Join meeting btn coordinates: {self.location}")
        if self.location == None:
            os.system(f"TASKKILL /F /IM {zoom_path}")
            time.sleep(1)
            subprocess.run(zoom_path)
            time.sleep(1)
            self.location = pyautogui.locateCenterOnScreen(
                location, confidence=0.7)
            self.click = pyautogui.click(self.location)
            logging.info(
                f"Join meeting btn coordinates after None: {self.location}")
        else:
            self.click = pyautogui.click(self.location)


def manual_launch():
    try:
        i = tree.selection()[0]
        if data[int(i)][4] == "Link":
            webbrowser.open(data[int(i)][5])
        elif data[int(i)][4] == "Meeting ID":
            try:
                # Open Zoom
                subprocess.run(zoom_path)
                time.sleep(5)
                # Locate the center of the join button then move the cursor
                Click('./doNotDelete/join_button.png')
                time.sleep(3)
                # Write the meeting id to the text field
                pyautogui.write(data[int(i)][5])
                # Press the enter key
                pyautogui.press('enter')
                time.sleep(3)
                # Write the passcode to the text field
                pyautogui.write(data[int(i)][6])
                # Press the enter key
                pyautogui.press('enter')
            except OSError:
                messagebox.showerror(
                    "Zoom Path Missing", "Your zoom path is missing, please fill your zoom.exe path to zoom_path.txt")
    except IndexError:
        messagebox.showwarning(
            "No columns selected", "Please select a column that you want to launch before hitting the launch button")


# Function to automate zoom launch
def auto_launch():
    try:
        for record in data:
            # Datetime and auto validation for web automation
            while True:
                convert_time_record = datetime.datetime.strptime(
                    record[2], '%H:%M').time()
                date_now = datetime.datetime.now()
                if record[0] == date_now.strftime('%A'):
                    if record[3] == "Yes":
                        if convert_time_record.strftime('%H:%M:%S') == date_now.strftime('%H:%M:%S') and record[4] == "Link":
                            webbrowser.open(record[5])
                            break
                        # Check if the method was by meeting ID
                        elif convert_time_record.strftime('%H:%M:%S') == date_now.strftime('%H:%M:%S') and record[4] == "Meeting ID":
                            try:
                                # Open Zoom
                                subprocess.Popen(zoom_path)
                                time.sleep(3)
                                # Locate the center of the join button then move the cursor
                                Click('./doNotDelete/join_button.png')
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
                                break
                            except OSError:
                                messagebox.showerror(
                                    "Zoom Path Missing", "Your zoom path is missing, please fill your zoom.exe path to zoom_path.txt")
                                root.quit()
                        # If current time is less than the time input
                        elif date_now.strftime('%H:%M:%S') < convert_time_record.strftime('%H:%M:%S'):
                            # Update label
                            up_next_label.config(text=f'Up next: {record[1]}')
                            # Prevent sleep mode when program is running
                            ctypes.windll.kernel32.SetThreadExecutionState(
                                0x80000002)
                        # If current time is greater than the time input, Skip to the next list
                        elif date_now.strftime('%H:%M:%S') > convert_time_record.strftime('%H:%M:%S'):
                            break
                    else:
                        break
                else:
                    break
                time.sleep(1)
        else:
            up_next_label.config(text='Up next: None')
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    except IndexError:
        pass


file_last_edited = None


# Check text file size. If text file is changed,
# restart the app
def check_file_changes():
    while True:
        try:
            file_name = "save.txt"
            file_stats = os.stat(file_name)
            if(file_stats.st_mtime != file_last_edited):
                python = sys.executable
                os.execl(python, python, * sys.argv)
                break
        except FileNotFoundError:
            time.sleep(1)
            pass
        time.sleep(1)


"""Root content"""
data = []
count = len(data)

# Open text file
try:
    with open('save.txt', 'r') as file:
        file_name = "save.txt"
        file_stats = os.stat(file_name)
        file_last_edited = file_stats.st_mtime
        # Check every line inside the file
        for line in file:
            stripped_line = line.strip()  # Remove space in each line
            # Split into list based on , and \n
            splitted_line = re.split('\n |,', stripped_line)
            data.append(splitted_line)  # Add splitted line to data list

        # Check the content of each list inside a data list
        # and insert it to treeview
        for record in data:
            # If there is a content inside the record list
            # then insert the list to treeview
            if(len(record) > 1):
                tree.insert(parent='', index='end', iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4]))
                count += 1
            # Else if the content of the record is empty or ['']
            # Delete the empty record
            elif(len(record) < 1):
                tree.delete(record)
except FileNotFoundError:
    with open('save.txt', 'w'):
        pass

# Open zoom_path.txt file
try:
    with open('zoom_path.txt', 'r') as path_file:
        global zoom_path
        split_line = path_file.read().split('=')
        zoom_path = split_line[1]
        if (zoom_path == None or zoom_path == ""):
            messagebox.showwarning(
                "Zoom path is missing", "Your zoom path is missing, please put your zoom path in zoom_path.txt file")
except FileNotFoundError:
    with open('zoom_path.txt', 'w') as path_file:
        path_file.write('YOUR_ZOOM_PATH=')

# Initialize menu
filemenu = Menu(menu)
menu.add_cascade(label="Add", menu=filemenu)
filemenu.add_command(label="Add by link", command=open_input_link_window)
filemenu.add_command(label="Add by ID", command=open_input_id_window)
filemenu.add_separator()
filemenu.add_command(label="exit", command=quit_window)

# Create tree column
tree["columns"] = ("day-column", "name-column",
                   "time-column", "auto-column", "method-column")

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

# Upnext laben and manual launch button
up_next_label = Label(root, text="Up next: None")
launch_button = Button(root, text="Launch", command=manual_launch)

up_next_label.pack(padx=5)
launch_button.pack(padx=5, pady=5)
# Putting tree column to windows
tree.pack(fill=BOTH)

auto_launch_thread = threading.Thread(target=auto_launch)
check_file_thread = threading.Thread(target=check_file_changes)

auto_launch_thread.daemon = True
check_file_thread.daemon = True

# Start threading

auto_launch_thread.start()
check_file_thread.start()

root.mainloop()
