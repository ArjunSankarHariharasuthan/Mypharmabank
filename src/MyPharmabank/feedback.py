#Purpose: FAQ screen to provide chance for user to provide feedback.
#Developer : Arjun Sankar Hariharasuthan

from tkinter import *
import json
from subprocess import call
from tkinter import messagebox

root=Tk()
#Setting the size of window frame.
root.title("My Pharmabank - FEEDBACK")
root.geometry("790x444+100+200")
root.config(background="light blue")
#bck_image = ImageTk.PhotoImage(file=".\\images\\upload_layout.png")
bck_image = PhotoImage(file=".\\images\\feedback_layout.png")
bck_image_label = Label(root, image=bck_image).place(x=0,y=0)

#All functions are listed below

def root_close():
    if messagebox.askokcancel("Exit","Do you want to exit the program?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", root_close)
root.resizable(False,False)

def call_goback():
    print('called')
    root.destroy()
    call(["python", "search.py"])

def get_csinput():
    fullname_input=entry_3.get("1.0","end-1c")
    print(fullname_input)
    email_input = entry_4.get("1.0", "end-1c")
    print(email_input)
    issue_input = entry_5.get("1.0", "end-1c")
    print(issue_input)
    dictionary = {
        "fullname": fullname_input,
        "email": email_input,
        "issue_input": issue_input

    }
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open(".\\datastore\\complaint.json", "w") as outfile:
        ret = outfile.write(json_object)
        outfile.close()
        if ret > 0:
            Label(root, bg='white', fg="Blue", text="Your feedback has been successfully received", font=("MessinaSansWeb", 10)).place(x=180,y=350)
            #print("Your complaint has been successfully received")



#Import the image using PhotoImage function for image button
goback_btn= PhotoImage(file=".\\images\\back.png")
Button(root, image=goback_btn,borderwidth=0, command= call_goback).place(x=470,y=37)

#Positioning the Plain Text
labl_0 = Label(root,bg='white', fg="blue", text="MAKE A SUGGESTION!",font=("KacstOne", 18, "bold"))
labl_0.place(x=35,y=60)
labl_01 = Label(root,bg='white', justify='left', text="My Pharmabank is committed to assess each feedback on priority basis\nand team will reach you!",font=("MessinaSansWeb", 10))
labl_01.place(x=35,y=110)
labl_02 = Label(root,bg='white', text="To submit an online feedback, please fill the form below..",font=("MessinaSansWeb", 10))
labl_02.place(x=35,y=160)

labl_3 = Label(root, bg='white',text="FullName", width=20, font=("MessinaSansWeb", 10))
labl_3.place(x=30, y=230)

entry_3 = Text(root, height=1, width=20, wrap=WORD, bd=2)
entry_3.place(x=170, y=230)

labl_4 = Label(root, bg='white',text="Email", width=20, font=("MessinaSansWeb", 10))
labl_4.place(x=30, y=260)

entry_4 = Text(root, height=1, width=20, wrap=WORD, bd=2)
entry_4.place(x=170, y=260)

labl_4 = Label(root, bg='white',text="Issue", width=20, font=("MessinaSansWeb", 10))
labl_4.place(x=30, y=300)

entry_5 = Text(root, height=2.5, width=40, wrap=WORD, bd=2)
entry_5.place(x=170, y=290)

Button(root, text='Submit',width=20,bg='Blue',fg='white', font=("MessinaSansWeb", 10),command= get_csinput).place(x=180,y=380)

mainloop()