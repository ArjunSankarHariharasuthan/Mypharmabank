#Purpose: Contact us screen to display contact details for user to reach us
#Developer : Arjun Sankar Hariharasuthan
# File is to provide Contact us details
from tkinter import *
from subprocess import call
from tkinter import messagebox
root=Tk()

#Setting the size of window frame.
root.title("My Pharmabank - CONTACT US")
root.geometry("790x444+100+200") # creates dimensions of page
root.resizable(0, 0) # will disable max/min tab of window
root.config(background="light blue")
#bck_image = ImageTk.PhotoImage(file=".\\images\\upload_layout.png")
bck_image = PhotoImage(file=".\\images\\contactus_layout.png")
bck_image_label = Label(root, image=bck_image).place(x=0,y=0)

def root_close():
    if messagebox.askokcancel("Exit","Do you want to exit the program?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", root_close)
root.resizable(False,False)

def call_goback():
    root.destroy()
    call(["python", "search.py"])

#Import the image using PhotoImage function for image button
goback_btn= PhotoImage(file=".\\images\\back.png")
goback = Button(root, image=goback_btn,borderwidth=0, command= call_goback)
goback.place(x=470,y=37)

#Positioning the Plain Text
labl_0 = Label(root,bg='white', justify='left',fg="Blue",text="CUSTOMER SUPPORT",font=("KacstOne", 15))
labl_0.place(x=35,y=80)
labl_01 = Label(root,bg='white',justify='left',fg="black",text="If you are experiencing any issues or require help from",font=("MessinaSansWeb", 11))
labl_01.place(x=35,y=120)
labl_02 = Label(root,bg='white',justify='left',fg="black",text="MyPharmabank Support team, please contact us at",font=("MessinaSansWeb", 11))
labl_02.place(x=35,y=145)
labl_03 = Label(root,bg='white',justify='left',fg="black",text="contactus_pharmabank@gmail.com",font=("MessinaSansWeb", 11,'underline'))
labl_03.place(x=35,y=170)


labl_1 = Label(root,bg='white', justify='left',fg="Blue",text="CONTACT US",font=("KacstOne", 15))
labl_1.place(x=35,y=215)
labl_11 = Label(root,bg='white',justify='left',fg="black",text="0491119850",font=("MessinaSansWeb", 11))
labl_11.place(x=35,y=250)
labl_12 = Label(root,bg='white',justify='left',fg="black",text="210 Great Western HWY",font=("MessinaSansWeb", 11))
labl_12.place(x=35,y=280)
labl_13 = Label(root,bg='white',justify='left',fg="black",text="NSW 2150 Australia",font=("MessinaSansWeb", 11))
labl_13.place(x=35,y=310)

def call_fb():
    root.destroy()
    call(["python", "feedback.py"])
    print("called Feedback")

mainloop()