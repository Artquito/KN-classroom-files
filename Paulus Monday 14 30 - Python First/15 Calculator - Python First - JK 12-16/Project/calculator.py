import  tkinter as tk

window = tk.Tk()
window.title("Calculator by KN")
window.resizable(0,0)
window.geometry('250x300')

expression = ""

def insert_number(number):
    global expression
    expression = expression + str(number)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def result():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = result

input_text = tk.StringVar()
#Entry input
entry = tk.Entry(window, width = 18, borderwidth= 5, font=("Arial", 18),textvariable= input_text, justify= "right")

#button numbers
button_1 = tk.Button(window, text = "1", padx=20, pady=20 , command= lambda : insert_number(1))
button_2 = tk.Button(window, text = "2", padx=20, pady=20 , command= lambda : insert_number(2))
button_3 = tk.Button(window, text = "3", padx=20, pady=20 , command= lambda : insert_number(3))
button_4 = tk.Button(window, text = "4", padx=20, pady=20 , command= lambda : insert_number(4))
button_5 = tk.Button(window, text = "5", padx=20, pady=20 , command= lambda : insert_number(5))
button_6 = tk.Button(window, text = "6", padx=20, pady=20 , command= lambda : insert_number(6))
button_7 = tk.Button(window, text = "7", padx=20, pady=20 , command= lambda : insert_number(7))
button_8 = tk.Button(window, text = "8", padx=20, pady=20 , command= lambda : insert_number(8))
button_9 = tk.Button(window, text = "9", padx=20, pady=20 , command= lambda : insert_number(9))
button_0 = tk.Button(window, text = "0", padx=20, pady=20 , command= lambda : insert_number(0))
button_add = tk.Button(window, text = "+", padx=22, pady=20,command= lambda : insert_number('+') )
button_substraction = tk.Button(window, text = "-", padx=24, pady=20,command= lambda : insert_number("-") )
button_multiplication = tk.Button(window, text = "*", padx=24, pady=20,command= lambda : insert_number("*") )
button_division = tk.Button(window, text = "/", padx=24, pady=20, command= lambda : insert_number("/") )
button_equal = tk.Button(window, text = "=", padx=20, pady=20, command= lambda : result())
button_clear = tk.Button(window,command=button_clear,text = "clear", padx=10, pady=20)

#Button Place Grid
entry.grid(row= 0 , column= 0, columnspan= 5)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_add.grid(row=2, column=3)
button_substraction.grid(row=1, column=3)
button_multiplication.grid(row=3, column=3)
button_division.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)




window.mainloop()