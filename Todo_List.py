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


root.mainloop()
