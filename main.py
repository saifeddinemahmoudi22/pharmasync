import tkinter
from tkinter import *
from tkinter import PhotoImage
app = Tk()
app.title("saifeddine")
app.geometry("1200x1000")

image_path=PhotoImage(file=r"C:\Users\21652\Desktop\friends\PharmaSync.png")
bg_Image=tkinter.Label(app,image=image_path)
bg_Image.pack()


mybutton = Button(app, text="Sign in", fg="white" , bg="green" ,command=exit )
mybutton.place(relx=0.5,rely=0.33, anchor="center" )
mylabel = Label(app, text="ID" , fg="white" , bg="green")
mylabel.place(relx=0.4 , rely=0.25 , anchor="center" )
mylabel = Label(app, text="Password" , fg="white" , bg="green")
mylabel.place(relx=0.4 , rely=0.30 , anchor="center" )
myinput = Entry ( app, width=20)
myinput.place(relx =0.5, rely=0.25, anchor="center")
myinput = Entry ( app, width=20)
myinput.place(relx =0.5, rely=0.30 , anchor="center" )
mybutton = Button(app, text="create new ", fg="white" , bg="blue" ,command=exit )
mybutton.place(relx=0.5,rely=0.37, anchor="center")





app.mainloop()
