''' This project demonstration how a Bank Management System or an ATM works. It contains functionality performed by an ATM. '''

import tkinter as tk
from tkinter import ttk
import  tkinter.messagebox as tmsg
import mysql.connector as con
import datetime as dt

def menu():
    main=tk.Tk()
    main.title("TrustBank-Main Menu")
    main.geometry("1000x600")

    icon=tk.PhotoImage(file='images.png')
    main.iconphoto(False, icon)

    a=ac_value.get()
    p=pin_value.get()

    frame_cb=tk.Frame(main)
    frame_cp=tk.Frame(main)
    frame_wm=tk.Frame(main)
    frame_dm=tk.Frame(main)
    frame_tm=tk.Frame(main)
    frame_th=tk.Frame(main)

    con1=con.connect(host="localhost",user="root",password="shubham@1234",database="trustbank")
    cur1=con1.cursor()

    sql="select balance from cust where acno={} and pin='{}'".format(a,p)
    cur1.execute(sql)
    rec=cur1.fetchone()
    for i in range(0,len(rec)):
        balance=rec[i]

    
    def check_balance():
        
        con1=con.connect(host="localhost",user="root",password="shubham@1234",database="trustbank")
        cur1=con1.cursor()

        sql="select balance from cust where acno={} and pin='{}'".format(a,p)
        cur1.execute(sql)
        rec=cur1.fetchone()
        #for i in range(0,len(rec)):
        #    balance=rec[i]
        t="Your Current balance is : Rs."+str(rec[0])
        l1=tk.Label(frame_cb,text=t,font="lucida 15 bold",padx=10,pady=40)
        l1.pack(padx=300,pady=260)

        frame_cb.pack()

        frame_cp.pack_forget()
        frame_wm.pack_forget()
        frame_dm.pack_forget()
        frame_tm.pack_forget()
        frame_th.pack_forget()
    
    def change_pin():
        np=tk.Label(frame_cp,text="Enter New PIN : ",font="lucida 15 bold",padx=20,pady=20)        
        np.pack(padx=20,pady=20)

        np_value=tk.StringVar()

        np_entry=tk.Entry(frame_cp,textvariable=np_value,font="lucida 15 bold")
        np_entry.pack(padx=20,pady=20)

        rnp=tk.Label(frame_cp,text="RE-Enter New PIN : ",font="lucida 15 bold",padx=20,pady=20)        
        rnp.pack(padx=20,pady=20)

        rnp_value=tk.StringVar()

        rnp_entry=tk.Entry(frame_cp,textvariable=rnp_value,font="lucida 15 bold")
        rnp_entry.pack(padx=20,pady=20)

        def change():
            n=np_value.get()
            rn=rnp_value.get()

            if n==rn:
                sql1="update cust set pin='{}' where acno={}".format(rn,a)
                cur1.execute(sql1)
                con1.commit()
                con1.close()
                tmsg.showinfo("Modify...","PIN Changed Sucessfully.")
            else:
                tmsg.showerror("ERROR","New PIN and RE-Enter PIN not MATCHED.")
    
        btn=tk.Button(frame_cp,text="Change PIN",font="lucida 15 bold",padx=20,pady=20,command=change)
        btn.pack(padx=20,pady=20)

        frame_cp.pack(pady=70)

        frame_cb.pack_forget()
        frame_wm.pack_forget()
        frame_dm.pack_forget()
        frame_tm.pack_forget()
        frame_th.pack_forget()
    
    def withdraw_money():
        wm=tk.Label(frame_wm,text="Enter Amount : ",font="lucida 15 bold",padx=20,pady=20)
        wm.pack(padx=20,pady=20)

        wm_value=tk.IntVar()

        wm_entry=tk.Entry(frame_wm,textvariable=wm_value,font="lucida 15 bold")
        wm_entry.pack(padx=20,pady=20)

        date=dt.date.today()
        time=dt.datetime.now()
        tm=time.strftime("%H:%M:%S")

        def withdraw():
            amt=wm_value.get()

            sql="select balance from cust where acno={} and pin='{}'".format(a,p)
            cur1.execute(sql)
            rec=cur1.fetchall()
            for i in range(len(rec)):
                b=rec[i][0]
            bal=b-amt

            if amt<=b:
                sql1="update cust set balance={} where acno={}".format(bal,a)
                cur1.execute(sql1)
                con1.commit()
                dr='Money Withdrawn'
                sql2="insert into history (acno,descr,date,time,withdrawals,balance) values({},'{}','{}','{}',{},{})".format(a,dr,date,tm,amt,bal)
                cur1.execute(sql2)
                con1.commit()
                msg="Withdrawn sucessfully.\n\nYour Current balance is : "+str(bal)
                tmsg.showinfo("Balance",msg)
                con1.close()
            else:
                tmsg.showwarning("Balance","Insufficient Balance.")

            
        btn=tk.Button(frame_wm,text="Withdraw",font="lucida 15 bold",command=withdraw,padx=20,pady=20)
        btn.pack(padx=20,pady=20)
        
        frame_wm.pack(pady=140)
        
        frame_cb.pack_forget()
        frame_cp.pack_forget()
        frame_dm.pack_forget()
        frame_tm.pack_forget()
        frame_th.pack_forget()
    
    def deposti_money():
        dm=tk.Label(frame_dm,text="Enter Amount : ",font="lucida 15 bold",padx=20,pady=20)
        dm.pack(padx=20,pady=20)

        dm_value=tk.IntVar()

        dm_entry=tk.Entry(frame_dm,textvariable=dm_value,font="lucida 15 bold")
        dm_entry.pack(padx=20,pady=20)

        date=dt.date.today()
        time=dt.datetime.now()
        tm=time.strftime("%H:%M:%S")

        def deposit():
            amt=dm_value.get()

            sql="select balance from cust where acno={} and pin='{}'".format(a,p)
            cur1.execute(sql)
            rec=cur1.fetchall()
            for i in range(len(rec)):
                b=rec[i][0]
            bal=b+amt

            sql1="update cust set balance={} where acno={}".format(bal,a)
            cur1.execute(sql1)
            con1.commit()
            dr='Money Deposit'
            sql2="insert into history (acno,descr,date,time,deposits,balance) values({},'{}','{}','{}',{},{})".format(a,dr,date,tm,amt,bal)
            cur1.execute(sql2)
            con1.commit()
            msg="Deposited sucessfully.\n\nYour Current balance is : "+str(bal)
            tmsg.showinfo("Balance",msg)
            con1.close()            
            

        btn=tk.Button(frame_dm,text="Deposit",font="lucida 15 bold",command=deposit,padx=20,pady=20)
        btn.pack(padx=20,pady=20)
        
        frame_dm.pack(pady=140)
        
        frame_cb.pack_forget()
        frame_cp.pack_forget()
        frame_wm.pack_forget()
        frame_tm.pack_forget()
        frame_th.pack_forget()
    
    def transfer_money():
        racno=tk.Label(frame_tm,text="Enter A/C of Reciver : ",font="lucida 15 bold",padx=20,pady=20)        
        racno.pack(padx=20,pady=20)

        racno_value=tk.IntVar()

        racno_entry=tk.Entry(frame_tm,textvariable=racno_value,font="lucida 15 bold")
        racno_entry.pack(padx=20,pady=20)

        amt=tk.Label(frame_tm,text="Enter Amount : ",font="lucida 15 bold",padx=20,pady=20)        
        amt.pack(padx=20,pady=20)

        amt_value=tk.IntVar()

        amt_entry=tk.Entry(frame_tm,textvariable=amt_value,font="lucida 15 bold")
        amt_entry.pack(padx=20,pady=20)

        def transfer():
            ac=racno_value.get()
            am=amt_value.get()

            sql1="select acno, balance from cust where acno={}".format(ac)
            cur1.execute(sql1)
            rec=cur1.fetchall()
            
            for i in rec:
                if ac==a:
                    tmsg.showwarning("A/C Number","Sender and Reciver has same A/C Number.")
                    ans=1
                    break
                elif am>balance:
                    tmsg.showwarning("Amount","Insufficient Amount.")
                    ans=1
                    break
                elif i[0]==ac:
                    sql2="update cust set balance=balance+{} where acno={}".format(am,ac)
                    sql3="update cust set balance=balance-{} where acno={}".format(am,a)
                    cur1.execute(sql2)
                    cur1.execute(sql3)
                    con1.commit()

                    dr_s="Money Transfered"
                    date=dt.date.today()
                    time=dt.datetime.now()
                    tm=time.strftime("%H:%M:%S")
                    sql_s="select balance from cust where acno={}".format(a)
                    cur1.execute(sql_s)
                    rec_s=cur1.fetchone()
                    for i in range(len(rec_s)):
                        b1=rec_s[0]
                    
                    sql_h_s="insert into history (acno,descr,date,time,r_acno,tranfer_amt,balance) values({},'{}','{}','{}',{},{},{})".format(a,dr_s,date,tm,ac,am,b1)
                    cur1.execute(sql_h_s)
                    con1.commit()

                    dr_r="Money Recived"
                    date=dt.date.today()
                    time=dt.datetime.now()
                    tm=time.strftime("%H:%M:%S")
                    sql_r="select balance from cust where acno={}".format(ac)
                    cur1.execute(sql_r)
                    rec_r=cur1.fetchone()
                    for i in range(len(rec_r)):
                        b2=rec_r[0]
                    
                    sql_h_r="insert into history (acno,descr,date,time,r_acno,tranfer_amt,balance) values({},'{}','{}','{}',{},{},{})".format(ac,dr_r,date,tm,a,am,b2)
                    cur1.execute(sql_h_r)
                    con1.commit()

                    con1.close()
                    msg="Rs."+str(am)+" Transfered Sucessfully."
                    tmsg.showinfo("Transfer",msg)
                    ans=1
                    break
            if ans==0:
                tmsg.showwarning("Transfer","Invalid Account Number.")

        btn=tk.Button(frame_tm,text="Transfer",font="lucida 15 bold",command=transfer,padx=20,pady=20)
        btn.pack(padx=20,pady=20)

        frame_tm.pack(pady=70)

        frame_cb.pack_forget()
        frame_cp.pack_forget()
        frame_wm.pack_forget()
        frame_dm.pack_forget()
        frame_th.pack_forget()
    
    def transection_history():
        table=ttk.Treeview(frame_th,columns=('Description','Date','Time','Withdrawals','Deposits','A/C','T. Amt.','Balance'),show="headings")
        table.heading("Description",text="Description")
        table.column("0",width=300,anchor="center")
        table.heading("Date",text="Date")
        table.column("1",width=120,anchor="center")
        table.heading("Time",text="Time")
        table.column("2",width=120,anchor="center")
        table.heading("Withdrawals",text="Withdrawals")
        table.column("3",width=170,anchor="center")
        table.heading("Deposits",text="Deposits")
        table.column("4",width=170,anchor="center")
        table.heading("A/C",text="A/C No.")
        table.column("5",width=100,anchor="center")
        table.heading("T. Amt.",text="Transfer Amount")
        table.column("6",width=170,anchor="center")
        table.heading("Balance",text="Balance")
        table.column("7",width=170,anchor="center")
        table.pack(padx=20,pady=20)

        sql1="select * from history where acno={}".format(a)
        cur1.execute(sql1)
        rech=cur1.fetchall()
        for i in range(len(rech)):
            table.insert(parent="",index=i,values=(rech[i][1],rech[i][2],rech[i][3],rech[i][4],rech[i][5],rech[i][6],rech[i][7],rech[i][8]))

        frame_th.pack(pady=170)

        frame_cb.pack_forget()
        frame_cp.pack_forget()
        frame_wm.pack_forget()
        frame_dm.pack_forget()
        frame_tm.pack_forget()
    
    head=tk.Label(main,text="PLEASE SELECT A OPTION",font="lucida 20 bold")
    head.pack()
    head.config()

    f1=tk.Frame(main)

    b1=tk.Button(f1,text="Check Balance",font="lucida 16 bold",command=check_balance)
    b1.pack(side="left",padx=27,pady=10)
    b1.config()
    b2=tk.Button(f1,text="Change PIN",font="lucida 16 bold",command=change_pin)
    b2.pack(side="left",padx=27,pady=10)
    b2.config()
    b3=tk.Button(f1,text="Withdraw Money",font="lucida 16 bold",command=withdraw_money)
    b3.pack(side="left",padx=27,pady=10)
    b3.config()
    b4=tk.Button(f1,text="Deposit Money",font="lucida 16 bold",command=deposti_money)
    b4.pack(side="left",padx=27,pady=10)
    b4.config()
    b5=tk.Button(f1,text="Transfor Money",font="lucida 16 bold",command=transfer_money)
    b5.pack(side="left",padx=27,pady=10)
    b5.config()
    b7=tk.Button(f1,text="Transection History",font="lucida 16 bold",command=transection_history)
    b7.pack(side="left",padx=27,pady=10)
    b7.config()

    f1.pack(side="top",fill="x")

    main.mainloop()

