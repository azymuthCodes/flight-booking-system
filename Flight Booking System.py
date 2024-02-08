import mysql.connector as ms
import random
#To Login into an account
def Login():
    cr=mydb.cursor()
    ch='y'     #For the While Loop to Iterate the given statements
    v=0       #To Know How Many Times The User Gets The Message "Invalid Credentials"
    while ch=='y':
            global u       #To Use the Username Variable Anywhere in this python file
            print("********Registered User***********")
            u=input("Enter Username")
            pwd=input("Enter Password")
            if len(u)==0 and len(pwd)==0:        #To Find Whether The User has entered Both Username and Password
                print("Please Enter Username And Password")
                ch='y'
            elif len(u)==0:        #To Find Whether the User has entered the Username
                print("Please Enter Username")
                ch='y'
            elif len(pwd)==0:       #To Find Whether the User has entered the Password
                print("Please Enter Password")
                ch='y'
            else:
                cr.execute("select Username,passwd from User")
                row=cr.fetchall()
                for i in row:
                    if u ==i[0] and pwd==i[1]:     #To Check whether the entered credentials matches that of credentials registered by the user
                        print('****Login Successful**** \n Welcome',u)
                        Options()
                        ch='n'
                        v=0
                        break
                    else:
                        continue
                else:     #If the Entered Credentials doesnt match any record
                    print("Invalid Credentials")
                    v=v+1
            if v==2:     #If the user gets the message "Invalid Credentials" twice
                t=input("New Register(y/n)")
                if t=='y':
                    NewUser()
                    v=0
                else:
                    print("Fine")
            elif v>=3:    #If the user gets the message "Invalid Credentials" more than 3 times
                z=input("Forgot Credentials?(y/n)")
                if z=='y':
                    change()
                    v=0
                    break
                elif z=='n':
                    print("OK")
                    v=0
#To Change Username And Password
def change():
    cr=mydb.cursor()
    print("********CHANGE USERNAME AND PASSWORD**********")
    ch='y'    #For the While Loop to Iterate the given statements
    while ch=='y':
        j=int(input('''1]Change Username
2]Change Password
3]Change Username and Password
4]Exit
Choose an option:'''))
        if j==1:     #If the User wants to change the username
            b=input("Enter Previous Username")
            x=input("Enter New Username")
            cr.execute("update User set Username='{}' where Username='{}'".format(x,b))
            mydb.commit()
            print("Username Successfully Changed")
            ch='n'
            Options()
        elif j==2:   #if the User wants to change the password
            p=input("Enter Previous Password")
            a=input("Enter New Password")
            cr.execute("update User set passwd='{}' where passwd='{}'".format(a,p))
            mydb.commit()
            print("Password Successfully Changed")
            ch='n'
            Options()
        elif j==3:   #if the User wants to change both username and password
            Pu=input("Enter Previous Username")
            Nu=input("Enter New Usesrname")
            Pp=input("Enter Previous Password")
            Np=input("Enter New Password")
            cr.execute("update User set username='{}' and passwd'{}' where username='{}' and passwd='{}'".format(Pu,Nu,Pp,Np))
            mydb.commit()
            print("Username and Password Successfully Changed")
            ch='n'
            Options()
        elif j==4:   #If the user wants to exit this option
            Options()
            ch='n'
        else:
            print("Invalid Options")
            ch='y'
#To Display various options for the user to perform
def Options():
    print("********OPTIONS*******")
    ch='y'
    while ch=='y':
        y=int(input('''1]Book A Flight
2]Cancel Ticket
3]Modify Passenger Details
4]Change Username and Password
5]Booking History
6]Log Out
Choose an option'''))
        if y==1:
            booking()
            ch='n'
        elif y==2:
            cancel()
            ch='n'
        elif y==3:
            Modify()
            ch='n'
        elif y==4:
            change()
            ch='n'
        elif y==5:
            bookinghistory()
            ch="n"
        elif y==6:
            print("**Logged Out**")
            print("******Thank You For Using Our Flight Booking System********")
            break
        else:
            print("Invalid Option")
            ch='y'
