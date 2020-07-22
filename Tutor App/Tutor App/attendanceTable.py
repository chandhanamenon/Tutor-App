from tkinter import ttk
import tkinter
import TutorAppDB
from tkinter import messagebox
import os
from functools import partial
import addComment


global combo

class attendanceTable(tkinter.Canvas):
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

        label = tkinter.Label(self.frame, text="Manage Attendance",background="white",font=headingFont)        
        label.grid(row=3,column=0,columnspan=4,pady=(10,20))        

        label = tkinter.Label(self.frame, text='                    Student ID                 ',font=labelFont)
        label.grid(row=4,column=0,padx=(15,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='                                                       Student Name                                                     ',font=labelFont)
        label.grid(row=4,column=1,padx=(1,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='                  Update Status                     ',font=labelFont)
        label.grid(row=4,column=2,padx=(1,1),pady=(0,10),columnspan=2)  
        
        db = TutorAppDB.TutorAppDB()
        attendance_data = db.get_all_students_for_batch_attendance()
 
        filepath = os.path.join(os.path.dirname(__file__),"images/edit.gif")
        edit_image = tkinter.PhotoImage(file=filepath)
        self.action_images.append(edit_image)
        
        filepath = os.path.join(os.path.dirname(__file__),"images/delete.gif")
        delete_image = tkinter.PhotoImage(file=filepath)
        self.action_images.append(delete_image)

                
        
        
        

        # populate the frame
        for i in range(len(attendance_data)):
            attendance = attendance_data[i]
            
            for j in range(len(attendance)-1):
                             
                label_text = (attendance[j])                        
                label = tkinter.Label(self.frame, text=label_text,background="white")
                if j==0:
                    label.grid(row=i+5,column=j,padx=(15,5),pady=(0,5))
                else:
                    label.grid(row=i+5,column=j,padx=(5,5),pady=(0,5))

            button = tkinter.Button(self.frame,
                                    image=edit_image,
                                    relief="flat",
                                    background="white",
                                    command= partial(self.comment,attendance[len(attendance)-1],i))
            button.grid(row=i+5,column=len(attendance)-1,sticky="e",padx=(0,15))


            

    def comment(self,student_id,row):

        addWin = addComment.addComment(self.root,self.root,student_id)
        

        # refesh the view
        self.root.manage_attendance()

        
        
