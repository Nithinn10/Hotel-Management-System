import os
from tkinter import*
from tkinter import ttk
import token
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

from customer import Cust_win



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    
    
    
    




class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        

        self.bg=ImageTk.PhotoImage(file=r"Images\hggyu.jpg")
        

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=140,width=340,height=450)

        img1=Image.open(r"E:\PROJECT\Images\5087579.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=635,y=145,width=75,height=75)

        get_str=Label(frame,text="WELCOME TO HOTELPRO",font=("times new roman",14,"bold"),fg="white",bg="black")
        get_str.place(x=47,y=85)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=40,y=135)

        self.txtuser=ttk.Entry(frame,font=('times new roman',15,"bold"))
        self.txtuser.place(x=40,y=170,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=220)

        self.txtpass=ttk.Entry(frame,font=('times new roman',15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)
        

        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#0d1b28",activeforeground="white",activebackground="#063970")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registration

        registerbtn=Button(frame,command=self.register_window,text="New User Registration",font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=160)

        #Forget Password

        loginbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        loginbtn.place(x=4.8,y=380,width=160)
        
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)
    
    
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
    
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nithin1234#",database='project')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                         self.txtuser.get(),
                                                                                         self.txtpass.get()   
                                                                                 ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("Yes/No","Access only admin")
                if open_main>0:
                    messagebox.showinfo("Welcome",f"Welcome {self.txtuser.get()}",parent=self.root)
                    os.system("main.py")
                else:
                    if not open_main:
                        return
                    
            conn.commit()
            conn.close()
    #####################################reset password##################################################
    def reset_pass(self):
        if self.txtnewpass.get() != self.txtrepass.get():
            messagebox.showerror("Error","Password doesn't match",parent=self.root2)
         
        elif self.txtconf.get()!= self.var_conf.get():
            messagebox.showerror("Error","Favorite thing doesn't match",parent=self.root2)
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nithin1234#",database='project')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and security=%s")
            value=(self.txtuser.get(),self.txtconf.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
             messagebox.showerror("Error","Please enter correct email",parent=self.root)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txtnewpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Password registered successfully")
            
            
            
        
    
    ######################################forget Password#########################################
    def forgot_password_window(self):
        
        
        if self.txtuser.get()=="":
            messagebox.showerror("Error","enter staffid to reset pasword",parent=self.root)
        
        else:
            #Forget pass
            self.var_conf=StringVar()
            self.var_newpass=StringVar()
            self.var_repass=StringVar()
            
            conn=mysql.connector.connect(host="localhost",user="root",password="nithin1234#",database='project')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)
            
            if row==None:
                messagebox.showerror("Error","Enter valide username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("forget password")
                self.root2.geometry("340x450+500+140")
                self.root2.configure(bg="#0d1b28")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",14,"bold"),fg="white",bg="#0d1b28")
                l.place(x=10,y=10,relwidth=1)
                
                username=Label(self.root2,text="Username",font=("times new roman",13,"bold"),fg="white",bg="#0d1b28")
                username.place(x=10,y=45)
                
                self.txtuser=ttk.Entry(self.root2,font=('times new roman',13,"bold"))
                self.txtuser.place(x=10,y=90,width=270)
                
                
                conf=Label(self.root2,text="Enter Your Favourite Thing",font=('times new roman',13,"bold"),fg="white",bg="#0d1b28")
                conf.place(x=10,y=130)
                
                self.txtconf=ttk.Entry(self.root2,textvariable=self.var_conf,font=('times new roman',13,"bold"))
                self.txtconf.place(x=10,y=170,width=270)
                

                
                newpass=Label(self.root2,text="Enter new Password",font=("times new roman",13,"bold"),fg="white",bg="#0d1b28")
                newpass.place(x=10,y=210)
                
                self.txtnewpass=ttk.Entry(self.root2,textvariable=self.var_newpass,font=('times new roman',13,"bold"),show="*")
                self.txtnewpass.place(x=10,y=250,width=270)
                
                repass=Label(self.root2,text="Confirm Password",font=("times new roman",13,"bold"),fg="white",bg="#0d1b28")
                repass.place(x=10,y=285)
                
                self.txtrepass=ttk.Entry(self.root2,textvariable=self.var_repass,font=("times new roman",13,"bold"),show="*")
                self.txtrepass.place(x=10,y=330,width=270)
                
                Button(self.root2,width=10,text="Submit",command=self.reset_pass,font=('times new roman',15,"bold"),fg="white",bg="#0d1b28").place(x=100,y=380)
  
                
                
              
                

            
     ##########################################################################################################################################################################    
                
                               
                        
            
            



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        
        ######################variables################################
        self.var_staffid=StringVar()
        self.var_email=StringVar()
        self.var_name=StringVar()
        self.var_password=StringVar()
        self.var_repass=StringVar()
        self.var_check=IntVar()
        self.var_conf=StringVar()
        
        
        
        #################background Image####################################################################
        self.bg=ImageTk.PhotoImage(file=r"Images\hggyu.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
############################Frame##################################################
        frame=Frame(self.root,bg="white")
        frame.place(x=300,y=55,width=800,height=600)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",15,"bold"),fg="#0d1b28",bg="white")
        register_lbl.place(x=300,y=20)
        
        ###############Label Entry ##############################
        staffId=Label(frame,text="Staff ID",font=("times new roman",15,"bold"),fg="#0d1b28",bg="white")
        staffId.place(x=40,y=75)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_staffid,font=('times new roman',15,"bold"))
        self.txtuser.place(x=40,y=110,width=270)

        email=lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="#0d1b28",bg="white")
        email.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=('times new roman',15,"bold"))
        self.txtuser.place(x=40,y=195,width=270)

        name=lbl=Label(frame,text="Enter Name",font=("times new roman",15,"bold"),fg="#0d1b28",bg="white")
        name.place(x=40,y=235)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_name,font=('times new roman',15,"bold"))
        self.txtuser.place(x=40,y=275,width=290)

        conf=lbl=Label(frame,text="Enter Your Favourite Thing",font=("times new roman",15,"bold"),fg="#0d1b28",bg="white")
        conf.place(x=40,y=305)

        self.txtconf=ttk.Entry(frame,textvariable=self.var_conf,font=('times new roman',15,"bold"))
        self.txtconf.place(x=40,y=345,width=290)
        
        password=lbl=Label(frame,text="Enter password",font=("times new roman",15,"bold"),fg="#0d1b28",bg="white")
        password.place(x=40,y=385)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_password,font=('times new roman',15,"bold"),show="*")
        self.txtpass.place(x=40,y=425,width=290)
        
        repass=lbl=Label(frame,text="Re-enter Password",font=("times new roman",15,"bold"),fg="#0d1b28",bg="white")
        repass.place(x=40,y=465)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_repass,font=('times new roman',15,"bold"),show="*")
        self.txtpass.place(x=40,y=500,width=290)
        
        ###########acknowledgement###########
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",15,"bold"),fg="#0d1b28",bg="white")
        self.checkbtn.place(x=380,y=500)
        
        
        ##################################Right side image####################################################
        img2=Image.open(r"Images\marten-bjork-n_IKQDCyrG0-unsplash.jpg")
        img2=img2.resize((400,400),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg1=Label(self.root,image=self.photoimg2,bd=2,relief=RIDGE)
        lblimg1.place(x=680,y=160,width=400,height=400)
        
        
        ##################################Buttons################################
        Button(frame,width=10,text="Submit",command=self.register_data,font=('times new roman',15,"bold"),fg="white",bg="#0d1b28").place(x=40,y=540)
        Button(frame,width=10,text="Log in",command=self.login,font=('times new roman',15,"bold"),fg="white",bg="#0d1b28").place(x=400,y=540)
        

        
    ###################Function declaration################################
    def register_data(self):
        if self.var_staffid.get()==""or self.var_email.get()==""or self.var_conf.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_password.get()!=self.var_repass.get():
            messagebox.showerror("Error","Password doesn't match",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        elif self.var_conf.get()==0:
            messagebox.showerror("Error","Please enter the confirmaion",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nithin1234#",database='project')
            my_cursor=conn.cursor()
            query=("select*from register where staffid =%s")
            value=(self.var_staffid.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already registered!")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",(
                                                                                      self.var_staffid.get(), 
                                                                                      self.var_email.get(),
                                                                                      self.var_name.get(),
                                                                                      self.var_conf.get(),
                                                                                      self.var_password.get()
                                            
                                                                                      
                                                                                       
                                                                                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered Successfully")

    def login(self):
        self.root.destroy()
        os.system("login.py")   
     #++++++++++++++++++++++++++++++++++++++++++++++++++++++++#           
class HotelManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        img1=Image.open(r"E:\PROJECT\Images\delmd-monson-2208-hor-clsc.jpg")
        img1=img1.resize((1500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=150)
        

        img2=Image.open(r"E:\PROJECT\Images\Article-3_986x660.webp")
        img2=img2.resize((230,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=150)

        #**********************************************************************************#
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=2,relief=RAISED)
        lbl_title.place(x=0,y=140,width=1550,height=50)

#**********************************************************************************#
        main_frame=Frame(self.root,bd=2,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620 )
#**********************************************************************************#
        lbl_menu=Label(self.root,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_menu.place(x=0,y=191,width=230)
#**********************************************************************************#
        btn_frame=Frame(self.root,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=227.5,width=230,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER DETAILS",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM", width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)
        

        details_btn=Button(btn_frame,text="CHECK IN",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="CHECK OUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

        #**************************Right Side Image********************************************************#

        img3=Image.open(r"E:\PROJECT\Images\JoinMR_photo_121918.webp")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(self.root,image=self.photoimg3,bd=2,relief=RIDGE)
        lblimg1.place(x=225,y=191,width=1310,height=590)
         #**************************Down Image********************************************************#

        img5=Image.open(r"Images\junior-montalvan-2W2G1Dla7qk-unsplash.jpg")
        img5=img5.resize((228,270),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(self.root,image=self.photoimg5,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=228,height=270)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)



if __name__=="__main__":
    main()