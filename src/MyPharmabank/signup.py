#Purpose: Signup screen to capture the registraton details
#Developer : Arjun Sankar Hariharasuthan

#import all the required modules
from tkinter import *
import customtkinter
import ttkbootstrap as ttk
from tkinter import messagebox
import re
from datetime import datetime
import sqlite3
from email.message import EmailMessage
import ssl
import smtplib
import secrets
import string
from subprocess import call
import time
import os

#creating the window with it's title, geomentry
root = Tk()
root.title("My Pharmabank - SIGNUP")
root.geometry("790x444+100+200")
#importing the background image for the GUI and placing it with the label attribute
bck_image = PhotoImage(file=".\\images\\loginbackground.png")
bck_image_label = Label(root, image=bck_image).place(x=0,y=0)

def root_close():
    if messagebox.askokcancel("Exit","Do you want to exit the program?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", root_close)
root.resizable(False,False)

input_string =""
pname = ""
ename = ""
mname = ""
hname = ""
sname = ""
sbname = ""
psname = ""
otp_input = ""

#Function to validate the values of full name
def on_leave_fn():
    input_string = fullname_entry.get()
    if  input_string == "" or input_string == "Full Name":
        fullname_entry.delete(0, 'end')
        fullname_entry.focus_set()
        messagebox.showerror("Error", "Full name cannot be blank.")
    elif not ''.join(input_string.split()):
        fullname_entry.focus_set()
        messagebox.showerror("Error", "Full name can only contain alphabetic characters.")
        fullname_entry.focus()
    elif len(input_string) > 100:
        fullname_entry.focus_set()
        messagebox.showerror("Error", "Full name cannot be more than 100 characters long.")
        fullname_entry.focus()
    else:
        return 'Y'


#Function to validate the values of password
def on_leave_ps():
    pname = password_entry.get()
    if pname == "" or pname == "Password" :
        password_entry.delete(0, 'end')
        password_entry.focus_set()
        messagebox.showerror("Error", "Password cannot be blank.")
    elif len(pname) < 6:
        password_entry.delete(0, 'end')
        password_entry.focus_set()
        messagebox.showerror("Error", "Password must be at least 6 characters long.")
    elif not any(char.isdigit() for char in pname):
        password_entry.delete(0, 'end')
        password_entry.focus_set()
        messagebox.showerror("Error", "Password must contain at least one number.")
    elif not re.search("[!@#$%^&*()_+-=,.<>/?;:'\"\\[\\]{}|`~]", pname):
        password_entry.delete(0, 'end')
        password_entry.focus_set()
        messagebox.showerror("Error", "Password must contain at least one special character.")
    else:
        return 'Y'

#Function to validate the values of email
def on_leave_em():
    ename=email_entry.get()
    if ename == "" or ename == "Email" :
        email_entry.delete(0, 'end')
        email_entry.focus_set()
        messagebox.showerror("Error", "Email cannot be blank.")
    elif not re.search("@", ename):
        email_entry.delete(0, 'end')
        email_entry.focus_set()
        messagebox.showerror("Error", "Email has to have @")
    else:
        return 'Y'

#Function to validate the values of mobile
def on_leave_mn():
    mname=mobilenum_entry.get()
    if mname == "" or mname == "Mobile Number" :
        mobilenum_entry.delete(0, 'end')
        mobilenum_entry.focus_set()
        messagebox.showerror("Error", "Mobile Number cannot be blank.")
    elif not mname.isnumeric():
        mobilenum_entry.delete(0, 'end')
        mobilenum_entry.focus_set()
        messagebox.showerror("Error", "Mobile Number should be numeric.")
    elif len(mname) != 10:
        mobilenum_entry.delete(0, 'end')
        mobilenum_entry.focus_set()
        messagebox.showerror("Error", "Mobile Number should consist 10 numbers")
    else:
        return 'Y'

#Function to validate the enable ABN textbox if pharmacy
def on_leave_customertype(event):
    customertype_input = type_combobox.get()
    print(customertype_input)
    if customertype_input == 'Pharmacy':
        abn_entry.configure(state="enable")
        abn_entry.delete(0, 'end')
        abn_entry.focus_set()
    else:
        houseunit_entry.focus_set()
        abn_entry.configure(state="disable")


