import tkinter as tk

window = tk.Tk()
frame = tk.Frame()

nameLabel = tk.Label(window, text="Name").grid( row=0, column= 0,  padx= 10, sticky="w")
nameEntry = tk.Entry(window)
nameEntry.grid(row=0, column= 1) 

window.mainloop()