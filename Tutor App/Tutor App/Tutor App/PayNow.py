import tkinter
import TutorAppDB

class PayNow(tkinter.Frame):

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

        windowTitle="Tutor App - Payment"
        self.dialog.title(windowTitle)


        self.create_ui()


    def create_ui(self):

        buttonLabel = "Pay"
        helpLabel = "Fee Payment"
            
        labelFont = ("Arial", "10", "bold");
        heading = tkinter.Label(self,text=helpLabel,font=labelFont,anchor="w")
        heading.place(x=15,y=15,width=400,height=25)

        self.messageLabel = tkinter.Label(self,text="Please enter the date:",anchor="w",fg="blue")
        self.messageLabel.place(x=40,y=50,width=400,height=25)

        label = tkinter.Label(self,text="Student Name :",anchor="w",font=labelFont)
        label.place(x=40,y=90)
        self.studentNameVar = tkinter.StringVar()
        self.studentName = tkinter.Label(self,textvariable=self.studentNameVar,fg="blue")
        self.studentName.place(x=145,y=90)

        label = tkinter.Label(self,text="Batch :",anchor="w",font=labelFont)
        label.place(x=40,y=140,width=100,height=25)
        self.studentMobVar = tkinter.StringVar()
        self.studentMob = tkinter.Label(self,textvariable=self.studentMobVar,fg="blue")
        self.studentMob.place(x=145,y=140)

        label = tkinter.Label(self,text="Amount :",anchor="w",font=labelFont)
        label.place(x=40,y=190,width=100,height=25)
        self.studentParenVar = tkinter.StringVar()
        self.studentParen = tkinter.Label(self,textvariable=self.studentParenVar,fg="blue")
        self.studentParen.place(x=145,y=191)

        label = tkinter.Label(self,text="Date : ",anchor="w",font=labelFont)
        label.place(x=40,y=240,width=100,height=25)
        self.studentdojVar = tkinter.StringVar()
        self.studentdoj = tkinter.Entry(self,textvariable=self.studentdojVar)
        self.studentdoj.place(x=155,y=240,width=205,height=25)

        addButton = tkinter.Button(self,text=buttonLabel,font=labelFont,command=self.handleAdd)
        addButton.place(x=150,y=290,width=100,height=30)

        cancelButton = tkinter.Button(self,text="Cancel",font=labelFont,command=self.handleCancel)
        cancelButton.place(x=260,y=290,width=100,height=30)

        self.studentIdVar = tkinter.StringVar()
        self.batchIdVar = tkinter.StringVar()
        
        

        if(self.student_id != None):
            db = TutorAppDB.TutorAppDB()
            student_data = db.get_fee_det_pay(self.student_id)            
            self.studentNameVar.set(student_data[0][0])
            self.studentMobVar.set(student_data[0][1])
            self.studentParenVar.set(student_data[0][2])
            self.batchIdVar.set(student_data[0][3])
            self.studentIdVar.set(student_data[0][4])
            
            
        
    def handleAdd(self):

        date_joined = self.studentdoj.get()
        batch_id = self.batchIdVar.get()
        student_id = self.studentIdVar.get()
        amount = self.studentParenVar.get()
  
        

               
        if(len(date_joined) == 0):    
               
                tkinter.messagebox.showerror(message="Please enter the Date")
                
        else:
                # Save the data to the database
                db = TutorAppDB.TutorAppDB()
                db.save_receipt(date_joined,amount,student_id ,batch_id)
                tkinter.messagebox.showinfo(message="Payment Successful !")
                                

        self.parent.manage_fees()
        




    def handleCancel(self):
        self.dialog.destroy()


        #Do not runn this code if imported in another file 
        if __name__ == "__main__":
            root = tkinter.Tk()
            app = PayNow(root)
            app.mainloop()
            
