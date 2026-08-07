import tkinter as tk

def update():
    label.config(text=entry.get())

window = tk.Tk()

entry = tk.Entry(window)
entry.pack(pady=10, padx=10)

label = tk.Label(window, text="This is a label")
label.pack(padx=8, anchor="w")

button = tk.Button(window, text="Update", command=update)
button.pack(padx=10, pady=10, anchor="w")

window.mainloop()