def check():
    con1=con.connect(host="localhost",user="root",password="shubham@1234",database="trustbank")
    cur1=con1.cursor()
    sql="select acno,pin from cust"
    cur1.execute(sql)
    rec=cur1.fetchall()
    
    a=ac_value.get()
    p=pin_value.get()

    for i in rec:
        if a==i[0] and p==i[1]:
            root.destroy()
            menu()
            break
    else:
        tmsg.showerror("ERROR!","Invalid A/C Number OR PIN Number.")

def acno():
    con1=con.connect(host="localhost",user="root",password="shubham@1234",database="trustbank")
    cur1=con1.cursor()
    sql="select count(*) from cust"
    cur1.execute(sql)
    rec=cur1.fetchall()
    for i in rec:
        return 10000+i[0]+1

def newac():
    root.destroy()
    cr=tk.Tk()
    cr.geometry("700x700")
    cr.maxsize(700,700)
    cr.minsize(700,700)
    cr.title("New Account")

    icon=tk.PhotoImage(file='images.png')
    cr.iconphoto(False, icon)
    
    tk.Label(cr,text="Fill the Form to Create your New Account",font="lucida 20 underline").place(x=100,y=20)
    
    na=tk.Label(cr,text="Enter your Full Name : ",font="lucida 15 bold")
    na.place(x=10,y=70)

    pn=tk.Label(cr,text="Create PIN : ",font="lucida 15 bold")
    pn.place(x=10,y=120)

    add=tk.Label(cr,text="Enter your Address : ",font="lucida 15 bold")
    add.place(x=10,y=170)

    ct=tk.Label(cr,text="Enter City : ",font="lucida 15 bold")
    ct.place(x=10,y=220)

    st=tk.Label(cr,text="Enter State(e.g. DL for Delhi) : ",font="lucida 15 bold")
    st.place(x=10,y=270)

    pcode=tk.Label(cr,text="Enter PIN Code : ",font="lucida 15 bold")
    pcode.place(x=10,y=320)

    mob=tk.Label(cr,text="Enter your Mobile No. : ",font="lucida 15 bold")
    mob.place(x=10,y=370)

    gn=tk.Label(cr,text="Enter your Gender(M/F) : ",font="lucida 15 bold")
    gn.place(x=10,y=420)

    dob=tk.Label(cr,text="Enter your Date of Birth(YYYY/MM/DD) : ",font="lucida 15 bold")
    dob.place(x=10,y=470)

    occ=tk.Label(cr,text="Enter your Occupation : ",font="lucida 15 bold")
    occ.place(x=10,y=520)

    bal=tk.Label(cr,text="Enter Initial Amount : ",font="lucida 15 bold")
    bal.place(x=10,y=570)

    na_value=tk.StringVar()
    pn_value=tk.StringVar()
    add_value=tk.StringVar()
    ct_value=tk.StringVar()
    st_value=tk.StringVar()
    pcode_value=tk.StringVar()
    mob_value=tk.StringVar()
    gn_value=tk.StringVar()
    dob_value=tk.StringVar()
    occ_value=tk.StringVar()
    bal_value=tk.IntVar()

    na_entry=tk.Entry(cr,textvariable=na_value,font="lucida 15 bold")
    na_entry.place(x=400,y=70)

    pn_entry=tk.Entry(cr,textvariable=pn_value,font="lucida 15 bold")
    pn_entry.place(x=400,y=120)

    add_entry=tk.Entry(cr,textvariable=add_value,font="lucida 15 bold")
    add_entry.place(x=400,y=170)

    ct_entry=tk.Entry(cr,textvariable=ct_value,font="lucida 15 bold")
    ct_entry.place(x=400,y=220)

    st_entry=tk.Entry(cr,textvariable=st_value,font="lucida 15 bold")
    st_entry.place(x=400,y=270)

    pcode_entry=tk.Entry(cr,textvariable=pcode_value,font="lucida 15 bold")
    pcode_entry.place(x=400,y=320)

    mob_entry=tk.Entry(cr,textvariable=mob_value,font="lucida 15 bold")
    mob_entry.place(x=400,y=370)

    gn_entry=tk.Entry(cr,textvariable=gn_value,font="lucida 15 bold")
    gn_entry.place(x=400,y=420)

    dob_entry=tk.Entry(cr,textvariable=dob_value,font="lucida 15 bold")
    dob_entry.place(x=400,y=470)

    occ_entry=tk.Entry(cr,textvariable=occ_value,font="lucida 15 bold")
    occ_entry.place(x=400,y=520)

    bal_entry=tk.Entry(cr,textvariable=bal_value,font="lucida 15 bold")
    bal_entry.place(x=400,y=570)

    con1=con.connect(host="localhost",user="root",password="shubham@1234",database="trustbank")
    cur1=con1.cursor()

    def create():
        ac=acno()
        name=na_value.get()
        pinno=pn_value.get()
        address=add_value.get()
        city=ct_value.get()
        state=st_value.get()
        pincode=pcode_value.get()
        phone=mob_value.get()
        gender=gn_value.get()
        date=dob_value.get()
        occupation=occ_value.get()
        balance=bal_value.get()

        if name=="" and pincode=="" and address=="":
            tmsg.showerror("ERROR","Fill All The Fields.")
        else:
            sql="insert into cust values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{})".format(ac,name,pinno,address,city,state,pincode,phone,gender,date,occupation,balance)
            cur1.execute(sql)
            con1.commit()
            con1.close()

            t="Your A/C Created Sucessfully.\n\nYour Account number is : "+str(acno()-1)
            tmsg.showinfo("A/C Number",t)

    btn=tk.Button(cr,text="Create",font="lucida 20 bold",command=create)
    btn.place(x=260,y=620)

    cr.mainloop()


