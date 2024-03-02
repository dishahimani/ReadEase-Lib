#importing all necessary modules
import os    #operating system 
import sys   #module for system specific functions
import webbot  #moduel for browser automation
from webbot import Browser
import pynput   # Library for controlling and monitoring input devices
from pynput.keyboard import Key, Controller
import time   #Provides time-related functions
import csv    #Handling CSV files
from pathlib import Path   #Module for working with file paths

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#changing directory to current directory or common folder
directory = os.getcwd()
os.chdir(directory)
original_directory = directory

#---------------------------------------------------------------------------
#specifying the browser
browserExe = "chrome.exe"
#---------------------------------------------------------------------------------------------------------------------------------------------------
#db implies database in short
#sw stands for software
#Taking an empty list , it ll be quite helpful ahead 
sw_db=[]



#initialising a few things
col_list = ["Serial No.","Name","DOB (DDMMYYYY)","Phone Number","City","Password","Books Issued/Downloaded"]
db_csv = open("User_Database.csv", 'a+', newline='')
db_writer = csv.writer(db_csv, delimiter =',')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Defining Functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#function for writing data to csv file

def DB_writer():
    
    with open("User_Database.csv", 'r+') as db_csv1:
        db_reader = csv.reader(db_csv1)
        for rec in db_reader:
            sw_db.append(rec)
    
    #Auto Generating the S.No
    last_record = sw_db[-1]
    last_s_no = int(last_record[0])
    S_no = int(last_s_no + 1)
    s = int(S_no)

    print("* - are mandate fields")
    Name = input("Name:*")
    DOB = int(input("Date Of Birth:(DDMMYYYY)*"))
    Ph = int(input("Phone Number:*"))
    city = input("Enter your city:*")
    password = input("Choose a Password for your account:*")
    db_writer.writerow([S_no,Name,DOB,Ph,city,password])
    
    print(" ")
    print("Your S_no. for our software is:",S_no," please remember it for future purposes")
    time.sleep(1)
    
    db_csv.close()

    print(" ")
    print("You successfully logged in...")
    
    book_choose(s)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#function for reading data to csv file

def DB_reader():
    
    with open("User_Database.csv", 'r+') as db_csv:
        db_reader = csv.reader(db_csv)
        for rec in db_reader:
            sw_db.append(rec)

    Serial_no = int(input("please enter your S_no. to gain access to your database:"))
    desired_rec = sw_db[Serial_no]
    passw = input("Please enter your password:")
    s = int(Serial_no)
    
    if passw == str(desired_rec[5]):
        print(" ")
        print("Authorisation Complete...")
        time.sleep(0.5)
        print("Here is your data:")
        for i in range(len(desired_rec)):
            time.sleep(0.05)
            print(sw_db[0][i],":",sw_db[Serial_no][i])

    else:
        print("Wrong password! Authorisation failed")
        sys.exit()
    db_csv.close()
    book_choose(s)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#main function for choosing books and updating the book taken in the user's profile , Downloading it locally 
def book_choose(x):
    print("------------------------------------------------------------------------------")
    print(" ")
    print("Welcome to book's corner!!!")
    time.sleep(0.5)
    print("Please choose the book you wanna download")
    time.sleep(0.05)

    books = []
    
    #Connecting to books database 
    with open("Books_Database.csv", 'r+') as b_csv:
        b_reader = csv.reader(b_csv)
        for data in b_reader:
            books.append(data)


    for i in books:
        time.sleep(0.05)
        print(i[0],")",i[1])
    

    Serial_no = int(input("please enter the Serial_no of book you wanna download:"))
    desired_book = books[Serial_no]
    book_name = str(desired_book[1])
    drive_link = str(desired_book[2])
    print("Your choosen Book is:",book_name)
    time.sleep(0.05)
    print("Please back off from your system , automation is going to start , pls don't do any other activity on system for now")
    time.sleep(0.05)
    print("Download starting...")
    
    time.sleep(5)

    web = Browser()
    keyboard = Controller()
    web.go_to(drive_link)
    time.sleep(3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    time.sleep(10)
    os.system("taskkill /f /im "+browserExe)
    #it kills all google tabs , so have to find an alternaive for just one google tab
    b_csv.close()

    downloads_path = str(Path.home() / "Downloads")
    raw_string = r"{}".format(downloads_path)
    os.chdir(raw_string)
    file_tbc = raw_string + "/" + str(book_name)

    print("Downloading....")

    #checking if file is downloaded locally or not
    if (os.path.exists(file_tbc)) == True :
        print("Download Successful!!!")     
    else:
        print("Sorry , Some Error came")
        return

    os.chdir(original_directory)
    sw_db= []
    file = open("User_Database.csv", 'r+')
    file.seek(0)
    db_reader = csv.reader(file)
    for rec in db_reader:
        sw_db.append(rec)
    desired_rec = []
    desired_rec = sw_db[x]

    if len(desired_rec) == 6:
        desired_rec.append(book_name)

    else:
        desired_rec[6] = desired_rec[6] + "," + book_name
    file.close()
        
    db_csv = open("User_Database.csv", 'w', newline='')
    db_writer = csv.writer(db_csv, delimiter =',')
    db_writer.writerows(sw_db)
    db_csv.close()

    print("Thank you")
    


         
    print(" ")
    print("------------------------------------------------------------------------------")

#---------------------------------------------------------------------------------------------------------------------------------------------------    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--main program --


print("------------------------------------------------------------------------------")
print("                                                                              ")
print("                         PROJECT WORK                                         ")
print("                        ==============                                        ")
print("                                                                              ")
print("                        ONLINE LIBRARY                                        ")
print("                 ============================                                 ")
print("                                                                              ")
print("------------------------------------------------------------------------------")


c='y'
while (c=='y' or c=='Y'):
    print("Welcome to our Online Library , fellow reader!")
    print("Download any book you want!")
    print("1. NEW USER ")    
    print("2. ALREADY EXISTING USER ")
    print("3. EXIT ")
    opt=int(input("Enter Your Choice (1/2/3 : )"))
    if opt==1:
        print("Welcome to our database , please provide us with the following information:")
        DB_writer()
        
    elif opt==2:
        DB_reader()

    else:
        print("Thank you for choosing us!") 
        break
    
    #after one full running ,we are refreshing these imp variables as we want our changes to reflect now
    sw_db=[]
    db_csv = open("User_Database.csv", 'a+', newline='')
    db_writer = csv.writer(db_csv, delimiter =',')

    
    c=input("\n Do you want to continue? yes(y)/no(n) :")
    
    print("------------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------------------------------------------------------------------
