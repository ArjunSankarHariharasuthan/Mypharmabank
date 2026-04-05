#Purpose: Term of use screen to provide disclaimer and term details
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


#Import the image using PhotoImage function for image button



labl_1 = Label(root,bg='white', fg="blue",text="My Pharmabank Terms of Use",font=("MessinaSansWeb", 13))
labl_1.place(x=30,y=53)
labl_11 = Label(root,bg='white',justify='left',fg="black",text="My Pharmabank app let's patients search for certain medications\n,and also displays the availability of the medication in various pharmacies and allows \npharmacies to upload their medicine details into the app.",font=("Tahoma", 10))
labl_11.place(x=30,y=73)

labl_2 = Label(root,bg='white', fg="blue",text="These Terms of Use contain details,disclaimers and limitations.",font=("MessinaSansWeb", 13))
labl_2.place(x=30,y=133)
labl_21 = Label(root,bg='white',justify='left',fg="black",text="1. To be eligible to register and access the app you must be 16 years of age or older",font=("Tahoma", 10))
labl_21.place(x=30,y=160)

labl_22 = Label(root,bg='white',justify='left',fg="black",text="2. You are responsible for the use of the app and must secure your credentails at \nall times",font=("Tahoma", 10))
labl_22.place(x=30,y=180)

labl_24 = Label(root,bg='white',justify='left',fg="black",text="3. You must not use or attempt to use app for the following reasons",font=("Tahoma", 10))
labl_24.place(x=30,y=220)

labl_25 = Label(root,bg='white',justify='left',fg="black",text="    3.1 Your not allowed to upload any pharmacy medicine data that is not yours",font=("Tahoma", 10))
labl_25.place(x=30,y=240)

labl_26 = Label(root,bg='white',justify='left',fg="black",text="    3.2 Your account should not be accessed by anyone but yourself",font=("Tahoma", 10))
labl_26.place(x=30,y=260)

labl_27 = Label(root,bg='white',justify='left',fg="black",text="    3.3 Send or post any unsolicited messages or any other offensive,infammatory,\nfraudulent activities",font=("Tahoma", 10))
labl_27.place(x=30,y=280)

labl_6 = Label(root,bg='white', fg="blue",text="Disclaimers",font=("MessinaSansWeb", 13))
labl_6.place(x=30,y=340)
labl_61 = Label(root,bg='white',fg="black",justify='left',text="My Pharmabank is provided to you on an 'as is' and 'as available' basis and from \ntime to time , contain erros , faults and inaccuracy.You should always make sure\nand rely on upon your own verification with the following Pharmacies",font=("Tahoma", 10))
labl_61.place(x=30,y=360)
mainloop()