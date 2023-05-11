from  tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("800x1422")
#width, Height
root.minsize(200,100)
root.maxsize(1200,988)
#p = PhotoImage(file="images.png")
image = Image.open("Krishnaji.jpg")
p = ImageTk.PhotoImage(image)
ak_label = Label(image=p)
ak_label.pack()
root.mainloop()