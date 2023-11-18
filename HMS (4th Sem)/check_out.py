from ast import List
import random,os
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tempfile


class Check_Out:
    def __init__ (self,root):
        self.root=root
        
        self.root.title("Hotel Management System")
        self.root.geometry("1530x800+0+0")
        
        ########Variables#1##########################
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_category=StringVar()
        self.var_floorno=StringVar()
        self.var_roomavailable=StringVar()
        self.var_noofdays=StringVar()
        self.var_price=StringVar()
        self.var_advance=StringVar()
        self.var_payable=DoubleVar()
        ######################################################______________________________________________
        #======================================#Variable2#+++++++++++++++++++++++++++++++++++++++++++++++++++++#
        self.c_name=StringVar()
        self.c_email=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=DoubleVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        
       
       
        ###################################################################################
        
        
        
        
        #Prosuct Catogories list
        
        self.Category=["Select Option","Vegiterian","Non-Vegiterian","Drinks"]
        self.SubCatVegiterian=["Salads"]
        self.Salads=["Avocado Shrimp Salad","Honey Mint Winter Salad","Carrot salad with black grape","Spicy Raw Mango Salad","Green Bean Salad"]
        self.price_Avacado=250
        self.price_honey=380
        self.price_raw=370
        self.price_carrot=320
        self.price_bean=310
        
        self.SubCatNonvegiterian=["Home Classics","Fire Grills"]
        self.Classics=["Biriyani","meals","Pulihora","Masala dosa","Palak paneer","Hyderabadi biryani","Vada pav","Upma","Chemmeen Porichathu","Karimeen Pollichathu","Alleppey Chicken Curry"]
        self.price_biriyani=200
        self.price_meals=100
        self.price_pulihora=140
        self.price_Masaladosa=60
        self.price_PalakPaneer=145
        self.price_Hydrabadibiriyani=400
        self.price_Vadapav=40
        self.price_Chemeenporichathu=130
        self.price_Upma=40
        self.price_Karimeenpollichathu=100
        self.price_Alappychickencurry=170
        
        self.Grills=["Shish Kebab","Kofta Kebab","Gambari Al Nar","Shish Taouk"]
        self.price_Shish=350
        self.price_Kofta=320
        self.price_Gambari=360
        self.price_Tauok=360
       

        
        self.SubCatDrinks=["Hot","Coolers"]
        
        self.Hot=["Select Option","Tea","Coffee","Green Tea","Hot Chocolate coffee","Hot lemon tea","Mint tea"]
        self.price_Tea=10
        self.price_coffee=25
        self.price_greentea=20
        self.price_hotchoc=50
        self.price_minttea=60
        self.price_leamontea=40
        
        self.Coolers=["Cold Coffee","Sprite","Seven up","Coca-cola","Apple Juice","Mango Juice","Grape Juice","Avil Milks","Mango Shakes","Saudi Shake"]
        self.price_coldcofee=100
        self.price_softdrinks=75
        self.price_avilmilk=60
        self.price_juice=80
        self.price_shake=120
        
        
        
        lbl_title=Label(self.root,text="CHECK-OUT            ",font=("times new roman",35,"bold"),bg="#0d1b28",fg="WHITE")
        lbl_title.place(x=0,y=0,width=1530,height=55)
        
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=55,width=1528,height=620)
        
        
        ###############Inputs######################
        
        
        #cust contact
        lbl_cust_contact=Label(Main_Frame,text="Contact:",font=("ariel",12,"bold"),padx=10,pady=15,bg="white")
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(Main_Frame,textvariable=self.var_contact,width=20,font=("ariel",12,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        #fetch
        btnFetch=Button(Main_Frame,text="Fetch data",command=self.Fetch_contact,font=("ariel",8,"bold"),bg="#0d1b28",fg="WHITE",width=16)
        btnFetch.place(x=280,y=14)
        
        #frame
        fetch_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg="white")
        fetch_Frame.place(x=13,y=105,width=400,height=305)
        
        lblName=Label(fetch_Frame,text="Name :",font=("ariel",10,"bold"),bg="white")
        lblName.place(x=0,y=0)
                
        lblEmail=Label(fetch_Frame,text="Email :",font=("ariel",10,"bold"),bg="white")
        lblEmail.place(x=0,y=30)
        
        lblAddress=Label(fetch_Frame,text="Check-in date :",font=("ariel",10,"bold"),bg="white")
        lblAddress.place(x=0,y=60)
        
        lblIdProof=Label(fetch_Frame,text="Check-out date :",font=("ariel",10,"bold"),bg="white")
        lblIdProof.place(x=0,y=90)
        
        lblIdNumber=Label(fetch_Frame,text="Category :",font=("ariel",10,"bold"),bg="white")
        lblIdNumber.place(x=0,y=120)
        
        lblIddays=Label(fetch_Frame,text="Days :",font=("ariel",10,"bold"),bg="white")
        lblIddays.place(x=0,y=150)
        
        lblIdRNumber=Label(fetch_Frame,text="Room Number :",font=("ariel",10,"bold"),bg="white")
        lblIdRNumber.place(x=0,y=180)
        
        lblIdprice=Label(fetch_Frame,text="Price :",font=("ariel",10,"bold"),bg="white")
        lblIdprice.place(x=0,y=210)
        
        lblIdad=Label(fetch_Frame,text="Advance paid :",font=("ariel",10,"bold"),bg="white")
        lblIdad.place(x=0,y=240)

        
        

        
        # No.of days
      #  lblNoOfDays=Label(Main_Frame,font=("arial",12,"bold"),text="No.of days:",padx=20,pady=15,bg="white")
       # lblNoOfDays.grid(row=14,column=0,sticky=W)
       # txtNoOfDays=ttk.Entry(Main_Frame,textvariable=self.var_noofdays,font=("arial",12,"bold"),width=23)
       # txtNoOfDays.grid(row=14,column=1)
        
        #
        
       # lblapproximate=Label(Main_Frame,font=("arial",12,"bold"),text="Advance:",padx=20,pady=15,bg="white")
       # lblapproximate.grid(row=16,column=0,sticky=W)
       # txtapproximate=ttk.Entry(Main_Frame,textvariable=self.var_advance,font=("arial",12,"bold"),width=23)
       # txtapproximate.grid(row=16,column=1)

        #Product Label Frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="Black")
        Product_Frame.place(x=420,y=5,width=400,height=460)
        
        self.lblCategory=Label(Product_Frame,font=("arial",12,'bold'),bg='white',text='Select Categories',bd=4)
        self.lblCategory.grid(row=1,column=0,sticky=W,padx=5,pady=10)
        
                #Cust frame
        Cust_Frame=LabelFrame(Product_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="Black")
        Cust_Frame.place(x=8,y=230,width=380,height=200)
        
        Custname=Label(Cust_Frame,text="Customer Name",font=("ariel",12,"bold"),padx=5,pady=10,bg="white")
        Custname.grid(row=1,column=0,sticky=W)

        Custname=ttk.Entry(Cust_Frame,textvariable=self.c_name,width=23,font=("ariel",12,"bold"))
        Custname.grid(row=1,column=1)

        phoneno=Label(Cust_Frame,text="Phone number",font=("ariel",12,"bold"),padx=5,pady=10,bg="white")
        phoneno.grid(row=2,column=0,sticky=W)

        phoneno=ttk.Entry(Cust_Frame,textvariable=self.var_contact,width=23,font=("ariel",12,"bold"))
        phoneno.grid(row=2,column=1)
        
        email=Label(Cust_Frame,text="Email",font=("ariel",12,"bold"),padx=5,pady=10,bg="white")
        email.grid(row=3,column=0,sticky=W)

        email=ttk.Entry(Cust_Frame,width=23,font=("ariel",12,"bold"))
        email.grid(row=3,column=1)
        
        
        #################
        
        #Categories
        self.lblCategory=Label(Product_Frame,font=("arial",12,'bold'),bg='white',text='Select Food Type',bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=10)
        
        self.Combo_Category=ttk.Combobox(Product_Frame,font=('ariel',10,'bold'),value=self.Category,width=20,state='readonly')
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=10)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

