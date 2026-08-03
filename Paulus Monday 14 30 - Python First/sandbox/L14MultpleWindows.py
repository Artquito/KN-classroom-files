import tkinter as tk

window = tk.Tk()
window.title("Multiple Window")
window.geometry("500x500")

lbl1 = tk.Label(window, text="This is the main window, this is the window open when the software start")
lbl1.pack()

extraWindow = tk.Toplevel(window)
extraWindow.title("I am the extra window")
extraWindow.geometry("400x400")
lbl2 = tk.Label(extraWindow, text="This is another window. Closing this window will not close the application")
lbl2.pack()

superExtraWindow = tk.Toplevel(extraWindow)
superExtraWindow.title("I am the super extra window")
superExtraWindow.geometry("300x300")
lbl3 = tk.Label(superExtraWindow, text="This is super extra window. Closing this window will not close the application")
lbl3.pack()

window.mainloop()