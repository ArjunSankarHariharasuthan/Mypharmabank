#Purpose: FAQ screen to provide details to user.
#Developer : Arjun Sankar Hariharasuthan

from tkinter import *
from subprocess import call
from tkinter import messagebox

root=Tk()
sb = Scrollbar(root)
sb.pack(side = RIGHT, fill = Y)

#Setting the size of window frame.
root.title("My Pharmabank - HELP & SUPPORT")
root.geometry("790x444+100+200") # creates dimensions of page
root.resizable(0, 0) # will disable max/min tab of window
#bck_image = ImageTk.PhotoImage(file=".\\images\\upload_layout.png")
bck_image = PhotoImage(file=".\\images\\upload_layout.png")
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

Button(root, image=goback_btn,borderwidth=0, command= call_goback).place(x=470,y=37)

labl_1 = Label(root,bg='white', fg="blue",text="How to create an account in My Pharmabank App?",font=("MessinaSansWeb", 13))
labl_1.place(x=35,y=53)
labl_11 = Label(root,bg='white',justify='left',fg="black",text="Click the REGISTER button in the app once you have provided all the necessary\ndetails such as the contact details. Then, become a member by completing the \nOTP verification",font=("Tahoma", 10))
labl_11.place(x=35,y=73)

labl_2 = Label(root,bg='white', fg="blue",text="Forgot my password! What should I do?",font=("MessinaSansWeb", 13))
labl_2.place(x=35,y=153)
labl_21 = Label(root,bg='white',justify='left',fg="black",text="Click the Forgot Login password button at the bottom left of the login page.\nThen provide the email that you have used for the registeration. Subsequently, the \npassword will be sent to your email.",font=("Tahoma", 10))
labl_21.place(x=35,y=173)

labl_3 = Label(root,bg='white', fg="blue",text="How to update my contact details in App?",font=("MessinaSansWeb", 13))
labl_3.place(x=35,y=250)
labl_31 = Label(root,bg='white',justify='left',fg="black",text="This feature is still not available. Till this feature is available, \nPlease send email at contactus-pharmabank@gmail.com from registered email.",font=("Tahoma", 10))
labl_31.place(x=35,y=270)

labl_4 = Label(root,bg='white', fg="blue",text="How does the search bar work?",font=("MessinaSansWeb", 13))
labl_4.place(x=35,y=330)
labl_41 = Label(root,bg='white',justify='left',fg="black",text="Start by entering the medicine's EXACT name into the searchbar.\nFor example, Nurofen Ibuprofen Pain Relief Tablets 200mg 24 Pack OR Nurofen",font=("Tahoma", 10))
labl_41.place(x=35,y=350)

labl_5 = Label(root,bg='white', fg="blue",text="How to update my contact detail in App?",font=("MessinaSansWeb", 13))
labl_5.place(x=10,y=470)
labl_51 = Label(root,bg='white',fg="black",text="Updating contact details in Application feature is still not available. Till this feature is available, \n you can send us email at contactus-pharmabank@gmail.com from your registered email.",font=("Tahoma", 10))
labl_51.place(x=10,y=520)

labl_6 = Label(root,bg='light blue', fg="blue",text="Is it possible to add multiple profiles to one user account?",font=("MessinaSansWeb", 13))
labl_6.place(x=10,y=670)
labl_61 = Label(root,bg='light blue',fg="black",text="The account is uniquely identified by their email. To Support privacy, App does not encourage \n to create multiple logins with same email id.",font=("Tahoma", 10))
labl_61.place(x=10,y=700)
mainloop()