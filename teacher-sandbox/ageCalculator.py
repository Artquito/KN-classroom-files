import tkinter as tk

window = tk.Tk()
title_frame = tk.Frame()
title_frame.pack(padx=10, pady=(10, 0), anchor="w")

calculator_frame = tk.Frame()
calculator_frame.pack(padx=10, pady=(0, 20), anchor="w")


result = tk.StringVar()
result.set("Enter your information")

title_lbl = tk.Label(title_frame, text="AGE CALCULATOR", font=("Arial", 8, "bold"))
title_lbl.pack(anchor="w")
sub_title_lbl = tk.Label(title_frame, text="Enter the name and birth year to know\nhow old a person is", justify="left")
sub_title_lbl.pack(anchor="w")

name_lbl = tk.Label(calculator_frame, text="Name", width=10, bg='salmon', anchor="w")
name_lbl.grid( row=0, column= 0,  padx=(0, 8), pady=10, sticky="we")
name_ent = tk.Entry(calculator_frame)
name_ent.grid(row=0, column= 1)

birth_year_lbl = tk.Label(calculator_frame, text="Birth Year", bg="violet", anchor="w")
birth_year_lbl.grid(row=1, column=0, padx=(0, 8), sticky="we")
birth_year_ent = tk.Entry(calculator_frame)
birth_year_ent.grid(row=1, column=1)

calc_btn = tk.Button(calculator_frame, text="Calculate", background="slategray")
calc_btn.grid(row=0, column=2, rowspan=2, padx=(10, 0), sticky="we")

result_lbl = tk.Label(calculator_frame, textvariable=result, bg="slategray", anchor="center")
result_lbl.grid(row=2, column=0, pady=(10, 0), columnspan=3, sticky="wens")

window.mainloop()