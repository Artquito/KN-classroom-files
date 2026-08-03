import tkinter as tk
import tkinter.messagebox as msgbox

def version():
    msgbox.showinfo("Version", "Current Version : 0.0")

window = tk.Tk()
window.title("Creating a menubar")
window.geometry("500x500")

menubar = tk.Menu(window)

filemenu=tk.Menu(menubar, tearoff= 0)
filemenu.add_command(label="Check Version", command=version)
filemenu.add_separator()
filemenu.add_command(label="Command 2")
filemenu.add_command(label="Command 2")
filemenu.add_command(label="Command 2")
menubar.add_cascade(label="File", menu= filemenu)


editmenu=tk.Menu(menubar)
editmenu.add_command(label="Command 1")
editmenu.add_command(label="Command 2")
editmenu.add_command(label="Command 3")
menubar.add_cascade(label="Edit", menu= editmenu)


window.config(menu = menubar)
window.mainloop()