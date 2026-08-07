import tkinter as tk


def update():
    label.config(text=entryValue.get())

window = tk.Tk()



entryValue = tk.StringVar()
entry = tk.Entry(window, textvariable=entryValue)
entry.pack(pady=10, padx=10)

label = tk.Label(window, text="This is a label")
label.pack(padx=8, anchor="w")

button = tk.Button(window, text="Update", command=update)
button.pack(padx=10, pady=10, anchor="w")

window.mainloop()