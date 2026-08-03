import tkinter as tk

def getText():
    inputText = tArea2.get("1.0","end-1c")
    label3.config(text=inputText)

window = tk.Tk()
window.title("Creating a Text Area")
window.geometry("500x300")

label = tk.Label(window, text="This is a text area")
tArea = tk.Text(window, height=2, width=30)
tArea.insert(tk.END, "Hello world!")

label2 = tk.Label(window, text="We can get the text from the text area")
tArea2 = tk.Text(window, height=2, width=30)
tArea2.insert(tk.END, "Hello world!")

button = tk.Button(window, text="Get Text", command = getText)
label3 = tk.Label(window)

label.pack()
tArea.pack()
label2.pack()
tArea2.pack()
button.pack()
label3.pack()

window.mainloop()