#_____main_____#

root=tk.Tk()
root.title("TrustBank")
root.geometry("500x600")
root.maxsize(500,600)
root.minsize(500,600)

icon=tk.PhotoImage(file='images.png')
root.iconphoto(False, icon)

wel=tk.Label(root,text="Welcome...",font="lucida 20 bold",)
wel.place(x=60,y=20)

user=tk.PhotoImage(file='user.png')
img=tk.Label(image=user)
img.place(x=140,y=65)

acn=tk.Label(root,text="Enter A/C No. : ",font="lucida 16 bold")
acn.place(x=80,y=320)
pin=tk.Label(root,text="Enter PIN No. : ",font="lucida 16 bold")
pin.place(x=80,y=370)

ac_value=tk.IntVar()
pin_value=tk.StringVar()

tk.Entry(root,textvariable=ac_value).place(x=250,y=325)
tk.Entry(root,textvariable=pin_value).place(x=250,y=375)

b1=tk.Button(root,text="Log in",font="lucida 12 bold",command=check)
b1.place(x=200,y=430)

oor=tk.Label(root,text="OR",font="lucida 12 bold")
oor.place(x=215,y=500)

b2=tk.Button(root,text="Create New Account",font="lucida 12 bold",command=newac)
b2.place(x=150,y=550)

root.mainloop()
#___________________________________THE_END___________________________________#