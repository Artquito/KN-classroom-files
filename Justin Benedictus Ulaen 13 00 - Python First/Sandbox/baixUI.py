import tkinter as tk

window = tk.Tk()
window.title("PPH Calculator")

title_frame = tk.Frame(window)
title_frame.pack(padx=10,pady=10)

calculator_frame = tk.Frame(window)
calculator_frame.pack(padx=10,pady=10, anchor="w")

title = tk.Label(title_frame, text="PPH Calculator", font=("Arial", 10, "bold"))
title.pack(anchor="w")
sub_title = tk.Label(title_frame, text="Enter the price of your item to get the taxed price")
sub_title.pack(anchor="w")

price_input_lbl = tk.Label(calculator_frame, text="NAME", bg="salmon", width=12)
price_input_lbl.grid(row=0, column=0)

price_input_ent = tk.Entry(calculator_frame)
price_input_ent.grid(row=0, column=1)

tax_input_lbl = tk.Label(calculator_frame, text="NAME", bg="salmon", width=12)
tax_input_lbl.grid(row=1, column=0)

tax_input_ent = tk.Entry(calculator_frame)
tax_input_ent.grid(row=1, column=1)

calculate_btn = tk.Button(calculator_frame, text="CALCULATE")
calculate_btn.grid(row=0, column=2, rowspan=2, sticky="ns")

window.mainloop()