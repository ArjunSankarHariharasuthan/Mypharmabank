#Purpose: Search screen to display the medicine data for user.
#Developer : Arjun Sankar Hariharasuthan

# File is to allow user to enter drug details in the search pages.
from tkinter import *
from subprocess import call
import sqlite3
import ttkbootstrap as ttk
from tkinter import messagebox

root=Tk()

#Setting the size of window frame.
root.title("My Pharmabank - SEARCH")
root.geometry("790x444+100+200")
root.config(background="light blue")
root.resizable(0, 0) # will disable max/min tab of window
#importing the background image for the GUI and placing it with the label attribute
bck_image = PhotoImage(file=".\\images\\search_layout.png")
bck_image_label = Label(root, image=bck_image).place(x=0,y=0)


#All functions are listed below

def root_close():
    if messagebox.askokcancel("Exit","Do you want to exit the program?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", root_close)
root.resizable(False,False)

def chosen_medicine(pharmacy_mail): # Get drug name and find out in main drug file
    print("pharmacy_mail"+pharmacy_mail)

#Import the image using PhotoImage function for image button
like_btn= PhotoImage(file=".\\images\\like.png")

def get_input(): # Get drug name and find out in main drug file
    search_input=search_bar.get("1.0","end-1c")

    # initialise the label text
    result_txt = "                                                                                                                                              \n"
    result_txt = result_txt +"                                                                                                                                               \n"
    result_txt = result_txt +"                                                                                                                                               \n"
    result_txt = result_txt +"                                                                                                                                               \n"
    result_txt = result_txt +"                                                                                                                                               \n"
    result_txt = result_txt + "                                                                                                                                               \n"
    result_txt = result_txt + "                                                                                                                                               \n"
    result_txt = result_txt + "                                                                                                                                               \n"
    result_txt = result_txt + "                                                                                                                                               \n"
    result_txt = result_txt + "                                                                                                                                               \n"
    result_label = Label(root, text=result_txt, font=('MessinaSansWeb', 10, 'bold'))
    result_label.config(bg='white', justify="left", fg='red')
    result_label.place(x=120, y=200)

    if search_input == "" or search_input == "Enter Medicine Full or Short name":
        result_label.place(x=120,y=200)
        result_label.configure(bg='white',fg='red',text="Please enter valid value to search ")
    else:
        user_typed_formated = ''.join(search_input.lower().split()) #full match word
        con = sqlite3.connect(".\\datastore\\pharmabank.db")  # create or connect the database - login_details.db
        searchcur = con.cursor()  # create the database cursor to execute SQL statements..
        user_typed_args = [user_typed_formated]
        logiresultcur =  searchcur.execute("SELECT * FROM MEDICINE_DETAIL WHERE lower(replace(Medicine_Full_Name,' ','')) = ? ORDER BY Postcode LIMIT 4 ",user_typed_args)
        loginresultlist = logiresultcur.fetchall()

        if  len(loginresultlist): #validate the result has mathcing row
            yaxix = 200
            for row in loginresultlist:
                result_txt = "Location : "+row[8]+" , "+str(row[7]) + "    " + "Availability : " + str(row[3])+"    "+ "Mail At "+row[11]+"\n"+row[2]
                result_label = Label(root,text=result_txt,font=('MessinaSansWeb', 10, 'bold'))
                result_label.config(bg='white',justify="left",fg='blue')
                result_label.place(x=120,y=yaxix)
                yaxix = yaxix + 40
        else:  # Probabilistic match
            user_typed_formated = '%' + ''.join(search_input.lower().split()) + '%'  # Short Word match
            con = sqlite3.connect(".\\datastore\\pharmabank.db")  # create or connect the database - login_details.db
            searchcur = con.cursor()  # create the database cursor to execute SQL statements..
            user_typed_args = [user_typed_formated]
            logiresultcur = searchcur.execute("SELECT * FROM MEDICINE_DETAIL  WHERE lower(replace(Medicine_Full_Name,' ','')) like ?  ORDER BY Postcode LIMIT 4",user_typed_args)
            loginresultlist = logiresultcur.fetchall()
            yaxix = 200
            for row in loginresultlist:
                result_txt = "Location : " + row[8] + " , " + str(row[7]) + "    " + "Availability : " + str(row[3]) + "    " + "Mail At " + row[11] + "\n" +row[2]
                result_label = Label(root, text=result_txt, font=('MessinaSansWeb', 10, 'bold'))
                result_label.config(bg='white', justify="left", fg='blue')
                result_label.place(x=120, y=yaxix)
                yaxix = yaxix + 40
            if not len(loginresultlist):
                result_txt = "Medicine data is not available, Please modify the search"
                result_label = Label(root, text=result_txt, font=('MessinaSansWeb', 10, 'bold'))
                result_label.config(bg='white', justify="left", fg='red')
                result_label.place(x=120, y=200)
def call_hs():
    root.destroy()
    call(["python", "generalfaq.py"])

def call_cu():
    root.destroy()
    call(["python","contact_us.py"])


def call_fb():
    root.destroy()
    call(["python", "feedback.py"])

#Positioning the Plain Text

title_label=ttk.Label(root, text="BETTER CONNECTED TO ALL PHARMACY", font=('KacstOne',18, 'bold'), bootstyle="info")
title_label.place(x=145,y=30)

labl_1 = Label(root,bg='white',fg='blue', justify='left', text="My PharmaBank is home to all pharamcies around Australia, with all in one place.\nFind your medicine in no time with the status of stock availability!",width=88,font=("MessinaSansWeb", 10))
labl_1.place(x=40,y=70)

filename = ".\\datastore\\config.env"
with open(filename, "r") as f:
    name = f.read()
    f.close()

labl_2 = ttk.Label(root, justify='left', text="Welcome "+name.upper(),width=20,font=("KacstOne", 10, "bold"),bootstyle="info")
labl_2.place(x=70,y=120)


#Setting the search text box and button in frame.
search_bar=Text(root, height=1.5, width=50)
search_bar.insert(INSERT,"Enter Medicine Full or Short name")
search_bar.tag_add("here", "1.0", "1.35")
search_bar.tag_config("here",  foreground="black", justify="center",font=("MessinaSansWeb", 10))
search_bar.place(x=200,y=140)

#Import the image using PhotoImage function for image button
click_btn= PhotoImage(file=".\\images\\search.png")

#Let us create a dummy button and pass the image
search_button= Button(root, image=click_btn,borderwidth=1, command= get_input)
search_button.place(x=515,y=140)

Button(root, text='Help & Support',width=15,bg='white',fg='blue',font=("Arial bold", 10),borderwidth=0, command= call_hs).place(x=50,y=390)
Button(root, text='Contact Us',width=10,bg='white',fg='blue',font=("Arial bold", 10),borderwidth=0,command= call_cu).place(x=348,y=390)
Button(root, text='Feedback',width=10,bg='white',fg='blue',font=("Arial bold", 10),borderwidth=0,command= call_fb).place(x=650,y=390)


mainloop()

