from os import system
import os
from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_win
from Room_Details import Room_Details
from Check_IN import Check_In
from check_out import Check_Out



class HotelManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        



        img2=Image.open(r"Images\Screenshot 2023-03-23 120327 (1).png")
        img2=img2.resize((225,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=40,width=225,height=150)

        #**********************************************************************************#
        lbl_title=Label(self.root,text="HOTELPRO",font=("times new roman",40,"bold"),bg="#0d1b28",fg="white",bd=2,relief=RAISED)
        lbl_title.place(x=0,y=0,width=1550,height=50)

#**********************************************************************************#
        main_frame=Frame(self.root,bd=2,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620 )
#**********************************************************************************#
        lbl_menu=Label(self.root,text="MENU",font=("times new roman",20,"bold"),bg="#0d1b28",fg="white",bd=2,relief=RIDGE)
        lbl_menu.place(x=0,y=191,width=230)
#**********************************************************************************#
        btn_frame=Frame(self.root,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=227.5,width=230,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER DETAILS",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="#0d1b28",fg="white",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.room_details,width=22,font=("times new roman",14,"bold"),bg="#0d1b28",fg="white",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)
        

        details_btn=Button(btn_frame,text="CHECK IN",command=self.checkin,width=22,font=("times new roman",14,"bold"),bg="#0d1b28",fg="white",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="CHECK OUT",command=self.check_out,width=22,font=("times new roman",14,"bold"),bg="#0d1b28",fg="white",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="#0d1b28",fg="white",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

        #**************************Right Side Image********************************************************#

        img3=Image.open(r"Images\rhema-kallianpur-uocSnWMhnAs-unsplash.jpg")
        img3=img3.resize((1310,690),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(self.root,image=self.photoimg3,bd=2,relief=RIDGE)
        lblimg1.place(x=225,y=50,width=1310,height=690)
         #**************************Down Image********************************************************#

        img5=Image.open(r"Images\marten-bjork-n_IKQDCyrG0-unsplash.jpg")
        img5=img5.resize((228,270),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(self.root,image=self.photoimg5,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=228,height=270)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)
    
    def checkin(self):
        self.new_window=Toplevel(self.root)
        self.app=Check_In(self.new_window)    
    
    def logout(self):
        self.root.destroy()
        os.system("login.py")
    
    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_Details(self.new_window)
    
    def check_out(self):
        self.new_window=Toplevel(self.root)
        self.app=Check_Out(self.new_window)






if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

