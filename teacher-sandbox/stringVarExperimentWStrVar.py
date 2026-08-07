import tkinter as tk

window = tk.Tk()
window.title = "StringVar Experiment"

entryValue = tk.StringVar()

entry = tk.Entry(textvariable=entryValue).pack(padx=(10, 50), pady=10)

label = tk.Label(window, textvariable=entryValue)
label.pack(padx=(8, 50), pady=(0, 10), anchor="w")

window.mainloop()