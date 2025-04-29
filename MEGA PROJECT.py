from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector
from PIL import ImageTk, Image
######################################################################################################################
mbd=mysql.connector.connect(host='localhost', user='root', password='Arvindshachi25819')
curso= mbd.cursor()
curso.execute('CREATE DATABASE BANK')
MBD=mysql.connector.connect(host='localhost', user='root', password='Arvindshachi25819',database='BANK')
cursor=MBD.cursor()
cursor.execute('CREATE TABLE CLIENTS (acc_no bigint PRIMARY KEY, dob DATE NOT NULL, mobile_no bigint, aadhar_no bigint NOT NULL, cvv_no bigint UNIQUE, name VARCHAR(15) NOT NULL)')
cursor.execute('CREATE TABLE TEMP (acc_no bigint PRIMARY KEY, mobile_no bigint, cvv_no bigint UNIQUE, name VARCHAR(15) NOT NULL)') 
#################################################  MAIN WINDOW  ######################################################
window=Tk()
window.title("Banking Management System")
window.geometry('1366x768')
IMG=Image.open("D:\\gif\\3c8f12b0606ad428cacccc09fd98246c-1.gif")
IMG=IMG.resize((1366,768))
bgi=ImageTk.PhotoImage(IMG)
LBL=Label(window,image=bgi)
LBL.place(x=0,y=0)
LBL.image=IMG
Lbl=Label(window,text="BHARAT BANK ONLINE MANAGEMENT SYSTEM",font=("Arial Black",20),bg="Royal blue",fg="Yellow",width=72,height=2,justify=CENTER)
Lbl.place(x=0,y=0)
LbL=Label(window,text='''CONTACT US :- 9569751231
          TO APPLY FOR ATM / DEBIT CARD / OR CREDIT CARD
            PLEASE VISIT TO ONE OF OUR BRANCHES

            Copyright (C) 2020 . All rights reserved''',font=("Arial black",10),bg="Royal blue",fg="White",width=150,height=6,justify=CENTER) 
