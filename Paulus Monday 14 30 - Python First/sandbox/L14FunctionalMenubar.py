import tkinter as tk
import tkinter.messagebox as msgbox

counterlbl = 0
stringlbl = ""
counterbtn = 0
stringbtn = ""

def addlabel():
    global counterlbl
    counterlbl += 1
    global stringlbl
    stringlbl = "label" + str(counterlbl)


    stringlbl = tk.Label (window, text="This is label " + str(stringlbl))
    stringlbl.pack()

def editlabel():
    global stringlbl
    stringlbl.configure(text="Edited Label " + str(counterlbl))

def dellabel():
    global stringlbl
    stringlbl.destroy()


def addbutton():
    global counterbtn
    counterbtn += 1
    global stringbtn
    stringbtn = "Button" + str(counterbtn)

    stringbtn = tk.Button(window, text="This is button" + str(stringbtn))
    stringbtn.pack()

# window properties
window = tk.Tk();
window.title("Functional Menubar")
window.geometry("500x500")

menubar = tk.Menu(window)

menubar.add_command(label="Add Label", command=addlabel)
menubar.add_command(label="Edit Label", command=editlabel)
menubar.add_command(label="Delete Label", command=dellabel)

menubar.add_command(label="Add Button", command=addbutton)
menubar.add_command(label="Edit Button")
menubar.add_command(label="Delete Button")


window.config(menu = menubar)
window.mainloop()