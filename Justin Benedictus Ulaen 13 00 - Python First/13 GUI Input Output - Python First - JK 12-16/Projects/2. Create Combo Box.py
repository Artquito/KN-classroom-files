import tkinter as tk
import tkinter.ttk
#from tkinter import ttk --> another way to import

def printsel():
    lbl.configure(text=combo.get())

window = tk.Tk()
window.title("Creating a combobox")
window.geometry("300x300")

combo = tkinter.ttk.Combobox(window, width=20)
combo["values"] = ("item_1", "item_2", "item_3", "item_4")
combo.current(0) # setting the current value of the combobox
btn = tk.Button(window, text="Click me to print the selection", command = printsel)
combo["values"] = combo["values"] + ("item_5",) # adding new item to the combobox
lbl = tk.Label(window, text="")

# shifting focus to another element so the combobox won't highlighted
# Lambda is a way to make function without defining a function
combo.bind("<<ComboboxSelected>>", lambda x : lbl.focus())
combo2 = tkinter.ttk.Combobox(window, values=("item1", "item2", "item3"), state="readonly")
combo3 = tkinter.ttk.Combobox(window, values=("item1","item2","item3"), state="disabled")


combo.pack()
btn.pack()
lbl.pack()
combo2.pack()
combo3.pack()

window.mainloop()
