import tkinter
import TutorAppDB
from tkinter import messagebox
import os
from functools import partial
import PayNow


class FeeTable(tkinter.Canvas):
    # The Constructor
    def __init__(self,root):

        super().__init__(root)
        self.root = root

        self.config(background="white")
        self.config(scrollregion=(0,0,978,1900))

        self.frame = tkinter.Frame(self,background="white")
        self.frame.place(x=0,y=0,width=978,height=900)
        self.create_window(0, 0, window=self.frame, anchor="nw")    

        self.action_images = []
        self.create_ui()

    def create_ui(self):
        headingFont = ("Arial", "14", "bold");
        labelFont = ("Arial", "10", "bold");

        db = TutorAppDB.TutorAppDB()
        fee_data = db.get_fee_det()
        print(fee_data)
                
        label = tkinter.Label(self.frame, text="Manage Fee",background="white",font=headingFont)        
        label.grid(row=0,column=0,columnspan=5,pady=(10,20))

        label = tkinter.Label(self.frame, text='                  Student ID                   ',font=labelFont)
        label.grid(row=1,column=0,padx=(15,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='                Student Name                ',font=labelFont)
        label.grid(row=1,column=1,padx=(1,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='              Batch Name              ',font=labelFont)
        label.grid(row=1,column=2,padx=(1,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='             Amount              ',font=labelFont)
        label.grid(row=1,column=3,padx=(1,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='                 Actions          ',font=labelFont)
        label.grid(row=1,column=4,padx=(1,1),pady=(0,10),columnspan=2)   
        
        filepath = os.path.join(os.path.dirname(__file__),"images/edit.gif")
        edit_image = tkinter.PhotoImage(file=filepath)
        self.action_images.append(edit_image)
        
        filepath = os.path.join(os.path.dirname(__file__),"images/delete.gif")
        delete_image = tkinter.PhotoImage(file=filepath)
        self.action_images.append(delete_image)

      # populate the frame
        for i in range(len(fee_data)):
            fee = fee_data[i]
            for j in range(len(fee)-1):
                                        
                label = tkinter.Label(self.frame, text= fee[j],background="white")
                if j==0:
                    label.grid(row=i+2,column=j,padx=(15,5),pady=(0,5))
                else:                                        
                    label.grid(row=i+2,column=j,padx=(5,5),pady=(0,5))
                
            
            button = tkinter.Button(self.frame, text="Pay Now",
            relief="raised",background="blue",fg="white",
            command= partial(self.payNow,fee[len(fee)-1],i))
            button.grid(row=i+2,column=len(fee)-1,sticky="e",padx=(5,15))
            print(fee[len(fee)-1],i)



    def payNow(self,student_id,row):
        print("edit_student",student_id,row)

        # Open the batch dialog in edit mode
        addWin = PayNow.PayNow(self.root,self.root,student_id)        
         


        # refesh the view
        self.root.manage_fees()   
        