# subMeow

        self.lblSubCategory=Label(Product_Frame,font=("arial",12,'bold'),bg='white',text='Select Sub category',bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=10)    
        
        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[''],font=('ariel',10,'bold'),width=20,state='readonly')
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=10)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)
#pro

        self.lblProduct=Label(Product_Frame,font=("ariel",12,"bold"),bg="white",text="Select product")
        self.lblProduct.grid(row=2,column=0,sticky=W,padx=5,pady=10)
        self.Combo_Product=ttk.Combobox(Product_Frame,value=[''],textvariable=self.product,font=('ariel',10,'bold'),width=20,state='readonly')
        self.Combo_Product.grid(row=2,column=1,sticky=W,padx=5,pady=10)
        self.Combo_Product.bind("<<ComboboxSelected>>",self.pricee)

    #Price
        
        self.lblPrice=Label(Product_Frame,font=("arial",12,'bold'),bg='white',text='Price Of Food',bd=4)
        self.lblPrice.grid(row=5,column=0,sticky=W,padx=5,pady=10)
        
        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=('ariel',10,'bold'),width=20)
        self.ComboPrice.grid(row=5,column=1,sticky=W,padx=5,pady=10)
 

        #Quantity
        Qtyfood=Label(Product_Frame,text="Quantitiy of food",font=("ariel",12,"bold"),padx=5,pady=10,bg="white")
        Qtyfood.grid(row=6,column=0,sticky=W)

        Qtyfood=ttk.Entry(Product_Frame,textvariable=self.qty,width=18,font=("ariel",12,"bold"))
        Qtyfood.grid(row=6,column=1)
        
        

      #======#  
        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=835,y=10,width=500,height=40)
        
        self.lblBill=Label(Search_Frame,font=('ariel',12,'bold'),bg="#0d1b28",fg="WHITE",text='Bill Number',bd=4)
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1) 
        
        self.txt_Entry_Search=ttk.Entry(Search_Frame,font=('ariel',10,'bold'),textvariable=self.search_bill,width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        btnAdd=Button(Search_Frame,text="Search",command=self.find_bill,font=("ariel",10,"bold"),bg="#0d1b28",fg="WHITE",width=8)
        btnAdd.grid(row=0,column=2,padx=1)        
        #Frame bill area
        
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="Black")
        RightLabelFrame.place(x=840,y=45,width=500,height=420)
        

        
        
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
       #Kunji right frame
        Rt_Frame=LabelFrame(Main_Frame,font=("times new roman",12,"bold"),bg="white",fg="Black")
        Rt_Frame.place(x=10,y=360,width=400,height=103) 
        
        lblPrice=Label(Rt_Frame,font=("arial",12,"bold"),text="Price:",padx=2,pady=6,bg="White")
        lblPrice.grid(row=1,column=0,sticky=W)
        txtPrice=ttk.Entry(Rt_Frame,textvariable=self.var_price,font=("arial",12,"bold"),width=23)
        txtPrice.grid(row=1,column=1)
        
        lblAdvance=Label(Rt_Frame,font=("arial",12,"bold"),text="Advance:",padx=2,pady=6,bg="white")
        lblAdvance.grid(row=2,column=0,sticky=W)
        txtAdvance=ttk.Entry(Rt_Frame,textvariable=self.var_advance,font=("arial",12,"bold"),width=23)
        txtAdvance.grid(row=2,column=1)

        lblAmount_Payable=Label(Rt_Frame,font=("arial",12,"bold"),text="Amount Payable :",padx=2,pady=6,bg="white")
        lblAmount_Payable.grid(row=3,column=0,sticky=W)
        txtAmount_Payable=ttk.Entry(Rt_Frame,textvariable=self.var_payable,font=("arial",12,"bold"),width=23)
        txtAmount_Payable.grid(row=3,column=1)
             
             
        
        #Bill Counter Label Frame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="Black")
        Bottom_Frame.place(x=0,y=465,width=1340,height=140)
        
        self.lblSubTotel=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Sub-Totel",bd=4)
        self.lblSubTotel.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.EntrySubTotel=ttk.Entry(Bottom_Frame,font=('ariel',10,'bold'),textvariable=self.sub_total,width=26)
        self.EntrySubTotel.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.lblGovTax=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Gov Tax",bd=4)
        self.lblGovTax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.EntryGovTax=ttk.Entry(Bottom_Frame,font=('ariel',10,'bold'),textvariable=self.tax_input,width=26)
        self.EntryGovTax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblTotel=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Total",bd=4)
        self.lblTotel.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.EntryTotel=ttk.Entry(Bottom_Frame,font=('ariel',10,'bold'),textvariable=self.total,width=26)
        self.EntryTotel.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        
        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=300,y=30)
        
        self.BtnRooBill=Button(Btn_Frame,height=2,text="Add Room Bill",command=self.adroom,font=('arial',9,'bold'),bg="#0d1b28",fg="WHITE",width=15,padx=5,cursor="hand2")
        self.BtnRooBill.grid(row=0,column=0)
        
        self.BtnFoodBill=Button(Btn_Frame,height=2,text="Add Food Bill",command=self.AddItem,font=('arial',9,'bold'),bg="#0d1b28",fg="WHITE",width=15,padx=5,cursor="hand2")
        self.BtnFoodBill.grid(row=0,column=1)
        
        
        self.BtnGenerateBill=Button(Btn_Frame,height=2,text="Generate Bill",command=self.gen_bill,font=('arial',9,'bold'),bg="#0d1b28",fg="WHITE",width=15,cursor="hand2")
        self.BtnGenerateBill.grid(row=0,column=2)
        
        self.BtnSaveBill=Button(Btn_Frame,height=2,text="Save Bill",command=self.savebill,font=('arial',9,'bold'),bg="#0d1b28",fg="WHITE",width=15,cursor="hand2")
        self.BtnSaveBill.grid(row=0,column=3)
        
        self.BtnPrint=Button(Btn_Frame,height=2,text="Print",command=self.iprint,font=('arial',9,'bold'),bg="#0d1b28",fg="WHITE",width=15,cursor='hand2')
        self.BtnPrint.grid(row=0,column=4) 
                
                
        self.BtnExit=Button(Btn_Frame,height=2,text="Exit",command=self.exit,font=('arial',9,'bold'),bg="#0d1b28",fg="WHITE",width=15,cursor='hand2')
        self.BtnExit.grid(row=0,column=6) 

        self.BtnClear=Button(Btn_Frame,height=2,text="Clear",command=self.clear,font=('arial',9,'bold'),bg="#0d1b28",fg="WHITE",width=15,cursor='hand2')
        self.BtnClear.grid(row=0,column=7)

        self.BtnVacate=Button(Btn_Frame,height=2,text="Vacate",command=self.vacate,font=('arial',9,'bold'),bg="#0d1b28",fg="WHITE",width=15,cursor='hand2')
        self.BtnVacate.grid(row=0,column=5) 
        self.welcome()
        self.l=[]
        
        ##################################################
    
    
    ####  
    def Categories(self,event=""):
        if self.Combo_Category.get()=="Vegiterian":
            self.ComboSubCategory.config(value=self.SubCatVegiterian)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Non-Vegiterian":
            self.ComboSubCategory.config(value=self.SubCatNonvegiterian)
            self.ComboSubCategory.current(0)
            
        if self.Combo_Category.get()=="Drinks":
            self.ComboSubCategory.config(value=self.SubCatDrinks)
            self.ComboSubCategory.current(0)
    
    def Product_add(self,event=""):
        #Veg
        if self.ComboSubCategory.get()=="Salads":
            self.Combo_Product.config(value=self.Salads)
            self.Combo_Product.current(0)
     
        # non Veg
        if self.ComboSubCategory.get()=="Home Classics":
            self.Combo_Product.config(value=self.Classics) 
            self.Combo_Product.current(0)
            
        if self.ComboSubCategory.get()=="Fire Grills":
            self.Combo_Product.config(value=self.Grills) 
            self.Combo_Product.current(0)
        #Drinks
        if self.ComboSubCategory.get()=="Hot":
            self.Combo_Product.config(value=self.Hot) 
            self.Combo_Product.current(0)
            
        if self.ComboSubCategory.get()=="Coolers":
            self.Combo_Product.config(value=self.Coolers) 
            self.Combo_Product.current(0)
       

    
    def pricee(self,event=""):
        #Salads
        if self.Combo_Product.get()=="Avocado Shrimp Salad":
            self.ComboPrice.config(value=self.price_Avacado)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Honey Mint Winter Salad":
            self.ComboPrice.config(value=self.price_honey)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Carrot salad with black grape":
            self.ComboPrice.config(value=self.price_carrot)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.Combo_Product.get()=="Spicy Raw Mango Salad":
            self.ComboPrice.config(value=self.price_raw)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Green Bean Salad":
            self.ComboPrice.config(value=self.price_bean)
            self.ComboPrice.current(0)
            self.qty.set(1)
        #Home classics
        if self.Combo_Product.get()=="Biriyani":
            self.ComboPrice.config(value=self.price_biriyani)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        if self.Combo_Product.get()=="meals":
            self.ComboPrice.config(value=self.price_meals)
            self.ComboPrice.current(0)
            self.qty.set(1)
        

        if self.Combo_Product.get()=="Pulihora":
            self.ComboPrice.config(value=self.price_pulihora)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Combo_Product.get()=="Masala dosa":
            self.ComboPrice.config(value=self.price_Masaladosa)
            self.ComboPrice.current(0)
            self.qty.set(1)
        

        if self.Combo_Product.get()=="Palak paneer":
            self.ComboPrice.config(value=self.price_PalakPaneer)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Combo_Product.get()=="Hyderabadi biryani":
            self.ComboPrice.config(value=self.price_Hydrabadibiriyani)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_Product.get()=="Vada pav":
            self.ComboPrice.config(value=self.price_Vadapav)
            self.ComboPrice.current(0)
            self.qty.set(1)  
        if self.Combo_Product.get()=="Chemmeen Porichathu":
            self.ComboPrice.config(value=self.price_Chemeenporichathu)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.Combo_Product.get()=="Upma":
            self.ComboPrice.config(value=self.price_Upma)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.Combo_Product.get()=="Karimeen Pollichathu":
            self.ComboPrice.config(value=self.price_Karimeenpollichathu)
            self.ComboPrice.current(0)
            self.qty.set(1)     

        if self.Combo_Product.get()=="Alleppey Chicken Curry":
            self.ComboPrice.config(value=self.price_Alappychickencurry)
            self.ComboPrice.current(0)
            self.qty.set(1)  

        
        #Grills
        if self.Combo_Product.get()=="Shish Kebab":
            self.ComboPrice.config(value=self.price_Shish)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.Combo_Product.get()=="Kofta Kebab":
            self.ComboPrice.config(value=self.price_Shish)
            self.ComboPrice.current(0)
            self.qty.set(1)
                                        
        if self.Combo_Product.get()=="Gambari Al Nar":
            self.ComboPrice.config(value=self.price_Shish)
            self.ComboPrice.current(0)
            self.qty.set(1)      

        if self.Combo_Product.get()=="Shish Taouk":
            self.ComboPrice.config(value=self.price_Shish)
            self.ComboPrice.current(0)
            self.qty.set(1)     
            
            
        #drinks
        
        #drinks
        
        if self.Combo_Product.get()=="Tea":
            self.ComboPrice.config(value=self.price_Tea)
            self.ComboPrice.current(0)
            self.qty.set(1)  


        if self.Combo_Product.get()=="Coffee":
            self.ComboPrice.config(value=self.price_coffee)
            self.ComboPrice.current(0)
            self.qty.set(1)  
       
        if self.Combo_Product.get()=="Green Tea":
            self.ComboPrice.config(value=self.price_greentea)
            self.ComboPrice.current(0)
            self.qty.set(1)  

    
        if self.Combo_Product.get()=="Hot Chocolate coffee":
            self.ComboPrice.config(value=self.price_hotchoc)
            self.ComboPrice.current(0)
            self.qty.set(1) 

    
        if self.Combo_Product.get()=="Mint tea":
            self.ComboPrice.config(value=self.price_minttea)
            self.ComboPrice.current(0)
            self.qty.set(1) 

    
        if self.Combo_Product.get()=="Hot lemon tea":
            self.ComboPrice.config(value=self.price_leamontea)
            self.ComboPrice.current(0)
            self.qty.set(1) 

    
        if self.Combo_Product.get()=="Cold Coffee":
            self.ComboPrice.config(value=self.price_coldcofee)
            self.ComboPrice.current(0)
            self.qty.set(1) 

    
        if self.Combo_Product.get()=="Sprite":
            self.ComboPrice.config(value=self.price_softdrinks)
            self.ComboPrice.current(0)
            self.qty.set(1) 
    
        if self.Combo_Product.get()=="Seven up":
            self.ComboPrice.config(value=self.price_softdrinks)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.Combo_Product.get()=="Coca-cola":
            self.ComboPrice.config(value=self.price_softdrinks)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.Combo_Product.get()=="Avil Milk":
            self.ComboPrice.config(value=self.price_avilmilk)
            self.ComboPrice.current(0)
            self.qty.set(1) 
    
        if self.Combo_Product.get()=="Apple Juice":
            self.ComboPrice.config(value=self.price_juice)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.Combo_Product.get()=="Mango Juice":
            self.ComboPrice.config(value=self.price_juice)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.Combo_Product.get()=="Grape Juice":
            self.ComboPrice.config(value=self.price_juice)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.Combo_Product.get()=="Mango Shakes":
            self.ComboPrice.config(value=self.price_shake)
            self.ComboPrice.current(0)
            self.qty.set(1)  
        if self.Combo_Product.get()=="Saudi Shake":
            self.ComboPrice.config(value=self.price_shake)
            self.ComboPrice.current(0)
            self.qty.set(1)  
        

    #Function declaration
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t\tHotel Pro")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.var_contact.get()}")
        self.textarea.insert(END,"\n\------------------------------------------------------------------------------------")
        self.textarea.insert(END,f"\n Dishes\t\tQuantity\t\tPrice")
        self.textarea.insert(END,"\n\------------------------------------------------------------------------------------")
          
    

    
      
        
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()

        self.s=self.var_payable.get()
        self.m=self.qty.get()*self.n
        self.nt=self.var_payable.get()+(self.prices.get()*self.qty.get())
        self.l.append(self.nt)
        

        self.textarea.insert(END,f"\n {self.product.get()}\t\t\t {self.qty.get()}\t\t\t {self.m}")
        self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
        self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
        self.total.set(str('Rs.%2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))
                
    def adroom(self):
        
        q1=float(self.var_price.get())
        q2=float(self.var_advance.get())
        q3=float(q1-q2)
        AP=str("%.2f"%(q3))
        self.var_payable.set(AP)
        self.textarea.insert(END,"\n------------------------------------------------------------------------------------")
        self.textarea.insert(END,f"\nPrice of Room : {self.var_payable.get()}")
        self.textarea.insert(END,"\n------------------------------------------------------------------------------------")

    
    def gen_bill(self):

            textt=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,textt)
            self.textarea.insert(END,"\n------------------------------------------------------------------------------------")
            self.textarea.insert(END,f"\nSub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\nTax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\nTotal Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n------------------------------------------------------------------------------------")
            
    
    def savebill(self):
        op=messagebox.askyesno("Save bill","Do you want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('savebills/'+str(self.bill_no.get())+'.txt','w')
            
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully ",)
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
    

    def find_bill(self):
        found="yes"
        for i in os.listdir('savebills/'):
            if i.split('.')[0]==self.search_bill.get():
                     f1=open(f'savebills/{i}','r')
                     self.textarea.delete(1.0,END)
                     for d in f1:
                        self.textarea.insert(END,d)
                     f1.close()
                     found="yes"
            if found=='no':
                messagebox.showerror('Error',"Invalid bill number")
                
    
    def clear(self):
        self.textarea.delete(1.0,END) 
        self.c_name.set("")
        self.c_email.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.search_bill.set('')
        self.product.set('')
        self.prices.set('')
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set('')
        self.tax_input.set('')
        self.total.set('')
        self.var_price.set('')
        self.var_advance.set('')
        self.var_payable.set('')
        self.welcome()
    
    def vacate(self):
        vactate=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if vactate>0:
             conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
             my_cursor=conn.cursor()
             query=("delete from checkin where Contact=%s")
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
             
        else:
             if not vactate:
                return
        conn.commit()
        conn.close()
        
    def exit(self):
        self.root.destroy()
        os.system("main.py")
    
    

    
###########################################################################################################################################        

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
                        
                showDataframe=Frame(self.root,bd=2,relief=RIDGE,padx=2,bg="white")
                showDataframe.place(x=15,y=105,width=400,height=305)
                
                lblName=Label(showDataframe,text="Name :",font=("ariel",10,"bold"),bg="white")
                lblName.place(x=0,y=0)
                
                lbl=Label(showDataframe,text=row,font=("ariel",10,"bold"),bg="white")
                lbl.place(x=60,y=0)
                
                #email
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select email from customer where mobile=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
           


                
                lblGender=Label(showDataframe,text="Email :",font=("ariel",10,"bold"),bg="white")
                lblGender.place(x=0,y=30)
                
                lbl2=Label(showDataframe,text=row,font=("ariel",10,"bold"),bg="white")
                lbl2.place(x=60,y=30)
                
                #checkin
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select check_in from checkin where contact=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lbladdress=Label(showDataframe,text="Check in date :",font=("ariel",10,"bold"),bg="white")
                lbladdress.place(x=0,y=60)
                
                lbl3=Label(showDataframe,text=row,font=("ariel",10,"bold"),bg="white")
                lbl3.place(x=110,y=60)
                # cout
                
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select check_out from checkin where Contact=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
           

                
                lblIdproof=Label(showDataframe,text="Check out date :",font=("ariel",10,"bold"),bg="White")
                lblIdproof.place(x=0,y=90)
                
                lbl4=Label(showDataframe,text=row,font=("ariel",10,"bold"),bg="white")
                lbl4.place(x=110,y=90)
                
                #category
                
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select category from checkin where contact=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                
                lblcat=Label(showDataframe,text="Category :",font=("ariel",10,"bold"),bg="white")
                lblcat.place(x=0,y=120)
                
                lbl5=Label(showDataframe,text=row,font=("ariel",10,"bold"),bg="White")
                lbl5.place(x=80,y=120)
                
                #Days
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select noofdays from checkin where contact=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
   

                
                lbldays=Label(showDataframe,text="Days :",font=("ariel",10,"bold"),bg="white")
                lbldays.place(x=0,y=150)
                
                lbl6=Label(showDataframe,text=row,font=("ariel",10,"bold"),bg="White")
                lbl6.place(x=80,y=150)
                
                #rno
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select roomavailable from checkin where contact=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                
                lblrno=Label(showDataframe,text="Room Number :",font=("ariel",10,"bold"),bg="white")
                lblrno.place(x=0,y=180)
                
                lbl7=Label(showDataframe,text=row,font=("ariel",10,"bold"),bg="White")
                lbl7.place(x=115,y=180)
                
                #pr
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select price from checkin where contact=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                
                lblprice=Label(showDataframe,text="Price :",font=("ariel",10,"bold"),bg="white")
                lblprice.place(x=0,y=210)
                
                lbl8=Label(showDataframe,text=row,font=("ariel",10,"bold"),bg="White")
                lbl8.place(x=50,y=210)
                
                
                #ad
                
                conn=mysql.connector.connect(host="localhost",username="root",password="nithin1234#",database="project")
                my_cursor=conn.cursor()
                query=('select advance  from checkin where contact=%s')
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                
                lblad=Label(showDataframe,text="Advance paid :",font=("ariel",10,"bold"),bg="white")
                lblad.place(x=0,y=240)
                
                lbl9=Label(showDataframe,text=row,font=("ariel",10,"bold"),bg="White")
                lbl9.place(x=100,y=240)
                
                conn.commit()
                conn.close()
                
        
                

                

    
if __name__ =='__main__':
    root=Tk()
    obj=Check_Out(root)
    root.mainloop()