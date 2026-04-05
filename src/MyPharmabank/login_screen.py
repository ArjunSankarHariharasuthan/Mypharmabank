#Purpose: login screen to validate login detail.. Also links for registration page and forgot passowrd
#Developer : Arjun Sankar Hariharasuthan


#import all the required modules
from tkinter import *
import ttkbootstrap as ttk
from subprocess import call
import sqlite3
import re
from tkinter import messagebox
##



#creating the window with it's title, geomentry
root = Tk()
root.title("MyPharmabank - LOG IN")
root.geometry("790x444+100+100")
root.resizable(0, 0) # will disable max/min tab of window
#bck_image = ImageTk.PhotoImage(file=".\\images\\loginbackground.png")
bck_image = PhotoImage(file=".\\images\\loginbackground.png")
bck_image_label = Label(root, image=bck_image).place(x=0,y=0)


def root_close():
    if messagebox.askokcancel("Exit","Do you want to exit the program?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", root_close)
root.resizable(False,False)

def open_signup_page():
    root.destroy()
    call(["python", "signup.py"])

# Function to invoke Forgot password screen
def forgot_password_root():
    root.destroy()
    call(["python", "forgot_password.py"])


#Function to validate the values of user name
def on_emailvalidate():
    ename=email_entry.get()
    #print(ename)
    if ename == "" or ename == "Email" :
        email_entry.delete(0, 'end')
        email_entry.focus_set()
        #messagebox.showerror("Error", "User name cannot be blank.")
        error_label = Label(root, bg='white', fg='red', text="User name cannot be blank.", font=('MessinaSansWeb', 10, 'bold'))
        error_label.place(x=450, y=400)
    elif not re.search("@", ename):
        email_entry.delete(0, 'end')
        email_entry.focus_set()
        #messagebox.showerror("Error", "Email does not have @")
        error_label = Label(root, bg='white', fg='red', text="Invalid Email, does not have @",font=('MessinaSansWeb', 10, 'bold'))
        error_label.place(x=450, y=400)
    else:
        return 'Y'
def on_leave_ps():
    print("called on_leave_ps")
    pname = password_entry.get()
    print(pname)
    print(password_entry.get())
    if pname == "" or pname == "Password" :
        password_entry.delete(0, 'end')
        password_entry.focus_set()
        #messagebox.showerror("Error", "Password cannot be blank.")
        error_label = Label(root, bg='white', fg='red', text="Password cannot be blank",
                            font=('MessinaSansWeb', 10, 'bold'))
        error_label.place(x=450, y=400)
    elif len(pname) < 6:
        password_entry.delete(0, 'end')
        password_entry.focus_set()
        error_label = Label(root, bg='white', fg='red', text="Password must be at least 6 characters long",
                            font=('MessinaSansWeb', 10, 'bold'))
        error_label.place(x=450, y=400)
    else:
        return 'Y'

#Function to validate the values of password
def validate_login():
    pname = password_entry.get()
    ename = email_entry.get()

    if on_emailvalidate() == 'Y':
        print("user name  is good")
        password_entry.focus_set()
        if on_leave_ps() == 'Y':
            print("ps is good")
            values = [ename, pname]
            con = sqlite3.connect(".\\datastore\\pharmabank.db")  # create or connect the database - login_details.db
            cur = con.cursor()  # create the database cursor to execute SQL statements..
            logiresultcur = cur.execute("SELECT * from REGISTRATION WHERE Email = ? AND Password = ?", values)
            loginresultlist = logiresultcur.fetchall()

            if  len(loginresultlist): #validate the result has mathcing row
                root.destroy()
                print(loginresultlist)
                cus_type=loginresultlist[0][4]

                # setting value in config file
                print("value" + loginresultlist[0][2])
                filename = ".\\datastore\\config.env"
                with open(filename, "w") as f:
                    f.write(loginresultlist[0][2])
                    f.close()
                # calling next module based on customer type.
                if cus_type=="I":
                    call(["python", "search.py"])
                elif cus_type=="B":
                    call(["python", "file_upload.py"])

            else:
                print("Invalid email")


title_label=ttk.Label(root, text="Your Trusted (MEDICINE STORE)", font=('KacstOne',12, 'bold'), bootstyle="info")
title_label.place(x=490, y=100)

# To cover GUI layout
email_entry = ttk.Entry(root,font=('Comic Sans MS',13, 'bold'), width=15,bootstyle="info")
email_entry.place(x=530, y=140)
email_entry.insert(0,"Email")

password_entry = ttk.Entry(root,font=('Comic Sans MS',13, 'bold'), width=15,bootstyle="info")
password_entry.place(x=530, y=200)
password_entry.insert(0,"Password")

login_btn = ttk.Button(root, text="Login",width=17,bootstyle="info", command=validate_login)
login_btn.place(x=547, y=250)

footer_label=ttk.Label(root, text="--------------OR------------------", font=('KacstOne',14, 'bold'), width=17,bootstyle="info")
footer_label.place(x=515, y=290)

Register_btn = ttk.Button(root, text="Register",width=17,bootstyle="info", command=open_signup_page)
Register_btn.place(x=547, y=320)


forgot_details=ttk.Label(root, text="Forgot Password, Don't Worry! - ",font=('KacstOne',10, 'bold'),bootstyle="info")
forgot_details.place(x=450, y=374)

forgot_password_btn = ttk.Button(root, text="Forgot Password!",width=15,bootstyle="info", command=forgot_password_root)
forgot_password_btn.place(x=657, y=370)

email_entry.focus()
root.mainloop()