LbL.place(x=0,y=581)
frame=Frame(window,height=400,width=700,bg="Royal blue")
frame.place(x=320,y=60)
lbl=Label(frame,text="Sign in to your bank", font=("Arial Black",32),bg="Royal blue",fg="White")
lbl.place(x=129,y=30)
lbl=Label(frame,text="Username",font=("Lucida Handwriting",20),bg="White",height=1,width=14,justify=CENTER,relief=RAISED)
lbl.place(x=95,y=150)
varb=StringVar
ENTR=Entry(frame,textvariable=varb,font=("Lucida Hanwriting",25),width=14,justify=CENTER,relief=RAISED)
ENTR.place(x=353,y=150)
lbl=Label(frame,text="Account no.",font=("Lucida Handwriting",20),bg="White",height=1,width=14,justify=CENTER,relief=RAISED)
lbl.place(x=95,y=210)
pswrd=StringVar
ENTR1=Entry(frame,textvariable=pswrd,font=("Lucida Hanwriting",25),width=14,justify=CENTER,relief=RAISED,show='x')
ENTR1.place(x=353,y=210)
################################################  DEFENITIONS  ######################################################
def empty():
           variable=ENTR.get()
           password=ENTR1.get()
           if (password==""):
                      def clicked():
                                 messagebox.showinfo("Password error","Password cannot be empty")
                                 btn.destroy()
                      img=Image.open("D:\\gif\\iconfinder_info_1282960.png")
                      img=img.resize((29,29))
                      my=ImageTk.PhotoImage(img)
                      btn=ttk.Button(window,image=my,command=clicked)
                      btn.place(x=929,y=270)
                      btn.image=my
           if (variable==""):
                      def clicked():
                                 messagebox.showinfo("Username error","Username cannot be empty")
                                 btn7.destroy()
                      img=Image.open("D:\\gif\\iconfinder_info_1282960.png")
                      img=img.resize((29,29))
                      my=ImageTk.PhotoImage(img)
                      btn7=ttk.Button(window,image=my,command=clicked)
                      btn7.place(x=929,y=210)
                      btn7.image=my
           elif (len(password)<8):
                      def clicked():
                                 messagebox.showinfo("Account no. error","Account no. must contain minimum 8 Characters")
                                 btn6.destroy()
                      img=Image.open("D:\\gif\\iconfinder_info_1282960.png")
                      img=img.resize((29,29))
                      my=ImageTk.PhotoImage(img)
                      btn6=ttk.Button(window,image=my,command=clicked)
                      btn6.place(x=929,y=270)
                      btn6.image=my
           else:
                      variable=str(ENTR.get())
                      password=str(ENTR1.get())
                      sel=cursor.execute('SELECT * FROM CLIENTS ')
                      result=cursor.fetchall()
                      print(result)
                      l=len(result)
                      L1=[]
                      L2=[]
                      L3=[]
                      if result==[]:
                                 messagebox.showinfo("Error","No account exist on drive!!")
                      else:
                                 for i in range(0,6):
                                            if l==1:
                                                       L1.append(result[0][i])
                                            elif l==2:
                                                       L1.append(result[0][i])
                                                       L2.append(result[1][i])
                                            elif l==3:
                                                       L1.append(result[0][i])
                                                       L2.append(result[1][i])
                                                       L3.append(result[2][i])
                      if L1[5]!=variable:
                                 if L2[5]!=variable:
                                            if L3[5]!=variable:
                                                       messagebox.showinfo("Error","No such account exist!!")
                                            else:
                                                       win1=Toplevel()
                                                       win1.geometry('1366x768')
                                                       lbl=Label(win1,text="DASHBOARD",font=("Arial black",30),bg="blue",fg="White",width=50,justify=CENTER)
                                                       lbl.place(x=0,y=0)
                                                       frame3=Frame(win1,height=580,width=700,bg="blue")
                                                       frame3.place(x=340,y=100)
                                                       img=Image.open("D:\\gif\\WA-IMG-20201226-0a9821e5.jpg")
                                                       img=img.resize((140,140))
                                                       my=ImageTk.PhotoImage(img)
                                                       lbl=Label(frame3,image=my)
                                                       lbl.place(x=290,y=10)
                                                       lbl.image=my
                                                       dash="Hello! "+variable
                                                       lbl=Label(frame3,text=dash,font=("Forte",20),bg="blue",fg="white")
                                                       lbl.place(x=230,y=160)
                                                       frame4=Frame(frame3,height=200,width=670,bg="yellow")
                                                       frame4.place(x=10,y=210)
                                                       lbl=Label(frame4,text="Current balance:-",font=("Arial black",30),bg="yellow",fg="Red")
                                                       lbl.place(x=0,y=0)
                                                       rad=str(random.randint(5000,500000))
                                                       conc="Rs "+rad
                                                       lbl=Label(frame4,text=conc,font=("Arial black",60),bg="yellow",fg="Green")
                                                       lbl.place(x=200,y=100)
                                                       def payment():
                                                                  wi=Toplevel()
                                                                  wi.geometry('400x400')
                                                                  wi.configure(background='yellow')
                                                                  lbl=Label(wi,text="Payment details",font=("Arial black",20),fg="Red",bg="Yellow",justify=CENTER)
                                                                  lbl.place(x=100,y=0)
                                                                  lbl=Label(wi,text="Amount",font=("Arial black",20),bg="White",justify=CENTER)
                                                                  lbl.place(x=10,y=50)
                                                                  amount=StringVar
                                                                  entr23=Entry(wi,textvariable=amount,font=("Arial black",20),width=10,justify=CENTER)
                                                                  entr23.place(x=150,y=50)
                                                                  lbl=Label(wi,text="Account no.",font=("Arial black",15),bg="White",justify=CENTER)
                                                                  lbl.place(x=10,y=100)
                                                                  entr=Entry(wi,font=("Arial black",20),width=10,justify=CENTER)
                                                                  entr.place(x=150,y=100)
                                                                  lbl=Label(wi,text="Payment reason",font=("Arial black",20),bg="White",justify=CENTER)
                                                                  lbl.place(x=10,y=150)
                                                                  entr=Entry(wi,font=("Arial black",20),width=10,justify=CENTER)
                                                                  entr.place(x=150,y=150)
                                                                  def Confi():
                                                                             messagebox.showinfo("Payment progress","Payment Done")
                                                                             wi.destroy()
                                                                  btn=Button(wi,text="Confirm",font=("Arial black",20),width=20,justify=CENTER,command=Confi)
                                                                  btn.place(x=10,y=200)
                                                       btn=Button(frame3,text="Make payment",font=("Arial black",28),bg="green",fg="White",width=25,command=payment)
                                                       btn.place(x=10,y=450)
                                 else:
                                            win1=Toplevel()
                                            win1.geometry('1366x768')
                                            lbl=Label(win1,text="DASHBOARD",font=("Arial black",30),bg="blue",fg="White",width=50,justify=CENTER)
                                            lbl.place(x=0,y=0)
                                            frame3=Frame(win1,height=580,width=700,bg="blue")
                                            frame3.place(x=340,y=100)
                                            img=Image.open("D:\\gif\\WA-IMG-20201226-0a9821e5.jpg")
                                            img=img.resize((140,140))
                                            my=ImageTk.PhotoImage(img)
                                            lbl=Label(frame3,image=my)
                                            lbl.place(x=290,y=10)
                                            lbl.image=my
                                            dash="Hello! "+variable
                                            lbl=Label(frame3,text=dash,font=("Forte",20),bg="blue",fg="white")
                                            lbl.place(x=230,y=160)
                                            frame4=Frame(frame3,height=200,width=670,bg="yellow")
                                            frame4.place(x=10,y=210)
                                            lbl=Label(frame4,text="Current balance:-",font=("Arial black",30),bg="yellow",fg="Red")
                                            lbl.place(x=0,y=0)
                                            rad=str(random.randint(5000,500000))
                                            conc="Rs "+rad
                                            lbl=Label(frame4,text=conc,font=("Arial black",60),bg="yellow",fg="Green")
                                            lbl.place(x=200,y=100)
                                            def payment():
                                                       wi=Toplevel()
                                                       wi.geometry('400x400')
                                                       wi.configure(background='yellow')
                                                       lbl=Label(wi,text="Payment details",font=("Arial black",20),fg="Red",bg="Yellow",justify=CENTER)
                                                       lbl.place(x=100,y=0)
                                                       lbl=Label(wi,text="Amount",font=("Arial black",20),bg="White",justify=CENTER)
                                                       lbl.place(x=10,y=50)
                                                       amount=StringVar
                                                       entr23=Entry(wi,textvariable=amount,font=("Arial black",20),width=10,justify=CENTER)
                                                       entr23.place(x=150,y=50)
                                                       lbl=Label(wi,text="Account no.",font=("Arial black",15),bg="White",justify=CENTER)
                                                       lbl.place(x=10,y=100)
                                                       entr=Entry(wi,font=("Arial black",20),width=10,justify=CENTER)
                                                       entr.place(x=150,y=100)
                                                       lbl=Label(wi,text="Payment reason",font=("Arial black",20),bg="White",justify=CENTER)
                                                       lbl.place(x=10,y=150)
                                                       entr=Entry(wi,font=("Arial black",20),width=10,justify=CENTER)
                                                       entr.place(x=150,y=150)
                                                       def Confi():
                                                                  messagebox.showinfo("Payment progress","Payment Done")
                                                                  wi.destroy()
                                                       btn=Button(wi,text="Confirm",font=("Arial black",20),width=20,justify=CENTER,command=Confi)
                                                       btn.place(x=10,y=200)
                                            btn=Button(frame3,text="Make payment",font=("Arial black",28),bg="green",fg="White",width=25,command=payment)
                                            btn.place(x=10,y=450)
                      else:
                                 win1=Toplevel()
                                 win1.geometry('1366x768')
                                 lbl=Label(win1,text="DASHBOARD",font=("Arial black",30),bg="blue",fg="White",width=50,justify=CENTER)
                                 lbl.place(x=0,y=0)
                                 frame3=Frame(win1,height=580,width=700,bg="blue")
                                 frame3.place(x=340,y=100)
                                 img=Image.open("D:\\gif\\WA-IMG-20201226-0a9821e5.jpg")
                                 img=img.resize((140,140))
                                 my=ImageTk.PhotoImage(img)
                                 lbl=Label(frame3,image=my)
                                 lbl.place(x=290,y=10)
                                 lbl.image=my
                                 dash="Hello! "+variable
                                 lbl=Label(frame3,text=dash,font=("Forte",20),bg="blue",fg="white")
                                 lbl.place(x=230,y=160)
                                 frame4=Frame(frame3,height=200,width=670,bg="yellow")
                                 frame4.place(x=10,y=210)
                                 lbl=Label(frame4,text="Current balance:-",font=("Arial black",30),bg="yellow",fg="Red")
                                 lbl.place(x=0,y=0)
                                 rad=str(random.randint(5000,500000))
                                 conc="Rs "+rad
                                 lbl=Label(frame4,text=conc,font=("Arial black",60),bg="yellow",fg="Green")
                                 lbl.place(x=200,y=100)
                                 def payment():
                                            wi=Toplevel()
                                            wi.geometry('400x400')
                                            wi.configure(background='yellow')
                                            lbl=Label(wi,text="Payment details",font=("Arial black",20),fg="Red",bg="Yellow",justify=CENTER)
                                            lbl.place(x=100,y=0)
                                            lbl=Label(wi,text="Amount",font=("Arial black",20),bg="White",justify=CENTER)
                                            lbl.place(x=10,y=50)
                                            amount=StringVar
                                            entr23=Entry(wi,textvariable=amount,font=("Arial black",20),width=10,justify=CENTER)
                                            entr23.place(x=150,y=50)
                                            lbl=Label(wi,text="Account no.",font=("Arial black",15),bg="White",justify=CENTER)
                                            lbl.place(x=10,y=100)
                                            entr=Entry(wi,font=("Arial black",20),width=10,justify=CENTER)
                                            entr.place(x=150,y=100)
                                            lbl=Label(wi,text="Payment reason",font=("Arial black",20),bg="White",justify=CENTER)
                                            lbl.place(x=10,y=150)
                                            entr=Entry(wi,font=("Arial black",20),width=10,justify=CENTER)
                                            entr.place(x=150,y=150)
                                            def Confi():
                                                       messagebox.showinfo("Payment progress","Payment Done")
                                                       wi.destroy()
                                            btn=Button(wi,text="Confirm",font=("Arial black",20),width=20,justify=CENTER,command=Confi)
                                            btn.place(x=10,y=200)
                                 btn=Button(frame3,text="Make payment",font=("Arial black",28),bg="green",fg="White",width=25,command=payment)
                                 btn.place(x=10,y=450)
