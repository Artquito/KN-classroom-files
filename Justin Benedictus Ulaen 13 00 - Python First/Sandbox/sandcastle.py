import tkinter as tk

window = tk.Tk()
window.geometry("300x300")

frame = tk.Frame(window)
frame.pack(fill="both", expand=True, ipady=10)

label = tk.Label(frame, text="This is a label", bg="salmon")
label.pack(expand=1, fill="both", side="left", padx=(0,10),)
label2 = tk.Label(frame, text="This is a label 2", bg="violet")
label2.pack(expand=1, fill="both", side="left", padx=(0,10))
label3 = tk.Label(frame, text="This is a label 3", bg="limegreen")
label3.pack(expand=1, fill="both", side="left")

window.mainloop()