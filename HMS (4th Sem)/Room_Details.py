import random
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Room_Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System") 
        self.root.geometry("1140x480+230+220")

    #Variables
        self.var_Floor=StringVar()
        self.var_RoomNo=StringVar()
        self.var_Category=StringVar()


         ###########################TITLE############################################
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",17,"bold"),bg="#0d1b28",fg="WHITE",bd=2,relief=RAISED)
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
        labelframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("ariel",12,"bold"),padx=2)
        labelframeright.place(x=5,y=50,width=380,height=480)

        #Floor
        lbl_Floor=Label(labelframeright,text="Floor:",font=("ariel",12,"bold"),padx=2,pady=6)
        lbl_Floor.grid(row=0,column=0,sticky=W)
        
        
        entry_Floor=ttk.Entry(labelframeright,textvariable=self.var_Floor,width=25,font=("ariel",12,"bold"))
        entry_Floor.grid(row=0,column=1,sticky=W)
         #room no
        lbl_Floor=Label(labelframeright,text="room no:",font=("ariel",12,"bold"),padx=2,pady=6)
        lbl_Floor.grid(row=2,column=0,sticky=W)

      
        entry_Floor=ttk.Entry(labelframeright,textvariable=self.var_RoomNo,width=25,font=("ariel",12,"bold"))
        entry_Floor.grid(row=2,column=1,sticky=W)
         #room type
        label_room=Label(labelframeright,font=("arial",12,"bold"),text="Category:",padx=2,pady=6)
        label_room.grid(row=3,column=0,sticky=W)
        combo_room=ttk.Combobox(labelframeright,textvariable=self.var_Category,font=("arial",12,"bold"),width=23)
        combo_room["value"]=("Gold    (1999)  ","Diamond     (3999)","Platinum   (4999)")
        combo_room.current(0)
        combo_room.grid(row=3,column=1,sticky=W)


        ####################Buttons##################
        
        btn_frame=Frame(labelframeright,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=360,width=372,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnReset.grid(row=0,column=3,padx=1)

        
        ########################TABLE FRAME SEARCH SYSYEM######################################

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="SHOW ROOM DETAILS",font=("ariel",10,"bold"),padx=2)
        Table_Frame.place(x=400,y=55,width=730,height=480) 

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.Cust_Details_Table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomType",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)       
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview) 
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("floor",text="floor")
        self.Cust_Details_Table.heading("roomno",text="room no")
        self.Cust_Details_Table.heading("roomType",text="room type")
        

        

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column('floor',width=100)
        self.Cust_Details_Table.column('roomno',width=100)
        self.Cust_Details_Table.column('roomType',width=100)
        

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
    def add_data(self):
        if self.var_Floor.get()=="" or self.var_Category.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                try:  
                   conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                   my_cursor=conn.cursor()
                   my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                        self.var_Floor.get(),
                                                                                        self.var_RoomNo.get(),
                                                                                        self.var_Category.get()
                                                                                        
                                                
                                                                                        

                                                                                     ))
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success"," New Room Added Successfully",parent=self.root)
                except Exception as es:
                   messagebox.showwarning("Warning",f"Something went wrong please try again:{str(es)}",parent=self.root)
    #fetch data 
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute('select * from details')
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
                conn.close() 
          # set cursor
        
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_Floor.set(row[0]),
        self.var_RoomNo.set(row[1]), 
        self.var_Category.set(row[2])
        
    def update(self):
        if self.var_Floor.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)

        else:
        
              conn = mysql.connector.connect(host="localhost", username="root", password="nithin1234#",
                                                   database="project")
              my_cursor = conn.cursor()
              my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",( 
                                                                                        self.var_Floor.get(),
                                                                                        self.var_RoomNo.get(),
                                                                                        self.var_Category.get()
                                                                                         ))
                
              conn.commit()
              self.fetch_data()
              conn.close()

              messagebox.showinfo("Success", "Customer updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer",
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="nithin1234#",
                                           database="project")
            my_cursor = conn.cursor()
            query = "delete from details where RoomNo=%s"
            value = (self.var_RoomNo.get(),)
            my_cursor.execute(query, value)
            messagebox.showinfo("Deleted","Deleted Successfully",parent=self.root)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()        



    def reset(self):
       self.var_RoomNo.set("")
       self.var_Floor.set("")
       self.var_Category.set("")


if __name__=="__main__":
    root=Tk()
    obj=Room_Details(root)
    root.mainloop()
