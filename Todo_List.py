import tkinter
from tkinter import *

root = Tk()
root.title("To-Do_List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

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

# Main

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="white", bd=0)
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

# Delete

Delete_icon = PhotoImage(
    file="/home/anon/Documents/Python Code/Todo_List/drive-download-20230516T165408Z-001/delete.png")
Button(root, image=Delete_icon, bd=0).pack(side=BOTTOM, pady=13)

root.mainloop()
