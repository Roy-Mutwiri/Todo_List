import sys
import tkinter as tk
from tkinter import *

root = Tk()
root.title("To-Do_List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []


# Kill command

def die():
    sys.exit()


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")

        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfie:
            for task in task_list:
                taskfie.write(task + "\n")

        listbox.delete(ANCHOR)


def openTaskFile():
    try:
        global task_list


        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open("tasklist.txt", "w")
        file.close()

# Focus Part
''''
with open("/home/anon/Documents/Python Code/Todo_List/tasklist.txt", "r") as file:
        todo_list = file.readlines()

last_task = todo_list[-1].strip()  # Get the last task and remove any leading/trailing whitespace
sentences = last_task.split(".")  # Split the last task into sentences
last_sentence = sentences[-1].strip()  # Get the last sentence and remove any leading/trailing whitespace

for task in todo_list:
    print(task)
'''

# Icon
Image_Icon = PhotoImage(file="/home/anon/Documents/Python Code/Todo_List/drive-download-20230516T165408Z-001/task.png")
root.iconphoto(False, Image_Icon)

# Top Bar
TopImage = PhotoImage(file="/home/anon/Documents/Python Code/Todo_List/drive-download-20230516T165408Z-001/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="/home/anon/Documents/Python Code/Todo_List/drive-download-20230516T165408Z-001/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="/home/anon/Documents/Python Code/Todo_List/drive-download-20230516T165408Z-001/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=30, y=25)

heading = Label(root, text="All Task", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Coffee Icon

coffee = PhotoImage(file="/home/anon/Documents/Python Code/Todo_List/pic.png")
Label(root, image=coffee, bg="#32405b").place(x=25, y=79)

# Main

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=28, font="calibri 12", bd=0)
task_entry.place(x=10, y=9)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="white", bd=0, command=addTask)
button.place(x=300, y=0)

# listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2",
                  selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
# Delete

Delete_icon = PhotoImage(
    file="/home/anon/Documents/Python Code/Todo_List/drive-download-20230516T165408Z-001/delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

# Add Exit Button

Ex = Button(root, text="Exit", activebackground="Red", bg="green", fg="white", command=die)
Ex.place(x=149, y=79)

root.mainloop()
