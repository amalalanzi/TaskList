
import tkinter
from tkinter import *

root = Tk()
root.title("TO-DO-LIST")
root.geometry("400x650+400+100")
root.resizable(False,False)


task_list= []
def show():
    lb=Label(root,text="Hello"+ entry_name.get(),  font=("Cndara",10))
    lb.place(x=230,y=120)

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("/Users/nez_1/Music/pro/mytasks.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("/Users/nez_1/Music/pro/mytasks.txt", 'w') as taskfie:
            for task in task_list:
                taskfie.write(task + "\n")
        listbox.delete( ANCHOR)


def openTaskFile():
    try:
        global task_list
        with open("/Users/nez_1/Music/pro/mytasks.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open("/Users/nez_1/Music/pro/mytasks.txt", 'w')
        file.close()
#icon
Image_icon = PhotoImage(file="C:\\Users\\nez_1\\Music\\pro\\task.png")
root.iconphoto(False,Image_icon)

#top bar
TopImage = PhotoImage(file="C:\\Users\\nez_1\\Music\\pro\\topbar.png")
Label(root,image=TopImage).pack()

dockImage =PhotoImage(file="C:\\Users\\nez_1\\Music\\pro\\dock.png")
Label(root,image=dockImage,bg="#32405b").place( x=30 , y=25)

noteImage = PhotoImage(file="C:\\Users\\nez_1\\Music\\pro\\task.png")
Label(root,image=noteImage,bg="#32405b").place( x=340 , y=25)

heading = Label(root,text="ALL TASK",font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=120, y=20)

name = Label(root,text="Enter Your Name:",font="arial 10 bold", fg="white", bg="#32405b")
name.place(x=20, y=90)
entry_name= Entry(root ,font=("Candara",13))
entry_name.insert(0,"  ")
entry_name.place(x=20,y=120)

b_submit = Button(root, text="SUBMIT",command=show,font="arial 10 bold", fg="white", bg="#32405b")
b_submit.place(x=20,y=150)

#main
frame =Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)
#to enter data
task= StringVar()
task_entry=Entry(frame,width=18,font="arial 20", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button= Button(frame,text="ADD", font="arial 20 bold", width=6,bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300,y=0)

#listbox
framel=Frame(root,bd=3,width=700, height=280, bg="#32405b")
framel.pack(pady=(160,0))

listbox=Listbox(framel,font=('arial',12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH , padx=2)
scrollbar =Scrollbar(framel)
scrollbar.pack(side=RIGHT , fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
Delete_icon = PhotoImage(file="C:\\Users\\nez_1\\Music\\pro\\delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask) .pack(side=BOTTOM, pady=13)



root.mainloop()


