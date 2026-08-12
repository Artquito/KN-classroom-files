import tkinter as tk
from tkinter import font  # Import the font module

tax = 0.12

window = tk.Tk()
window.geometry("300x200")
window.title("PPh Calculator")


heading = font.Font(family="Arial", size=12, weight="bold")
paragraph = font.Font(family="Arial", size=8)

'''
Header UI Code
'''
header_frame = tk.Frame(window)
header_frame.pack(padx=10, pady=10, anchor="w")

title = tk.Label(header_frame, text="PPh Calculator", font=heading, justify="left")
title.pack(pady=(0, 1), anchor="w")

sub_title = tk.Label(header_frame, text="Enter the amount of your item to get the taxed amount", font=paragraph, justify="left")
sub_title.pack(anchor="w")

# ---------------------------------------------------------#


calculator_frame = tk.Frame(window)
calculator_frame.pack(anchor="w", padx=10)

price_lbl = tk.Label(calculator_frame, text="Item Price", anchor="w",background="salmon")
price_lbl.grid(row=0, column= 0, padx=4, sticky="we")
price_ent = tk.Entry(calculator_frame)
price_ent.grid(row=0, column=1)

tax_lbl = tk.Label(calculator_frame, text="Tax amount(%)", background="limegreen", anchor="w")
tax_lbl.grid(row=1, column= 0, padx=4, pady=(8, 0), sticky="wen")
tax_ent = tk.Entry(calculator_frame)
tax_ent.insert(0, "0.12")
tax_ent.config(state="disabled")
tax_ent.grid(row=1, column=1, pady=(8, 0), sticky="n")

calc_btn = tk.Button(calculator_frame, text="CALCULATE")
calc_btn.grid(row=0, column=2, rowspan=2, sticky="ns")



window.mainloop()