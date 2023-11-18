import random
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os
from tkcalendar import  DateEntry



class Check_In:
    def __init__ (self,root):
        self.root=root
        
        self.root.title("Hotel Management System")
        self.root.geometry("1140x480+230+220")
        
        ######################variables##############################
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_category=StringVar()
        self.var_floorno=StringVar()
        self.var_roomavailable=StringVar()
        self.var_noofdays=StringVar()
        self.var_price=StringVar()
        self.var_advance=StringVar()
     
      
        ###########################TITLE############################################
        lbl_title=Label(self.root,text="CHECK IN DETAILS",font=("times new roman",17,"bold"),bg="#0d1b28",fg="WHITE",bd=2,relief=RAISED)
        lbl_title.place(x=0,y=0,width=1290,height=50)


        #########################logo##########################################
        img=Image.open(r"Images\Screenshot 2023-03-23 120327 (1).png")
        img=img.resize((100,47),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lblimg=Label(self.root,image=self.photoimg,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=49)
        ################################LABEL FRAME############################
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("ariel",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=385,height=480)
        
                ################################LABEL FRAME############################
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Check-In Details",font=("ariel",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=385,height=480)
        
        
                ############################Labels and entries###################################
#cust contact
        lbl_cust_contact=Label(labelframeleft,text="Contact:",font=("ariel",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,width=18,font=("ariel",12,"bold"),textvariable=self.var_contact)
        entry_contact.grid(row=0,column=1,sticky=W)
        
        #Fetch data btn
        btnFetch=Button(labelframeleft,text="Fetch data",command=self.Fetch_contact,font=("ariel",8,"bold"),bg="#0d1b28",fg="WHITE",width=7)
        btnFetch.place(x=320,y=1)
        
        #check in date
        check_out_date=Label(labelframeleft,text="Check In Date : ",font=("ariel",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=1,column=0,sticky=W)

        Calender=ttk.Entry(labelframeleft,width=20,textvariable=self.var_checkin,font=("ariel",12,"bold"))
        Calender.grid(row=1,column=1)
        
        #check out date
        check_in_date=Label(labelframeleft,text="Check Out Date : ",font=("ariel",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=2,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=20,textvariable=self.var_checkout,font=("ariel",12,"bold"))
        enty_ref.grid(row=2,column=1)

# Room Type
        
        label_room=Label(labelframeleft,font=("arial",12,"bold"),text="Category:",padx=2,pady=6)
        label_room.grid(row=3,column=0,sticky=W)


        conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
        my_cursor=conn.cursor()
        
        combo_room=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=20)
        combo_room["value"]=("Gold    (1999)  ","Diamond     (3999)","Platinum   (4999)")
        combo_room.current(0)
        combo_room.grid(row=3,column=1,sticky=W)


        
        #=========Floor Numner========
        lblFloorno=Label(labelframeleft,font=("arial",12,"bold"),text="Floor Number:",padx=2,pady=6)
        lblFloorno.grid(row=4,column=0,sticky=W)
        conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute('select Floor from details')
        idk=my_cursor.fetchall()
        combo_room=ttk.Combobox(labelframeleft,textvariable=self.var_floorno,font=("arial",12,"bold"),width=20)
        combo_room["value"]=idk
        combo_room.current(0)
        combo_room.grid(row=4,column=1,sticky=W)

        
        #=========Room Number========
        lblRoomno=Label(labelframeleft,font=("arial",12,"bold"),text="Room Number:",padx=2,pady=6)
        lblRoomno.grid(row=5,column=0,sticky=W)
        #txtRoomno=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=23)
        #txtRoomno.grid(row=5,column=1)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute('select roomNo from details ')
        rows=my_cursor.fetchall()
        
      
        combo_roomno=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=20)
        combo_roomno["value"]=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=5,column=1,sticky=W)

        
        #=========Price========
        lblPrice=Label(labelframeleft,font=("arial",12,"bold"),text="Price:",padx=2,pady=6)
        lblPrice.grid(row=7,column=0,sticky=W)
        txtPrice=ttk.Entry(labelframeleft,textvariable=self.var_price,font=("arial",12,"bold"),width=23)
        txtPrice.grid(row=7,column=1)

        
        # No.of days
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No.of days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",12,"bold"),width=23)
        txtNoOfDays.grid(row=6,column=1)
        
        #
        
        lblapproximate=Label(labelframeleft,font=("arial",12,"bold"),text="Advance:",padx=2,pady=6)
        lblapproximate.grid(row=8,column=0,sticky=W)
        txtapproximate=ttk.Entry(labelframeleft,textvariable=self.var_advance,font=("arial",12,"bold"),width=23)
        txtapproximate.grid(row=8,column=1)
        
        ######################
        
        ####################Buttons##################
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=360,width=372,height=40)

        btnAdd=Button(btn_frame,text="Book",command=self.add_data,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnReset.grid(row=0,column=3,padx=1)
        
        

        
        ##############################Bill Button#####################################
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("ariel",11,'bold'),bg="#0d1b28",fg="WHITE",width=8)
        btnBill.grid(row=9,column=0,padx=1,sticky=W)
        
        ##############Right side image###############################
        
        img2=Image.open(r"Images\loginbg.jpg")
        img2=img2.resize((300,180),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=2,relief=RIDGE)
        lblimg2.place(x=820,y=55,width=300,height=180)
        
        


        ########################TABLE FRAME SEARCH SYSYEM######################################

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & Search System",font=("ariel",10,"bold"),padx=2)
        Table_Frame.place(x=395,y=230,width=730,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg='#0d1b28',fg='white')
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.var_com_search=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.var_com_search,font=("arial",12,"bold"),width=22,state="readonly")
        combo_Search["value"]=("Contact","roomavailable")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.var_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.var_search,font=("arial",13,"bold"),width=22)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search_data,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnSearch.grid(row=0,column=3,padx=2)

        btnshowall=Button(Table_Frame,text="Showall",command=self.fetch_data,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnshowall.grid(row=0,column=4,padx=2)
        
        #####################################Left Side Box#################################################
        fetch_Frame=LabelFrame(self.root,bd=2,relief=RIDGE)
        fetch_Frame.place(x=395,y=55,width=420,height=175)
        
        lblName=Label(fetch_Frame,text="Name :",font=("ariel",10,"bold"))
        lblName.place(x=0,y=0)
                
        lblEmail=Label(fetch_Frame,text="Email :",font=("ariel",10,"bold"))
        lblEmail.place(x=0,y=30)
        
        lblAddress=Label(fetch_Frame,text="Address :",font=("ariel",10,"bold"))
        lblAddress.place(x=0,y=60)
        
        lblIdProof=Label(fetch_Frame,text="Id Proof :",font=("ariel",10,"bold"))
        lblIdProof.place(x=0,y=90)
        
        lblIdNumber=Label(fetch_Frame,text="Id Number :",font=("ariel",10,"bold"))
        lblIdNumber.place(x=0,y=120)

        
        

        

      ####################################Show data table######################################################
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=700,height=160)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("contact","check-in","check-out","category",
                                            "floorno","roomno","noofdays","advance","price",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)       
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview) 
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("contact",text="Contact")
        self.Cust_Details_Table.heading("check-in",text="Check-In")
        self.Cust_Details_Table.heading("check-out",text="Check-Out")
        self.Cust_Details_Table.heading("category",text="Category")
        self.Cust_Details_Table.heading("floorno",text="Floor-no")
        self.Cust_Details_Table.heading("roomno",text="Room no")
        self.Cust_Details_Table.heading("noofdays",text="No.of Days")
        
        self.Cust_Details_Table.heading("price",text="Price")
        self.Cust_Details_Table.heading("advance",text="Advance")
        

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column('contact',width=100)
        self.Cust_Details_Table.column('check-in',width=100)
        self.Cust_Details_Table.column('check-out',width=100)
        self.Cust_Details_Table.column('category',width=100)
        self.Cust_Details_Table.column('floorno',width=100)
        self.Cust_Details_Table.column('roomno',width=100)
        self.Cust_Details_Table.column('noofdays',width=100)
        
        self.Cust_Details_Table.column('price',width=100)
        self.Cust_Details_Table.column('advance',width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
 #fetch details fun
    def Fetch_contact(self):
                if self.var_contact.get()=="":
                        messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                        my_cursor=conn.cursor()
                        query=('select Name from customer where mobile=%s ')
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
           
                        if row==None:
                                messagebox.showerror("Error","No data found",parent=self.root)
                                
                        else:
                                conn.commit()
                                conn.close()
                        
                showDataframe=Frame(self.root,bd=2,relief=RIDGE,padx=2)
                showDataframe.place(x=395,y=55,width=420,height=175)
                
                lblName=Label(showDataframe,text="Name :",font=("ariel",10,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(showDataframe,text=row,font=("ariel",10,"bold"))
                lbl.place(x=60,y=0)
                
                #email
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select email from customer where mobile=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
           


                
                lblGender=Label(showDataframe,text="Email :",font=("ariel",10,"bold"))
                lblGender.place(x=0,y=30)
                
                lbl2=Label(showDataframe,text=row,font=("ariel",10,"bold"))
                lbl2.place(x=60,y=30)
                
                #address
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select Address from customer where mobile=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lbladdress=Label(showDataframe,text="Address :",font=("ariel",10,"bold"))
                lbladdress.place(x=0,y=60)
                
                lbl3=Label(showDataframe,text=row,font=("ariel",10,"bold"))
                lbl3.place(x=60,y=60)
                # id proof
                
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select idproof from customer where mobile=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
           

                
                lblIdproof=Label(showDataframe,text="Id Proof :",font=("ariel",10,"bold"))
                lblIdproof.place(x=0,y=90)
                
                lbl4=Label(showDataframe,text=row,font=("ariel",10,"bold"))
                lbl4.place(x=60,y=90)
                
                #id Number
                
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select idnumber from customer where mobile=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                conn.commit()
                conn.close()

                
                lblidnumber=Label(showDataframe,text="Id Number :",font=("ariel",10,"bold"))
                lblidnumber.place(x=0,y=120)
                
                lbl5=Label(showDataframe,text=row,font=("ariel",10,"bold"))
                lbl5.place(x=80,y=120)
          
    def add_data(self):
        if self.var_contact.get()==""or self.var_noofdays.get()=="":
                 messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                try:  
                   conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                   my_cursor=conn.cursor()
                   my_cursor.execute("insert into checkin  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_category.get(),
                                                                                        self.var_floorno.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_noofdays.get(),
                                                                                        self.var_price.get(),
                                                                                        self.var_advance.get()
                                                
                                                                                        

                                                                                               ))
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success"," Customer details have been added",parent=self.root)
                except Exception as es:
                   messagebox.showwarning("Warning",f"Something went wrong please try again:{str(es)}",parent=self.root)


        
    #fetch data 
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute('select*from checkin')
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                        self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
        conn.close() 
    
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]


        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_category.set(row[3]),
        self.var_floorno.set(row[4]),
        self.var_roomavailable.set(row[5]),
        self.var_noofdays.set(row[6]),
        self.var_advance.set(row[7]),
        self.var_price.set(row[8])
        
     
     
    def update(self):
        if self.var_contact.get()=="":
                messagebox.showerror("Error","Please enter valid number",parent=self.root)
        else:
              conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
              my_cursor=conn.cursor()
              my_cursor.execute("update checkin set check_in=%s,check_out=%s,category=%s,floor_no=%s,roomavailable=%s,noofdays=%s,advance=%s,price=%s where Contact=%s",(
                                                                                                                                                        self.var_checkin.get(),
                                                                                                                                                        self.var_checkout.get(),
                                                                                                                                                        self.var_category.get(),
                                                                                                                                                        self.var_floorno.get(),
                                                                                                                                                        self.var_roomavailable.get(),
                                                                                                                                                        self.var_noofdays.get(),
                                                                                                                                                        self.var_advance.get(),
                                                                                                                                                        self.var_price.get(),
                                                                                                                                                        self.var_contact.get()
                                                                                                                                                  ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Update","Changes Saved Successfully",parent=self.root)
            
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
             conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
             my_cursor=conn.cursor()
             query=("delete from checkin where roomavailable=%s")
             value=(self.var_roomavailable.get(),)
             my_cursor.execute(query,value)
        else:
             if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
             
            
     
        
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_category.set("")
        self.var_floorno.set("")
        self.var_roomavailable.set("")
        self.var_noofdays.set("")
        self.var_advance.set("")
        self.var_price.set("")
    
    #search
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from checkin where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                        self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
        conn.close()
        
        
    
    
        
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")  
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if(self.var_category.get()=="Gold"):
           q1=float(1999)
           q2=float(self.var_noofdays.get())
           q3=float(q1*q2)
           Ad="Rs."+str("%.2f"%((q3/3)))
           TT="Rs."+str("%.2f"%(q3))
           self.var_advance.set(Ad)
           self.var_price.set(TT)
        

        elif(self.var_category.get()=="Platinum"):
           q1=float(4999)
           q2=float(self.var_noofdays.get())
           q3=float(q1*q2)
           Ad="Rs."+str("%.2f"%((q3/3)))
           TT="Rs."+str("%.2f"%(q3))
           self.var_advance.set(Ad)
           self.var_price.set(TT)
           
        else:
           q1=float(3999)
           q2=float(self.var_noofdays.get())
           q3=float(q1*q2)
           Ad="Rs."+str("%.2f"%((q3/3)))
           TT="Rs."+str("%.2f"%(q3))
           self.var_advance.set(Ad)
           self.var_price.set(TT)
                
 
        

if __name__=="__main__":       
         root=Tk()
         obj=Check_In(root)
         root.mainloop()