#Function to validate the values of house unit
def on_leave_hu():
    hname=houseunit_entry.get()
    if hname == "" or hname == "Unit/Street Number" :
        houseunit_entry.delete(0, 'end')
        houseunit_entry.focus_set()
        messagebox.showerror("Error", "Unit / Street no cannot be empty.")
    else:
        return 'Y'

#Function to validate the values of street
def on_leave_st():
    sname=street_entry.get()
    if sname == "" or sname == "Street Name" :
        street_entry.delete(0, 'end')
        street_entry.focus_set()
        messagebox.showerror("Error", "Street name cannot be blank.")
    else:
        return 'Y'

#Function to validate the values of suburb
def on_leave_sb():
    sbname=suburb_entry.get()
    if sbname == "" or sbname == "Suburb" :
        suburb_entry.delete(0, 'end')
        suburb_entry.focus_set()
        messagebox.showerror("Error", "Suburb cannot be blank.")
    else:
        return 'Y'

#Function to validate the values of suburb
def on_leave_pc():
    pcode = postcode_entry.get()
    if pcode == "" or pcode == "Postcode" :
        postcode_entry.delete(0, 'end')
        postcode_entry.focus_set()
        messagebox.showerror("Error", "Postcode cannot be blank.")
    elif not pcode.isnumeric():
        postcode_entry.delete(0, 'end')
        postcode_entry.focus_set()
        messagebox.showerror("Error", "Post code should be numeric.")
    else:
        return 'Y'


# Delete the temp txt file created for OTP
def clean_up():
    ename= email_entry.get()
    filename = ".\\datastore\\"+f"{ename}.txt"
    if os.path.exists(filename):
        os.remove(filename)
# To call login screen
def open_login_page():
    root.destroy()
    call(["python", "login_screen.py"])

def open_term_page():
    call(["python", "term_screen.py"])


#Below logic calls individual step functions for initial check up
def inital_check():
    #if user submitted directly without entering any value
    #chk = on_leave_fn()
    #print(chk)
    if on_leave_fn() == 'Y':
        print("fn is good")
        password_entry.focus_set()
        if on_leave_ps() == 'Y':
            print("ps is good")
            email_entry.focus_set()
            if on_leave_em() == 'Y':
                print("em is good")
                mobilenum_entry.focus_set()
                if on_leave_mn() == 'Y':
                    print("mn is good")
                    houseunit_entry.focus_set()
                    if on_leave_hu() == 'Y':
                        print("Unit is good")
                        street_entry.focus_set()
                        if on_leave_st() == 'Y':
                            print("St is good")
                            suburb_entry.focus_set()
                            if on_leave_sb() == 'Y':
                                print("Suburb is good")
                                postcode_entry.focus_set()
                                if on_leave_pc() == 'Y':
                                    print("All  is good")
                                    ename = email_entry.get()
                                    print(ename)
                                    email_check = validate_duplicateemail(ename)  # duplicate email check during registration
                                    if email_check == 'Y':
                                        send_otpemail(ename)  # send otp email for registration completion

# duplicate email check during registration
def validate_duplicateemail(ename):
    values = [ename]
    con = sqlite3.connect(".\\datastore\\pharmabank.db")  # create or connect the database - login_details.db
    cur = con.cursor()  # create the database cursor to execute SQL statements..
    dupemailcur = cur.execute("SELECT * from REGISTRATION WHERE Email = ?", values)
    dupemaillist = dupemailcur.fetchall()

    if len(dupemaillist):  # validate the email already existing
        email_entry.focus_set()
        messagebox.showerror("Error", "This email had already been used, enter different one")
    else:
        return 'Y'
    print("duplicate email check completed")