#To Register for New Users
def NewUser():
    print("*******NEW USER***********")
    global u
    cr=mydb.cursor()
    s=True #To Keep While loop Iterate
    first=input("Enter First Name")
    last=input("Enter Last Name")
    passwd=input("Enter Password")
    while s==True:
        u=input("Enter Username")
        cr.execute("select Username from User")
        row=cr.fetchall()
        for i in row:
            if u in i: #To check whether the given username is taken or not
                print("Username Taken")
                s=True
                break
            else:
                s=False
    cr.execute("insert into User values('{}','{}','{}','{}')".format(u,passwd,first,last))
    mydb.commit()
    print("***Registered****")
#To Book Flight
def booking():
    ch='y'#To keep While Loop Iterate
    mp=int(input("""1]Book Ticket
2]Exit
Choose an option:"""))
    if mp==2:
        Options()
        ch="n"
    print("*********************BOOKING*****************")
    while ch=='y':
        cr=mydb.cursor()
        Dest=input("Enter Destination")
        Board=input("Enter Boarding ")
        TimeA=input("Enter Time of Arrival")
        TimeD=input("Enter Time of Departure")
        Date=input("Enter Date of Journey (dd/mm/yyyy)")
        if len(TimeA)==0 and len(TimeD)==0 and len(Board)==0 and len(Dest)==0 and len(Date)==0: #If the user forgets to enter any one of the details
            print("Please Enter Any One of the Option")
            ch="y"
        elif len(Dest)==0 and len(TimeA)==0 and len(TimeD)==0 and len(Date)==0: #If the user enters only Boarding Place
            cr.execute("select * from flight where Board='{}'".format(Board))
            ch='n'
        elif len(Dest)==0 and len(TimeA)==0 and len(TimeD)==0: #If the User enters Boarding Place and Date of Journey
            cr.execute("select * from flight where Board='{}'and Date='{}'".format(Board,Date))
            ch='n'
        elif len(Dest)==0 and len(TimeA)==0: #If User enters Boarding Place,Time of Departure and Date of Journey
            cr.execute("select * from flight where Board='{}'and TimeD={} and Date='{}'".format(Board,TimeD,Date))
            ch='n'
        elif len(Dest)==0 and len(TimeD)==0: #If User enters Boarding Place,Time of Arrival and Date of Journey
            cr.execute("select * from flight where Board='{}'and TimeA={} and Date='{}'".format(Board,TimeA,Date))
            ch='n'
        elif len(Board)==0 and len(TimeD)==0 and len(TimeD)==0 and len(Date)==0:  #If User enters only Destination
            cr.execute("select * from flight where Dest='{}'".format(Dest))
            ch='n'
        elif len(Board)==0 and len(TimeA)==0 and len(TimeD)==0: #If User enters Destination and Date of Journey
            cr.execute("select * from flight where Dest='{}'and Date='{}'".format(Dest,Date))
            ch='n'
        elif len(Board)==0 and len(TimeA)==0: #If User enters Destination,Time of Departure and Date of Journey
            cr.exeute("select * from flight where Dest='{}'and TimeD='{}'and Date='{}'".format(Dest,TimeD,Date))
            ch='n'
        elif len(Board)==0 and len(TimeD)==0: #If User enters Destination,Time of Arrival and Date of Journey
            cr.execute("select 8 from flight where Dest='{}'and TimeA='{}'and Date='{}'".format(Dest,TimeA,Date))
            ch='n'
        elif len(TimeD)==0:#If User does not  enter Time of Departure
            cr.execute("select * from flight where Dest='{}'and Board='{}'and TimeA='{}'and Date='{}'".format(Dest,Board,TimeA,Date))
            ch='n'
        elif len(TimeA)==0:#If User does not enter Time of Arrival
            cr.execute("select * from flight where Dest='{}'and Board='{}'and TimeD='{}'and Date='{}'".format(Dest,Board,TimeD,Date))
            ch='n'
        elif len(Date)==0 and len(TimeA)==0: #If User Enters Destination,Boarding Place and Time of Departure
            cr.execute("select * from flight where Dest='{}'and Board='{}'and TimeD='{}'".format(Dest,Board,TimeD))
            ch='n'
        elif len(Date)==0 and len(TimeD)==0: #If User Enters Destination,Boarding Place and Time of Arrival
            cr.execute("select * from flight where Dest='{}'and Board='{}'and TimeA='{}'".format(Dest,Board,TimeA))
            ch='n'
        elif len(Date)==0: #If User does not enter Date of Journey
            cr.execute("select * from flight where Dest='{}'and Board='{}'and TimeA='{}'and TimeD='{}'".format(Dest,Board,TimeA,TimeD))
            ch='n'
        else: #If User Enters all details
            cr.execute("select * from flight where Dest='{}'and Board='{}'and TimeA='{}'and TimeD='{}' and Date='{}'".format(Dest,Board,TimeA,TimeD,Date))
            ch='n'
        for i in cr:
            #To print flights according to the User
            print("*******************************************************************************************************************************************")
            print("Destination:",i[0],"Boarding:",i[1],"Time Of Arrival:",i[2],"Time of Departure:",i[3],"Date:",i[4],"Flight No.:",i[5],"Flight Name:",i[6])
            print("********************************************************************************************************************************************")
        passengers()
        break
