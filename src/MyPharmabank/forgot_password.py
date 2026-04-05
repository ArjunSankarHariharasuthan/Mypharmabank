#Purpose: Forgot  screen to provide user to get the login detail after OTP authentication
#Developer : Arjun Sankar Hariharasuthan

#import all the required modules
from tkinter import *
import ttkbootstrap as ttk
from subprocess import call
import os
from email.message import EmailMessage
import ssl
import smtplib
import secrets
import string
import sqlite3
import time
from tkinter import messagebox

#creating the window with it's title, geomentry
root = Tk()
root.title("MyPharmabank - FORGOT PASSWORD")
root.geometry("790x444+100+100")
root.resizable(False,False)
#bck_image = ImageTk.PhotoImage(file=".\\images\\upload_layout.png")
bck_image = PhotoImage(file=".\\images\\upload_layout.png")
bck_image_label = Label(root, image=bck_image).place(x=0,y=0)



#sending email function
email_sender = "noreply.mypharmabank@gmail.com"
email_password = "iqjujjnvcwbshlmb"


def root_close():
    if messagebox.askokcancel("Exit","Do you want to exit the program?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", root_close)
root.resizable(False,False)

def send_email():
    # get the email address from the tkinter widget
    email_getter = email_entry.get()
    values = [email_getter]
    con = sqlite3.connect(".\\datastore\\pharmabank.db")  # create or connect the database - login_details.db
    cur = con.cursor()  # create the database cursor to execute SQL statements..
    logiresultcur = cur.execute("SELECT * from REGISTRATION WHERE Email = ?", values)
    loginresultlist = logiresultcur.fetchall()


    if  len(loginresultlist): #validate the result has mathcing row
        alphabet = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(alphabet) for i in range(5))

        # save the reset token to a file
        filename = ".\\datastore\\" + f"{email_getter}.txt"
        with open(filename, "w") as f:
            f.write(token)

        # Get OTP from REGISTERATION TABLE
        # Write code to get it and token variable

        # construct the email message
        subject = "Forgot Password Request"
        body = "Dear Valued Member,\n\nThank you for registrating. Please use the following generated One Time Password(OTP) to complete your Authentication:\n" + token + "\n\nIf you did not request this password reset, please ignore this email.\n\nBest regards,\nMyPharmabank"

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_getter
        em["Subject"] = subject
        em.set_content(body)

        # send the email using SSL
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(em)

        status_label = Label(root, text="OTP has been sent successfully.", font=('KacstOne',10, 'bold'))
        status_label.place(x=100, y=300)
        reset_entry.configure(state="enable")
        reset_btn.configure(state="enable")
        reset_entry.focus_set()
    else:
        status_label = Label(root, text="Email is not registered", font=('KacstOne', 10, 'bold'), fg="Red")
        status_label.place(x=100, y=300)

# Delete the temp txt file created for OTP
def clean_up():
    email_getter= email_entry.get()
    filename = ".\\datastore\\"+f"{email_getter}.txt"
    if os.path.exists(filename):
        os.remove(filename)
def check_token():
    # get the email address from the tkinter widget
    email_getter = email_entry.get()

    # get the token from the file
    filename = ".\\datastore\\" + f"{email_getter}.txt"
    with open(filename, "r") as f:
        token = f.read()

    # Get OTP from user typed
    # Write code to to check the match with token that u got it from table
    # if write, send user an email with old password
    # Advise user to change the password.

    # get the reset token from the user input
    reset_token = reset_entry.get()

    # check if the reset token is correct
    if reset_token == token:
        status_label = Label(root, text="OTP validated successfully. Check your mail", font=('KacstOne', 10, 'bold'), fg="Green")
        status_label.place(x=100, y=300)


        #if OTP is successful, the email sent to the user with the login inputs,
        #redirect to login page
        email_getter = email_entry.get()
        values = [email_getter]
        con = sqlite3.connect(".\\datastore\\pharmabank.db")  # create or connect the database - login_details.db
        cur = con.cursor()  # create the database cursor to execute SQL statements..
        logiresultcur = cur.execute("SELECT * from REGISTRATION WHERE Email = ?", values)
        loginresultlist = logiresultcur.fetchall()
        pd = loginresultlist[0][1]

        if pd != '':


            # construct the email message
            subject = "Registration Login Request"
            body = "Dear Valued Member,\n\n Please use this Password to login into Application next time . :\n" + pd + "\n\nIf you did not request this password reset, please ignore this email.\n\nBest regards,\nMyPharmabank"

            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_getter
            em["Subject"] = subject
            em.set_content(body)

            # send the email using SSL
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.send_message(em)

            clean_up()
            time.sleep(3)
            root.destroy()
            call(["python", "login_screen.py"])
            

    else:
        status_label = Label(root, text="Incorrect OTP, Please Try again   ", font=('KacstOne', 10, 'bold'))
        status_label.place(x=100, y=300)



title_label=ttk.Label(root, text="I HAVE FORGOTTEN MY PASSWORD? ", font=('MessinaSansWeb',18, 'bold'), bootstyle="info")
title_label.place(x=40, y=100)

#username
email_entry = ttk.Entry(root,font=('MessinaSansWeb',10, 'bold'), width=20,bootstyle="info")
email_entry.place(x=60, y=190)
email_entry.insert(0,"Email")

send_btn = ttk.Button(root, text="NEXT",width=10,bootstyle="info", command=send_email)
send_btn.place(x=220, y=190)

#OTP
reset_entry = ttk.Entry(root,font=('MessinaSansWeb',10, 'bold'), width=20,bootstyle="info")
reset_entry.place(x=60, y=260)
reset_entry.insert(0,"Input the OTP")
reset_entry.configure(state="disable")

reset_btn = ttk.Button(root, text="SUBMIT",width=12,bootstyle="info", command=check_token)
reset_btn.place(x=220, y=260)
reset_btn.configure(state="disable")

root.mainloop()