def register():
    win2=Toplevel()
    win2.geometry('1366x768')
    win2.configure(background="Royal blue")
    lbl=Label(win2,text="",bg="Red",width=200)
    lbl.place(x=0,y=0)
    lbl=Label(win2,text="ALL YOUR BANKING FROM A SINGLE SECURE LOGIN",font=("Calibri",14),bg="Royal blue",fg="White",width=150,justify=CENTER)
    lbl.place(x=0,y=20)
    lbl=Label(win2,text="Self User Creation",font=("Calibri",14),bg="White")
    lbl.place(x=0,y=60)
    frame1=Frame(win2,height=190,width=1320,bg="Yellow",borderwidth=10)
    frame1.place(x=15,y=89)
    lbl=Label(frame1,text='''Please read this before proceeding for self creation
1.Internet Banking User ID,ATM Card no.,ATM pin.
2.Account no. should be linked with the ATM Card.
3.DOB and AADHAR should be present for the account at branch.
4.Your mobile no. should be present for the account at branch.
 *Update the above detail at branch,if not present.''',font=("Arial black",15),bg="yellow",fg="red",justify=LEFT)
    lbl.place(x=0,y=0)
    lbl=Label(win2,text="Account no.",font=("Arial black",15))
    lbl.place(x=15,y=310)
    reg_accno=StringVar
    ent1=Entry(win2,textvariable=reg_accno,font=("Arial black",15),width=20,justify=CENTER,relief=SOLID)
    ent1.place(x=160,y=310)
    lbl=Label(win2,text="Date of birth (yyyy/mm/dd)",font=("Arial black",15))
    lbl.place(x=480,y=310)
    reg_dob=StringVar
    ent2=Entry(win2,textvariable=reg_dob,font=("Arial black",15),width=12,justify=CENTER,relief=SOLID)
    ent2.place(x=790,y=310)
    lbl=Label(win2,text="MOBILE NO.",font=("Arial black",15))
    lbl.place(x=1000,y=310)
    reg_mob=StringVar
    ent3=Entry(win2,textvariable=reg_mob,font=("Arial black",15),width=12,justify=CENTER,relief=SOLID)
    ent3.place(x=1180,y=310)
    lbl=Label(win2,text="AADHAR CARD NUMBER",font=("Arial black",15))
    lbl.place(x=15,y=390)
    reg_aadhar=StringVar
    ent4=Entry(win2,textvariable=reg_aadhar,font=("Arial black",15),width=19,justify=CENTER,relief=SOLID)
    ent4.place(x=315,y=390)
    lbl=Label(win2,text="CVV NUMBER",font=("Arial black",15))
    lbl.place(x=610,y=390)
    reg_cvv=StringVar
    ent5=Entry(win2,textvariable=reg_cvv,font=("Arial black",15),width=10,justify=CENTER,relief=SOLID)
    ent5.place(x=780,y=390)
    lbl=Label(win2,text="NAME",font=("Arial black",15))
    lbl.place(x=1000,y=390)
    reg_name=StringVar
    ent6=Entry(win2,textvariable=reg_name,font=("Arial black",15),width=15,justify=CENTER,relief=SOLID)
    ent6.place(x=1100,y=390)
    lbl=Label(win2,text='''HUMAN VERIFICATION
Write the given code in the box  below :-''',font=("Arial black",15),bg="Royal blue",justify=LEFT)
    lbl.place(x=290,y=500)
    randomno=str(random.randint(1000,9999))
    lbl=Label(win2,text=randomno,font=("Arial black",30),relief=SOLID)
    lbl.place(x=750,y=500)
    reg_verify=StringVar
    entr_1=Entry(win2,textvariable=reg_verify,font=("Arial black",15),width=12,justify=CENTER,relief=SOLID)
    entr_1.place(x=730,y=570)
    check=Checkbutton(win2,text="I understand and agree with the 'terms of use' of the bank",font=("Arial black",15),bg="Royal blue")
    check.place(x=400,y=650)
    def confirmbtn():
               accountno=ent1.get()
               dob=ent2.get()
               mobile=ent3.get()
               aadhar=ent4.get()
               cvvno=ent5.get()
               name=ent6.get()
               if (entr_1.get()==randomno):
                          cursor.execute(f'INSERT INTO CLIENTS (acc_no,dob,mobile_no,aadhar_no,cvv_no,name) VALUES("{accountno}","{dob}","{mobile}","{aadhar}","{cvvno}","{name}")')
                          MBD.commit()
                          win2.destroy()
               else:
                          messagebox.showinfo("ERROR","HUMAN VERIFICATION ERROR")
    btn=Button(win2,text="Confirm",font=("Arial black",25),bg="#32CD32",command=confirmbtn,relief=SOLID)
    btn.place(x=1120,y=620)
