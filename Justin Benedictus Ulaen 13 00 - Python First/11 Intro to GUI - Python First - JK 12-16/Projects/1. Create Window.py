#library used for making GUI in python
import tkinter

#The main part of creating a GUI is by creating the window of the GUI
#First, we declare a variable for creating the window object
window = tkinter.Tk()
#Giving title to the window
window.title("window example")
#Giving size to the window where the number represents Width x Height
window.geometry("600x500")

#To execute the GUI command until the program closed
window.mainloop()
