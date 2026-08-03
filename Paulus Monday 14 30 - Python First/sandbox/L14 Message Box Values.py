import tkinter as tk
import tkinter.messagebox as msgbox


def showMsg():
    result = msgbox.askyesno("Binary Question", "Are you good at valorant?")
    if result == ___:
        print("you press yess, your goood at valorant")
    elif result == ___:
        print("You Press no")

window = tk.Tk()
window.title("test")
window.geometry("300x300")

btn = tk.Button(window, text="Click Me", command= showMsg)
btn.pack()

window.mainloop()