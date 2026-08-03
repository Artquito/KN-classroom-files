import tkinter

window = tkinter.Tk()
window.title("This is a title")
window.geometry("600x500")

label = tkinter.Label(window, text="This is a label")
label.pack()
lbl = tkinter.Label(window, text="This is a label with Calibri font", font=("Calibri", 10))
lbl.pack()
lbl2 = tkinter.Label(window, text="This is a label with Arial font", font=("Arial", 15))
lbl2.pack()

#how to put image in Tkinter
img = tkinter.PhotoImage(file="image/button.png")
#to resize the size of an image if it is too big to fit the label
#subsample(5,5) means it will use every 5th pixel in the image
#meaning (1,1) will use all the pixels, which is the original size
resizeImg = img.subsample(5,5)
lbl3 = tkinter.Label(window, image=resizeImg)

lbl3.pack()


window.mainloop()
