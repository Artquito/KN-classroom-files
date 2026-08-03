import tkinter as tk

def printselection():
    print(chkValue2.get())

window = tk.Tk()
window.title("Checkbox Example")
window.geometry("300x300")

check = tk.Checkbutton(window, text="choose Me")
check2 = tk.Checkbutton(window, text="Choose Me")
#check.select()
#check.deselect()
#check.toggle()
check.pack()
check2.pack()

chkValue = tk.BooleanVar()
chkValue.set(True)
check3 = tk.Checkbutton(window, text="I am selected using Variable", var = chkValue)
check3.pack()

chkValue2 = tk.StringVar()
chkValue2.set("True")
check4 = tk.Checkbutton(window, text="First", onvalue="First", offvalue="",var=chkValue2, command=printselection)
check4.pack()

window.mainloop()
