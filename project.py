from tkinter import*
from tkinter import ttk




class Employee:
     def __init__(self,root):
         self.root=root
         self.root.geometry("1530x780+0+0")
         self.root.title('Staff Management system')

         title=Label(self.root,text='STAFF MANAGEMENT SYSTEM',bd=5,relief=GROOVE,font=('times new romam',40,'bold'),fg='darkblue',bg='white')
         title.place(x=0,y=0,width=1530,height=50)


     
         #======Manage Frame=======================
         Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="daRK blue")
         Manage_Frame.place(x=20,y=100,width=450,height=580)

         m_title=Label(Manage_Frame,text="Staff information",bg="dark blue",fg="white",font=('times new romam',20,'bold'))
         m_title.grid(row=0,column=0,pady=20)

         lbl_dep=Label(Manage_Frame,text='Department',bg="dark blue",fg="white",font=('times new romam',15,'bold'))
         lbl_dep.grid(row=1,column=0,pady=10,padx=20,sticky="W")

         txt_dep=Entry(Manage_Frame,font=('times new romam',10,'bold'),bd=1,relief=GROOVE) 
         txt_dep.grid(row=1,column=1,pady=10,padx=20,sticky="W")

         lbl_name=Label(Manage_Frame,text='Name',bg="dark blue",fg="white",font=('times new romam',15,'bold'))
         lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="W")

         txt_name=Entry(Manage_Frame,font=('times new romam',10,'bold'),bd=1,relief=GROOVE) 
         txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="W")

         lbl_Designation=Label(Manage_Frame,text='Designation',bg="dark blue",fg="white",font=('times new romam',15,'bold'))
         lbl_Designation.grid(row=3,column=0,pady=10,padx=20,sticky="W")

         txt_Designation=Entry(Manage_Frame,font=('times new romam',10,'bold'),bd=1,relief=GROOVE) 
         txt_Designation.grid(row=3,column=1,pady=10,padx=20,sticky="W")

         lbl_Email=Label(Manage_Frame,text='Email',bg="dark blue",fg="white",font=('times new romam',15,'bold'))
         lbl_Email.grid(row=4,column=0,pady=10,padx=20,sticky="W")

         txt_Email=Entry(Manage_Frame,font=('times new romam',10,'bold'),bd=1,relief=GROOVE) 
         txt_Email.grid(row=4,column=1,pady=10,padx=20,sticky="W")


         lbl_DOJ=Label(Manage_Frame,text='DOJ',bg="dark blue",fg="white",font=('times new romam',15,'bold'))
         lbl_DOJ.grid(row=5,column=0,pady=10,padx=20,sticky="W")

         txt_DOJ=Entry(Manage_Frame,font=('times new romam',10,'bold'),bd=1,relief=GROOVE) 
         txt_DOJ.grid(row=5,column=1,pady=10,padx=20,sticky="W")

         lbl_Gender=Label(Manage_Frame,text='Gender',bg="dark blue",fg="white",font=('times new romam',15,'bold'))
         lbl_Gender.grid(row=6,column=0,pady=10,padx=20,sticky="W")

         combo_gender=ttk.Combobox(Manage_Frame,font=('times new romam',8,'bold'),state="readonly")
         combo_gender["values"]=("Male","Female","Others")
         combo_gender.grid(row=6,column=1,pady=10,padx=20,sticky="W")

         lbl_contact=Label(Manage_Frame,text='contact',bg="dark blue",fg="white",font=('times new romam',15,'bold'))
         lbl_contact.grid(row=7,column=0,pady=10,padx=20,sticky="W")

         txt_contact=Entry(Manage_Frame,font=('times new romam',10,'bold'),bd=1,relief=GROOVE) 
         txt_contact.grid(row=7,column=1,pady=10,padx=20,sticky="W")


         lbl_Address=Label(Manage_Frame,text='Address',bg="dark blue",fg="white",font=('times new romam',15,'bold'))
         lbl_Address.grid(row=8,column=0,pady=10,padx=20,sticky="W")

         txt_Address=Entry(Manage_Frame,font=('times new romam',10,'bold'),bd=1,relief=GROOVE) 
         txt_Address.grid(row=8,column=1,pady=10,padx=20,sticky="W")

         #======Button Frame=
         btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="daRK blue")
         btn_Frame.place(x=10,y=500,width=430)

         Addbtn=Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
         Updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
         Deletebtn=Button(btn_Frame,text="Delate",width=10).grid(row=0,column=2,padx=10,pady=10)
         Clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)


         #======Detail Frame=======================
         Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="daRK blue")
         Detail_Frame.place(x=500,y=100,width=900,height=580)

         lbl_search=Label(Detail_Frame,text='Search By',bg="dark blue",fg="white",font=('times new romam',15,'bold'))
         lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="W")

         combo_search=ttk.Combobox(Detail_Frame,font=('times new romam',8,'bold'),state="readonly")
         combo_search["values"]=("Department","Name","Designation")
         combo_search.grid(row=0,column=1,pady=10,padx=10)

         txt_search=Entry(Detail_Frame,width=15,font=('times new romam',10,'bold'),bd=1,relief=GROOVE) 
         txt_search.grid(row=0,column=1,pady=10,padx=20,sticky="W")

         searchbtn=Button(Detail_Frame,text="Search",width=10).grid(row=0,column=3,padx=10,pady=10)
         showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

         #========Table Frame==================
         Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="daRK blue")
         Table_Frame.place(x=10,y=70,width=800,height=500)


         Scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
         Scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
         Staff_table=ttk.Treeview(Table_Frame,columns=("department","Name","Designation","Email","DOJ","Contact","Address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
         Scroll_x.pack(side=BOTTOM,fill=X)
         Scroll_y.pack(side=BOTTOM,fill=Y)
         Scroll_x.config(command=Staff_table.xview)
         Scroll_y.config(command=Staff_table.yview)
         Staff_table.heading("Name",text="Name")
         Staff_table.heading("Designation",text="Designation")
         Staff_table.heading("Email",text="Email")
         Staff_table.heading("DOJ",text="DOJ")
         Staff_table.heading("Contact",text="Contact")
         Staff_table.heading("Address",text="Address")
         Staff_table["show"]="headings"
         Staff_table.column("Name",width=100)
         Staff_table.column("Designation",width=100)
         Staff_table.column("Email",width=100)
         Staff_table.column("DOJ",width=100)
         Staff_table.column("Contact",width=100)
         Staff_table.column("Address",width=150)
         Staff_table.pack(fill=BOTH,expand=1)
         Staff_table.pack()



root=Tk() 
obj=Employee(root)
root.mainloop()