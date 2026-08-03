import tkinter as tk
import tkinter.messagebox as msgbox

window = tk.Tk()
window.title("Creating a menubar")
window.geometry("500x500")

menubar = tk.Menu(window)

filemenu=tk.Menu(menubar, tearoff= 0)
filemenu.add_command(label="Add Lable")
filemenu.add_separator()
filemenu.add_command(label="")
filemenu.add_separator()
filemenu.add_command(label="Command 2")
filemenu.add_command(label="Command 2")
menubar.add_cascade(label="Lable", menu= filemenu)


window.config(menu = menubar)
window.mainloop()