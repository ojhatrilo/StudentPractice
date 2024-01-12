from tkinter import*
root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('D:/STAFF/OJHA/Python tutorials/billing system/icon.ico')
# heading
toplabel=Label(root,text='Retail Billing shop',fg='gold',bg='gray20',font=('times new roman',30,'bold'),relief='groove',bd='12')
toplabel.pack(fill='x')
# Coustomer_details_labelframe
Coustomer_Details_label=LabelFrame(root,text='Coustomer Details',font=('times new roman',15,'bold'),fg='gold',bg='gray20',relief='groove',bd='10')
Coustomer_Details_label.pack(fill='x')
# name label in the  Coustomer_details_labelframe 
Namelabel=Label(Coustomer_Details_label,text='Name',font=('arial',15,'bold'),fg='white',bg='gray20',bd='10')
Namelabel.grid(row='0',column='0')
# name entry in the  Coustomer_details_labelframe
NameEntry=Entry(Coustomer_Details_label,bd='9',font=('arial',10))
NameEntry.grid(row='0',column='1',padx='10')
# phone no label in Coustomer_details_labelframe
phonelabel=Label(Coustomer_Details_label,text='Phone no',font=('arial',15,'bold'),fg='white',bg='gray20',bd='10')
phonelabel.grid(row='0',column='2')
# phone no entery in Coustomer_details_labelframe
phoneEntry=Entry(Coustomer_Details_label,bd='9',font=('arial',10))
phoneEntry.grid(row='0',column='3',padx='10')
# bill no label in Coustomer_details_labelframe
bill_no_label=Label(Coustomer_Details_label,text='Bill no',font=('arial',15,'bold'),fg='white',bg='gray20',bd='10')
bill_no_label.grid(row='0',column='4')
# bill no entery in Coustomer_details_labelframe
bill_no_Entry=Entry(Coustomer_Details_label,bd='9',font=('arial',10))
bill_no_Entry.grid(row='0',column='5',padx='10')
# Seach button in Coustomer_details_labelframe
Searchbt1=Button(Coustomer_Details_label,text='SEARCH',font=('arial',15,'bold'),bd='10')
Searchbt1.grid(row='0',column='6',padx='20',pady='5')
# product frame
product_frame=Frame(root)
product_frame.pack()
# cosmetic Frame 
cosmetic_frame=LabelFrame(product_frame,text='Cosmetics',fg='gold',bg='gray20',font=('times new roman',15,'bold'),relief='groove',bd='12')
cosmetic_frame.grid(row='0',column='0')
# bathsoap in cosmetic Frame
bathsoap=Label(cosmetic_frame,text='Bath Soap',font=('arial',15,'bold'),fg='white',bg='gray20',bd='10')
bathsoap.grid(row='0',column='1')
# bathsoap Entry in cosmetic frame
bath_soap_Entry=Entry(cosmetic_frame,bd='9',font=('arial',10))
bath_soap_Entry.grid(row='0',column='2')
# conditioner in cosmetic frame
conditioner_label=Label(cosmetic_frame,text='Conditioner',font=('arial',15,'bold'),fg='white',bg='gray20',bd='10')
conditioner_label.grid(row='1',column='1')
# coditioner Entry in cosmetic frame
conditioner_Entry=Entry(cosmetic_frame,bd='9',font=('arial',10))
conditioner_Entry.grid(row='1',column='2')
# oil label in cosmetic frame
oil_label=Label(cosmetic_frame,text='Conditioner',font=('arial',15,'bold'),fg='white',bg='gray20',bd='10')
oil_label.grid(row='2',column='1')
# oil entry in cosmetic frame
oil_Entry=Entry(cosmetic_frame,bd='9',font=('arial',10))
oil_Entry.grid(row='2',column='2')

root.mainloop()
