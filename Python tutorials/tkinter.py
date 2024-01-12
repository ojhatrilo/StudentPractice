from tkinter import *
from tkinter.ttk import * 
root=Tk()
style=Style()
style.configure('test.TButton',font=('calibri',10,'bold'),foreground='red')
btn1=Button(root,text='quit',style='test.TButton',command=root.destroy)
btn1.grid(row=0,column=3,padx=100)
btn2=Button(root,text='click me',style='test.TButton',command=root.destroy)
btn2.grid(row=1,column=1,padx=200,pady='20')
root.mainloop()