# send otp email for registration completion
def send_otpemail(ename):
    # sending email function
    email_sender = "noreply.mypharmabank@gmail.com"
    email_password = "iqjujjnvcwbshlmb"

    # generate a random password reset token
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for i in range(5))

    # save the reset token to a file
    filename = ".\\datastore\\"+f"{ename}.txt"
    with open(filename, "w") as f:
        f.write(token)

    # construct the email message
    subject = "Registration Authentication Request"
    body = "Dear Valued Member,\n\nThank you for registrating. Please use the following generated One Time Password(OTP) to complete your registration:\n" + token + "\n\nIf you did not request this password reset, please ignore this email.\n\nBest regards,\nMyPharmabank"

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = ename
    em["Subject"] = subject
    em.set_content(body)

    # send the email using SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)

    status_label = ttk.Label(root, text="OTP has been sent to your registered email", font=('KacstOne', 10, 'bold'), bootstyle="danger")
    status_label.place(x=450, y=350)
    otp_entry.configure(state="enable")
    otp_btn.configure(state="enable")
    otp_entry.focus_set()

# below logic to call OTP check and final data insert
def get_csinput():
    print("OTP check started")
    next_btn.configure(state="disable")
    status = otp_check()
    print("OTP check completed")
    print(status)
    if status == 'Y':
        print("Data insert started")
        insert_reginfo()
        print("Data insert completed")
def otp_check():
    # get the reset token from the user input
    otp_typed= otp_entry.get()
    email_getter = email_entry.get()
    # get the token from the file
    filename = ".\\datastore\\"+f"{email_getter}.txt"
    with open(filename, "r") as f:
        token = f.read()

    # check if the reset token is correct
    if otp_typed == token:
        status ='Y'
    else:
        status ='N'
    return status

def insert_reginfo():
    psname = postcode_entry.get()
    if psname == '':
        postcode_entry.focus_set()
        messagebox.showerror("Error", "Postcode cannot be blank.")
    fullname_input = fullname_entry.get()
    password_input = password_entry.get()
    email_input = email_entry.get()
    mobilenum_input = mobilenum_entry.get()
    houseunit_input = houseunit_entry.get()
    street_input = street_entry.get()
    suburb_input = suburb_entry.get()
    postcode_input = postcode_entry.get()
    customertype_input = type_combobox.get()
    if customertype_input ==    'Patient':
        customertype_input = 'I'
    else:
        customertype_input = 'B'
    state_input = state_combobox.get()
    dt_string = datetime.today().strftime("%y-%m-%d %H:%M:%S")
    dt_object = datetime.strptime(dt_string,"%y-%m-%d %H:%M:%S")
    abn_entry = 12345
    data = (
        {
            "email": email_input, "Password":   password_input, "Full_Name": fullname_input,
            "Mobile": mobilenum_input, "Customer_Type": customertype_input, "Pharmacy_ABN": abn_entry,
            "Unit_Street_No": houseunit_input,  "Street_Name": street_input,
            "Postcode": postcode_input, "Suburb": suburb_input, "State": state_input,
            "Created_Datetime": dt_object,
     }

    )
    con = sqlite3.connect(".\\datastore\\pharmabank.db")  # create the database - login_details.db
    regcur = con.cursor()  # create the database cursor to execute SQL statements..
    signupregcur = regcur.execute("INSERT INTO REGISTRATION VALUES(:email,:Password,:Full_Name,:Mobile,:Customer_Type,:Pharmacy_ABN,:Unit_Street_No,:Street_Name,:Postcode,:Suburb,:State,:Created_Datetime)", data)
    con.commit()
    # to check DB insert successful
    status = regcur.execute("select total_changes()")
    status_val = status.fetchone()
    val = status_val[0]
    if val != 0:
        status_label = Label(root, text="The registration process is completed..\n Will redirect you in few seconds",font=('KacstOne', 10, 'bold'))
        status_label.place(x=450, y=350)
        clean_up()
        # setting value in config file
        filename = ".\\datastore\\config.env"
        with open(filename, "w") as f:
            f.write(fullname_input)
            f.close()
        time.sleep(3)
        root.destroy()
        if customertype_input == 'I':
            call(["python", "search.py"])
        else:
            call(["python", "file_upload.py"])