#To Register Passenger Details
def passengers():
    print("********************PASSENGER DETAILS******************")
    cr=mydb.cursor()
    fno=input("Enter Flight Number")
    p=int(input("Enter How Many Passengers"))
    m=0#To Iterate While Loop
    while m<p:
        fname=input("Enter First Name")
        lname=input("Enter Last Name")
        Age=input("Enter Age")
        DOB=input("Enter Date Of Birth")
        Gender=input("Enter Gender")
        d='y'#To Iterate While Loop
        v=' '#To Enter Flight Class
        while d=='y':
            z=input('''1]Economy
2]Business
Choose Class:''')
            if z=='1':
                v="Economy"
                d='n'
            elif z=='2':
                v="Business"
                d='n'
            else:
                v=' '
                d='n'
        if len(fname)==0 and len(lname)==0 and len(Age)==0 and len(DOB)==0 and len(Gender)==0 and len(v)==0:#If the User Forgets to Enter the Passenger Details
            print("Please Enter All The Details")
            p=p+1
            continue
        elif len(fname)==0 and len(Age)==0 and len(DOB)==0 and len(Gender)==0:
            print("Please Enter All The Details")
            p=p+1
            continue
        elif len(fname)==0 and len(lname)==0 and len(Age)==0 and len(DOB)==0:
            print("Please Enter First Name,Last Name ,Age and Date Of Birth")
            p=p+1
            continue
        elif len(fname)==0 and len(lname)==0 and len(Age)==0 and len(Gender)==0:
            print("Please Enter First Name,Last Name ,Age and Date Of Birth")
            p=p+1
            continue
        elif len(fname)==0 and len(Age)==0 and len(DOB)==0:
            print("Please Enter First Name,Age and Date of Birth")
            p=p+1
            continue
        elif len(fname)==0 and len(Age)==0 and len(Gender)==0:
            print("Please Enter First Name,Age and Gender")
            p=p+1
            continue
        elif len(fname)==0 and len(DOB)==0 and len(Gender)==0:
            print("Please Enter First Name,Date of Birth and Gender")
            p=p+1
            continue
        elif len(lname)==0 and len(Age)==0 and len(DOB)==0:
            print("Please Enter First Name,Last Name ,Age and Date Of Birth")
            p=p+1
            continue
        elif len(lname)==0 and len(Age)==0 and len(Gender)==0:
            print("Please Enter First Name,Last Name ,Age and Date Of Birth")
            p=p+1
            continue
        elif len(lname)==0 and len(DOB)==0 and len(Gender)==0:
            print("Please Enter Last Name,Date of Birth and Gender")
            p=p+1
            continue
        elif len(DOB)==0 and len(Gender)==0 and len(Age)==0:
            print("Please Enter Date of Birth,Gender and Age")
            p=p+1
            continue
        elif len(fname)==0 and len(lname)==0 and len(Age)==0:
            print("Please Enter First Name,Last Name and Age")
            p=p+1
            continue
        elif len(fname)==0 and len(lname)==0 and len(Gender)==0:
            print("Please Enter First Name,Last Name and Gender")
            p=p+1
            continue
        elif len(fname)==0 and len(lname)==0 and len(DOB)==0:
            print("Please Enter First Name,Last Name and Date of Birth")
            p=p+1
            continue
        elif len(fname)==0 and len(Age)==0:
            print("Please Enter First Name and Age")
            p=p+1
            continue
        elif len(fname)==0 and len(DOB)==0:
            print("Please Enter All The Details")
            p=p+1
            continue
        elif len(fname)==0 and len(Gender)==0:
            print("Please Enter All The Details")
            p=p+1
            continue
        elif len(fname)==0 and len(lname)==0:
            print("Please Enter First And Last Name")
            p=p+1
            continue
        elif len(lname)==0 and len(Age)==0:
            print("Please Enter Last Name and Age")
            p=p+1
            continue
        elif len(lname)==0 and len(DOB)==0:
            print("Please Enter Last Name and Date of Birth")
            p=p+1
            continue
        elif len(lname)==0 and len(Gender)==0:
            print("Please Enter Last Name and Gender")
            p=p+1
            continue
        elif len(Age)==0 and len(DOB)==0:
            print("Please Enter Age and Date of Birth")
            p=p+1
            continue
        elif len(Age)==0 and len(Gender)==0:
            print("Please Enter Age and Gender")
            p=p+1
            continue
        elif len(DOB)==0 and len(Gender)==0:
            print("Please Enter Date of Birth and Gender")
            p=p+1
            continue
        elif len(fname)==0:
            print("Please Enter First Name")
            p=p+1
            continue
        elif len(lname)==0:
            print("Please Enter Last Name")
            p=p+1
            continue
        elif len(Age)==0:
            print("Please Enter Age")
            p=p+1
            continue
        elif len(DOB)==0:
            print("Please Enter Date of Birth")
            p=p+1
            continue
        elif len(Gender)==0:
            print("Please Enter Gender")
            p=p+1
            continue
        elif len(v)==0:
            print("Please Choose a Class")
            p=p+1
            continue
        else:
            #For The Seat Number
            l=True
            if m==0:
                while l==True:
                    c=random.randint(1,20)
                    j=random.randrange(65,70,3)
                    l=False
            for q in range(1):
                SeatNo=str(c)+chr(j)
                j=j+1
                #To Check whether the given details are entered already
                cr.execute("insert into Passengers values('{}','{}',{},'{}','{}','{}','{}','{}','{}')".format(fname,lname,Age,DOB,Gender,v,SeatNo,fno,u))
                mydb.commit()
                cr.execute("select count(*) from passengers group by fname,lname,fno")
                row=cr.fetchall()
                for i in row:
                    if i[0]>1:
                        print("***************The Given Details Have Been Already Booked*********************")
                        cr.execute("delete from Passengers where fname='{}'and lname='{}'and fno='{}' and seatno='{}'".format(fname,lname,fno,SeatNo))
                        mydb.commit()
                        p=p+1
                        j=j-1
                        break
                    else:
                        continue
                else:
                    print("*************Booked****************")

        m=m+1
    Options()
