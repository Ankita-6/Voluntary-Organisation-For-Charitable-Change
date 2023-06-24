from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector



class Ngo:
    def __init__(self,root):
        self.root=root
        self.root.title("NGO activity integration") 
        self.root.geometry("1540x800+0+0")

        self.CategoryofNeedy=StringVar()
        self.IdNo=StringVar()
        self.Age=StringVar()
        self.RoomNo=StringVar()
        self.AadharNo=StringVar()
        self.EnrollmentDate=StringVar()
        self.ExitDate=StringVar()
        self.FloorNo=StringVar()
        self.Nationality=StringVar()
        self.FurtherInfo=StringVar()
        self.NoofRelatives=StringVar()
        self.IsChild=StringVar()
        self.Issue=StringVar()
        self.RefNo=StringVar()
        self.PhoneNo=StringVar()
        self.Name=StringVar()
        self.Dob=StringVar()
        self.Address=StringVar()

        

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="NGO ACTIVITY INTEGRATION",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #=================================Data frame===============================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="People Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Details")
        DataframeRight.place(x=0,y=5,width=980,height=350)
        DataframeRight.place(x=990,y=5,width=460,height=350)


    
        #=========================buttons frame==========================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        #=========================Details frame==========================

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #==========================DataframeLeft===========================

        lblCategory=Label(DataframeLeft,text="Category of needy",font=("arial",12,"bold"),padx=2,pady=6)
        lblCategory.grid(row=0,column=0,sticky=W)

        comCategory=ttk.Combobox(DataframeLeft,textvariable=self.CategoryofNeedy,state="readonly",font=("arial",12,"bold"),width=33)

        comCategory["value"]=("Orphan","Homeless","Poor","Handicap","Oldage")
        comCategory.current(0)
        comCategory.grid(row=0,column=1)


        lblid=Label(DataframeLeft,font=("arial",12,"bold"),text="Id No:",padx=2)
        lblid.grid(row=1,column=0,sticky=W)
        txtid=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.IdNo,width=35)
        txtid.grid(row=1,column=1)

        lblage=Label(DataframeLeft,font=("arial",12,"bold"),text="Age:",padx=2,pady=4)
        lblage.grid(row=2,column=0,sticky=W)
        txtage=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Age,width=35)
        txtage.grid(row=2,column=1)

        lblroom=Label(DataframeLeft,font=("arial",12,"bold"),text="Room No:",padx=2,pady=4)
        lblroom.grid(row=3,column=0,sticky=W)
        txtroom=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.RoomNo,width=35)
        txtroom.grid(row=3,column=1)

        lblaadhar=Label(DataframeLeft,font=("arial",12,"bold"),text="Aadhar No:",padx=2,pady=6)
        lblaadhar.grid(row=4,column=0,sticky=W)
        txtaadhar=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.AadharNo,width=35)
        txtaadhar.grid(row=4,column=1)

        lbledate=Label(DataframeLeft,font=("arial",12,"bold"),text="Enrollment date:",padx=2,pady=6)
        lbledate.grid(row=5,column=0,sticky=W)
        txtedate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.EnrollmentDate,width=35)
        txtedate.grid(row=5,column=1)

        lblexdate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exit date:",padx=2,pady=6)
        lblexdate.grid(row=6,column=0,sticky=W)
        txtexdate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ExitDate,width=35)
        txtexdate.grid(row=6,column=1)

        lblfloor=Label(DataframeLeft,font=("arial",12,"bold"),text="Floor No:",padx=2,pady=4)
        lblfloor.grid(row=7,column=0,sticky=W)
        txtfloor=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.FloorNo,width=35)
        txtfloor.grid(row=7,column=1)

        lblnation=Label(DataframeLeft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=4)
        lblnation.grid(row=8,column=0,sticky=W)
        txtnation=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Nationality,width=35)
        txtnation.grid(row=8,column=1)

        lblfinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further information",padx=2)
        lblfinfo.grid(row=0,column=2,sticky=W)
        txtfinfo=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.FurtherInfo,width=35)
        txtfinfo.grid(row=0,column=3)

        lblrelative=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Relatives:",padx=2,pady=6)
        lblrelative.grid(row=1,column=2,sticky=W)
        txtrelative=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.NoofRelatives,width=35)
        txtrelative.grid(row=1,column=3)

        lblchild=Label(DataframeLeft,font=("arial",12,"bold"),text="Child?",padx=2,pady=6)
        lblchild.grid(row=2,column=2,sticky=W)
        txtchild=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.IsChild,width=35)
        txtchild.grid(row=2,column=3)

        lblissue=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue",padx=2,pady=6)
        lblissue.grid(row=3,column=2,sticky=W)
        txtissue=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Issue,width=35)
        txtissue.grid(row=3,column=3,sticky=W)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Ref No:",padx=2,pady=6)
        lblref.grid(row=4,column=2,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.RefNo,width=35)
        txtref.grid(row=4,column=3)

        lblphno=Label(DataframeLeft,font=("arial",12,"bold"),text="Phone No(if any):",padx=2,pady=6)
        lblphno.grid(row=5,column=2,sticky=W)
        txtphno=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PhoneNo,width=35)
        txtphno.grid(row=5,column=3)

        lblname=Label(DataframeLeft,font=("arial",12,"bold"),text="Name:",padx=2,pady=6)
        lblname.grid(row=6,column=2,sticky=W)
        txtname=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Name,width=35)
        txtname.grid(row=6,column=3)

        lbldob=Label(DataframeLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lbldob.grid(row=7,column=2,sticky=W)
        txtdob=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Dob,width=35)
        txtdob.grid(row=7,column=3)

        lbladdress=Label(DataframeLeft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lbladdress.grid(row=8,column=2,sticky=W)
        txtaddress=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Address,width=35)
        txtaddress.grid(row=8,column=3)


        #=====================DataFrameRight================================
        self.txtDetail=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtDetail.grid(row=0,column=0)


        #=======================Buttons======================================
        #btnDetails=Button(Buttonframe,text="Print",bg="white",fg="black",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        #btnDetails.grid(row=0,column=0)

        #btnDetail=Button(Buttonframe,command=self.iDetail,text="Details",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        #btnDetail.grid(row=0,column=0)

        btnDetail=Button(Buttonframe,text=("PRINT DETAILS"),font=("arial,10,bold"),padx=2,pady=6,bg='blue',fg='white',width=22,command=self.iDetail)
        btnDetail.grid(row=0,column=0)

        btnDetaildata=Button(Buttonframe,text=("INSERT"),font=("arial,10,bold"),padx=2,pady=6,bg='green',fg='white',width=22,command=self.iShowData)
        btnDetaildata.grid(row=0,column=1)
        
        btnUpdate=Button(Buttonframe,text=("UPDATE"),font=("arial,10,bold"),padx=2,pady=6,bg='magenta',fg='white',width=22,command=self.update_data)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text=("DELETE"),font=("arial,10,bold"),padx=2,pady=6,bg='red',fg='white',width=22,command=self.idelete)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text=("CLEAR"),font=("arial,10,bold"),padx=2,pady=6,bg='purple',fg='white',width=22,command=self.clear)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text=("EXIT"),font=("arial,10,bold"),padx=2,pady=6,bg='gray',fg='white',width=20,command=self.iExit)
        btnExit.grid(row=0,column=5)


        #btnDetaildata=Button(Buttonframe,command=self.iShowData,text="Show data",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        #btnDetaildata.grid(row=0,column=1)

        #btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        #btnUpdate.grid(row=0,column=2)

        #btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        #btnDelete.grid(row=0,column=3)

        #btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        #btnClear.grid(row=0,column=4)

        #btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        #btnExit.grid(row=0,column=5)


        #==========================================Table========================================
        #=============================Scroll Bar==========================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.ngo_table=ttk.Treeview(Detailsframe,column=("category","id","age","room","aadhar","enrollmentdate","floor","nationality",
                                "child?","phno","name","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.ngo_table.xview)
        scroll_y=ttk.Scrollbar(command=self.ngo_table.yview)

        self.ngo_table.heading("category",text="Category of needy")
        self.ngo_table.heading("id",text="ID No")
        self.ngo_table.heading("age",text="Age")
        self.ngo_table.heading("room",text="Room No")
        self.ngo_table.heading("aadhar",text="Aadhar No")
        self.ngo_table.heading("enrollmentdate",text="Enrollment Date")
        #self.ngo_table.heading("Exit date",text="Exit Date")
        self.ngo_table.heading("floor",text="Floor No")
        self.ngo_table.heading("nationality",text="Nationality")
        #self.ngo_table.heading("Further info",text="Further Info")
        #self.ngo_table.heading("No of relatives",text="No of Relatives")
        self.ngo_table.heading("child?",text="Child??")
        #self.ngo_table.heading("Issue",text="Issue")
        #self.ngo_table.heading("Ref No",text="Reference No")
        self.ngo_table.heading("phno",text="Ph No")
        self.ngo_table.heading("name",text="Name")
        self.ngo_table.heading("dob",text="Dob")
        self.ngo_table.heading("address",text="Address")
        
        self.ngo_table["show"]="headings"

        
        self.ngo_table.column("category",width=100)
        self.ngo_table.column("id",width=100)
        self.ngo_table.column("age",width=100)
        self.ngo_table.column("room",width=100)
        self.ngo_table.column("aadhar",width=100)
        self.ngo_table.column("enrollmentdate",width=100)
        self.ngo_table.column("floor",width=100)
        self.ngo_table.column("nationality",width=100)
        self.ngo_table.column("child?",width=100)
        self.ngo_table.column("phno",width=100)
        self.ngo_table.column("name",width=100)
        self.ngo_table.column("dob",width=100)
        self.ngo_table.column("address",width=100)

        self.ngo_table.pack(fill=BOTH,expand=1)
        self.ngo_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #==============================Functionality Declaration===========================
    def iShowData(self):
        if self.CategoryofNeedy.get()=="" or self.IdNo.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="ankita",password="ankita123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into ngo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                self.CategoryofNeedy.get(),
                                                                                                self.IdNo.get(),
                                                                                                self.Age.get(),
                                                                                                self.RoomNo.get(),
                                                                                                self.AadharNo.get(),
                                                                                                self.EnrollmentDate.get(),
                                                                                                self.FloorNo.get(),
                                                                                                self.Nationality.get(),
                                                                                                self.IsChild.get(),
                                                                                                self.PhoneNo.get(),
                                                                                                self.Name.get(),
                                                                                                self.Dob.get(),
                                                                                                self.Address.get()

                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="ankita",password="ankita123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update ngo set CategoryofNeedy=%s,age=%s,roomno=%s,aadharno=%s,enrollmentdate=%s,floor=%s,nationality=%s,ischild=%s,phno=%s,name=%s,dob=%s,address=%s where Id=%s",(

                                                                                                self.CategoryofNeedy.get(),
                                                                                                self.Age.get(),
                                                                                                self.RoomNo.get(),
                                                                                                self.AadharNo.get(),
                                                                                                self.EnrollmentDate.get(),
                                                                                                self.FloorNo.get(),
                                                                                                self.Nationality.get(),
                                                                                                self.IsChild.get(),
                                                                                                self.PhoneNo.get(),
                                                                                                self.Name.get(),
                                                                                                self.Dob.get(),
                                                                                                self.Address.get(),
                                                                                                self.IdNo.get(),
                                                                                                
                                                                                                ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Update","Record has been updated Successfully",parent=self.root)



    
            
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="ankita",password="ankita123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from ngo")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.ngo_table.delete(*self.ngo_table.get_children())
            for i in rows:
                self.ngo_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.ngo_table.focus()
        content=self.ngo_table.item(cursor_row)
        row=content["values"]
        self.CategoryofNeedy.set(row[0])
        self.IdNo.set(row[1])
        self.Age.set(row[2])
        self.RoomNo.set(row[3])
        self.AadharNo.set(row[4])
        self.EnrollmentDate.set(row[5])
        self.FloorNo.set(row[6])
        self.Nationality.set(row[7])
        self.IsChild.set(row[8])
        self.PhoneNo.set(row[9])
        self.Name.set(row[10])
        self.Dob.set(row[11])
        self.Address.set(row[12])

    def iDetail(self):
        self.txtDetail.insert(END,"Category of needy:\t\t\t" + self.CategoryofNeedy.get() + "\n")
        self.txtDetail.insert(END,"Id No:\t\t\t"+self.IdNo.get()+"\n")        
        self.txtDetail.insert(END,"Age:\t\t\t"+self.Age.get()+"\n")
        self.txtDetail.insert(END,"Room No:\t\t\t"+self.RoomNo.get()+"\n")
        self.txtDetail.insert(END,"Aadhar No:\t\t\t"+self.AadharNo.get()+"\n")
        self.txtDetail.insert(END,"Enrollment Date:\t\t\t"+self.EnrollmentDate.get()+"\n")
        self.txtDetail.insert(END,"Exit Date:\t\t\t"+self.ExitDate.get()+"\n")
        self.txtDetail.insert(END,"Floor No:\t\t\t"+self.FloorNo.get()+"\n")
        self.txtDetail.insert(END,"Nationality:\t\t\t"+self.Nationality.get()+"\n")
        self.txtDetail.insert(END,"Further Info:\t\t\t"+self.FurtherInfo.get()+"\n")
        self.txtDetail.insert(END,"No of Relatives:\t\t\t"+self.NoofRelatives.get()+"\n")
        self.txtDetail.insert(END,"Child?:\t\t\t"+self.IsChild.get()+"\n")
        self.txtDetail.insert(END,"Issue:\t\t\t"+self.Issue.get()+"\n")
        self.txtDetail.insert(END,"Ref No:\t\t\t"+self.RefNo.get()+"\n")
        self.txtDetail.insert(END,"Phone No:\t\t\t"+self.PhoneNo.get()+"\n")
        self.txtDetail.insert(END,"Name:\t\t\t"+self.Name.get()+"\n")
        self.txtDetail.insert(END,"Date of Birth:\t\t\t"+self.Dob.get()+"\n")
        self.txtDetail.insert(END,"Address:\t\t\t"+self.Address.get()+"\n")

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="ankita",password="ankita123",database="mydata")
        my_cursor=conn.cursor()
        query="delete from ngo where Id=%s"
        value=(self.IdNo.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Person has been deleted successfully",parent=self.root)

    def clear(self):
        self.CategoryofNeedy.set("")
        self.IdNo.set("")
        self.Age.set("")
        self.RoomNo.set("")
        self.AadharNo.set("")
        self.EnrollmentDate.set("")
        self.ExitDate.set("")
        self.FloorNo.set("")
        self.Nationality.set("")
        self.FurtherInfo.set("")
        self.NoofRelatives.set("")
        self.IsChild.set("")
        self.Issue.set("")
        self.RefNo.set("")
        self.PhoneNo.set("")
        self.Name.set("")
        self.Dob.set("")
        self.Address.set("")
        self.txtDetail.delete("1.0",END)


    def iExit(self):
        iExit=messagebox.askyesno("NGO data maintenance-Admin","Confirm you want to exit?")
        if iExit>0:
            root.destroy()
            return
        
        




      
root=Tk()
ob=Ngo(root)
root.mainloop()
