import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("Pack Placement")

# pack placement and grid placement
lbl = tk.Label(window, text="This is a label", foreground="indigo", background="salmon")
lbl.pack()

lbl2 = tk.Label(window, text="This is also a lable", fg="pink", bg="yellow")
lbl2.pack(fill=tk.X)

lbl3 = tk.Label(window, text="This is a label with external padding added", bg="white")
lbl3.pack(pady = (10, 50), padx=10)

lbl4 = tk.Label(window, text="This is a label with internal padding added", bg="green")
lbl4.pack(ipadx=10, ipady=10)

lbl5 = tk.Label(window, text="This is a different label", bg="purple")
lbl5.pack(side=tk.LEFT)

lbl6 = tk.Label(window, text="Label beside previous label", bg="lightblue")
lbl6.pack(padx = 10, side=tk.BOTTOM)

lbl7 = tk.Label(window, text="Label beside previous label", bg="lightgreen")
lbl7.pack(padx = 10, side=tk.RIGHT)

window.mainloop()