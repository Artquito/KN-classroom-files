import tkinter as tk

window = tk.Tk()
window.title("pack and grid")
window.geometry("500x500")

frame1 = tk.Frame()
frame2 = tk.Frame()

lbl1= tk.Label(frame1, text="This is label 1")
lbl2= tk.Label(frame1, text="This is label 2")
lbl3= tk.Label(frame1, text="This is label 3")
lbl4= tk.Label(frame2, text="This is label 4")
lbl5= tk.Label(frame2, text="This is label 5")
lbl6= tk.Label(frame2, text="This is label 6")

lbl1.pack(side=tk.TOP)
lbl2.pack(side=tk.TOP)
lbl3.pack(side=tk.TOP)
lbl4.pack(side=tk.TOP)
lbl5.pack(side=tk.TOP)
lbl6.pack(side=tk.TOP)

frame1.grid(column=0, row=0)
frame2.grid(column=1, row=0, columnspan=4)


window.mainloop()