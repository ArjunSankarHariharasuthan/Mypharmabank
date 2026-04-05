#Purpose: File upload screen to validate file then upload to database
#Developer : Arjun Sankar Hariharasuthan

# File is to allow user to enter drug details in the search pages.
from tkinter import *
from tkinter import filedialog
import csv
from datetime import datetime
import sqlite3
from tkinter import messagebox
root=Tk()

#Setting the size of window frame.
root.title("My Pharmabank- FILE UPLOAD")
root.geometry("790x444") # creates dimensions of page
root.config(background="light blue")
root.resizable(0, 0) # will disable max/min tab of window
#bck_image = ImageTk.PhotoImage(file=".\\images\\upload_layout.png")
bck_image = PhotoImage(file=".\\images\\upload_layout.png")
bck_image_label = Label(root, image=bck_image).place(x=0,y=0)

#All functions are listed below

def root_close():
    if messagebox.askokcancel("Exit","Do you want to exit the program?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", root_close)
root.resizable(False,False)

def upload_file():

    # Open the uploaded file and write to main file
    file = filedialog.askopenfilename(title = "Select a drug availability file to upload",filetypes=[('CSV files',"*.csv")])
    csvf = open(file,'r')
    csvReader = csv.reader(csvf) # Open the input file for reading
    #Validate the upload file has proper field sequence in first row
    row=[]
    row = next(csvReader)

    if row[0] != 'pharmacyabn'  or  row[1] != 'pharmacyname' or row[2] != 'medicinefullname' or row[3] != 'availabilityquantity' or row[4] != 'finalprice' or row[5] != 'discountedprice' or row[6] != 'streetname' or row[7] != 'postcode' or row[8] != 'suburb' or row[9] != 'state' or row[10] != 'uploaddatetime' or row[11] != 'uploademail':
        labl_error = Label(root, bg='white', fg='red',text="Incorrect File format, Field Sequence not followed", width=50,font=("MessinaSansWeb", 12))
        labl_error.place(x=60, y=240)

    else:
        # Store the individual uploaded file for backup
        dt_object = datetime.today().strftime("%y-%m-%d-%H-%M-%S")
        outfilename = '.\\datastore\\Master_Medicine_Detail_' + dt_object + '.csv'
        #next(csvReader, None)  # skip the headers for file processing
        csvw = open(outfilename, 'a', encoding='UTF8') # Store the individual files
        csvwriter = csv.writer(csvw)
        con = sqlite3.connect(".\\datastore\\pharmabank.db")  # create or connect  the database - login_details.db
        regcur = con.cursor()  # create the database cursor to execute SQL statements..

        for row in csvReader: # Insert data is started
            csvwriter.writerow(row)

            #Medicine_Full_Name,Availability_Quantity,Final_Price,Discounted_Price post code validation. If not numeric, skip this
            if row[2] != "" and row[3] != "" and row[4] != "" and row[7] != "" and row[7].isdigit() and row[11] != "":

                data = (
                    {
                        "PharmacyABN": row[0],  "Pharmacyname": row[1],
                        "Medicine_Full_Name": row[2],  "Availability_Quantity": row[3],
                        "Final_Price": row[4], "Discounted_Price": row[5], "Street_Name": row[6],
                        "Postcode": row[7], "Suburb": row[8], "State": row[9],
                        "Upload_Datetime": row[10], "Upload_By_Email": row[11],
                    }
                )
                signupregcur = regcur.execute("INSERT INTO MEDICINE_DETAIL VALUES(:PharmacyABN	,:Pharmacyname,:Medicine_Full_Name,:Availability_Quantity,:Final_Price,:Discounted_Price,:Street_Name,:Postcode,:Suburb,:State,:Upload_Datetime,:Upload_By_Email)",data)
                con.commit()

        # to check DB insert successful then pick no of records impacted
        status = regcur.execute("select total_changes()")
        status_val = status.fetchone()
        val = status_val[0]



        res = regcur.execute("SELECT * FROM MEDICINE_DETAIL")
        loginresultlist = res.fetchall()
        print(loginresultlist)
        # Provide confirmation message in the screen
        labl_conf = Label(root, bg='white',fg='blue' ,text="The File is processed successfully with "+str(val) +" records", width=50,font=("MessinaSansWeb", 12))
        labl_conf.place(x=60,y=240)




#Positioning the Plain Text
labl_0 = Label(root,bg='white',fg='blue', text="BETTER CONNECTED TO ALL PHARMACY",font=("KacstOne", 15, "bold"))
labl_0.place(x=75,y=53)

labl_1 = Label(root,bg='white',fg='black', text="My Pharmabank is your home for pharmacy, with all in one place.",font=("MessinaSansWeb", 12))
labl_1.place(x=50,y=100)

filename = ".\\datastore\\config.env"
with open(filename, "r") as f:
    name = f.read()
    f.close()

labl_2 = Label(root, bg='white',fg='blue', justify='left', text="Welcome "+name.upper(),width=20,font=("KacstOne", 10, "bold"))
labl_2.place(x=70,y=155)

#importing the background image for the GUI and placing it with the label attribute
upload_btn= PhotoImage(file=".\\images\\file_upload.png")
upload_button= Button(root, image=upload_btn,borderwidth=1, command= upload_file)
upload_button.place(x=430,y=180)

upload_bar=Text(root, height=2.1, width=40)
upload_bar.insert(INSERT,"Click the button to choose the file")
upload_bar.tag_add("here", "1.0", "1.35")
upload_bar.tag_config("here",  foreground="blue", justify="center",font=("MessinaSansWeb", 12))
upload_bar.place(x=100,y=180)




mainloop()