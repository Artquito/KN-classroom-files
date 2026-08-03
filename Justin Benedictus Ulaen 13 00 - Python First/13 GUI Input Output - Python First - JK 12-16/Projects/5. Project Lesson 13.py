import tkinter as tk
import tkinter.ttk as combobox
from tkinter import messagebox as mb

def sloganCreator():
    fname = fnameinput.get()
    fnameinput.delete(0, tk.END)
    lname = lnameinput.get()
    lnameinput.delete(0, tk.END)
    age = agespinner.get()
    gender = gendervar.get()
    gendervar.set(False)
    sloganpicked = slogan.get()
    slogan.set("")
    trait1picked = trait1var.get()
    trait2picked = trait2var.get()
    if trait1picked == "0" and trait2picked == "0":
        strtrait = "I have no particular trait"
    elif trait1picked == "0" and trait2picked != "0":
        strtrait = "I am " + trait2picked
    elif trait2picked == "0" and trait1picked != "0":
        strtrait = "I am " + trait1picked
    else:
        strtrait = "I am " + trait1picked + " and " + trait2picked
    trait1.deselect()
    trait2.deselect()
    reslbl.configure(text = "Hello, My name is " + fname + " " + lname +". I am "+ age + " years old." + " I am a "+ gender +". My Favorite Slogan is "+ sloganpicked + ". also " +strtrait)

def getText():
    inputText = fnameinput.get() + " : " + tArea.get("1.0",'end-1c')
    commentlbl.config(text=inputText)
        
window = tk.Tk()
window.title("Profile Creator")
window.geometry("1000x500")

lbl = tk.Label(window, text="Welcome to Profile Creator. With this program, we can create a profile for you based on your input.")
lbl2 = tk.Label(window, text="Please fill all the fields and press the button to create your slogan !")
fnamelbl = tk.Label(window, text="First Name")
lnamelbl = tk.Label(window, text="Last Name")
fnameinput = tk.Entry(window)
lnameinput = tk.Entry(window)
agelbl = tk.Label(window, text="Age")
agespinner = tk.Spinbox(window, from_ = 10, to = 30, width = 10, state="readonly")
genderlbl = tk.Label(window, text="Gender")
gendervar = tk.StringVar()
gendervar.set("False")
gender1 = tk.Radiobutton(window, text="Male", value="Male", var = gendervar)
gender2 = tk.Radiobutton(window, text="Female", value="Female", var = gendervar)
sloganlbl = tk.Label(window, text="Slogan")
slogan = combobox.Combobox(window, state = "readonly",width = 50,values=("A man chooses, a slave obeys","A thousand miles journey starts from one step", "Rome is not built in one day", "GET TO THE CHOPPAAAAAAAAAA!!!!"))
traitlbl = tk.Label(window, text="Traits (Can choose more than one)")
trait1var = tk.StringVar()
trait1var.set(False)
trait1 = tk.Checkbutton(window, onvalue="Prideful", text="Prideful", var = trait1var)
trait2var = tk.StringVar()
trait2var.set(False)
trait2 = tk.Checkbutton(window, onvalue="Strong-willed", text="Strong-Willed", var= trait2var)
resbtn = tk.Button(window, text="Click me for your Slogan !", command=sloganCreator)
reslbl = tk.Label(window, text="")
lblcmnt = tk.Label(window, text="Comment")
tArea = tk.Text(window, height=2, width=30)
tArea.insert(tk.END, "Type your comment here")
commentbtn = tk.Button(window, text="Post comment", command=getText)
commentlbl = tk.Label(window)

lbl.grid(row = 0 , column = 0, columnspan = 2)
lbl2.grid(row = 1, column = 0, columnspan = 2)
fnamelbl.grid(row = 2, column = 0, ipadx = 10)
lnamelbl.grid(row = 3, column = 0, ipadx = 10)
fnameinput.grid(row = 2 , column = 1, sticky = tk.W+tk.E)
lnameinput.grid(row = 3, column = 1, sticky = tk.W+tk.E)
agelbl.grid(row = 4, column = 0)
agespinner.grid(row = 4, column = 1)
genderlbl.grid(row = 5, column = 0)
gender1.grid(row = 5, column = 1)
gender2.grid(row = 5, column = 2)
sloganlbl.grid(row = 6 , column = 0)
slogan.grid(row = 6, column = 1)
traitlbl.grid(row = 7, column = 0)
trait1.grid(row = 7, column = 1)
trait2.grid(row = 7, column = 2)
resbtn.grid(row = 8, column = 0)
reslbl.grid(row = 9, column = 0, columnspan = 3)
lblcmnt.grid(row = 10, column = 0)
tArea.grid(row = 10, column = 1, sticky = tk.W+tk.E)
commentbtn.grid(row = 11, column = 1)
commentlbl.grid(row = 12, column = 1)

slogan.bind("<<ComboboxSelected>>", lambda x : lbl.focus())

window.mainloop()
