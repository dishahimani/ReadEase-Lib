#menu driven program to perform all operation on a binary file
import os
import csv

#change directory to current directory
directory = os.getcwd()
os.chdir(directory)
original_directory = directory
col_list = ["Serial No.","Name","DOB (DDMMYYYY)","Phone Number","City","Password","Books Issued/Downloaded"]

#write function
def write():
    f=open("User_Database.csv","r+")
    rec_reader = csv.reader(f)
    rec_writer = csv.writer(f)
    sw_db = []
    for rec in rec_reader:
            sw_db.append(rec)
    print("Database Connected.....  Record Insertion Facility")
    last_record = sw_db[-1]
    last_s_no = int(last_record[0])
    S_no = int(last_s_no + 1)
    s = int(S_no)

    print("Enter data ->")
    Name = input("Name:*")
    DOB = input("Date Of Birth:(DDMMYYYY)*")
    Ph = input("Phone Number:*")
    city = input("Enter your city:*")
    password = input("Choose a Password for your account:*")
    Books_Issued = input("Enter Name of the Books Issued:")
    rec_writer.writerow([S_no,Name,DOB,Ph,city,password,Books_Issued])
    print("S_no. for this user is:",S_no," please remember it for future purposes")
    print(" ")
    print("Insertion completed")
    f.close()

#read function
def read():
    f=open("User_Database.csv","r")
    print("Database Connected..... Record view Facility")
    print("These are the contents in the database:")
    s=csv.reader(f)
    for i in s:
        for a in i:
            if a != i[-1]:
                print(a,end=",")
            if a == i[-1]:
                print(a)
    f.close()

#append function
def append():
  
    f=open("User_Database.csv","r")
    print("Database Connected.....Record Updation Facility")
    s = csv.reader(f)
    db= []
    for rec in s:
        db.append(rec)

    f.close
    
    f1=open("User_Database.csv","w",newline='')
    w1 = csv.writer(f1)
    Serial_no = int(input("Enter S No.of the record to be updated:"))
    Name = input("Enter Updated Name:")
    DOB = input("Enter Updated Date Of Birth:(DDMMYYYY)")
    Ph = input("Enter Updated Phone Number:")
    city = input("Enter Updated city:")
    password = input("Enter Updated Password:")
    Books_Issued = input("Enter Name of the Books Issued:")
    rec_to_be_upd = [Serial_no,Name,DOB,Ph,city,password,Books_Issued]
    
    db[Serial_no] = rec_to_be_upd
    w1.writerows(db)
    print("Record Appended")
    f1.close()



#search function
def search():
    f=open("User_Database.csv","r")
    print("Database Connected...... Record Search Facility")
    s = csv.reader(f)
    db_view = []
    for rec in s:
        db_view.append(rec)
    word = str(input("Enter what you want to search:"))
    word = word.lower()
    found=0
    print("Searching...")
    
    for rows in db_view:
        for ele in rows:
            ele = str(ele)
            ele = ele.lower()
            if ele == word:
                found = 1
                print(rows)
                break
    if found == 1:
        print("These are the results found")
    if found == 0:
        print("Sorry!No records found")
    f.close()


#delete function
def delete():
    f=open("User_Database.csv","r")
    print("Database Connected.....  Record Deletion Facility")
    s = csv.reader(f)
    reclst=[]
    for i in s:
        reclst.append(i)
    f.close
    f=open("User_Database.csv","w",newline='')
    sl=int(input("Enter Sl_no of the record to be deleted"))
    reclst.pop(sl)
    w = csv.writer(f, delimiter =',')
    w.writerows(reclst)
    f.close()
    print("Record succesfully deleted")


#----------------------------------------------------------------------    
#main
print("-------------------------------------------------------------")
print("                                                             ")
print("                  PROJECT WORK                               ")
print("                  =============                              ")
print("                                                             ")
print("             LIBRARY MANAGEMENT SYSTEM                       ")
print("           =============================                     ")
print("                                                             ")
print("-------------------------------------------------------------")

c='y'
while (c=='y' or c=='Y'):
       print("Welcome to Library Management System!")
       print("1.INSERT RECORDS")
       print("2.VIEW RECORDS")
       print("3.UPDATE RECORDS")
       print("4.SEACRH RECORDS")
       print("5.DELETE RECORDS")
       print("6.Exit")
       ch=int(input("Enter Your Choice (1/2/3/4/5/6 : )"))
       if ch==1:
           write()
       elif ch==2:
           read()
       elif ch==3:
           append()
       elif ch==4:
           search()
       elif ch==5:
           delete()
       elif ch==6:
           break   
       c=input("\n Do you want to continue  y/n :")




