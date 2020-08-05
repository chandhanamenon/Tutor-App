import tkinter
import TutorAppDB

class AddStudentWindow(tkinter.Frame):

    #The constructor
    def __init__(self,root,parent,student_id=None):
        self.root = root
        self.parent = parent
        self.student_id = student_id

        self.dialog = tkinter.Toplevel(root)
        super().__init__(self.dialog)

        self.dialog.protocol("WM_DELETE_WINDOW",self.handleCancel)

        diaHeight = 350

        self.place(width=600,height=diaHeight);

        xloc = (self.root.winfo_screenwidth()-500)//2
        yloc = (self.root.winfo_screenheight()-diaHeight)//2
        self.dialog.geometry("500x" + str(diaHeight) + "+" + str(xloc) + "+" +str(yloc))
        self.dialog.resizable(0,0)

        windowTitle="Tutor App - Add Student Window"
        self.dialog.title(windowTitle)


        self.create_ui()


    def create_ui(self):

        buttonLabel = "Add Student"
        helpLabel = "Add New Student"

        if(self.student_id != None):
            buttonLabel = "Update "
            helpLabel = "Update Student"
            
        labelFont = ("Arial", "10", "bold");
        heading = tkinter.Label(self,text=helpLabel,font=labelFont,anchor="w")
        heading.place(x=15,y=15,width=400,height=25)

        self.messageLabel = tkinter.Label(self,text="Please enter the student details",anchor="w",fg="blue")
        self.messageLabel.place(x=40,y=50,width=400,height=25)

        label = tkinter.Label(self,text="Student Name*",anchor="w",font=labelFont)
        label.place(x=40,y=90,width=100,height=25)
        self.studentNameVar = tkinter.StringVar()
        self.studentName = tkinter.Entry(self,textvariable=self.studentNameVar)
        self.studentName.place(x=150,y=90,width=205,height=25)

        label = tkinter.Label(self,text="Mobile*",anchor="w",font=labelFont)
        label.place(x=40,y=140,width=100,height=25)
        self.studentMobVar = tkinter.StringVar()
        self.studentMob = tkinter.Entry(self,textvariable=self.studentMobVar)
        self.studentMob.place(x=150,y=140,width=205,height=25)

        label = tkinter.Label(self,text="Parent Name*",anchor="w",font=labelFont)
        label.place(x=40,y=190,width=100,height=25)
        self.studentParenVar = tkinter.StringVar()
        self.studentParen = tkinter.Entry(self,textvariable=self.studentParenVar)
        self.studentParen.place(x=150,y=190,width=205,height=25)

        label = tkinter.Label(self,text="Date Of Joining* ",anchor="w",font=labelFont)
        label.place(x=40,y=240,width=100,height=25)
        self.studentdojVar = tkinter.StringVar()
        self.studentdoj = tkinter.Entry(self,textvariable=self.studentdojVar)
        self.studentdoj.place(x=150,y=240,width=205,height=25)
            
        addButton = tkinter.Button(self,text=buttonLabel,font=labelFont,command=self.handleAdd)
        addButton.place(x=150,y=290,width=100,height=30)

        cancelButton = tkinter.Button(self,text="Cancel",font=labelFont,command=self.handleCancel)
        cancelButton.place(x=260,y=290,width=100,height=30)

        if(self.student_id != None):
            db = TutorAppDB.TutorAppDB()
            student_data = db.get_student_for_ids(self.student_id)            
            self.studentNameVar.set(student_data[0][0])
            self.studentMobVar.set(student_data[0][1])
            self.studentParenVar.set(student_data[0][2])
            self.studentdojVar.set(student_data[0][3])
            
        
    def handleAdd(self):
        student_name = self.studentName.get()
        mobile = self.studentMob.get()
        parent_name = self.studentParen.get()
        date_joined = self.studentdoj.get()

        if len(student_name) == 0 or student_name.isspace():
            tkinter.messagebox.showerror(message="Please specify a student name")
        else:

            if len(mobile) == 0 or mobile.isspace():
                studentMob="Please enter the Mobile Number."

            db = TutorAppDB.TutorAppDB()
               
            if(self.student_id == None):    
                # Save the data to the database                
                db.save_student(student_name, mobile, parent_name, date_joined)
                self.dialog.destroy()
            else:
                # Update the data to the database
                db.update_student(student_name, mobile, parent_name, date_joined, self.student_id)
                self.dialog.destroy()                

            self.parent.manage_students()
        




    def handleCancel(self):
        self.dialog.destroy()


        #Do not runn this code if imported in another file 
        if __name__ == "__main__":
            root = tkinter.Tk()
            app = AddStudentWindow(root)
            app.mainloop()
            
