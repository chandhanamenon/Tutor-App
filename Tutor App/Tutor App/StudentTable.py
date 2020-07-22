import tkinter
import TutorAppDB
from tkinter import messagebox
import os
from functools import partial
import AddStudentWindow

class StudentTable(tkinter.Canvas):
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
        student_data = db.get_active_student()
                
        label = tkinter.Label(self.frame, text="Manage Students",background="white",font=headingFont)        
        label.grid(row=0,column=0,columnspan=5,pady=(10,20))

        label = tkinter.Label(self.frame, text='              Student Name               ',font=labelFont)
        label.grid(row=1,column=0,padx=(15,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='            Mobile Number            ',font=labelFont)
        label.grid(row=1,column=1,padx=(1,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='          Parent Name          ',font=labelFont)
        label.grid(row=1,column=2,padx=(1,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='         Date of Joining            ',font=labelFont)
        label.grid(row=1,column=3,padx=(1,1),pady=(0,10))
        label = tkinter.Label(self.frame, text='               Actions               ',font=labelFont)
        label.grid(row=1,column=4,padx=(1,1),pady=(0,10),columnspan=2)   
##
##        label = tkinter.Label(self.frame, text='              Student Name              ',font=labelFont)
##        label.grid(row=1,column=0,padx=(15,1),pady=(0,10))
##        label = tkinter.Label(self.frame, text='               Mobile                   ',font=labelFont)
##        label.grid(row=1,column=1,padx=(1,1),pady=(0,10))
##        label = tkinter.Label(self.frame, text='        Parent Name         ',font=labelFont)
##        label.grid(row=1,column=2,padx=(1,1),pady=(0,10))
##        label = tkinter.Label(self.frame, text='          Date of Joining          ',font=labelFont)
##        label.grid(row=1,column=3,padx=(1,1),pady=(0,10))
##        label = tkinter.Label(self.frame, text='               Action              ',font=labelFont)
##        label.grid(row=1,column=4,padx=(1,1),pady=(0,10)) 
##        
        
        filepath = os.path.join(os.path.dirname(__file__),"images/edit.gif")
        edit_image = tkinter.PhotoImage(file=filepath)
        self.action_images.append(edit_image)
        
        filepath = os.path.join(os.path.dirname(__file__),"images/delete.gif")
        delete_image = tkinter.PhotoImage(file=filepath)
        self.action_images.append(delete_image)

      # populate the frame
        for i in range(len(student_data)):
            student = student_data[i]
            for j in range(len(student)-1):
                                        
                label = tkinter.Label(self.frame, text= student[j],background="white")
                if j==0:
                    label.grid(row=i+2,column=j,padx=(15,5),pady=(0,5))
                else:                                        
                    label.grid(row=i+2,column=j,padx=(5,5),pady=(0,5))
                
            
            button = tkinter.Button(self.frame, image=edit_image, relief="flat",background="white",
                                            command= partial(self.edit_student,student[len(student)-1],i))
            button.grid(row=i+2,column=len(student)-1,sticky="e",padx=(0,15))
            print(len(student)-1)

            button = tkinter.Button(self.frame, image=delete_image, relief="flat",background="white",
                                            command= partial(self.delete_student,student[len(student)-1],i))
            button.grid(row=i+2,column=len(student),sticky="w")
        
    def edit_student(self,student_id,row):
        print("edit_student",student_id,row)
       

        # Open the batch dialog in edit mode
        print("Opening edit batch")
        addWin = AddStudentWindow.AddStudentWindow(self.root,self.root,student_id)        
         

    def delete_student(self,student_id,row):
        print("delete_student",student_id,row)
        
        # Get an user confirmation for the delete
        response = tkinter.messagebox.askquestion(message="Do you really want to delete the Student?")
        if response == "yes":
            # If the user confirms delete exeute the query
            db = TutorAppDB.TutorAppDB()
            db.deactivate_student(student_id)

            # refesh the view
            self.root.manage_students()   
        