def forgotten():
           messagebox.showinfo("Forgotten","Please contact this number :-1800 2045 9872 for changing password")

def tips():
           win5=Toplevel()
           win5.geometry('1366x768')
           lbl=Label(win5,text="Customer Alert !!! [Beware of phishing]",font=("Arial black",40),fg="RED")
           lbl.place(x=10,y=5)
           lbl=Label(win5,text='''
->Do not respond to fraudnlent comminucations asking you your confidentials like A/C
  No, User ID, Password, Card no,etc.
->Fraudulent e-mails contain links of look-alike websites to mislead into entering
  sensitive financial data.
->Bank will never send such communication to customers asking for their
  personal or confidential information.
->Always visit Bank's site instead of clicking on the links provided in emails or third
  party websites.
->Do not respond to pop-up windows asking for your confidential information.''',font=("Arial black",20))
           lbl.place(x=10,y=5)
def reg_atm():
           win6=Toplevel()
           win6.geometry('1366x768')
           win6.configure(background="Royal blue")
           lbl=Label(win6,text="",bg="Red",width=200)
           lbl.place(x=0,y=0)
           lbl=Label(win6,text="ALL YOUR BANKING FROM A SINGLE SECURE LOGIN",font=("Calibri",14),bg="Royal blue",fg="White",width=150,justify=CENTER)
           lbl.place(x=0,y=20)
           lbl=Label(win6,text="Self User Creation",font=("Calibri",14),bg="White")
           lbl.place(x=0,y=60)
           frame1=Frame(win6,height=190,width=1320,bg="Yellow",borderwidth=10)
           frame1.place(x=15,y=89)
           lbl=Label(frame1,text='''Please read this before proceeding for self creation
1.Internet Banking User ID,ATM Card no.,ATM pin.
2.Account no. should be linked with the ATM Card.
3.DOB and AADHAR should be present for the account at branch.
4.Your mobile no. should be present for the account at branch.
 *Update the above detail at branch,if not present.''',font=("Arial black",15),bg="yellow",fg="red",justify=LEFT)
           lbl.place(x=0,y=0)
           lbl=Label(win6,text="Account no.",font=("Arial black",15))
           lbl.place(x=15,y=310)
           reg_accno=StringVar
           ent1=Entry(win6,textvariable=reg_accno,font=("Arial black",15),width=20,justify=CENTER,relief=SOLID)
           ent1.place(x=160,y=310)
           lbl=Label(win6,text=" NAME-OF-OWNER ",font=("Arial black",15))
           lbl.place(x=480,y=310)
           reg_dob=StringVar
           ent2=Entry(win6,textvariable=reg_dob,font=("Arial black",15),width=12,justify=CENTER,relief=SOLID)
           ent2.place(x=790,y=310)
           lbl=Label(win6,text="MOBILE NO.",font=("Arial black",15))
           lbl.place(x=1000,y=310)
           reg_mob=StringVar
           ent3=Entry(win6,textvariable=reg_mob,font=("Arial black",15),width=12,justify=CENTER,relief=SOLID)
           ent3.place(x=1180,y=310)
           lbl=Label(win6,text="CVV NUMBER",font=("Arial black",15))
           lbl.place(x=610,y=390)
           reg_cvv=StringVar
           ent5=Entry(win6,textvariable=reg_cvv,font=("Arial black",15),width=10,justify=CENTER,relief=SOLID)
           ent5.place(x=780,y=390)
           lbl=Label(win6,text='''HUMAN VERIFICATION
Write the given code in the box  below :-''',font=("Arial black",15),bg="Royal blue",justify=LEFT)
           lbl.place(x=290,y=500)
           randomno=str(random.randint(1000,9999))
           lbl=Label(win6,text=randomno,font=("Arial black",30),relief=SOLID)
           lbl.place(x=750,y=500)
           reg_verify=StringVar
           entr_1=Entry(win6,textvariable=reg_verify,font=("Arial black",15),width=12,justify=CENTER,relief=SOLID)
           entr_1.place(x=730,y=570)
           check=Checkbutton(win6,text="I understand and agree with the 'terms of use' of the bank",font=("Arial black",15),bg="Royal blue")
           check.place(x=400,y=650)
           def confirmbtn():
                      accountno=ent1.get()
                      mobile=ent3.get()
                      cvvno=ent5.get()
                      name=ent2.get()
                      if (entr_1.get()==randomno):
                                 cursor.execute(f'INSERT INTO TEMP (acc_no,mobile_no,cvv_no,name) VALUES("{accountno}","{mobile}","{cvvno}","{name}")')
                                 MBD.commit()
                                 win6.destroy()
                                 w=Toplevel()
                                 w.title("Banking Management System")
                                 w.geometry('1366x768')
                                 I=Image.open("D:\\gif\\3c8f12b0606ad428cacccc09fd98246c-1.gif")
                                 I=I.resize((1366,768))
                                 bi=ImageTk.PhotoImage(I)
                                 L=Label(w,image=bi)
                                 L.place(x=0,y=0)
                                 L.image=I
                                 Lbl=Label(w,text="BHARAT BANK ONLINE MANAGEMENT SYSTEM",font=("Arial Black",20),bg="Royal blue",fg="Yellow",width=72,height=2,justify=CENTER)
                                 Lbl.place(x=0,y=0)
                                 LbL=Label(w,text='''CONTACT US :- 9569751231
               TO APPLY FOR ATM / DEBIT CARD / OR CREDIT CARD
                   PLEASE VISIT TO ONE OF OUR BRANCHES

                Copyright (C) 2020 . All rights reserved''',font=("Arial black",10),bg="Royal blue",fg="White",width=150,height=6,justify=CENTER)
                                 LbL.place(x=0,y=581)
                                 frame=Frame(w,height=400,width=700,bg="Royal blue")
                                 frame.place(x=320,y=60)
                                 lbl=Label(frame,text="Sign in to your bank", font=("Arial Black",32),bg="Royal blue",fg="White")
                                 lbl.place(x=129,y=30)
                                 lbl=Label(frame,text="Username",font=("Lucida Handwriting",20),bg="White",height=1,width=14,justify=CENTER,relief=RAISED)
                                 lbl.place(x=95,y=150)
                                 varb=StringVar
                                 ENTR=Entry(frame,textvariable=varb,font=("Lucida Hanwriting",25),width=14,justify=CENTER,relief=RAISED)
                                 ENTR.place(x=353,y=150)
                                 lbl=Label(frame,text="Account no.",font=("Lucida Handwriting",20),bg="White",height=1,width=14,justify=CENTER,relief=RAISED)
                                 lbl.place(x=95,y=210)
                                 pswrd=StringVar
                                 ENTR1=Entry(frame,textvariable=pswrd,font=("Lucida Hanwriting",25),width=14,justify=CENTER,relief=RAISED,show='x')
                                 ENTR1.place(x=353,y=210)
                                 def hello():
                                            variable=ENTR.get()
                                            password=ENTR1.get()
                                            if (password==""):
                                                       def clicked():
                                                                  messagebox.showinfo("Password error","Password cannot be empty")
                                                                  btn.destroy()
                                                       img=Image.open("D:\\gif\\iconfinder_info_1282960.png")
                                                       img=img.resize((29,29))
                                                       my=ImageTk.PhotoImage(img)
                                                       btn=ttk.Button(w,image=my,command=clicked)
                                                       btn.place(x=929,y=270)
                                                       btn.image=my
                                            if (variable==""):
                                                       def clicked():
                                                                  messagebox.showinfo("Username error","Username cannot be empty")
                                                                  btn7.destroy()
                                                       img=Image.open("D:\\gif\\iconfinder_info_1282960.png")
                                                       img=img.resize((29,29))
                                                       my=ImageTk.PhotoImage(img)
                                                       btn7=ttk.Button(w,image=my,command=clicked)
                                                       btn7.place(x=929,y=210)
                                                       btn7.image=my
                                            elif (len(password)<8):
                                                       def clicked():
                                                                  messagebox.showinfo("Account no. error","Account no. must contain minimum 8 Characters")
                                                                  btn6.destroy()
                                                       img=Image.open("D:\\gif\\iconfinder_info_1282960.png")
                                                       img=img.resize((29,29))
                                                       my=ImageTk.PhotoImage(img)
                                                       btn6=ttk.Button(w,image=my,command=clicked)
                                                       btn6.place(x=929,y=270)
                                                       btn6.image=my
                                            else:
                                                       variable=str(ENTR.get())
                                                       password=str(ENTR1.get())
                                                       sel=cursor.execute('SELECT * FROM TEMP ')
                                                       result=cursor.fetchall()
                                                       print(result)
                                                       l=len(result)
                                                       L1=[]
                                                       L2=[]
                                                       L3=[]
                                                       if result==[]:
                                                                  messagebox.showinfo("Error","No account exist on drive!!")
                                                       else:
                                                                  for i in range(0,4):
                                                                             if l==1:
                                                                                        L1.append(result[0][i])
                                                                             elif l==2:
                                                                                        L1.append(result[0][i])
                                                                                        L2.append(result[1][i])
                                                                             elif l==3:
                                                                                        L1.append(result[0][i])
                                                                                        L2.append(result[1][i])
                                                                                        L3.append(result[2][i])
                                                                  if L1[3]!=variable:
                                                                             if L2[3]!=variable:
                                                                                        if L3[3]!=variable:
                                                                                                   messagebox.showinfo("Error","No such account exist!!")
                                                                                        else:
                                                                                                   win1=Toplevel()
                                                                                                   win1.geometry('1366x768')
                                                                                                   lbl=Label(win1,text="DASHBOARD",font=("Arial black",30),bg="blue",fg="White",width=50,justify=CENTER)
                                                                                                   lbl.place(x=0,y=0)
                                                                                                   frame3=Frame(win1,height=580,width=700,bg="blue")
                                                                                                   frame3.place(x=340,y=100)
                                                                                                   img=Image.open("D:\\gif\\WA-IMG-20201226-0a9821e5.jpg")
                                                                                                   img=img.resize((140,140))
                                                                                                   my=ImageTk.PhotoImage(img)
                                                                                                   lbl=Label(frame3,image=my)
                                                                                                   lbl.place(x=290,y=10)
                                                                                                   lbl.image=my
                                                                                                   dash="Hello! "+variable
                                                                                                   lbl=Label(frame3,text=dash,font=("Forte",20),bg="blue",fg="white")
                                                                                                   lbl.place(x=230,y=160)
                                                                                                   frame4=Frame(frame3,height=200,width=670,bg="yellow")
                                                                                                   frame4.place(x=10,y=210)
                                                                                                   lbl=Label(frame4,text="Current balance:-",font=("Arial black",30),bg="yellow",fg="Red")
                                                                                                   lbl.place(x=0,y=0)
                                                                                                   rad=str(random.randint(5000,500000))
                                                                                                   conc="Rs "+rad
                                                                                                   lbl=Label(frame4,text=conc,font=("Arial black",60),bg="yellow",fg="Green")
                                                                                                   lbl.place(x=200,y=100)
                                                                                                   def payment():
                                                                                                              messagebox.showinfo("KYC ERROR!","PLEASE COMPLETE YOUR KYC!")
                                                                                                   btn=Button(frame3,text="Make payment",font=("Arial black",28),bg="green",fg="White",width=25,command=payment)
                                                                                                   btn.place(x=10,y=450)
                                                                             else:
                                                                                        win1=Toplevel()
                                                                                        win1.geometry('1366x768')
                                                                                        lbl=Label(win1,text="DASHBOARD",font=("Arial black",30),bg="blue",fg="White",width=50,justify=CENTER)
                                                                                        lbl.place(x=0,y=0)
                                                                                        frame3=Frame(win1,height=580,width=700,bg="blue")
                                                                                        frame3.place(x=340,y=100)
                                                                                        img=Image.open("D:\\gif\\WA-IMG-20201226-0a9821e5.jpg")
                                                                                        img=img.resize((140,140))
                                                                                        my=ImageTk.PhotoImage(img)
                                                                                        lbl=Label(frame3,image=my)
                                                                                        lbl.place(x=290,y=10)
                                                                                        lbl.image=my
                                                                                        dash="Hello! "+variable
                                                                                        lbl=Label(frame3,text=dash,font=("Forte",20),bg="blue",fg="white")
                                                                                        lbl.place(x=230,y=160)
                                                                                        frame4=Frame(frame3,height=200,width=670,bg="yellow")
                                                                                        frame4.place(x=10,y=210)
                                                                                        lbl=Label(frame4,text="Current balance:-",font=("Arial black",30),bg="yellow",fg="Red")
                                                                                        lbl.place(x=0,y=0)
                                                                                        rad=str(random.randint(5000,500000))
                                                                                        conc="Rs "+rad
                                                                                        lbl=Label(frame4,text=conc,font=("Arial black",60),bg="yellow",fg="Green")
                                                                                        lbl.place(x=200,y=100)
                                                                                        def payment():
                                                                                                   messagebox.showinfo("KYC ERROR!","PLEASE COMPLETE YOUR KYC!")
                                                                                        btn=Button(frame3,text="Make payment",font=("Arial black",28),bg="green",fg="White",width=25,command=payment)
                                                                                        btn.place(x=10,y=450)
                                                                  else:
                                                                             win1=Toplevel()
                                                                             win1.geometry('1366x768')
                                                                             lbl=Label(win1,text="DASHBOARD",font=("Arial black",30),bg="blue",fg="White",width=50,justify=CENTER)
                                                                             lbl.place(x=0,y=0)
                                                                             frame3=Frame(win1,height=580,width=700,bg="blue")
                                                                             frame3.place(x=340,y=100)
                                                                             img=Image.open("D:\\gif\\WA-IMG-20201226-0a9821e5.jpg")
                                                                             img=img.resize((140,140))
                                                                             my=ImageTk.PhotoImage(img)
                                                                             lbl=Label(frame3,image=my)
                                                                             lbl.place(x=290,y=10)
                                                                             lbl.image=my
                                                                             dash="Hello! "+variable
                                                                             lbl=Label(frame3,text=dash,font=("Forte",20),bg="blue",fg="white")
                                                                             lbl.place(x=230,y=160)
                                                                             frame4=Frame(frame3,height=200,width=670,bg="yellow")
                                                                             frame4.place(x=10,y=210)
                                                                             lbl=Label(frame4,text="Current balance:-",font=("Arial black",30),bg="yellow",fg="Red")
                                                                             lbl.place(x=0,y=0)
                                                                             rad=str(random.randint(5000,500000))
                                                                             conc="Rs "+rad
                                                                             lbl=Label(frame4,text=conc,font=("Arial black",60),bg="yellow",fg="Green")
                                                                             lbl.place(x=200,y=100)
                                                                             def payment():
                                                                                        messagebox.showinfo("KYC ERROR!","PLEASE COMPLETE YOUR KYC!")
                                                                             btn=Button(frame3,text="Make payment",font=("Arial black",28),bg="green",fg="White",width=25,command=payment)
                                                                             btn.place(x=10,y=450)
                                 btn=Button(frame,text=" LOG IN ",font=("Lucida Hanwriting",15),bg="#32CD32",fg="White",width=46,command=hello,justify=CENTER,relief=RAISED)
                                 btn.place(x=95,y=270)
                      else:
                                 messagebox.showinfo("ERROR","HUMAN VERIFICATION ERROR")
           btn=Button(win6,text="Confirm",font=("Arial black",25),bg="#32CD32",command=confirmbtn,relief=SOLID)
           btn.place(x=1120,y=620)
