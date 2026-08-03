import tkinter as tk
import tkinter.messagebox as msgbox

window = tk.Tk()
window.title("Hello World")
window.geometry("300x200")
window.resizable(False, False)

def displayMessage():
    msgbox.showinfo("Message",textInputValue.get())


frame = tk.Frame(window)
frame.pack()

textInputValue = tk.StringVar()
textInputLable = tk.Label(frame, text="Input your name").grid(column=0, row= 0, pady=5, padx=0)
textInputField = tk.Entry(frame, text="Input your name", justify="center", textvariable=textInputValue).grid(column=0, row= 2)
submitBtn= tk.Button(frame,text="Submit", command=displayMessage).grid(column=0, row=3, pady=10)

# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)

# label1=tk.Label(window, text="Hello World")
# label2=tk.Label(window, text="Hello Child")
# label1.grid(row=0   , column=0)
# label2.grid(row=2   , column=0)


window.mainloop()