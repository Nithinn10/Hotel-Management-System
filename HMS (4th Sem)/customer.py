import random
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Cust_win:
    def __init__ (self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1140x480+230+220")

###########################Variables#######################################
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()
        self.var_pincode=StringVar()

###########################TITLE############################################
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",17,"bold"),bg="#0d1b28",fg="WHITE",bd=2,relief=RAISED)
        lbl_title.place(x=0,y=0,width=1290,height=50)


        #########################logo##########################################
        img2=Image.open(r"Images\Screenshot 2023-03-23 120327 (1).png")
        img2=img2.resize((100,47),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=49)
        ################################LABEL FRAME############################
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=385,height=480)

        ############################Labels and entries###################################
#cust ref 
        lbl_cust_ref=Label(labelframeleft,text="Customer ref : ",font=("ariel",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=25,textvariable=self.var_ref,font=("ariel",12,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

#cust name
        lbl_cust_ref=Label(labelframeleft,text="Name : ",font=("ariel",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=25,textvariable=self.var_cust_name,font=("ariel",12,"bold"))
        enty_ref.grid(row=1,column=1)

# Gender
        
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=2,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=22)
        combo_gender["value"]=("Male","Female","other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)

        #=========mobilenumber========
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=3,column=0,sticky=W)
        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",12,"bold"),width=25)
        txtmobile.grid(row=3,column=1)
   
        #=========email===========
        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=4,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=25)
        txtEmail.grid(row=4,column=1)

        #==========nationlity===========
        lblNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=5,column=0,sticky=W)
        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=22,state="readonly")
        combo_Nationality["value"]=("Indian","other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=5,column=1)

        #==============id poorf type combobox===========
        lblidpoorf=Label(labelframeleft,font=("arial",12,"bold"),text="id proof:",padx=2,pady=6)
        lblidpoorf.grid(row=6,column=0,sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=22,state="readonly")
        combo_id["value"]=("Adharcard","Driving licence","passport")
        combo_id.current(0)
        combo_id.grid(row=6,column=1)

        #============id number===========
        lblIdnumber=Label(labelframeleft,font=("arial",12,"bold"),text="ID Number:",padx=2,pady=6)
        lblIdnumber.grid(row=7,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=25)
        txtIdNumber.grid(row=7,column=1)

        #==========address=======
        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=8,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=25)
        txtAddress.grid(row=8,column=1)

      #============pincode============
        lblpincode=Label(labelframeleft,font=("arial",12,"bold"),text="PinCode:",padx=2,pady=6)
        lblpincode.grid(row=9,column=0,sticky=W)
        txtpincode=ttk.Entry(labelframeleft,textvariable=self.var_pincode,font=("arial",13,"bold"),width=25)
        txtpincode.grid(row=9,column=1)

        #########################button 1#################################

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=360,width=372,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnReset.grid(row=0,column=3,padx=1)


        ########################TABLE FRAME SEARCH SYSYEM######################################

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & Search System",font=("ariel",12,"bold"),padx=2)
        Table_Frame.place(x=390,y=50,width=730,height=480)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg='#0d1b28',fg='white')
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.var_com_search=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.var_com_search,font=("arial",12,"bold"),width=22,state="readonly")
        combo_Search["value"]=("Name","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.var_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.var_search,font=("arial",13,"bold"),width=22)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search_data,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnSearch.grid(row=0,column=3,padx=2)

        btnshowall=Button(Table_Frame,text="Showall",command=self.fetch_data,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnshowall.grid(row=0,column=4,padx=2)
####################################Show data table######################################################
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=730,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","gender","mobile",
                                            "email","nationality","idproof","idnumber","address","pincode",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)       
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview) 
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")
        self.Cust_Details_Table.heading('pincode',text="Pincode")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column('ref',width=100)
        self.Cust_Details_Table.column('name',width=100)
        self.Cust_Details_Table.column('gender',width=100)
        self.Cust_Details_Table.column('mobile',width=100)
        self.Cust_Details_Table.column('email',width=100)
        self.Cust_Details_Table.column('nationality',width=100)
        self.Cust_Details_Table.column('idproof',width=100)
        self.Cust_Details_Table.column('idnumber',width=100)
        self.Cust_Details_Table.column('address',width=100)
        self.Cust_Details_Table.column('pincode',width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
              
#add data
    def add_data(self):
        if self.var_mobile.get()==""or self.var_email.get()=="":
                 messagebox.showerror("Error","All fields are required",parent=self.root)
        
        else:
                try:  
                   conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                   my_cursor=conn.cursor()
                   my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_id_proof.get(),
                                                                                        self.var_id_number.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_pincode.get()

                                                                                               ))
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success"," Customer details have been added",parent=self.root)
                except Exception as es:
                   messagebox.showwarning("Warning",f"Something went wrong please try again:{str(es)}",parent=self.root)
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute('select*from customer')
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


        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_email.set(row[4]),
        self.var_nationality.set(row[5]),
        self.var_id_proof.set(row[6]),
        self.var_id_number.set(row[7]),
        self.var_address.set(row[8]),
        self.var_pincode.set(row[9])
    def update(self):
        if self.var_mobile.get()=="":
             messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        
        else:
                try:
                        update=messagebox.askyesno("Update","Are you sure update this customer data",parent=self.root)
                        if update>0:
                                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                                my_cursor=conn.cursor()
                                my_cursor.execute("update customer set Name=%s,Gender=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s,PinCode=%s where Ref=%s",(
                                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                                self.var_id_number.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_pincode.get(), 
                                                                                                                                                                self.var_ref.get()  
                                                                                                                                                                 ))
                        else:
                             if not update:
                                return
                        conn.commit()
                        self.fetch_data()
                        conn.close()  

                        messagebox.showinfo("Success","Customer updated successfully",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
             conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
             my_cursor=conn.cursor()
             query="delete from customer where Ref=%s"
             value=(self.var_ref.get(),)
             my_cursor.execute(query,value)
        else:
             if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    

    
    
    
    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set("")
        #self.var_gender.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        #self.var_nationality.set("")
        #self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")
        self.var_pincode.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))  

    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                        self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
        conn.close()
        









if __name__=="__main__":       
         root=Tk()
         obj=Cust_win(root)
         root.mainloop()