##############################################  BUTTONS  ##########################################################
btn=Button(frame,text=" LOG IN ",font=("Lucida Hanwriting",15),bg="#32CD32",fg="White",width=46,justify=CENTER,relief=RAISED,command=empty)
btn.place(x=95,y=270)
btn=Button(frame,text="Forgotten username or password?",font=("Lucida Hanwriting",8),bg="Royal blue",fg="White",width=30,justify=LEFT,relief=FLAT,command=forgotten)
btn.place(x=75,y=315)
btn=Button(frame,text="New to online banking?",font=("Lucida Hanwriting",29),bg="Royal blue",fg="White",width=20,justify=LEFT,relief=FLAT,command=tips)
btn.place(x=115,y=335)
#############################################  REGISTER BUTTONS  ##################################################
btnn=Button(window,text='''REGISTER WITH YOUR SC ATM
/DEBIT CARD AND AADHAR''',font=("Arial black",14),width=27,justify=LEFT,command=register)
btnn.place(x=200,y=490)
imgg=Image.open("D:\\gif\\credit-card.png")
imgg=imgg.resize((70,70))
my=ImageTk.PhotoImage(imgg)
lbl=ttk.Label(window,image=my)
lbl.place(x=560,y=490)
btn4=Button(window,text='''REGISTER WITH YOUR TEMPORARY
ACCOUNT AND CVV NO.''',font=("Arial black",14),width=30,command=reg_atm,justify=LEFT)
btn4.place(x=670,y=490)
img=Image.open("D:\\gif\\iconfinder_26-Smartphone_2674059.gif")
img=img.resize((70,70))
HT=ImageTk.PhotoImage(img)
lbl7=ttk.Label(window,image=HT)
lbl7.place(x=1070,y=490)
###################################################################################################################
window.mainloop()