#To Modify Passenger Details
def Modify():
    print("*********************MODIFY PASSENGER RECORD***************")
    cr=mydb.cursor()
    z='y'
    while z=='y':
        i=int(input('''1]Change the Flight
2]Update Passenger record
3]Exit
Choose an Option:'''))
        if i==1:
            ch='y'
            while ch=='y':
                p=input("Enter Flight Number")
                if p==0:
                    print("Please Enter Flight Number")
                else:
                    cr.execute("select fno from flight")
                    row=cr.fetchall()
                    num=0
                    for i in row:
                        if i[0]==p:
                            num=0
                            break
                        else:
                            num=num+1
                    if num>0:
                        print("Invalid FlightNo.")
                        ch='y'
                    else:
                        ch='n'
            cr.execute("select * from Flight")
            for i in cr:
                print(i)
            v=0
            q=1
            m=int(input("Enter No.of Passengers to change the flight"))
            while v<m and q!=0:
                l=input("Enter Desired Flight Number To Change")
                u=input("Enter First Name")
                f=input("Enter Last Name")
                if len(l)==0 and len(u)==0 and len(f)==0:
                    print("Please Enter Details")
                    m=m+1
                    continue
                elif len(l)==0 and len(u)==0:
                    print("Please Enter Flight Number and First Name")
                    m=m+1
                    continue
                elif len(l)==0  and len(f)==0:
                    print("Please Enter Flight Number and Last Name")
                    m=m+1
                    continue
                elif  len(u)==0 and len(f)==0:
                    print("Please Enter First Name and Last Name")
                    m=m+1
                    continue
                elif len(l)==0:
                    print("Please Flight Number")
                    m=m+1
                    continue
                elif len(u)==0:
                    print("Please First Name")
                    m=m+1
                    continue
                elif len(f)==0:
                    print("Please Last Name")
                    m=m+1
                    continue
                a=True
                while a==True:
                    i=random.randint(1,20)
                    j=random.randrange(65,70,3)
                    a=False
                for q in range(m):
                    SeatNo=str(i)+chr(j)
                    i=i+1
                    j=j+1
                cr.execute("select fname,lname from passengers")
                row=cr.fetchall()
                for i in row:
                    if i[0]==u and i[1]==f:
                        cr.execute("update Passengers set fno='{}',seatno='{}' where fname='{}' and lname='{}'".format(l,SeatNo,u,f))
                        mydb.commit()
                        print("Updated Details")
                        v=v+1
                        q=1
                    else:
                        print("Sorry The Given Passenger Is Not Booked")
                        q=0
                        break
            z='n'
            Options()
        elif i==2:
            k='y'
            while k=='y':
                fno=input("Enter Flight Number to change passenger record")
                if len(fno)==0:
                    print("Please Enter Flight Number")
                else:
                    cr.execute("select fno from flight")
                    row=cr.fetchall()
                    num=0
                    for i in row:
                        if i[0]==fno:
                            num=0
                            break
                        else:
                            num=num+1
                    if num>0:
                        print("Invalid Flight Number")
                        k='y'
                    else:
                        k='n'
        
            break
            x=0
            w=0
            h=int(input("Enter No.Of Passengers To Update"))
            while x<h and w==0:
                j=int(input('''1]First Name and Last Name
2]Age and Date Of Birth
3]Exit
Choose an option to update:'''))
                if j==1:
                    ch='y'
                    while ch=='y':
                        print("********************************************")
                        PFirst_Name=input("Enter Previous First Name")
                        PLast_Name=input("Enter Previous Last Name")
                        NFirst_Name=input("Enter First Name")
                        NLast_Name=input("Enter Last Name")
                        if len(PFirst_Name)==0 and len(PLast_Name)==0 and len(NFirst_Name)==0 and len(NLast_Name)==0:
                            print("Please Enter All Details")
                            ch='y'
                        if len(PFirst_Name)==0 and len(PLast_Name)==0 and len(NFirst_Name)==0 :
                            print("Please Enter Previous First and Last Name and New First Name")
                            ch='y'
                        elif len(PFirst_Name)==0 and len(PLast_Name)==0 and len(NLast_Name)==0:
                            print("Please Enter Previous First and Last Name and New Last Name")
                            ch='y'
                        elif len(PLast_Name)==0 and len(NFirst_Name)==0 and len(NLast_Name)==0:
                            print("Please Enter Previous Last Name and New First And Last Name")
                            ch='y'
                        elif len(PFirst_Name)==0 and len(PLast_Name)==0:
                            print("Please Previous First and Last Name")
                            ch='y'
                        elif len(PLast_Name)==0 and len(NFirst_Name)==0:
                            print("Please Enter Previous Last Name and New First Name")
                            ch='y'
                        elif len(NFirst_Name)==0 and len(NLast_Name)==0:
                            print("Please Enter New First and Last Name")
                            ch='y'
                        elif len(PFirst_Name)==0:
                            print("Please Enter Previous First Name")
                            ch='y'
                        elif len(PLast_Name)==0:
                            print("Please Enter Previous Last Name")
                            ch='y'
                        elif len(NFirst_Name)==0:
                            print("Please Enter New First Name")
                            ch='y'
                        elif len(NLast_Name)==0:
                            print("Please Enter New Last Name")
                            ch='y'
                        else:
                            ch='n'
                        cr.execute("select fname,lname from passengers")
                        row=cr.fetchall()
                        for i in row:
                            if i[0]==PFirst_Name and i[1]==PLast_Name:
                                cr.execute("update Passengers set fname='{}' where fname='{}' and fno='{}'".format(NFirst_Name,PFirst_Name,fno))
                                mydb.commit()
                                cr.execute("update Passengers set lname='{}' where lname='{} and fno='{}''".format(NLast_Name,PLast_Name,fno))
                                mydb.commit()
                                print("Updated Details")
                                x=x+1
                            else:
                                print("Sorry The Given Passenger Is Not Booked")
                                x=0
                                break
                        if x==0:
                            break
                elif j==2:
                    ch='y'
                    while ch=='y':
                        print("***************************")
                        n=input("Enter First Name")
                        l=input("Enter Last Name")
                        a=int(input("Enter Age"))
                        dob=input("Enter Date Of Birth")
                        cr.execute("select fname,lname from passengers")
                        row=cr.fetchall()
                        for i in row:
                            if i[0]==n and i[1]==l:
                                cr.execute("update Passengers set Age={} where fname='{}' and lname='{}'".format(a,n,l))
                                mydb.commit()
                                cr.execute("update Passengers set DOB='{}' where fname='{}' and lname='{}'".format(dob,n,l))
                                mydb.commit()
                                print("Updated Details")
                                x=x+1
                            else:
                                print("Sorry The Given Passenger Is Not Booked")
                                w=1
                                break
                        ch='n'
                elif j==3:
                     Options()
                     w=1

                else:
                    print("Invalid Option")
                    x=0
        elif i==3:
            Options()
            k="n"
            break
        else:
            print("Invalid Option")
                   
