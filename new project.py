from msilib.schema import ComboBox
from telnetlib import COM_PORT_OPTION
from tkinter import*
from  tkinter import ttk
from tkinter.tix import COLUMN
from PIL import Image,ImageTk




class Employee:
               def __init__(self,root):
                              self.root=root
                              self.root.geometry("1530x780+0+0")
                              self.root.title('Staff Management system')



                              lbl_title=Label(self.root,text='STAFF MANAGEMENT SYSTEM',font=('times new romam',37,'bold'),fg='darkblue',bg='white')
                              lbl_title.place(x=0,y=0,width=1530,height=50)


                              # image Frame
                              img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='dark blue')
                              img_frame.place(x=0,y=50,width=1530,height=160)


                              # Main Frame
                              Maim_frame=Frame(self.root,bd=2,relief=RIDGE,bg='dark blue')
                              Maim_frame.place(x=10,y=220,width=1500,height=560)


                              # Upper Frame
                              Upper_frame=LabelFrame(Maim_frame,bd=2,relief=RIDGE,bg='dark blue',text='Staff Information',font=('times new romam',11,'bold'),fg='Green')
                              Upper_frame.place(x=10,y=10,width=1480,height=270)

                              # Labels and Entry fields
                              lbl_dep=Label(Upper_frame,text='Department',font=('arial',11,'bold'),bg='dark blue')
                              lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

                              combo_dep=ttk.Combobox(Upper_frame,font=('arial',11,'bold'),width=17,state='readonly')
                              combo_dep['value']=('Select Department','HR','Software Engineer','Project Manager','Reporting Manager','Technical Team')
                              combo_dep.current(0)
                              combo_dep.grid(row=0,column=1,padx=10,sticky=W)

                              lbl_name=Label(Upper_frame,font=("arial",11,"bold"),text="Name:",bg="dark blue")
                              lbl_name.grid(row=1,column=0,pady=2,padx=2,sticky="W")

                              txt_name=Entry(Upper_frame,width=22,font=("arial",11,"bold")) 
                              txt_name.grid(row=1,column=1,padx=2,sticky="W")

                              lbl_Designation=Label(Upper_frame,font=("arial",11,"bold"),text="Designation",bg="dark blue")
                              lbl_Designation.grid(row=2,column=0,pady=2,padx=2,sticky="W")

                              txt_Designation=Entry(Upper_frame,width=22,font=("arial",11,"bold")) 
                              txt_Designation.grid(row=2,column=1,padx=2,sticky="W")

                              lbl_Email=Label(Upper_frame,font=("arial",11,"bold"),text="Email",bg="dark blue")
                              lbl_Email.grid(row=3,column=0,pady=2,padx=2,sticky="W")

                              txt_Email=Entry(Upper_frame,width=22,font=("arial",11,"bold")) 
                              txt_Email.grid(row=3,column=1,padx=2,sticky="W")

                              lbl_Address=Label(Upper_frame,font=("arial",11,"bold"),text="Address",bg="dark blue")
                              lbl_Address.grid(row=4,column=0,pady=2,padx=2,sticky="W")

                              txt_Address=Entry(Upper_frame,width=22,font=("arial",11,"bold")) 
                              txt_Address.grid(row=4,column=1,padx=2,sticky="W")

                              lbl_DOB=Label(Upper_frame,font=("arial",11,"bold"),text="DOB",bg="dark blue")
                              lbl_DOB.grid(row=5,column=0,pady=2,padx=2,sticky="W")

                              txt_DOB=Entry(Upper_frame,width=22,font=("arial",11,"bold")) 
                              txt_DOB.grid(row=5,column=1,padx=2,sticky="W")

                              lbl_DOJ=Label(Upper_frame,font=("arial",11,"bold"),text="DOJ",bg="dark blue")
                              lbl_DOJ.grid(row=1,column=3,pady=2,padx=2,sticky="W")

                              txt_DOJ=Entry(Upper_frame,width=22,font=("arial",11,"bold")) 
                              txt_DOJ.grid(row=1,column=4,padx=2,sticky="W")

                              lbl_Gender=Label(Upper_frame,font=("arial",12,"bold"),text="Gender",bg="dark blue")
                              lbl_Gender.grid(row=2,column=3,pady=2,padx=2,sticky="W")

                              combo_gender=ttk.Combobox(Upper_frame,state="readonly",font=("arial",12,"bold"),width=18)
                              combo_gender["values"]=("Male","Female","Others")
                              combo_gender.grid(row=2,column=4,padx=2,sticky="W")

                              lbl_Mobile=Label(Upper_frame,font=("arial",11,"bold"),text="Mobile",bg="dark blue")
                              lbl_Mobile.grid(row=3,column=3,pady=2,padx=2,sticky="W")

                              txt_Mobile=Entry(Upper_frame,width=22,font=("arial",11,"bold")) 
                              txt_Mobile.grid(row=3,column=4,padx=2,sticky="W")

                              lbl_proof=Label(Upper_frame,font=("arial",12,"bold"),text="ID Proof",bg="dark blue")
                              lbl_proof.grid(row=4,column=3,pady=2,padx=2,sticky="W")

                              combo_proof=ttk.Combobox(Upper_frame,state="readonly",font=("arial",12,"bold"),width=18)
                              combo_proof["values"]=("select ID proof","PAN CARD", "AADHAR CARD","DRIVING LICENCE","PASSPORT","VOTER ID")
                              combo_proof.grid(row=4,column=4,padx=2,sticky="W")

                              
                              lbl_country=Label(Upper_frame,font=("arial",11,"bold"),text="Country",bg="dark blue")
                              lbl_country.grid(row=5,column=3,pady=2,padx=2,sticky="W")

                              txt_country=Entry(Upper_frame,width=22,font=("arial",11,"bold")) 
                              txt_country.grid(row=5,column=4,padx=2,sticky="W")

                              
                              lbl_CTC=Label(Upper_frame,font=("arial",11,"bold"),text="Salary_CTC",bg="dark blue")
                              lbl_CTC.grid(row=1,column=5,pady=2,padx=2,sticky="W")

                              txt_CTC=Entry(Upper_frame,width=22,font=("arial",11,"bold")) 
                              txt_CTC.grid(row=1,column=6,padx=2,sticky="W")

                              lbl_Married_Status=Label(Upper_frame,font=("arial",12,"bold"),text="Married_Status",bg="dark blue")
                              lbl_Married_Status.grid(row=2,column=5,pady=2,padx=2,sticky="W")

                              combo_Married_status=ttk.Combobox(Upper_frame,state="readonly",font=("arial",12,"bold"),width=18)
                              combo_Married_status["values"]=("Married","Unmarried")
                              combo_Married_status.grid(row=2,column=6,padx=2,sticky="W")

                              # Button Frame
                              button_frame=Frame(Upper_frame,bd=2,relief=RIDGE,bg='dark blue')
                              button_frame.place(x=1290,y=10,width=170,height=210)
               

                              btn_add=Button(button_frame,text="save",font=("arial",15,"bold"),width=13,bg="white",fg="red")
                              btn_add.grid(row=0,column=0,padx=1,pady=5)

                              btn_Update=Button(button_frame,text="Update",font=("arial",15,"bold"),width=13,bg="white",fg="red")
                              btn_Update.grid(row=1,column=0,padx=1,pady=5)

                              btn_Delete=Button(button_frame,text="Delete",font=("arial",15,"bold"),width=13,bg="white",fg="red")
                              btn_Delete.grid(row=2,column=0,padx=1,pady=5)

                              btn_Clear=Button(button_frame,text="Clear",font=("arial",15,"bold"),width=13,bg="white",fg="red")
                              btn_Clear.grid(row=3,column=0,padx=1,pady=5)




                              # Down Frame
                              Down_frame=LabelFrame(Maim_frame,bd=2,relief=RIDGE,bg='white',text='Staff Information',font=('times new romam',11,'bold'),fg='dark blue')
                              Down_frame.place(x=10,y=280,width=11480,height=270)


                              # Search Frame
                              search_frame=LabelFrame(Down_frame,bd=2,relief=RIDGE,bg='white',text='Search Staff Information',font=('times new romam',11,'bold'),fg='Dark blue')
                              search_frame.place(x=0,y=0,width=1470,height=270)

                              search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="dark blue",bg="red")
                              search_by.grid(row=0,column=0,sticky="w",padx=5)

                              # search
                              combo_search=ttk.Combobox(search_frame,font=("arial",11,"bold"),state="readonly")
                              combo_search["values"]=("select option","Department","Name")
                              combo_search.current(0)
                              combo_search.grid(row=0,column=1,padx=5,sticky="w")

                              txt_search=Entry(search_frame,width=22,font=("arial",11,"bold"),bd=1,relief=GROOVE) 
                              txt_search.grid(row=0,column=1,padx=5,sticky="W")

                              searchbtn=Button(search_frame,text="Search",width=14).grid(row=0,column=3,padx=5,)
                              showallbtn=Button(search_frame,text="Show All",width=14).grid(row=0,column=4,padx=5)

                              #==================Employee table================
                              # Table Frame
                              table_frame=Frame(Down_frame,bd=3,relief=RIDGE)
                              table_frame.place(x=0,y=60,width=1470,height=170)

                              scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                              scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                              self.staff_table=ttk.Treeview(table_frame,column=("dep","name","email","Addrees","Dob","Doj","Idproof","gender","Mobile","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
                              
                              scroll_x.pack(side=BOTTOM,fill=X)
                              scroll_Y.pack(side=RIGHT,fill=Y)

                              scroll_x.config(command=self.staff_table.xview)
                              scroll_Y.config(command=self.staff_table.yview)


                              self.staff_table.heading("dep",text="Department")
                              self.staff_table.heading("name",text="Name")
                              self.staff_table.heading("email",text="Email")
                              self.staff_table.heading("salary",text="salary")
                              self.staff_table.heading("country",text="Country")

                              self.staff_table["show"]='headings'

                              self.staff_table.column("dep",width=100)
                              self.staff_table.column("name",width=100)
                              self.staff_table.column("email",width=100)
                              self.staff_table.column("salary",width=100)
                              self.staff_table.column("country",width=100)
                             
                              
                              self.staff_table.pack(fill=BOTH,expand=1)


                                                            

root=Tk() 
obj=Employee(root)
root.mainloop()