#using the label to place the title of the page
title_text = ttk.Label(text="BECOME ONE OF US!",font=('KacstOne',14, 'bold'), bootstyle="info")
title_text.place(x=510, y=40)

fullname_entry = ttk.Entry(root, font=('Comic Sans MS', 10, 'bold'), width=13, bootstyle="info")
fullname_entry.place(x=480, y=80)

password_entry = ttk.Entry(root, font=('Comic Sans MS', 10, 'bold'), width=13, bootstyle="info")
password_entry.place(x=625, y=80)
password_entry.insert(0, "Password")

email_entry = ttk.Entry(root,font=('Comic Sans MS',10, 'bold'), width=13,bootstyle="info")
email_entry.place(x=480, y=120)
email_entry.insert(0,"Email")

mobilenum_entry = ttk.Entry(root,font=('Comic Sans MS',10, 'bold'), width=13,bootstyle="info")
mobilenum_entry.place(x=625, y=120)
mobilenum_entry.insert(0,"Mobile Number")

type_variable = customtkinter.StringVar()
type_variable.set('Patient') # set initial value
type_combobox = customtkinter.CTkOptionMenu(master=root, height=35,width=119, values=['Patient','Pharmacy'],variable=type_variable,command=on_leave_customertype)
type_combobox.place(x=480, y=160)
abn_entry= ttk.Entry(root,font=('Comic Sans MS',10, 'bold'), width=13,bootstyle="info")
abn_entry.place(x=625, y=160)
abn_entry.insert(0,"ABN")
abn_entry.configure(state="disable")

#using the label to place the mailing address title on the page
#title_text = ttk.Label(text="MAILING ADDRESS!",font=('KacstOne',14, 'bold'), bootstyle="info")
#title_text.place(x=515, y=220)

houseunit_entry = ttk.Entry(root,font=('Comic Sans MS',10, 'bold'), width=8,bootstyle="info")
houseunit_entry.place(x=460, y=210)
houseunit_entry.insert(0,"Unit/Street Number")
street_entry = ttk.Entry(root,font=('Comic Sans MS',10, 'bold'), width=16,bootstyle="info")
street_entry.place(x=550, y=210)
street_entry.insert(0,"Street Name")


state_variable = customtkinter.StringVar()  # set initial value
state_variable.set('NSW') # set initial value
state_combobox = customtkinter.CTkOptionMenu(master=root, height=35, width=10,values=["NSW","WA", "VIC", "NT", "SA", "TAS"],variable=state_variable)
state_combobox.place(x=700, y=210)
suburb_entry = ttk.Entry(root,font=('Comic Sans MS',10, 'bold'), width=10,bootstyle="info")
suburb_entry.place(x=460, y=255)
suburb_entry.insert(0,"Suburb")

postcode_entry = ttk.Entry(root, font=('Comic Sans MS',10, 'bold'),width=8,bootstyle="info")
postcode_entry.place(x=560, y=255)
postcode_entry.insert(0,"Postcode")
next_btn = ttk.Button(root, text="NEXT",width=8, bootstyle="info",command=inital_check)
next_btn.place(x=700, y=260)

otp_entry = ttk.Entry(root,width=8, font=('Comic Sans MS',10, 'bold'),  bootstyle="info")
otp_entry.place(x=460, y=300)
otp_entry.insert(0,"OTP")
otp_entry.configure(state="disable")
otp_btn = ttk.Button(root, text="VERIFY" ,width=8,bootstyle="info",command= get_csinput)
otp_btn.place(x=560, y=300)
otp_btn.configure(state="disable")

termuse_btn = ttk.Button(root, text="Terms of Use",width=12,bootstyle="info", command=open_term_page)
termuse_btn.place(x=680, y=300)

login_shift = ttk.Label(root, text="Are you already a member?", font=('KacstOne',12, 'bold'), bootstyle="info")
login_shift.place(x=450, y=400)
login_btn = ttk.Button(root, text="Login",width=13,bootstyle="info", command=open_login_page)
login_btn.place(x=670, y=395)


fullname_entry.focus()
fullname_entry.insert(0,"Full Name")
root.mainloop()