def cancel():
    print("***********************CANCEL TICKET**********************")
    cr=mydb.cursor()
    o='y'
    mp=int(input("""1]Cancel Ticket
2]Exit
Choose an option:"""))
    if mp==2:
        Options()
        o="n"
    while o=='y':
        p=input("Enter Flight Number")
        if len(p)==0:
            print("Please Enter Flight Number")
        else:
            cr.execute("select fno from flight")
            row=cr.fetchall()
            num=0
            for i in row:
                if i[0]==p:
                    num=0
                    break
                else:
                    num=num+1
            if num>0:
                print("Invalid Flight Number")
                o='y'
            else:
                o='n'
                q=int(input("Enter No.of Passengers to Cancel"))
                for i in range(0,q):
                    ch='y'
                    while ch=='y':
                        fname=input("Enter First Name")
                        lname=input("Enter Last Name")
                        if len(fname)==0 and len(lname)==0:
                            print("Please Enter First and Last Name")
                            ch='y'
                        elif len(fname)==0:
                            print("Please Enter First Name")
                            ch='y'
                        elif len(lname)==0:
                            print("Please Enter Last Name")
                            ch='y'
                        else:
                            ch='n'
                        cr.execute("delete from Passengers where fname='{}' and lname='{}' and fno='{}'".format(fname,lname,p))
                        mydb.commit()
                        print("********")
                        print("Cancelled")
                        print("*********")
                Options()
