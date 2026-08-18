import tkinter as tk

window = tk.Tk()
window.geometry("300x300")

frame = tk.Frame(window)
frame.pack(fill="both", expand=True, ipady=10)
frame2 = tk.Frame(window)
frame2.pack(fill="both", expand=True, ipady=10)

lbl = tk.Label(frame, text="Label 1")
lbl.pack(side="right")
lbl2 = tk.Label(frame, text="Label 2")
lbl2.pack(side="right")
lbl3 = tk.Label(frame2, text="Label 3")
lbl3.grid(column=0, row=0)

window.mainloop()