import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize



from tkinter import *


class MyWindow:
    def __init__(self, win):
        lbl = Label(window, text="Face Recognition Attendance System ", fg='red', font=("Helvetica", 16))
        lbl.place(x=10, y=10)
        btn1 = Button(win, text="Check Camera", fg='blue')
        btn1.place(x=10, y=50)
        btn1.bind('<Button-1>', checkCamera)
        btn2 = Button(window, text="New Entry", fg='blue')
        btn2.place(x=10, y=100)

def checkCamera():
    check_camera.camer()

window = Tk()
mywin = MyWindow(window)
window.title('Auto Attendance')
window.geometry("1000x500+10+10")
window.mainloop()