import tkinter as tk

window = tk.Tk()
window.title("Configuration of Grid Placement")
window.geometry("300x300")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

lbl1 = tk.Label(window, text="Label 1" , bg="lightgreen")
lbl2 = tk.Label(window, text="Label 2", bg="lightblue")
lbl3 = tk.Label(window, text="Label 3", bg="pink")
lbl4 = tk.Label(window, text="Label 4", bg="pink")

lbl1.grid(column=0, row=0, ipadx=30)
lbl2.grid(column=1, row=0, ipadx=30)
lbl3.grid(column=2, row=0, ipadx=30)
lbl4.grid(column=2, row=0, ipadx=30)

window.mainloop()