def bookinghistory():
    cr=mydb.cursor()
    global u
    print("*********************************BOOKING HISTORY********************************")
    cr.execute("select * from passengers,flight where passengers.username='{}' and passengers.fno=flight.fno".format(u))
    for i in cr:
        print("********************************************")
        print("First Name:",i[0])
        print("Last Name:",i[1])
        print("Age:",i[2])
        print("Date Of Birth:",i[3])
        print("Gender:",i[4])
        print("Class:",i[5])
        print("SeatNo:",i[6])
        print("FlightNo.:",i[7])
        print("username:",i[8])
        print("Boarding:",i[9])
        print("Destination:",i[10])
        print("Time Of Depature:",i[11])
        print("Time of Arrival:",i[12])
        print("Date Of Journey:",i[13])
        print("Flight No:",i[14])
        print("Flight Name:",i[15])
        print("************************************")
    Options()
mydb=ms.connect(host="localhost",user="root",passwd="vignesh3",database="project")
print(''' A PROJECT DONE BY NIHAL AND VIGNESH
        OF GRADE 12A-M''')
print('''********************************
*                                                 *
* ASIS Flight Booking System  *
*                                                 *
********************************''')
ch='y'
while ch=='y':
    x=int(input('''1]New User
2]Registered User
3]Exit
Enter A Choice:'''))
    if x==1:
        NewUser()
        Options()
        ch='n'
    elif x==2:
        Login()
        ch='n'
    elif x==3:
         print("******Thank You For Using Our Flight Booking System********")
         ch='n'
    else:
        print("Invalid Option")
        ch='y'
